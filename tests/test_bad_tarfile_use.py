#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestBadTarfileUse(dlint.test.base.BaseTest):

    def test_bad_tarfile_usage(self):
        python_string = self.get_ast_node(
            """
            import tarfile

            def func():
                tf1 = tarfile.TarFile()
                tf2 = tarfile.TarFile.open()
                tf1.extract()
                tf2.extractall()
                tf1.extractall()
                tf2.extract()
            """
        )

        linter = dlint.linters.BadTarfileUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=4,
                message=dlint.linters.BadTarfileUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=8,
                col_offset=4,
                message=dlint.linters.BadTarfileUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=9,
                col_offset=4,
                message=dlint.linters.BadTarfileUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=10,
                col_offset=4,
                message=dlint.linters.BadTarfileUseLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_bad_tarfile_from_usage(self):
        python_string = self.get_ast_node(
            """
            from tarfile import TarFile

            def func():
                tf1 = TarFile()
                tf2 = TarFile.open()
                tf1.extract()
                tf2.extractall()
                tf1.extractall()
                tf2.extract()
            """
        )

        linter = dlint.linters.BadTarfileUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=4,
                message=dlint.linters.BadTarfileUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=8,
                col_offset=4,
                message=dlint.linters.BadTarfileUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=9,
                col_offset=4,
                message=dlint.linters.BadTarfileUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=10,
                col_offset=4,
                message=dlint.linters.BadTarfileUseLinter._error_tmpl
            )
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
