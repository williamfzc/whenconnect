# whenac

> when adb connected, init your android device.

## design

adb轮询以确认设备增减，若有变化：

- 执行操作
    - 自由配置，插件化
    - 增减分别是不同的操作
- 更新设备列表
    - 设备列表直接在内存里，不需要文件io

## modules

- scanner
    - 轮询
    - 不断向外输出当前有效设备列表

- core
    - 服务器形式
    - 处理scanner返回的数据
    - 通过方法库，调度操作流程
    - 通过消息队列处理其他模块的请求

- plugin
    - 通过配置文件加载外部模块
    - 方法库

- timer
    - 定时任务模块
    - 管理定时任务，在需要触发时向外输出任务参数

## TODO

- scanner是否作为plugin与timer的一部分？
