#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import abc

from .. import base
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

    @staticmethod
    def same_modules(s1, s2):
        """Compare two module strings where submodules of an illegal
        parent module should also be illegal. I.e. blacklisting 'foo.bar'
        should also make 'foo.bar.baz' illegal.

        The first argument should 'encompass' the second, not the other way
        around. I.e. passing same_modules('foo', 'foo.bar') will return True,
        but same_modules('foo.bar', 'foo') will not.
        """
        modules1 = s1.split(".")
        modules2 = s2.split(".")

        return (
            len(modules1) <= len(modules2)
            and all(m1 == m2 for (m1, m2) in zip(modules1, modules2))
        )

    def visit_Import(self, node):
        import_names = [
            alias.name for alias in node.names
            if alias.name not in self.whitelisted_modules
        ]

        bad_import = any(
            self.same_modules(illegal_module, name)
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
            ".".join([node.module, alias.name])
            for alias in node.names
        ]
        from_import_names = [
            import_name for import_name in from_import_names
            if import_name not in self.whitelisted_modules
        ]

        bad_from_import = any(
            self.same_modules(illegal_module, name)
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
