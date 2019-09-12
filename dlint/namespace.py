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
            raise TypeError('expected type ast.Module, received {}'.format(type(module_node)))

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

    def illegal_module_imported(self, module_path, illegal_module_path):
        modules = module_path.split('.')

        # 'm1.m2.m3.m4' -> ['m1', 'm1.m2', 'm1.m2.m3', 'm1.m2.m3.m4']
        nested_module_imports = [
            '.'.join(modules[:i + 1])
            for i in range(len(modules))
        ]
        nested_module_imported = any(
            (
                alias.name == nested_module_import
                and module_path == illegal_module_path
            )
            for imp in self.imports
            for alias in imp.names
            for nested_module_import in nested_module_imports
        )
        if nested_module_imported:
            return True

        nested_module_from_imported = any(
            (
                alias.name == modules[0]
                and (imp.module + '.' + module_path) == illegal_module_path
            )
            for imp in self.from_imports
            for alias in imp.names
            if imp.module is not None  # Relative import, e.g. 'from .'
        )
        if nested_module_from_imported:
            return True

        return False
