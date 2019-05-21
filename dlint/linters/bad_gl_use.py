#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from .helpers import bad_module_use


class BadGlUseLinter(bad_module_use.BadModuleUseLinter):
    """This linter looks for use of the "gl" module.

        "Some illegal calls to the GL library cause the Python interpreter to
        dump core. In particular, the use of most GL calls is unsafe before the
        first window is opened."

    https://docs.python.org/2.7/library/gl.html
    """
    off_by_default = False

    _code = 'DUO118'
    _error_tmpl = 'DUO118 avoid "gl" module use'

    @property
    def illegal_modules(self):
        return [
            "gl",
        ]
