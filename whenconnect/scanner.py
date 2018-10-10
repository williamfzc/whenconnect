import subprocess
import warnings
import os

from whenconnect.utils import exec_cmd


def parse_process_output_to_device_list(process_output: str) -> list:
    """
    return available device list

    :param process_output: output of subprocess, after decode
    :return: ['abcdef', 'ghijkl']
    """
    device_list = [i.split('\t') for i in process_output.split(os.linesep)[1:] if i]
    available_device_list = []
    for each_device in device_list:
        if 'device' in each_device:
            available_device_list.append(each_device[0])
    return available_device_list


def get_device_list():
    """
    use adb to get available device list

    :return: ['abcdef', 'ghijkl']
    """
    adb_devices_cmd = ['adb', 'devices']
    adb_result, adb_stdout_content, adb_stderr_content = exec_cmd(adb_devices_cmd)
    if adb_result:
        error_msg = '\n'.join((adb_stdout_content, adb_stderr_content))
        warnings.warn('adb devices error: {}'.format(error_msg))
        raise subprocess.CalledProcessError(adb_result, adb_devices_cmd)

    current_device_list = parse_process_output_to_device_list(adb_stdout_content)
    current_device_set = set(current_device_list)
    return current_device_set


# FOR TEST
def _test():
    current_device_list = get_device_list()
    print(current_device_list)


if __name__ == '__main__':
    _test()
