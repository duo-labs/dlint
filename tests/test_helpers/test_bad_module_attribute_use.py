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
        python_node = self.get_ast_node(
            """
            """
        )

        linter = get_bad_module_attribute_use_implementation({'foo': ['bar']})
        linter.visit(python_node)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_empty_illegal_module_attributes(self):
        python_node = self.get_ast_node(
            """
            import os

            var = 'test'

            os.path.join(var)
            """
        )

        linter = get_bad_module_attribute_use_implementation({})
        linter.visit(python_node)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_module_attribute_usage(self):
        python_node = self.get_ast_node(
            """
            import foo

            var = 'echo "TEST"'

            foo.bar(var)
            """
        )

        linter = get_bad_module_attribute_use_implementation({'foo': ['bar']})
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=linter._error_tmpl
            )
        ]

        assert result == expected

    def test_module_attribute_as_usage(self):
        python_node = self.get_ast_node(
            """
            import foo.bar as baz

            var = 'echo "TEST"'

            baz.qux(var)
            """
        )

        linter = get_bad_module_attribute_use_implementation({'foo.bar': ['qux']})
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=linter._error_tmpl
            )
        ]

        assert result == expected

    def test_module_attribute_import_from_usage(self):
        python_node = self.get_ast_node(
            """
            from foo import bar

            var = 'echo "TEST"'

            bar(var)
            """
        )

        linter = get_bad_module_attribute_use_implementation({'foo': ['bar']})
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=linter._error_tmpl
            )
        ]

        assert result == expected

    def test_module_attribute_import_from_as_usage(self):
        python_node = self.get_ast_node(
            """
            from foo.bar import baz as qux

            var = 'echo "TEST"'

            qux(var)
            """
        )

        linter = get_bad_module_attribute_use_implementation({'foo.bar': ['baz']})
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=linter._error_tmpl
            )
        ]

        assert result == expected

    def test_module_attribute_from_wildcard_usage(self):
        python_node = self.get_ast_node(
            """
            from foo import *

            var = 'echo "TEST"'

            bar(var)
            """
        )

        linter = get_bad_module_attribute_use_implementation({'foo': ['bar']})
        linter.visit(python_node)

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
        python_node = self.get_ast_node(
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
        linter.visit(python_node)

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
        python_node = self.get_ast_node(
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
        linter.visit(python_node)

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
        python_node = self.get_ast_node(
            """
            import foo.bar.baz

            var = 'echo "TEST"'

            foo.bar.baz.qux(var)
            """
        )

        linter = get_bad_module_attribute_use_implementation(
            {'foo.bar.baz': ['qux']}
        )
        linter.visit(python_node)

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
        python_node = self.get_ast_node(
            """
            from foo import bar

            var = 'echo "TEST"'

            bar.baz.qux(var)
            """
        )

        linter = get_bad_module_attribute_use_implementation(
            {'foo.bar.baz': ['qux']}
        )
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=linter._error_tmpl
            ),
        ]

        assert result == expected

    def test_no_module_attribute_usage(self):
        python_node = self.get_ast_node(
            """
            import os

            var = 'test'

            os.path.join(var)
            """
        )

        linter = get_bad_module_attribute_use_implementation({'foo': ['bar']})
        linter.visit(python_node)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_bad_module_class_use(self):
        python_node = self.get_ast_node(
            """
            import foo

            bar = foo.Bar()
            """
        )

        linter = get_bad_module_attribute_use_implementation({'foo': ['Bar']})
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=6,
                message=linter._error_tmpl
            )
        ]

        assert result == expected

    def test_module_attribute_missing_import_usage(self):
        python_node = self.get_ast_node(
            """
            import baz
            from qux import quine
            from . import xyz

            var = 'echo "TEST"'

            foo = None
            foo.bar(var)
            """
        )

        linter = get_bad_module_attribute_use_implementation({'foo': ['bar']})
        linter.visit(python_node)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_module_attribute_arbitrary_depth_usage_legacy(self):
        python_node = self.get_ast_node(
            """
            import m1
            from m1 import m2
            from m1.m2 import m3
            from m1.m2.m3 import m4

            m1.m2.m3.m4.bad_attribute()
            m2.m3.m4.bad_attribute()
            m3.m4.bad_attribute()
            m4.bad_attribute()
            """
        )

        linter = get_bad_module_attribute_use_implementation({
            'm1.m2.m3.m4': ['bad_attribute'],
            'm2.m3.m4': ['bad_attribute'],
            'm3.m4': ['bad_attribute'],
            'm4': ['bad_attribute'],
        })
        linter.visit(python_node)

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
            ),
            dlint.linters.base.Flake8Result(
                lineno=9,
                col_offset=0,
                message=linter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=10,
                col_offset=0,
                message=linter._error_tmpl
            )
        ]

        assert result == expected

    def test_module_attribute_arbitrary_depth_usage_new(self):
        python_node = self.get_ast_node(
            """
            import m1
            from m1 import m2
            from m1.m2 import m3
            from m1.m2.m3 import m4

            m1.m2.m3.m4.bad_attribute()
            m2.m3.m4.bad_attribute()
            m3.m4.bad_attribute()
            m4.bad_attribute()
            """
        )

        linter = get_bad_module_attribute_use_implementation({
            'm1.m2.m3.m4': ['bad_attribute'],
        })
        linter.visit(python_node)

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
            ),
            dlint.linters.base.Flake8Result(
                lineno=9,
                col_offset=0,
                message=linter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=10,
                col_offset=0,
                message=linter._error_tmpl
            )
        ]

        assert result == expected

    def test_module_attribute_arbitrary_import_depth_usage_new(self):
        python_strings = [
            """
            import m1
            m1.m2.m3.m4.bad_attribute()
            """,
            """
            import m1.m2
            m1.m2.m3.m4.bad_attribute()
            """,
            """
            import m1.m2.m3
            m1.m2.m3.m4.bad_attribute()
            """,
            """
            import m1.m2.m3.m4
            m1.m2.m3.m4.bad_attribute()
            """,
        ]

        for python_string in python_strings:
            python_node = self.get_ast_node(python_string)

            linter = get_bad_module_attribute_use_implementation({
                'm1.m2.m3.m4': ['bad_attribute'],
            })
            linter.visit(python_node)

            result = linter.get_results()
            expected = [
                dlint.linters.base.Flake8Result(
                    lineno=3,
                    col_offset=0,
                    message=linter._error_tmpl
                )
            ]

            assert result == expected

    def test_module_attribute_arbitrary_import_as_depth_usage_new(self):
        python_strings = [
            """
            import m1 as alias
            alias.m2.m3.m4.bad_attribute()
            """,
            """
            import m1.m2 as alias
            alias.m3.m4.bad_attribute()
            """,
            """
            import m1.m2.m3 as alias
            alias.m4.bad_attribute()
            """,
            """
            import m1.m2.m3.m4 as alias
            alias.bad_attribute()
            """,
        ]

        for python_string in python_strings:
            python_node = self.get_ast_node(python_string)

            linter = get_bad_module_attribute_use_implementation({
                'm1.m2.m3.m4': ['bad_attribute'],
            })
            linter.visit(python_node)

            result = linter.get_results()
            expected = [
                dlint.linters.base.Flake8Result(
                    lineno=3,
                    col_offset=0,
                    message=linter._error_tmpl
                )
            ]

            assert result == expected

    def test_module_attribute_arbitrary_from_import_as_depth_usage_new(self):
        python_strings = [
            """
            from m1 import m2 as alias
            alias.m3.m4.bad_attribute()
            """,
            """
            from m1.m2 import m3 as alias
            alias.m4.bad_attribute()
            """,
            """
            from m1.m2.m3 import m4 as alias
            alias.bad_attribute()
            """,
        ]

        for python_string in python_strings:
            python_node = self.get_ast_node(python_string)

            linter = get_bad_module_attribute_use_implementation({
                'm1.m2.m3.m4': ['bad_attribute'],
            })
            linter.visit(python_node)

            result = linter.get_results()
            expected = [
                dlint.linters.base.Flake8Result(
                    lineno=3,
                    col_offset=0,
                    message=linter._error_tmpl
                )
            ]

            assert result == expected

    def test_module_attribute_arbitrary_from_import_wildcard_depth_usage_new(self):
        python_strings = [
            """
            from m1 import *
            m2.m3.m4.bad_attribute()
            """,
            """
            from m1.m2 import *
            m3.m4.bad_attribute()
            """,
            """
            from m1.m2.m3 import *
            m4.bad_attribute()
            """,
        ]

        for python_string in python_strings:
            python_node = self.get_ast_node(python_string)

            linter = get_bad_module_attribute_use_implementation({
                'm1.m2.m3.m4': ['bad_attribute'],
            })
            linter.visit(python_node)

            result = linter.get_results()
            expected = [
                dlint.linters.base.Flake8Result(
                    lineno=3,
                    col_offset=0,
                    message=linter._error_tmpl
                )
            ]

            assert result == expected

    def test_module_attribute_usage_nested(self):
        python_node = self.get_ast_node(
            """
            import foo

            var = 'echo "TEST"'

            foo.bar(var).baz()
            """
        )

        linter = get_bad_module_attribute_use_implementation({'foo': ['bar']})
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=linter._error_tmpl
            )
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
