#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from .helpers import bad_module_attribute_use


class BadSSLModuleAttributeUseLinter(bad_module_attribute_use.BadModuleAttributeUseLinter):
    """This linter looks for unsafe use of the Python "ssl" module. Securely
    making SSL connections is a difficult task, and is often filled with
    gotchas. This linter performs basic sanity checks on various common
    mistakes, but still can't guarantee that no findings means usage is safe.

    Further, there may be false positives associated with this rule. For
    example, PROTOCOL_SSLv23 allows for ALL protocol versions, including the
    secure TLSv1.2, and the insecure SSLv3. PROTOCOL_SSLv23 may be fine in
    specific contexts, but its usage may point to code warranting further
    investigation.
    """
    off_by_default = False

    _code = 'DUO122'
    _error_tmpl = 'DUO122 insecure "ssl" module attribute use'

    @property
    def illegal_module_attributes(self):
        return {
            'ssl': [
                '_create_unverified_context',
                '_https_verify_certificates',
                'CERT_NONE',
                'CERT_OPTIONAL',
                'PROTOCOL_SSLv2',
                'PROTOCOL_SSLv23',
                'PROTOCOL_SSLv3',
                'PROTOCOL_TLS',
            ],
        }
