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


class ReturnValueInInlineCallbacksLinter(base.BaseLinter):
    """This linter looks for returnValue calls that are in a function missing
    a inlineCallbacks decorator.
    """
    off_by_default = False

    _code = 'DUO114'
    _error_tmpl = 'DUO114 returnValue in function missing inlineCallbacks decorator'

    def visit_FunctionDef(self, node):
        self.generic_visit(node)

        if tree.function_has_inlinecallbacks_decorator(node):
            return

        results = []

        def returnvalue_statement_callback(inner_node):
            if isinstance(inner_node, ast.Call) and tree.call_is_returnvalue(inner_node.func):
                results.append(inner_node)

        tree.walk_callback_same_scope(node, returnvalue_statement_callback)

        if results:
            self.results.append(
                base.Flake8Result(
                    lineno=node.lineno,
                    col_offset=node.col_offset,
                    message=self._error_tmpl
                )
            )
