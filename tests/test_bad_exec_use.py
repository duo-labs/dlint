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

IS_PYTHON_THREE = sys.version_info >= (3, 0)


class TestBadExecUse(dlint.test.base.BaseTest):

    def test_bad_exec_usage(self):
        python_string = self.get_ast_node(
            """
            var = 1

            exec('print var + 1')
            """
        )

        linter = dlint.linters.BadExecUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadExecUseLinter._error_tmpl
            )
        ]

        assert result == expected

    @unittest.skipIf(IS_PYTHON_THREE, 'exec statements are a SyntaxError in Python 3')
    def test_bad_exec_statement_usage(self):
        python_string = self.get_ast_node(
            """
            var = 1

            exec 'print var + 1'
            """
        )

        linter = dlint.linters.BadExecUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadExecUseLinter._error_tmpl
            )
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
