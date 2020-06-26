from __future__ import absolute_import, division, print_function

import os
import warnings
import numpy as np
from multiprocessing import cpu_count

from astropy.io import fits
from astropy.wcs import WCS
from astropy import units as u
from astropy.nddata import StdDevUncertainty
from astropy.utils.console import ProgressBar

from .nikamap import retrieve_primary_keys, NikaMap
from .utils import update_header

__all__ = ["Jackknife", "Bootstrap"]


def compare_header(header_ref, header_target):
    """Crude comparison of two header

    Parameters
    ----------
    header_ref : astropy.io.fits.Header
        the reference header
    header_target : astropy.io.fits.Header
        the target header to check

    Notes
    -----
    This will raise assertion error if the two header are not equivalent
    """
    wcs_ref = WCS(header_ref)
    wcs_target = WCS(header_target)

    assert wcs_ref.wcs == wcs_target.wcs, "Different header found"
    for key in ["UNIT", "NAXIS1", "NAXIS2"]:
        if key in header_ref:
            assert header_ref[key] == header_target[key], "Different key found"


class MultiScans(object):
    """A class to hold multi single scans from a list of fits files.

    This acts as a python lazy iterator and/or a callable

    Parameters
    ----------
    filenames : list or `~MultiScans` object
        the list of fits files to produce the Jackknifes or an already filled object
    ipython_widget : bool, optional
        If True, the progress bar will display as an IPython notebook widget.

    Notes
    -----
    A crude check is made on the wcs of each map when instanciated
    """

    def __init__(self, filenames, ipython_widget=False, **kwd):

        self.i = 0
        self.n = None
        self.kwargs = kwd
        self.ipython_widget = ipython_widget

        if isinstance(filenames, MultiScans):
            data = filenames

            self.filenames = data.filenames
            self.primary_header = data.primary_header
            self.header = data.header
            self.unit = data.unit
            self.shape = data.shape
            self.datas = data.datas
            self.weights = data.weights
            self.time = data.time
            self.mask = data.mask
        else:

            # Chek for existence
            checked_filenames = []
            for filename in filenames:
                if os.path.isfile(filename):
                    checked_filenames.append(filename)
                else:
                    warnings.warn("{} does not exist, removing from list".format(filename), UserWarning)

            self.filenames = checked_filenames

            nm = NikaMap.read(self.filenames[0], **kwd)

            self.primary_header = nm.meta.get("primary_header", None)
            self.header = nm.meta["header"]
            self.unit = nm.unit
            self.shape = nm.shape

            # This is a low_mem=False case ...
            # TODO: How to refactor that for low_mem=True ?
            datas = np.zeros((len(self.filenames),) + self.shape)
            weights = np.zeros((len(self.filenames),) + self.shape)
            time = np.zeros(self.shape) * u.h

            for i, filename in enumerate(ProgressBar(self.filenames, ipython_widget=self.ipython_widget)):

                nm = NikaMap.read(filename, **kwd)
                try:
                    compare_header(self.header, nm.meta["header"])
                except AssertionError as e:
                    raise ValueError("{} for {}".format(e, filename))

                datas[i, :, :] = nm.data
                with np.errstate(invalid="ignore", divide="ignore"):
                    weights[i, :, :] = nm.uncertainty.array ** -2
                time += nm.time

                # make sure that we do not have nans in the data
                datas[i, nm.time == 0] = 0
                weights[i, nm.time == 0] = 0

            unobserved = time == 0

            self.datas = datas
            self.weights = weights
            self.time = time
            self.mask = unobserved

    def __len__(self):
        # to retrieve the legnth of the iterator, enable ProgressBar on it
        return self.n

    def __iter__(self):
        # Iterators are iterables too.
        # Adding this functions to make them so.
        return self

    def __call__(self):
        """The main method which should be overrided

        should return a  :class:`nikamap.NikaMap`
        """
        pass

    def __next__(self):
        """Iterator on the objects"""
        if self.n is None or self.i < self.n:
            # Produce data until last iter
            self.i += 1
            data = self.__call__()
        else:
            raise StopIteration()

        return data


