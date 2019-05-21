#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import ast
import sys

from . import base
from .. import tree


class YieldReturnStatementLinter(base.BaseLinter):
    """This linter looks for inlineCallbacks functions that have
    non-empty return statements. Using a non-empty return statement and a
    yield statement in the same function is a syntax error.
    """
    off_by_default = False

    _code = 'DUO101'
    _error_tmpl = 'DUO101 inlineCallbacks function cannot have non-empty return statement'

    def visit_FunctionDef(self, node):
        self.generic_visit(node)

        # https://twistedmatrix.com/documents/17.1.0/api/twisted.internet.defer.inlineCallbacks.html
        is_python_3_3 = sys.version_info >= (3, 3)

        if (is_python_3_3
                or not tree.function_has_inlinecallbacks_decorator(node)):
            return

        results = []

        def return_statement_callback(inner_node):
            if isinstance(inner_node, ast.Return) and tree.non_empty_return(inner_node):
                results.append(inner_node)

        tree.walk_callback_same_scope(node, return_statement_callback)

        self.results.extend([
            base.Flake8Result(
                lineno=result.lineno,
                col_offset=result.col_offset,
                message=self._error_tmpl
            )
            for result in results
        ])
