import ConnectionTracer
from whenconnect.logger import logger
from whenconnect.manager import TaskManager


class DeviceManager(object):
    _devices = set()

    @classmethod
    def get_devices(cls):
        return cls._devices

    @classmethod
    def set_devices(cls, current_devices):
        add_device_set = current_devices - cls._devices
        lost_device_set = cls._devices - current_devices

        # remove device
        for each_device in lost_device_set:
            logger.info('LOST DEVICE', device=each_device)
            TaskManager.exec_task(each_device, 'disconnect')

        # add device
        for each_device in add_device_set:
            logger.info('ADD DEVICE', device=each_device)
            TaskManager.exec_task(each_device, 'connect')

        cls._devices = current_devices


def update_current_devices(devices):
    DeviceManager.set_devices(devices)


def change_adb_port(new_port):
    ConnectionTracer.stop()
    ConnectionTracer.config = new_port
    ConnectionTracer.start(update_current_devices)


ConnectionTracer.start(update_current_devices)
