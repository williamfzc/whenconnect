import warnings
from whenconnect.logger import logger


# 事件注册
class TaskManager(object):
    #
    _operation_dict = {
        'any': '_register_any_task',
        'exactly': '_register_exactly_task',
    }

    # {device_id: { event_type: set([func1, func2]) }}
    # eg: { '123456F': { 'connect': set([func1, func2]), 'disconnect': set([func1, func2]) }, ...}
    _exactly_task_dict = dict()

    # { event_type: set([func1, func2]) }
    # { 'connect': set([func1, func2]), 'disconnect': set([func1, func2]) }
    _any_task_dict = dict()

    def __init__(self):
        raise NotImplementedError('should not init')

    @classmethod
    def _default_operation(cls, method_name):
        warnings.warn('operation {} not implemented'.format(method_name))
        raise NotImplementedError()

    @classmethod
    def _apply_operation(cls, method_name, *args, **kwargs):
        if method_name in cls._operation_dict:
            method_name = cls._operation_dict[method_name]
        func_item = getattr(cls, method_name, cls._default_operation)
        return func_item(*args, **kwargs)

    @classmethod
    def _register_any_task(cls, todo=None, event_type=None):
        if not todo:
            return
        if event_type not in cls._any_task_dict:
            cls._any_task_dict[event_type] = set()
        cls._any_task_dict[event_type].add(todo)
        logger.info('RESISTER ANY', func_name=todo.__name__)

    @classmethod
    def _register_exactly_task(cls, device_list=None, todo=None, event_type=None):
        for each_device in device_list:
            if each_device not in cls._exactly_task_dict:
                cls._exactly_task_dict[each_device] = dict()
            if event_type not in cls._exactly_task_dict[each_device]:
                cls._exactly_task_dict[each_device][event_type] = set()
            cls._exactly_task_dict[each_device][event_type].add(todo)
            logger.info('RESISTER EXACTLY', func_name=todo.__name__, device=each_device)

    @classmethod
    def register_task(cls, operate_type, *args, **kwargs):
        logger.info('START REGISTER', type=operate_type)
        cls._apply_operation(operate_type, *args, **kwargs)

    @classmethod
    def exec_task(cls, device_id, event_type):
        # any func
        func_list = cls._any_task_dict[event_type].copy()

        # exactly func
        if device_id in cls._exactly_task_dict:
            _exactly_func_list = cls._exactly_task_dict[device_id][event_type]
            func_list |= _exactly_func_list

        logger.info('ALL FUNC NEED EXEC', func_list=[i.__name__ for i in func_list])
        for each_func in func_list:
            logger.info('EXEC FUNC', func=each_func.__name__, device=device_id)
            each_func(device_id)
