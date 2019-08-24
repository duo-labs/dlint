#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestBadUrllib3KwargUse(dlint.test.base.BaseTest):

    def test_bad_urllib3_kwarg_usage(self):
        python_node = self.get_ast_node(
            """
            import urllib3
            import ssl
            from ssl import CERT_NONE

            urllib3.PoolManager(cert_reqs="CERT_NONE")
            urllib3.ProxyManager(cert_reqs="CERT_NONE")
            urllib3.HTTPSConnectionPool(cert_reqs="NONE")
            urllib3.connection_from_url(cert_reqs=ssl.CERT_NONE)
            urllib3.proxy_from_url(cert_reqs=CERT_NONE)
            """
        )

        linter = dlint.linters.BadUrllib3KwargUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=dlint.linters.BadUrllib3KwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=0,
                message=dlint.linters.BadUrllib3KwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=8,
                col_offset=0,
                message=dlint.linters.BadUrllib3KwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=9,
                col_offset=0,
                message=dlint.linters.BadUrllib3KwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=10,
                col_offset=0,
                message=dlint.linters.BadUrllib3KwargUseLinter._error_tmpl
            ),
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
