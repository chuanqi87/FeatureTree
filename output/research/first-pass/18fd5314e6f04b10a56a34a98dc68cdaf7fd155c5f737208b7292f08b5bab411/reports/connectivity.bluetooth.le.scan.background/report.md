# BLE后台扫描 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

Android 与 iOS 均有后台 BLE 扫描的直接官方文档：Android 后台使用扫描 API 需应用进程存活，进程未运行时可用 PendingIntent 版 startScan 投递匹配结果；iOS 需 bluetooth-central 后台模式、后台必须指定 serviceUUIDs 且扫描选项无效，iOS 26+ 可借 Live Activity 保留前台扫描特权。HarmonyOS @ohos.bluetooth.ble 仅文档化回调式 startBLEScan 机制，全文未见后台/前台表述，只能 possible_mapping。版本基线未固定，全部 low，真机未验证。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | documented_mechanism | direct | 官方《Communicate in the background》指南明示：应用不可见时使用 BluetoothLeScanner 或 CompanionDeviceManager 没有限制，但需应用进程存活；进程未运行时 BluetoothLeScanner 可改用 PendingIntent 版 startScan 在匹配设备出现时投递结果，官方不建议周期性调度扫描。android.bluetooth.le 包自 API 21 提供 BluetoothLeScanner/ScanFilter/ScanSettings/ScanCallback。 | recommended |
| ios | documented_mechanism | direct | Core Bluetooth 文档明示：声明 bluetooth-central 后台模式即可后台扫描，但必须显式指定 serviceUUIDs，且 CBCentralManager 扫描选项在后台无效；iOS 26+ 若已实例化 CBManager 并启动 Live Activity，可在后台保留前台同等扫描特权（无 UUID 扫描、禁用去重过滤）；iPad apps 运行于 macOS 不支持蓝牙后台模式。scanForPeripherals 新参数会覆盖旧参数。 | recommended |
| harmonyos | possible_mapping | indirect | @ohos.bluetooth.ble 模块文档化 startBLEScan/stopBLEScan：需 ohos.permission.ACCESS_BLUETOOTH、仅 Stage 模型、SystemCapability.Communication.Bluetooth.Core，单路扫描（多路需 API 15+ BleScanner），结果经 on('BLEDeviceFind') 回调。但全文 6077 行未见任何后台/前台扫描行为表述，后台可用性与挂起/唤醒条件未文档化，扫描接口只能视为可能映射。 | unassessed |

## android 条件与证据

适用范围：developer.android.com 当前指南（抓取 2026-09-05），正文提及 Android 10+/12+ 行为变化；android.bluetooth.le 包 API 21+；未固定 API Level 与手机基线。
条件：后台使用扫描 API 无限制但需应用进程存活（回调式）；进程未运行时可改用 PendingIntent 版 startScan 接收匹配过滤设备的结果；外设必须在广播中才能经 PendingIntent 唤醒应用；通用后台工作规则同样适用于蓝牙任务；Android 12+ 有前台服务启动限制；官方不建议周期性调度扫描（无论设备在不在范围都会周期唤醒进程）
缺口：BluetoothLeScanner.startScan(List, ScanSettings, PendingIntent) 重载的 API 参考正文未在本包读取；BLUETOOTH_SCAN 等权限要求及其版本演变未在本包正文核实；Doze/应用待机对后台扫描的具体配额与停止条件未在读取正文展开；未固定 Android 版本基线，指南所述行为与具体版本的对应需后续核对
真机分类理由：机制已由官方指南明示（进程存活、PendingIntent、前台服务限制），但 Doze/厂商电源管理对后台扫描的实际停止与结果投递时序未量化，真机可验证；非本轮必需。

