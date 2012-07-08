#! /usr/bin/env python
#! -*- coding: utf-8 *-*-

import sys
from setuptools import Command, setup, find_packages

readme = """
            CoderWall
====
    Simple Pythonic way to access CoderWall profile.

Built With
----
    - requests
    - Cement
         """
setup(
    name='pycoderwall',
    version='0.0.4',
    url='https://github.com/kracekumar/coderwall',
    license='BSD',
    author='kracekumar',
    author_email='me@kracekumar.com',
    description='CLI for accessing coderwall user details',
    long_description=readme,
    packages=find_packages(),
    install_requires=['requests', 'cement'],
    entry_points={
        'console_scripts': [
            'pycoderwall = coderwall.main:main',
            ]
    },
    classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: BSD License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Topic :: Software Development',
          'Topic :: Software Development :: Build Tools',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',

    ],
    )