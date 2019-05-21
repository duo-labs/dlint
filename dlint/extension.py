#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import importlib
import inspect
import pkgutil

import dlint


class Flake8Extension(object):
    name = dlint.__name__
    version = dlint.__version__

    def __init__(self, tree, filename):
        self.tree = tree
        self.filename = filename

    @staticmethod
    def get_plugin_classes():
        module_prefix = 'dlint_plugin_'
        class_prefix = 'Dlint'

        plugin_modules = [
            importlib.import_module(name)
            for finder, name, ispkg in pkgutil.iter_modules()
            if name.startswith(module_prefix)
        ]
        plugin_classes = [
            cls
            for module in plugin_modules
            for name, cls in inspect.getmembers(module, predicate=inspect.isclass)
            if name.startswith(class_prefix)
        ]

        return plugin_classes

    def run(self):
        plugin_classes = self.get_plugin_classes()
        linters = dlint.linters.ALL + tuple(plugin_classes)

        for linter in linters:
            linter_instance = linter()
            linter_instance.visit(self.tree)

            for result in linter_instance.get_results():
                yield (
                    result.lineno,
                    result.col_offset,
                    result.message,
                    linter
                )
