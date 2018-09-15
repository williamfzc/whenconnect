import subprocess
import warnings
import os


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
    adb_process = subprocess.Popen(adb_devices_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    adb_result = adb_process.wait(timeout=30)
    adb_stdout_content = adb_process.stdout.read().decode()
    adb_stderr_content = adb_process.stderr.read().decode()
    if adb_result:
        error_msg = '\n'.join((adb_stdout_content, adb_stderr_content))
        warnings.warn('adb devices error: {}'.format(error_msg))
        raise subprocess.CalledProcessError(adb_result, adb_devices_cmd)

    return parse_process_output_to_device_list(adb_stdout_content)


if __name__ == '__main__':
    cur_device_list = get_device_list()
    print(cur_device_list)
