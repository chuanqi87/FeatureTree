# 应用安装更新 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

首轮文档初判：仅 Android 读到应用级安装/更新机制正文（Google Play EMM API Installs，update 可远程安装或把已装应用更新到最新版本，但方法已弃用且文档明示 2025-09-30 后不可访问）；iOS 两篇分别为 SKAdNetwork 广告归因安装验证与 MDM 系统软件更新强制；HarmonyOS 两篇为 ohpm 开发期依赖更新与 MDM OTA 固件更新，均非应用级机制。三平台应用级安装/更新文档缺口并存，基线未固定，全部 low。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | documented_mechanism | direct | Google Play EMM API v1 Installs 文档描述企业托管设备的应用安装/更新：创建 install 资源触发设备实际安装，对已有 install 调用 update 会更新到最新可用版本，不能指定版本（versionCode 只读）；get/list/update 均已弃用且文档明示 2025-09-30 后不可访问。另一篇为 Play services 安全 Provider 组件更新（ProviderInstaller），非完整应用安装。 | recommended |
| ios | possible_mapping | indirect | 两篇均非应用安装/更新机制正文：StoreKit 文档把『用户安装应用』作为广告归因时间窗事件并描述安装验证回传分层；DeviceManagement 文档描述系统软件更新强制的声明式阶段流程（声明同步、下载、准备、通知、安装、状态上报）。应用级安装/版本更新机制（如商店分发、MDM 应用安装命令）未见文档，仅存在待确认映射。 | recommended |
| harmonyos | unknown | missing | 两篇均不覆盖完整应用的安装与版本更新：ohpm update 是开发期更新工程三方库依赖的包管理器命令（semver 规则），非设备端应用安装；MDM Kit API diff 页新增的是企业 OTA 系统更新接口（OtaUpdatePolicy/UpdatePackageInfo/UpdateStatus，PackageType 为 FIRMWARE），属固件/系统更新。未能就本节点建立判断。 | unassessed |

## android 条件与证据

适用范围：Google Play EMM API v1（生态服务，非 Android 系统 SDK）；快照 2026-09-05 获取、version_verified=false；文档明示方法 2025-09-30 后不可访问（相对 2026-09-06 已过期）；未固定启动日最新正式版基线。
条件：企业/EMM 托管设备场景，经 Google Play 生态服务（非 Android 系统 SDK）；创建 install 需 entitlement；付费应用无可用许可证时创建失败；get/list/update 方法已弃用，文档明示 2025-09-30 后任何人不可访问；更新语义为更新到最新可用版本，不可强制指定 versionCode
缺口：未读 Android 系统 SDK 应用安装接口（如 PackageInstaller/安装 session）文档；未读消费侧应用自更新与 Play 应用内更新（in-app updates）文档；EMM 方法已过期，现行替代（如 Android Management API）未在本轮冻结来源中；版本基线未固定，未核对启动日最新正式版行为
真机分类理由：应用安装/更新是设备端可观察行为（安装状态迁移、更新到最新版本的实际效果），正式核实建议真机加 EMM/Play 环境实测；本轮仅文档初判，无实测。

