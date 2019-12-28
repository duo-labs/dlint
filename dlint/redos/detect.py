#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import sre_constants
import sre_parse

import itertools


class OpNode(object):

    def __init__(self, op, args):
        self.op = op
        self.args = args
        self.children = []

    def __str__(self, level=0):
        result = (
            "  " * level
            + "{}: {}".format(self.op, self.args)
            + "\n"
        )

        for child in self.children:
            result += child.__str__(level + 1)

        return result

    def __repr__(self):
        return "<OpNode - op={} args={}>".format(self.op, self.args)


def build_op_tree(node, subpattern):
    for op, av in subpattern.data:
        args = []
        subpatterns = []

        if op is sre_constants.BRANCH:
            for a in av[1]:
                subpatterns.append(a)
        elif op is sre_constants.GROUPREF_EXISTS:
            condgroup, item_yes, item_no = av
            subpatterns.append(item_yes)
            if item_no:
                subpatterns.append(item_no)
        elif isinstance(av, (tuple, list)):
            for a in av:
                if isinstance(a, sre_parse.SubPattern):
                    subpatterns.append(a)
                else:
                    args.append(a)
        else:
            args.append(av)

        new_node = OpNode(op, tuple(args))
        for sp in subpatterns:
            build_op_tree(new_node, sp)

        node.children.append(new_node)


def large_repeat(node):
    repeat_min, repeat_max = node.args

    # Repetition sizes that cause catastrophic backtracking depend on many
    # factors including subject length, machine hardware, and the repetition
    # size itself. This value was mostly arbitrarily chosen after running a
    # few basic catastrophic cases. We may consider making it configurable
    # in the future.
    large_max = 10

    return (
        repeat_max is sre_constants.MAXREPEAT  # e.g. '{min,}', '+', '*'
        or repeat_max >= large_max
    )


def max_nested_quantifiers(node):
    if not node.children:
        return 0

    child_max = max(
        max_nested_quantifiers(child)
        for child in node.children
    )
    is_large_repeat = int(
        node.op in sre_parse._REPEATCODES
        and large_repeat(node)
    )

    return is_large_repeat + child_max


def inclusive_alternation_branch(branch_node):
    anys = [
        child for child in branch_node.children
        if child.op is sre_constants.ANY
    ]

    literals = [
        child for child in branch_node.children
        if child.op is sre_constants.LITERAL
    ]

    not_literals = [
        child for child in branch_node.children
        if child.op is sre_constants.NOT_LITERAL
    ]

    negate_literals = [
        child for child in branch_node.children
        if (
            child.op is sre_constants.IN
            and child.args
            and child.args[0][0] is sre_constants.NEGATE
            and child.args[0][1] is None
        )
    ]

    ins = [
        child for child in branch_node.children
        if child.op is sre_constants.IN
    ]

    ranges = [
        (node_type, args)
        for _in in ins
        for node_type, args in _in.args
        if node_type is sre_constants.RANGE
    ]

    def any_overlap():
        return bool(anys)

    def literal_overlap():
        return any(
            _range[1][0] <= literal.args[0] <= _range[1][1]
            for literal, _range in itertools.product(literals, ranges)
        )

    def not_literal_overlap():
        ranges_values = set()
        ranges_values.update(*[
            [i for i in range(_range[1][0], _range[1][1] + 1)]
            for _range in ranges
        ])
        ranges_values.difference_update([
            not_literal.args[0] for not_literal in not_literals
        ])

        return not_literals and bool(ranges_values)

    def negate_literal_overlap():
        in_literals = [
            (node_type, arg)
            for _in in negate_literals
            for node_type, arg in _in.args
            if node_type is sre_constants.LITERAL
        ]

        ranges_values = set()
        ranges_values.update(*[
            [i for i in range(_range[1][0], _range[1][1] + 1)]
            for _range in ranges
        ])
        ranges_values.difference_update([
            negate_literal[1] for negate_literal in in_literals
        ])

        return negate_literals and bool(ranges_values)

    def range_overlap():
        return any(
            r1[1][0] <= r2[1][0] <= r1[1][1]
            or r1[1][0] <= r2[1][1] <= r1[1][1]
            for r1, r2 in itertools.combinations(ranges, 2)
        )

    return any(
        fn() for fn in [  # Lazily evaluate
            any_overlap,
            literal_overlap,
            not_literal_overlap,
            negate_literal_overlap,
            range_overlap,
        ]
    )


def mutually_inclusive_alternation_helper(node, nested_quantifier):
    if not node.children:
        return False

    nested_quantifier = nested_quantifier or node.op in sre_parse._REPEATCODES

    inclusive_alternation = False
    if node.op is sre_constants.BRANCH:
        inclusive_alternation = inclusive_alternation_branch(node)

    for child in node.children:
        return (
            (nested_quantifier and inclusive_alternation)
            or mutually_inclusive_alternation_helper(child, nested_quantifier)
        )


def mutually_inclusive_alternation(node):
    return mutually_inclusive_alternation_helper(node, False)


def catastrophic(pattern):
    subpattern = sre_parse.parse(pattern)
    root = OpNode(None, ())

    build_op_tree(root, subpattern)
    nested_quantifiers = max_nested_quantifiers(root) > 1
    alternation = mutually_inclusive_alternation(root)

    return any([
        nested_quantifiers,
        alternation
    ])


def dump(pattern):
    subpattern = sre_parse.parse(pattern)
    subpattern.dump()


def dump_tree(pattern):
    subpattern = sre_parse.parse(pattern)
    root = OpNode(None, ())
    build_op_tree(root, subpattern)
    print(root)
