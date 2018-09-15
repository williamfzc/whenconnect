"""
- 外部调用API，进而启动core
    - 确认core状态
    - 传入参数，启动core
    - 返回
- core将初始化pipe初始化用于数据传递，并在子线程中启动scanner用于监听设备，并将三者互相绑定
"""

from collections import Iterable
from whenconnect.core import api_handler


def when_connect(device, do):
    if isinstance(device, str):
        return api_handler('any', todo_list=do)
    if isinstance(device, Iterable):
        return api_handler('exactly', device_list=device, todo_list=do)


__all__ = [
    'when_connect',
]
