# BLE连接 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

三平台均读到 BLE/GATT 连接机制：Android 概述明示权限→扫描→连接 GATT server 流程；iOS 仅 MIDI 场景明示 CoreBluetooth 扫描连接与 iOS 16+ 系统自动重连；HarmonyOS 接口级明示 GattClientDevice.connect、GattSetting/GattServer.connect(autoConnect) 及 ACCESS_BLUETOOTH 权限与 API 10/26 版本。基线未固定，全部 low；Android 连接指南与 iOS Core Bluetooth 正文缺失为主要缺口。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | documented_mechanism | direct | BLE 概述明示：声明权限后经 BluetoothAdapter 确认蓝牙可用并扫描，发现设备后通过连接其 GATT server 建立通信，之后按服务/特征传输数据；平台内建 central 角色支持。连接 API 细节未入包。 | recommended |
| ios | documented_mechanism | indirect | 仅读到 Core MIDI 的 MIDI Bluetooth 页：iOS 16+（并列 macOS 13+）系统自动重连支持配对的 BLE MIDI 外设；不配对设备由 Core MIDI 经 CoreBluetooth 扫描并连接、确认 MIDI 服务。通用 BLE 连接 API 正文未读到。 | recommended |
| harmonyos | documented_mechanism | direct | HarmonyOS（华为官网）API 参考明示：ble.createGattClientDevice 创建 client 实例后调用 connect() 主动发起 GATT 连接，经 on('BLEConnectionStateChange') 感知结果；需 ACCESS_BLUETOOTH 权限、Stage 模型；GattSetting 重载与 GattServer.connect(autoConnect) 自 API 26 起。 | recommended |

## android 条件与证据

适用范围：未固定基线；快照（2026-09-05）为 developer.android.com BLE 概述，正文未标注 API Level 或最低 Android 版本
条件：应用需先在 manifest 声明多项蓝牙权限（概述明示，具体权限清单正文未读）；本机蓝牙可用并完成 BLE 设备发现（扫描）后连接对端 GATT server；本机通常为 central/GATT client 角色，概述亦提及可作 GATT server（BluetoothGattServer）
缺口：connect-gatt-server 指南与 BluetoothGatt/BluetoothDevice.connectGatt API 参考未入冻结源，连接 API 形态、autoConnect、连接参数均未核实；概述未标注适用 API Level/Android 版本，与当前正式版对应关系未核实；后台连接限制、连接数量上限、超时行为未在已读正文出现；包内 android-2（Cross-Device SDK secure-connection）为生态层设备间连接，与本节点 BLE 外设连接不直接相关，未用于结论
真机分类理由：概述级文档可确认机制存在，但连接建立时序、运行时权限行为及与扫描的衔接需真机核实；本轮为文档初判，未做实测。

