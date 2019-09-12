#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestBadCryptographyModuleAttributeUse(dlint.test.base.BaseTest):

    def test_bad_cryptography_module_attribute_usage(self):
        python_node = self.get_ast_node(
            """
            import cryptography.hazmat.primitives.hashes
            import cryptography.hazmat.primitives.ciphers.modes
            import cryptography.hazmat.primitives.ciphers.algorithms
            import cryptography.hazmat.primitives.asymmetric.padding

            cryptography.hazmat.primitives.hashes.MD5
            cryptography.hazmat.primitives.hashes.SHA1
            cryptography.hazmat.primitives.ciphers.modes.ECB
            cryptography.hazmat.primitives.ciphers.algorithms.Blowfish
            cryptography.hazmat.primitives.ciphers.algorithms.ARC4
            cryptography.hazmat.primitives.ciphers.algorithms.IDEA
            cryptography.hazmat.primitives.asymmetric.padding.PKCS1v15
            """
        )

        linter = dlint.linters.BadCryptographyModuleAttributeUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=0,
                message=dlint.linters.BadCryptographyModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=8,
                col_offset=0,
                message=dlint.linters.BadCryptographyModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=9,
                col_offset=0,
                message=dlint.linters.BadCryptographyModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=10,
                col_offset=0,
                message=dlint.linters.BadCryptographyModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=11,
                col_offset=0,
                message=dlint.linters.BadCryptographyModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=12,
                col_offset=0,
                message=dlint.linters.BadCryptographyModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=13,
                col_offset=0,
                message=dlint.linters.BadCryptographyModuleAttributeUseLinter._error_tmpl
            ),
        ]

        assert result == expected

    def test_bad_cryptography_module_attribute_usage_from_import(self):
        python_node = self.get_ast_node(
            """
            from cryptography.hazmat.primitives import hashes
            from cryptography.hazmat.primitives.ciphers import modes
            from cryptography.hazmat.primitives.ciphers import algorithms
            from cryptography.hazmat.primitives.asymmetric import padding

            hashes.MD5
            hashes.SHA1
            modes.ECB
            algorithms.Blowfish
            algorithms.ARC4
            algorithms.IDEA
            padding.PKCS1v15
            """
        )

        linter = dlint.linters.BadCryptographyModuleAttributeUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=0,
                message=dlint.linters.BadCryptographyModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=8,
                col_offset=0,
                message=dlint.linters.BadCryptographyModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=9,
                col_offset=0,
                message=dlint.linters.BadCryptographyModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=10,
                col_offset=0,
                message=dlint.linters.BadCryptographyModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=11,
                col_offset=0,
                message=dlint.linters.BadCryptographyModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=12,
                col_offset=0,
                message=dlint.linters.BadCryptographyModuleAttributeUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=13,
                col_offset=0,
                message=dlint.linters.BadCryptographyModuleAttributeUseLinter._error_tmpl
            ),
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
