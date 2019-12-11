#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestBadItsDangerousKwargUse(dlint.test.base.BaseTest):

    def test_bad_itsdangerous_kwarg_usage(self):
        python_node = self.get_ast_node(
            """
            import itsdangerous

            itsdangerous.signer.Signer("key", algorithm=itsdangerous.signer.NoneAlgorithm())
            itsdangerous.signer.Signer("key", algorithm=itsdangerous.NoneAlgorithm())
            itsdangerous.Signer("key", algorithm=itsdangerous.NoneAlgorithm())
            itsdangerous.Signer("key", algorithm=itsdangerous.signer.NoneAlgorithm())

            itsdangerous.timed.TimestampSigner("key", algorithm=itsdangerous.signer.NoneAlgorithm())
            itsdangerous.timed.TimestampSigner("key", algorithm=itsdangerous.NoneAlgorithm())
            itsdangerous.TimestampSigner("key", algorithm=itsdangerous.NoneAlgorithm())
            itsdangerous.TimestampSigner("key", algorithm=itsdangerous.signer.NoneAlgorithm())

            itsdangerous.jws.JSONWebSignatureSerializer("key", algorithm_name="none")
            itsdangerous.JSONWebSignatureSerializer("key", algorithm_name="none")
            """
        )

        linter = dlint.linters.BadItsDangerousKwargUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadItsDangerousKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=5,
                col_offset=0,
                message=dlint.linters.BadItsDangerousKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=dlint.linters.BadItsDangerousKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=0,
                message=dlint.linters.BadItsDangerousKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=9,
                col_offset=0,
                message=dlint.linters.BadItsDangerousKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=10,
                col_offset=0,
                message=dlint.linters.BadItsDangerousKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=11,
                col_offset=0,
                message=dlint.linters.BadItsDangerousKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=12,
                col_offset=0,
                message=dlint.linters.BadItsDangerousKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=14,
                col_offset=0,
                message=dlint.linters.BadItsDangerousKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=15,
                col_offset=0,
                message=dlint.linters.BadItsDangerousKwargUseLinter._error_tmpl
            ),
        ]

        assert result == expected

    def test_missing_algorithm_name(self):
        python_node = self.get_ast_node(
            """
            from itsdangerous import JSONWebSignatureSerializer as Serializer

            serializer = Serializer(app.config['SECRET_KEY'])
            """
        )

        linter = dlint.linters.BadItsDangerousKwargUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = []

        assert result == expected


if __name__ == "__main__":
    unittest.main()
