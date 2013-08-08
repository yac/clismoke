class TestFailed(RuntimeError):
    pass


def fail():
    raise TestFailed()

