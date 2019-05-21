#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from .helpers import bad_module_attribute_use


class BadPickleUseLinter(bad_module_attribute_use.BadModuleAttributeUseLinter):
    """This linter looks for use of the Python "pickle" module. Pickling is
    not secure against erroneous or maliciously constructed data.
    """
    off_by_default = False

    _code = 'DUO103'
    _error_tmpl = 'DUO103 improper use of "pickle" or "cPickle"'

    @property
    def illegal_module_attributes(self):
        return {
            'cPickle': [
                'loads',
                'load',
                'Unpickler',
            ],
            'pickle': [
                'loads',
                'load',
                'Unpickler',
            ],
        }
