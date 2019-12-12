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

    def __init__(self, *args, **kwargs):
        self.bad_nodes = []

        super(BadModuleAttributeUseLinter, self).__init__(*args, **kwargs)

    def get_results(self):

        return [
            base.Flake8Result(
                lineno=node.lineno,
                col_offset=node.col_offset,
                message=self._error_tmpl
            )
            for node in self.bad_nodes
        ]

    def visit_Name(self, node):
        def illegal_import_with_name_resolution(name, attributes, illegal_module_path):
            if name in attributes:
                resolved_name = name
            else:
                resolved_name = self.namespace.asname_to_name(name)
                if resolved_name not in attributes:
                    return False

            return self.namespace.illegal_module_imported(
                resolved_name,
                illegal_module_path + "." + resolved_name
            )

        illegal_call_use = any(
            illegal_import_with_name_resolution(
                node.id,
                attributes,
                illegal_module_path
            )
            for illegal_module_path, attributes in self.illegal_module_attributes.items()
        )

        if illegal_call_use:
            self.bad_nodes.append(node)

    def visit_Attribute(self, node):
        self.generic_visit(node)

        module_path = tree.module_path_str(node.value)

        illegal_attribute_use = any(
            node.attr in attributes
            and self.namespace.illegal_module_imported(module_path, illegal_module_path)
            for illegal_module_path, attributes in self.illegal_module_attributes.items()
        )

        if illegal_attribute_use:
            self.bad_nodes.append(node)
