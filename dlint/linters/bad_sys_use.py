#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from .helpers import bad_module_attribute_use


class BadSysUseLinter(bad_module_attribute_use.BadModuleAttributeUseLinter):
    """This linter looks for unsafe use of the Python "sys" module. These
    functions allow for an arbitrary function to be passed in that the
    interpreter will call at a later point in time. This could lead to
    arbitrary code execution.
    """
    off_by_default = False

    _code = 'DUO111'
    _error_tmpl = 'DUO111 "sys" function found that could lead to arbitrary code execution'

    @property
    def illegal_module_attributes(self):
        return {
            'sys': [
                'call_tracing',
                'setprofile',
                'settrace',
            ],
        }
