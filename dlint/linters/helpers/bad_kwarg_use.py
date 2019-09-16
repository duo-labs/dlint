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


class BadKwargUseLinter(base.BaseLinter, util.ABC):
    """This abstract base class provides an simple interface for creating new
    lint rules that block bad kwarg use.
    """

    @property
    @abc.abstractmethod
    def kwargs(self):
        """Subclasses must implement this property to return a list that
        looks like:

            [
                {
                    "attribute_name": "name1|mod1.mod2.name1",
                    "kwarg_name": "kwarg1",
                    "predicate": <function>,
                },
            ]

        Which would represent 'name1(kwarg1=...)' where 'predicate' is a
        function that takes the Call object and a kwarg name and returns
        True|False.

        The "attribute_name" has been overloaded to behave differently if a
        period (".") is included or not. This key can now take a value like
        "attribute" or "module1.module2.attribute". This is a temporary,
        backwards-compatible change to allow us to more accurately specify an
        attribute from a specific module. E.g. "subprocess.Popen(shell=True)"
        vs. just "Popen(shell=True)". In the future we should deprecate and
        eventually remove the old behavior in favor of fully specified module
        attributes.
        """

    def visit_Call(self, node):
        self.generic_visit(node)

        if not isinstance(node.func, (ast.Attribute, ast.Name)):
            return

        def compare_attribute_name_and_call(attribute, call_node):
            if "." not in attribute:
                return attribute == tree.call_name(call_node)

            module_path = ".".join(tree.module_path(node.func))

            return self.namespace.illegal_module_imported(
                module_path,
                attribute
            )

        bad_kwarg = any(
            (
                compare_attribute_name_and_call(kwarg["attribute_name"], node)
                and kwarg["predicate"](node, kwarg["kwarg_name"])
            )
            for kwarg in self.kwargs
        )

        if bad_kwarg:
            self.results.append(
                base.Flake8Result(
                    lineno=node.lineno,
                    col_offset=node.col_offset,
                    message=self._error_tmpl
                )
            )
