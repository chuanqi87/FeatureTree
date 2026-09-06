# GATT读写通知 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

三平台文档初判：Android 指南以 BluetoothGatt 回调模型覆盖服务发现/读特征/通知（需手动写 CCCD 描述符）；HarmonyOS GATT 指南完整给出客户端读写特征值与通知/指示使能 API 及服务端收发流程；iOS 仅读到 Core Bluetooth 框架概览页，特征读写与通知订阅的具体操作 API 未在本包正文出现。提出通知使能方式、异步串行约束、权限形态 3 条差异假设。版本基线未固定，全部 low 初判。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | documented_mechanism | direct | 官方指南以 BluetoothGatt 为核心：连接后 discoverServices() 发现服务；readCharacteristic() 异步读特征、结果经 onCharacteristicRead 回调；通知用 setCharacteristicNotification() 并对 CCCD 写 ENABLE_NOTIFICATION_VALUE，特征变化经 onCharacteristicChanged 送达。正文仅概述可读写属性，未展示写特征示例。 | recommended |
| ios | possible_mapping | indirect | 仅读到框架概览页：Core Bluetooth 提供 BLE 通信所需类，列出 CBCharacteristic、CBATTRequest（ATT 请求）、CBATTError（GATT 服务端 ATT 事务错误）与 CBPeripheralDelegate（外设服务使用更新）；特征读写与通知订阅的具体操作 API 未在本包正文出现，ios-2 为 Security 错误码与 GATT 无关。 | unassessed |
| harmonyos | documented_mechanism | direct | GATT 指南完整描述客户端 createGattClientDevice→connect→getServices→readCharacteristicValue/writeCharacteristicValue，on('BLECharacteristicChange') 订阅 + setCharacteristicChangeNotification/Indication 使能（通知/指示二选一，指示由子系统确认）；服务端 on('characteristicRead'/'characteristicWrite') 与 notifyCharacteristicChanged；需 ACCESS_BLUETOOTH 权限。 | recommended |

## android 条件与证据

适用范围：developer.android.com 指南快照（2026-09-05 抓取），正文未标注 API Level/AndroidX 版本；BluetoothGatt 最低系统版本未核实
条件：需先 connectGatt 连接并在 discoverServices 完成服务发现后才可读写属性；通知使能需对 Client Characteristic Configuration 描述符写入 ENABLE_NOTIFICATION_VALUE；依赖 BluetoothAdapter 可用（设备具备蓝牙）
缺口：writeCharacteristic 写特征用法与写类型未在本包正文出现，需读 BluetoothGatt API 参考；未标注 API Level，相关接口的最低系统版本未核实；后台执行与多连接约束未在本包正文覆盖
真机分类理由：读写与通知时序、CCCD 写入后的实际通知行为依赖真实外设与协议栈实现，静态文档不足以确认运行行为

