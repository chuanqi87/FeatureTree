# NFC读写 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

三平台均直接文档化 NFC 标签读写：Android 概述明示 Reader/writer mode（读写无源标签/贴纸，框架以 NDEF 为核心）；iOS Core NFC 明示读取 NDEF（类型1–5）并向可写标签写入，经 reader session 类完成；HarmonyOS 指南给出前台/后台读写流程、tag 模块技术对象（API 9+）与 ohos.permission.NFC_TAG。差异假设集中于发现/分发模型、权限声明方式与发现前置条件（HarmonyOS 需亮屏解锁、iOS 有免应用后台读取入口）。Android 仅概述级正文、Apple 版本适用性未核、HarmonyOS tag API 参考未读；全部 low 置信，真机均判 required。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | documented_mechanism | direct | 官方概述明示 Android NFC 设备支持 Reader/writer mode：读取和写入无源 NFC 标签与贴纸；简单标签提供读写语义，框架 API 以 NDEF 为核心；Advanced NFC 概述说明可检测标签技术并以自有协议栈按原始字节读写。HCE 文档（卡模拟范围）旁证 Android NFC 设备可作为读取器并使用 IsoDep 类。 | required |
| ios | documented_mechanism | direct | Core NFC 官方页明示：可检测 NFC 标签、读取含 NDEF 数据的消息并向可写标签写入数据；支持 NDEF 类型 1–5，并可与 ISO 7816、ISO 15693、FeliCa、MIFARE 等协议标签交互；读写经 NFCNDEFReaderSession/NFCTagReaderSession 等会话类进行。NFCReaderError 列出标签不可写、写入失败、transceive 等错误，佐证读写与通信机制。 | required |
| harmonyos | documented_mechanism | direct | HarmonyOS 官方指南明示前台/后台 NFC 标签读写：经 tag 模块按技术类型（NfcA/NfcB/NfcF/NfcV/IsoDep/NDEF/MifareClassic/MifareUltralight，API 9 起）获取标签对象，connect/transmit 完成读写；前台动态注册、后台 module.json5 静态声明；权限 ohos.permission.NFC_TAG；发现前提为亮屏且解锁。@ohos.nfc.controller（API 7 起）仅管理 NFC 开关状态。 | required |

## android 条件与证据

适用范围：developer.android.com 当前指南快照（2026-09-05 抓取）；概述正文未标注具体 API Level（HCE 文档提及 Android 4.4+，但属卡模拟范围）；未固定启动日最新正式版基线。
条件：需要具备 NFC 硬件的 Android 设备，连接通常要求 4 cm 以内（概述正文）；框架 API 围绕 NDEF（NFC Forum 标准）构建；非 NDEF 或无法完全解析的数据需用自有协议栈按原始字节读写（Advanced NFC 概述）；HCE 文档表明 Android NFC 设备可作为读取器使用 IsoDep 类（属卡模拟文档的旁证）；权限要求、前台分发与后台 dispatch 条件未在本轮正文出现
缺口：NFC Basics 与 Advanced NFC 正文未纳入冻结来源：NDEF 读写 API、TagTechnology 类、foreground dispatch、权限声明（如 android.permission.NFC）未核实；未核对具体 API Level 与设备条件（Android 系统 SDK 版本适用性）；HCE 文档主体属卡模拟（connectivity.nfc 其他子节点范围），对读写节点仅有间接旁证；锁屏/息屏状态下标签发现行为未在正文出现
真机分类理由：读写 NFC 标签依赖设备 NFC 硬件与实体标签交互，模拟器无法完整复现；权限提示、前台分发与各标签技术实际读写行为需真机验证后方可正式确认。本轮仅分类未设计用例。

