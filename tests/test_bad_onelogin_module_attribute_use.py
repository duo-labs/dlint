#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestBadOneLoginModuleAttributeUse(dlint.test.base.BaseTest):

    def test_bad_onelogin_module_attribute_usage(self):
        python_string = self.get_ast_node(
            """
            import onelogin.saml2.utils.OneLogin_Saml2_Constants

            onelogin.saml2.utils.OneLogin_Saml2_Constants.SHA1
            onelogin.saml2.utils.OneLogin_Saml2_Constants.RSA_SHA1
            onelogin.saml2.utils.OneLogin_Saml2_Constants.DSA_SHA1
            onelogin.saml2.utils.OneLogin_Saml2_Constants.TRIPLEDES_CBC
            """
        )

        linter = dlint.linters.BadOneLoginModuleAttributeUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadOneLoginModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=5,
                col_offset=0,
                message=dlint.linters.BadOneLoginModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=dlint.linters.BadOneLoginModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=0,
                message=dlint.linters.BadOneLoginModuleAttributeUseLinter._error_tmpl
            ),
        ]

        assert result == expected

    def test_bad_onelogin_module_attribute_usage_from_import(self):
        python_string = self.get_ast_node(
            """
            from onelogin.saml2.utils import OneLogin_Saml2_Constants

            OneLogin_Saml2_Constants.SHA1
            OneLogin_Saml2_Constants.RSA_SHA1
            OneLogin_Saml2_Constants.DSA_SHA1
            OneLogin_Saml2_Constants.TRIPLEDES_CBC
            """
        )

        linter = dlint.linters.BadOneLoginModuleAttributeUseLinter()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadOneLoginModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=5,
                col_offset=0,
                message=dlint.linters.BadOneLoginModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=dlint.linters.BadOneLoginModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=0,
                message=dlint.linters.BadOneLoginModuleAttributeUseLinter._error_tmpl
            ),
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
