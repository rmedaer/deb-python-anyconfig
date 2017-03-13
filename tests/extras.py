#
# Copyright (C) 2016 Satoru SATOH <ssato @ redhat.com>
# License: MIT
#
# pylint: disable=missing-docstring
from __future__ import absolute_import

import unittest
import sys


class TestImportErrors(unittest.TestCase):

    def test_10_ac_compat(self):
        fun = "NullHandler"
        sys.modules["logging"] = None
        import anyconfig.compat

        self.assertFalse(fun in globals())
        self.assertFalse(getattr(anyconfig.compat, fun) is None)

    def test_20_ac_backends(self):
        for mod in ("yaml", "configobj", "msgpack", "toml", "bson"):
            sys.modules[mod] = None
            import anyconfig.backends

            self.assertTrue(sys.modules[mod] is None)
            self.assertFalse(anyconfig.backends is None)

    def test_30_ac_schema(self):
        mod = "jsonschema"
        sys.modules[mod] = None
        import anyconfig.schema

        self.assertTrue(sys.modules[mod] is None)
        self.assertFalse(anyconfig.schema is None)

# vim:sw=4:ts=4:et:
