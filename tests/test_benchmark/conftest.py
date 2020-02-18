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
    parser.addoption(
        "--benchmark-group-base-class",
        action="store_true",
        help="Group Dlint benchmark results by base class."
    )


@pytest.fixture
def benchmark_py_file(request):
    fd = request.config.getoption("--benchmark-py-file", skip=True)

    if fd.tell() > 0:
        # Read calls from previous tests exhaust the file descriptor
        fd.seek(0)

    return ast.parse(fd.read())


@pytest.fixture
def benchmark_group_base_class(request):
    return request.config.getoption("--benchmark-group-base-class")
