# 延迟与条件任务 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

Android 读到 WorkManager 约束式延迟任务机制（NetworkType/RequiresCharging 等约束使工作推迟到条件满足，系统 doze/待机桶进一步延迟并限额）；iOS 读到 BackgroundTasks 框架目录页（BGTaskScheduler 与 BGAppRefreshTask/BGProcessingTask 任务族），约束属性与调度时机细节不在本文。HarmonyOS 冻结两篇来源（Node-API 进程内异步、企业网络管理）均与本节点无关，保留 unknown。基线未固定，全部 low，差异假设仅限 Android/iOS。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | documented_mechanism | direct | WorkManager 以 WorkRequest 定义一次性/周期任务，Constraints（NetworkType、RequiresCharging、BatteryNotLow、DeviceIdle、StorageNotLow）使工作延迟到条件全部满足，约束失效会停止并重试；系统侧 doze/待机桶会推迟并限额 JobScheduler 任务（WorkManager 后台经其调度），充电状态可解除限制。 | recommended |
| ios | documented_mechanism | direct | BackgroundTasks 框架提供 BGTaskScheduler 调度器与 BGAppRefreshTask（短刷新）、BGProcessingTask（数分钟级处理）等任务类型及对应 Request 类，用于后台更新与维护；本文为框架目录页，约束属性、entitlement 与调度时机细节未包含。 | recommended |
| harmonyos | unknown | missing | 冻结两篇来源均不涉及系统级约束调度的延迟任务：harmonyos-1 讲 Node-API napi_create_async_work 进程内异步（避免阻塞 ArkTS 线程），harmonyos-2 为 MDM Kit 企业网络管理 API。未读到相关机制正文，无法建立支持与否的判断。 | unassessed |

## android 条件与证据

适用范围：AndroidX WorkManager 库文档（文中提及 2.7.0 引入 expedited work）；系统侧行为引用 Android 9–16 变化。快照未核实具体库版本与 API Level 适用性。
条件：工作在全部 Constraints 满足后才运行，多约束须同时满足；周期任务最小重复间隔 15 分钟，可加 flex 区间；应用不可见时 WorkManager 经 JobScheduler 调度，受 doze/待机桶限额（如 rare 桶 24 小时滚动窗口 10 分钟）；设备充电时系统解除多数执行限额；expedited work 受系统配额限制且不能延迟调度
缺口：未核实当前 AndroidX WorkManager 最新正式版与本文快照的版本对应；Android 16 JobScheduler 配额变化对 WorkManager 的具体影响需按 API Level 逐一核对；Android 系统 SDK、AndroidX 库与 Google 生态服务（如 FCM）的版本与运行条件需分别固定；文档明确待机桶数值非执行时长保证，实际调度精度需实测
真机分类理由：机制与约束已由官方文档明示，但文档同时声明待机桶限额非执行时长保证、实际执行依赖设备状态，调度时机与限额行为需真机核实；本轮未做实测。

