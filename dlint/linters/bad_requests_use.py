#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from .helpers import bad_kwarg_use

from .. import tree


class BadRequestsUseLinter(bad_kwarg_use.BadKwargUseLinter):
    """This linter looks for use of the "verify=False" kwarg when using the
    "requests" module. SSL verification is good, use SSL verification.

    http://docs.python-requests.org/en/master/user/advanced/#ssl-cert-verification
    """
    off_by_default = False

    _code = 'DUO123'
    _error_tmpl = 'DUO123 use of "verify=False" is insecure in "requests" module'

    @property
    def kwargs(self):
        return [
            {
                "module_path": "requests.request",
                "kwarg_name": "verify",
                "predicate": tree.kwarg_false,
            },
            {
                "module_path": "requests.get",
                "kwarg_name": "verify",
                "predicate": tree.kwarg_false,
            },
            {
                "module_path": "requests.options",
                "kwarg_name": "verify",
                "predicate": tree.kwarg_false,
            },
            {
                "module_path": "requests.head",
                "kwarg_name": "verify",
                "predicate": tree.kwarg_false,
            },
            {
                "module_path": "requests.post",
                "kwarg_name": "verify",
                "predicate": tree.kwarg_false,
            },
            {
                "module_path": "requests.put",
                "kwarg_name": "verify",
                "predicate": tree.kwarg_false,
            },
            {
                "module_path": "requests.patch",
                "kwarg_name": "verify",
                "predicate": tree.kwarg_false,
            },
            {
                "module_path": "requests.delete",
                "kwarg_name": "verify",
                "predicate": tree.kwarg_false,
            },
        ]
