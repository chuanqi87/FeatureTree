# 工作数据隔离 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

本节点定义为企业工作应用与数据容器隔离。冻结的6篇来源经通读均为关键词误匹配：Android 两篇为 Firebase Firestore 事务隔离与开发环境隔离；iOS 两篇为 Swift Testing 框架 actor isolation 参数；HarmonyOS 两篇为病毒文件隔离处置与应用内状态管理FAQ，均不涉及工作资料容器隔离。三平台本轮均 unknown，无差异假设。缺口：需从官方入口补查 Android Work Profiles、Apple User Enrollment/托管应用、HarmonyOS 企业管理/MDM 正文并固定版本基线。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | unknown | missing | 两篇冻结正文分别描述 Cloud Firestore 事务串行化/数据争用隔离与 Firebase 项目开发/预发/生产环境隔离，属 Google 云服务与开发流程主题，不涉及 Android 工作资料（Work Profile）应用与数据容器隔离；未读到 DevicePolicyManager 等企业管理机制正文。 | unassessed |
| ios | unknown | missing | 两篇冻结正文为 Swift Testing 框架 confirmation(_:expectedCount:isolation:sourceLocation:_:) API 参考，其中 isolation 参数指 Swift 并发的 actor 隔离，与本节点企业工作数据容器隔离无关；未读到 User Enrollment、Managed App Configuration 等 Apple 企业管理正文。 | unassessed |
| harmonyos | unknown | missing | 冻结两篇：virusRemediation（起始6.1.1(24)）为安全防护类应用提供威胁文件扫描与文件隔离/恢复/删除、终止进程，属病毒处置而非工作数据容器；另一篇为应用内状态管理FAQ（装饰器使用隔离）。未读到华为企业设备管理/工作空间/应用分身类正文。 | unassessed |

## android 条件与证据

适用范围：冻结来源为 Firebase 云服务文档（抓取2026-09-05，version_verified=false），无 Android API Level 信息；任务版本基线 unresolved，无法判定系统版本适用性。
条件：仅通读冻结的 android-1/android-2 两篇 Firebase 正文，未覆盖 Android 系统 SDK 或 AndroidX 企业管理主题；来源快照仅验完整性，版本与适用性未核实；本轮不联网补查，未读取 Work Profiles 官方指南正文
缺口：缺 Android Work Profiles/managed profile 官方指南与 API 正文（创建、资料容器隔离、badge、暂停/删除生命周期）；缺 DevicePolicyManager 及工作资料相关 API 的 API Level 版本与设备条件；Firebase 生态服务文档不证明系统级工作数据隔离行为，需系统 SDK 证据
真机分类理由：未建立任何工作数据隔离机制证据，无从设计真机验证项；须先补齐官方文档与版本基线再评估。