- [Define work requests](https://developer.android.com/topic/libraries/architecture/workmanager/how-to/define-work)，Work constraints：Constraints 使工作延迟到最优条件满足，列出 NetworkType/RequiresCharging/BatteryNotLow/DeviceIdle/StorageNotLow，正文 351–362 行；获取 2026-09-05T10:48:10.456751+00:00；SHA 3f34ec45b5840a790e1f9892c320b51fb00a2ffe822e51884899a02ad7bd3a86。
- [Define work requests](https://developer.android.com/topic/libraries/architecture/workmanager/how-to/define-work)，多约束须全部满足；运行中约束失效则 WorkManager 停止并待条件满足后重试；周期任务最小间隔 15 分钟，正文 293–294 行；获取 2026-09-05T10:48:10.456751+00:00；SHA 3f34ec45b5840a790e1f9892c320b51fb00a2ffe822e51884899a02ad7bd3a86。
- [Define work requests](https://developer.android.com/topic/libraries/architecture/workmanager/how-to/define-work)，多约束全部满足才运行；约束运行中失效时停止并重试，正文 399–404 行；获取 2026-09-05T10:48:10.456751+00:00；SHA 3f34ec45b5840a790e1f9892c320b51fb00a2ffe822e51884899a02ad7bd3a86。
- [Power management resource limits](https://developer.android.com/topic/performance/power/power-details)，系统在低电状态（doze）推迟任务执行；WorkManager 在应用不可见时经 JobScheduler 调度并受限额影响，正文 6–21 行；获取 2026-09-05T10:37:44.214495+00:00；SHA 326edbf570f7a90b7f7eab31a5f69d71df5b804d86fca4a71a24dd1acdaf11fc。
- [Power management resource limits](https://developer.android.com/topic/performance/power/power-details)，设备充电时系统解除待机桶执行限制，正文 29–32 行；获取 2026-09-05T10:37:44.214495+00:00；SHA 326edbf570f7a90b7f7eab31a5f69d71df5b804d86fca4a71a24dd1acdaf11fc。

## ios 条件与证据

适用范围：Apple BackgroundTasks 框架文档（2026 快照）；本文未给出各符号 iOS 最低版本/availability，iOS 适用版本未核实。
条件：需注册 launch handlers 并经 BGTaskScheduler 提交任务请求；框架定位为后台内容更新与需数分钟完成的任务，长任务可利用外部电源、网络连接；本页未含约束属性（如网络/电源要求）、Info.plist 配置与系统调度时机说明
缺口：BGTaskRequest/BGProcessingTaskRequest/BGAppRefreshTaskRequest 符号页（含约束属性如网络/外部电源要求）未在冻结来源中，约束表达待核；各符号 iOS availability 与最低部署版本未读到，不能确认 iOS 版本范围；系统调度时机与延迟策略（如系统何时运行任务）文档不在冻结集；本包另一来源 ios-1（Metal 示例库）与本节点无关，已排除引用
真机分类理由：框架机制已文档化，但系统实际何时运行任务、约束条件如何生效未在本文说明，需后续读符号页并真机核实调度行为；本轮未做实测。

- [Background Tasks](https://developer.apple.com/documentation/backgroundtasks)，Overview：框架用于后台更新与需数分钟的任务，注册 launch handlers 并调度任务，正文 5–11 行；获取 2026-09-05T10:30:00.542329+00:00；SHA c18ed3d47729cc341f5f62231efa84d6a5fcfd5fc00005febf9a78e1c9b245cc。
- [Background Tasks](https://developer.apple.com/documentation/backgroundtasks)，BGTaskScheduler：为应用最关键工作提供后台支持的调度类，正文 19–21 行；获取 2026-09-05T10:30:00.542329+00:00；SHA c18ed3d47729cc341f5f62231efa84d6a5fcfd5fc00005febf9a78e1c9b245cc。
- [Background Tasks](https://developer.apple.com/documentation/backgroundtasks)，BGProcessingTask（后台数分钟处理任务）与 BGAppRefreshTask（后台短刷新任务），正文 39–45 行；获取 2026-09-05T10:30:00.542329+00:00；SHA c18ed3d47729cc341f5f62231efa84d6a5fcfd5fc00005febf9a78e1c9b245cc。
- [Background Tasks](https://developer.apple.com/documentation/backgroundtasks)，任务请求类型：BGProcessingTaskRequest、BGAppRefreshTaskRequest、BGTaskRequest，正文 63–75 行；获取 2026-09-05T10:30:00.542329+00:00；SHA c18ed3d47729cc341f5f62231efa84d6a5fcfd5fc00005febf9a78e1c9b245cc。

## harmonyos 条件与证据

适用范围：无可判定机制的版本范围；harmonyos-2 标注 API 21–23（企业网络管理），与本节点无关。
条件：无可判定运行条件：冻结来源中无本节点机制文档
缺口：缺少 HarmonyOS 后台任务/延迟任务调度机制官方正文（如 resourceschedule 后台任务申请与延迟任务相关指南/API 参考），未能检索到不代表不支持；未核对 HarmonyOS 与 OpenHarmony 各自发行版的对应文档与版本条件；无法判断 HarmonyOS 是否提供网络/充电约束的延迟任务 API 及其行为差异
真机分类理由：尚未读到 HarmonyOS 相关机制文档，无法评估机制存在性与真机验证需求，待补官方正文后再分类。

- [使用Node-API接口进行异步任务开发](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-asynchronous-task)，场景介绍：napi_create_async_work 用于进程内耗时操作异步化，避免阻塞 ArkTS 线程；非系统级约束调度延迟任务，正文 3–15 行；获取 2026-09-05T10:25:03.303253+00:00；SHA 9bc8a004033d864ef3f51f08724a929c15e469efcae6b3a0d7cf83c05d2f0612。

## 待验证差异假设

- programming_model：假设 Android 与 iOS 的约束表达模型不同：Android WorkManager 以显式 Constraints 对象（NetworkType、RequiresCharging 等必须满足的条件）声明延迟任务；iOS 以 BGTaskScheduler 的任务请求类型（BGAppRefreshTaskRequest/BGProcessingTaskRequest）组织任务，约束是否及如何声明待读符号页确认。；待核：iOS 请求对象的约束属性（如网络/外部电源要求）是否存在于符号页及其语义是提示还是必须条件（can/must）未证；Android 约束在 iOS 侧是否有等价配置方式需读 BGTaskRequest 符号页确认。
- limits_precision：假设系统侧调度精度策略不同：Android 文档明示 doze/待机桶会推迟并限额 JobScheduler 任务（WorkManager 受其影响，充电解除限制）；iOS 本页仅说明框架用途，未说明系统调度时机、延迟或限额策略。；待核：iOS 系统调度时机与延迟策略文档（如选择后台策略指南）不在冻结集，差异方向无法判定；Android 各待机桶限额随版本变化（文提及 Android 16），需按 API Level 核实后才能比较。

范围缺口：HarmonyOS 平台完全缺源：冻结集中无延迟任务/后台任务调度机制正文（如 resourceschedule 相关指南与 API 参考），节点在该平台保持 unknown；iOS 缺符号级正文：BGTaskRequest 系列约束属性、availability 与配置要求未读到，约束表达能力未证；Android 版本基线未固定：WorkManager 库版本与 Android 9–16 系统行为变化的适用性未逐项核实；启动日最新正式版与手机基线未固定（version_baseline unresolved），全部结论仅限快照文本初判；本包 ios-1（Metal 示例库）与本节点主题无关，属来源选择噪声

后续优先级：P1；HarmonyOS 侧关键缺口（无任何相关机制来源，节点三平台之一无法判断），iOS 侧机制映射依赖缺失的符号页（约束属性与 iOS 适用版本），属于高风险映射与关键缺口并存的 P1 精研项。

逐条引用及原文摘录见同目录 normalized.json。
