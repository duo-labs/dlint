#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import functools

from .helpers import bad_kwarg_use

from .. import tree


class BadUrllib3KwargUseLinter(bad_kwarg_use.BadKwargUseLinter):
    """This linter looks for unsafe use of urllib3 keyword arguments. These
    keyword arguments may indicate insecure connections are being performed.
    """
    off_by_default = False

    _code = 'DUO132'
    _error_tmpl = 'DUO132 urllib3 certificate verification disabled - insecure connections possible'

    @property
    def kwargs(self):
        # See 'urllib3.util.ssl_.resolve_cert_reqs' for more information
        def unverified_cert_reqs(call, kwarg_name):
            # Short-circuit evaluation
            return any(
                fn() for fn in [
                    functools.partial(
                        tree.kwarg_str,
                        call,
                        kwarg_name,
                        "CERT_NONE"
                    ),
                    functools.partial(
                        tree.kwarg_str,
                        call,
                        kwarg_name,
                        "NONE"
                    ),
                    functools.partial(
                        tree.kwarg_attribute,
                        call,
                        kwarg_name,
                        ["CERT_NONE"]
                    ),
                    functools.partial(
                        tree.kwarg_attribute,
                        call,
                        kwarg_name,
                        ["ssl", "CERT_NONE"]
                    ),
                ]
            )

        return [
            {
                "attribute_name": "PoolManager",
                "kwarg_name": "cert_reqs",
                "predicate": unverified_cert_reqs,
            },
            {
                "attribute_name": "ProxyManager",
                "kwarg_name": "cert_reqs",
                "predicate": unverified_cert_reqs,
            },
            {
                "attribute_name": "HTTPSConnectionPool",
                "kwarg_name": "cert_reqs",
                "predicate": unverified_cert_reqs,
            },
            {
                "attribute_name": "connection_from_url",
                "kwarg_name": "cert_reqs",
                "predicate": unverified_cert_reqs,
            },
            {
                "attribute_name": "proxy_from_url",
                "kwarg_name": "cert_reqs",
                "predicate": unverified_cert_reqs,
            },
        ]
