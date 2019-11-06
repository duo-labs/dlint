#!/usr/bin/env python

import sys
import unittest

import dlint

IS_PYTHON_3_8 = sys.version_info >= (3, 8)


class TestReturnValueInlineCallbacks(dlint.test.base.BaseTest):

    def test_empty(self):
        python_node = self.get_ast_node(
            """
            """
        )

        linter = dlint.linters.ReturnValueInInlineCallbacksLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_not_inlinecallbacks_decorator(self):
        python_node = self.get_ast_node(
            """
            from twisted.internet import defer

            @other_decorator
            def func(arg):
                defer.returnValue(arg)
            """
        )

        linter = dlint.linters.ReturnValueInInlineCallbacksLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=5 if IS_PYTHON_3_8 else 4,
                col_offset=0,
                message=dlint.linters.ReturnValueInInlineCallbacksLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_name_decorator_with_argument(self):
        python_node = self.get_ast_node(
            """
            from twisted.internet import defer

            CONST = 5

            @other_decorator(CONST)
            def func(arg):
                defer.returnValue(arg)
            """
        )

        linter = dlint.linters.ReturnValueInInlineCallbacksLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=7 if IS_PYTHON_3_8 else 6,
                col_offset=0,
                message=dlint.linters.ReturnValueInInlineCallbacksLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_attribute_decorator_with_argument(self):
        python_node = self.get_ast_node(
            """
            from twisted.internet import defer

            CONST = 5

            @module.other_decorator(CONST)
            def func(arg):
                defer.returnValue(arg)
            """
        )

        linter = dlint.linters.ReturnValueInInlineCallbacksLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=7 if IS_PYTHON_3_8 else 6,
                col_offset=0,
                message=dlint.linters.ReturnValueInInlineCallbacksLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_returnvalue_statement(self):
        python_node = self.get_ast_node(
            """
            from twisted.internet import defer

            @defer.inlineCallbacks
            def func(arg):
                yield 'foo'
                defer.returnValue('foo')
            """
        )

        linter = dlint.linters.ReturnValueInInlineCallbacksLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_returnvalue_statement_with_weird_calls(self):
        python_node = self.get_ast_node(
            """
            from twisted.internet import defer

            def func(arg):
                foo(argument).bar()
                foo(argument).bar()()
                defer.returnValue('foo')
            """
        )

        linter = dlint.linters.ReturnValueInInlineCallbacksLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.ReturnValueInInlineCallbacksLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_returnvalue_name_statement(self):
        python_node = self.get_ast_node(
            """
            from twisted.internet.defer import inlineCallbacks, returnValue

            @inlineCallbacks
            def func(arg):
                yield 'foo'
                returnValue('foo')
            """
        )

        linter = dlint.linters.ReturnValueInInlineCallbacksLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_nested_yield_statement(self):
        python_node = self.get_ast_node(
            """
            from twisted.internet import defer

            @defer.inlineCallbacks
            def func(arg):
                if True:
                    for _ in range(10):
                        defer.returnValue('foo')
            """
        )

        linter = dlint.linters.ReturnValueInInlineCallbacksLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_missing_inlinecallbacks_decorator(self):
        python_node = self.get_ast_node(
            """
            from twisted.internet import defer

            def func(arg):
                foo = yield bar()
                defer.returnValue('baz')
            """
        )

        linter = dlint.linters.ReturnValueInInlineCallbacksLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.ReturnValueInInlineCallbacksLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_function_with_nested_missing_inlinecallbacks_decorator(self):
        python_node = self.get_ast_node(
            """
            from twisted.internet import defer

            def func(arg):
                if arg:
                    arg += 5

                @defer.inlineCallbacks
                def inner_func():
                    defer.returnValue('foo')

                defer.returnValue('qux')
            """
        )

        linter = dlint.linters.ReturnValueInInlineCallbacksLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.ReturnValueInInlineCallbacksLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_regular_function_with_nested_missing_inlinecallbacks_decorator(self):
        python_node = self.get_ast_node(
            """
            from twisted.internet import defer

            def func(arg):
                if arg:
                    arg += 5

                def inner_func():
                    return 'foo'

                defer.returnValue('qux')
            """
        )

        linter = dlint.linters.ReturnValueInInlineCallbacksLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.ReturnValueInInlineCallbacksLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_nested_function_missing_inlinecallbacks_decorator(self):
        python_node = self.get_ast_node(
            """
            from twisted.internet import defer

            def func(arg):
                if arg:
                    arg += 5

                def inner_func():
                    defer.returnValue('qux')

                return 'foo'
            """
        )

        linter = dlint.linters.ReturnValueInInlineCallbacksLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=8,
                col_offset=4,
                message=dlint.linters.ReturnValueInInlineCallbacksLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_nested_class_missing_inlinecallbacks_decorator(self):
        python_node = self.get_ast_node(
            """
            from twisted.internet import defer

            def func(arg):
                if arg:
                    arg += 5

                class Foo(object):
                    @defer.inlineCallbacks
                    def bar(self):
                        defer.returnValue('baz')

                defer.returnValue('qux')
            """
        )

        linter = dlint.linters.ReturnValueInInlineCallbacksLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.ReturnValueInInlineCallbacksLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_nested_regular_class_missing_inlinecallbacks_decorator(self):
        python_node = self.get_ast_node(
            """
            from twisted.internet import defer

            def func(arg):
                if arg:
                    arg += 5

                class Foo(object):
                    def bar(self):
                        return 'baz'

                defer.returnValue('qux')
            """
        )

        linter = dlint.linters.ReturnValueInInlineCallbacksLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.ReturnValueInInlineCallbacksLinter._error_tmpl
            )
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
