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
import optparse
import sys

from flake8 import style_guide

import dlint


class Flake8Extension(object):
    name = dlint.__name__
    version = dlint.__version__
    options = None

    def __init__(self, tree, filename):
        self.tree = tree
        self.filename = filename

    @classmethod
    def add_options(cls, parser):
        try:
            parser.add_option(
                '--print-dlint-linters',
                action='store_true',
                help='Print Dlint linter information.',
                parse_from_config=False
            )
        except optparse.OptionConflictError:
            # Occurs during development when flake8 detects the dlint package
            # twice: once because it's been installed in editable mode, and
            # once from the local filesystem directory. We can safely nop here
            # since the option(s) have already been added.
            pass

    @classmethod
    def parse_options(cls, options):
        if options.print_dlint_linters:
            code_prefix_len = 7
            linters = cls.get_linter_classes()
            output_lines = [
                "{} {} {}".format(l._code, l.__name__, l._error_tmpl[code_prefix_len:])
                for l in sorted(linters, key=lambda li: li._code)
            ]
            print("\n".join(output_lines))
            EX_OK = 0
            sys.exit(EX_OK)

        cls.options = options

    @classmethod
    def get_plugin_linter_classes(cls):
        module_prefix = 'dlint_plugin_'
        class_prefix = 'Dlint'

        plugin_modules = [
            importlib.import_module(name)
            for finder, name, ispkg in pkgutil.iter_modules()
            if name.startswith(module_prefix)
        ]
        plugin_classes = [
            inner_cls
            for module in plugin_modules
            for name, inner_cls in inspect.getmembers(module, predicate=inspect.isclass)
            if name.startswith(class_prefix)
        ]

        return plugin_classes

    @classmethod
    def get_linter_classes(cls):
        linter_classes = dlint.linters.ALL + tuple(cls.get_plugin_linter_classes())

        if cls.options:
            engine = style_guide.DecisionEngine(cls.options)
            selected = style_guide.Decision.Selected
            linter_classes = tuple(
                linter_class for linter_class in linter_classes
                if engine.decision_for(linter_class._code) is selected
            )

        return linter_classes

    def run(self):
        linter_instances = [l() for l in self.get_linter_classes()]
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
