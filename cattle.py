#!/usr/bin/env python
import time
import gdapi
import os
from gdapi import *  # NOQA

DEFAULT_TIMEOUT = 45


class Client(gdapi.Client):
    def __init__(self, *args, **kw):
        super(Client, self).__init__(*args, **kw)

    def wait_success(self, obj, timeout=DEFAULT_TIMEOUT):
        obj = self.wait_transitioning(obj, timeout)
        if obj.transitioning != 'no':
            raise gdapi.ClientApiError(obj.transitioningMessage)
        return obj

    def wait_transitioning(self, obj, timeout=DEFAULT_TIMEOUT):
        start = time.time()
        obj = self.reload(obj)
        while obj.transitioning == 'yes':
            time.sleep(.5)
            obj = self.reload(obj)
            if time.time() - start > timeout:
                msg = 'Timeout waiting for [{0}] to be done'.format(obj)
                raise Exception(msg)

        return obj


def from_env(prefix='CATTLE_', **kw):
    return gdapi.from_env(prefix=prefix, factory=Client, **kw)


def _main():
    if 'CATTLE_URL' not in os.environ:
        os.environ['CATTLE_URL'] = 'http://localhost:8080/v1'

    gdapi._main()

if __name__ == '__main__':
    _main()
