#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import argparse
import sys

from dlint import redos


def parse_args():
    p = argparse.ArgumentParser(description='''
        Detect redos regular expression patterns from the command-line.
        ''', formatter_class=argparse.RawTextHelpFormatter)

    p.add_argument(
        '-p',
        '--pattern',
        action='store',
        required=True,
        help='regular expression pattern'
    )

    dump_group = p.add_mutually_exclusive_group()

    dump_group.add_argument(
        '-d',
        '--dump',
        action='store_true',
        help='print parsed pattern'
    )
    dump_group.add_argument(
        '-t',
        '--dump-tree',
        action='store_true',
        help='print parsed op node tree'
    )

    args = p.parse_args()

    return args


def main():
    args = parse_args()

    if args.dump:
        redos.detect.dump(args.pattern)
        return

    if args.dump_tree:
        redos.detect.dump_tree(args.pattern)
        return

    if args.pattern == '-':
        pattern = sys.stdin.read()
    else:
        pattern = args.pattern

    print((pattern, redos.detect.catastrophic(pattern)))


if __name__ == "__main__":
    main()
