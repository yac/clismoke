#!/usr/bin/env python

import sys

if __name__ == '__main__':
    import common.direct_testing as testing
    testing.setup()

from clismoke.sh import run
from clismoke.core import fail
from clismoke import log
from clismoke.tester import run_tests_module

import common.shared as shared


TEST_VOLUME_NAME = 'test_volume_clismoke'
TEST_SNAPSHOT_NAME = 'test_snapshot_clismoke'


def test_basic():
    o = run("cinder list | grep '%s'" % TEST_VOLUME_NAME, fatal=False)
    if o.success:
        log.info("Testing volume already present...")
    else:
        run("cinder create --display-name '%s' 1" % TEST_VOLUME_NAME)
        shared.wait_for_output("cinder show '%s'" % TEST_VOLUME_NAME,
                               'status.*(available|active)')
    o = run("cinder show test_volume_clismoke")
    volume_id = shared.parse_id(o)
    o = run("cinder snapshot-create --display-name '%s' '%s'" % (TEST_SNAPSHOT_NAME, volume_id))
    snapshot_id = shared.parse_id(o)
    shared.wait_for_output("cinder snapshot-show '%s'" % snapshot_id,
                           'status.*available')
    run("cinder snapshot-list --volume-id '%s' | grep '%s'" % (volume_id, snapshot_id))
    run("cinder snapshot-delete '%s'" % snapshot_id)
    shared.wait_for_returncode("cinder snapshot-show '%s'" % snapshot_id, 1)
    run("cinder delete '%s'" % volume_id)


def test_version():
    shared.test_version('cinder')

def test_manpage():
    shared.test_manpage('cinder')



if __name__ == '__main__':
    run_tests_module(sys.modules[__name__])
