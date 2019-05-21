#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from .helpers import bad_kwarg_use

from .. import tree


class BadXmlrpcUseLinter(bad_kwarg_use.BadKwargUseLinter):
    """This linter looks for unsage usage of the
    "SimpleXMLRPCServer.register_instance" function. Note that in Python 3
    this module is called "xmlrpc.server", but this linter still works because
    the attribute name is the same. Unsafe usage looks like:

        "Enabling the allow_dotted_names option allows intruders to access your
        module's global variables and may allow intruders to execute arbitrary
        code on your machine. Only use this option on a secure, closed network."

    https://docs.python.org/2/library/simplexmlrpcserver.html
    """
    off_by_default = False

    _code = 'DUO124'
    _error_tmpl = 'DUO124 instance with "allow_dotted_names" enabled is unsafe'

    @property
    def kwargs(self):
        return [
            {
                "attribute_name": "register_instance",
                "kwarg_name": "allow_dotted_names",
                "predicate": tree.kwarg_true,
            },
        ]
