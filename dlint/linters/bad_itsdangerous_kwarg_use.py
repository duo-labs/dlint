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


class BadItsDangerousKwargUseLinter(bad_kwarg_use.BadKwargUseLinter):
    """This linter looks for unsafe use of itsdangerous keyword arguments. These
    keyword arguments may indicate insecure signing is being performed.
    """
    off_by_default = False

    _code = 'DUO137'
    _error_tmpl = 'DUO137 insecure "itsdangerous" use allowing empty signing'

    @property
    def kwargs(self):
        def none_algorithm_predicate(call, kwarg_name):
            return tree.kwarg_any([
                functools.partial(
                    tree.kwarg_module_path_call,
                    call,
                    kwarg_name,
                    "itsdangerous.signer.NoneAlgorithm",
                    self.namespace
                ),
                functools.partial(
                    tree.kwarg_module_path_call,
                    call,
                    kwarg_name,
                    "itsdangerous.NoneAlgorithm",
                    self.namespace
                ),
            ])

        def none_string_predicate(call, kwarg_name):
            return tree.kwarg_str(call, kwarg_name, "none")

        return [
            {
                "module_path": "itsdangerous.signer.Signer",
                "kwarg_name": "algorithm",
                "predicate": none_algorithm_predicate,
            },
            {
                "module_path": "itsdangerous.Signer",
                "kwarg_name": "algorithm",
                "predicate": none_algorithm_predicate,
            },
            {
                "module_path": "itsdangerous.timed.TimestampSigner",
                "kwarg_name": "algorithm",
                "predicate": none_algorithm_predicate,
            },
            {
                "module_path": "itsdangerous.TimestampSigner",
                "kwarg_name": "algorithm",
                "predicate": none_algorithm_predicate,
            },
            {
                "module_path": "itsdangerous.jws.JSONWebSignatureSerializer",
                "kwarg_name": "algorithm_name",
                "predicate": none_string_predicate,
            },
            {
                "module_path": "itsdangerous.JSONWebSignatureSerializer",
                "kwarg_name": "algorithm_name",
                "predicate": none_string_predicate,
            },
        ]
