#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import os
import sys
import unittest

import pytest

# Since extension imports dlint we cannot add it to the module or else we'll
# have circular imports. Thus we must come up with some tricks to import it
sys.path.append(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "dlint"
    )
)

import extension  # noqa: E402

# These must be in the same order for parametrize to index correctly
LINTERS = sorted(extension.dlint.linters.ALL, key=lambda l: l._code)
LINTER_IDS = ["{}-{}".format(l._code, l.__name__) for l in LINTERS]


def get_single_linter_extension(linter):
    class SingleLinterExtention(extension.Flake8Extension):
        @classmethod
        def get_linter_classes(cls):
            return [linter]

    return SingleLinterExtention


def test_benchmark_run(benchmark_py_file, benchmark):
    ext = extension.Flake8Extension(benchmark_py_file, "unused")

    benchmark(lambda: list(ext.run()))

    assert ext


@pytest.mark.parametrize('linter', LINTERS, ids=LINTER_IDS)
def test_benchmark_individual(benchmark_py_file, benchmark, linter):
    ext_class = get_single_linter_extension(linter)
    ext = ext_class(benchmark_py_file, "unused")

    benchmark(lambda: list(ext.run()))

    assert ext


if __name__ == "__main__":
    unittest.main()
