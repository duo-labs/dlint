#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import abc
import ast
import warnings

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
                    "attribute_name": "name1", | "module_path": "mod1.mod2.name1",
                    "kwarg_name": "kwarg1",
                    "predicate": <function>,
                },
            ]

        Which would represent 'name1(kwarg1=...)' where 'predicate' is a
        function that takes the Call object and a kwarg name and returns
        True|False.

        Either "attribute_name" or "module_path" can be specified, however
        "attribute_name" is deprecated and will be removed in the future.
        This is a temporary, backwards-compatible change to allow us to more
        accurately specify an attribute from a specific module. E.g.
        "subprocess.Popen(shell=True)" vs. just "Popen(shell=True)". In the
        future we will remove the old behavior in favor of fully specified
        module attributes.
        """

    def visit_Call(self, node):
        self.generic_visit(node)

        if not isinstance(node.func, (ast.Attribute, ast.Name)):
            return

        def compare_kwarg_and_call(kwarg, call_node):
            if "attribute_name" in kwarg:
                warnings.warn(
                    "'attribute_name' deprecated, please use fully specified 'module_path'",
                    DeprecationWarning
                )
                return kwarg["attribute_name"] == tree.call_name(call_node)

            module_path = tree.module_path_str(node.func)

            return self.namespace.illegal_module_imported(
                module_path,
                kwarg["module_path"]
            )

        bad_kwarg = any(
            (
                compare_kwarg_and_call(kwarg, node)
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
