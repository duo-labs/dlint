#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import abc
import ast
import collections

from .. import base
from ... import tree
from ... import util

Assignment = collections.namedtuple(
    'Assignment',
    ['variable', 'module_path', 'lineno', 'col_offset']
)


class BadNameAttributeUseLinter(base.BaseLinter, util.ABC):
    """This abstract base class provides an simple interface for creating new
    lint rules that block bad attributes on a variable object.
    """

    @property
    @abc.abstractmethod
    def illegal_name_attributes(self):
        """Subclasses must implement this property to return a dictionary
        that looks like:

            {
                "object_attribute": [
                    ["module_name1", "module_name2"],
                    ["module_name3", "module_name4"],
                ]
            }
        """

    def visit_FunctionDef(self, node):
        self.generic_visit(node)

        targets = []

        def variable_assignment_callback(inner_node):
            if not (isinstance(inner_node, ast.Assign)
                    and isinstance(inner_node.value, ast.Call)):
                return

            module_path = tree.module_path(inner_node.value.func)
            targets.extend([
                Assignment(
                    variable=target.id,
                    module_path=module_path,
                    lineno=inner_node.lineno,
                    col_offset=inner_node.col_offset,
                )
                for target in inner_node.targets
                if isinstance(target, ast.Name)
            ])

        tree.walk_callback_same_scope(node, variable_assignment_callback)

        results = []

        def attribute_use_callback(inner_node):
            if not (isinstance(inner_node, ast.Call)
                    and isinstance(inner_node.func, ast.Attribute)
                    and isinstance(inner_node.func.value, ast.Name)):
                return

            variable = inner_node.func.value.id
            attribute = inner_node.func.attr

            illegal_calls = [
                target for target in targets
                if target.variable == variable
                and attribute in self.illegal_name_attributes
                and target.module_path in self.illegal_name_attributes[attribute]
            ]

            try:
                latest_variable_assignment = max(
                    [
                        target for target in targets
                        if target.variable == variable
                    ],
                    key=lambda target: (target.lineno, target.col_offset)
                )
            except ValueError:
                # No variable name matches
                return

            if latest_variable_assignment in illegal_calls:
                results.append(inner_node)

        tree.walk_callback_same_scope(node, attribute_use_callback)

        self.results.extend([
            base.Flake8Result(
                lineno=result.lineno,
                col_offset=result.col_offset,
                message=self._error_tmpl
            )
            for result in results
        ])
