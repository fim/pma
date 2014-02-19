#!/usr/bin/env python

from distutils.core import setup


setup(name='pma',
    version='0.1',
    description='A simple script to create Postfix backends on SQLite/PSQL/MySQL',
    author='fim'
    packages=['pma'],
    scripts=['pma']
)
