#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from .helpers import bad_module_attribute_use


class BadXmlsecModuleAttributeUseLinter(bad_module_attribute_use.BadModuleAttributeUseLinter):
    """This linter looks for unsafe use of xmlsec module attributes.
    These attributes may indicate weaknesses in cryptographic operations.
    """
    off_by_default = False

    _code = 'DUO136'
    _error_tmpl = 'DUO136 insecure "xmlsec" attribute use'

    @property
    def illegal_module_attributes(self):
        return {
            'xmlsec.constants': [
                'TransformDes3Cbc',
                'TransformKWDes3',
                'TransformDsaSha1',
                'TransformEcdsaSha1',
                'TransformRsaMd5',
                'TransformRsaRipemd160',
                'TransformRsaSha1',
                'TransformRsaPkcs1',
                'TransformMd5',
                'TransformRipemd160',
                'TransformSha1'
            ],
        }
