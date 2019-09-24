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
    _error_tmpl = 'DUO127 use of "ca_certs=HTTP|DISABLE" is insecure in "duo_client" module'

    @property
    def kwargs(self):
        def http_or_disable(call, kwarg_name):
            return (
                tree.kwarg_str(call, kwarg_name, "HTTP")
                or tree.kwarg_str(call, kwarg_name, "DISABLE")
            )

        return [
            {
                "module_path": "duo_client.Client",
                "kwarg_name": "ca_certs",
                "predicate": http_or_disable,
            },
            {
                "module_path": "duo_client.AsyncDuoClient",
                "kwarg_name": "ca_certs",
                "predicate": http_or_disable,
            },
            {
                "module_path": "duo_client.Auth",
                "kwarg_name": "ca_certs",
                "predicate": http_or_disable,
            },
            {
                "module_path": "duo_client.AuthAPI",
                "kwarg_name": "ca_certs",
                "predicate": http_or_disable,
            },
            {
                "module_path": "duo_client.Admin",
                "kwarg_name": "ca_certs",
                "predicate": http_or_disable,
            },
            {
                "module_path": "duo_client.AdminAPI",
                "kwarg_name": "ca_certs",
                "predicate": http_or_disable,
            },
            {
                "module_path": "duo_client.Accounts",
                "kwarg_name": "ca_certs",
                "predicate": http_or_disable,
            },
            {
                "module_path": "duo_client.AccountsAPI",
                "kwarg_name": "ca_certs",
                "predicate": http_or_disable,
            },
        ]
