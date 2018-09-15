from whenconnect import when_connect


def special_thing(device):
    print('do something special!', device)


def normal_thing(device):
    print('do something normal.', device)


# set device list
when_connect(device=['9c12aa96', 'def456'], do=special_thing)

# or command mode
when_connect(device='any', do=normal_thing)
