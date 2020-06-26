import argparse
import sys

from setuptools import find_packages, setup


def get_version(name):
    version = {}
    with open('dagster_shell/version.py') as fp:
        exec(fp.read(), version)  # pylint: disable=W0122

    if name == 'dagster-shell':
        return version['__version__']
    elif name == 'dagster-shell-nightly':
        return version['__nightly__']
    else:
        raise Exception('Shouldn\'t be here: bad package name {name}'.format(name=name))


parser = argparse.ArgumentParser()
parser.add_argument('--nightly', action='store_true')


def _do_setup(name='dagster-shell'):
    setup(
        name=name,
        version=get_version(name),
        author='Elementl',
        license='Apache-2.0',
        description='Package for Dagster shell solids.',
        url='https://github.com/dagster-io/dagster/tree/master/python_modules/libraries/dagster-shell',
        classifiers=[
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent',
        ],
        packages=find_packages(exclude=['test']),
        install_requires=['dagster'],
        zip_safe=False,
    )


if __name__ == '__main__':
    parsed, unparsed = parser.parse_known_args()
    sys.argv = [sys.argv[0]] + unparsed
    if parsed.nightly:
        _do_setup('dagster-shell-nightly')
    else:
        _do_setup('dagster-shell')
