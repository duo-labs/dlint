#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from .helpers import bad_name_attribute_use


class BadZipfileUseLinter(bad_name_attribute_use.BadNameAttributeUseLinter):
    """This linter looks for use of the Python "zipfile" library
    "extract|extractall" function. These functions allows for arbitrary file
    overwrite.
    """
    off_by_default = False

    _code = 'DUO112'
    _error_tmpl = 'DUO112 use of "extract|extractall" not allowed'

    @property
    def illegal_name_attributes(self):
        return {
            "extract": [
                ["zipfile", "ZipFile"],
                ["ZipFile"],
            ],
            "extractall": [
                ["zipfile", "ZipFile"],
                ["ZipFile"],
            ]
        }
