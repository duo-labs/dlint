#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from .helpers import bad_kwarg_use

from .. import tree


class BadDefusedxmlUseLinter(bad_kwarg_use.BadKwargUseLinter):
    """This linter looks for lack of "defusedxml" parsing defenses. The
    "defusedxml" library offers "forbid_dtd", "forbid_entities", and
    "forbid_external" keyword arguments to prevent various XML attack
    vectors[1]. All defenses should be enabled.

    [1] https://pypi.org/project/defusedxml/
    """
    off_by_default = False

    _code = 'DUO135'
    _error_tmpl = 'DUO135 enable all "forbid_*" defenses when using "defusedxml" parsing'

    @property
    def kwargs(self):
        return [
            {
                "module_path": "defusedxml.lxml.fromstring",
                "kwarg_name": "forbid_dtd",
                "predicate": tree.kwarg_not_present,
            },
            {
                "module_path": "defusedxml.lxml.iterparse",
                "kwarg_name": "forbid_dtd",
                "predicate": tree.kwarg_not_present,
            },
            {
                "module_path": "defusedxml.lxml.parse",
                "kwarg_name": "forbid_dtd",
                "predicate": tree.kwarg_not_present,
            },
            {
                "module_path": "defusedxml.lxml.fromstring",
                "kwarg_name": "forbid_entities",
                "predicate": tree.kwarg_false,
            },
            {
                "module_path": "defusedxml.lxml.iterparse",
                "kwarg_name": "forbid_entities",
                "predicate": tree.kwarg_false,
            },
            {
                "module_path": "defusedxml.lxml.parse",
                "kwarg_name": "forbid_entities",
                "predicate": tree.kwarg_false,
            },
            {
                "module_path": "defusedxml.lxml.fromstring",
                "kwarg_name": "forbid_external",
                "predicate": tree.kwarg_false,
            },
            {
                "module_path": "defusedxml.lxml.iterparse",
                "kwarg_name": "forbid_external",
                "predicate": tree.kwarg_false,
            },
            {
                "module_path": "defusedxml.lxml.parse",
                "kwarg_name": "forbid_external",
                "predicate": tree.kwarg_false,
            },
            {
                "module_path": "defusedxml.cElementTree.fromstring",
                "kwarg_name": "forbid_dtd",
                "predicate": tree.kwarg_not_present,
            },
            {
                "module_path": "defusedxml.cElementTree.iterparse",
                "kwarg_name": "forbid_dtd",
                "predicate": tree.kwarg_not_present,
            },
            {
                "module_path": "defusedxml.cElementTree.parse",
                "kwarg_name": "forbid_dtd",
                "predicate": tree.kwarg_not_present,
            },
            {
                "module_path": "defusedxml.cElementTree.fromstring",
                "kwarg_name": "forbid_entities",
                "predicate": tree.kwarg_false,
            },
            {
                "module_path": "defusedxml.cElementTree.iterparse",
                "kwarg_name": "forbid_entities",
                "predicate": tree.kwarg_false,
            },
            {
                "module_path": "defusedxml.cElementTree.parse",
                "kwarg_name": "forbid_entities",
                "predicate": tree.kwarg_false,
            },
            {
                "module_path": "defusedxml.cElementTree.fromstring",
                "kwarg_name": "forbid_external",
                "predicate": tree.kwarg_false,
            },
            {
                "module_path": "defusedxml.cElementTree.iterparse",
                "kwarg_name": "forbid_external",
                "predicate": tree.kwarg_false,
            },
            {
                "module_path": "defusedxml.cElementTree.parse",
                "kwarg_name": "forbid_external",
                "predicate": tree.kwarg_false,
            },
            {
                "module_path": "defusedxml.ElementTree.fromstring",
                "kwarg_name": "forbid_dtd",
                "predicate": tree.kwarg_not_present,
            },
            {
                "module_path": "defusedxml.ElementTree.iterparse",
                "kwarg_name": "forbid_dtd",
                "predicate": tree.kwarg_not_present,
            },
            {
                "module_path": "defusedxml.ElementTree.parse",
                "kwarg_name": "forbid_dtd",
                "predicate": tree.kwarg_not_present,
            },
            {
                "module_path": "defusedxml.ElementTree.fromstring",
                "kwarg_name": "forbid_entities",
                "predicate": tree.kwarg_false,
            },
            {
                "module_path": "defusedxml.ElementTree.iterparse",
                "kwarg_name": "forbid_entities",
                "predicate": tree.kwarg_false,
            },
            {
                "module_path": "defusedxml.ElementTree.parse",
                "kwarg_name": "forbid_entities",
                "predicate": tree.kwarg_false,
            },
            {
                "module_path": "defusedxml.ElementTree.fromstring",
                "kwarg_name": "forbid_external",
                "predicate": tree.kwarg_false,
            },
            {
                "module_path": "defusedxml.ElementTree.iterparse",
                "kwarg_name": "forbid_external",
                "predicate": tree.kwarg_false,
            },
            {
                "module_path": "defusedxml.ElementTree.parse",
                "kwarg_name": "forbid_external",
                "predicate": tree.kwarg_false,
            },
        ]
