"""
device object, offer device info and so on.
"""
from whenconnect.utils import exec_cmd
from whenconnect.logger import logger


def get_prop(device_id):
    """ get prop """
    cmd_list = ['adb', '-s', device_id, 'shell', 'getprop']
    return_code, output, error = exec_cmd(cmd_list)
    if return_code:
        logger.info('GETPROP ERROR', code=return_code, msg=error)
        return
    prop_dict = {
        each.split(':')[0].strip('[] '): each.split(':')[1].strip('[] ')
        for each in output.split('\r\n') if each}
    return prop_dict


class WCDevice(object):
    def __init__(self, device_id):
        self.device_id = device_id
        self.device_prop = get_prop(device_id)

    def __repr__(self):
        return '<WCDevice {}>'.format(self.device_id)

    __str__ = __repr__


if __name__ == '__main__':
    wc_device = WCDevice('9c12aa96')
    print(wc_device.device_prop)
