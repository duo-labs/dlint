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
    _error_tmpl = 'DUO132 "urllib3" certificate verification disabled, insecure connections possible'

    @property
    def kwargs(self):
        # See 'urllib3.util.ssl_.resolve_cert_reqs' for more information
        def unverified_cert_reqs(call, kwarg_name):
            return tree.kwarg_any([
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
                    tree.kwarg_module_path,
                    call,
                    kwarg_name,
                    "ssl.CERT_NONE",
                    self.namespace
                ),
            ])

        return [
            {
                "module_path": "urllib3.PoolManager",
                "kwarg_name": "cert_reqs",
                "predicate": unverified_cert_reqs,
            },
            {
                "module_path": "urllib3.ProxyManager",
                "kwarg_name": "cert_reqs",
                "predicate": unverified_cert_reqs,
            },
            {
                "module_path": "urllib3.HTTPSConnectionPool",
                "kwarg_name": "cert_reqs",
                "predicate": unverified_cert_reqs,
            },
            {
                "module_path": "urllib3.connection_from_url",
                "kwarg_name": "cert_reqs",
                "predicate": unverified_cert_reqs,
            },
            {
                "module_path": "urllib3.proxy_from_url",
                "kwarg_name": "cert_reqs",
                "predicate": unverified_cert_reqs,
            },
        ]
