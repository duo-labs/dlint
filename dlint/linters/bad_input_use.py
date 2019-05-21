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


class BadInputUseLinter(base.BaseLinter):
    """This linter looks for use of the Python "input" function. In Python 2
    this function is equilavent to eval(raw_input()), and thus should not be
    used. In Python 3 raw_input() functionality has been moved to input().
    """
    off_by_default = False

    _code = 'DUO108'
    _error_tmpl = 'DUO108 improper use of "input"'

    def __init__(self, *args, **kwargs):
        self.unsafe_input_import = True

        super(BadInputUseLinter, self).__init__(*args, **kwargs)

    def visit_Call(self, node):
        is_python_2 = sys.version_info < (3, 0)

        if (is_python_2
                and self.unsafe_input_import
                and isinstance(node.func, ast.Name)
                and node.func.id == 'input'):
            self.results.append(
                base.Flake8Result(
                    lineno=node.lineno,
                    col_offset=node.col_offset,
                    message=self._error_tmpl
                )
            )

    def visit_ImportFrom(self, node):
        # Using input from six.moves is valid, so if input is imported
        # in a safe way, allow input to be used for the rest of the file
        if (node.module == 'six.moves'
                and any(alias.name == 'input' for alias in node.names)):
            self.unsafe_input_import = False
