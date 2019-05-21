#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from .helpers import bad_module_attribute_use


class BadOSUseLinter(bad_module_attribute_use.BadModuleAttributeUseLinter):
    """This linter looks for unsafe use of the Python "os" module. Use of
    system|popen|popen2|popen3|popen4 allows for easy code execution bugs.
    Further:

        "Use of tempnam|tmpnam() is vulnerable to symlink attacks; consider
        using tmpfile() (section File Object Creation) instead."

    https://docs.python.org/2.7/library/os.html
    """
    off_by_default = False

    _code = 'DUO106'
    _error_tmpl = 'DUO106 improper use of "os" module'

    @property
    def illegal_module_attributes(self):
        return {
            'os': [
                'popen',
                'popen2',
                'popen3',
                'popen4',
                'system',
                'tempnam',
                'tmpnam',
            ],
        }
