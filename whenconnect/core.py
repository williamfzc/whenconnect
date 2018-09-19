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
    last_device_set = set()
    while IS_ALIVE:
        # get device set from scanner
        current_device_set = event_queue.get()
        event_queue.task_done()

        # nothing different
        if last_device_set == current_device_set:
            continue

        # if something changed
        add_device_set = current_device_set - last_device_set
        lost_device_set = last_device_set - current_device_set

        # less device
        for each_device in lost_device_set:
            logger.info('LOST DEVICE', device=each_device)
            TaskManager.exec_task(each_device, 'disconnect')
        # more device
        for each_device in add_device_set:
            logger.info('ADD DEVICE', device=each_device)
            TaskManager.exec_task(each_device, 'connect')

        last_device_set = current_device_set


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