- [Near field communication (NFC) overview](https://developer.android.com/develop/connectivity/nfc)，Reader/writer mode 与 Card emulation mode 两种工作模式，正文 18–25 行；获取 2026-09-05T10:24:19.626460+00:00；SHA f7538bc876e9d656e04244f0728c4c2612c60f9f402a3310c20d4f6db61e1f82。
- [Near field communication (NFC) overview](https://developer.android.com/develop/connectivity/nfc)，标签读写语义与 NDEF 框架 API 基础，正文 8–16 行；获取 2026-09-05T10:24:19.626460+00:00；SHA f7538bc876e9d656e04244f0728c4c2612c60f9f402a3310c20d4f6db61e1f82。
- [Near field communication (NFC) overview](https://developer.android.com/develop/connectivity/nfc)，Advanced NFC：非 NDEF 数据按原始字节手动读写，正文 34–41 行；获取 2026-09-05T10:24:19.626460+00:00；SHA f7538bc876e9d656e04244f0728c4c2612c60f9f402a3310c20d4f6db61e1f82。
- [Host-based card emulation overview](https://developer.android.com/develop/connectivity/nfc/hce)，Android NFC 设备可作为读取器（IsoDep 类），正文 48–54 行；获取 2026-09-05T10:24:20.246506+00:00；SHA a27119a157caf10013a32f153086d69c0317c089c8135172a61c294161e7148a。

## ios 条件与证据

适用范围：Apple 开发者文档快照（© 2026，2026-09-05 抓取）；页面无 iOS 版本 availability 元数据，Core NFC 最低 iOS 版本与写标签设备条件未核实；Apple 目录含多操作系统，iOS 适用性需逐符号核对。
条件：Core NFC 不适用于 app extensions；需要支持 NFC 的设备；开始 reader session 前应检查 readingAvailable；可读 NDEF 类型 1–5 标签并可向可写标签写入；可与 ISO 7816、ISO 15693、FeliCa、MIFARE 协议标签交互；引用 entitlement com.apple.developer.nfc.readersession.formats 与 Info.plist NFCReaderUsageDescription（本轮仅目录引用，正文未读）
缺口：iOS 版本适用性未核实：页面无 availability 元数据，Core NFC 最低 iOS 版本、写标签所需设备/系统条件未确认；entitlement 与 NFCReaderUsageDescription 具体要求仅有目录引用，正文未读；后台标签读取（Background Tag Reading）正文未读，触发条件与适用设备范围未知；写标签 API（NFCNDEFTag 写入方法）与协议标签交互细节未读正文
真机分类理由：正文明示 Core NFC 需要支持 NFC 的设备且不可用于 app extensions；会话生命周期、entitlement 生效与实际读写行为需真机加实体标签验证；模拟器路径未在本轮证据中出现。本轮仅分类未设计用例。

- [Core NFC](https://developer.apple.com/documentation/corenfc)，Core NFC 概述：读取 NDEF（类型1–5）、写入可写标签、设备与 app extension 条件，正文 5–11 行；获取 2026-09-05T10:30:09.525759+00:00；SHA 80e2fb994de51be7ef40ef661ca38810b3662d938b052db6953dad2150cd92c7。
- [Core NFC](https://developer.apple.com/documentation/corenfc)，Reader sessions：NFCNDEFReaderSession/NFCTagReaderSession 等，正文 27–37 行；获取 2026-09-05T10:30:09.525759+00:00；SHA 80e2fb994de51be7ef40ef661ca38810b3662d938b052db6953dad2150cd92c7。
- [Core NFC](https://developer.apple.com/documentation/corenfc)，Tag types：读写标签数据与 Creating NFC Tags from Your iPhone，正文 61–67 行；获取 2026-09-05T10:30:09.525759+00:00；SHA 80e2fb994de51be7ef40ef661ca38810b3662d938b052db6953dad2150cd92c7。
- [NFCReaderError](https://developer.apple.com/documentation/corenfc/nfcreadererror-swift.struct)，NDEF Tag Errors：tagNotWritable/tagSizeTooSmall/tagUpdateFailure，正文 33–49 行；获取 2026-09-05T10:46:59.963451+00:00；SHA d2b85fc4526b5c0e42508372148bd5e623512d79db8784241ec6e9ae09a02ca3。

## harmonyos 条件与证据

适用范围：华为 HarmonyOS 官方 guides/references 快照（2026-09-04/05 抓取）；tag 读写接口标注从 API version 9 起支持，nfcController 首批 API 7（isNfcSupported 为 API 26 起）；具体 HarmonyOS 发行版与手机基线未固定。
条件：发现 NFC 标签的前提是设备亮屏且解锁（指南明示）；前台读写须经 tag.registerForegroundDispatch 或 tag.on('readerMode') 动态注册并指定技术类型；页面退后台需显式注销；后台读写需在 module.json5 静态声明 TAG_FOUND action、tag-tech/ 技术类型与 ohos.permission.NFC_TAG 权限；Wearable 设备不支持后台读卡；NFC 开关控制接口仅系统应用可调用（ohos.permission.MANAGE_SECURE_SETTINGS）；普通应用可查询状态
缺口：@ohos.nfc.tag (js-apis-nfctag) API 参考正文未读：读写接口签名、错误码、NDEF 写入方法未核实；具体 HarmonyOS 发行版（API 9/26 对应的手机版本）未固定，映射待核；平板（tablet）形态适用性与元服务条件未核对；OpenHarmony 与 HarmonyOS 发行版差异未核对
真机分类理由：指南明示通过设备 NFC 天线触碰标签完成读写，且约束亮屏解锁；实际前后台分发、权限生效与各技术类型读写行为需真机加标签验证；Wearable 约束亦需设备核对。本轮仅分类未设计用例。

- [NFC标签读写开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nfc-tag-access-guide)，场景介绍：NFC 标签前台读写与后台读写，正文 20–27 行；获取 2026-09-04T09:35:09+00:00；SHA 2a19e07427e200c0fe0a23ffe491542f9f87e859012a1b2d0f4566940bb48e58。
- [NFC标签读写开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nfc-tag-access-guide)，标签读写约束：亮屏且解锁，正文 35–37 行；获取 2026-09-04T09:35:09+00:00；SHA 2a19e07427e200c0fe0a23ffe491542f9f87e859012a1b2d0f4566940bb48e58。
- [NFC标签读写开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nfc-tag-access-guide)，getNfcA…getMifareUltralight 接口表（从 API version 9 起支持），正文 45–54 行；获取 2026-09-04T09:35:09+00:00；SHA 2a19e07427e200c0fe0a23ffe491542f9f87e859012a1b2d0f4566940bb48e58。
- [NFC标签读写开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nfc-tag-access-guide)，前台读写动态注册与注销（registerForegroundDispatch/tag.on），正文 62–67 行；获取 2026-09-04T09:35:09+00:00；SHA 2a19e07427e200c0fe0a23ffe491542f9f87e859012a1b2d0f4566940bb48e58。
- [NFC标签读写开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nfc-tag-access-guide)，requestPermissions 声明 ohos.permission.NFC_TAG，正文 120–126 行；获取 2026-09-04T09:35:09+00:00；SHA 2a19e07427e200c0fe0a23ffe491542f9f87e859012a1b2d0f4566940bb48e58。
- [@ohos.nfc.controller (标准NFC)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-nfccontroller)，@ohos.nfc.controller 模块职责：NFC 状态管理（首批接口 API 7），正文 1–5 行；获取 2026-09-05T10:27:44.541030+00:00；SHA aa3f2bb90f16503633bd09c4fb917909413caa3ebd42158ef920e3a0710a28ee。

## 待验证差异假设

- programming_model：标签发现与应用接收模型可能不同：iOS 经 NFCNDEFReaderSession/NFCTagReaderSession 等显式会话类扫描检测标签；HarmonyOS 前台经 tag.registerForegroundDispatch/tag.on('readerMode') 动态注册、后台经 module.json5 静态声明技术类型由系统分发；Android 概述称由系统处理发现的标签并通知相关应用，具体 intent/前台分发机制未在本轮正文核实。；待核：Android NFC Basics 正文（intent filter、foreground dispatch、Beam）未读，分发细节为概述级推断；iOS 会话生命周期、并发会话限制与后台触发细节未读正文；HarmonyOS registerForegroundDispatch 与 tag.on 在卡模拟互斥上的差异仅有指南一句话描述，API 参考未核。
- permissions_privacy：权限与声明机制可能不同：HarmonyOS 要求 module.json5 声明 ohos.permission.NFC_TAG 权限、TAG_FOUND action 及 tag-tech/ 技术类型；iOS 依赖 entitlement（com.apple.developer.nfc.readersession.formats）与 NFCReaderUsageDescription 用途字符串，二者声明位置与形态不同（iOS 依据本轮仅为目录引用，正文未读）。；待核：iOS entitlement 正文与配置流程未读，不能断言与 HarmonyOS 权限模型的完整差异；Android NFC 权限要求未在冻结来源出现，三平台完整比较待补；ohos.permission.NFC_TAG 的授权级别（安装时/运行时）未核实。
- lifecycle_background：标签发现的前置条件与后台能力可能不同：HarmonyOS 明示发现标签需设备亮屏且解锁，且 Wearable 不支持后台读卡；iOS 提供无需打开应用的后台标签读取（Background Tag Reading）能力入口；Android 在锁屏/息屏下的标签发现行为未在本轮正文出现。；待核：iOS 后台读取的适用设备、系统版本与触发条件未读正文；Android 屏幕状态与标签发现关系未核实；HarmonyOS 亮屏解锁约束在不同设备形态上的表现未核对。

范围缺口：Android 仅读到概述级正文：NFC Basics/Advanced NFC、NFC 权限与前台分发 API 未纳入冻结来源，读写具体 API 与条件未核实；Apple 符号级 availability 未核对：Core NFC 最低 iOS 版本、写标签设备条件、iPad 适用性未确认；HarmonyOS @ohos.nfc.tag API 参考正文未读：接口签名、错误码、NDEF 写入方法与元服务条件未核实；三平台启动日最新正式版与手机基线未固定，本轮仅基于 2026-09-04/05 文档快照初判；HCE/卡模拟与安全元件属 connectivity.nfc 其他子节点范围，本轮未比较也未据此推断读写能力

后续优先级：P1；三平台读写机制均已直接文档化，但构成比较核心的分发模型、权限声明与后台行为差异所依赖的正文（Android NFC Basics/Advanced NFC、iOS entitlement 与符号级 availability、@ohos.nfc.tag API 参考）均未读，存在以概述推断具体行为的高风险映射，属关键缺口。

逐条引用及原文摘录见同目录 normalized.json。
