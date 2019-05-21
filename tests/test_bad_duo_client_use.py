#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestBadDuoClientUse(dlint.test.base.BaseTest):

    def test_bad_duo_client_usage(self):
        python_string = self.get_ast_node(
            """
            import duo_client

            duo_client.Client(ca_certs="HTTP")
            duo_client.Client(ca_certs="DISABLE")
            duo_client.AsyncDuoClient(ca_certs="HTTP")
            duo_client.AsyncDuoClient(ca_certs="DISABLE")
            duo_client.Auth(ca_certs="HTTP")
            duo_client.Auth(ca_certs="DISABLE")
            duo_client.AuthAPI(ca_certs="HTTP")
            duo_client.AuthAPI(ca_certs="DISABLE")
            duo_client.Admin(ca_certs="HTTP")
            duo_client.Admin(ca_certs="DISABLE")
            duo_client.AdminAPI(ca_certs="HTTP")
            duo_client.AdminAPI(ca_certs="DISABLE")
            duo_client.Accounts(ca_certs="HTTP")
            duo_client.Accounts(ca_certs="DISABLE")
            duo_client.AccountsAPI(ca_certs="HTTP")
            duo_client.AccountsAPI(ca_certs="DISABLE")
            """
        )

        linter = dlint.linters.BadDuoClientUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadDuoClientUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=5,
                col_offset=0,
                message=dlint.linters.BadDuoClientUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=dlint.linters.BadDuoClientUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=0,
                message=dlint.linters.BadDuoClientUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=8,
                col_offset=0,
                message=dlint.linters.BadDuoClientUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=9,
                col_offset=0,
                message=dlint.linters.BadDuoClientUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=10,
                col_offset=0,
                message=dlint.linters.BadDuoClientUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=11,
                col_offset=0,
                message=dlint.linters.BadDuoClientUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=12,
                col_offset=0,
                message=dlint.linters.BadDuoClientUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=13,
                col_offset=0,
                message=dlint.linters.BadDuoClientUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=14,
                col_offset=0,
                message=dlint.linters.BadDuoClientUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=15,
                col_offset=0,
                message=dlint.linters.BadDuoClientUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=16,
                col_offset=0,
                message=dlint.linters.BadDuoClientUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=17,
                col_offset=0,
                message=dlint.linters.BadDuoClientUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=18,
                col_offset=0,
                message=dlint.linters.BadDuoClientUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=19,
                col_offset=0,
                message=dlint.linters.BadDuoClientUseLinter._error_tmpl
            ),
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
