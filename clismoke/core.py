import clismoke.log as log


class TestFailed(RuntimeError):
    pass


def fail(msg=None):
    if msg:
        log.error(msg)
        raise TestFailed(msg)
    else:
        raise TestFailed()

