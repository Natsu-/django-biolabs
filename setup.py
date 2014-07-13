#!/usr/bin/python
# -*- coding: utf8 -*-
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='django-biolabs',
    version='0.1',
    author='Romain Garrigues',
    author_email='romain.garrigues.cs@gmail.com',
    url='http://youkidea.com',
    description="Biolabs",
    install_requires=[
        'South == 0.8.4',
        'django == 1.6',
        'djangorestframework == 2.3.14',
        'markdown == 2.4.1',
        'django-filter == 0.7'
    ],
    license='BSD, see LICENSE file.',
    packages=find_packages(),
    classifiers=['Natural Language :: English',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Programming Language :: Python :: 2.7'],
)
