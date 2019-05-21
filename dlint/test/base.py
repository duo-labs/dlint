#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import ast
import textwrap
import unittest


class BaseTest(unittest.TestCase):

    @staticmethod
    def get_ast_node(s):
        return ast.parse(textwrap.dedent(s))
