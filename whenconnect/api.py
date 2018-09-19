"""
- 外部调用API，进而启动core
    - 确认core状态
    - 传入参数，启动core
    - 返回
- core将初始化pipe初始化用于数据传递，并在子线程中启动scanner用于监听设备，并将三者互相绑定
"""

from collections import Iterable
from whenconnect.manager import TaskManager
from whenconnect.core import start_detect


def when_connect(device, do):
    if isinstance(device, str):
        return TaskManager.register_task('any', event_type='connect', todo=do)
    if isinstance(device, Iterable):
        return TaskManager.register_task('exactly', event_type='connect', device_list=device, todo=do)


def when_disconnect(device, do):
    if isinstance(device, str):
        return TaskManager.register_task('any', event_type='disconnect', todo=do)
    if isinstance(device, Iterable):
        return TaskManager.register_task('exactly', event_type='disconnect', device_list=device, todo=do)


__all__ = [
    'when_connect',
    'when_disconnect',
    'start_detect'
]
