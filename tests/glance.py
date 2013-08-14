#!/usr/bin/env python

import sys
import re
from time import sleep

if __name__ == '__main__':
    import common.direct_testing as testing
    testing.setup()

from clismoke.sh import run
from clismoke.core import fail
import clismoke.log as log
from clismoke.tester import run_tests_module
import common.shared as shared


INSTANCE = 'clismoke'


TEST_IMAGE_NAME = 'cirros-clismoke'
TEST_IMAGE_URL = 'https://launchpad.net/cirros/trunk/0.3.0/+download/cirros-0.3.0-x86_64-disk.img'


def get_test_image():
    log.info("Getting testing image...")
    run("glance image-create --name '%(name)s' --disk-format qcow2"
        " --container-format bare --copy-from '%(url)s'" %{
            'name': TEST_IMAGE_NAME,
            'url': TEST_IMAGE_URL
        })
    shared.wait_for_output("glance image-show '%s'" % TEST_IMAGE_NAME,
                           'status.*active')

def ensure_test_image():
    # This is needed by nova test as well, thus the separate function.
    o = run("glance image-list | grep '%s'" % TEST_IMAGE_NAME, fatal=False)
    if o.success:
        log.info("Testing image is present.")
        return
    get_test_image()

def test_image_basic():
    o = run("glance image-list | grep '%s'" % TEST_IMAGE_NAME, fatal=False)
    if o.success:
        run("glance image-delete '%s'" % TEST_IMAGE_NAME)
    get_test_image()
    run("glance image-delete '%s'" % TEST_IMAGE_NAME)

def test_packaging():
    man = run("man glance > /dev/null")
    ver = run("glance --version 2>&1")
    if not re.match('[0-9]+.[0-9]+', ver):
        fail("Weird version returned.")


if __name__ == '__main__':
    run_tests_module(sys.modules[__name__])
