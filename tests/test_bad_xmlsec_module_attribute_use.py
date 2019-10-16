#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestBadXmlsecModuleAttributeUse(dlint.test.base.BaseTest):

    def test_bad_xmlsec_module_attribute_usage(self):
        python_node = self.get_ast_node(
            """
            import xmlsec.constants

            xmlsec.constants.TransformDes3Cbc
            xmlsec.constants.TransformKWDes3
            xmlsec.constants.TransformDsaSha1
            xmlsec.constants.TransformEcdsaSha1
            xmlsec.constants.TransformRsaMd5
            xmlsec.constants.TransformRsaRipemd160
            xmlsec.constants.TransformRsaSha1
            xmlsec.constants.TransformRsaPkcs1
            xmlsec.constants.TransformMd5
            xmlsec.constants.TransformRipemd160
            xmlsec.constants.TransformSha1
            """
        )

        linter = dlint.linters.BadXmlsecModuleAttributeUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadXmlsecModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=5,
                col_offset=0,
                message=dlint.linters.BadXmlsecModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=dlint.linters.BadXmlsecModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=0,
                message=dlint.linters.BadXmlsecModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=8,
                col_offset=0,
                message=dlint.linters.BadXmlsecModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=9,
                col_offset=0,
                message=dlint.linters.BadXmlsecModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=10,
                col_offset=0,
                message=dlint.linters.BadXmlsecModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=11,
                col_offset=0,
                message=dlint.linters.BadXmlsecModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=12,
                col_offset=0,
                message=dlint.linters.BadXmlsecModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=13,
                col_offset=0,
                message=dlint.linters.BadXmlsecModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=14,
                col_offset=0,
                message=dlint.linters.BadXmlsecModuleAttributeUseLinter._error_tmpl
            ),
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
