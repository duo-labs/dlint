#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestBadUrllib3ModuleAttributeUse(dlint.test.base.BaseTest):

    def test_bad_urllib3_module_attribute_usage(self):
        python_node = self.get_ast_node(
            """
            import urllib3
            urllib3.disable_warnings()
            """
        )

        linter = dlint.linters.BadUrllib3ModuleAttributeUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=3,
                col_offset=0,
                message=dlint.linters.BadUrllib3ModuleAttributeUseLinter._error_tmpl
            ),
        ]

        assert result == expected

    def test_bad_urllib3_module_attribute_usage_from_import(self):
        python_node = self.get_ast_node(
            """
            from urllib3 import disable_warnings
            disable_warnings()
            """
        )

        linter = dlint.linters.BadUrllib3ModuleAttributeUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=3,
                col_offset=0,
                message=dlint.linters.BadUrllib3ModuleAttributeUseLinter._error_tmpl
            ),
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
