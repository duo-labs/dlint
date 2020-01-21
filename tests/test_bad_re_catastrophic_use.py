#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import itertools
import sys
import unittest

import dlint

IS_PYTHON_3_7 = sys.version_info >= (3, 7)


class TestBadReCatastrophicUse(dlint.test.base.BaseTest):

    def test_bad_re_catastrophic_usage(self):
        python_node = self.get_ast_node(
            """
            import re

            re.compile('(a+)+b')
            re.search('(a+)+b')
            re.match('(a+)+b')
            re.fullmatch('(a+)+b')
            re.split('(a+)+b')
            re.findall('(a+)+b')
            re.finditer('(a+)+b')
            re.sub('(a+)+b')
            re.subn('(a+)+b')
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=5,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=8,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=9,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=10,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=11,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=12,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            ),
        ]

        assert result == expected

    def test_bad_re_catastrophic_usage_from_import(self):
        python_node = self.get_ast_node(
            """
            from re import compile, search, match, fullmatch, split, findall, finditer, sub, subn

            compile('(a+)+b')
            search('(a+)+b')
            match('(a+)+b')
            fullmatch('(a+)+b')
            split('(a+)+b')
            findall('(a+)+b')
            finditer('(a+)+b')
            sub('(a+)+b')
            subn('(a+)+b')
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=5,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=8,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=9,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=10,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=11,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=12,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            ),
        ]

        assert result == expected

    def test_bad_re_catastrophic_usage_django(self):
        python_node = self.get_ast_node(
            """
            import django

            django.core.validators.RegexValidator('(a+)+b')
            django.urls.re_path('(a+)+b')
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=5,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            ),
        ]

        assert result == expected

    def test_bad_re_catastrophic_usage_from_import_django(self):
        python_node = self.get_ast_node(
            """
            from django.core.validators import RegexValidator
            from django.urls import re_path

            RegexValidator('(a+)+b')
            re_path('(a+)+b')
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=5,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            ),
        ]

        assert result == expected

    def get_individual_result(self, python_code):
        python_node = self.get_ast_node(python_code)

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)
        results = linter.get_results()

        if len(results) > 1:
            raise Exception("too many results found - len={}".format(len(results)))

        return results[0]

    def test_bad_re_nested_quantifiers(self):
        qualifiers = [
            "+",
            "+?",
            "*",
            "*?",
            "{1,10}",
            "{1,10}?",
            "{10}",
            "{10}?",
            "{,10}",
            "{,10}?",
            "{10,}",
            "{10,}?",
        ]
        fmt = (
            """
            import re
            re.search('(a{}){}b')
            """
        )
        cases = [
            fmt.format(*case)
            for case in itertools.permutations(qualifiers, 2)
        ]
        result = [self.get_individual_result(case) for case in cases]
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=3,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            )
        ] * len(cases)

        assert result == expected

    def test_bad_re_catastrophic_adjacent_quantifier_ok(self):
        python_node = self.get_ast_node(
            """
            import re

            re.search('[abc]+[def]*')
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_bad_re_catastrophic_diagonal_quantifier_ok(self):
        python_node = self.get_ast_node(
            """
            import re

            re.search('[abc]+([def]*)')
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_bad_re_catastrophic_nested_quantifier_alternation_any_overlap(self):
        python_node = self.get_ast_node(
            """
            import re

            re.search('(.|[a-c])+')
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_bad_re_catastrophic_nested_quantifier_alternation_literal_overlap(self):
        python_node = self.get_ast_node(
            """
            import re

            re.search('(a|[a-c])+')
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()

        # sre_parse optimization nullifies this alternation check in Python 3.7+
        expected = [] if IS_PYTHON_3_7 else [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_bad_re_catastrophic_nested_quantifier_alternation_literal_no_overlap(self):
        python_node = self.get_ast_node(
            """
            import re

            re.search('(d|[a-c])+')
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_bad_re_catastrophic_nested_quantifier_alternation_not_literal_overlap(self):
        python_node = self.get_ast_node(
            """
            import re

            re.search('([^d]|[a-c])+')
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_bad_re_catastrophic_nested_quantifier_alternation_not_literal_incomplete_overlap(self):
        python_node = self.get_ast_node(
            """
            import re

            re.search('([^b]|[a-c])+')
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_bad_re_catastrophic_nested_quantifier_alternation_not_literal_no_overlap(self):
        python_node = self.get_ast_node(
            """
            import re

            re.search('([^a]|a)+')
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_bad_re_catastrophic_nested_quantifier_alternation_multiple_not_literal_overlap(self):
        python_node = self.get_ast_node(
            """
            import re

            re.search('([^d]|[^b]|[a-c])+')
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_bad_re_catastrophic_nested_quantifier_alternation_multiple_negate_literal_no_overlap(self):
        python_node = self.get_ast_node(
            """
            import re

            re.search('([^abcABC]|[a-c]|[A-C])+')
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_bad_re_catastrophic_nested_quantifier_alternation_multiple_negate_literal_overlap(self):
        python_node = self.get_ast_node(
            """
            import re

            re.search('([^abcAB]|[a-c]|[A-C])+')
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_bad_re_catastrophic_nested_quantifier_alternation_range_overlap(self):
        python_node = self.get_ast_node(
            """
            import re

            re.search('([a-c]|[c-e])+')
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()

        # sre_parse optimization nullifies this alternation check in Python 3.7+
        expected = [] if IS_PYTHON_3_7 else [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_bad_re_catastrophic_nested_quantifier_alternation_range_no_overlap(self):
        python_node = self.get_ast_node(
            """
            import re

            re.search('([a-c]|[d-e])+')
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_bad_re_catastrophic_nested_quantifier_alternation_range_literals_no_overlap(self):
        python_node = self.get_ast_node(
            """
            import re

            re.search('([a-c]|[def])+')
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_bad_re_catastrophic_nested_quantifier_alternation_ranges_no_overlap(self):
        python_node = self.get_ast_node(
            """
            import re

            re.search('([a-c]|[^a-c])+')
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_bad_re_catastrophic_nested_quantifier_alternation_category_overlap(self):
        python_node = self.get_ast_node(
            r"""
            import re

            re.search('(\\w|[a-c])+')
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()

        # sre_parse optimization nullifies this alternation check in Python 3.7+
        expected = [] if IS_PYTHON_3_7 else [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_bad_re_catastrophic_nested_quantifier_alternation_not_category_overlap(self):
        python_node = self.get_ast_node(
            r"""
            import re

            re.search('(\\S|[a-c])+')
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()

        # sre_parse optimization nullifies this alternation check in Python 3.7+
        expected = [] if IS_PYTHON_3_7 else [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_bad_re_catastrophic_nested_quantifier_alternation_digit_category_overlap(self):
        python_node = self.get_ast_node(
            r"""
            import re

            re.search('(\\d|123)+')
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_bad_re_catastrophic_nested_quantifier_alternation_negate_category_overlap(self):
        python_node = self.get_ast_node(
            r"""
            import re

            re.search('([^\\W]|[a-c])+')
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadReCatastrophicUseLinter._error_tmpl
            )
        ]

        assert result == expected

    def test_bad_re_catastrophic_nested_quantifier_alternation_small_repeat(self):
        python_node = self.get_ast_node(
            r"""
            import re

            re.search('(a|a)?b')
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_bad_re_catastrophic_groupref_detection(self):
        python_node = self.get_ast_node(
            """
            import re

            re.search('(?P<name>[foo])(?(name)yes|no)')
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_bad_re_catastrophic_not_literal_string(self):
        python_node = self.get_ast_node(
            """
            import re

            s = 'test'
            re.search(s)
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_bad_re_catastrophic_missing_argument(self):
        python_node = self.get_ast_node(
            """
            import re

            re.search()
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = []

        assert result == expected

    def test_bad_re_catastrophic_malformed_expression(self):
        python_node = self.get_ast_node(
            """
            import re

            re.search('(foo')
            """
        )

        linter = dlint.linters.BadReCatastrophicUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = []

        assert result == expected


if __name__ == "__main__":
    unittest.main()
