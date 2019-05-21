#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from .helpers import bad_module_use


class BadMarshalUseLinter(bad_module_use.BadModuleUseLinter):
    """This linter looks for use of the "marshal" module.

        "The marshal module is not intended to be secure against erroneous
        or maliciously constructed data. Never unmarshal data received from an
        untrusted or unauthenticated source."

    https://docs.python.org/2.7/library/marshal.html
    """
    off_by_default = False

    _code = 'DUO120'
    _error_tmpl = 'DUO120 avoid "marshal" module use'

    @property
    def illegal_modules(self):
        return [
            "marshal",
        ]
