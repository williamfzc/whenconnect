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
    - 挂载插件
    - 处理scanner返回的数据
    - 调度操作流程

- plugin
    - 通过配置文件加载外部模块
    - 封装成为可挂载的形式，方便core导入
