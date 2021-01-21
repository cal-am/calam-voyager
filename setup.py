#!/usr/bin/env python

from distutils.core import setup
from pathlib import Path


readme = Path(__file__).parent / 'README.md'

with open(readme, 'r') as file:
    long_description = file.read()

setup(
    name='calam-voyager',
    version='0.1a1',
    description='Python package for interacting with Yardi Voyager.',
    long_description=long_description,
    author='Ben Russell',
    author_email='benr@cal-am.com',
    url='https://github.com/benr-calam/calam-voyager',
    packages=['calam_voyager', 'calam_voyager.blocking'],
    requires=[
        'aiohttp',
        'requests',
        'beautifulsoup4',
        'aiodns',
        'cchardet'
    ]
)