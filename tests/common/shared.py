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

def wait_for_returncode(command, return_code, timeout=30, period=1.0):
    t = 0.0
    while t < timeout:
        out = run(command, fatal=False)
        if out.return_code == return_code:
            log.info("Got desired return code.")
            return
        sleep(period)
        t += period
        log.info("%g s remaining..." % (timeout - t))
    fail("Timeout: Command didn't return desired return code within %d s." % timeout)

def parse_id(output):
    m = re.search('^\|\s+id\s+\|\s(\S+)\s\|', output, flags=re.M)
    if not m:
        raise fail("Failed to parse ID from command output.")
    return m.group(1)

def test_version(cli, prefix=''):
    ver = run('%s --version 2>&1' % cli)
    if not re.match('%s[0-9]+.[0-9]+' % prefix, ver):
        fail("Weird version returned.")

def test_manpage(cli):
    man = run('man %s > /dev/null' % cli, fatal=False)
    if not man.success:
        fail("No man page for %s" % cli)
