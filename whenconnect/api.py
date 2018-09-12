from collections import Iterable


def when_connect(device, do):
    if isinstance(device, str):
        return _connect_any(do)
    if isinstance(device, Iterable):
        return _connect_device(device, do)


def _connect_any(todo_list):
    return 'connect any, args: {}'.format(str(todo_list))


def _connect_device(device_list, todo_list):
    return 'connect device, args: {}, {}'.format(device_list, todo_list)


__all__ = [
    'when_connect',
]
