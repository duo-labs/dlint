#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


def get_builtin_use_implementation(illegal_builtin):
    class Cls(dlint.linters.helpers.bad_builtin_use.BadBuiltinUseLinter):
        _code = 'DUOXXX'
        _error_tmpl = 'DUOXXX error message'

        @property
        def illegal_builtin(self):
            return illegal_builtin

    return Cls()


class TestBadBuiltinUse(dlint.test.base.BaseTest):

    def test_empty(self):
        python_string = self.get_ast_node(
            """
            """
        )

        linter = get_builtin_use_implementation('foo')
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_bad_builtin_usage(self):
        python_string = self.get_ast_node(
            """
            var = 1

            result = foo('var + 1')
            """
        )

        linter = get_builtin_use_implementation('foo')
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=9,
                message=linter._error_tmpl
            )
        ]

        assert result == expected

    def test_no_builtin_usage(self):
        python_string = self.get_ast_node(
            """
            import os

            var = 'test'

            os.path.join(var)
            """
        )

        linter = get_builtin_use_implementation('foo')
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected


if __name__ == "__main__":
    unittest.main()
