import ConnectionTracer


class DeviceManager(object):
    _devices = set()

    @classmethod
    def get_devices(cls):
        return cls._devices

    @classmethod
    def set_devices(cls, value):
        print('something changed')
        cls._devices = value


def update_current_devices(devices):
    DeviceManager.set_devices(devices)


ConnectionTracer.start(update_current_devices)
