#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestBadTempfileUse(dlint.test.base.BaseTest):

    def test_bad_tempfile_usage(self):
        python_string = self.get_ast_node(
            """
            import tempfile

            tempfile.mktemp()
            """
        )

        linter = dlint.linters.BadTempfileUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadTempfileUseLinter._error_tmpl
            ),
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
