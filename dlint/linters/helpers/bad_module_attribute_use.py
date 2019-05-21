#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import abc
import ast

from .. import base
from ... import tree
from ... import util


class BadModuleAttributeUseLinter(base.BaseLinter, util.ABC):
    """This abstract base class provides an simple interface for creating new
    lint rules that block bad attributes within a module.
    """

    def __init__(self, *args, **kwargs):
        self.illegal_wildcard_imports = []
        self.illegal_calls = []

        super(BadModuleAttributeUseLinter, self).__init__(*args, **kwargs)

    @property
    @abc.abstractmethod
    def illegal_module_attributes(self):
        """Subclasses must implement this property to return a dictionary
        that looks like:

            {
                "module_name": [
                    "attribute_name1",
                    "attribute_name2",
                ]
            }
        """

    def get_results(self):
        used_illegal_attributes = [
            attributes
            for module, attributes in self.illegal_module_attributes.items()
            if module in self.illegal_wildcard_imports
        ]

        self.results.extend([
            base.Flake8Result(
                lineno=node.lineno,
                col_offset=node.col_offset,
                message=self._error_tmpl
            )
            for node in self.illegal_calls
            if any(
                node.func.id in attributes
                for attributes in used_illegal_attributes
            )
        ])

        return self.results

    def visit_Call(self, node):
        self.generic_visit(node)

        if isinstance(node.func, ast.Name):
            illegal_call = any(
                node.func.id in illegal_attributes
                for illegal_attributes in self.illegal_module_attributes.values()
            )

            if illegal_call:
                self.illegal_calls.append(node)

    def visit_Attribute(self, node):
        if isinstance(node.value, (ast.Attribute, ast.Name)):
            module_path = '.'.join(tree.module_path(node.value))

            illegal_attribute_use = any(
                module_path == module and node.attr in attributes
                for module, attributes in self.illegal_module_attributes.items()
            )

            if illegal_attribute_use:
                self.results.append(
                    base.Flake8Result(
                        lineno=node.lineno,
                        col_offset=node.col_offset,
                        message=self._error_tmpl
                    )
                )

    def visit_ImportFrom(self, node):
        wildcard_import = any(
            alias.name == '*'
            for alias in node.names
        )
        if wildcard_import and node.module in self.illegal_module_attributes.keys():
            self.illegal_wildcard_imports.append(node.module)

        self.results.extend([
            base.Flake8Result(
                lineno=node.lineno,
                col_offset=node.col_offset,
                message=self._error_tmpl
            )
            for module, attributes in self.illegal_module_attributes.items()
            if node.module == module and any(
                alias.name in attributes for alias in node.names
            )
        ])
