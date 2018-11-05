"""
device object, offer device info and so on.
"""
from pyatool import PYAToolkit


class WCDevice(object):
    def __init__(self, device_id):
        self.device_id = device_id
        self._toolkit = PYAToolkit(device_id)

    def __getattr__(self, item):
        if not hasattr(self._toolkit, item):
            raise AttributeError('no function named {}'.format(item))
        return getattr(self._toolkit, item)

    def __str__(self):
        return '<WCDevice {}>'.format(self.device_id)


if __name__ == '__main__':
    wc_device = WCDevice('9c12aa96')
    wc_device.hello_world()
