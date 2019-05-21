#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from .helpers import bad_module_attribute_use


class BadTempfileUseLinter(bad_module_attribute_use.BadModuleAttributeUseLinter):
    """This linter looks for unsafe use of the Python "tempfile.mktemp" module:

        "Use of this function may introduce a security hole in your program. By
        the time you get around to doing anything with the file name it
        returns, someone else may have beaten you to the punch. mktemp() usage
        can be replaced easily with NamedTemporaryFile(), passing it the
        delete=False parameter."

    https://docs.python.org/2.7/library/tempfile.html
    """
    off_by_default = False

    _code = 'DUO121'
    _error_tmpl = 'DUO121 use of "tempfile.mktemp" allows for race conditions'

    @property
    def illegal_module_attributes(self):
        return {
            'tempfile': [
                'mktemp',
            ],
        }
