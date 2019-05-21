#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import ast
import unittest

import pytest

import dlint


class TestTree(unittest.TestCase):

    def test_decorator_name_unknown_type(self):
        unknown_type = None

        with pytest.raises(TypeError):
            dlint.tree.decorator_name(unknown_type)

    def test_call_name_unknown_type(self):
        unknown_type = ast.Call(func=None)

        with pytest.raises(TypeError):
            dlint.tree.call_name(unknown_type)


if __name__ == "__main__":
    unittest.main()
