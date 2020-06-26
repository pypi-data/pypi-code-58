# This file was automatically generated by Shore. Do not edit manually.
# For more information on Shore see https://pypi.org/project/nr.shore/

from __future__ import print_function
import io
import os
import re
import setuptools
import sys

with io.open('src/nr/databind/core/__init__.py', encoding='utf8') as fp:
  version = re.search(r"__version__\s*=\s*'(.*)'", fp.read()).group(1)

readme_file = 'README.md'
if os.path.isfile(readme_file):
  with io.open(readme_file, encoding='utf8') as fp:
    long_description = fp.read()
else:
  print("warning: file \"{}\" does not exist.".format(readme_file), file=sys.stderr)
  long_description = None

requirements = ['nr.collections >=0.0.1,<1.0.0', 'nr.interface >=0.0.1,<0.1.0', 'nr.stream >=0.0.1,<0.1.0', 'nr.pylang.utils >=0.0.3,<0.1.0']
extras_require = {}
extras_require['test'] = ['pytest', 'PyYAML']
tests_require = []
tests_require = ['pytest', 'PyYAML']

setuptools.setup(
  name = 'nr.databind.core',
  version = version,
  author = 'Niklas Rosenstein',
  author_email = 'rosensteinniklas@gmail.com',
  description = 'Bind structured data directly to typed objects.',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  url = 'https://git.niklasrosenstein.com/NiklasRosenstein/nr-python-libs',
  license = 'MIT',
  packages = setuptools.find_packages('src', ['test', 'test.*', 'docs', 'docs.*']),
  package_dir = {'': 'src'},
  include_package_data = True,
  install_requires = requirements,
  extras_require = extras_require,
  tests_require = tests_require,
  python_requires = None, # TODO: '>=2.7,<3.0.0|>=3.4,<4.0.0',
  data_files = [],
  entry_points = {
    'nr.databind.core.union.test_entrypoints': [
      'int = test_union_type:Integer',
      'string = test_union_type:String',
    ]
  },
  cmdclass = {},
  keywords = [],
  classifiers = [],
  options = {
    'bdist_wheel': {
      'universal': True,
    },
  },
)
