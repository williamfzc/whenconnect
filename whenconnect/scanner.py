import ConnectionTracer
import functools
from whenconnect.logger import logger
from whenconnect.manager import TaskManager
from whenconnect import config


class DeviceManager(object):
    _devices = set()
    _update = False

    @classmethod
    def get_devices(cls):
        return cls._devices

    @classmethod
    def updating(cls):
        return cls._update

    @classmethod
    def set_devices(cls, current_devices):
        cls._update = True

        add_device_set = current_devices - cls._devices
        lost_device_set = cls._devices - current_devices

        cls._devices = current_devices
        cls._update = False

        # remove device
        for each_device in lost_device_set:
            logger.info('LOST DEVICE', device=each_device)
            TaskManager.exec_task(each_device, 'disconnect')

        # add device
        for each_device in add_device_set:
            logger.info('ADD DEVICE', device=each_device)
            TaskManager.exec_task(each_device, 'connect')


def update_current_devices(devices):
    DeviceManager.set_devices(devices)


def change_adb_port(new_port):
    ConnectionTracer.stop()
    ConnectionTracer.start(update_current_devices, port=new_port)


def api_wrapper(func):
    """ before API call, check connection first """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        check_scanner()
        return func(*args, **kwargs)
    return wrapper


def check_scanner():
    """ check connection, and start it if it did not start """
    if not ConnectionTracer.get_status():
        ConnectionTracer.start(update_current_devices, port=config.ADB_PORT)
