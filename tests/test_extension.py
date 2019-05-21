#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import os
import sys
import unittest

# Since extension imports dlint we cannot add it to the module or else we'll
# have circular imports. Thus we must come up with some tricks to import it
sys.path.append(
    os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "dlint"
    )
)
sys.path.append(
    os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "dlint",
        "test"
    )
)

import base  # noqa: E402
import extension  # noqa: E402


class TestFlake8Extension(base.BaseTest):

    def test_flake8_extension_empty(self):
        python_string = self.get_ast_node(
            """
            """
        )

        linter = extension.Flake8Extension(python_string, "unused")

        result = list(linter.run())
        expected = []

        assert result == expected

    def test_flake8_extension_basic(self):
        python_string = self.get_ast_node(
            """
            exec('print "TEST"')
            """
        )

        linter = extension.Flake8Extension(python_string, "unused")

        result = list(linter.run())
        expected = [
            (
                2,
                0,
                extension.dlint.linters.BadExecUseLinter._error_tmpl,
                extension.dlint.linters.BadExecUseLinter
            )
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
