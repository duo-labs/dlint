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
from ... import util


class BadBuiltinUseLinter(base.BaseLinter, util.ABC):
    """This abstract base class provides an simple interface for creating new
    lint rules that block builtin functions.
    """
    @property
    @abc.abstractmethod
    def illegal_builtin(self):
        """Subclasses must implement this property to return a string of the
        builtin function name they'd like to blacklist.
        """

    def visit_Call(self, node):
        if (isinstance(node.func, ast.Name)
                and node.func.id == self.illegal_builtin):
            self.results.append(
                base.Flake8Result(
                    lineno=node.lineno,
                    col_offset=node.col_offset,
                    message=self._error_tmpl
                )
            )
