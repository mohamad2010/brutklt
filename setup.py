#!/usr/bin/env python3
"""
setup.py

    Installs brute as CLI application locally.

"""

import os
from setuptools import setup, find_packages

NAME = "brute"
VERSION = "4.0"
REPO = "https://github.com/ex0dus-0x/brute"
DESC = """brute is a security-oriented tool for
conducting bruteforce attacks against a multitude of protocols and services"""

# Main setup method
setup(
    name = NAME,
    version = VERSION,
    author = "ex0dus",
    description = DESC,
    license = "GPLv3",
    url=REPO,
    download_url='{}/archive/v{}'.format(REPO, VERSION),
    packages = find_packages(),
    entry_points = {
        'console_scripts': [
            'brute=brute.__main__:main'
        ],
    },
    install_requires=[
        'paramiko',
        'selenium',
        'xmpppy',
        'requests'
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
