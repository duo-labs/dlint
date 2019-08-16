#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import ast
import collections

from .. import namespace

Flake8Result = collections.namedtuple(
    'Flake8Result',
    ['lineno', 'col_offset', 'message']
)


class BaseLinter(ast.NodeVisitor):
    def __init__(self, *args, **kwargs):
        self.results = []
        self.namespace = None

        super(BaseLinter, self).__init__(*args, **kwargs)

    def get_results(self):

        return self.results

    def visit(self, node):
        if not self.namespace:
            # Assuming that 'visit' is always called the first time with 'node'
            # as an ast.Module. If not, we should fail fast with a raised
            # exception and investigate.
            self.namespace = namespace.Namespace.from_module_node(node)

        super(BaseLinter, self).visit(node)
