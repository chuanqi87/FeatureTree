# 截屏

在调试过程中，可以通过多种方式截取屏幕截图。  

#### 通过DevEco Studio截屏

1. 连接真机设备或模拟器，并在其中运行应用。
2. 在DevEco Studio底部切换到Log页签。
3. 点击左侧工具栏中![](https://media:201787890324501167)，即可截取屏幕截图。

   <br />

   截图的图片将直接显示在DevEco Studio中。

   ![](https://media:201787890324554168)

   <br />

4. （可选）在图片显示区域右击，选择Copy Path/Reference...可以查看截屏的本地存储路径或者在菜单栏下方查看本地存储路径。

   <br />

   ![](https://media:201787890324602169)

   <br />

#### 通过命令行方式截屏

hdc是可以用于调试的命令行工具，通过该工具可以实现截屏功能。更多关于命令行工具hdc的说明请参见[hdc工具使用指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdc)。

```
hdc shell snapshot_display -f /data/local/tmp/0.jpeg  // -f参数指定图片在设备上的存储路径，如不指定，会在命令执行完成后显示图片默认存储路径。
hdc file recv /data/local/tmp/0.jpeg  // 将图片从设备发送到本地目录，本示例将图片发送到当前执行hdc命令的目录。
```
