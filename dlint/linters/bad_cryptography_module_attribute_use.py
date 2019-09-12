#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from .helpers import bad_module_attribute_use


class BadCryptographyModuleAttributeUseLinter(bad_module_attribute_use.BadModuleAttributeUseLinter):
    """This linter looks for unsafe use of cryptography module attributes.
    These attributes may indicate weaknesses in cryptographic operations.
    """
    off_by_default = False

    _code = 'DUO134'
    _error_tmpl = 'DUO134 insecure "cryptography" attribute use'

    @property
    def illegal_module_attributes(self):
        return {
            'cryptography.hazmat.primitives.hashes': [
                'MD5',
                'SHA1',
            ],
            'cryptography.hazmat.primitives.ciphers.modes': [
                'ECB',
            ],
            'cryptography.hazmat.primitives.ciphers.algorithms': [
                'Blowfish',
                'ARC4',
                'IDEA',
            ],
            'cryptography.hazmat.primitives.asymmetric.padding': [
                'PKCS1v15',
            ],
        }
