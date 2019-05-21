#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestBadRequestsUse(dlint.test.base.BaseTest):

    def test_bad_requests_usage(self):
        python_string = self.get_ast_node(
            """
            import requests

            requests.request(verify=False)
            requests.get(verify=False)
            requests.options(verify=False)
            requests.head(verify=False)
            requests.post(verify=False)
            requests.put(verify=False)
            requests.patch(verify=False)
            requests.delete(verify=False)
            """
        )

        linter = dlint.linters.BadRequestsUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadRequestsUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=5,
                col_offset=0,
                message=dlint.linters.BadRequestsUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=dlint.linters.BadRequestsUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=0,
                message=dlint.linters.BadRequestsUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=8,
                col_offset=0,
                message=dlint.linters.BadRequestsUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=9,
                col_offset=0,
                message=dlint.linters.BadRequestsUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=10,
                col_offset=0,
                message=dlint.linters.BadRequestsUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=11,
                col_offset=0,
                message=dlint.linters.BadRequestsUseLinter._error_tmpl
            ),
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
