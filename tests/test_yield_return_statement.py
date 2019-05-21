#!/usr/bin/env python

import sys
import unittest

import dlint

IS_PYTHON_3_3 = sys.version_info >= (3, 3)


class TestYieldReturnStatement(dlint.test.base.BaseTest):

    def test_empty(self):
        python_string = self.get_ast_node(
            """
            """
        )

        linter = dlint.linters.YieldReturnStatementLinter()
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

        linter = dlint.linters.YieldReturnStatementLinter()
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

        linter = dlint.linters.YieldReturnStatementLinter()
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

        linter = dlint.linters.YieldReturnStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_none_return_statement(self):
        python_string = self.get_ast_node(
            """
            from twisted.internet import defer

            @defer.inlineCallbacks
            def func(arg):
                return None
            """
        )

        linter = dlint.linters.YieldReturnStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [] if IS_PYTHON_3_3 else [
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=4,
                message=dlint.linters.YieldReturnStatementLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_empty_return_statement(self):
        python_string = self.get_ast_node(
            """
            from twisted.internet import defer

            @defer.inlineCallbacks
            def func(arg):
                return
            """
        )

        linter = dlint.linters.YieldReturnStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_non_empty_return_statement(self):
        python_string = self.get_ast_node(
            """
            from twisted.internet import defer

            @defer.inlineCallbacks
            def func(arg):
                return arg
            """
        )

        linter = dlint.linters.YieldReturnStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [] if IS_PYTHON_3_3 else [
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=4,
                message=dlint.linters.YieldReturnStatementLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_multiple_return_statement(self):
        python_string = self.get_ast_node(
            """
            from twisted.internet import defer

            @defer.inlineCallbacks
            def func(arg):
                if condition:
                    return

                if arg > 10:
                    return
                else:
                    return arg
            """
        )

        linter = dlint.linters.YieldReturnStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [] if IS_PYTHON_3_3 else [
            dlint.linters.base.Flake8Result(
                lineno=12,
                col_offset=8,
                message=dlint.linters.YieldReturnStatementLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_nested_function_return_statement(self):
        python_string = self.get_ast_node(
            """
            from twisted.internet import defer

            @defer.inlineCallbacks
            def func(arg):
                if arg:
                    arg += 5

                def inner_func():
                    return arg

                return
            """
        )

        linter = dlint.linters.YieldReturnStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_nested_function_non_empty_return_statement(self):
        python_string = self.get_ast_node(
            """
            from twisted.internet import defer

            def func(arg):
                if arg:
                    arg += 5

                @defer.inlineCallbacks
                def inner_func():
                    return arg

                return
            """
        )

        linter = dlint.linters.YieldReturnStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [] if IS_PYTHON_3_3 else [
            dlint.linters.base.Flake8Result(
                lineno=10,
                col_offset=8,
                message=dlint.linters.YieldReturnStatementLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_nested_class_return_statement(self):
        python_string = self.get_ast_node(
            """
            from twisted.internet import defer

            @defer.inlineCallbacks
            def func(arg):
                if arg:
                    arg += 5

                class inner_class:
                    def inner_func():
                        return arg

                return
            """
        )

        linter = dlint.linters.YieldReturnStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_short_import(self):
        python_string = self.get_ast_node(
            """
            import twisted

            @twisted.internet.defer.inlineCallbacks
            def func(arg):
                return arg
            """
        )

        linter = dlint.linters.YieldReturnStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [] if IS_PYTHON_3_3 else [
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=4,
                message=dlint.linters.YieldReturnStatementLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_long_import(self):
        python_string = self.get_ast_node(
            """
            from twisted.internet.defer import inlineCallbacks

            @inlineCallbacks
            def func(arg):
                return arg
            """
        )

        linter = dlint.linters.YieldReturnStatementLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [] if IS_PYTHON_3_3 else [
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=4,
                message=dlint.linters.YieldReturnStatementLinter._error_tmpl
            )
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
