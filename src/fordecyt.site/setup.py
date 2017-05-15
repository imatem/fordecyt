# -*- coding: utf-8 -*-
"""Installer for the moda.theme package."""

from setuptools import find_packages
from setuptools import setup


long_description = 'Theme for Fordecyt site'


setup(
    name='fordecyt.site',
    version='1.0a1',
    description='Fordecyt site',
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='Informatica Academica',
    author_email='informatica.academica@matem.unam.mx',
    url='https://github.com/imatem/fordecyt',
    license='GPL version 2',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['fordecyt'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.app.theming',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.testing>=5.0.0',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
