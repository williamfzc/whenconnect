class WCore(object):
    # 单例
    # 提供事件注册API
    # 维护queue
    # 维护scanner
    pass


def api_handler(operate_type, device_list=None, todo_list=None):
    print(operate_type, device_list, todo_list)
