# BLE广播 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

三平台文档初判：HarmonyOS错误码正文直接证实BLE广播机制（startAdvertising返回广播标识符、传统广播31字节上限、扩展广播除外），但js-apis-bluetooth-ble的API参考与权限不在本包；Android两篇冻结正文（BLE后台指南、广告标识符）均未覆盖应用作为Peripheral的广播机制；iOS两篇（AdSupport、BLE MIDI）仅为中心角色或无关主题。无跨平台双方证据，差异假设为空；基线未固定，全部low。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | unknown | missing | 两篇冻结正文均未覆盖应用作为Peripheral的BLE广播机制。android-1是BLE中心角色后台指南（扫描/连接），仅在外设发现语境提及外设须在广播（140行）；android-2主题为用户可重置的广告标识符（ad tracking），与BLE广播无关。未读到任何广播API正文。 | unassessed |
| ios | unknown | missing | 两篇均未覆盖应用作为Peripheral的广播接口。ios-1为AdSupport广告标识符框架（需配合App Tracking Transparency），与BLE广播无关；ios-2说明iOS 16+/macOS 13+系统对BLE MIDI外设的自动重连与CoreBluetooth连接步骤，均为中心角色视角。未读到CBPeripheralManager类广播接口正文。 | unassessed |
| harmonyos | documented_mechanism | direct | 错误码正文直接证实BLE广播机制：2902054规定传统广播报文上限31字节（扩展广播不受此限）；2902055表明存在startAdvertising接口并返回广播标识符（无效值默认0xFF），链接锚点指向js-apis-bluetooth-ble。另一篇@ohos.nearlink.advertising为星闪广播（起始版本26.0.0、NearLink.Base），属另一无线技术，不构成BLE证据。 | recommended |

## android 条件与证据

适用范围：快照2026-09-05抓取；正文仅提及Android 10/12行为变化，未声明API Level；广播API适用版本未读到，启动日基线未固定
条件：android-1：BLE扫描/连接API在应用不可见时可用，但需应用进程存活（45-47行）；android-1：进程被杀后后台连接关闭；Android 12+后台启动前台服务受限（101-107行）；未读到应用作为Peripheral广播的权限或运行条件
缺口：缺少应用侧广播API（如BluetoothLeAdvertiser/AdvertiseData路径）参考正文，本包无该来源；广播权限（如BLUETOOTH_ADVERTISE类）与运行条件未核实；广播后台限制、可连接广播与广播数据长度约束均未读到正文；最新正式版与手机基线未固定，不能声称当前版本支持或不支持
真机分类理由：冻结来源无广播机制正文，无法评估真机验证范围；需先补广播API参考与权限正文再判定

