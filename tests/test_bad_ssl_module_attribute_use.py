#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestBadSSLModuleAttributeUse(dlint.test.base.BaseTest):

    def test_bad_ssl_usage(self):
        python_string = self.get_ast_node(
            """
            import ssl

            ssl._create_unverified_context()
            ssl._https_verify_certificates()
            ssl.CERT_NONE
            ssl.CERT_OPTIONAL
            ssl.PROTOCOL_SSLv2
            ssl.PROTOCOL_SSLv23
            ssl.PROTOCOL_SSLv3
            ssl.PROTOCOL_TLS
            """
        )

        linter = dlint.linters.BadSSLModuleAttributeUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadSSLModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=5,
                col_offset=0,
                message=dlint.linters.BadSSLModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=dlint.linters.BadSSLModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=0,
                message=dlint.linters.BadSSLModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=8,
                col_offset=0,
                message=dlint.linters.BadSSLModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=9,
                col_offset=0,
                message=dlint.linters.BadSSLModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=10,
                col_offset=0,
                message=dlint.linters.BadSSLModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=11,
                col_offset=0,
                message=dlint.linters.BadSSLModuleAttributeUseLinter._error_tmpl
            ),
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
