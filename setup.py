#!/usr/bin/env python

import os.path

import setuptools

with open('requirements.txt') as f:
    required_packages = f.read().splitlines()

setuptools.setup(
    name='beancount-mercury',
    long_description=open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)),
                     'README.md')).read(),
    long_description_content_type="text/markdown",
    version='0.1.4',
    description='Import Mercury banking transactions into beancount format',
    author='Michael Lynch',
    license="MIT",
    keywords="mercury beancount bookkeeping finance",
    url='https://github.com/mtlynch/beancount-mercury.git',
    packages=['beancount_mercury'],
    install_requires=[required_packages],
    python_requires='>=3.9',
)
