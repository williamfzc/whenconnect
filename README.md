# whenconnect

> once your android connected, do sth :)

## design

只保留最核心的部分，具体操作完全插件化

## API

```python
from whenconnect import when_connect

def sth(device):
    print('do something 1', device)
    

# set device list
when_connect(device=['abc123', 'def456'], do=sth)

# or command mode
when_connect(device='any', do=sth) 
```

- 一旦新连接上的设备符合要求，将依次执行do列表中的函数
- 函数的第一个参数为当前操作的设备id

## modules

- scanner
    - 轮询
    - 不断输出当前有效设备列表

- pipe
    - 负责scanner与core的通信
    - 后续扩展需要

- core
    - 解析queue传递过来的请求，进行对应的处理
    
- api
    - 外部调用

## License

MIT
