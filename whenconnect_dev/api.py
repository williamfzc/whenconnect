from whenconnect_dev.scanner import DeviceManager


def when_connect(device, do):
    return


def when_disconnect(device, do):
    return


def get_devices():
    return DeviceManager.get_devices()


def get_tasks():
    return


__all__ = [
    # register
    'when_connect',
    'when_disconnect',

    # get info
    'get_devices',
    'get_tasks',
]
