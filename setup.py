#!/usr/bin/env python
from counters import __version__

sdict = {
    'name' : 'counters',
    'version' : __version__,
    'description' : 'A Python port of https://github.com/francois/counters',
    'long_description' : 'Provides an easy interface to count any kind of performance metrics within a system',
    'url': 'http://github.com/francois/pycounters',
    'download_url' : 'http://cloud.github.com/downloads/francois/pycounters/counters-%s.tar.gz' % __version__,
    'author' : 'François Beausoleil',
    'author_email' : 'francois@teksol.info',
    'maintainer' : 'François Beausoleil',
    'maintainer_email' : 'francois@teksol.info',
    'keywords' : ['Redis', 'key-value store'],
    'license' : 'MIT',
    'packages' : ['counters'],
    'test_suite' : 'tests.all_tests',
    'classifiers' : [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'],
}

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
setup(**sdict)

