"""
# 单例
# 提供事件注册API
# 维护queue
# 维护scanner
"""

# 事件注册

# {
#     device_id: [func1, func2],
# }
_EXACTLY_TASK_DICT = {}

# any
_ANY_TASK_LIST = []


def _register_any_task(todo=None):
    global _ANY_TASK_LIST
    _ANY_TASK_LIST.append(todo)


def _register_exactly_task(device_list=None, todo=None):
    for each_device in device_list:
        if each_device not in _EXACTLY_TASK_DICT:
            _EXACTLY_TASK_DICT[each_device] = []
        _EXACTLY_TASK_DICT[each_device].append(todo)


_operator_map = {
    'any': _register_any_task,
    'exactly': _register_exactly_task,
}


def register_task(operate_type, *args, **kwargs):
    _operator_map[operate_type](*args, **kwargs)
