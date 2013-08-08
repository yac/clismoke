#!/usr/bin/env python

import sys

if __name__ == '__main__':
    import _direct_testing
    _direct_testing.setup()

from clismoke.sh import run
from clismoke.tester import run_tests_module


def test_basic_cli():
    o = run("ls")


if __name__ == '__main__':
    run_tests_module(sys.modules[__name__])
