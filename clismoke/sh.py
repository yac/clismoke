import core
import log
from log import term

import subprocess
import sys

class _CommandOutput(str):                                                    
    """
    Just a string subclass with atribute access.
    """
    @property
    def success(self):
        return (self.return_code == 0)


def log_cmd_fail(cmd, cout, fail_log_fun=log.warning, out_log_fun=log.info):
    fail_str = term.red('command failed:')
    fail_log_fun('%s %s' % (fail_str, cmd))
    if cout:
        out_log_fun(term.bold("stdout:"))
        out_log_fun(cout)
    if cout.stderr:
        out_log_fun(term.yellow("stderr:"))
        out_log_fun(cout.stderr)

def run(cmd, fatal=True, stdout=True, stderr=True):
    log.command('$ %s' % cmd)
    if stdout:
        sout = sys.stdout
    else:
        sout = subprocess.PIPE
    if stderr:
        serr = sys.stderr
    else:
        serr = subprocess.PIPE
    prc = subprocess.Popen(cmd, shell=True, stdout=sout, stderr=serr)
    out, err = prc.communicate()
    errcode = prc.returncode
    if out:
        out = out.rstrip()
    else:
        out = ''
    if err:
        err = err.rstrip()
    else:
        err = ''
    cout = _CommandOutput(out)
    cout.stderr = err
    cout.return_code = errcode
    if errcode != 0 and fatal:
        log_cmd_fail(cmd, cout)
        core.fail()
    return cout
