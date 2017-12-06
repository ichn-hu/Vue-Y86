Y86 Simulator, for ICS2017 @ Fudan, by ichn-hu

# Vue-Y86 运行与测试说明

## 输入数据

初版代码支持标准Y86指令集, 暂不支持`iaddl`和`leave`. 后续考虑拓展.

支持`.yo`的字符`01`串输入, 这一点与CMU标准是一致的, 方便直接使用其数据.

## 后端

使用python3.6以上版本, 安装最新的flask库即可.

在根目录`Vue-Y86/`下执行`python server.py`即可运行服务.

## 前端

推荐使用最新的Chrome浏览器, 并保证网络通畅(前端库引用了cdn服务)

启动服务后访问`localhost:8080`, 并拖拽`.yo`文件执行.

## 测试

为了方便测试, `runner.py`文件实现了`runInstrCode(str)`方法, 传入`.yo`文件的文本字符串(要求`utf-8`编码), 返回一个字典, 里面定义了

```json
{
  "Stat": int, // 表示整个程序终止的状态
  "0": { // clock cycle 为 0 的状态
    "F": { info of Fetch }, // Fetch 阶段的流水线寄存器的状态以及operation
    "D": { info of Decode },
    "E": { 同上 },
    "M": { 同上 },
    "W": { 同上 },
    "mem": [{地址: 值}], // 字典的数组, key为地址, value是那个地址开始的一个Bite, 没有指明的地址是默认的0
    "reg": {"%EAX": str}, // 寄存器状态
    "cc": {'CF': bool, 'ZF': bool, 'SF': bool} // condition code
  },
  "2": {
    ...
  },
  ...
}
```

具体可以参考`cpu.py`的实现.

此外, 为了方便测试, 在根目录添加了`test.py`可以直接执行. 在第`8`行指明测试`.yo`文件所在文件夹的绝对路径, 在第`9`行指明测试文件的文件名. 然后`python test.py`执行. 结束后结果以`json`的形式存在测试文件同目录下的`run.txt`内.

具体测试代码编写可以参考test文件夹下的jupyter notebook.

注意事项: 默认的`MAXCLOCK`为`1000`, 定义在`kernel/const.py:60`处, 可自行修改.