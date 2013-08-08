#!/usr/bin/env python

import sys

if __name__ == '__main__':
    import common.direct_testing as testing
    testing.setup()

from clismoke.sh import run
from clismoke.tester import run_tests_module
import common.shared as shared


def test_basic_cli():
    shared.ensure_test_image()
    o = run("nova list")


if __name__ == '__main__':
    run_tests_module(sys.modules[__name__])
