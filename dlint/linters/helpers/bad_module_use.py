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


class BadModuleUseLinter(base.BaseLinter, util.ABC):
    """This abstract base class provides an simple interface for creating new
    lint rules that block bad modules.
    """

    @property
    @abc.abstractmethod
    def illegal_modules(self):
        """Subclasses must implement this property to return a list that
        looks like:

            [
                "module_name1",
                "parent_module_name.module_name2",
            ]
        """

    @property
    def whitelisted_modules(self):
        """Subclasses may implement this property to return a list that
        looks like:

            [
                "parent_module_name.whitelisted_name1",
            ]
        """
        return []

    def visit_Import(self, node):
        import_names = [
            alias.name for alias in node.names
            if alias.name not in self.whitelisted_modules
        ]

        bad_import = any(
            tree.same_modules(illegal_module, name)
            for illegal_module in self.illegal_modules
            for name in import_names
        )

        if bad_import:
            self.results.append(
                base.Flake8Result(
                    lineno=node.lineno,
                    col_offset=node.col_offset,
                    message=self._error_tmpl
                )
            )

    def visit_ImportFrom(self, node):
        if not node.module:
            # Relative imports, e.g. 'from .' or 'from ..'
            return

        from_import_names = [
            node.module + "." + alias.name
            for alias in node.names
            if node.module + "." + alias.name not in self.whitelisted_modules
        ]

        bad_from_import = any(
            tree.same_modules(illegal_module, name)
            for illegal_module in self.illegal_modules
            for name in from_import_names
        )

        if bad_from_import:
            self.results.append(
                base.Flake8Result(
                    lineno=node.lineno,
                    col_offset=node.col_offset,
                    message=self._error_tmpl
                )
            )
