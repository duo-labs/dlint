#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestBadYAMLUse(dlint.test.base.BaseTest):

    def test_bad_yaml_usage(self):
        python_string = self.get_ast_node(
            """
            import yaml

            var1 = {'foo': 'bar'}
            var2 = 'test: !!python/object/apply:print ["HAI"]'

            yaml.dump(var1)
            yaml.dump_all([var1])

            yaml.load(var2)
            yaml.load_all(var2)
            """
        )

        linter = dlint.linters.BadYAMLUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=0,
                message=dlint.linters.BadYAMLUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=8,
                col_offset=0,
                message=dlint.linters.BadYAMLUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=10,
                col_offset=0,
                message=dlint.linters.BadYAMLUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=11,
                col_offset=0,
                message=dlint.linters.BadYAMLUseLinter._error_tmpl
            ),
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
