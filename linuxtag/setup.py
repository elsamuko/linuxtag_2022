#!/usr/bin/env python3
# https://github.com/pypa/sampleproject/blob/main/setup.py

from setuptools import find_packages, setup

setup(
    name='linuxtag',
    use_scm_version={
        "root": "..",
    },
    description='Demo project for Linuxtag 2022',
    url='https://github.com/elsamuko/linuxtag_2020',
    packages=find_packages(),
    setup_requires=[
        "setuptools_scm", # for use_scm_version
    ],
    install_requires=[
        "importlib-metadata",
    ],
    entry_points={
        "console_scripts": [
            "linuxtag=linuxtag.__main__:main",
        ],
    },
)
