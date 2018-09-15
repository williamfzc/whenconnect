"""
# 单例
# 提供事件注册API
# 维护queue
# 维护scanner
"""
import structlog
import threading
from whenconnect.pipe import event_queue
from whenconnect.scanner import loop_get_device_list

logger = structlog.getLogger()

# 事件注册

# {
#     device_id: [func1, func2],
# }
_EXACTLY_TASK_DICT = {}

# any
_ANY_TASK_LIST = []


def _register_any_task(todo=None):
    if not todo:
        return
    global _ANY_TASK_LIST
    _ANY_TASK_LIST.append(todo)
    logger.info('RESISTER ANY', func_name=todo.__name__)


def _register_exactly_task(device_list=None, todo=None):
    for each_device in device_list:
        if each_device not in _EXACTLY_TASK_DICT:
            _EXACTLY_TASK_DICT[each_device] = []
        _EXACTLY_TASK_DICT[each_device].append(todo)
        logger.info('RESISTER EXACTLY', func_name=todo.__name__, device=each_device)


_operator_map = {
    'any': _register_any_task,
    'exactly': _register_exactly_task,
}


def register_task(operate_type, *args, **kwargs):
    logger.info('START REGISTER', type=operate_type)
    _operator_map[operate_type](*args, **kwargs)


def exec_task(device_id):
    # any func
    func_list = _ANY_TASK_LIST
    # exactly func
    if device_id in _EXACTLY_TASK_DICT:
        func_list += _EXACTLY_TASK_DICT[device_id]

    for each_func in func_list:
        logger.info('EXEC FUNC', func=each_func.__name__, device=device_id)
        each_func(device_id)


# device loop
threading.Thread(target=loop_get_device_list).start()


# queue handler
def handle_event():
    last_device_list = []
    while True:
        current_device_list = event_queue.get(timeout=2)
        # nothing different
        if last_device_list == current_device_list:
            continue
        # something changed
        diff_device_list = [i for i in current_device_list if i not in last_device_list]
        # less device
        if not diff_device_list:
            last_device_list = current_device_list
            continue
        # more device
        logger.info('DEVICE ADDED', device=diff_device_list)
        for each_device in diff_device_list:
            exec_task(each_device)
        last_device_list = current_device_list


threading.Thread(target=handle_event).start()
