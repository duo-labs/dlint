#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from .helpers import bad_builtin_use


class BadEvalUseLinter(bad_builtin_use.BadBuiltinUseLinter):
    """This linter looks for use of the Python "eval" function. This function
    makes it far too easy to achieve arbitrary code execution, so we shouldn't
    support it in any context.
    """
    off_by_default = False

    _code = 'DUO104'
    _error_tmpl = 'DUO104 use of "eval" not allowed'

    @property
    def illegal_builtin(self):
        return 'eval'
