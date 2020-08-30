#!/usr/bin/python3

from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='getquote',
    version='1.1.0',
    scripts=['getquote.py'],
    entry_points={
        'console_scripts': [
            'getquote = getquote:main',
        ],
    },
    author='Jean-Ralph Aviles',
    author_email='jeanralph.aviles@gmail.com',
    description='A ledger-cli getquote implementation using free IEX Cloud API',
    long_description=readme(),
    long_description_content_type='text/markdown',
    keywords=' '.join([
        'ledger-cli', 'personal', 'finance', 'stocks',
    ]),
    url='https://github.com/jeanralphaviles/getquote',
    license='MIT',
)
