#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import abc
import ast
import itertools

from .. import base
from ... import tree
from ... import util


class BadKwargUseLinter(base.BaseLinter, util.ABC):
    """This abstract base class provides an simple interface for creating new
    lint rules that block bad kwarg use.
    """

    def __init__(self, *args, **kwargs):
        self.minimized_bad_kwarg_func = None

        module_path_grouped = [
            (k, list(v))
            for k, v in itertools.groupby(
                sorted(self.kwargs, key=lambda k: k["module_path"]),
                key=lambda k: k["module_path"]
            )
        ]

        def minimized_illegal_module_imported(module_path, node):
            return any(
                self.namespace.illegal_module_imported(
                    module_path,
                    kwarg["module_path"]
                )
                and kwarg["predicate"](node, kwarg["kwarg_name"])
                for illegal_module_path, kwargs in module_path_grouped
                for kwarg in kwargs
            )

        kwarg_predicate_grouped = [
            (k, list(v))
            for k, v in itertools.groupby(
                sorted(self.kwargs, key=lambda k: (k["kwarg_name"], id(k["predicate"]))),
                key=lambda k: (k["kwarg_name"], id(k["predicate"]))
            )
        ]

        def minimized_kwarg_predicate(module_path, node):
            return any(
                self.namespace.illegal_module_imported(
                    module_path,
                    kwarg["module_path"]
                )
                and kwarg["predicate"](node, kwarg["kwarg_name"])
                for kwarg_predicate_tuple, kwargs in kwarg_predicate_grouped
                for kwarg in kwargs
            )

        # Minimize kwarg checks by grouping similar rules
        if (len(kwarg_predicate_grouped) < len(self.kwargs)
                and len(module_path_grouped) == len(self.kwargs)):
            self.minimized_bad_kwarg_func = minimized_kwarg_predicate
        else:
            self.minimized_bad_kwarg_func = minimized_illegal_module_imported

        super(BadKwargUseLinter, self).__init__(*args, **kwargs)

    @property
    @abc.abstractmethod
    def kwargs(self):
        """Subclasses must implement this property to return a list that
        looks like:

            [
                {
                    "module_path": "mod1.mod2.name1",
                    "kwarg_name": "kwarg1",
                    "predicate": <function>,
                },
            ]

        Which would represent 'mod1.mod2.name1(kwarg1=...)' where 'predicate'
        is a function that takes the Call object and a kwarg name and returns
        True|False.
        """

    def visit_Call(self, node):
        self.generic_visit(node)

        if not isinstance(node.func, (ast.Attribute, ast.Name)):
            return

        bad_kwarg = self.minimized_bad_kwarg_func(
            tree.module_path_str(node.func),
            node
        )

        if bad_kwarg:
            self.results.append(
                base.Flake8Result(
                    lineno=node.lineno,
                    col_offset=node.col_offset,
                    message=self._error_tmpl
                )
            )
