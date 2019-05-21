#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from .helpers import bad_module_use


class BadShelveUseLinter(bad_module_use.BadModuleUseLinter):
    """This linter looks for use of the "shelve" module.

        "Because the shelve module is backed by pickle, it is insecure to load
        a shelf from an untrusted source. Like with pickle, loading a shelf can
        execute arbitrary code."

    https://docs.python.org/2.7/library/shelve.html
    """
    off_by_default = False

    _code = 'DUO119'
    _error_tmpl = 'DUO119 avoid "shelve" module use'

    @property
    def illegal_modules(self):
        return [
            "shelve",
        ]
