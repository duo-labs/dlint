#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


def get_bad_module_attribute_use_implementation(illegal_module_attributes):
    class Cls(dlint.linters.helpers.bad_module_attribute_use.BadModuleAttributeUseLinter):
        _code = 'DUOXXX'
        _error_tmpl = 'DUOXXX error message'

        @property
        def illegal_module_attributes(self):
            return illegal_module_attributes

    return Cls()


class TestBadModuleAttributeUse(dlint.test.base.BaseTest):

    def test_empty_code(self):
        python_string = self.get_ast_node(
            """
            """
        )

        linter = get_bad_module_attribute_use_implementation({'foo': ['bar']})
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_empty_illegal_module_attributes(self):
        python_string = self.get_ast_node(
            """
            import os

            var = 'test'

            os.path.join(var)
            """
        )

        linter = get_bad_module_attribute_use_implementation({})
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_bad_foo_bar_usage(self):
        python_string = self.get_ast_node(
            """
            import foo

            var = 'echo "TEST"'

            foo.bar(var)
            """
        )

        linter = get_bad_module_attribute_use_implementation({'foo': ['bar']})
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=linter._error_tmpl
            )
        ]

        assert result == expected

    def test_bad_foo_bar_import_from_usage(self):
        python_string = self.get_ast_node(
            """
            from foo import bar

            var = 'echo "TEST"'

            bar(var)
            """
        )

        linter = get_bad_module_attribute_use_implementation({'foo': ['bar']})
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

    def test_bad_foo_bar_from_wildcard_usage(self):
        python_string = self.get_ast_node(
            """
            from foo import *

            var = 'echo "TEST"'

            bar(var)
            """
        )

        linter = get_bad_module_attribute_use_implementation({'foo': ['bar']})
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=linter._error_tmpl
            ),
        ]

        assert result == expected

    def test_multiple_bad_attributes_usage(self):
        python_string = self.get_ast_node(
            """
            import foo

            var = 'echo "TEST"'

            foo.bar(var)
            foo.baz(var)
            """
        )

        linter = get_bad_module_attribute_use_implementation(
            {'foo': ['bar', 'baz']}
        )
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=linter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=0,
                message=linter._error_tmpl
            )
        ]

        assert result == expected

    def test_multiple_bad_modules_usage(self):
        python_string = self.get_ast_node(
            """
            import foo
            import baz

            var = 'echo "TEST"'

            foo.bar(var)
            baz.qux(var)
            """
        )

        linter = get_bad_module_attribute_use_implementation(
            {'foo': ['bar'], 'baz': ['qux']}
        )
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=0,
                message=linter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=8,
                col_offset=0,
                message=linter._error_tmpl
            )
        ]

        assert result == expected

    def test_multiple_module_depth_usage(self):
        python_string = self.get_ast_node(
            """
            import foo.bar.baz

            var = 'echo "TEST"'

            foo.bar.baz.qux(var)
            """
        )

        linter = get_bad_module_attribute_use_implementation(
            {'foo.bar.baz': ['qux']}
        )
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=linter._error_tmpl
            ),
        ]

        assert result == expected

    def test_multiple_module_depth_from_usage(self):
        python_string = self.get_ast_node(
            """
            from foo import bar

            var = 'echo "TEST"'

            bar.baz.qux(var)
            """
        )

        linter = get_bad_module_attribute_use_implementation(
            {'bar.baz': ['qux']}
        )
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=linter._error_tmpl
            ),
        ]

        assert result == expected

    def test_no_foo_bar_usage(self):
        python_string = self.get_ast_node(
            """
            import os

            var = 'test'

            os.path.join(var)
            """
        )

        linter = get_bad_module_attribute_use_implementation({'foo': ['bar']})
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_bad_module_class_use(self):
        python_string = self.get_ast_node(
            """
            import foo

            bar = foo.Bar()
            """
        )

        linter = get_bad_module_attribute_use_implementation({'foo': ['Bar']})
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=6,
                message=linter._error_tmpl
            )
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
