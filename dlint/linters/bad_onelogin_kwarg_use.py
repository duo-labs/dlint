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


class BadOneLoginKwargUseLinter(bad_kwarg_use.BadKwargUseLinter):
    """This linter looks for unsafe use of OneLogin SAML keyword arguments.
    These arguments may indicate weaknesses in SAML authentication support.
    """
    off_by_default = False

    _code = 'DUO128'
    _error_tmpl = 'DUO128 insecure "OneLogin" SAML function call'

    @property
    def kwargs(self):
        def missing_or_string(s, call, kwarg_name):
            return (
                tree.kwarg_not_present(call, kwarg_name)
                or tree.kwarg_str(call, kwarg_name, s)
            )

        def missing_or_false(call, kwarg_name):
            return (
                tree.kwarg_not_present(call, kwarg_name)
                or tree.kwarg_false(call, kwarg_name)
            )

        def insecure_algorithm(call, kwarg_name):
            # Short-circuit evaluation
            return any(
                fn() for fn in [
                    functools.partial(
                        tree.kwarg_str,
                        call,
                        kwarg_name,
                        "http://www.w3.org/2000/09/xmldsig#sha1"
                    ),
                    functools.partial(
                        tree.kwarg_str,
                        call,
                        kwarg_name,
                        "http://www.w3.org/2000/09/xmldsig#rsa-sha1"
                    ),
                    functools.partial(
                        tree.kwarg_str,
                        call,
                        kwarg_name,
                        "http://www.w3.org/2000/09/xmldsig#dsa-sha1"
                    ),
                    functools.partial(
                        tree.kwarg_attribute,
                        call,
                        kwarg_name,
                        ["OneLogin_Saml2_Constants", "SHA1"]
                    ),
                    functools.partial(
                        tree.kwarg_attribute,
                        call,
                        kwarg_name,
                        ["OneLogin_Saml2_Constants", "RSA_SHA1"]
                    ),
                    functools.partial(
                        tree.kwarg_attribute,
                        call,
                        kwarg_name,
                        ["OneLogin_Saml2_Constants", "DSA_SHA1"]
                    ),
                ]
            )

        def missing_or_insecure_algorithm(call, kwarg_name):
            return (
                tree.kwarg_not_present(call, kwarg_name)
                or insecure_algorithm(call, kwarg_name)
            )

        return [
            {
                "attribute_name": "calculate_x509_fingerprint",
                "kwarg_name": "alg",
                "predicate": functools.partial(missing_or_string, "sha1"),
            },
            {
                "attribute_name": "add_sign",
                "kwarg_name": "sign_algorithm",
                "predicate": missing_or_insecure_algorithm,
            },
            {
                "attribute_name": "add_sign",
                "kwarg_name": "digest_algorithm",
                "predicate": missing_or_insecure_algorithm,
            },
            {
                "attribute_name": "validate_sign",
                "kwarg_name": "fingerprintalg",
                "predicate": functools.partial(missing_or_string, "sha1"),
            },
            {
                "attribute_name": "validate_sign",
                "kwarg_name": "validatecert",
                "predicate": missing_or_false,
            },
            {
                "attribute_name": "validate_metadata_sign",
                "kwarg_name": "fingerprintalg",
                "predicate": functools.partial(missing_or_string, "sha1"),
            },
            {
                "attribute_name": "validate_metadata_sign",
                "kwarg_name": "validatecert",
                "predicate": missing_or_false,
            },
            {
                "attribute_name": "validate_node_sign",
                "kwarg_name": "fingerprintalg",
                "predicate": functools.partial(missing_or_string, "sha1"),
            },
            {
                "attribute_name": "validate_node_sign",
                "kwarg_name": "validatecert",
                "predicate": missing_or_false,
            },
            {
                "attribute_name": "validate_binary_sign",
                "kwarg_name": "algorithm",
                "predicate": missing_or_insecure_algorithm,
            }
        ]
