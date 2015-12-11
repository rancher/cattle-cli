#!/usr/bin/env python
import time
import gdapi
import os
from gdapi import *  # NOQA

DEFAULT_TIMEOUT = 45


class Client(gdapi.Client):
    def __init__(self, *args, **kw):
        super(Client, self).__init__(*args, **kw)

    def wait_success(self, obj, timeout=-1):
        obj = self.wait_transitioning(obj, timeout)
        if obj.transitioning != 'no':
            raise gdapi.ClientApiError(obj.transitioningMessage)
        return obj

    def wait_transitioning(self, obj, timeout=-1, sleep=0.01):
        timeout = _get_timeout(timeout)
        start = time.time()
        obj = self.reload(obj)
        while obj.transitioning == 'yes':
            time.sleep(sleep)
            sleep *= 2
            if sleep > 2:
                sleep = 2
            obj = self.reload(obj)
            delta = time.time() - start
            if delta > timeout:
                msg = 'Timeout waiting for [{}:{}] to be done after {} seconds'.format(obj.type, obj.id, delta)
                raise Exception(msg)

        return obj


def _get_timeout(timeout):
    if timeout == -1:
        return DEFAULT_TIMEOUT
    return timeout


def from_env(prefix='CATTLE_', **kw):
    return gdapi.from_env(prefix=prefix, factory=Client, **kw)


def _main():
    if 'CATTLE_URL' not in os.environ:
        os.environ['CATTLE_URL'] = 'http://localhost:8080/v1'

    gdapi._main()

if __name__ == '__main__':
    _main()
