import subprocess


def exec_cmd(cmd_list, timeout=30):
    """
    run cmd and get its return code, output, and error.

    :param cmd_list:
    :param timeout:
    :return:
    """
    adb_process = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = adb_process.communicate(timeout=timeout)
    adb_stdout_content = stdout.decode()
    adb_stderr_content = stderr.decode()
    return adb_process.returncode, adb_stdout_content, adb_stderr_content
