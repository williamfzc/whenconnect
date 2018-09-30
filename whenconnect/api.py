"""
- 外部调用API，进而启动core
    - 确认core状态
    - 传入参数，启动core
    - 返回
- core将初始化pipe初始化用于数据传递，并在子线程中启动scanner用于监听设备，并将三者互相绑定
"""

from whenconnect.manager import TaskManager
from whenconnect.core import start_detect
from whenconnect.scanner import get_device_list


def _get_task_type(device):
    if isinstance(device, str):
        return 'any'
    if isinstance(device, list):
        return 'specific'


def when_connect(device, do):
    return TaskManager.register_task(_get_task_type(device), event_type='connect', device_list=device, todo=do)


def when_disconnect(device, do):
    return TaskManager.register_task(_get_task_type(device), event_type='disconnect', device_list=device, todo=do)


def get_devices():
    return list(get_device_list())


__all__ = [
    'when_connect',
    'when_disconnect',
    'start_detect',
    'get_devices',
]
