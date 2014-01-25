#!/usr/bin/env python
from setuptools import setup, find_packages

DESCRIPTION = "A python client for redisq (Fast message processing queue backed up by redis and nodejs.)"

LONG_DESCRIPTION = open('README.rst').read()

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

INSTALL_REQUIRES = ['redis']

try:
    import importlib
except ImportError:
    INSTALL_REQUIRES.append('importlib')

tests_require = [
    'redis'
]

setup(
    name='redisq-py',
    version='1.0.0',
    packages=find_packages(exclude=[]),
    author='Joshua Karjala-Svenden',
    author_email='joshua@fluxuries.com',
    url='https://github.com/joshuakarjala/redisq-py/',
    license='MIT',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    platforms=['any'],
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIRES,
    # tests_require=tests_require,
    # extras_require={'test': tests_require},
    # test_suite='runtests.runtests',
    #include_package_data=True,
)
