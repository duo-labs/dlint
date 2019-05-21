#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from .helpers import bad_module_use


class BadCommandsUseLinter(bad_module_use.BadModuleUseLinter):
    """This linter looks for use of the "commands" module. This module execute
    shell commands, which often leads to arbitrary code execution bugs.
    """
    off_by_default = False

    _code = 'DUO125'
    _error_tmpl = 'DUO125 avoid "commands" module use'

    @property
    def illegal_modules(self):
        return [
            "commands",
        ]
