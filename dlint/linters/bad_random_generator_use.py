#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import ast

from . import base


class BadRandomGeneratorUseLinter(base.BaseLinter):
    """This linter looks for any use of the Python "random" module EXCEPT
    SystemRandom.

    By default Python uses a Mersenne Twister[1] implementation to generate
    random values, and this is not suitable for cryptographic purposes.
    SystemRandom uses os.urandom to get random data, which is generally a
    much better choice.

    [1] https://en.wikipedia.org/wiki/Mersenne_twister
    """
    off_by_default = False

    _code = 'DUO102'
    _error_tmpl = 'DUO102 improper use of "random" module, please use "random.SystemRandom"'

    def visit_Attribute(self, node):
        legal_module_functions = [
            ('random', 'SystemRandom'),
        ]

        if (isinstance(node.value, ast.Name)):
            illegal_function_use = any(
                node.value.id == module and node.attr != function
                for module, function in legal_module_functions
            )

            if illegal_function_use:
                self.results.append(
                    base.Flake8Result(
                        lineno=node.lineno,
                        col_offset=node.col_offset,
                        message=self._error_tmpl
                    )
                )

    def visit_ImportFrom(self, node):
        legal_module_functions = [
            ('random', 'SystemRandom'),
        ]
        illegal_import_from_use = any(
            node.module == module and any(alias.name != function for alias in node.names)
            for module, function in legal_module_functions
        )

        if illegal_import_from_use:
            self.results.append(
                base.Flake8Result(
                    lineno=node.lineno,
                    col_offset=node.col_offset,
                    message=self._error_tmpl
                )
            )
