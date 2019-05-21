#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from .helpers import bad_kwarg_use

from .. import tree


class BadSubprocessUseLinter(bad_kwarg_use.BadKwargUseLinter):
    """This linter looks for use of the "shell=True" kwarg when using the
    "subprocess" module.

        "If the shell is invoked explicitly, via shell=True, it is the
        application's responsibility to ensure that all whitespace and
        metacharacters are quoted appropriately to avoid shell injection
        vulnerabilities."

    https://docs.python.org/3.6/library/subprocess.html#security-considerations
    """
    off_by_default = False

    _code = 'DUO116'
    _error_tmpl = 'DUO116 avoid "shell" kwarg with "subprocess" calls'

    @property
    def kwargs(self):
        return [
            {
                "attribute_name": "call",
                "kwarg_name": "shell",
                "predicate": tree.kwarg_present,
            },
            {
                "attribute_name": "check_call",
                "kwarg_name": "shell",
                "predicate": tree.kwarg_present,
            },
            {
                "attribute_name": "check_output",
                "kwarg_name": "shell",
                "predicate": tree.kwarg_present,
            },
            {
                "attribute_name": "Popen",
                "kwarg_name": "shell",
                "predicate": tree.kwarg_present,
            },
        ]
