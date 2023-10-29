# -*- coding: utf-8 -*-

from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='megaville',
    version='1.0',
    description='Cool game !',
    long_description=readme,
    author='Skyend3, Birdo3D',
    url='https://github.com/Megaville/megaville',
    packages=['megaville']
)
