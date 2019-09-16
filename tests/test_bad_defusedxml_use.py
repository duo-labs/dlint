#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestBadDefusedxmlUse(dlint.test.base.BaseTest):

    def test_bad_defusedxml_usage(self):
        python_node = self.get_ast_node(
            """
            import defusedxml.lxml
            import defusedxml.ElementTree
            import defusedxml.cElementTree

            defusedxml.lxml.parse("")
            defusedxml.ElementTree.fromstring("", forbid_entities=False)
            defusedxml.cElementTree.iterparse("", forbid_external=False)
            """
        )

        linter = dlint.linters.BadDefusedxmlUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=dlint.linters.BadDefusedxmlUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=0,
                message=dlint.linters.BadDefusedxmlUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=8,
                col_offset=0,
                message=dlint.linters.BadDefusedxmlUseLinter._error_tmpl
            ),
        ]

        assert result == expected

    def test_bad_defusedxml_from_usage(self):
        python_node = self.get_ast_node(
            """
            from defusedxml.lxml import parse
            from defusedxml.ElementTree import fromstring
            from defusedxml.cElementTree import iterparse

            parse("")
            fromstring("", forbid_entities=False)
            iterparse("", forbid_external=False)
            """
        )

        linter = dlint.linters.BadDefusedxmlUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=dlint.linters.BadDefusedxmlUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=0,
                message=dlint.linters.BadDefusedxmlUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=8,
                col_offset=0,
                message=dlint.linters.BadDefusedxmlUseLinter._error_tmpl
            ),
        ]

        assert result == expected

    def test_defusedxml_avoid_false_positive(self):
        python_node = self.get_ast_node(
            """
            from otherlib1 import parse
            from otherlib2 import fromstring
            from otherlib3 import iterparse

            parse("")
            fromstring("", forbid_entities=False)
            iterparse("", forbid_external=False)
            """
        )

        linter = dlint.linters.BadDefusedxmlUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = []

        assert result == expected


if __name__ == "__main__":
    unittest.main()
