#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestBadSubprocessUse(dlint.test.base.BaseTest):

    def test_bad_subprocess_usage(self):
        python_string = self.get_ast_node(
            """
            import subprocess

            subprocess.call(shell=True)
            subprocess.check_call(shell=True)
            subprocess.check_output(shell=True)
            subprocess.Popen(shell=True)
            """
        )

        linter = dlint.linters.BadSubprocessUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadSubprocessUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=5,
                col_offset=0,
                message=dlint.linters.BadSubprocessUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=dlint.linters.BadSubprocessUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=0,
                message=dlint.linters.BadSubprocessUseLinter._error_tmpl
            ),
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
