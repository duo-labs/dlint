#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import importlib
import inspect
import os
import pkgutil
import sys

import dlint


class Flake8Extension(object):
    name = dlint.__name__
    version = dlint.__version__

    def __init__(self, tree, filename):
        self.tree = tree
        self.filename = filename

    @classmethod
    def add_options(cls, parser):
        parser.add_option(
            '--print-dlint-linters',
            action='store_true',
            help='Print Dlint linter information.',
            parse_from_config=False
        )

    @classmethod
    def parse_options(cls, options):
        if options.print_dlint_linters:
            code_prefix_len = 7
            linters = Flake8Extension.get_linter_classes()
            output_lines = [
                "{} {} {}".format(l._code, l.__name__, l._error_tmpl[code_prefix_len:])
                for l in sorted(linters, key=lambda li: li._code)
            ]
            print("\n".join(output_lines))
            sys.exit(os.EX_OK)

    @staticmethod
    def get_plugin_linter_classes():
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

    @staticmethod
    def get_linter_classes():
        return dlint.linters.ALL + tuple(Flake8Extension.get_plugin_linter_classes())

    def run(self):
        linter_instances = [l() for l in Flake8Extension.get_linter_classes()]
        multi_visitor = dlint.multi.MultiNodeVisitor(linter_instances)
        multi_visitor.visit(self.tree)

        for linter_instance in linter_instances:
            for result in linter_instance.get_results():
                yield (
                    result.lineno,
                    result.col_offset,
                    result.message,
                    type(linter_instance)
                )
