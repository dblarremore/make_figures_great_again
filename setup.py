from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='make_figures_great_again',
    version='0.2dev',
    description=(
        'Color palettes for Python'),
    long_description=long_description,
    author='author',
    author_email='author@email.com',
    url='https://www.donaldjtrump.com/',
    packages=find_packages(exclude=["*.test"]),
    install_requires=[
        'matplotlib',
        'palettable'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering :: Visualization'])
