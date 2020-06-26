# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pkgstat']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0', 'requests>=2.24.0,<3.0.0']

entry_points = \
{'console_scripts': ['pkgstat = pkgstat:main']}

setup_kwargs = {
    'name': 'pkgstat',
    'version': '0.1.1',
    'description': 'Exercise',
    'long_description': None,
    'author': 'Jose C. Massón',
    'author_email': 'jose.masson@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