- [Communicate in the background](https://developer.android.com/develop/connectivity/bluetooth/ble/background)，Connect to a device > In the background（唯一advertising提法：外设须在广播，中心角色视角），正文 138–144 行；获取 2026-09-05T10:24:14.792416+00:00；SHA 182ec066ae789fe02b98a1c9bc494ff9f92c105f42237812ec86d52f0a3e98bf。
- [Communicate in the background](https://developer.android.com/develop/connectivity/bluetooth/ble/background)，Find a device > In the background（扫描API需进程存活），正文 43–47 行；获取 2026-09-05T10:24:14.792416+00:00；SHA 182ec066ae789fe02b98a1c9bc494ff9f92c105f42237812ec86d52f0a3e98bf。
- [Get a user-resettable advertising ID Part of Android Jetpack .](https://developer.android.com/identity/ad-id)，标题与导语（advertising ID广告标识符主题，与BLE广播无关），正文 1–12 行；获取 2026-09-05T10:32:24.231775+00:00；SHA 3ec63cc6c47545f1faa76fb8ea942472d84eee3dd11b8413d60a2557a6235ca1。

## ios 条件与证据

适用范围：快照2026-09-05抓取；ios-2提及iOS 16/macOS 13（BLE MIDI重连）、ios-1提及iOS 14.5+（广告标识符）；广播接口适用iOS版本未读到，启动日基线未固定
条件：ios-2：iOS 16+支持配对的BLE MIDI外设开机自动重连（7行）；ios-1：iOS 14.5+获取广告标识符需ATT授权（与BLE广播无关，9-11行）；未读到应用作为Peripheral广播的权限或运行条件
缺口：缺少CBPeripheralManager等广播接口正文，本包无该来源；广播接口的iOS适用性、最低系统版本与蓝牙权限说明未核实；广播后台模式与广播数据长度约束未读到正文；最新正式版与手机基线未固定，不能声称当前版本支持或不支持
真机分类理由：冻结来源无广播接口正文，无法评估真机验证需求；需先补广播接口与权限正文再判定

- [MIDI Bluetooth](https://developer.apple.com/documentation/coremidi/midi-bluetooth)，Discussion（BLE MIDI外设连接流程，中心角色），正文 5–17 行；获取 2026-09-05T10:19:31.589071+00:00；SHA ab572b5edaf882af58dfc263216a20694da4a1d8d1ea7aa9ae1a4f2090cbdae3。
- [AdSupport](https://developer.apple.com/documentation/adsupport)，Overview（advertisingIdentifier广告标识符），正文 5–11 行；获取 2026-09-05T10:29:51.126127+00:00；SHA 8dfc2d5ccee28ac0d8368c703ec4ed681783469229a2a424956156392f563a10。

## harmonyos 条件与证据

适用范围：错误码快照2026-09-04抓取，正文未声明适用API/SDK版本；URL锚点blestartadvertising11暗示API 11（未核实）；星闪篇起始版本26.0.0但非BLE；启动日基线未固定
条件：传统广播报文最大31字节，超限返回异常；该限制仅适用传统广播，不含扩展广播（974行）；广播标识符须为startAdvertising接口返回值，无效值默认0xFF（992行）；错误码正文未声明BLE广播权限要求与适用API版本
缺口：js-apis-bluetooth-ble的startAdvertising API参考正文不在本包，参数、权限（如ACCESS_BLUETOOTH类）与返回值未核实；startAdvertising适用API版本未核实（仅错误码文档URL锚点暗示API 11）；HarmonyOS与OpenHarmony发行版适用性未区分核实；扩展广播的接口、约束与手机设备支持范围未读到正文
真机分类理由：错误码描述的31字节上限与扩展广播行为依赖设备/芯片实现，且API适用版本未核实；精研时建议真机验证广播启停与报文长度行为

- [蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)，错误码2902054 广播报文超限（传统广播31字节上限，扩展广播除外），正文 962–978 行；获取 2026-09-04T04:07:05.243692+00:00；SHA 4042af7df2166c5fd6290d590a46c431c0462efbadfb5107b098efcad1ba98d6。
- [蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)，错误码2902055 广播标识符无效（引用js-apis-bluetooth-ble的startAdvertising），正文 980–996 行；获取 2026-09-04T04:07:05.243692+00:00；SHA 4042af7df2166c5fd6290d590a46c431c0462efbadfb5107b098efcad1ba98d6。
- [@ohos.nearlink.advertising (星闪广播能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-nearlink-advertising)，模块说明（星闪广播能力，起始版本26.0.0，非BLE），正文 1–5 行；获取 2026-09-05T10:27:40.751329+00:00；SHA ab47ab72d2f5f095fbeb17ca333c9d48358445078004096fef3a0ebf8024a9ff。
- [@ohos.nearlink.advertising (星闪广播能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-nearlink-advertising)，advertising.startAdvertising（星闪广播，权限ACCESS_NEARLINK，系统NearLink.Base），正文 137–149 行；获取 2026-09-05T10:27:40.751329+00:00；SHA ab47ab72d2f5f095fbeb17ca333c9d48358445078004096fef3a0ebf8024a9ff。

## 待验证差异假设

没有形成满足双方引用要求的差异假设；不代表没有差异。

范围缺口：Android：应用作为Peripheral的BLE广播API正文完全缺失，android-1仅为中心角色指南，android-2为广告标识符主题（无关）；iOS：CBPeripheralManager广播正文缺失，ios-1为广告标识符框架（无关），ios-2为中心角色BLE MIDI连接；HarmonyOS：js-apis-bluetooth-ble的startAdvertising API参考缺失，权限/参数/适用版本未核实；星闪广播为另一技术不可混作BLE证据；三平台广播后台限制、可连接/不可连接广播、扩展广播支持范围等比较维度均无正文；启动日最新正式版与手机基线未固定（version_baseline unresolved），所有初判仅限冻结快照

后续优先级：P1；Android与iOS的广播关键机制正文完全缺失，HarmonyOS仅有错误码级证据而缺API参考正文；且存在将广告标识符（advertising ID）或星闪广播误映射为BLE广播的高风险，属关键缺口，需优先补正文与版本核实

逐条引用及原文摘录见同目录 normalized.json。
