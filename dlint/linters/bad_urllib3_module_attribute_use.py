#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from .helpers import bad_module_attribute_use


class BadUrllib3ModuleAttributeUseLinter(bad_module_attribute_use.BadModuleAttributeUseLinter):
    """This linter looks for unsafe use of urllib3 module attributes. These
    attributes may indicate insecure connections are being performed.
    """
    off_by_default = False

    _code = 'DUO131'
    _error_tmpl = 'DUO131 urllib3 warnings disabled - insecure connections possible'

    @property
    def illegal_module_attributes(self):
        return {
            'urllib3': [
                'disable_warnings',
            ],
        }
