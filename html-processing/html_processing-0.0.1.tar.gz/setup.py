import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="html_processing",
    version="0.0.1",
    author="J. Hohenstein",
    author_email="j.hoh@t-online.de",
    description="Helps processing html with lxml",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.uni-due.de/",
    packages=setuptools.find_packages(exclude=("tests",)),
    install_requires=[
        'lxml~=4.5.1',
        'requests~=2.24.0',
        'dpp_common_utils~=0.1.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
