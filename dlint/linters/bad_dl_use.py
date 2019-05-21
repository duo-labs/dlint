#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from .helpers import bad_module_use


class BadDlUseLinter(bad_module_use.BadModuleUseLinter):
    """This linter looks for use of the "dl" module.

        "The dl module bypasses the Python type system and error handling. If
        used incorrectly it may cause segmentation faults, crashes or other
        incorrect behaviour."

    https://docs.python.org/2.7/library/dl.html
    """
    off_by_default = False

    _code = 'DUO117'
    _error_tmpl = 'DUO117 avoid "dl" module use'

    @property
    def illegal_modules(self):
        return [
            "dl",
        ]