- [Transaction serializability and isolation](https://firebase.google.com/docs/firestore/transaction-data-contention)，标题与导语：本页描述事务数据争用、串行化与隔离，属数据库事务主题，正文 1–5 行；获取 2026-09-05T11:17:05.434742+00:00；SHA de359e41484f44f60f5ba7cdabaed930b7f51fcea6b15767b139e85f9049a39e。
- [Overview of environments](https://firebase.google.com/docs/projects/dev-workflows/overview-environments)，About environments：环境隔离指开发/测试/生产工作流隔离，建议每环境使用独立 Firebase 项目，正文 21–32 行；获取 2026-09-05T11:07:38.261464+00:00；SHA 7e3c43b2d8e81037c8131defd78d7581faeb962e1fc8e58407f83d45667d0cdb。

## ios 条件与证据

适用范围：冻结来源为 Swift Testing API 页面（抓取2026-09-05，version_verified=false），页面未标注 iOS 最低适用版本；任务版本基线 unresolved，无法判定 iOS 版本适用性。
条件：仅通读冻结的 ios-1/ios-2 两篇 Swift Testing API 正文，未覆盖 Apple 企业管理/MDM 主题；来源快照仅验完整性，iOS 适用性与版本未核实；本轮不联网补查，未读取 User Enrollment/托管应用官方正文
缺口：缺 Apple 企业数据分离官方正文（User Enrollment、Managed App Configuration、工作/个人数据分离机制）；缺所涉框架符号的 iOS availability 与最低版本核对；Apple 目录含 macOS 等多平台，需逐符号确认 iOS 适用性
真机分类理由：未建立任何工作数据隔离机制证据，无从设计真机验证项；须先补齐 Apple 企业管理官方文档与 iOS 版本核对。

- [confirmation(_:expectedCount:isolation:sourceLocation:_:)](https://developer.apple.com/documentation/testing/confirmation(_:expectedcount:isolation:sourcelocation:_:)-l3il)，标题与函数签名：Swift Testing confirmation API，用于确认测试期间事件发生，正文 1–7 行；获取 2026-09-05T11:19:31.938603+00:00；SHA feeb2531c9062ea9dad86a5c04162a4aed01fca49202403c2936d93998a5f911。
- [confirmation(_:expectedCount:isolation:sourceLocation:_:)](https://developer.apple.com/documentation/testing/confirmation(_:expectedcount:isolation:sourcelocation:_:)-5mqz2)，isolation 参数说明：body 所隔离到的 actor，属 Swift 并发 actor 隔离，正文 23–25 行；获取 2026-09-05T11:19:31.699091+00:00；SHA 044565e5685d918819337fc44d4a32f134698654e6957e71f661e57ad70be16d。

## harmonyos 条件与证据

适用范围：virusRemediation 起始版本 6.1.1(24)，约束 Stage 模型与 SystemCapability.PCService.VirusRemediation（抓取2026-09-05，version_verified=false）；该版本信息属病毒处置接口，与工作数据隔离无关；任务基线 unresolved。
条件：仅通读冻结的 harmonyos-1/harmonyos-2 两篇正文，未覆盖华为企业管理/MDM/工作空间主题；virusRemediation 面向安全防护类应用并需申请权限，与本节点工作资料容器范围不同；本轮不联网补查，未读取 HarmonyOS 企业管理指南正文
缺口：缺 HarmonyOS 企业场景下工作应用与数据容器隔离的官方正文（企业设备管理/MDM/应用隔离类 Kit 或指南）；需区分 HarmonyOS 商业发行版与 OpenHarmony 的企业能力；缺手机/平板设备形态与系统版本条件下的适用性证据
真机分类理由：未建立任何工作数据隔离机制证据，无从设计真机验证项；须先补齐华为官方企业管理文档与版本基线。

- [virusRemediation（病毒检测与处置）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/enterprisethreatprotection-virusremediation-interface)，标题与导语：病毒检测与处置提供威胁文件隔离等能力，需安全防护类应用申请权限；起始版本6.1.1(24)，正文 1–5 行；获取 2026-09-05T10:26:11.118183+00:00；SHA 1b6df2ff9df90d6c401b397b17f8803f34b5337e59bb9627710f63659348c08e。
- [应用内状态管理和其他常见问题](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-faq-application-and-others)，标题与导语：应用内状态管理常见问题，正文 1–3 行；获取 2026-09-04T09:35:09+00:00；SHA 4cb63b0ee4d40e857f3afd4751f2b0b9542ff24c600977d6d40d6bee033bd17d。

## 待验证差异假设

没有形成满足双方引用要求的差异假设；不代表没有差异。

范围缺口：三平台冻结来源全部为关键词误匹配（事务隔离/环境隔离/actor isolation/病毒文件隔离/装饰器隔离），无一涉及工作应用与数据容器隔离；Android：缺 Work Profiles/managed profile 指南与 DevicePolicyManager API 正文及 API Level 条件；iOS：缺 User Enrollment/Managed App Configuration 等企业数据分离正文及 iOS availability 核对；HarmonyOS：缺企业设备管理/MDM/工作空间类正文，需区分 HarmonyOS 与 OpenHarmony 发行版；版本基线 unresolved，三平台最新正式版与手机基线未固定，无法判定当前版本支持情况

后续优先级：P1；三平台均无相关冻结来源，全部候选为关键词误匹配，本节点首轮完全 unknown，且存在把 Firebase 事务隔离、Swift actor isolation、病毒文件隔离误映射为企业工作数据隔离的高风险；须优先从官方入口重新检索三平台企业工作资料容器隔离主题。

逐条引用及原文摘录见同目录 normalized.json。
