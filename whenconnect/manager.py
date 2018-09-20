import warnings
from whenconnect.logger import logger


# 事件注册
class TaskManager(object):
    #
    _operation_dict = {
        'any': '_register_any_task',
        'specific': '_register_specific_task',
    }

    # {device_id: { event_type: set([func1, func2]) }}
    # eg: { '123456F': { 'connect': set([func1, func2]), 'disconnect': set([func1, func2]) }, ...}
    _specific_task_dict = dict()

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
    def _register_any_task(cls, _, todo, event_type):
        if not todo:
            return
        if event_type not in cls._any_task_dict:
            cls._any_task_dict[event_type] = set()
        cls._any_task_dict[event_type].add(todo)
        logger.info('RESISTER ANY', func_name=todo.__name__)

    @classmethod
    def _register_specific_task(cls, device_list, todo, event_type):
        for each_device in device_list:
            if each_device not in cls._specific_task_dict:
                cls._specific_task_dict[each_device] = dict()
            if event_type not in cls._specific_task_dict[each_device]:
                cls._specific_task_dict[each_device][event_type] = set()
            cls._specific_task_dict[each_device][event_type].add(todo)
            logger.info('RESISTER SPECIFIC', func_name=todo.__name__, device=each_device)

    @classmethod
    def register_task(cls, operate_type, event_type, todo, device_list=None):
        logger.info('START REGISTER', type=operate_type)

        if operate_type in cls._operation_dict:
            operate_type = cls._operation_dict[operate_type]
        func_item = getattr(cls, operate_type, cls._default_operation)
        return func_item(device_list, todo, event_type)

    @classmethod
    def exec_task(cls, device_id, event_type):
        # any func
        func_list = cls._any_task_dict[event_type].copy()

        # specific func
        if device_id in cls._specific_task_dict:
            _specific_func_list = cls._specific_task_dict[device_id][event_type]
            func_list |= _specific_func_list

        logger.info('ALL FUNC NEED EXEC', func_list=[i.__name__ for i in func_list])
        for each_func in func_list:
            logger.info('EXEC FUNC', func=each_func.__name__, device=device_id)
            each_func(device_id)
