#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestBadPickleUse(dlint.test.base.BaseTest):

    def test_bad_pickle_usage(self):
        python_string = self.get_ast_node(
            """
            import pickle

            var = 'test'

            pickle.loads(var)

            with open('data.pickle', 'r') as f:
                pickle.load(f)
                up = pickle.Unpickler(f)
                up.load()
            """
        )

        linter = dlint.linters.BadPickleUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=dlint.linters.BadPickleUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=9,
                col_offset=4,
                message=dlint.linters.BadPickleUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=10,
                col_offset=9,
                message=dlint.linters.BadPickleUseLinter._error_tmpl
            )
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
