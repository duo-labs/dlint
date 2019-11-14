#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import ast
import copy

from . import util


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
        modules = module_path.split('.') if module_path else []
        illegal_modules = illegal_module_path.split('.')

        module_imported = False
        canonicalized_modules = modules

        for imp in self.imports:
            for alias in imp.names:
                if util.lstartswith(illegal_modules, alias.name.split('.')):
                    module_imported = True
                if modules and modules[0] == alias.asname:
                    # 'import foo.bar as baz', 'baz.qux' -> 'foo.bar.baz'
                    canonicalized_modules = alias.name.split('.') + modules[1:]

        for imp in self.from_imports:
            if not imp.module:
                continue  # Relative import, e.g. 'from .'

            imp_modules = imp.module.split('.')

            for alias in imp.names:
                if util.lstartswith(illegal_modules, imp_modules + [alias.name]):
                    module_imported = True
                if modules and modules[0] in [alias.name, alias.asname]:
                    # 'from foo.bar import baz as qux', 'qux.quine' -> 'foo.bar.baz.quine'
                    canonicalized_modules = imp_modules + [alias.name] + modules[1:]
                if (util.lstartswith(illegal_modules, imp_modules)
                        and illegal_modules[len(imp_modules):] == modules
                        and alias.name == '*'):
                    # 'from foo.bar import *', 'baz.qux' -> 'foo.bar.baz.qux'
                    module_imported = True
                    canonicalized_modules = imp_modules + modules

        return module_imported and (canonicalized_modules == illegal_modules)
