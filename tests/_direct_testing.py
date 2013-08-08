import os.path
import sys

def setup():
    """
    Add parent directory to python path so that tests can import clismoke from
    there.
    """
    module_dir, _ = os.path.split(os.path.dirname(__file__))
    sys.path.insert(0, module_dir)
