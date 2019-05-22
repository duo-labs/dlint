#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from .helpers import bad_module_attribute_use


class BadHashlibUseLinter(bad_module_attribute_use.BadModuleAttributeUseLinter):
    """This linter looks for unsafe use of the Python "hashlib" module. Use of
    md5|sha1 is known to have hash collision weaknesses.
    """
    off_by_default = False

    _code = 'DUO130'
    _error_tmpl = 'DUO130 insecure use of "hashlib" module'

    @property
    def illegal_module_attributes(self):
        return {
            'hashlib': [
                'md5',
                'sha1',
            ],
        }
