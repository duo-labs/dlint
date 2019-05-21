#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestBadRandomGeneratorUse(dlint.test.base.BaseTest):

    def test_empty(self):
        python_string = self.get_ast_node(
            """
            """
        )

        linter = dlint.linters.BadRandomGeneratorUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_good_import(self):
        python_string = self.get_ast_node(
            """
            import random

            _generator = random.SystemRandom()

            var1 = _generator.randint(256)
            var2 = random.SystemRandom().randint(256)
            """
        )

        linter = dlint.linters.BadRandomGeneratorUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_good_from_import(self):
        python_string = self.get_ast_node(
            """
            from random import SystemRandom

            _generator = SystemRandom()

            var1 = _generator.randint(256)
            var2 = SystemRandom().randint(256)
            """
        )

        linter = dlint.linters.BadRandomGeneratorUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_bad_attribute_usage(self):
        python_string = self.get_ast_node(
            """
            import random

            var = random.random()
            """
        )

        linter = dlint.linters.BadRandomGeneratorUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=6,
                message=dlint.linters.BadRandomGeneratorUseLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_bad_attribute_usage_with_good_usage(self):
        python_string = self.get_ast_node(
            """
            import random

            _generator = random.SystemRandom()

            var1 = _generator.randint(256)
            var2 = random.randint(256)
            """
        )

        linter = dlint.linters.BadRandomGeneratorUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=7,
                message=dlint.linters.BadRandomGeneratorUseLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_bad_from_import(self):
        python_string = self.get_ast_node(
            """
            from random import random
            """
        )

        linter = dlint.linters.BadRandomGeneratorUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=2,
                col_offset=0,
                message=dlint.linters.BadRandomGeneratorUseLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_bad_from_import_with_good_import(self):
        python_string = self.get_ast_node(
            """
            from random import SystemRandom, random
            """
        )

        linter = dlint.linters.BadRandomGeneratorUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=2,
                col_offset=0,
                message=dlint.linters.BadRandomGeneratorUseLinter._error_tmpl
            )
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
