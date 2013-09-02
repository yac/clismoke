#!/usr/bin/env python

import sys

if __name__ == '__main__':
    import common.direct_testing as testing
    testing.setup()

from clismoke.sh import run
from clismoke.core import fail
from clismoke.tester import run_tests_module

import common.shared as shared


def test_transfer():
    test_fn = 'test_file_abc'
    content = 'content'
    container = 'test-container'
    run("echo '%s' > %s" % (content, test_fn))
    run("swift upload %s %s" % (container, test_fn))
    l = run("swift list %s" % container)
    if l.find(test_fn) == -1:
        fail("Uploaded file not listed.")
    run("rm %s" % test_fn)
    run("swift download %s %s" % (container, test_fn))
    c = run("cat %s" % test_fn)
    if c != content:
        fail("Downloaded file content doesn't match.")

def test_version():
    shared.test_version('swift', prefix='swift ')

def test_manpage():
    shared.test_manpage('swift')



if __name__ == '__main__':
    run_tests_module(sys.modules[__name__])
