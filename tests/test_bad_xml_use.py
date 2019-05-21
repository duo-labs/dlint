#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestBadXMLUse(dlint.test.base.BaseTest):

    def test_xml_import_usage(self):
        python_string = self.get_ast_node(
            """
            import xml
            import xmlrpclib
            import lxml
            """
        )

        linter = dlint.linters.BadXMLUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=2,
                col_offset=0,
                message=dlint.linters.BadXMLUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=3,
                col_offset=0,
                message=dlint.linters.BadXMLUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadXMLUseLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_saxutils_import_usage(self):
        python_string = self.get_ast_node(
            """
            import xml.sax.saxutils
            from xml.sax import saxutils
            """
        )

        linter = dlint.linters.BadXMLUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_defused_lxml_usage(self):
        python_string = self.get_ast_node(
            """
            from defusedxml import lxml
            """
        )

        linter = dlint.linters.BadXMLUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected


if __name__ == "__main__":
    unittest.main()
