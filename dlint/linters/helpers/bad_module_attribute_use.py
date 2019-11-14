#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import abc

from .. import base
from ... import tree
from ... import util


class BadModuleAttributeUseLinter(base.BaseLinter, util.ABC):
    """This abstract base class provides an simple interface for creating new
    lint rules that block bad attributes within a module.
    """

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

    def visit_Name(self, node):
        # Names have no module path by definition - i.e. they're a
        # naked name in the namespace like 'Foo()' instead of 'bar.baz.Foo()'
        name_module_path = ""

        illegal_call_use = any(
            node.id in attributes
            and self.namespace.illegal_module_imported(name_module_path, illegal_module_path)
            for illegal_module_path, attributes in self.illegal_module_attributes.items()
        )

        if illegal_call_use:
            self.results.append(
                base.Flake8Result(
                    lineno=node.lineno,
                    col_offset=node.col_offset,
                    message=self._error_tmpl
                )
            )

    def visit_Attribute(self, node):
        self.generic_visit(node)

        module_path = tree.module_path_str(node.value)

        illegal_attribute_use = any(
            node.attr in attributes
            and self.namespace.illegal_module_imported(module_path, illegal_module_path)
            for illegal_module_path, attributes in self.illegal_module_attributes.items()
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
