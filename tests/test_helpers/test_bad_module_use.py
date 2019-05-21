#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


def get_bad_module_use_implementation(illegal_modules, whitelisted_modules=None):
    if whitelisted_modules is None:
        whitelisted_modules = []

    class Cls(dlint.linters.helpers.bad_module_use.BadModuleUseLinter):
        _code = 'DUOXXX'
        _error_tmpl = 'DUOXXX error message'

        @property
        def illegal_modules(self):
            return illegal_modules

        @property
        def whitelisted_modules(self):
            return whitelisted_modules

    return Cls()


class TestBadModuleUse(dlint.test.base.BaseTest):

    def test_empty(self):
        python_string = self.get_ast_node(
            """
            """
        )

        linter = get_bad_module_use_implementation([""])
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_empty_illegal_module_usage(self):
        python_string = self.get_ast_node(
            """
            import foo
            """
        )

        linter = get_bad_module_use_implementation([])
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_bad_import_usage(self):
        python_string = self.get_ast_node(
            """
            import foo
            """
        )

        linter = get_bad_module_use_implementation(["foo"])
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=2,
                col_offset=0,
                message=linter._error_tmpl
            )
        ]

        assert result == expected

    def test_multiple_bad_import_usage(self):
        python_string = self.get_ast_node(
            """
            import foo
            import bar
            """
        )

        linter = get_bad_module_use_implementation(["foo", "bar"])
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=2,
                col_offset=0,
                message=linter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=3,
                col_offset=0,
                message=linter._error_tmpl
            )
        ]

        assert result == expected

    def test_bad_parent_import_usage(self):
        python_string = self.get_ast_node(
            """
            import foo.bar.baz
            """
        )

        linter = get_bad_module_use_implementation(["foo.bar"])
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=2,
                col_offset=0,
                message=linter._error_tmpl
            )
        ]

        assert result == expected

    def test_bad_nested_import_usage(self):
        python_string = self.get_ast_node(
            """
            import foo.bar
            """
        )

        linter = get_bad_module_use_implementation(["foo.bar"])
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=2,
                col_offset=0,
                message=linter._error_tmpl
            )
        ]

        assert result == expected

    def test_deeper_mismatch_import_usage(self):
        python_string = self.get_ast_node(
            """
            import foo.bar
            """
        )

        linter = get_bad_module_use_implementation(["foo.bar.baz"])
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_child_mismatch_import_usage(self):
        python_string = self.get_ast_node(
            """
            import foo.bar
            """
        )

        linter = get_bad_module_use_implementation(["foo.baz"])
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_bad_import_from_usage(self):
        python_string = self.get_ast_node(
            """
            from foo import bar
            """
        )

        linter = get_bad_module_use_implementation(["foo"])
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=2,
                col_offset=0,
                message=linter._error_tmpl
            )
        ]

        assert result == expected

    def test_bad_namespaced_import_from_usage(self):
        python_string = self.get_ast_node(
            """
            from foo import bar
            """
        )

        linter = get_bad_module_use_implementation(["foo.bar"])
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=2,
                col_offset=0,
                message=linter._error_tmpl
            )
        ]

        assert result == expected

    def test_child_mismatch_import_from_usage(self):
        python_string = self.get_ast_node(
            """
            from foo import bar
            """
        )

        linter = get_bad_module_use_implementation(["foo.baz"])
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_multiple_bad_import_from_usage(self):
        python_string = self.get_ast_node(
            """
            from foo import bar
            from baz import qux
            """
        )

        linter = get_bad_module_use_implementation(["foo", "baz"])
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=2,
                col_offset=0,
                message=linter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=3,
                col_offset=0,
                message=linter._error_tmpl
            )
        ]

        assert result == expected

    def test_bad_nested_import_from_usage(self):
        python_string = self.get_ast_node(
            """
            from foo.bar.baz import qux
            """
        )

        linter = get_bad_module_use_implementation(["foo.bar"])
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=2,
                col_offset=0,
                message=linter._error_tmpl
            )
        ]

        assert result == expected

    def test_whitelisted_import_usage(self):
        python_string = self.get_ast_node(
            """
            import foo.bar
            import foo.bar.baz
            """
        )

        linter = get_bad_module_use_implementation(
            ["foo"],
            whitelisted_modules=["foo.bar.baz"]
        )
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=2,
                col_offset=0,
                message=linter._error_tmpl
            )
        ]

        assert result == expected

    def test_whitelisted_from_import_usage(self):
        python_string = self.get_ast_node(
            """
            from foo import bar
            from foo.bar import baz
            """
        )

        linter = get_bad_module_use_implementation(
            ["foo"],
            whitelisted_modules=["foo.bar.baz"]
        )
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=2,
                col_offset=0,
                message=linter._error_tmpl
            )
        ]

        assert result == expected

    def test_relative_import_from_usage(self):
        python_string = self.get_ast_node(
            """
            from . import foo
            from .. import bar
            from .baz import qux
            """
        )

        linter = get_bad_module_use_implementation(["foo"])
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_no_foo_usage(self):
        python_string = self.get_ast_node(
            """
            import os

            var = 'test'

            os.path.join(var)
            """
        )

        linter = get_bad_module_use_implementation(["foo"])
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected


if __name__ == "__main__":
    unittest.main()
