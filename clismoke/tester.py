import log
from log import term
import core
import sys

from inspect import getmembers, isfunction
import os.path


def get_requested_tests():
    tests = sys.argv[1:]
    if not tests:
        return tests
    def test_norm(name):
        if name.startswith('test_'):
            return name
        return "test_" + name
    return map(test_norm, tests)

def run_tests_module(module):
    module_name = os.path.basename(os.path.splitext(module.__file__)[0])
    funs = [o for o in getmembers(module, isfunction)
                       if o[0].startswith('test_')]
    selfuns = get_requested_tests()
    for name, fun in funs:
        if selfuns and name not in selfuns:
            continue
        label = "%s: %s" % (module_name, name)
        log.info(term.bold("=== %s ===" % label))
        try:
            fun()
            print term.bold_green("SUCCESS %s\n" % label)
        except core.TestFailed as e:
            print term.bold_red("FAIL %s\n" % label)
