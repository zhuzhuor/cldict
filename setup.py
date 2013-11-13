#!/usr/bin/env python

from setuptools import setup

setup(
    name='cldict',
    version='0.1',
    description='Command-line English-Chinese Dictionary',
    author='Bo Zhu',
    url='https://github.com/zhuzhuor/cldict/',
    packages=['cldict'],
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
    ]
)
