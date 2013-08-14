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
