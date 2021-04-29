#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="deecosim-lib",
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    author="Gabriel Rodrigues",
    author_email="gabrielsr@gmail.com",
    description="fork of pydeeco to be used a library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gabrielsr/deecosim-lib",
    packages=find_packages(include=['deeco']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
