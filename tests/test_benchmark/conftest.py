#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import argparse
import ast

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--benchmark-py-file",
        action="store",
        type=argparse.FileType("r"),
        help="Benchmark Dlint against this Python file."
    )


@pytest.fixture
def benchmark_py_file(request):
    fd = request.config.getoption("--benchmark-py-file", skip=True)
    return ast.parse(fd.read())
