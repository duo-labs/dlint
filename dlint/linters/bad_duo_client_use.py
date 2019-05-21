#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from .helpers import bad_kwarg_use

from .. import tree


class BadDuoClientUseLinter(bad_kwarg_use.BadKwargUseLinter):
    """This linter looks for unsafe HTTP use when using the "duo_client" module.
    """
    off_by_default = False

    _code = 'DUO127'
    _error_tmpl = 'DUO127 avoid "HTTP" or "DISABLE" when using "ca_certs"'

    @property
    def kwargs(self):
        def http_or_disable(call, kwarg_name):
            return (
                tree.kwarg_str(call, kwarg_name, "HTTP")
                or tree.kwarg_str(call, kwarg_name, "DISABLE")
            )

        return [
            {
                "attribute_name": "Client",
                "kwarg_name": "ca_certs",
                "predicate": http_or_disable,
            },
            {
                "attribute_name": "AsyncDuoClient",
                "kwarg_name": "ca_certs",
                "predicate": http_or_disable,
            },
            {
                "attribute_name": "Auth",
                "kwarg_name": "ca_certs",
                "predicate": http_or_disable,
            },
            {
                "attribute_name": "AuthAPI",
                "kwarg_name": "ca_certs",
                "predicate": http_or_disable,
            },
            {
                "attribute_name": "Admin",
                "kwarg_name": "ca_certs",
                "predicate": http_or_disable,
            },
            {
                "attribute_name": "AdminAPI",
                "kwarg_name": "ca_certs",
                "predicate": http_or_disable,
            },
            {
                "attribute_name": "Accounts",
                "kwarg_name": "ca_certs",
                "predicate": http_or_disable,
            },
            {
                "attribute_name": "AccountsAPI",
                "kwarg_name": "ca_certs",
                "predicate": http_or_disable,
            },
        ]
