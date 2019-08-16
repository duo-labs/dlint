#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import ast
import copy


class Namespace(object):
    def __init__(self, imports, from_imports):
        self.imports = imports
        self.from_imports = from_imports

    @classmethod
    def from_module_node(cls, module_node):
        # For now only add top-level, module imports. Let's avoid the rabbit
        # hole of looking at things like function and class-scope imports and
        # conditional imports in 'if' or 'try' statements
        if not isinstance(module_node, ast.Module):
            raise TypeError("only module-level imports are supported")

        imports = []
        from_imports = []

        for node in module_node.body:
            if isinstance(node, ast.Import):
                imports.append(copy.copy(node))
            elif isinstance(node, ast.ImportFrom):
                from_imports.append(copy.copy(node))

        return cls(imports, from_imports)

    def name_imported(self, name):
        def alias_includes_name(alias):
            return (
                (alias.name == name and alias.asname is None)
                or (alias.asname == name)
            )

        return any(
            alias_includes_name(alias)
            for imp in self.imports + self.from_imports
            for alias in imp.names
        )
