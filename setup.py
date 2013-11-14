#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='cldict',
    version='0.1.2',
    description='Command-line English-Chinese Dictionary',
    author='Bo Zhu',
    url='https://github.com/zhuzhuor/cldict/',
    packages=find_packages(),
    license='MIT',
    entry_points={
        'console_scripts': [
            'cldict = cldict.cmdln:main_func'
        ]
    },
    install_requires=[
        'beautifulsoup4',
        'bisheng',
        'requests'
    ],
    test_suite='tests'
)
