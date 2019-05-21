#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from .helpers import bad_name_attribute_use


class BadTarfileUseLinter(bad_name_attribute_use.BadNameAttributeUseLinter):
    """This linter looks for use of the Python "tarfile" library
    "extract|extractall" function. These functions allows for arbitrary file
    overwrite.
    """
    off_by_default = False

    _code = 'DUO115'
    _error_tmpl = 'DUO115 use of "extract|extractall" not allowed'

    @property
    def illegal_name_attributes(self):
        return {
            "extract": [
                ["tarfile", "TarFile", "open"],
                ["tarfile", "TarFile"],
                ["TarFile", "open"],
                ["TarFile"],
            ],
            "extractall": [
                ["tarfile", "TarFile", "open"],
                ["tarfile", "TarFile"],
                ["TarFile", "open"],
                ["TarFile"],
            ]
        }
