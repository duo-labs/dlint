#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from . import base


class FormatStringLinter(base.BaseLinter):
    """This linter looks for use of Python's format string operator, e.g. '%'.
    Use of the format string operator in Python can lead to information
    disclosure, DoS, etc, if not done properly[1].

    [1] http://www.drdobbs.com/security/programming-language-format-string-vulne/197002914?pgno=3
    """

    # We're still working on this one...
    off_by_default = True

    _code = 'DUO104'
    _error_tmpl = 'DUO104 avoid format strings, please use "format" function'

    def visit_BinOp(self, node):
        pass