- [Bluetooth Low Energy](https://developer.android.com/develop/connectivity/bluetooth/ble/ble-overview)，Bluetooth Low Energy > 开篇平台支持声明（central 角色 API），正文 3–5 行；获取 2026-09-05T10:24:14.825262+00:00；SHA 294b09396e5cd041a9b75fb637a470d29a0362808b28669e04ed753dc1b80c0f。
- [Bluetooth Low Energy](https://developer.android.com/develop/connectivity/bluetooth/ble/ble-overview)，Bluetooth Low Energy > The basics（权限→扫描→连接 GATT server 流程），正文 25–39 行；获取 2026-09-05T10:24:14.825262+00:00；SHA 294b09396e5cd041a9b75fb637a470d29a0362808b28669e04ed753dc1b80c0f。
- [Bluetooth Low Energy](https://developer.android.com/develop/connectivity/bluetooth/ble/ble-overview)，Bluetooth Low Energy > Roles and responsibilities（central/peripheral 与 GATT client/server），正文 80–110 行；获取 2026-09-05T10:24:14.825262+00:00；SHA 294b09396e5cd041a9b75fb637a470d29a0362808b28669e04ed753dc1b80c0f。

## ios 条件与证据

适用范围：快照（2026-09-05）明示 iOS 16 or later 适用于系统自动重连，同页并列 macOS 13 or later；为 Apple 多平台目录，iOS 适用性在本页明示
条件：系统自动重连：iOS 16+ 且外设支持配对；应用侧连接：外设不支持配对时经 CoreBluetooth 扫描并连接，需确认外设含 BLE MIDI 服务与 MIDI I/O characteristic；已读范围限 BLE MIDI profile 场景，不能推广为通用 BLE 外设连接行为
缺口：Core Bluetooth（CBCentralManager.connect 等）API 参考未入冻结源，通用 BLE 连接仅能由 MIDI 场景间接推断；应用侧所需蓝牙权限/授权要求未在已读正文出现（不能据此断言无需权限）；系统自动重连是否仅限 MIDI profile 未确认；包内 ios-2（XPC connections）为进程间通信，与本节点无关，未用于结论
真机分类理由：已读证据仅 MIDI 场景与系统重连行为，通用 BLE 连接在 iOS 真机上的表现需待 Core Bluetooth 文档补读后实测确认；本轮未做实测。

- [MIDI Bluetooth](https://developer.apple.com/documentation/coremidi/midi-bluetooth)，MIDI Bluetooth > 页面主题（连接 BLE MIDI 外设），正文 1–3 行；获取 2026-09-05T10:19:31.589071+00:00；SHA ab572b5edaf882af58dfc263216a20694da4a1d8d1ea7aa9ae1a4f2090cbdae3。
- [MIDI Bluetooth](https://developer.apple.com/documentation/coremidi/midi-bluetooth)，MIDI Bluetooth > Discussion（iOS 16+/macOS 13+ 自动重连；CoreBluetooth 连接三步骤与断连 API），正文 5–17 行；获取 2026-09-05T10:19:31.589071+00:00；SHA ab572b5edaf882af58dfc263216a20694da4a1d8d1ea7aa9ae1a4f2090cbdae3。

## harmonyos 条件与证据

适用范围：华为官网 harmonyos-references（HarmonyOS，非 OpenHarmony）：模块首批接口 API 10 起；connect 与状态回调元服务 API 12 起；GattSetting 重载与 GattServer.connect 起始 API 26.0.0；对应商用发行版本号未核实
条件：需要 ohos.permission.ACCESS_BLUETOOTH 权限（拒绝报 201）；仅可在 Stage 模型使用；对端地址需来自 BLE 扫描结果，且对端 BLE 广播须可连接；GattSetting 的 transport 默认 TRANSPORT_LE，不能设为 TRANSPORT_UNKNOWN（API 26 重载）；2in1 设备未插近距离芯片时 API 26 重载报 801 能力不支持
缺口：连接时序、超时、重试策略与并发连接数量上限未在已读正文确认；BLEConnectionChangeState 结构与 connect 成功判定的具体状态值未读全文；API 26.0.0 对应的商用 HarmonyOS 正式发行版本号未核实（基线未固定）；phone/tablet 形态上的实际连接行为未验证（本轮无实测）
真机分类理由：API 参考已明示接口、权限与错误码，但连接成功率、回调时序、2in1/手机形态差异及 API 26 行为需真机验证；本轮未做实测。

- [@ohos.bluetooth.ble (蓝牙ble模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble)，@ohos.bluetooth.ble > 模块说明（基于 GATT 的连接与传输，首批接口 API 10 起），正文 1–5 行；获取 2026-09-05T09:34:21.800954+00:00；SHA f1d80db2df10406273b22c90053098e4370a49f6924dd1618d93759c7d19ce2f。
- [@ohos.bluetooth.ble (蓝牙ble模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble)，ble.createGattClientDevice（创建 client 端、地址来自扫描、广播须可连接），正文 89–97 行；获取 2026-09-05T09:34:21.800954+00:00；SHA f1d80db2df10406273b22c90053098e4370a49f6924dd1618d93759c7d19ce2f。
- [@ohos.bluetooth.ble (蓝牙ble模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble)，ble.createGattClientDevice（GattSetting 重载，起始版本 26.0.0），正文 136–146 行；获取 2026-09-05T09:34:21.800954+00:00；SHA f1d80db2df10406273b22c90053098e4370a49f6924dd1618d93759c7d19ce2f。
- [@ohos.bluetooth.ble (蓝牙ble模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble)，GattServer.connect（server 端发起连接，autoConnect 参数，起始版本 26.0.0），正文 1899–1924 行；获取 2026-09-05T09:34:21.800954+00:00；SHA f1d80db2df10406273b22c90053098e4370a49f6924dd1618d93759c7d19ce2f。
- [@ohos.bluetooth.ble (蓝牙ble模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble)，GattClientDevice > connect（client 端发起 GATT 连接，需 ACCESS_BLUETOOTH），正文 3033–3048 行；获取 2026-09-05T09:34:21.800954+00:00；SHA f1d80db2df10406273b22c90053098e4370a49f6924dd1618d93759c7d19ce2f。
- [@ohos.bluetooth.ble (蓝牙ble模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble)，GattClientDevice > on('BLEConnectionStateChange')（client 订阅连接状态变化），正文 4637–4656 行；获取 2026-09-05T09:34:21.800954+00:00；SHA f1d80db2df10406273b22c90053098e4370a49f6924dd1618d93759c7d19ce2f。

## 待验证差异假设

- lifecycle_background：自动重连层级假设：iOS 对支持配对的 BLE MIDI 外设在 iOS 16+ 由系统自动重连（can 行为，系统层）；HarmonyOS 的自动重连由应用在 GattSetting/GattServer.connect 中以 autoConnect 参数显式开启（must 显式配置，应用层）。两平台自动重连的触发层级与适用范围（MIDI profile vs 通用 GATT）可能不同。；待核：iOS 系统自动重连是否仅限 MIDI profile 未确认；Android 侧 autoConnect 行为未读（connect-gatt-server 指南未入包），无法纳入本假设；HarmonyOS autoConnect=true 的实际重连时机与耗电行为未验证。
- programming_model：连接发起角色假设：HarmonyOS 明示两类发起接口——client 端 GattClientDevice.connect()（对端地址在创建实例时固定）与 server 端 GattServer.connect(deviceId, autoConnect)（API 26 起，本机作 GATT server 仍可主动发起）；Android 概述将连接描述为 central 设备发现后连接对端 GATT server，并提及手机可作 GATT server（BluetoothGattServer），但该角色能否主动发起连接未在已读正文说明。双方'本机作为 server 角色发起连接'的能力与 API 形态可能存在差异。；待核：Android BluetoothGattServer 是否支持主动发起连接需读 API 参考确认；HarmonyOS GattServer.connect 与 GattClientDevice.connect 的适用场景区别；iOS 端对应能力未读到正文，未纳入本假设。
- permissions_privacy：权限模型假设：Android 概述要求应用在 manifest 声明多项蓝牙权限后方可使用 BLE API（声明位置为清单）；HarmonyOS 在 connect() 接口级明示需 ohos.permission.ACCESS_BLUETOOTH（权限拒绝报 201，运行时校验）；iOS 已读正文（MIDI Bluetooth）未提及应用侧权限要求（系统自动重连不涉及应用声明）。三平台连接外设所需权限的声明位置、粒度与校验时机可能不同。；待核：Android 具体权限清单（如 BLUETOOTH_CONNECT 运行时权限）正文未读；iOS Core Bluetooth 权限/授权要求未读，不能断言 iOS 无权限要求；HarmonyOS ACCESS_BLUETOOTH 的申请与授权方式（安装授予或用户授权）未确认。

范围缺口：Android：connect-gatt-server 指南与 BluetoothGatt/BluetoothDevice.connectGatt API 参考未入冻结源，连接 API 形态、autoConnect、连接参数（transport/PHY）均未核实。；iOS：Core Bluetooth（CBCentralManager.connect）正文未入冻结源，通用 BLE 外设连接仅能由 MIDI 场景间接推断。；三平台最新正式版基线未固定（version_baseline unresolved），已读快照与当前手机系统/API Level 对应关系未核实。；连接数量上限、超时、后台连接限制、断连重试策略在已读正文均未覆盖。；包内 android-2（Cross-Device SDK）与 harmonyos-2（碰一碰）源与本节点范围（与外设建立 BLE 连接）不直接相关，未用于结论。

后续优先级：P1；Android 连接 API 与 iOS Core Bluetooth 核心正文缺失，当前映射依赖概述与 MIDI 场景推断，属高风险映射；HarmonyOS 已有接口级证据但 API 26 发行版本与行为待核实。为关键缺口，精研应优先补齐两平台正文并固定基线。

逐条引用及原文摘录见同目录 normalized.json。
