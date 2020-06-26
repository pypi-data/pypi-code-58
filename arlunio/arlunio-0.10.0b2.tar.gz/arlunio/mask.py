import functools
from typing import Union

import numpy as np

import arlunio as ar


class Mask(np.ndarray):
    """A mask is just a boolean numpy array.

    They are typically used to represent 'selections' for various operations such as
    when coloring a region of an image.
    """

    def __new__(cls, arr):
        return np.asarray(arr).view(cls)

    def __mul__(self, other):

        try:
            return np.logical_and(self, other)
        except ValueError:

            mask = self.copy()
            size = np.prod(other.shape)

            if mask[mask].shape == size:
                mask[mask] = other.reshape(size)
                return mask

            raise

    def __neg__(self):
        return np.logical_not(self)

    def __sub__(self, other):
        return np.logical_and(self, np.logical_not(other))

    def __rsub__(self, other):
        return np.logical_and(other, np.logical_not(self))

    @classmethod
    def empty(cls, *shape):
        """Return an empty mask with the given shape.

        Example
        -------
        >>> from arlunio.mask import Mask
        >>> Mask.empty(3, 4)
        Mask([[False, False, False, False],
              [False, False, False, False],
              [False, False, False, False]])
        """

        if len(shape) == 1 and isinstance(shape[0], tuple):
            return cls(np.full(shape[0], False))

        return cls(np.full(shape, False))

    @classmethod
    def full(cls, *shape):
        """Return a full mask with the given shape.

        Example
        -------
        >>> from arlunio.mask import Mask
        >>> Mask.full(3, 4)
        Mask([[ True,  True,  True,  True],
              [ True,  True,  True,  True],
              [ True,  True,  True,  True]])
        """

        if len(shape) == 1 and isinstance(shape[0], tuple):
            return cls(np.full(shape[0], True))

        return cls(np.full(shape, True))


@ar.definition
def Empty(width: int, height: int) -> Mask:
    """An empty mask.

    Example
    -------
    >>> from arlunio.mask import Empty
    >>> empty = Empty()
    >>> empty(width=4, height=3)
    Mask([[False, False, False, False],
          [False, False, False, False],
          [False, False, False, False]])
    """
    return Mask.empty(height, width)


@ar.definition
def Full(width: int, height: int) -> Mask:
    """An full mask.

    Example
    -------
    >>> from arlunio.mask import Full
    >>> full = Full()
    >>> full(width=4, height=3)
    Mask([[ True,  True,  True,  True],
          [ True,  True,  True,  True],
          [ True,  True,  True,  True]])
    """
    return Mask.full(height, width)


@ar.definition(operation=ar.Defn.OP_ADD)
def MaskAdd(
    width: int, height: int, *, a: ar.Defn[Mask] = None, b: ar.Defn[Mask] = None
) -> Mask:
    """Add any two mask producing definitions together.

    The resulting defintion will return a mask that is :code:`True` if a given point
    is :code:`True` in either :code:`a` or :code:`b`.

    Attributes
    ----------
    a:
        The first mask
    b:
        The second mask
    """

    return a(width=width, height=height) + b(width=width, height=height)


@ar.definition(operation=ar.Defn.OP_SUB)
def MaskSub(
    width: int, height: int, *, a: ar.Defn[Mask] = None, b: ar.Defn[Mask] = None
) -> Mask:
    """Subtract one mask away from another mask.

    The resulting definition will return a mask that is :code:`True` only if a given
    point is in :code:`a` **and not** in :code:`b`.

    .. note::

       You will get very different results depending on which way around you set
       :code:`a` and :code:`b`!

    Attributes
    ----------
    a:
        The first "base" mask
    b:
        The second mask that defines the region to remove from :code:`a`
    """
    return a(width=width, height=height) - b(width=width, height=height)


@ar.definition(operation=ar.Defn.OP_MUL)
def MaskMul(
    width: int, height: int, *, a: ar.Defn[Mask] = None, b: ar.Defn[Mask] = None
) -> Mask:
    """Muliply any two mask producing definitions together.

    The resulting definition will return a mask that is :code:`True` only if a given
    point is in both :code:`a` and :code:`b`.

    Attributes
    ----------
    a:
        The first mask
    b:
        The second mask
    """
    return a(width=width, height=height) * b(width=width, height=height)


def any_(*args: Union[bool, np.ndarray]) -> Mask:
    """Given a number of conditions, return :code:`True` if any of the conditions
    are true.

    This function is implemented as a thin wrapper around numpy's
    :code:`np.logical_or` function so that it can take an arbitrary number of inputs.
    This also means that this function will accept arrays of differing sizes - assuming
    that they can be broadcasted to a common shape.

    Parameters
    ----------
    args:
      A number of boolean conditions, a condition can either be a single boolean value
      or a numpy array of boolean values.

    Examples
    --------

    >>> from arlunio.mask import any_
    >>> any_(True, False, False)
    Mask(True)
    >>> any_(False, False, False, False)
    Mask(False)

    If the arguments are boolean numpy arrays, then the any condition is applied
    element-wise

    >>> import numpy as np
    >>> x1 = np.array([True, False, True])
    >>> x2 = np.array([False, False, True])
    >>> x3 = np.array([False, True, False])
    >>> any_(x1, x2, x3)
    Mask([ True,  True,  True])

    This function can even handle a mixture of arrays and single values - assuming
    their shapes can be broadcasted to a common shape.

    >>> any_(False, np.array([True, False]), np.array([[False, True], [True, False]]))
    Mask([[ True,  True],
          [ True, False]])


    See Also
    --------

    |numpy.Broadcasting|
       Numpy documentation on broadcasting.

    |numpy.Array Broadcasting|
       Further background on broadcasting.

    |numpy.logical_or|
       Reference documentation on the :code:`np.logical_or` function
    """
    return Mask(functools.reduce(np.logical_or, args))


def all_(*args: Union[bool, np.ndarray]) -> Mask:
    """Given a number of conditions, return :code:`True` only if **all**
    of the given conditions are true.

    This function is implemented as a thin wrapper around numpy's
    :code:`np.logical_and` function so that it can take an arbitrary number of inputs.
    This also means that this function will accept arrays of differing sizes - assuming
    that they can be broadcasted to a common shape.

    Parameters
    ----------
    args:
      A number of boolean conditions, a conditon can either be a single boolean value,
      or a numpy array of boolean values.

    Examples
    --------

    >>> from arlunio.mask import all_
    >>> all_(True, True, True)
    Mask(True)
    >>> all_(True, False, True, True)
    Mask(False)

    If the arguments are boolean numpy arrays, then the any condition is applied
    element-wise

    >>> import numpy as np
    >>> x1 = np.array([True, False, True])
    >>> x2 = np.array([False, False, True])
    >>> x3 = np.array([False, True, True])
    >>> all_(x1, x2, x3)
    Mask([False, False,  True])

    This function can even handle a mixture of arrays and single values - assuming
    their shapes can be broadcasted to a common shape.

    >>> all_(True, np.array([True, False]), np.array([[False, True], [True, False]]))
    Mask([[False, False],
          [ True, False]])


    See Also
    --------

    |numpy.Broadcasting|
       Numpy documentation on broadcasting.

    |numpy.Array Broadcasting|
       Further background on broadcasting.

    |numpy.logical_and|
       Reference documentation on the :code:`logical_and` function.
    """
    return Mask(functools.reduce(np.logical_and, args))
