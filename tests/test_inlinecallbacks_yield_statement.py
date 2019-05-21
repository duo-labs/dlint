#!/usr/bin/env python

import unittest

import dlint


class TestInlineCallbacksYieldStatement(dlint.test.base.BaseTest):

    def test_empty(self):
        python_string = self.get_ast_node(
            """
            """
        )

        linter = dlint.linters.InlineCallbacksYieldStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_not_inlinecallbacks_decorator(self):
        python_string = self.get_ast_node(
            """
            @other_decorator
            def func(arg):
                return arg
            """
        )

        linter = dlint.linters.InlineCallbacksYieldStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_name_decorator_with_argument(self):
        python_string = self.get_ast_node(
            """
            CONST = 5

            @other_decorator(CONST)
            def func(arg):
                return arg
            """
        )

        linter = dlint.linters.InlineCallbacksYieldStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_attribute_decorator_with_argument(self):
        python_string = self.get_ast_node(
            """
            CONST = 5

            @module.other_decorator(CONST)
            def func(arg):
                return arg
            """
        )

        linter = dlint.linters.InlineCallbacksYieldStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_yield_statement(self):
        python_string = self.get_ast_node(
            """
            from twisted.internet import defer

            @defer.inlineCallbacks
            def func(arg):
                yield 'foo'
                return
            """
        )

        linter = dlint.linters.InlineCallbacksYieldStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_nested_yield_statement(self):
        python_string = self.get_ast_node(
            """
            from twisted.internet import defer

            @defer.inlineCallbacks
            def func(arg):
                if True:
                    for _ in range(10):
                        yield 'foo'
                return
            """
        )

        linter = dlint.linters.InlineCallbacksYieldStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_assign_yield_statement(self):
        python_string = self.get_ast_node(
            """
            from twisted.internet import defer

            @defer.inlineCallbacks
            def func(arg):
                bar = yield foo()
                return
            """
        )

        linter = dlint.linters.InlineCallbacksYieldStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_nested_assign_yield_statement(self):
        python_string = self.get_ast_node(
            """
            from twisted.internet import defer

            @defer.inlineCallbacks
            def func(arg):
                if True:
                    for _ in range(10):
                        bar = yield foo()
                return
            """
        )

        linter = dlint.linters.InlineCallbacksYieldStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_missing_yield_statement(self):
        python_string = self.get_ast_node(
            """
            from twisted.internet import defer

            @defer.inlineCallbacks
            def func(arg):
                return
            """
        )

        linter = dlint.linters.InlineCallbacksYieldStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.InlineCallbacksYieldStatementLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_nested_function_yield_statement(self):
        python_string = self.get_ast_node(
            """
            from twisted.internet import defer

            @defer.inlineCallbacks
            def func(arg):
                if arg:
                    arg += 5

                def inner_func():
                    yield 'foo'

                return
            """
        )

        linter = dlint.linters.InlineCallbacksYieldStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.InlineCallbacksYieldStatementLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_nested_class_yield_statement(self):
        python_string = self.get_ast_node(
            """
            from twisted.internet import defer

            @defer.inlineCallbacks
            def func(arg):
                if arg:
                    arg += 5

                class Foo(object):
                    def bar(self):
                        yield 'baz'

                return
            """
        )

        linter = dlint.linters.InlineCallbacksYieldStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.InlineCallbacksYieldStatementLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_nested_function_missing_yield_statement(self):
        python_string = self.get_ast_node(
            """
            from twisted.internet import defer

            def func(arg):
                if arg:
                    arg += 5

                @defer.inlineCallbacks
                def inner_func():
                    return

                yield 'foo'
                return
            """
        )

        linter = dlint.linters.InlineCallbacksYieldStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=8,
                col_offset=4,
                message=dlint.linters.InlineCallbacksYieldStatementLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_only_raise_statement(self):
        python_string = self.get_ast_node(
            """
            from twisted.internet import defer

            @defer.inlineCallbacks
            def func(arg):
                raise NotImplementedError()
            """
        )

        linter = dlint.linters.InlineCallbacksYieldStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_multiple_raise_statements(self):
        python_string = self.get_ast_node(
            """
            from twisted.internet import defer

            @defer.inlineCallbacks
            def func(arg):
                raise errors.ApiException(errors.FORBIDDEN)
                raise errors.ApiException(errors.MISSING)
            """
        )

        linter = dlint.linters.InlineCallbacksYieldStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_only_pass_statement(self):
        python_string = self.get_ast_node(
            """
            from twisted.internet import defer

            @defer.inlineCallbacks
            def func(arg):
                pass
            """
        )

        linter = dlint.linters.InlineCallbacksYieldStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_raise_statement_with_docstring(self):
        python_string = self.get_ast_node(
            """
            from twisted.internet import defer

            @defer.inlineCallbacks
            def func(arg):
                '''Foo
                '''
                raise NotImplementedError()
            """
        )

        linter = dlint.linters.InlineCallbacksYieldStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_raise_with_missing_yield(self):
        python_string = self.get_ast_node(
            """
            from twisted.internet import defer

            @defer.inlineCallbacks
            def func(arg):
                if True:
                    raise NotImplementedError()
                return
            """
        )

        linter = dlint.linters.InlineCallbacksYieldStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.InlineCallbacksYieldStatementLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_raise_with_yield(self):
        python_string = self.get_ast_node(
            """
            from twisted.internet import defer

            @defer.inlineCallbacks
            def func(arg):
                if True:
                    raise NotImplementedError()
                yield 'foo'
                return
            """
        )

        linter = dlint.linters.InlineCallbacksYieldStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected


if __name__ == "__main__":
    unittest.main()
