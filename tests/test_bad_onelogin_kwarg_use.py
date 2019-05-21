#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestBadOneLoginKwargUse(dlint.test.base.BaseTest):

    def test_bad_onelogin_kwarg_usage(self):
        python_string = self.get_ast_node(
            """
            from onelogin.saml2.utils import OneLogin_Saml2_Utils
            from onelogin.saml2.constants import OneLogin_Saml2_Constants

            OneLogin_Saml2_Utils.calculate_x509_fingerprint()
            OneLogin_Saml2_Utils.calculate_x509_fingerprint(alg="sha1")

            OneLogin_Saml2_Utils.add_sign(sign_algorithm=OneLogin_Saml2_Constants.RSA_SHA1)
            OneLogin_Saml2_Utils.add_sign(sign_algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1")
            OneLogin_Saml2_Utils.add_sign(digest_algorithm=OneLogin_Saml2_Constants.SHA1)
            OneLogin_Saml2_Utils.add_sign(digest_algorithm="http://www.w3.org/2000/09/xmldsig#sha1")

            OneLogin_Saml2_Utils.validate_sign()
            OneLogin_Saml2_Utils.validate_sign(fingerprintalg="sha1")
            OneLogin_Saml2_Utils.validate_sign(fingerprintalg="sha256", validatecert=False)

            OneLogin_Saml2_Utils.validate_metadata_sign()
            OneLogin_Saml2_Utils.validate_metadata_sign(fingerprintalg="sha1")
            OneLogin_Saml2_Utils.validate_metadata_sign(fingerprintalg="sha256", validatecert=False)

            OneLogin_Saml2_Utils.validate_node_sign()
            OneLogin_Saml2_Utils.validate_node_sign(fingerprintalg="sha1")
            OneLogin_Saml2_Utils.validate_node_sign(fingerprintalg="sha256", validatecert=False)

            OneLogin_Saml2_Utils.validate_binary_sign()
            OneLogin_Saml2_Utils.validate_binary_sign(algorithm=OneLogin_Saml2_Constants.RSA_SHA1)
            OneLogin_Saml2_Utils.validate_binary_sign(algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1")
            """
        )

        linter = dlint.linters.BadOneLoginKwargUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=5,
                col_offset=0,
                message=dlint.linters.BadOneLoginKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=dlint.linters.BadOneLoginKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=8,
                col_offset=0,
                message=dlint.linters.BadOneLoginKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=9,
                col_offset=0,
                message=dlint.linters.BadOneLoginKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=10,
                col_offset=0,
                message=dlint.linters.BadOneLoginKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=11,
                col_offset=0,
                message=dlint.linters.BadOneLoginKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=13,
                col_offset=0,
                message=dlint.linters.BadOneLoginKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=14,
                col_offset=0,
                message=dlint.linters.BadOneLoginKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=15,
                col_offset=0,
                message=dlint.linters.BadOneLoginKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=17,
                col_offset=0,
                message=dlint.linters.BadOneLoginKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=18,
                col_offset=0,
                message=dlint.linters.BadOneLoginKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=19,
                col_offset=0,
                message=dlint.linters.BadOneLoginKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=21,
                col_offset=0,
                message=dlint.linters.BadOneLoginKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=22,
                col_offset=0,
                message=dlint.linters.BadOneLoginKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=23,
                col_offset=0,
                message=dlint.linters.BadOneLoginKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=25,
                col_offset=0,
                message=dlint.linters.BadOneLoginKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=26,
                col_offset=0,
                message=dlint.linters.BadOneLoginKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=27,
                col_offset=0,
                message=dlint.linters.BadOneLoginKwargUseLinter._error_tmpl
            )
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
