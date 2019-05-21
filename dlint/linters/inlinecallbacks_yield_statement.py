#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import ast

from . import base
from .. import tree


class InlineCallbacksYieldStatementLinter(base.BaseLinter):
    """This linter looks for inlineCallbacks functions that are missing a
    yield statement. The presence of a yield statement turns a normal function
    into a generator. The inlineCallback generator depends on this behavior,
    so let's check for cases where it's missing.
    """
    off_by_default = False

    _code = 'DUO113'
    _error_tmpl = 'DUO113 inlineCallbacks function missing yield statement'

    def visit_FunctionDef(self, node):
        self.generic_visit(node)

        if not tree.function_has_inlinecallbacks_decorator(node):
            return

        if tree.function_is_empty(node):
            return

        results = []

        def yield_statement_callback(inner_node):
            if isinstance(inner_node, ast.Yield):
                results.append(inner_node)

        tree.walk_callback_same_scope(node, yield_statement_callback)

        if not results:
            self.results.append(
                base.Flake8Result(
                    lineno=node.lineno,
                    col_offset=node.col_offset,
                    message=self._error_tmpl
                )
            )