class Jackknife(MultiScans):
    """A class to create weighted Jackknife maps from a list of IDL fits files.

    This acts as a python lazy iterator and/or a callable

    Parameters
    ----------
    filenames : list
        the list of fits files to produce the Jackknifes
    ipython_widget : bool, optional
        If True, the progress bar will display as an IPython notebook widget.
    n : int
        the number of Jackknifes maps to be produced in the iterator

            if set to `None`, produce only one weighted average of the maps

    parity_threshold : float
        mask threshold between 0 and 1 to keep partially jackknifed area
        * 1 pure jackknifed
        * 0 partially jackknifed, keep all


    Notes
    -----
    A crude check is made on the wcs of each map when instanciated
    """

    def __init__(self, filenames, n=1, parity_threshold=1, **kwd):
        super(Jackknife, self).__init__(filenames, **kwd)
        self.n = n
        self.parity_threshold = parity_threshold

        if n is not None and len(self.filenames) % 2:
            warnings.warn("Even number of files, dropping the last one", UserWarning)
            self.filenames = self.filenames[:-1]

        assert len(self.filenames) > 1, "Less than 2 existing files in filenames"

        # Base jackknife weights
        jk_weights = np.ones(len(self.filenames))

        if n is not None:
            jk_weights[::2] *= -1

        self.jk_weights = jk_weights

    @property
    def parity_threshold(self):
        return self._parity

    @parity_threshold.setter
    def parity_threshold(self, value):
        if value is not None and isinstance(value, (int, float)) and 0 <= value <= 1:
            self._parity = value
        else:
            raise TypeError("parity must be between 0 and 1")

    def __call__(self):
        """Compute a jackknifed dataset

        Returns
        -------
        :class:`nikamap.NikaMap`
            a jackknifed data set
        """
        np.random.shuffle(self.jk_weights)

        with np.errstate(invalid="ignore", divide="ignore"):
            e_data = 1 / np.sqrt(np.sum(self.weights, axis=0))
            data = np.sum(self.datas * self.weights * self.jk_weights[:, np.newaxis, np.newaxis], axis=0) * e_data ** 2
            parity = np.mean((self.weights != 0) * self.jk_weights[:, np.newaxis, np.newaxis], axis=0)
            weighted_parity = np.sum(self.weights * self.jk_weights[:, np.newaxis, np.newaxis], axis=0) * e_data ** 2

        if self.n is not None:
            mask = (1 - np.abs(parity)) < self.parity_threshold
        else:
            mask = parity < self.parity_threshold

        mask = mask | self.mask

        data[mask] = np.nan
        e_data[mask] = np.nan

        # TBC: time will have a different mask here....
        data = NikaMap(
            data,
            mask=mask,
            uncertainty=StdDevUncertainty(e_data),
            unit=self.unit,
            wcs=WCS(self.header),
            meta={"header": self.header, "primary_header": self.primary_header},
            time=self.time,
        )

        return data  # , weighted_parity


class Bootstrap(MultiScans):
    """A class to create bootstraped maps from a list of IDL fits files.

    This acts as a python lazy iterator and/or a callable

    Parameters
    ----------
    filenames : list
        the list of fits files to produce the Jackknifes
    ipython_widget : bool, optional
        If True, the progress bar will display as an IPython notebook widget.
    n : int
        the number of bootstrap maps to be produced in the iterator
    n_bootstrap : int
        the number of realization to produce a bootsrapped map, by default twice the length of the input filename list

    Notes
    -----
    A crude check is made on the wcs of each map when instanciated
    """

    def __init__(self, filenames, n=1, n_bootstrap=None, **kwd):
        super(Bootstrap, self).__init__(filenames, **kwd)
        self.n = n

        if n_bootstrap is None:
            n_bootstrap = 2 * len(self.filenames)

        self.n_bootstrap = n_bootstrap

    def shuffled_average(self, *args):
        """Actually do one shuffled average."""
        if len(args) > 0:
            n_shuffle = len(args[0])
        else:
            n_shuffle = 1
        n_scans = self.datas.shape[0]
        outputs = []
        for i_shuffle in range(n_shuffle):
            shuffled_index = np.floor(np.random.uniform(0, n_scans, n_scans)).astype(np.int)
            # np.ma.average is needed as some of the pixels have zero weights (should be masked)
            outputs.append(
                np.ma.average(self.datas[shuffled_index], weights=self.weights[shuffled_index], axis=0, returned=False)
            )
        return outputs

    def __call__(self):
        """Compute a bootstraped map

        Returns
        -------
        :class:`nikamap.NikaMap`
            a bootstraped data set
        """

        bs_array = np.concatenate(
            ProgressBar.map(
                self.shuffled_average,
                np.array_split(np.arange(self.n_bootstrap), cpu_count()),
                ipython_widget=self.ipython_widget,
                multiprocess=True,
            )
        )

        data = np.mean(bs_array, axis=0)
        e_data = np.std(bs_array, axis=0, ddof=1)

        # Mask unobserved regions
        unobserved = self.time == 0
        data[unobserved] = np.nan
        e_data[unobserved] = np.nan

        data = NikaMap(
            data,
            mask=unobserved,
            uncertainty=StdDevUncertainty(e_data),
            unit=self.unit,
            wcs=WCS(self.header),
            meta={"header": self.header, "primary_header": self.primary_header},
            time=self.time,
        )

        return data
