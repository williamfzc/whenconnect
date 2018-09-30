from whenconnect import *


def special_thing(device):
    print('do something special!', device)


def normal_thing(device):
    print('do something normal.', device)


def lose_connect(device):
    print('{} lost!'.format(device))


# init when_connect
# if no need for log, you can set 'with_log' to False. Default to True.
start_detect(with_log=False)

# set device list
when_connect(device=['123', 'def456'], do=special_thing)

# or command mode
when_connect(device='any', do=normal_thing)

# of course, when disconnect:
when_disconnect(device='any', do=lose_connect)

# or, get connected devices list anytime
device_list = get_devices()
print(device_list)

# CARE ONLY WHAT U REALLY NEED
while True:
    pass
