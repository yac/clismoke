import log
from log import term
import core

from inspect import getmembers, isfunction



def run_tests_module(module):
    funs = [o for o in getmembers(module, isfunction)
                       if o[0].startswith('test_')]
    for name, fun in funs:
        log.info(term.bold("=== %s ===" % name))
        try:
            fun()
        except core.TestFailed as e:
            print term.bold_red("FAIL: %s" % name)
