#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestBadXmlrpcUse(dlint.test.base.BaseTest):

    def test_bad_xmlrpc_usage(self):
        python_string = self.get_ast_node(
            """
            import SimpleXMLRPCServer

            SimpleXMLRPCServer.register_instance(allow_dotted_names=True)
            """
        )

        linter = dlint.linters.BadXmlrpcUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadXmlrpcUseLinter._error_tmpl
            ),
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
