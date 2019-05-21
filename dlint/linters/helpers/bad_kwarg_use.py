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
                    "attribute_name": "name1",
                    "kwarg_name": "kwarg1",
                    "predicate": <function>,
                },
            ]

        Which would represent 'name1(kwarg1=...)' where 'predicate' is a
        function that takes the Call object and a kwarg name and returns
        True|False.
        """

    def visit_Call(self, node):
        self.generic_visit(node)

        if not isinstance(node.func, (ast.Attribute, ast.Name)):
            return

        bad_kwarg = any(
            (
                kwarg["attribute_name"] == tree.call_name(node)
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
