#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from .helpers import bad_builtin_use


class BadCompileUseLinter(bad_builtin_use.BadBuiltinUseLinter):
    """This linter looks for use of the Python "compile" function. While not
    bad in and of itself, this function is _probably_ a code smell that
    something else we don't want could be going on. I.e. "compile" is often
    proceeded by "eval" or "exec".

    The Python docs also have this to say about "compile":

        "Warning: It is possible to crash the Python interpreter with a
        sufficiently large/complex string when compiling to an AST object
        due to stack depth limitations in Python's AST compiler."
    """
    off_by_default = False

    _code = 'DUO110'
    _error_tmpl = 'DUO110 use of "compile" not allowed'

    @property
    def illegal_builtin(self):
        return 'compile'
