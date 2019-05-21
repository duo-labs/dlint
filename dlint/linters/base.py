#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import ast
import collections

Flake8Result = collections.namedtuple(
    'Flake8Result',
    ['lineno', 'col_offset', 'message']
)


class BaseLinter(ast.NodeVisitor):
    def __init__(self, *args, **kwargs):
        self.results = []

        super(BaseLinter, self).__init__(*args, **kwargs)

    def get_results(self):

        return self.results
