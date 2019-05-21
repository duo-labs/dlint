#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestBadOSUse(dlint.test.base.BaseTest):

    def test_bad_os_usage(self):
        python_string = self.get_ast_node(
            """
            import os

            var = 'echo "TEST"'

            os.popen('ls')
            os.popen2('ls')
            os.popen3('ls')
            os.popen4('ls')
            os.system(var)
            os.tempnam()
            os.tmpnam()
            """
        )

        linter = dlint.linters.BadOSUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=dlint.linters.BadOSUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=0,
                message=dlint.linters.BadOSUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=8,
                col_offset=0,
                message=dlint.linters.BadOSUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=9,
                col_offset=0,
                message=dlint.linters.BadOSUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=10,
                col_offset=0,
                message=dlint.linters.BadOSUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=11,
                col_offset=0,
                message=dlint.linters.BadOSUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=12,
                col_offset=0,
                message=dlint.linters.BadOSUseLinter._error_tmpl
            ),
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
