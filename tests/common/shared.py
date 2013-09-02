import re
from time import sleep

from clismoke.sh import run
from clismoke.core import fail
import clismoke.log as log


def wait_for_output(command, pattern, timeout=30, period=1.0):
    t = 0.0
    while t < timeout:
        out = run(command)
        if re.search(pattern, out):
            log.info("Got desired output.")
            return
        sleep(period)
        t += period
        log.info("%g s remaining..." % (timeout - t))
    fail("Timeout: Command didn't return desired output within %d s." % timeout)


def test_version(cli, prefix=''):
    ver = run('%s --version 2>&1' % cli)
    if not re.match('%s[0-9]+.[0-9]+' % prefix, ver):
        fail("Weird version returned.")

def test_manpage(cli):
    man = run('man %s > /dev/null' % cli, fatal=False)
