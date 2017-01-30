#!/usr/bin/env python

from setuptools import setup

setup(
    name="python-liberaexporter",
    version="0.2.1",
    description="Prometheus exporter for libera devices.",
    author="Vasileios Martos",
    author_email="vasileios.martos@maxlab.lu.se",
    license="GPLv3",
    url="http://www.maxlab.lu.se",
    packages=['liberaexporter'],
    entry_points={
        'console_scripts': [
            'liberaexporter = liberaexporter:main'
        ]
    }
)