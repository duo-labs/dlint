#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


def get_bad_name_attribute_use_implementation(illegal_name_attributes):
    class Cls(dlint.linters.helpers.bad_name_attribute_use.BadNameAttributeUseLinter):
        _code = 'DUOXXX'
        _error_tmpl = 'DUOXXX error message'

        @property
        def illegal_name_attributes(self):
            return illegal_name_attributes

    return Cls()


class TestBadNameAttributeUse(dlint.test.base.BaseTest):

    def test_empty_code(self):
        python_string = self.get_ast_node(
            """
            """
        )

        linter = get_bad_name_attribute_use_implementation(
            {
                'foo': [
                    ['bar', 'Baz'],
                ],
            }
        )
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_empty_illegal_name_attributes(self):
        python_string = self.get_ast_node(
            """
            import os

            var = 'test'

            os.path.join(var)
            """
        )

        linter = get_bad_name_attribute_use_implementation({})
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_bad_name_attributes_basic(self):
        python_string = self.get_ast_node(
            """
            import bar

            def func():
                obj = bar.Baz()
                return obj.foo()
            """
        )

        linter = get_bad_name_attribute_use_implementation(
            {
                'foo': [
                    ['bar', 'Baz'],
                ],
            }
        )
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=11,
                message=linter._error_tmpl
            )
        ]

        assert result == expected

    def test_bad_name_attributes_nested(self):
        python_string = self.get_ast_node(
            """
            import bar

            def func():
                def inner_func():
                    obj = bar.Baz()
                    return obj.foo()
            return
            """
        )

        linter = get_bad_name_attribute_use_implementation(
            {
                'foo': [
                    ['bar', 'Baz'],
                ],
            }
        )
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=15,
                message=linter._error_tmpl
            )
        ]

        assert result == expected

    def test_bad_name_attributes_nested_overwrite(self):
        python_string = self.get_ast_node(
            """
            import bar

            def func():
                obj = bar.Qux()

                def inner_func():
                    obj = bar.Baz()

                return obj.foo()
            """
        )

        linter = get_bad_name_attribute_use_implementation(
            {
                'foo': [
                    ['bar', 'Baz'],
                ],
            }
        )
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_bad_name_attributes_multiple_findings(self):
        python_string = self.get_ast_node(
            """
            import bar

            def func():
                obj = bar.Baz()

                result1 = obj.foo('test1')
                result2 = obj.foo('test2')

                return
            """
        )

        linter = get_bad_name_attribute_use_implementation(
            {
                'foo': [
                    ['bar', 'Baz'],
                ],
            }
        )
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=14,
                message=linter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=8,
                col_offset=14,
                message=linter._error_tmpl
            ),
        ]

        assert result == expected

    def test_bad_name_attributes_multiple_attributes(self):
        python_string = self.get_ast_node(
            """
            import bar

            def func():
                obj1 = bar.Baz()
                obj2 = bar.class_method()

                result1 = obj1.foo('test1')
                result2 = obj2.foo('test2')

                return
            """
        )

        linter = get_bad_name_attribute_use_implementation(
            {
                'foo': [
                    ['bar', 'Baz'],
                    ['bar', 'class_method'],
                ],
            }
        )
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=8,
                col_offset=14,
                message=linter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=9,
                col_offset=14,
                message=linter._error_tmpl
            ),
        ]

        assert result == expected

    def test_bad_name_attributes_overwrite(self):
        python_string = self.get_ast_node(
            """
            import bar

            def func():
                obj1 = bar.Baz()
                obj1 = bar.Qux()

                return obj1.foo()
            """
        )

        linter = get_bad_name_attribute_use_implementation(
            {
                'foo': [
                    ['bar', 'Baz'],
                ],
            }
        )
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_bad_name_attributes_no_module(self):
        python_string = self.get_ast_node(
            """
            from bar import Baz

            def func():
                obj = Baz()
                return obj.foo()
            """
        )

        linter = get_bad_name_attribute_use_implementation(
            {
                'foo': [
                    ['Baz'],
                ],
            }
        )
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=11,
                message=linter._error_tmpl
            )
        ]

        assert result == expected

    def test_bad_name_attributes_multiple_attribute_calls(self):
        python_string = self.get_ast_node(
            """
            import bar

            def func():
                obj = bar.Baz()
                ret1 = obj.foo()
                ret2 = obj.qux()
                return
            """
        )

        linter = get_bad_name_attribute_use_implementation(
            {
                'foo': [
                    ['bar', 'Baz'],
                ],
                'qux': [
                    ['bar', 'Baz'],
                ],
            }
        )
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=11,
                message=linter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=11,
                message=linter._error_tmpl
            )
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
