"""
- 外部调用API，进而启动core
    - 确认core状态
    - 传入参数，启动core
    - 返回
- core将初始化pipe初始化用于数据传递，并在子线程中启动scanner用于监听设备，并将三者互相绑定
"""
import time

from whenconnect.manager import TaskManager
from whenconnect.scanner import DeviceManager, api_wrapper


def _get_task_type(device):
    if isinstance(device, str):
        return 'any'
    if isinstance(device, list):
        return 'specific'


@api_wrapper
def when_connect(device, do):
    return TaskManager.register_task(_get_task_type(device), event_type='connect', device_list=device, todo=do)


@api_wrapper
def when_disconnect(device, do):
    return TaskManager.register_task(_get_task_type(device), event_type='disconnect', device_list=device, todo=do)


@api_wrapper
def get_devices():
    while DeviceManager.updating():
        time.sleep(0.1)
    return DeviceManager.get_devices()


@api_wrapper
def get_current_task(task_type=None):
    time.sleep(0.1)
    current_task_dict = TaskManager.get_task_dict()
    if task_type and task_type in current_task_dict:
        return current_task_dict[task_type]
    return current_task_dict


__all__ = [
    # register
    'when_connect',
    'when_disconnect',

    # get info
    'get_devices',
    'get_current_task',
]
