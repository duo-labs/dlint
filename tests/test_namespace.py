#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import pytest

import dlint


class TestNamespace(dlint.test.base.BaseTest):

    def test_basic_import(self):
        python_node = self.get_ast_node(
            """
            import foo
            """
        )

        namespace = dlint.namespace.Namespace.from_module_node(python_node)

        result = namespace.name_imported("foo")
        expected = True

        assert result == expected

    def test_basic_from_import(self):
        python_node = self.get_ast_node(
            """
            from foo import bar
            """
        )

        namespace = dlint.namespace.Namespace.from_module_node(python_node)

        result = namespace.name_imported("bar")
        expected = True

        assert result == expected

    def test_basic_as_import(self):
        python_node = self.get_ast_node(
            """
            import foo as bar
            """
        )

        namespace = dlint.namespace.Namespace.from_module_node(python_node)

        result = namespace.name_imported("bar")
        expected = True

        assert result == expected

    def test_basic_as_from_import(self):
        python_node = self.get_ast_node(
            """
            from foo import bar as baz
            """
        )

        namespace = dlint.namespace.Namespace.from_module_node(python_node)

        result = namespace.name_imported("baz")
        expected = True

        assert result == expected

    def test_as_import_mismatch(self):
        python_node = self.get_ast_node(
            """
            import foo as bar
            """
        )

        namespace = dlint.namespace.Namespace.from_module_node(python_node)

        result = namespace.name_imported("foo")
        expected = False

        assert result == expected

    def test_as_from_import_mismatch(self):
        python_node = self.get_ast_node(
            """
            from foo import bar as baz
            """
        )

        namespace = dlint.namespace.Namespace.from_module_node(python_node)

        result = (
            namespace.name_imported("foo")
            or namespace.name_imported("bar")
        )
        expected = False

        assert result == expected

    def test_from_module_node_unknown_type(self):
        unknown_type = None

        with pytest.raises(TypeError):
            dlint.namespace.Namespace.from_module_node(unknown_type)


if __name__ == "__main__":
    unittest.main()
