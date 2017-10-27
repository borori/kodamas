from setuptools import setup, find_packages
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='kodamas',
    version='1.0.0',
    description='',
    long_description=long_description,
    author='boroir',
    url='',
    scripts=['bin/kodamas'],
    license="MIT",
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    classifiers=(
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License'
    ),
)
