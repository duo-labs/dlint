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
    _error_tmpl = 'DUO123 enable SSL verification when using "requests" module'

    @property
    def kwargs(self):
        return [
            {
                "attribute_name": "request",
                "kwarg_name": "verify",
                "predicate": tree.kwarg_false,
            },
            {
                "attribute_name": "get",
                "kwarg_name": "verify",
                "predicate": tree.kwarg_false,
            },
            {
                "attribute_name": "options",
                "kwarg_name": "verify",
                "predicate": tree.kwarg_false,
            },
            {
                "attribute_name": "head",
                "kwarg_name": "verify",
                "predicate": tree.kwarg_false,
            },
            {
                "attribute_name": "post",
                "kwarg_name": "verify",
                "predicate": tree.kwarg_false,
            },
            {
                "attribute_name": "put",
                "kwarg_name": "verify",
                "predicate": tree.kwarg_false,
            },
            {
                "attribute_name": "patch",
                "kwarg_name": "verify",
                "predicate": tree.kwarg_false,
            },
            {
                "attribute_name": "delete",
                "kwarg_name": "verify",
                "predicate": tree.kwarg_false,
            },
        ]
