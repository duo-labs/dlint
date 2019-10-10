#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import ast

from . import namespace


class MultiNodeVisitor(ast.NodeVisitor):
    def __init__(self, linters, *args, **kwargs):
        self.linters = linters
        self.namespace = None

        super(MultiNodeVisitor, self).__init__(*args, **kwargs)

    def visit(self, node):
        if not self.namespace:
            # Assuming that 'visit' is always called the first time with 'node'
            # as an ast.Module. If not, we should fail fast with a raised
            # exception and investigate.
            self.namespace = namespace.Namespace.from_module_node(node)
            for linter in self.linters:
                linter.namespace = self.namespace

        # Python 2 cannot rebind free variables, i.e. 'nonlocal'
        nonlocal_hack = {'any_recurse': False}

        def recurse_visit(inner_node):
            # To avoid having each linter call its own 'generic_visit' we
            # update the linters to report back whether they would've called
            # the function or not.
            nonlocal_hack['any_recurse'] = True

        for linter in self.linters:
            linter.generic_visit = recurse_visit

        method = 'visit_' + node.__class__.__name__

        # Only recurse further down the AST once if ANY of the linters doesn't
        # implement a visit function. This is optimized over recursing down the
        # AST for ALL linters.
        any_generic = False
        for linter in self.linters:
            visitor = getattr(linter, method, None)

            if visitor is None:
                any_generic = True
                continue

            visitor(node)

        if any_generic or nonlocal_hack['any_recurse']:
            self.generic_visit(node)
