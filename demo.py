from whenconnect import *


def start_connect(device):
    print('{} connected'.format(device))
    print('all devices: {}'.format(get_devices()))


def lose_connect(device):
    print('{} lost'.format(device))
    print('all devices: {}'.format(get_devices()))


def special_connect(device):
    print('{} specially connected'.format(device))


# or command mode
when_connect(device='any', do=start_connect)

# of course, when disconnect:
when_disconnect(device='any', do=lose_connect)

# specify a device
when_connect(device=['9c12aa96'], do=special_connect)

# or, get connected devices list anytime
device_list = get_devices()
print(device_list)

# check registered tasks
task_dict = get_current_task()
print(task_dict)
