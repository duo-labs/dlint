#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestBadZipfileUse(dlint.test.base.BaseTest):

    def test_bad_zipfile_usage(self):
        python_string = self.get_ast_node(
            """
            import zipfile

            def func():
                zf = zipfile.ZipFile()
                zf.extract()
                zf.extractall()
            """
        )

        linter = dlint.linters.BadZipfileUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=4,
                message=dlint.linters.BadZipfileUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=4,
                message=dlint.linters.BadZipfileUseLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_bad_zipfile_from_usage(self):
        python_string = self.get_ast_node(
            """
            from zipfile import ZipFile

            def func():
                zf = ZipFile()
                zf.extract()
                zf.extractall()
            """
        )

        linter = dlint.linters.BadZipfileUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=4,
                message=dlint.linters.BadZipfileUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=4,
                message=dlint.linters.BadZipfileUseLinter._error_tmpl
            )
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
