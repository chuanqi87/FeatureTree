# 经典蓝牙 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

三平台均读到经典蓝牙相关官方机制：Android 权限文档按 target SDK 区分权限集并以 FEATURE_BLUETOOTH 区分经典与 BLE；iOS Core Bluetooth 声明可与 BR/EDR（Classic）设备通信并列经典样例入口；HarmonyOS API diff 显示 SPP socket 与 A2DP 模块接口。各平台连接建立与配置文件完整正文均未读，基线未固定，全部为 low 初判，建议 P1 补 API 参考后精研。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | documented_mechanism | direct | 官方权限文档区分经典蓝牙与 BLE：target Android 12+ 需 BLUETOOTH_SCAN/ADVERTISE/CONNECT 运行时权限（旧权限设 maxSdkVersion=30），target 11 及以下需 BLUETOOTH；经 android.hardware.bluetooth 特性声明与 FEATURE_BLUETOOTH 运行时检查经典可用性，BLUETOOTH 权限明示覆盖经典连接、接受连接与数据传输。 | recommended |
| ios | documented_mechanism | direct | Core Bluetooth 框架页明示可与 BR/EDR（Classic）设备通信，并单列 Bluetooth Classic Support 主题指向 Using Core Bluetooth Classic 样例（关联 WWDC19 session 901）；样例页仅 11 行落地简介，无经典 API 细节；iOS 13 起链接的 App 须提供 NSBluetoothAlwaysUsageDescription，否则崩溃。 | recommended |
| harmonyos | documented_mechanism | indirect | oh_bluetooth.h NDK 仅提供蓝牙开关状态查询（起始版本 13，状态含 LE only 模式）；Connectivity Kit API diff 显示 @ohos.bluetooth.socket 存在 sppWriteAsync/sppReadAsync 接口记录，@ohos.bluetooth.a2dp 新增 CodecInfoList/CodecBitRate/CodecFrameLength 等，可作 SPP/A2DP 经典配置文件 API 存在的间接证据。 | recommended |

## android 条件与证据

适用范围：文档按 target SDK 分层（Android 12/API 31 及以上与 Android 11/API 30 及以下）描述权限集；正文未标注文档适用的最高 API Level，最新正式版未核实。
条件：target Android 12（API 31）及以上：BLUETOOTH_SCAN/BLUETOOTH_ADVERTISE/BLUETOOTH_CONNECT 为运行时权限，旧 BLUETOOTH/BLUETOOTH_ADMIN 声明需设 maxSdkVersion=30；target Android 11（API 30）及以下：BLUETOOTH 权限用于经典或 BLE 通信，扫描需 ACCESS_FINE_LOCATION 运行时权限；经典蓝牙可用 <uses-feature android.hardware.bluetooth required> 声明，运行时以 PackageManager.FEATURE_BLUETOOTH 检查；Android 8.0（API 26）+ 可改用 Companion Device Manager 配对且不要求位置权限
缺口：未读 BluetoothAdapter/BluetoothSocket（RFCOMM）及各经典配置文件 API 参考正文，经典连接与 profile 范围仅有权限侧描述；文档快照未核实适用 API Level 上限与启动日最新正式版（version_verified=false）；CDM 路径与传统权限路径对经典配置文件能力的覆盖差异未读正文；后台扫描/连接对经典蓝牙的限制（如 ACCESS_BACKGROUND_LOCATION 的适用范围）仅有局部描述
真机分类理由：经典蓝牙连接与配置文件行为依赖设备无线电硬件与系统实现，且基线未固定；文档初判不足以确认实机连接表现，正式确认前建议真机验证。

