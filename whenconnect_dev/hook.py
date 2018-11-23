from whenconnect_dev.logger import logger

TAG = 'FunctionManager'


class BaseFunctionManager(object):
    _func_dict = {
        'connect': set(),
        'disconnect': set(),
    }

    @classmethod
    def add(cls, new_func: callable, action: str, target_devices: set = None, *args, **kwargs):
        if action not in cls._func_dict:
            raise KeyError('action should be "connect" or "disconnect"')
        cls._func_dict[action].add(new_func)


class NormalFunctionManager(BaseFunctionManager):
    @classmethod
    def run(cls, action, ):
        for each_func_name, each_func in cls._func_dict.items():
            logger.info(TAG, name=each_func_name)


class SpecFunctionManager(BaseFunctionManager):
    _device_func_map = dict()

    @classmethod
    def add(cls, new_func: callable, target_devices: set = None, *args, **kwargs):
        super(SpecFunctionManager, cls).add(new_func)

        # register functions
        for each_device in target_devices:
            if each_device in cls._device_func_map:
                cls._device_func_map[each_device] = [new_func]
            else:
                cls._device_func_map[each_device].append(new_func)

    @classmethod
    def run(cls):
        for each_func_name, each_func in cls._func_dict.items():
            logger.info(TAG, name=each_func_name)
