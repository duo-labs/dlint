#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import sys
import unittest

import dlint

IS_PYTHON_2 = sys.version_info < (3, 0)


class TestBadInputUse(dlint.test.base.BaseTest):

    def test_empty(self):
        python_string = self.get_ast_node(
            """
            """
        )

        linter = dlint.linters.BadInputUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_bad_input_usage(self):
        python_string = self.get_ast_node(
            """
            var = 1

            result = input('var + 1')
            """
        )

        linter = dlint.linters.BadInputUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [] if not IS_PYTHON_2 else [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=9,
                message=dlint.linters.BadInputUseLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_six_moves_input_usage(self):
        python_string = self.get_ast_node(
            """
            from six.moves import input

            var = 1

            result = input('var + 1')
            """
        )

        linter = dlint.linters.BadInputUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_no_input_usage(self):
        python_string = self.get_ast_node(
            """
            import os

            var = 'test'

            os.path.join(var)
            """
        )

        linter = dlint.linters.BadInputUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected


if __name__ == "__main__":
    unittest.main()
