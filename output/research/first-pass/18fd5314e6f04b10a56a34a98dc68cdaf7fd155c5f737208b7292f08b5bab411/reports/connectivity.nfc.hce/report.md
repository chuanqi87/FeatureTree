# 主机卡模拟 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

三平台均读到 HCE 官方机制:Android 4.4+ HostApduService 开放给任意应用;iOS 17.4+ CardSession 限 EEA 授权开发者(仅更新页,未见 API 正文);HarmonyOS cardEmulation 首批 API 6/HceService API 8+ 提供且明确禁灭屏。差异假设:准入与区域限制、灭屏行为、AID 注册与默认应用模型。置信全 low,启动日基线未固定。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | documented_mechanism | direct | Android 4.4+ 任意应用可经 HostApduService 实现 HCE,按 AID 路由应答读卡器 APDU;AID 组分 PAYMENT/OTHER 两类,支持前台优先、默认钱包角色与 Observe Mode(Android 15+),灭屏/锁屏行为分版本。 | required |
| ios | documented_mechanism | indirect | iOS 17.4 起 CoreNFC CardSession 支持 EEA 内应用 HCE 非接触交易,授权开发者可经 entitlement 被用户选为默认处理者;iOS 18.1 另有基于安全元素的 SecureElementCredential 凭证卡模拟(非 HCE)。 | required |
| harmonyos | documented_mechanism | direct | @ohos.nfc.cardEmulation(首批 API 6)提供 HceService(API 8+):start/stop 动态 AID+前台优先、on('hceCmd') 收 APDU、transmit 应答;后台刷卡需静态声明 payment-aid/other-aid;明确不支持灭屏刷卡;OFFHOST 自 API 22 仅 SIM。 | required |

## android 条件与证据

适用范围：指南陈述 Android 4.4(API 19)+ 支持 HCE,分版本行为涉及 Android 9/10/12/15(API 28/29/31/35);快照未标注适用上限,启动日最新正式版未核实。
条件：设备需具备 NFC 与 FEATURE_NFC_HOST_CARD_EMULATION 特性；服务需 manifest 声明 HOST_APDU_SERVICE、BIND_NFC_SERVICE、NFC 权限及 apduservice.xml 静态 AID 组；CATEGORY_PAYMENT 交易需为默认支付应用(Android 15+ 为钱包角色持有者)或前台调用 setPreferredService；灭屏/锁屏可用性随 Android 版本、Secure NFC 与 requireDeviceScreenOn/requireDeviceUnlock 设置变化；仅支持 ISO-DEP(ISO 14443-4)/ISO 7816-4 APDU,Nfc-A 强制、Nfc-B 可选,且仅单逻辑通道
缺口：未读 HostApduService/CardEmulation 等 API 参考正文,接口签名与逐项 API Level 标注未核实；Observe Mode、polling loop filter 的设备硬件与厂商支持条件未说明；android-2 与 android-1 正文相同,无增量信息;启动日最新正式版行为未核实；Secure NFC 与 requireDeviceScreenOn=false 在具体机型上的实际行为未验证
真机分类理由：HCE 依赖 NFC 控制器路由、灭屏功耗策略、Secure NFC 与默认钱包角色等系统行为,静态文档无法验证实际读卡器交互、厂商差异与各版本实际表现,最终确认需真机。

