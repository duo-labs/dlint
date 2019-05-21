#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestBadGlUse(dlint.test.base.BaseTest):

    def test_bad_gl_usage(self):
        python_string = self.get_ast_node(
            """
            import gl
            """
        )

        linter = dlint.linters.BadGlUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=2,
                col_offset=0,
                message=dlint.linters.BadGlUseLinter._error_tmpl
            )
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
