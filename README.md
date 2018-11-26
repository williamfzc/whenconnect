# whenconnect

[English README](README_en.md)

[![Maintainability](https://api.codeclimate.com/v1/badges/c6e406c3416bbbcbd898/maintainability)](https://codeclimate.com/github/williamfzc/whenconnect/maintainability)
[![PyPI version](https://badge.fury.io/py/whenconnect.svg)](https://badge.fury.io/py/whenconnect)
[![Downloads](https://pepy.tech/badge/whenconnect)](https://pepy.tech/project/whenconnect)

> when your android connected, do sth :)

## 目标

提供一个简洁方便的方案以解决设备**连接与断开**时的监听工作，例如安装应用、启动应用、杀死进程，或是定制任何你希望的。

## 使用

### 基本用法

如果你希望，在设备123456F成功连接电脑后执行函数A，你只需要：

```python
from whenconnect import when_connect


def A(device):
    print('call function A', device)

# 事件注册
when_connect(device=['123456F'], do=A)
```

这样做之后，在你的程序执行时whenconnect将会同步检测123456F是否已经连接上；如果连接上，将把设备ID传入函数A并执行它：

```bash
call function A 123456F
```

当然，你也可以选择响应所有设备：

```python
when_connect(device='any', do=A)
```

这样做之后，一旦新增了android设备都会执行函数A并传入连接上的设备id。

同样的，whenconnect也支持当设备断开时的场景，你只需要：

```python
from whenconnect import when_disconnect


def A(device):
    print('call function A', device)

# 事件注册
when_disconnect(device=['123456F'], do=A)
```

### 获取当前设备与任务

whenconnect也提供了API以便在程序任意位置获取到当前的设备与任务注册状态：

```python
from whenconnect import get_devices, get_current_task


device_list = get_devices()
print(device_list)
# ['123456F']

task_dict = get_current_task()
print(task_dict)
# {'any': {'connect': {<function normal_thing at 0x1033dad08>}, 'disconnect': {<function lose_connect at 0x1068d5b70>}}, 'specific': {'123': {'connect': {<function special_thing at 0x101dc8ea0>}}, 'def456': {'connect': {<function special_thing at 0x101dc8ea0>}}}}
```

### 实际使用例子

如果你只是单纯希望它单独作为一个长期的监听模块存在，只需要让你的程序保持工作即可：

- 在末尾加入死循环
- 嵌入到服务器
- `...`

基于whenconnect，你可以自由定制你需要的场景。例如，希望在设备插入后每五秒钟查看一次设备信息：

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

# 事件注册
when_connect(device='any', do=check_device_info)
```

## API

whenconnect只提供了为数不多的API：

- 连接设备时
- 断开设备时
- 获取当前已连接的设备列表
- 获取当前已注册的任务

可直接阅读[api.py](whenconnect/api.py)了解实现细节，或参考[demo.py](demo.py)使用。

## 安装

```
pip install whenconnect
```

- Only tested on python3.
- and ADB installed.

## License

MIT