- [Host-based card emulation overview](https://developer.android.com/develop/connectivity/nfc/hce)，Host-based card emulation overview > Host-based card emulation(Android 4.4+ 定义)，正文 8–13 行；获取 2026-09-05T10:24:20.246506+00:00；SHA a27119a157caf10013a32f153086d69c0317c089c8135172a61c294161e7148a。
- [Host-based card emulation overview](https://developer.android.com/develop/connectivity/nfc/hce)，Host-based card emulation overview > Supported NFC cards and protocols，正文 56–62 行；获取 2026-09-05T10:24:20.246506+00:00；SHA a27119a157caf10013a32f153086d69c0317c089c8135172a61c294161e7148a。
- [Host-based card emulation overview](https://developer.android.com/develop/connectivity/nfc/hce)，Host-based card emulation overview > HCE services(基于 Service 后台运行)，正文 64–74 行；获取 2026-09-05T10:24:20.246506+00:00；SHA a27119a157caf10013a32f153086d69c0317c089c8135172a61c294161e7148a。
- [Host-based card emulation overview](https://developer.android.com/develop/connectivity/nfc/hce)，Host-based card emulation overview > AID groups and categories 及 CATEGORY_PAYMENT 交易条件，正文 109–141 行；获取 2026-09-05T10:24:20.246506+00:00；SHA a27119a157caf10013a32f153086d69c0317c089c8135172a61c294161e7148a。
- [Host-based card emulation overview](https://developer.android.com/develop/connectivity/nfc/hce)，Host-based card emulation overview > Service manifest declaration and AID registration，正文 246–316 行；获取 2026-09-05T10:24:20.246506+00:00；SHA a27119a157caf10013a32f153086d69c0317c089c8135172a61c294161e7148a。
- [Host-based card emulation overview](https://developer.android.com/develop/connectivity/nfc/hce)，Host-based card emulation overview > Screen off and lock-screen behavior，正文 460–521 行；获取 2026-09-05T10:24:20.246506+00:00；SHA a27119a157caf10013a32f153086d69c0317c089c8135172a61c294161e7148a。

## ios 条件与证据

适用范围：文档标注 HCE/CardSession 自 iOS 17.4、NFC & SE Platform 自 iOS 18.1;未核对符号级 availability 与 iPhone/iPad 型号适用性,启动日最新 iOS 版本未核实。
条件：HCE 交易限欧洲经济区(EEA)；面向授权开发者,需 managed entitlement com.apple.developer.nfc.hce.default-contactless-app 才能设为默认处理者；SecureElementCredential(非 HCE 路线)需经 Apple Business Register 管理凭证与 applet；SE 凭证卡模拟需会话进入 cardEmulation 状态并持有 PresentmentIntentAssertion
缺口：未读 CoreNFC/CardSession API 参考正文,会话生命周期、AID 处理、后台/灭屏约束未知；entitlement 授权申请条件与 EEA 限制的执行细则未读到原文；ios-2 为安全元素凭证机制(SE),非 HCE,仅作相邻机制参考,不能证明 iOS HCE 细节；iPhone/iPad 符号级 availability 与最新 iOS 版本适用性未核对
真机分类理由：iOS HCE 限 EEA 且依赖授权 entitlement 与真机 NFC 栈,CardSession 与 Wallet/SE 平台的共存、灭屏表现需真机验证;无授权环境只能静态分析。

- [Default apps updates](https://developer.apple.com/documentation/updates/defaultapps)，Default apps updates > HCE-based contactless transactions for apps(iOS 17.4、EEA、CardSession、entitlement)，正文 63–71 行；获取 2026-09-05T10:27:51.574171+00:00；SHA 7084606b591f82cd2420a8cead3fd4b5bb16a7ea9efa6cb8870ea6adac4138a7。
- [Default apps updates](https://developer.apple.com/documentation/updates/defaultapps)，Default apps updates > Contactless NFC and SE platform apps(iOS 18.1 NFC & SE Platform)，正文 53–61 行；获取 2026-09-05T10:27:51.574171+00:00；SHA 7084606b591f82cd2420a8cead3fd4b5bb16a7ea9efa6cb8870ea6adac4138a7。
- [Accessing and using secure element credentials](https://developer.apple.com/documentation/secureelementcredential/accessing-and-using-secure-element-credentials)，Accessing and using secure element credentials > 会话状态(management/wired/card emulation)，正文 51–61 行；获取 2026-09-05T10:25:33.920661+00:00；SHA 2eb41d0bb3c1df3be7e419de3e4bc5fceabb2849e4d3a35fdef6d320f7fcc301。
- [Accessing and using secure element credentials](https://developer.apple.com/documentation/secureelementcredential/accessing-and-using-secure-element-credentials)，Accessing and using secure element credentials > Perform card emulation(performTransaction/cardEmulation 状态)，正文 210–216 行；获取 2026-09-05T10:25:33.920661+00:00；SHA 2eb41d0bb3c1df3be7e419de3e4bc5fceabb2849e4d3a35fdef6d320f7fcc301。

## harmonyos 条件与证据

适用范围：模块首批 API 6;HceService/on API 8+,start/stop/transmit/hasHceCapability API 9+,off API 18+,OFFHOST API 22+;为 HarmonyOS 文档(非 OpenHarmony),对应发行版与手机系统版本未核实。
条件：设备需具备 NFC 控制器芯片;有无安全单元芯片无约束；需 ohos.permission.NFC_CARD_EMULATION 权限与 SystemCapability.Communication.NFC.CardEmulation 系统能力；前台刷卡经 start() 动态注册 AID;后台刷卡需 module.json5 静态 payment-aid/other-aid 声明；前台/后台均不支持灭屏或熄屏状态下的 HCE 刷卡；actions 必须包含 ohos.nfc.cardemulation.action.HOST_APDU_SERVICE,AID name 仅接受 payment-aid/other-aid
缺口：on('hceCmd')/transmit 的完整参数、错误码与元服务限制未逐行核对；轻量穿戴 FA 模型差异仅部分读取;平板等设备形态适用性未单独核对；HarmonyOS 发行版与 API 6/8/9/18/22 的手机版本对应关系未核实；Other 类型 AID 冲突的用户解决流程与钱包类应用共存细节未读到
真机分类理由：灭屏约束、AID 路由冲突、前台优先时序(hceService.on 需同步执行)等行为依赖真机 NFC 栈与实际读卡器交互验证,静态文档无法确认。

- [HCE卡模拟开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nfc-hce-guide)，HCE卡模拟开发指南 > 简介(HCE/OFFHOST 定义与起始版本)，正文 3–5 行；获取 2026-09-04T09:35:09+00:00；SHA 99087fdaf7a9d9c8a3d2822e34581c1dfa6274286fa2854d63658eae24332b2a。
- [HCE卡模拟开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nfc-hce-guide)，HCE卡模拟开发指南 > HCE应用刷卡的约束条件(灭屏不支持、NFC 控制器、权限)，正文 20–27 行；获取 2026-09-04T09:35:09+00:00；SHA 99087fdaf7a9d9c8a3d2822e34581c1dfa6274286fa2854d63658eae24332b2a。
- [HCE卡模拟开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nfc-hce-guide)，HCE卡模拟开发指南 > 接口说明(hasHceCapability/start/stop/on/transmit 及起始版本)，正文 34–42 行；获取 2026-09-04T09:35:09+00:00；SHA 99087fdaf7a9d9c8a3d2822e34581c1dfa6274286fa2854d63658eae24332b2a。
- [HCE卡模拟开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nfc-hce-guide)，HCE卡模拟开发指南 > HCE应用支持前台或后台刷卡的选择(动态/静态 AID、默认付款应用)，正文 46–63 行；获取 2026-09-04T09:35:09+00:00；SHA 99087fdaf7a9d9c8a3d2822e34581c1dfa6274286fa2854d63658eae24332b2a。
- [@ohos.nfc.cardEmulation (标准NFC-cardEmulation)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cardemulation)，@ohos.nfc.cardEmulation > 模块说明与首批 API version 6，正文 3–7 行；获取 2026-09-05T10:27:07.157700+00:00；SHA b907b05612a3f1b0aa47b517efcfdce5421acfbaf66adaac85b44de7c64cbcf0。
- [@ohos.nfc.cardEmulation (标准NFC-cardEmulation)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cardemulation)，@ohos.nfc.cardEmulation > HceService^8+^(APDU 收发实现)，正文 317–319 行；获取 2026-09-05T10:27:07.157700+00:00；SHA b907b05612a3f1b0aa47b517efcfdce5421acfbaf66adaac85b44de7c64cbcf0。

## 待验证差异假设

- availability：假设:HCE 准入与区域条件不同——Android 4.4+ 任意应用可实现;iOS 17.4+ 限 EEA 且需授权开发者与 managed entitlement;HarmonyOS 自 API 6/8 提供且所读文档未提区域或准入限制。；待核：iOS entitlement 授权条件与 EEA 之外是否完全不可用未读到原文；Android/HarmonyOS 是否存在未在这些文档说明的准入或区域限制；HarmonyOS API 版本与手机发行版对应关系未核实。
- lifecycle_background：假设:灭屏可用性不同——HarmonyOS 前台/后台均明确不支持灭屏刷卡;Android 分版本(Android 9- 不可用,10+ 受 Secure NFC 约束,12+ 可设 requireDeviceScreenOn=false 允许灭屏支付,15+ Observe Mode 可覆盖);iOS 灭屏行为未读到。；待核：iOS CardSession 灭屏/锁屏行为缺失,暂无法纳入三方比较；Android 12+ requireDeviceScreenOn=false 的设备实际支持范围与厂商差异未核实；HarmonyOS 灭屏约束是否随后续 API 版本变化未读到说明。
- programming_model：假设:AID 注册与默认应用模型不同——Android 以 manifest 静态 apduservice.xml AID 组+类别+前台 setPreferredService+钱包角色;HarmonyOS 以 module.json5 静态 payment-aid/other-aid+start() 动态 AID+系统默认付款应用;iOS 经 CardSession 会话与 default-contactless-app entitlement 由用户选默认,未见静态 AID 声明机制。；待核：iOS 是否存在静态 AID 声明机制及 CardSession 会话内 AID 选择方式未读到；三平台默认应用冲突解决规则的完整比较需 API 参考正文核实；HarmonyOS Other 类型 AID 冲突的用户交互细节仅部分描述。

范围缺口：本轮仅读概览指南/更新页,未读 HostApduService、CardEmulation、CardSession、NfcAdapter 等 API 参考正文；iOS HCE 证据来自默认应用更新页,CoreNFC 指南与 API 正文缺失,是最高风险映射；启动日最新正式版与手机基线未固定,各平台版本适用性均未核实；平板/iPad 与轻量穿戴等设备形态适用性未逐项核对；off-host/SE 卡模拟路线仅作相邻上下文,与 HCE 的完整对比不在本轮范围

后续优先级：P1；iOS HCE 仅凭更新页支撑且区域/授权限制属高风险映射,CardSession API 正文缺失;三平台灭屏行为与默认应用模型差异需 API 参考及真机核实,属关键缺口。

逐条引用及原文摘录见同目录 normalized.json。
