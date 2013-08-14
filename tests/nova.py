#!/usr/bin/env python

import sys
from time import sleep

if __name__ == '__main__':
    import common.direct_testing as testing
    testing.setup()

from clismoke.sh import run
from clismoke.core import fail
from clismoke.tester import run_tests_module

import common.shared as shared
import glance


INSTANCE = 'clismoke'


def get_new_instance_name():
    ilist = run("nova list")
    i = 1
    while True:
        instance = "%s-%d" % (INSTANCE, i)
        if ilist.find(instance) == -1:
            return instance
        i += 1
        if i > 1000:
            fail("Failed to get non-conflicting name for new instance.")


def test_boot():
    run("nova help > /dev/null")
    run("nova service-list")
    glance.ensure_test_image()
    iname = get_new_instance_name()
    run("nova boot --flavor 1 --image %(image)s %(name)s" % {
        'image': glance.TEST_IMAGE_NAME,
        'name': iname
    })
    run("nova show %s" % iname)
    sleep(0.5)
    run("nova delete %s" % iname)

def test_version():
    shared.test_version('nova')

def test_manpage():
    shared.test_manpage('nova')



if __name__ == '__main__':
    run_tests_module(sys.modules[__name__])
