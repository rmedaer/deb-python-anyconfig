#
# Copyright (C) 2012 - 2017 Satoru SATOH <ssato @ redhat.com>
# License: MIT
#
# pylint: disable=missing-docstring,invalid-name,too-few-public-methods
# pylint: disable=ungrouped-imports
from __future__ import absolute_import

import anyconfig.backend.json as TT
import tests.backend.common as TBC

from anyconfig.compat import OrderedDict


CNF_0_S = """{
  "a": 0,
  "b": "bbb",
  "c": 5,

  "sect0": {
    "d": ["x", "y", "z"]
  }
}
"""

CNF_0 = OrderedDict((("a", 0), ("b", "bbb"), ("c", 5),
                     ("sect0", OrderedDict((("d", ["x", "y", "z"]), )))))


class HasParserTrait(TBC.HasParserTrait):

    psr = TT.Parser()
    cnf_s = CNF_0_S
    cnf = CNF_0


class Test_10(TBC.Test_10_dumps_and_loads, HasParserTrait):

    load_options = dump_options = dict(parse_int=None, indent=2)


class Test_20(TBC.Test_20_dump_and_load, HasParserTrait):

    pass

# vim:sw=4:ts=4:et:
