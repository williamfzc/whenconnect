# whenconnect

[中文版README](https://github.com/williamfzc/whenconnect/blob/master/README_zh.md)

[![Maintainability](https://api.codeclimate.com/v1/badges/c6e406c3416bbbcbd898/maintainability)](https://codeclimate.com/github/williamfzc/whenconnect/maintainability)
[![PyPI version](https://badge.fury.io/py/whenconnect.svg)](https://badge.fury.io/py/whenconnect)
[![Downloads](https://pepy.tech/badge/whenconnect)](https://pepy.tech/project/whenconnect)

> when your android connected, do sth :)

## What For

A better way to handle things when connect android device, such as install an app, launch an app, and something else you wish.

- Have same lifecycle with your python script.
- And when your python script end, it will end too.

## Usage

### Base

If you want to call function A when device '123456F' connected:

```python
from whenconnect import when_connect


def A(device):
    print('call function A', device)

# register event
when_connect(device=['123456F'], do=A)
```

After that, when 123456F connected, function A will be called!

Of course, you can choose to detect 'any' devices.

```python
when_connect(device='any', do=A)
```

Or, get connected devices list or registered tasks anytime:

```python
from whenconnect import get_devices, get_current_task


device_list = get_devices()
print(device_list)
# ['123456F']

task_dict = get_current_task()
print(task_dict)
# {'any': {'connect': {<function normal_thing at 0x1033dad08>}, 'disconnect': {<function lose_connect at 0x1068d5b70>}}, 'specific': {'123': {'connect': {<function special_thing at 0x101dc8ea0>}}, 'def456': {'connect': {<function special_thing at 0x101dc8ea0>}}}}
```

### More

Use dead loop or server to keep when_connect alive for a long time if you want.

For example, after device connected, check its device info every 5 seconds：

```python
from whenconnect import when_connect
import os
import threading


def check_device_info(device):
    cmd = 'adb -s {} shell getprop ro.product.model'.format(device)
    device_model = os.popen(cmd).read()
    print(device_model)

    global timer
    timer = threading.Timer(5, lambda: check_device_info(device))
    timer.start()

when_connect(device='any', do=check_device_info)
```

Can not become easier.

## API

See `whenconnect/api.py` for detail.

## Install

```
pip install whenconnect
```

- Only tested on python3.
- and ADB installed.

## License

MIT
