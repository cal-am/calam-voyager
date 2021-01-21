#!/usr/bin/env python

from distutils.core import setup

setup(
    name='calam-voyager',
    version='0.0.1',
    description='Python package for interacting with Yardi Voyager.',
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