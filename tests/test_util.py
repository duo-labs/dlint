#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestUtil(unittest.TestCase):

    def test_abc(self):
        assert dlint.util.ABC


if __name__ == "__main__":
    unittest.main()
