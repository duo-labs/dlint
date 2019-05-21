#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestBadEvalUse(dlint.test.base.BaseTest):

    def test_bad_eval_usage(self):
        python_string = self.get_ast_node(
            """
            var = 1

            result = eval('var + 1')
            """
        )

        linter = dlint.linters.BadEvalUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=9,
                message=dlint.linters.BadEvalUseLinter._error_tmpl
            )
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