- [Transfer BLE data](https://developer.android.com/develop/connectivity/bluetooth/ble/transfer-ble-data)，导言：连接 GATT 服务器后可查询数据并在特征变化时请求通知，正文 3–7 行；获取 2026-09-05T10:24:15.107049+00:00；SHA 0260725dffa47cbc059c4ce50c64282b91cedad56c99f21fb85853711c7397cb。
- [Transfer BLE data](https://developer.android.com/develop/connectivity/bluetooth/ble/transfer-ble-data)，Read BLE characteristics：readCharacteristic 为异步调用，结果经 onCharacteristicRead 回调，正文 360–365 行；获取 2026-09-05T10:24:15.107049+00:00；SHA 0260725dffa47cbc059c4ce50c64282b91cedad56c99f21fb85853711c7397cb。
- [Transfer BLE data](https://developer.android.com/develop/connectivity/bluetooth/ble/transfer-ble-data)，Receive GATT notifications：调用 setCharacteristicNotification 方法，正文 498–504 行；获取 2026-09-05T10:24:15.107049+00:00；SHA 0260725dffa47cbc059c4ce50c64282b91cedad56c99f21fb85853711c7397cb。
- [Transfer BLE data](https://developer.android.com/develop/connectivity/bluetooth/ble/transfer-ble-data)，通知使能需写 CCCD 描述符 ENABLE_NOTIFICATION_VALUE 并 writeDescriptor，正文 520–524 行；获取 2026-09-05T10:24:15.107049+00:00；SHA 0260725dffa47cbc059c4ce50c64282b91cedad56c99f21fb85853711c7397cb。
- [Transfer BLE data](https://developer.android.com/develop/connectivity/bluetooth/ble/transfer-ble-data)，通知使能后特征变化触发 onCharacteristicChanged 回调，正文 557–559 行；获取 2026-09-05T10:24:15.107049+00:00；SHA 0260725dffa47cbc059c4ce50c64282b91cedad56c99f21fb85853711c7397cb。
- [Connect to a GATT server](https://developer.android.com/develop/connectivity/bluetooth/ble/connect-gatt-server)，connectGatt 返回 BluetoothGatt 实例用于 GATT 客户端操作，回调投递结果，正文 21–26 行；获取 2026-09-05T10:24:14.941740+00:00；SHA ed8cbb13ad3490093d67e6aac935991ed8758b59b8442a45508b7031d3169270。

## ios 条件与证据

适用范围：developer.apple.com Core Bluetooth 框架页快照（2026-09-05 抓取），提及 iOS 13+/iOS 26 条件；各符号 iOS 适用版本（availability）未核对
条件：iOS 13 起访问 Core Bluetooth API 需 Info.plist 含 NSBluetoothAlwaysUsageDescription，否则应用崩溃；iOS 12 及更早使用 NSBluetoothPeripheralUsageDescription；iPad 应用运行于 macOS 不支持 Core Bluetooth 后台执行模式
缺口：未读到 CBPeripheral 特征读/写/订阅通知的具体 API 正文（如 readValue/setNotifyValue 对应符号）；ios-2（Security 结果码）与 GATT 无关，属无关绑定来源；各符号 iOS 适用版本（availability）未核对；ATT/GATT 事务错误与特征操作的对应关系仅有目录级描述
真机分类理由：本轮未读到特征读写与通知订阅的具体操作正文，无法基于现有证据评估真机验证需求

- [Core Bluetooth](https://developer.apple.com/documentation/corebluetooth)，Overview：Core Bluetooth 提供与 BLE（及 BR/EDR）设备通信所需的类，正文 7–9 行；获取 2026-09-05T09:34:21.400334+00:00；SHA 248c4c6af3a8e8a9658cf9e3492f6e12039b70b1fcd1fefc0d2e5d4810a49c03。
- [Core Bluetooth](https://developer.apple.com/documentation/corebluetooth)，Important：iOS 13 起需 NSBluetoothAlwaysUsageDescription，iOS 12 及更早用 NSBluetoothPeripheralUsageDescription，正文 18–19 行；获取 2026-09-05T09:34:21.400334+00:00；SHA 248c4c6af3a8e8a9658cf9e3492f6e12039b70b1fcd1fefc0d2e5d4810a49c03。
- [Core Bluetooth](https://developer.apple.com/documentation/corebluetooth)，Topics：CBPeripheralDelegate 提供外设服务使用情况的更新，正文 43–45 行；获取 2026-09-05T09:34:21.400334+00:00；SHA 248c4c6af3a8e8a9658cf9e3492f6e12039b70b1fcd1fefc0d2e5d4810a49c03。
- [Core Bluetooth](https://developer.apple.com/documentation/corebluetooth)，Topics：CBCharacteristic 表示远端外设服务的特征，正文 91–93 行；获取 2026-09-05T09:34:21.400334+00:00；SHA 248c4c6af3a8e8a9658cf9e3492f6e12039b70b1fcd1fefc0d2e5d4810a49c03。
- [Core Bluetooth](https://developer.apple.com/documentation/corebluetooth)，CBATTError Code：GATT 服务端（远端外设）在 BLE ATT 事务中可能返回的错误，正文 153–155 行；获取 2026-09-05T09:34:21.400334+00:00；SHA 248c4c6af3a8e8a9658cf9e3492f6e12039b70b1fcd1fefc0d2e5d4810a49c03。

## harmonyos 条件与证据

适用范围：华为 developer.huawei.com harmonyos-guides/references 快照（2026-09-04 抓取），HarmonyOS 发行版；各接口起始 API 版本未在正文标注
条件：需申请 ohos.permission.ACCESS_BLUETOOTH 权限；读写特征值/描述符必须在服务发现完成后进行且特征在服务集合内，否则失败；通知或指示要求特征含 CCC 描述符（UUID 00002902-0000-1000-8000-00805F9B34FB）；读写/通知等异步接口上一操作完成前调用下一操作会报 2900011 操作频繁
缺口：各接口起始 API 版本需读 js-apis-bluetooth-ble API 参考核实；手机/平板设备形态差异未在正文说明；后台执行与多连接并发约束未覆盖
真机分类理由：机制文档完整，但通知/指示使能时序、错误码实际触发条件与真实外设交互建议真机复核

- [连接和传输数据](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gatt-development-guide)，开发步骤：申请权限 ohos.permission.ACCESS_BLUETOOTH，正文 19–21 行；获取 2026-09-04T09:35:09+00:00；SHA 31cc58a4425c83a413fb7853894b8eb20ee3f0ccf4ba5e1c18b6dca667d6646c。
- [连接和传输数据](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gatt-development-guide)，服务发现：读写特征值、读写描述符等操作需在服务发现完成后进行，否则失败，正文 88–91 行；获取 2026-09-04T09:35:09+00:00；SHA 31cc58a4425c83a413fb7853894b8eb20ee3f0ccf4ba5e1c18b6dca667d6646c。
- [连接和传输数据](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gatt-development-guide)，客户端读取/写入特征值：readCharacteristicValue 与 writeCharacteristicValue，正文 112–118 行；获取 2026-09-04T09:35:09+00:00；SHA 31cc58a4425c83a413fb7853894b8eb20ee3f0ccf4ba5e1c18b6dca667d6646c。
- [连接和传输数据](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gatt-development-guide)，接收特征值变化通知或指示：需 CCC 描述符，先订阅 on('BLECharacteristicChange') 再 setCharacteristicChangeNotification/Indication 使能，指示由蓝牙子系统确认，正文 211–218 行；获取 2026-09-04T09:35:09+00:00；SHA 31cc58a4425c83a413fb7853894b8eb20ee3f0ccf4ba5e1c18b6dca667d6646c。
- [连接和传输数据](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gatt-development-guide)，服务端 notifyCharacteristicChanged 发送通知或指示，confirm 参数决定类型，正文 532–539 行；获取 2026-09-04T09:35:09+00:00；SHA 31cc58a4425c83a413fb7853894b8eb20ee3f0ccf4ba5e1c18b6dca667d6646c。
- [蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)，错误码 2900011 操作频繁：readCharacteristicValue 等未完成即执行下一操作会阻塞，正文 170–188 行；获取 2026-09-04T04:07:05.243692+00:00；SHA 4042af7df2166c5fd6290d590a46c431c0462efbadfb5107b098efcad1ba98d6。

## 待验证差异假设

- programming_model：通知订阅使能方式假设存在差异：Android 指南要求应用在 setCharacteristicNotification 后手动对 CCCD 描述符写入 ENABLE_NOTIFICATION_VALUE；HarmonyOS 提供专用 API setCharacteristicChangeNotification/Indication 使能，且指示确认由蓝牙子系统自动完成。待核实的 can/must 级编程模型差异。；待核：iOS 的通知订阅 API 是否同样封装 CCCD 写入未核实；Android 是否存在系统级封装避免手动写描述符需读 API 参考；两平台在通知/指示切换场景的实际行为差异需真机验证。
- limits_precision：GATT 客户端异步操作并发约束假设存在差异：HarmonyOS 错误码文档明确读写特征值/描述符、通知使能等接口上一操作未完成即调用下一操作会报 2900011 并阻塞；Android 指南仅说明 readCharacteristic 为异步回调模型，本包正文未说明同类串行限制。；待核：Android BluetoothGatt 操作排队/并发行为需读 API 参考并实测核实；HarmonyOS 串行限制是否区分同一特征与不同特征的操作组合；iOS 的并发 GATT 操作限制未核实。
- permissions_privacy：使用 GATT 能力的前置授权形态假设不同：iOS 要求 Info.plist 使用描述键（iOS 13 起 NSBluetoothAlwaysUsageDescription，缺失即崩溃）；HarmonyOS 要求声明 ohos.permission.ACCESS_BLUETOOTH 权限；Android 侧权限条件未在本包正文出现，无法三方比较。；待核：Android 的 BLUETOOTH_CONNECT 等运行时权限要求需另行核实；ACCESS_BLUETOOTH 的授权级别与用户授权流程未读正文；iOS 26 Live Activity 后台特权对 GATT 通知接收的影响未核实。

范围缺口：iOS 仅有框架概览级证据，特征读写与通知订阅操作 API 正文缺失；ios-2 为 Security 框架结果码，与 GATT 无关；Android 写特征用法、BluetoothGatt API 参考正文与 API Level 条件未读；HarmonyOS 各 GATT 接口起始 API 版本需读 js-apis-bluetooth-ble 参考核实；三平台最新正式版与手机基线未固定，全部结论为 low 初判

后续优先级：P1；iOS 侧仅有间接证据且存在无关绑定来源，特征读写/通知机制映射属高风险；Android 写特征用法与版本条件缺失，需优先读 API 参考正文并固定基线

逐条引用及原文摘录见同目录 normalized.json。
