# 全量首轮粗分析

**初判资料，不是已确认知识；没有人工真机实测。**

目标 212 节点；当前 {'pending': 170, 'delivered': 33, 'failed': 1, 'running': 8}。叶子和父级范围草图分开计数：{'rollup': 106, 'leaf': 106}。
状态：running；截止：2026-09-07T11:26:00+08:00。
此处的全量是现有节点的首次调查覆盖，不是全部知识项精审，也不是三个完整SDK的覆盖证明。

所有正式置信度为 low；direct/indirect/missing 只是文档证据强弱，不能当 high/medium 使用。
父级仅初判自身范围，不自动继承或证明子节点的支持情况。失败和未运行项不会伪填研究结论。

| 节点 | 角色 | 执行状态 | 精研优先级 | 初步摘要 |
| --- | --- | --- | --- | --- |
| 无障碍 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 无障碍框架 | rollup | pending | 未评估 | 尚未取得合格初判 |
| [无障碍树与语义](reports/a11y.framework.tree/report.md) | leaf | delivered | P1 | 三平台均读到向辅助技术暴露语义的官方机制：Android Compose 并行语义树（merged/unmerged 双树、语义属性）；iOS UIKit accessibility element（label/hint/分组）与 Safari 网页内容无障碍树；HarmonyOS 服务卡片无障碍属性（API 8+）与 NDK Provider 节点树（API 13/23+）。三平台系统级树 API 正文均未读，版本基线未固定，全部 low 初判。 |
| 无障碍服务 | rollup | pending | 未评估 | 尚未取得合格初判 |
| [无障碍服务扩展](reports/a11y.service.extension/report.md) | leaf | delivered | P1 | 三平台文档初判：Android（Android 11 行为变更）证实应用可实现无障碍服务并以 AccessibilityServiceInfo flags 与服务元数据文件声明，但观察/操作界面能力正文未读到；HarmonyOS 明示 AccessibilityExtensionAbility 允许三方应用实现、支持访问与操作前台界面，并给出 capabilities 与 Action 能力模型；iOS 冻结资料（BrowserEngineKit、Safari 16 说明）未涉及该机制，保持 unknown。全部 low 置信，基线未固定。 |
| AI与智能 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 端侧推理 | rollup | pending | 未评估 | 尚未取得合格初判 |
| [端侧ML运行时](reports/ai.on_device.runtime/report.md) | leaf | delivered | P1 | 三平台均读到官方端侧模型执行机制：Android LiteRT 经 Google Play services 分发并配 delegates/Acceleration Service；iOS Core ML 为平台框架统一调度 CPU/GPU/Neural Engine；HarmonyOS MindSpore Lite 经 NNRt 异构调度、要求 .ms 模型。均属机制级初判，三平台版本基线未固定；包内 ios-2（SwiftData/CoreData）与 harmonyos-2（ML-DSA 密码学）与本节点无关。差异假设聚焦分发方式、模型格式、加速暴露。 |
| 系统智能 | rollup | pending | 未评估 | 尚未取得合格初判 |
| [系统智能建议](reports/ai.system.suggestions/report.md) | leaf | delivered | P1 | Android 冻结来源仅 ML Kit Smart Reply（Google 生态库，英语会话、最多3条回复、API 23+），映射到系统级节点待确认；iOS 读到 Apple Intelligence Smart Reply（UIKit 会话上下文）与 Journaling Suggestions（entitlement+系统通知）两个系统机制，但文档未标注 iOS 版本；HarmonyOS 两篇来源（车机导航流转、性能测试）与本节点无关，unknown。差异假设：调用模型、生成限制、分发条件。全部 low。 |
| 应用模型 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 后台执行 | rollup | pending | 未评估 | 尚未取得合格初判 |
| [延迟与条件任务](reports/app.background.deferred_work/report.md) | leaf | delivered | P1 | Android 读到 WorkManager 约束式延迟任务机制（NetworkType/RequiresCharging 等约束使工作推迟到条件满足，系统 doze/待机桶进一步延迟并限额）；iOS 读到 BackgroundTasks 框架目录页（BGTaskScheduler 与 BGAppRefreshTask/BGProcessingTask 任务族），约束属性与调度时机细节不在本文。HarmonyOS 冻结两篇来源（Node-API 进程内异步、企业网络管理）均与本节点无关，保留 unknown。基线未固定，全部 low，差异假设仅限 Android/iOS。 |
| 前台长时任务 | leaf | failed | 未评估 | Difference outside assigned dimensions; Difference outside assigned dimensions; Difference outside assigned dimensions |
| 桌面能力 | rollup | pending | 未评估 | 尚未取得合格初判 |
| [桌面快捷方式](reports/app.desktop.shortcuts/report.md) | leaf | delivered | P1 | Android与HarmonyOS均读到明示的长按图标快捷方式机制：Android分静态/动态/固定三类，launcher最多同时显示4个静态+动态、设备上限各异、pinned无上限；HarmonyOS经shortcuts_config.json+module.json5 metadata静态配置，桌面最多展示4个，shortcutManager管理可见性，仅跳转UIAbility。iOS已读AppIntents App Shortcuts面向Shortcuts app/Siri/Spotlight，未见长按图标入口明示，仅算可能映射。三平台版本基线均未固定，结论全部low。提出3条差异假设：快捷方式类型与运行时能力、展示surface、数量上限机制。 |
| [桌面小组件](reports/app.desktop.widget/report.md) | leaf | delivered | P2 | 三平台均读到官方明示的桌面卡片机制：Android App Widget（RemoteViews/Glance，picker 添加、手势受限）、iOS WidgetKit（extension+SwiftUI、timeline 预算更新）、HarmonyOS ArkTS 卡片（FormExtensionAbility、共包/独立包）。刷新与打包形态存在文档级差异假设；版本基线与刷新约束未核实，全部为 low 初判。 |
| 扩展点 | rollup | pending | 未评估 | 尚未取得合格初判 |
| [分享扩展](reports/app.extensions.share/report.md) | leaf | delivered | P1 | 三平台文档初判：iOS 读到 share extension 官方机制（Xcode 模板、NSExtension/INSendMessageIntent 捐赠、SLComposeServiceViewController 预填）；HarmonyOS 读到 ShareExtensionAbility（三方可实现、系统服务管理）及 Share Kit 碰一碰跨设备分享；Android 两篇冻结来源（Firebase 扩展、KTX）与本节点无关，未能建立判断，不据此称不支持。差异假设 3 条均限 iOS/HarmonyOS；全部 low，未确认支持状态。 |
| 安装与更新 | rollup | pending | 未评估 | 尚未取得合格初判 |
| [轻量即用安装](reports/app.install.instant/report.md) | leaf | delivered | P1 | 三平台均读到官方轻量即用机制正文：Android 为 Google Play Instant（instant-enabled App Bundle，合计≤15MB、Android 8.0+、受限沙箱），且官方两处明示自 2025-12 起停发并终止所有 Instant API；iOS 为 App Clips（随父应用构建、invocation 入口、不驻留主屏）；HarmonyOS 为元服务（免安装、可独立上架、仅元服务API集，需 HarmonyOS NEXT DP1/API 11+）。三平台初判均 low，启动日基线未固定；主要缺口为 Android 终止后残余状态与 iOS/HarmonyOS 数值级限制。 |
| [应用安装更新](reports/app.install.package_update/report.md) | leaf | delivered | P1 | 首轮文档初判：仅 Android 读到应用级安装/更新机制正文（Google Play EMM API Installs，update 可远程安装或把已装应用更新到最新版本，但方法已弃用且文档明示 2025-09-30 后不可访问）；iOS 两篇分别为 SKAdNetwork 广告归因安装验证与 MDM 系统软件更新强制；HarmonyOS 两篇为 ohpm 开发期依赖更新与 MDM OTA 固件更新，均非应用级机制。三平台应用级安装/更新文档缺口并存，基线未固定，全部 low。 |
| 组件生命周期 | rollup | pending | 未评估 | 尚未取得合格初判 |
| [界面组件生命周期](reports/app.lifecycle.activity_ability/report.md) | leaf | delivered | P1 | 三平台均读到前台界面组件生命周期官方正文：Android Activity定义七回调、四状态与三个生命期，重建后经savedInstanceState/rememberSaveable自动恢复；iOS UIViewController以视图出现/消失回调为主，状态保留为opt-in(restorationIdentifier+恢复归档)；HarmonyOS UIAbility(仅Stage模型,API9+首批)为组件级四状态，页面加载在onWindowStageCreate，onSaveState仅限appRecovery故障场景。初判回调粒度与状态恢复触发条件存在结构性差异；iOS入口组件映射与三平台版本基线是主要缺口。 |
| [进程与内存回收](reports/app.lifecycle.process/report.md) | leaf | delivered | P1 | 三平台均读到因内存查杀应用进程的机制正文：Android LMK 按进程重要性终止后台进程，Android 17 起 cgroup v2 Memory Limiter 按前后台动态限额并可静默查杀，可用 ApplicationExitInfo 查询被杀原因；iOS 内存压力下经低内存通知后 jetsam 终止应用（per-process-limit/vm-pageshortage 等 reason）；HarmonyOS 6.1.0 起资源泄漏管控与内核查杀（如 RSS 超整机内存 1/3 且低内存，不区分前后台）。被杀后恢复策略三平台包内均无来源，进程优先级细节均不足；基线未固定，全部 low。 |
| 商业与增长 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 广告 | rollup | pending | 未评估 | 尚未取得合格初判 |
| [广告SDK](reports/commerce.ads.sdk/report.md) | leaf | delivered | P1 | 三平台广告SDK初判：Android/iOS 均读到 Google AdMob（Mobile Ads SDK）官方正文，文档化 Banner/Interstitial（iOS 另有 Native）/Rewarded 广告单元及清单配置与初始化机制；C++ 跨平台路径已弃用（2025-06 EoM），instant app 广告路径 2025-12 终止。HarmonyOS 本包仅有智能体广告展示合规规范与 hvigor 构建错误码，未见应用内广告 SDK 正文，判 unknown。均为生态服务证据，版本基线未固定，置信度 low。 |
| 分析 | rollup | pending | 未评估 | 尚未取得合格初判 |
| [分析事件](reports/commerce.analytics.events/report.md) | leaf | delivered | P1 | 三平台均读到自定义事件采集官方机制：Android/iOS 为 Firebase Analytics logEvent（500 种事件类型上限、名称区分大小写、控制台报表），HarmonyOS 为系统级 hiAppEvent.write+addWatcher（domain/name/参数规格受限、本地存储订阅）。上传侧 Firebase 有控制台与调试日志证据，HarmonyOS 冻结来源未覆盖云端上报，生态对位服务未核实；全部 low 置信，基线未固定。 |
| 应用内购买 | rollup | pending | 未评估 | 尚未取得合格初判 |
| [内购商品](reports/commerce.iap.products/report.md) | leaf | delivered | P1 | 三平台均读到内购商品查询/购买机制：Android 经 Play Billing（Unity 插件、Play Points 指南）见购买流程、延迟购买与店外购买交付；iOS StoreKit views 列四类商品、StoreView 展示并监听交易；HarmonyOS IAP Kit 有 queryEnvironmentStatus 地区前置检查与 queryProducts 单类型≤200条约束。Android 客户端查询主流程、iOS 购买 API 版本、HarmonyOS 购买流程正文未读到，全部 low 初判。 |
| 连接与外设 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 蓝牙 | rollup | pending | 未评估 | 尚未取得合格初判 |
| [经典蓝牙](reports/connectivity.bluetooth.classic/report.md) | leaf | delivered | P1 | 三平台均读到经典蓝牙相关官方机制：Android 权限文档按 target SDK 区分权限集并以 FEATURE_BLUETOOTH 区分经典与 BLE；iOS Core Bluetooth 声明可与 BR/EDR（Classic）设备通信并列经典样例入口；HarmonyOS API diff 显示 SPP socket 与 A2DP 模块接口。各平台连接建立与配置文件完整正文均未读，基线未固定，全部为 low 初判，建议 P1 补 API 参考后精研。 |
| 低功耗蓝牙 | rollup | pending | 未评估 | 尚未取得合格初判 |
| [BLE广播](reports/connectivity.bluetooth.le.advertise/report.md) | leaf | delivered | P1 | 三平台文档初判：HarmonyOS错误码正文直接证实BLE广播机制（startAdvertising返回广播标识符、传统广播31字节上限、扩展广播除外），但js-apis-bluetooth-ble的API参考与权限不在本包；Android两篇冻结正文（BLE后台指南、广告标识符）均未覆盖应用作为Peripheral的广播机制；iOS两篇（AdSupport、BLE MIDI）仅为中心角色或无关主题。无跨平台双方证据，差异假设为空；基线未固定，全部low。 |
| [BLE连接](reports/connectivity.bluetooth.le.connect/report.md) | leaf | delivered | P1 | 三平台均读到 BLE/GATT 连接机制：Android 概述明示权限→扫描→连接 GATT server 流程；iOS 仅 MIDI 场景明示 CoreBluetooth 扫描连接与 iOS 16+ 系统自动重连；HarmonyOS 接口级明示 GattClientDevice.connect、GattSetting/GattServer.connect(autoConnect) 及 ACCESS_BLUETOOTH 权限与 API 10/26 版本。基线未固定，全部 low；Android 连接指南与 iOS Core Bluetooth 正文缺失为主要缺口。 |
| [GATT读写通知](reports/connectivity.bluetooth.le.gatt/report.md) | leaf | delivered | P1 | 三平台文档初判：Android 指南以 BluetoothGatt 回调模型覆盖服务发现/读特征/通知（需手动写 CCCD 描述符）；HarmonyOS GATT 指南完整给出客户端读写特征值与通知/指示使能 API 及服务端收发流程；iOS 仅读到 Core Bluetooth 框架概览页，特征读写与通知订阅的具体操作 API 未在本包正文出现。提出通知使能方式、异步串行约束、权限形态 3 条差异假设。版本基线未固定，全部 low 初判。 |
| BLE扫描 | rollup | pending | 未评估 | 尚未取得合格初判 |
| [BLE后台扫描](reports/connectivity.bluetooth.le.scan.background/report.md) | leaf | delivered | P1 | Android 与 iOS 均有后台 BLE 扫描的直接官方文档：Android 后台使用扫描 API 需应用进程存活，进程未运行时可用 PendingIntent 版 startScan 投递匹配结果；iOS 需 bluetooth-central 后台模式、后台必须指定 serviceUUIDs 且扫描选项无效，iOS 26+ 可借 Live Activity 保留前台扫描特权。HarmonyOS @ohos.bluetooth.ble 仅文档化回调式 startBLEScan 机制，全文未见后台/前台表述，只能 possible_mapping。版本基线未固定，全部 low，真机未验证。 |
| [BLE批量扫描结果](reports/connectivity.bluetooth.le.scan.batch/report.md) | leaf | delivered | P1 | 三平台冻结源均未明示BLE扫描结果的硬件/系统级批量投递机制。Android指南仅展示逐条onScanResult交付，ScanSettings未提批量参数；iOS两源离题（MDM分批检索、MIDI连接）；HarmonyOS回调为数组（Array<ScanResult>/ScanReport）疑可聚合交付，但批量语义与节能意图未文档化。全部low置信，差异假设1条，需补API参考正文。 |
| [BLE扫描过滤](reports/connectivity.bluetooth.le.scan.filter/report.md) | leaf | delivered | P1 | 三平台均读到文档化BLE扫描过滤机制：Android ScanFilter(API 21+，UUID/名称/MAC/服务数据/厂商数据+mask组合，API 33增广播数据类型过滤)；HarmonyOS ble.ScanFilter(字段+mask+rssiThreshold，明示硬件过滤匹配模式与全系统共享过滤器配额)；iOS读文仅见scanForPeripherals按服务UUID扫描。过滤执行位置三平台静态文档均未完整说明，iOS过滤面宽度是最大缺口；均为初判low。 |
| NFC | rollup | pending | 未评估 | 尚未取得合格初判 |
| [主机卡模拟](reports/connectivity.nfc.hce/report.md) | leaf | delivered | P1 | 三平台均读到 HCE 官方机制:Android 4.4+ HostApduService 开放给任意应用;iOS 17.4+ CardSession 限 EEA 授权开发者(仅更新页,未见 API 正文);HarmonyOS cardEmulation 首批 API 6/HceService API 8+ 提供且明确禁灭屏。差异假设:准入与区域限制、灭屏行为、AID 注册与默认应用模型。置信全 low,启动日基线未固定。 |
| [NFC读写](reports/connectivity.nfc.reader/report.md) | leaf | delivered | P1 | 三平台均直接文档化 NFC 标签读写：Android 概述明示 Reader/writer mode（读写无源标签/贴纸，框架以 NDEF 为核心）；iOS Core NFC 明示读取 NDEF（类型1–5）并向可写标签写入，经 reader session 类完成；HarmonyOS 指南给出前台/后台读写流程、tag 模块技术对象（API 9+）与 ohos.permission.NFC_TAG。差异假设集中于发现/分发模型、权限声明方式与发现前置条件（HarmonyOS 需亮屏解锁、iOS 有免应用后台读取入口）。Android 仅概述级正文、Apple 版本适用性未核、HarmonyOS tag API 参考未读；全部 low 置信，真机均判 required。 |
| USB | rollup | pending | 未评估 | 尚未取得合格初判 |
| [USB主机模式](reports/connectivity.usb.host/report.md) | leaf | delivered | P1 | Android 指南直接描述应用级 USB 主机模式（API 12+、硬件相关、需用户授权）；iOS 冻结来源仅 USBDriverKit 驱动级符号目录、无 iOS 适用性标注；HarmonyOS 有 USB 服务术语表与旧 @ohos.usb 主机 API 的 API 9 废弃记录，现行 API 面未覆盖。三条差异假设涉及 API 表面、可用性条件与设备匹配层级。全部 low 置信初判，基线未固定。 |
| Wi-Fi | rollup | pending | 未评估 | 尚未取得合格初判 |
| [Wi-Fi连接建议](reports/connectivity.wifi.connect/report.md) | leaf | delivered | P1 | Android读到Wi-Fi建议API（Android 10+，应用提交建议、平台最终决定，按应用审批，建议不入保存网络列表）；HarmonyOS读到STA候选网络机制（addCandidateConfig+connectToCandidateConfig，需STA能力与GET/SET_WIFI_INFO权限，版本未注明）；iOS两篇冻结来源（Siri事件建议Markup、Wi-Fi Aware点对点配对）均未建立本节点机制。差异假设集中于连接决策归属、审批权限模型与API用例面。全部low，版本基线未固定。 |
| [Wi-Fi扫描](reports/connectivity.wifi.scan/report.md) | leaf | delivered | P1 | Android 文档明确 WifiManager 扫描流程、位置权限与前台/后台节流；HarmonyOS 文档给出 getScanInfoList 获取结果，但主动扫描接口 API version 10 起废弃、替代仅向系统应用开放；iOS TN3111 明示无通用 Wi-Fi 扫描 API，仅特殊用途路径（entitlement/MFi 门槛）。另 3 篇冻结来源与本节点无关。均 low 初判，版本基线未核实。 |
| 设备与系统资源 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 音频路由 | rollup | pending | 未评估 | 尚未取得合格初判 |
| [音频输出路由](reports/device.audio_route.output/report.md) | leaf | delivered | P1 | 三平台均读到输出路由机制：Android 为系统输出切换器+AndroidX MediaRouter（选择）与 getRoutedDevice()/OnRoutingChangedListener（查询监听，TV 指南）；iOS 仅读到无版本标注的 AudioToolbox 旧常量（听筒/扬声器覆盖与路由类型枚举）；HarmonyOS 为 AudioRoutingManager 查询监听加 API 20 AudioSessionManager 默认设备设置与含变更原因事件。首轮初判置信度全 low；缺口：iOS 现代 AVAudioSession、Android 手机场景选择 API、HarmonyOS 发行版对应与权限。 |
| 显示 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 亮度控制 | leaf | running | 未评估 | 尚未取得合格初判 |
| 电量 | rollup | pending | 未评估 | 尚未取得合格初判 |
| [电池状态](reports/device.power.battery/report.md) | leaf | delivered | P1 | Android 训练文档给出机制：BatteryManager 粘性广播查询电量/充电状态，清单 receiver 监听 POWER_CONNECTED/DISCONNECTED，Android 8.0 起禁止持续监听电量并推荐 WorkManager 约束；HarmonyOS @ohos.batteryInfo（API 6+）同步查询电量/充电/充电器类型，workScheduler（API 9+）支持电量条件触发；iOS 冻结来源仅 MDM/HIDDriverKit 内容，应用级电池 API 缺失，保留 unknown。全部 low 置信。 |
| 分布式与多端 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 任务接续 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 跨设备接续 | leaf | running | 未评估 | 尚未取得合格初判 |
| 附近设备 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 附近发现 | leaf | running | 未评估 | 尚未取得合格初判 |
| 跨设备通信 | rollup | pending | 未评估 | 尚未取得合格初判 |
| [跨设备调用与数据传输](reports/distributed.softbus.fabric/report.md) | leaf | delivered | P1 | 三平台文档初判：Android 读到 Cross device SDK（Developer Preview，经 Google Play Services Beta 分发，需开启 Quick Share），提供设备发现、加密双向数据共享与多设备会话，但连接中断处理与远端能力调用语义未读到；HarmonyOS 仅读到分布式设备管理基座（发现/认证/状态监听，API 10+，需 DISTRIBUTED_DATASYNC 权限），远端调用与数据传输本体 API 缺失；iOS 两篇冻结来源均不相关，无判断依据。差异假设聚焦交付形态与权限模型。全部 low 置信，未实测。 |
| 企业与管理 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 设备管理 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 管理策略 | leaf | running | 未评估 | 尚未取得合格初判 |
| 工作资料 | rollup | pending | 未评估 | 尚未取得合格初判 |
| [工作数据隔离](reports/enterprise.work_profile.isolation/report.md) | leaf | delivered | P1 | 本节点定义为企业工作应用与数据容器隔离。冻结的6篇来源经通读均为关键词误匹配：Android 两篇为 Firebase Firestore 事务隔离与开发环境隔离；iOS 两篇为 Swift Testing 框架 actor isolation 参数；HarmonyOS 两篇为病毒文件隔离处置与应用内状态管理FAQ，均不涉及工作资料容器隔离。三平台本轮均 unknown，无差异假设。缺口：需从官方入口补查 Android Work Profiles、Apple User Enrollment/托管应用、HarmonyOS 企业管理/MDM 正文并固定版本基线。 |
| 图形与渲染 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 二维绘制 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 画布绘制 | leaf | running | 未评估 | 尚未取得合格初判 |
| 三维与GPU | rollup | pending | 未评估 | 尚未取得合格初判 |
| 现代GPU图形API | leaf | running | 未评估 | 尚未取得合格初判 |
| 截屏与录屏 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 屏幕录制 | leaf | running | 未评估 | 尚未取得合格初判 |
| 截屏 | leaf | running | 未评估 | 尚未取得合格初判 |
| 健康运动家居车 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 车载投影 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 车机应用投影 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 健康数据 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 健康记录 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 智能家居 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 家居配件控制 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 身份与账号 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 联邦登录 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 平台账号登录 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 系统账号 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 账号管理 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 输入与文本 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 剪贴板 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 剪贴板读写 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 拖放 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 跨应用拖放 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 输入法 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 输入法框架 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 触控与手势 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 手势识别 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 跨应用协作 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 跨应用动作分发 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 目标组件调用 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 系统意图注册 | leaf | pending | 未评估 | 尚未取得合格初判 |
| URL拉起应用 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 深度链接 | rollup | pending | 未评估 | 尚未取得合格初判 |
| URL深度链接 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 系统分享 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 分享面板 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 位置与地理 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 地理围栏 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 区域围栏 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 地图展示 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 地图SDK | leaf | pending | 未评估 | 尚未取得合格初判 |
| 定位 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 后台定位 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 前台定位 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 媒体 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 媒体采集 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 相机捕获管线 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 麦克风录音 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 编解码 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 硬件编解码 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 媒体库 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 系统媒体选择器 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 媒体播放 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 音频播放 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 视频播放 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 网络 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 热点与网络共享 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 本地热点 | leaf | pending | 未评估 | 尚未取得合格初判 |
| HTTP客户端 | rollup | pending | 未评估 | 尚未取得合格初判 |
| HTTP请求 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 套接字 | rollup | pending | 未评估 | 尚未取得合格初判 |
| TCP与UDP | leaf | pending | 未评估 | 尚未取得合格初判 |
| VPN | rollup | pending | 未评估 | 尚未取得合格初判 |
| 应用VPN扩展 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 通知与推送 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 本地通知 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 通知操作按钮 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 通知展示 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 远程推送通道 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 推送通道 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 可观测与质量 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 崩溃与ANR | rollup | pending | 未评估 | 尚未取得合格初判 |
| 崩溃报告 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 日志 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 应用日志 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 性能追踪 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 性能Trace | leaf | pending | 未评估 | 尚未取得合格初判 |
| 运行时与国际化 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 并发模型 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 异步任务调度与协作 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 国际化 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 语言区域 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 安全与隐私 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 生物识别 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 本地生物认证 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 密钥与密码学 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 硬件支持密钥库 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 权限模型 | rollup | pending | 未评估 | 尚未取得合格初判 |
| [运行时权限请求](reports/security.permissions.runtime/report.md) | leaf | delivered | P1 | 三平台均读到运行时向用户请求敏感权限的机制。Android 指南明示 API 23+ 设备上运行时权限须应用自行请求且先在 manifest 声明；iOS 由系统在首次访问受保护资源时弹窗，需 Info.plist 用途字符串，各框架提供 requestAuthorization 类 API；HarmonyOS 经 AtManager.requestPermissionsFromUser(API 9+，Stage 模型)拉起动态授权弹窗，拒绝后不可再弹。Android 实际请求 API 未在冻结来源中，iOS 版本适用性、HarmonyOS API 与发行版映射未核实，全部 low。 |
| 特殊权限与设置页 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 安全存储 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 凭据安全存储 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 传感器与运动 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 环境传感器 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 环境读数 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 运动传感器 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 加速度与陀螺仪 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 数据与存储 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 云端同步存储 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 云记录同步 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 结构化存储 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 关系数据库 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 键值存储 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 偏好键值 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 应用沙箱文件 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 私有文件读写 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 用户文件访问 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 文档选择器 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 通信与内容 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 日历 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 日历事件 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 联系人 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 读取联系人 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 电话 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 发起通话 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 短信 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 发送短信 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 界面与窗口 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 控件类别 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 按钮 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 弹层对话框 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 图像视图 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 列表 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 导航栏 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 文本输入框 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 声明式UI框架 | rollup | pending | 未评估 | 尚未取得合格初判 |
| [状态驱动界面更新](reports/ui.declarative.vs_imperative/report.md) | leaf | delivered | P1 | 三平台均读到声明式状态驱动UI的官方描述：HarmonyOS最直接（ArkTS声明式：声明UI结构与状态，自动驱动界面渲染）；Android证据来自Wear迁移文（状态驱动+recomposition）与compose.ui实验性接口的快照失效说明，手机范围核心状态文档未读；iOS仅SwiftUI/UIKit框架页概述（模型到视图数据流、事件驱动命令式对照），细节正文未读。命令式路径（UIKit、ArkUI NDK/类Web；Android View缺证）与更新范围粒度均待补。版本均未核实，置信度全low。 |
| 命令式视图系统 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 导航栈 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 页面导航栈 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 主题与外观 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 深色模式 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 窗口与多窗 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 分屏与多窗 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 画中画 | leaf | pending | 未评估 | 尚未取得合格初判 |
| Web与混合 | rollup | pending | 未评估 | 尚未取得合格初判 |
| JS桥接 | rollup | pending | 未评估 | 尚未取得合格初判 |
| 原生与JS互调 | leaf | pending | 未评估 | 尚未取得合格初判 |
| 嵌入式Web视图 | rollup | pending | 未评估 | 尚未取得合格初判 |
| WebView嵌入 | leaf | pending | 未评估 | 尚未取得合格初判 |

来源、版本限制、差异假设、真机需求和具体缺口见各节点报告及 index.json。
后续内容抽查单独记录，自动检查通过不代表抽查通过；费用不可观测，不以reported_cost=0宣称免费。
