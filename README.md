# whenac

> when adb connected, manage your android device.

## design

只保留最核心的部分，具体操作完全插件化

## modules

- scanner
    - 轮询
    - 不断向sender输出当前有效设备列表

- timer
    - 定时任务模块（周期性而非定时性）
    - 管理定时任务，在需要触发时向sender输出任务参数

- sender（消息队列）
    - 负责模块与core的通信
    - 将队列中的内容通过API传递给core

- core
    - 服务器形式
    - 通过API接收其他模块的请求（sender、外界request）
    - 结合plugin解析请求，做出响应

- plugin
    - 方法库，一些自定义复杂操作的拓展
    - 对应形式 方法名对应cmd命令`function_name: cmd`

## problem

- [x] scanner是否作为plugin与timer的一部分？
    - 暂不作为，scanner频率较高，且作用不同于其他插件

- [ ]插件的形式只用cmd是否合理？

- [ ]通信机制需要细化及检验
