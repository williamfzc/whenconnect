from whenconnect import when_connect


def sth(device):
    print('do something 1', device)


# set device list
when_connect(device=['abc123', 'def456'], do=sth)

# or command mode
when_connect(device='any', do=sth)
