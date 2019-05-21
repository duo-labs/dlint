#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from .helpers import bad_builtin_use
from . import base


class BadExecUseLinter(bad_builtin_use.BadBuiltinUseLinter):
    """This linter looks for use of the Python "exec" function. This function
    makes it far too easy to achieve arbitrary code execution, so we shouldn't
    support it in any context.
    """
    off_by_default = False

    _code = 'DUO105'
    _error_tmpl = 'DUO105 use of "exec" not allowed'

    # Python 2
    def visit_Exec(self, node):
        self.results.append(
            base.Flake8Result(
                lineno=node.lineno,
                col_offset=node.col_offset,
                message=self._error_tmpl
            )
        )

    @property
    def illegal_builtin(self):
        return 'exec'
