# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='',
    version='0.0.0',
    description='',
    long_description=readme,
    author='',
    author_email='',
    url='',
    license=license,
    packages=[""],#find_packages(exclude=('tests', 'docs')),
    zip_safe=False
)
