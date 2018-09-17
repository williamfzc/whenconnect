"""
# 单例
# 提供事件注册API
# 维护queue
# 维护scanner
"""
import threading
import time

from whenconnect.pipe import event_queue
from whenconnect.scanner import get_device_list
from whenconnect.manager import TaskManager
from whenconnect.logger import logger, no_output

IS_ALIVE = 0


def loop_get_device_list():
    while IS_ALIVE:
        current_device_list = get_device_list()
        event_queue.put(current_device_list)
        time.sleep(1)


def handle_event():
    """
    获取最新的设备列表，处理后让TaskManager执行对应的事件

    :return:
    """
    last_device_list = []
    while IS_ALIVE:
        current_device_list = event_queue.get()
        event_queue.task_done()
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
            TaskManager.exec_task(each_device)
        last_device_list = current_device_list


class ThreadManager(object):
    loop_device_thread = threading.Thread(target=loop_get_device_list)
    event_handler_thread = threading.Thread(target=handle_event)

    @classmethod
    def start(cls):
        global IS_ALIVE
        IS_ALIVE = 1
        cls.loop_device_thread.start()
        cls.event_handler_thread.start()

    @classmethod
    def stop(cls):
        global IS_ALIVE
        IS_ALIVE = 0


def start_detect(with_log=True):
    if not with_log:
        no_output()
    ThreadManager.start()
