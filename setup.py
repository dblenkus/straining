#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Open source dataflow package for Django framework.
See:
https://github.com/dblenkus/straining
"""

from setuptools import find_packages, setup
from os import path

base_dir = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(base_dir, 'README.rst')) as f:
    long_description = f.read()

# Get package metadata from 'straining.__about__.py' file
about = {}
with open(path.join(base_dir, 'straining', '__about__.py')) as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],

    version=about['__version__'],

    description=about['__summary__'],
    long_description=long_description,

    url=about['__url__'],

    author=about['__author__'],
    author_email=about['__email__'],

    license=about['__license__'],

    # exclude tests from built/installed package
    packages=find_packages(exclude=['tests', 'tests.*', '*.tests', '*.tests.*']),
    install_requires=[
        'asgiref~=2.3.0',
        'channels~=2.1.0',
        'channels_redis~=2.3.0',
        'Django~=2.1.0',
        'django-fernet-fields==0.5',
        'djangorestframework~=3.9.0',
        'requests~=2.19.1',
    ],
    python_requires='>=3.6, <3.8',
    extras_require={
        'package': [
            'twine',
            'wheel',
        ],
    },

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',

        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Other Audience',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: Apache Software License',

        'Operating System :: OS Independent',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='training cycling running',
)