- [Communicate in the background](https://developer.android.com/develop/connectivity/bluetooth/ble/background)，Find a device > In the background：进程存活要求与 PendingIntent 扫描，正文 43–64 行；获取 2026-09-05T10:24:14.792416+00:00；SHA 182ec066ae789fe02b98a1c9bc494ff9f92c105f42237812ec86d52f0a3e98bf。
- [Communicate in the background](https://developer.android.com/develop/connectivity/bluetooth/ble/background)，Note：通用后台工作规则适用于蓝牙任务，正文 19–21 行；获取 2026-09-05T10:24:14.792416+00:00；SHA 182ec066ae789fe02b98a1c9bc494ff9f92c105f42237812ec86d52f0a3e98bf。
- [android.bluetooth.le](https://developer.android.com/reference/android/bluetooth/le/package-summary)，android.bluetooth.le 包 Added in API level 21，正文 3–3 行；获取 2026-09-05T10:39:42.849773+00:00；SHA 887ae99c2ead2aa5fd260a0d530b2a81f655bf0a2d294561fd2fcadb0f87b309。
- [android.bluetooth.le](https://developer.android.com/reference/android/bluetooth/le/package-summary)，Classes：BluetoothLeScanner 提供 BLE 扫描操作，正文 26–26 行；获取 2026-09-05T10:39:42.849773+00:00；SHA 887ae99c2ead2aa5fd260a0d530b2a81f655bf0a2d294561fd2fcadb0f87b309。

## ios 条件与证据

适用范围：框架页提及 iOS 26（Live Activity）与 iOS 13+（NSBluetoothAlwaysUsageDescription，链接后应用）；scanForPeripherals 快照未标注 availability；未固定 iOS 版本基线。
条件：需在应用中指定 bluetooth-central 后台模式；后台扫描必须显式指定一个或多个 serviceUUIDs；CBCentralManager 扫描选项在后台无效；iOS 26+ 需实例化 CBManager 并在进入后台前启动 Live Activity 才保留前台特权；iPad apps 运行在 macOS 上不支持 Core Bluetooth 后台执行模式
缺口：bluetooth-central 模式的声明步骤正文（如 Choosing background modes）未在本包读取；后台扫描的系统调度、时长限制与终止条件未在读取正文说明；scanForPeripherals 快照无 availability 元数据，iOS 适用版本需用符号页/DocC JSON 核实；Apple 目录含 macOS 等其他平台，本包仅读框架页与一个方法页，需逐符号核对 iOS 适用性
真机分类理由：后台模式与 UUID 过滤为声明式机制，可静态核实；但系统对后台扫描的实际调度、终止行为及 iOS 26 Live Activity 特权边界需真机确认；非本轮必需。

- [scanForPeripherals(withServices:options:)](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/scanforperipherals(withservices:options:))，Discussion：bluetooth-central 后台模式、serviceUUIDs 要求、扫描选项后台无效，正文 26–28 行；获取 2026-09-05T16:45:20.610016+00:00；SHA 24bdafc40e68c9735183ff4fa376d828a06c71ce94ee366b3af903f87e40526f。
- [scanForPeripherals(withServices:options:)](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/scanforperipherals(withservices:options:))，Discussion：serviceUUIDs 过滤语义与新参数覆盖旧参数，正文 21–26 行；获取 2026-09-05T16:45:20.610016+00:00；SHA 24bdafc40e68c9735183ff4fa376d828a06c71ce94ee366b3af903f87e40526f。
- [Core Bluetooth](https://developer.apple.com/documentation/corebluetooth)，Overview：iPad apps on macOS 不支持蓝牙后台模式；iOS 26 Live Activity 后台保留前台特权，正文 11–16 行；获取 2026-09-05T09:34:21.400334+00:00；SHA 248c4c6af3a8e8a9658cf9e3492f6e12039b70b1fcd1fefc0d2e5d4810a49c03。
- [Core Bluetooth](https://developer.apple.com/documentation/corebluetooth)，Important：iOS 13+ 链接后需 NSBluetoothAlwaysUsageDescription，正文 18–19 行；获取 2026-09-05T09:34:21.400334+00:00；SHA 248c4c6af3a8e8a9658cf9e3492f6e12039b70b1fcd1fefc0d2e5d4810a49c03。

## harmonyos 条件与证据

适用范围：模块首批接口 API 10+，正文提及 BleScanner（API 15+）与 API 23 权限说明；HarmonyOS 具体发行版/SDK 版本未固定；harmonyos-2 为历史 API 迁移 diff 记录。
条件：需 ohos.permission.ACCESS_BLUETOOTH 权限；仅可在 Stage 模型下使用；startBLEScan 单路扫描，下次调用前需先 stopBLEScan；设备需具备 SystemCapability.Communication.Bluetooth.Core 且蓝牙开启
缺口：@ohos.bluetooth.ble 全文（6077 行）无后台/前台扫描表述，后台扫描可用性未知；HarmonyOS 后台任务（长时任务/应用挂起）与蓝牙扫描的关系需读后台任务指南核实，本包未含该资料；未固定 HarmonyOS 发行版与 API 版本基线；OpenHarmony 与 HarmonyOS 发行版行为差异未核对
真机分类理由：静态文档未说明后台扫描行为，无法基于本包资料评估真机验证方案；需先补读 HarmonyOS 后台任务/长时任务指南再分类。

- [@ohos.bluetooth.ble (蓝牙ble模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble)，ble.startBLEScan：发起扫描、单路限制、权限与 Stage 模型约束，正文 288–304 行；获取 2026-09-05T09:34:21.800954+00:00；SHA f1d80db2df10406273b22c90053098e4370a49f6924dd1618d93759c7d19ce2f。
- [@ohos.bluetooth.ble (蓝牙ble模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble)，扫描结果经 on('BLEDeviceFind') 回调获取，正文 294–294 行；获取 2026-09-05T09:34:21.800954+00:00；SHA f1d80db2df10406273b22c90053098e4370a49f6924dd1618d93759c7d19ce2f。
- [@ohos.bluetooth.ble (蓝牙ble模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble)，模块首批接口从 API version 10 开始支持，正文 5–5 行；获取 2026-09-05T09:34:21.800954+00:00；SHA f1d80db2df10406273b22c90053098e4370a49f6924dd1618d93759c7d19ce2f。
- [Connectivity Kit](https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-hdc)，API diff：startBLEScan 新增于 @ohos.bluetooth.ble（历史接口迁移记录），正文 1141–1141 行；获取 2026-09-05T11:01:32.042523+00:00；SHA 61ed7d37c963ecd55ca636b57c784bcc6362dd366cf2a7b4e1ad3c5c095073ee。

## 待验证差异假设

- lifecycle_background：后台扫描的进程存活要求与结果投递机制可能不同：Android 指南明示后台使用 BluetoothLeScanner 需应用进程存活、进程未运行时改用 PendingIntent 投递匹配结果；iOS 明示以 bluetooth-central 后台模式在后台扫描并接收委托回调。；待核：HarmonyOS 后台扫描是否存在、结果如何投递未知（本包资料无后台表述）；iOS bluetooth-central 模式下进程被系统终止后扫描是否持续，未在读取正文说明。
- limits_precision：后台扫描的过滤参数约束可能不同：iOS 文档明示后台必须显式指定 serviceUUIDs 且扫描选项（如去重过滤）在后台无效；Android 指南的后台 PendingIntent 扫描未强制要求服务 UUID 过滤（过滤用于匹配投递）；HarmonyOS filters 可为 null 仅建议填写且未区分前后台。；待核：Android 后台扫描是否受扫描频次/配额或 Doze 限制，未在读取正文量化；HarmonyOS 若支持后台扫描是否强制过滤条件，完全未知。
- lifecycle_background：后台扫描特权的豁免路径可能不同：iOS 26+ 文档化 CBManager 实例加 Live Activity 可在后台保留前台扫描特权（无 UUID 扫描、禁用去重过滤）；Android 指南以后台限制加前台服务 connectedDevice 类型/CompanionDeviceManager/PendingIntent 为后台路径，读取资料中未见同类 Live Activity 式豁免。；待核：HarmonyOS 是否存在同类后台特权延续机制未知；iOS 26 Live Activity 特权的具体边界、降级与回收条件未在读取正文展开。

范围缺口：HarmonyOS：@ohos.bluetooth.ble API 参考无后台/前台扫描表述，后台任务（长时任务/挂起）指南与蓝牙扫描的关系未读取，后台可用性未知；Android：startScan(PendingIntent) 重载 API 参考、BLUETOOTH_SCAN 等权限要求与 Doze/配额影响未在本包核实；iOS：bluetooth-central 声明步骤正文与后台扫描系统终止条件未读取；scanForPeripherals 快照无 availability 元数据，iOS 适用版本待核；三平台最新正式版与手机基线均未固定，本包结论均为 first_pass 文档初判，不代表最新版本行为；平板形态仅 iOS 有 iPad apps on macOS 一句例外说明；Android/HarmonyOS 平板后台扫描行为未单独说明

后续优先级：P1；HarmonyOS 后台扫描完全缺乏文档依据属高风险映射（无法判断支持与否），且 Android/iOS 后台机制涉及进程存活模型、权限与过滤约束的关键差异，需优先精研补证。

逐条引用及原文摘录见同目录 normalized.json。