- [Installs](https://developers.google.com/android/work/play/emm-api/v1/installs)，Resource representations：install 创建触发实际安装、update 更新到最新版本、versionCode 只读，正文 5–17 行；获取 2026-09-05T10:51:54.596982+00:00；SHA 49b37437faa701eecb2efdca840abd9069a09719db6124b0db6e38ddbfe4a0c6。
- [Installs](https://developers.google.com/android/work/play/emm-api/v1/installs)，Methods: update（Deprecated，2025-09-30 后不可访问，请求安装最新版本），正文 60–68 行；获取 2026-09-05T10:51:54.596982+00:00；SHA 49b37437faa701eecb2efdca840abd9069a09719db6124b0db6e38ddbfe4a0c6。
- [Update your security provider to protect against SSL exploits](https://developer.android.com/privacy-and-security/security-gms-provider)，Patch the security provider using ProviderInstaller（安全 Provider 组件级更新，非完整应用安装），正文 27–36 行；获取 2026-09-05T10:34:33.738340+00:00；SHA 8502bfc98fae3c3670889414f5811aa5a05149217d8bf3557350417876384578。

## ios 条件与证据

适用范围：Apple 文档快照 2026-09-05 获取、version_verified=false；ios-1 分层提及 iOS 14.6/15/16.1 行为；ios-2 未标注适用系统版本，iOS 适用性未逐符号核对；未固定启动日基线。
条件：ios-1 面向广告网络与 StoreKit 生态，行为按 SKAdNetwork 签名版本与 iOS 14.6/15/16.1 分层；ios-2 面向 MDM 设备管理服务（声明式管理），对象是系统软件更新而非应用更新；Apple 目录跨多操作系统，ios-2 页面未明示 iOS 适用版本，需逐符号核对
缺口：无 App Store 应用安装/更新流程文档；无 MDM 应用安装命令与自动应用更新设置文档；ios-2 为系统更新域，与节点应用域的映射未确认；iOS 适用版本未逐符号核对；基线未固定
真机分类理由：应用安装/更新行为（含商店分发与 MDM 强制路径）最终核实需真机与对应管理/商店环境；本轮仅文档初判，无实测。

- [Receiving ad attributions and postbacks](https://developer.apple.com/documentation/storekit/receiving-ad-attributions-and-postbacks)，Discussion：安装事件与时间窗、安装验证回传触发条件，正文 5–14 行；获取 2026-09-05T11:20:20.945996+00:00；SHA 35c4e56fbb556ac8343639d91115466104e3e6c2d359c5485706d92a6a1b2220。
- [Phases of software update enforcement](https://developer.apple.com/documentation/devicemanagement/phases-of-software-update-enforcement)，Phase 1–3：SoftwareUpdateEnforcementSpecific 声明、下载与 prepared 状态（对象为系统软件更新），正文 15–38 行；获取 2026-09-05T10:50:34.962310+00:00；SHA e0540390bf82ef2e9a3655efb16e86c1c26a189b9858f84a48bd010f20bf5462。

## harmonyos 条件与证据

适用范围：快照 2026-09-05 获取、version_verified=false；ohpm 文档提及 6.0.2.636 与 26.0.0.630 工具版本门槛；MDM diff 页（b031）为特定版本 API 变更清单，未固定 HarmonyOS 正式发行版基线。
条件：ohpm update 作用于开发工程依赖（oh-package.json5，semver 规则），非设备端应用安装/更新；MDM Kit 接口面向企业 admin（Want 参数），更新对象为固件包（PackageType FIRMWARE）；MDM diff 页仅 API 变更清单无正文行为说明；@ohos.enterprise 需区分 OpenHarmony 与 HarmonyOS 发行版可见性
缺口：未读到应用安装/更新机制文档（AppGallery 分发、bundleManager 安装接口、应用市场更新、企业应用安装）；MDM diff 页仅 API 清单，接口正文、权限与版本条件未读；OpenHarmony 与 HarmonyOS 发行版区分未核对；基线未固定，未核对启动日最新正式版
真机分类理由：未建立机制判断（未读到应用级安装/更新文档），真机需求待补充官方文档并确认域映射后再评估。

- [ohpm update](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-update)，功能描述：按 semver 规范更新本地三方库依赖（非应用安装），正文 16–19 行；获取 2026-09-05T10:23:23.588932+00:00；SHA ccf057445b33a261c30050f4b78a0ff1b5f6c36c385d3bd2105296994e583815。
- [MDM Kit](https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mdmkit-b031)，systemManager 新增 PolicyType 枚举（含 UPDATE_TO_SPECIFIC_VERSION/POSTPONE/WINDOWS）与 OtaUpdatePolicy 接口，正文 12–24 行；获取 2026-09-05T11:02:11.449626+00:00；SHA cd9baa082a438195744280356034d74fed93317be7b7f92f6008d930d900f070。
- [MDM Kit](https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mdmkit-b031)，UpdateStatus 枚举与 setOtaUpdatePolicy/getOtaUpdatePolicy/notifyUpdatePackages/getUpdateResult 函数，正文 44–56 行；获取 2026-09-05T11:02:11.449626+00:00；SHA cd9baa082a438195744280356034d74fed93317be7b7f92f6008d930d900f070。

## 待验证差异假设

- api_surface：企业侧远程触发完整应用安装/更新的接口面（can 层面）：Android 文档明示 Google Play EMM API（生态服务）可远程安装并把已装应用更新到最新版本（方法已弃用且 2025-09-30 后不可访问）；iOS 已读文档仅见系统软件更新强制与广告归因安装验证，未见应用级远程安装/更新接口。假设两平台该接口面存在文档层面的差异，属文档缺口而非能力结论。；待核：iOS MDM 应用安装命令与 App Store 批量采购安装文档未检索，不能据此认为 iOS 无此能力；HarmonyOS 企业应用安装/更新文档缺失，第三平台对照未建立；Android EMM 过期方法的现行替代（如 Android Management API）未读，现行机制待补。
- programming_model：系统级更新治理编程模型（注意：两者均为系统/固件更新域，映射到本应用节点待确认）：iOS 采用声明式管理（SoftwareUpdateEnforcementSpecific 声明同步 + waiting/downloading/prepared/installing/failed 状态上报的分阶段流程）；HarmonyOS MDM Kit 为命令式策略函数（setOtaUpdatePolicy/getOtaUpdatePolicy/notifyUpdatePackages/getUpdateResult，PolicyType 含 UPDATE_TO_SPECIFIC_VERSION/POSTPONE/WINDOWS）。假设两平台系统更新管理的接口形态不同。；待核：两者均为系统/固件更新域，与本节点应用域的对应关系待精研确认；HarmonyOS MDM API 参考正文（非 diff 清单）与适用发行版未读，OpenHarmony/HarmonyOS 区分未核对；iOS 声明式管理是否延伸到应用更新未读。

范围缺口：消费侧应用商店安装/更新流程文档三平台均未进入本轮冻结来源；Android 系统 SDK 安装接口（PackageInstaller 等）、iOS MDM 应用安装命令、HarmonyOS 应用安装/更新接口文档缺失；版本基线未固定（unresolved），结论仅代表 2026-09-05 文档快照，不代表启动日最新正式版；已读 iOS/HarmonyOS 文档属系统更新或开发工具域，与节点应用域的映射未确认，存在错配风险

后续优先级：P1；三平台中两平台无应用级安装/更新正文，且已读 iOS/HarmonyOS 文档属系统更新或开发工具域，存在错配到应用域的高风险映射；需优先补 App Store/MDM 应用安装与 AppGallery/bundleManager 等官方文档并核对映射与版本条件。

逐条引用及原文摘录见同目录 normalized.json。
