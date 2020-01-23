#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import ast

from .helpers import bad_module_attribute_use
from . import base
from .. import redos


class BadReCatastrophicUseLinter(bad_module_attribute_use.BadModuleAttributeUseLinter):
    """This linter looks for regular expression catastrophic backtracking in
    the re module. Catastrophic backtracking can cause denial-of-service.

    Some people, when confronted with a problem, think
    "I know, I'll use regular expressions." Now they have two problems.
        * Jamie Zawinski, 1997: http://regex.info/blog/2006-09-15/247
    """
    off_by_default = False

    _code = 'DUO138'
    _error_tmpl = 'DUO138 catastrophic "re" usage - denial-of-service possible'

    @property
    def illegal_module_attributes(self):
        return {
            're': [
                'compile',
                'search',
                'match',
                'fullmatch',
                'split',
                'findall',
                'finditer',
                'sub',
                'subn',
            ],
            'django.core.validators': [
                'RegexValidator',
            ],
            'django.urls': [
                're_path',
            ]
        }

    def __init__(self, *args, **kwargs):
        self.calls = {}

        super(BadReCatastrophicUseLinter, self).__init__(*args, **kwargs)

    def visit_Call(self, node):
        self.generic_visit(node)

        self.calls[node.func] = node

    def get_results(self):
        pattern_argument_number = 0

        def pattern_is_catastrophic(node):
            call = self.calls.get(node)
            if call is None or not call.args:
                return False

            pattern = call.args[pattern_argument_number]

            # Only handle string literals for now
            if not isinstance(pattern, ast.Str):
                return False

            return redos.detect.catastrophic(pattern.s)

        return [
            base.Flake8Result(
                lineno=node.lineno,
                col_offset=node.col_offset,
                message=self._error_tmpl
            )
            for node in self.bad_nodes
            if pattern_is_catastrophic(node)
        ]
