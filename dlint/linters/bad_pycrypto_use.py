#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from .helpers import bad_module_use


class BadPycryptoUseLinter(bad_module_use.BadModuleUseLinter):
    """This linter looks for use of the "Crypto" module. This module is part
    of the "pycrypto" library which is unmaintained and has known
    vulnerabilities and exploits.
    """
    off_by_default = False

    _code = 'DUO133'
    _error_tmpl = 'DUO133 use of "Crypto" module is insecure'

    @property
    def illegal_modules(self):
        return [
            "Crypto",
        ]
