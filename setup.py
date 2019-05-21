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
    description=(
        "Dlint is a tool for encouraging best coding practices "
        "and helping ensure we're writing secure code."
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/duo-labs/dlint',
    packages=find_packages(),
    license='BSD-3-Clause',
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
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
