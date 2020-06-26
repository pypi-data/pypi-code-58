# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['numpoly',
 'numpoly.array_function',
 'numpoly.construct',
 'numpoly.poly_function',
 'numpoly.poly_function.divide',
 'numpoly.utils']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.16,<2.0', 'six']

setup_kwargs = {
    'name': 'numpoly',
    'version': '1.0.1',
    'description': 'Polynomials as a numpy datatype',
    'long_description': ".. image:: doc/.static/numpoly_logo.svg\n   :height: 200 px\n   :width: 200 px\n   :align: center\n\n|circleci| |codecov| |pypi| |readthedocs|\n\n.. |circleci| image:: https://circleci.com/gh/jonathf/numpoly/tree/master.svg?style=shield\n    :target: https://circleci.com/gh/jonathf/numpoly/tree/master\n.. |codecov| image:: https://codecov.io/gh/jonathf/numpoly/branch/master/graph/badge.svg\n    :target: https://codecov.io/gh/jonathf/numpoly\n.. |pypi| image:: https://badge.fury.io/py/numpoly.svg\n    :target: https://badge.fury.io/py/numpoly\n.. |readthedocs| image:: https://readthedocs.org/projects/numpoly/badge/?version=master\n    :target: http://numpoly.readthedocs.io/en/master/?badge=master\n\nNumpoly is a generic library for creating, manipulating and evaluating\narrays of polynomials based on ``numpy.ndarray`` objects.\n\n.. contents:: Table of Contents:\n\nFeature Overview\n----------------\n\n* Intuitive interface for users experienced with ``numpy``, as the library\n  provides a high level of compatibility with the ``numpy.ndarray``, including\n  fancy indexing, broadcasting, ``numpy.dtype``, vectorized operations to name\n  a few.\n* Computationally fast evaluations of lots of functionality inherent from\n  ``numpy``.\n* Vectorized polynomial evaluation.\n* Support for arbitrary number of dimensions and name for the indeterminants.\n* Native support for lots of ``numpy.<name>`` functions using ``numpy``'s\n  compatibility layer (which also exists as ``numpoly.<name>``\n  equivalents).\n* Support for polynomial division through the operators ``/``, ``%`` and\n  ``divmod``.\n* Extra polynomial specific attributes exposed on the polynomial objects like\n  ``poly.exponents``, ``poly.coefficients``, ``poly.indeterminants`` etc.\n* Polynomial derivation through functions like ``numpoly.diff``,\n  ``numpoly.gradient``, ``numpoly.hessian`` etc.\n* Decompose polynomial sums into vector of addends using ``numpoly.decompose``.\n* Variable substitution through ``numpoly.call``.\n\n``numpoly`` is currently being used as the backend is the uncertainty\nquantification library `chaospy <https://github.com/jonathf/chaospy>`_.\n\nInstallation\n------------\n\nInstallation should be straight forward:\n\n.. code-block:: bash\n\n    pip install numpoly\n\nAnd you should be ready to go. That is it. You should now be able to import the\nlibrary in your Python REPL:\n\n.. code-block:: python\n\n    >>> import numpoly\n\nExample Usage\n-------------\n\nConstructing polynomial is typically done using one of the available\nconstructors:\n\n.. code-block:: python\n\n    >>> numpoly.monomial(start=0, stop=3, names=2)\n    polynomial([1, q0, q0**2, q1, q0*q1, q1**2])\n\nIt is also possible to construct your own from symbols:\n\n.. code-block:: python\n\n    >>> q0, q1 = numpoly.variable(2)\n    >>> numpoly.polynomial([1, q0**2-1, q0*q1, q1**2-1])\n    polynomial([1, q0**2-1, q0*q1, q1**2-1])\n\nOr in combination with numpy objects using various arithmetics:\n\n.. code-block:: python\n\n    >>> q0**numpy.arange(4)-q1**numpy.arange(3, -1, -1)\n    polynomial([-q1**3+1, -q1**2+q0, q0**2-q1, q0**3-1])\n\nThe constructed polynomials can be evaluated as needed:\n\n.. code-block:: python\n\n    >>> poly = 3*q0+2*q1+1\n    >>> poly(q0=q1, q1=[1, 2, 3])\n    polynomial([3*q1+3, 3*q1+5, 3*q1+7])\n\nOr manipulated using various numpy functions:\n\n.. code-block:: python\n\n    >>> numpy.reshape(q0**numpy.arange(4), (2, 2))\n    polynomial([[1, q0],\n                [q0**2, q0**3]])\n    >>> numpy.sum(numpoly.monomial(13)[::3])\n    polynomial(q0**12+q0**9+q0**6+q0**3+1)\n\nDevelopment\n-----------\n\nDevelopment is done using `Poetry <https://poetry.eustace.io/>`_ manager.\nInside the repository directory, install and create a virtual environment with:\n\n.. code-block:: bash\n\n   poetry install\n\nTo run tests:\n\n.. code-block:: bash\n\n   poetry run pytest numpoly test doc --doctest-modules\n\nTo build documentation, run:\n\n.. code-block:: bash\n\n   cd doc/\n   make html\n\nThe documentation will be generated into the folder ``doc/.build/html``.\n\nQuestions and Contributions\n---------------------------\n\nPlease feel free to `file an issue\n<https://github.com/jonathf/numpoly/issues>`_ for:\n\n* bug reporting\n* asking questions related to usage\n* requesting new features\n* wanting to contribute with code\n",
    'author': 'Jonathan Feinberg',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jonathf/numpoly',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