- [Bluetooth permissions](https://developer.android.com/develop/connectivity/bluetooth/bt-permissions)，开头概述：使用蓝牙须声明权限并指明需要经典蓝牙或 BLE 支持，正文 3–7 行；获取 2026-09-05T10:24:15.481622+00:00；SHA ddbdf41370ec599a02b570a7f1721c3f45d495fac6dfda30da8c8fcbfc8cddb1。
- [Bluetooth permissions](https://developer.android.com/develop/connectivity/bluetooth/bt-permissions)，Target Android 12 or higher：BLUETOOTH_SCAN/ADVERTISE/CONNECT 清单与旧权限 maxSdkVersion=30，正文 33–53 行；获取 2026-09-05T10:24:15.481622+00:00；SHA ddbdf41370ec599a02b570a7f1721c3f45d495fac6dfda30da8c8fcbfc8cddb1。
- [Bluetooth permissions](https://developer.android.com/develop/connectivity/bluetooth/bt-permissions)，三项新权限为运行时权限，须经用户批准（Nearby devices），正文 61–68 行；获取 2026-09-05T10:24:15.481622+00:00；SHA ddbdf41370ec599a02b570a7f1721c3f45d495fac6dfda30da8c8fcbfc8cddb1。
- [Bluetooth permissions](https://developer.android.com/develop/connectivity/bluetooth/bt-permissions)，Target Android 11 or lower：BLUETOOTH 权限用于经典或 BLE 的连接、接受连接与传输，正文 143–148 行；获取 2026-09-05T10:24:15.481622+00:00；SHA ddbdf41370ec599a02b570a7f1721c3f45d495fac6dfda30da8c8fcbfc8cddb1。
- [Bluetooth permissions](https://developer.android.com/develop/connectivity/bluetooth/bt-permissions)，uses-feature android.hardware.bluetooth 声明经典蓝牙为必需，正文 212–217 行；获取 2026-09-05T10:24:15.481622+00:00；SHA ddbdf41370ec599a02b570a7f1721c3f45d495fac6dfda30da8c8fcbfc8cddb1。
- [Bluetooth permissions](https://developer.android.com/develop/connectivity/bluetooth/bt-permissions)，运行时 PackageManager.FEATURE_BLUETOOTH 检查经典蓝牙是否可用，正文 241–245 行；获取 2026-09-05T10:24:15.481622+00:00；SHA ddbdf41370ec599a02b570a7f1721c3f45d495fac6dfda30da8c8fcbfc8cddb1。

## ios 条件与证据

适用范围：框架页提到 iOS 13 起链接需 NSBluetoothAlwaysUsageDescription、iOS 12 及更早用旧键、iOS 26 起配合 Live Activity 可保留部分后台扫描权限；经典支持本身无 availability 元数据，iOS 适用版本未核实。
条件：链接 iOS 13 或更高版本的 App 须在 Info.plist 含 NSBluetoothAlwaysUsageDescription，iOS 12 及更早使用 NSBluetoothPeripheralUsageDescription；Core Bluetooth 后台执行模式不支持在 macOS 上运行的 iPad App；iOS 26+ 起 App 启动 Live Activity 进入后台后可保留部分前台权限（如无 UUID 扫描、关闭去重过滤）；不得子类化 Core Bluetooth 类，覆盖会导致未定义行为
缺口：Using Core Bluetooth Classic 仅 11 行样例落地页，经典设备发现与通信的具体 API 正文未读到；经典蓝牙 profile（如 SPP/A2DP 类串口/音频）在 iOS 的可用性正文未读，不得据此推断 iOS 不支持任何 profile；框架页无经典相关符号 availability 元数据，Apple 目录含多平台，iOS 适用性与最低版本未逐符号核对；经典蓝牙是否涉及 MFi/ExternalAccessory 等其他框架未在冻结来源中覆盖
真机分类理由：BR/EDR 通信依赖设备硬件与 iOS 版本，样例正文未展开实现细节且 availability 未核实；正式确认经典连接与 profile 行为前建议真机验证。

- [Core Bluetooth](https://developer.apple.com/documentation/corebluetooth)，Core Bluetooth 框架概述：与 BLE 和 BR/EDR（Classic）设备通信，正文 3–7 行；获取 2026-09-05T09:34:21.400334+00:00；SHA 248c4c6af3a8e8a9658cf9e3492f6e12039b70b1fcd1fefc0d2e5d4810a49c03。
- [Core Bluetooth](https://developer.apple.com/documentation/corebluetooth)，Important：iOS 13 起链接的 App 需 NSBluetoothAlwaysUsageDescription，缺失会崩溃，正文 18–19 行；获取 2026-09-05T09:34:21.400334+00:00；SHA 248c4c6af3a8e8a9658cf9e3492f6e12039b70b1fcd1fefc0d2e5d4810a49c03。
- [Core Bluetooth](https://developer.apple.com/documentation/corebluetooth)，Topics > Bluetooth Classic Support：指向 Using Core Bluetooth Classic 样例，正文 125–129 行；获取 2026-09-05T09:34:21.400334+00:00；SHA 248c4c6af3a8e8a9658cf9e3492f6e12039b70b1fcd1fefc0d2e5d4810a49c03。
- [Using Core Bluetooth Classic](https://developer.apple.com/documentation/corebluetooth/using-core-bluetooth-classic)，样例页概述：用 Core Bluetooth API 发现并通信经典蓝牙设备，关联 WWDC 2019 session 901，正文 3–7 行；获取 2026-09-05T10:19:05.460431+00:00；SHA c3b570f36cb1aa1aa6e75035b8fee951c4b7482822976728bc67fe4892277372。

## harmonyos 条件与证据

适用范围：oh_bluetooth.h 标注起始版本 13（SystemCapability.Communication.Bluetooth.Core，libbluetooth_ndk.so）；API diff 页正文未标明适用 HarmonyOS/API 版本号（仅 URL 含 5111 线索），发行版未核实。
条件：NDK oh_bluetooth.h 需引用 ConnectivityKit/bluetooth/oh_bluetooth.h 并链接 libbluetooth_ndk.so，起始版本 API 13；蓝牙开关状态区分经典开关与 BLE only 模式（BLUETOOTH_STATE_BLE_ON 等枚举）；API diff 显示 SPP 异步读写接口位于 @ohos.bluetooth.socket.d.ts，A2DP 编解码配置接口位于 @ohos.bluetooth.a2dp.d.ts
缺口：未读 @ohos.bluetooth.socket/@ohos.bluetooth.a2dp 等 API 参考正文，SPP 连接建立、权限要求与错误码未核实；API diff 页未标明适用 HarmonyOS 版本，HarmonyOS 与 OpenHarmony 发行版区分未核；BR/EDR 连接生命周期、后台限制与配对指南正文未读；oh_bluetooth.h 与经典蓝牙能力无直接对应；手机/平板形态上的经典蓝牙 profile 支持清单未核实
真机分类理由：经典蓝牙 profile 行为依赖设备硬件与具体 HarmonyOS 版本，且适用发行版未核实；正式确认前建议真机验证。

- [oh_bluetooth.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-bluetooth-h)，oh_bluetooth.h 概述：查询蓝牙开关状态接口、库、系统能力与起始版本 13，正文 3–13 行；获取 2026-09-04T04:07:05.243692+00:00；SHA 8a79a6390695cf2eb10898f0577831e8c7e63fcd6e1693a20b3965a5617a019a。
- [oh_bluetooth.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-bluetooth-h)，Bluetooth_SwitchState 枚举表：含 BLE only 模式各状态，正文 46–54 行；获取 2026-09-04T04:07:05.243692+00:00；SHA 8a79a6390695cf2eb10898f0577831e8c7e63fcd6e1693a20b3965a5617a019a。
- [Connectivity Kit](https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-5111)，socket 模块 sppWriteAsync/sppReadAsync 差异记录（@ohos.bluetooth.socket.d.ts），正文 3–6 行；获取 2026-09-05T11:01:29.643524+00:00；SHA c200fc88b0de6a53bf4a213bd2a99228cf506d2440dadafd29743af93136fb82。
- [Connectivity Kit](https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-5111)，a2dp 模块新增 CodecInfoList/CodecBitRate/CodecFrameLength 等接口（@ohos.bluetooth.a2dp.d.ts），正文 27–46 行；获取 2026-09-05T11:01:29.643524+00:00；SHA c200fc88b0de6a53bf4a213bd2a99228cf506d2440dadafd29743af93136fb82。

## 待验证差异假设

- permissions_privacy：权限与声明模型可能不同（can 级）：Android 按 target SDK 分层声明蓝牙权限组合（Android 12+ 为 BLUETOOTH_CONNECT 等运行时权限，target 11 及以下为 BLUETOOTH+位置权限）；iOS 以 Info.plist 用途描述键（iOS 13 起链接 NSBluetoothAlwaysUsageDescription，缺失即崩溃）控制访问；HarmonyOS 对应权限模型本轮未读到正文。；待核：HarmonyOS 蓝牙权限正文未读，无法纳入三方比较；各平台运行时授予流程对经典蓝牙与 BLE 的区分粒度待核。
- api_surface：经典蓝牙能力的 API 组织方式可能不同（can 级）：iOS 由统一 Core Bluetooth 框架声明同时覆盖 LE 与 BR/EDR；Android 在特性与权限层并列区分经典与 BLE 两种标志（FEATURE_BLUETOOTH 与 FEATURE_BLUETOOTH_LE）；HarmonyOS 在 @ohos.bluetooth 下按配置文件分模块组织（socket 对应 SPP、a2dp 对应 A2DP 编解码配置）。；待核：各平台实际可用的经典 profile 清单与能力深度需读 API 参考正文核实；iOS 经典设备交互的具体 API 与限制未在样例正文展开；HarmonyOS socket/a2dp 模块与经典连接建立的完整机制未读。

范围缺口：本轮 6 篇冻结正文均非经典蓝牙连接建立与配置文件的完整 API 参考：Android 未含 BluetoothAdapter/BluetoothSocket 正文，iOS 经典样例为落地页，HarmonyOS 仅有 API diff 记录与开关状态 NDK；启动日基线 unresolved，三平台最新正式版与手机形态基线均未核实，全部结论为 low 初判；HarmonyOS API diff 适用版本、Apple 符号级 iOS availability、Android 文档 API Level 适用范围均未核实；经典配置文件（A2DP/HFP/SPP 等）各平台支持清单、后台与隐私限制正文未读

后续优先级：P1；三平台经典蓝牙连接与配置文件的核心 API 正文均未读到：iOS 经典样例无实现细节、HarmonyOS 仅 diff 记录、Android 仅权限侧文档，属高风险映射且缺口关键，需优先补读各平台 API 参考/指南后再精审。

逐条引用及原文摘录见同目录 normalized.json。
