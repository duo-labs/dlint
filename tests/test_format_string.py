#!/usr/bin/env python

import unittest

import dlint


class TestFormatString(dlint.test.base.BaseTest):

    def test_empty(self):
        python_string = self.get_ast_node(
            """
            """
        )

        linter = dlint.linters.FormatStringLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected


if __name__ == "__main__":
    unittest.main()
