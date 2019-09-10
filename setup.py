from setuptools import (
    find_packages,
    setup,
)

import os

import dlint

requirements_filename = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'requirements.txt')

with open(requirements_filename) as fd:
    install_requires = [i.strip() for i in fd.readlines()]

requirements_dev_filename = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'requirements-dev.txt')

with open(requirements_dev_filename) as fd:
    tests_require = [i.strip() for i in fd.readlines()]

long_description_filename = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'README.md')

with open(long_description_filename) as fd:
    long_description = fd.read()

setup(
    name=dlint.__name__,
    version=dlint.__version__,
    description=dlint.__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=dlint.__url__,
    packages=find_packages(),
    license=dlint.__license__,
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Security',
        'Topic :: Software Development :: Quality Assurance',
    ],
    tests_require=tests_require,
    install_requires=install_requires,
    entry_points={
        'flake8.extension': [
            'DUO = dlint.extension:Flake8Extension',
        ],
    },
)
