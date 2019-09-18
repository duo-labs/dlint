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
            return tree.kwarg_any([
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
                    tree.kwarg_module_path,
                    call,
                    kwarg_name,
                    "onelogin.saml2.constants.OneLogin_Saml2_Constants.SHA1",
                    self.namespace
                ),
                functools.partial(
                    tree.kwarg_module_path,
                    call,
                    kwarg_name,
                    "onelogin.saml2.constants.OneLogin_Saml2_Constants.RSA_SHA1",
                    self.namespace
                ),
                functools.partial(
                    tree.kwarg_module_path,
                    call,
                    kwarg_name,
                    "onelogin.saml2.constants.OneLogin_Saml2_Constants.DSA_SHA1",
                    self.namespace
                ),
            ])

        def missing_or_insecure_algorithm(call, kwarg_name):
            return (
                tree.kwarg_not_present(call, kwarg_name)
                or insecure_algorithm(call, kwarg_name)
            )

        return [
            {
                "module_path": "onelogin.saml2.utils.OneLogin_Saml2_Utils.calculate_x509_fingerprint",
                "kwarg_name": "alg",
                "predicate": functools.partial(missing_or_string, "sha1"),
            },
            {
                "module_path": "onelogin.saml2.utils.OneLogin_Saml2_Utils.add_sign",
                "kwarg_name": "sign_algorithm",
                "predicate": missing_or_insecure_algorithm,
            },
            {
                "module_path": "onelogin.saml2.utils.OneLogin_Saml2_Utils.add_sign",
                "kwarg_name": "digest_algorithm",
                "predicate": missing_or_insecure_algorithm,
            },
            {
                "module_path": "onelogin.saml2.utils.OneLogin_Saml2_Utils.validate_sign",
                "kwarg_name": "fingerprintalg",
                "predicate": functools.partial(missing_or_string, "sha1"),
            },
            {
                "module_path": "onelogin.saml2.utils.OneLogin_Saml2_Utils.validate_sign",
                "kwarg_name": "validatecert",
                "predicate": missing_or_false,
            },
            {
                "module_path": "onelogin.saml2.utils.OneLogin_Saml2_Utils.validate_metadata_sign",
                "kwarg_name": "fingerprintalg",
                "predicate": functools.partial(missing_or_string, "sha1"),
            },
            {
                "module_path": "onelogin.saml2.utils.OneLogin_Saml2_Utils.validate_metadata_sign",
                "kwarg_name": "validatecert",
                "predicate": missing_or_false,
            },
            {
                "module_path": "onelogin.saml2.utils.OneLogin_Saml2_Utils.validate_node_sign",
                "kwarg_name": "fingerprintalg",
                "predicate": functools.partial(missing_or_string, "sha1"),
            },
            {
                "module_path": "onelogin.saml2.utils.OneLogin_Saml2_Utils.validate_node_sign",
                "kwarg_name": "validatecert",
                "predicate": missing_or_false,
            },
            {
                "module_path": "onelogin.saml2.utils.OneLogin_Saml2_Utils.validate_binary_sign",
                "kwarg_name": "algorithm",
                "predicate": missing_or_insecure_algorithm,
            }
        ]
