from whenconnect import when_connect, start_detect


def special_thing(device):
    print('do something special!', device)


def normal_thing(device):
    print('do something normal.', device)


# init when_connect
# if no need for log, you can set 'with_log' to False. Default to True.
start_detect(with_log=False)

# set device list
when_connect(device=['9c12aa96', 'def456'], do=special_thing)

# or command mode
when_connect(device='any', do=normal_thing)

# CARE ONLY WHAT U REALLY NEED
while True:
    pass
