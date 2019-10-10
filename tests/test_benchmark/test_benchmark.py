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

# Since extension imports dlint we cannot add it to the module or else we'll
# have circular imports. Thus we must come up with some tricks to import it
sys.path.append(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "dlint"
    )
)

import extension  # noqa: E402


def test_benchmark_run(benchmark_py_file, benchmark):
    ext = extension.Flake8Extension(benchmark_py_file, "unused")

    benchmark(lambda: list(ext.run()))

    assert ext


if __name__ == "__main__":
    unittest.main()
