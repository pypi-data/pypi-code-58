import os
import runpy
import subprocess
from distutils.cmd import Command
from setuptools import setup
from tempfile import TemporaryDirectory


class PyinstallerCommand(Command):
    description = "create a self-contained executable with PyInstaller"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        with TemporaryDirectory() as temp_dir:
            subprocess.check_call(["python3", "-m", "venv", os.path.join(temp_dir, "env")])
            subprocess.check_call([os.path.join(temp_dir, "env/bin/pip"), "install", "."])
            subprocess.check_call([os.path.join(temp_dir, "env/bin/pip"), "install", "pyinstaller"])
            with open(os.path.join(temp_dir, "entrypoint.py"), "w") as f:
                f.write(
                    """
#!/usr/bin/env python3

from github_binary_upload import main


if __name__ == "__main__":
    main()
                    """.strip()
                )
            subprocess.check_call(
                [
                    os.path.join(temp_dir, "env/bin/pyinstaller"),
                    "--clean",
                    "--name=github-binary-upload",
                    "--onefile",
                    "--strip",
                    os.path.join(temp_dir, "entrypoint.py"),
                ]
            )


def get_version_from_pyfile(version_file="github_binary_upload.py"):
    file_globals = runpy.run_path(version_file)
    return file_globals["__version__"]


def get_long_description_from_readme(readme_filename="README.md"):
    long_description = None
    if os.path.isfile(readme_filename):
        with open(readme_filename, "r", encoding="utf-8") as readme_file:
            long_description = readme_file.read()
    return long_description


version = get_version_from_pyfile()
long_description = get_long_description_from_readme()

setup(
    name="github-binary-upload",
    version=version,
    py_modules=["github_binary_upload"],
    python_requires="~=3.3",
    install_requires=["requests", "yacl"],
    entry_points={"console_scripts": ["github-binary-upload = github_binary_upload:main"]},
    cmdclass={"bdist_pyinstaller": PyinstallerCommand},
    author="Ingo Heimbach",
    author_email="i.heimbach@fz-juelich.de",
    description="github-binary-upload is a utility for publishing releases from tags with attached files on GitHub.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/sciapp/github-binary-upload",
    keywords=["git", "GitHub", "release", "assets"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Version Control :: Git",
        "Topic :: Utilities",
    ],
)
