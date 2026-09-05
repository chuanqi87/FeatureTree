# app.background.foreground_task 研究试点笔记（2026-09-06）

复核版：原始模型交付保存在 `output/research/pilot-originals/2026-09-06/`。协调者已修正 Android 版本条件、真机计划与证据元数据；本文仍是诊断草稿，不是验收通过的正式知识。实际模型已由执行记录核对，费用不可据此确定。

- 性质：限量报告型试点，仅证据/边界诊断。模型固定 volcengine/glm-5.3，不使用子代理；模型/费用不可观测。
- 未读取 output/research/tasks 旧任务包，未写 candidate.yaml，未填24条比较，未读校验实现代码。
- **阶段结果：low / 未正式确认**。全局版本基线未完成，所有项均未核对最低版本适用性；差异仅为候选，不声称任何平台独有或不支持。

## 节点范围

定义"向用户明示的长时后台工作（如下载、导航）"。判断：这是**场景级**比较单元而非同一API概念。三平台均有"用户可感知、系统明示约束"的长时后台机制，但形态不同：Android前台服务（FGS）、iOS连续后台任务（BGContinuedProcessingTask，属"Foreground tasks with background support"主题）及更早background modes、HarmonyOS长时任务（ContinuousTask）。比较维度应落在：用户明示载体（通知/Live Activity）、触发条件、取消语义、数量与时长配额、系统一致性管控。

## 文档观察（每平台1条，证据见表）

1. **Android**［A1,A2］：`Service.startForeground`将已启动服务转前台并提供持续通知。A1 区分：targeting P+ 须声明 `FOREGROUND_SERVICE` 权限；以 Q+ SDK 构建的应用**可以**指定 `foregroundServiceType`，并非 Q+ 一律必须；targeting UPSIDE_DOWN_CAKE（Android 14）+ 必须在清单声明有效服务类型。targeting S+ 的后台启动受限，具体豁免需补读。`onTimeout`说明特定类型存在超时契约，不证明所有类型同限额；A2 将 FGS 列为立即运行任务的一种机制，仍需按场景判断适用性。
2. **iOS**［I1,I2］：BackgroundTasks框架明设"Foreground tasks with background support"：BGContinuedProcessingTask前台开始、可后台继续；**须响应用户动作发起**；系统以Live Activity展示进度，用户可取消；用户在app切换器关闭应用时系统取消运行中任务且不通知应用；后台GPU需entitlement。**两篇均未标注最低iOS版本（缺口）**。iOS存在替代机制，不能判unsupported。
3. **HarmonyOS**［H1,H2］：长时任务经`backgroundTaskManager.startBackgroundRunning`申请，需`ohos.permission.KEEP_BACKGROUND_RUNNING`权限并在module.json5声明backgroundModes；申请成功后通知栏消息与任务绑定，**用户删除通知即停止任务**；系统做一致性校验：业务与申请类型不符、未执行或已结束时退后台被挂起/终止；API 9起支持，API 21起一个UIAbility最多10个。

## 待证差异/反例（2个）

- **D1 用户侧取消入口**：iOS明示"关闭app→任务取消"；HarmonyOS明示"删通知→任务停止"；Android未见"用户移除通知即停止FGS"的对等明示（需补FGS文档核实；缺失不构成不支持结论）。
- **D2 触发约束与存活落差**：iOS必须用户动作在前台发起；Android有后台启动豁免（如高优先FCM）；HarmonyOS未明示必须用户触发。**反例**：HarmonyOS明示DATA_TRANSFER托管给@ohos.request时退后台仍被挂起——申请成功≠后台存活，文档限制与真机存活必须分开验证。

## 先补文档 vs 真机

**先补文档**：Android FGS类型清单与类型超时（dataSync等）、用户移除通知对FGS的影响、Android 14+启动限制；iOS BGContinuedProcessingTask符号availability与最低系统版本、iOS 26前background modes替代路径；HarmonyOS长时任务类型全表、ACL权限（TASK_KEEPING）、HarmonyOS发行版与API version映射。

**真机复核（均未实测，不写pass）**：
- Android（建议）：前台启动dataSync FGS→退后台记录存活30分钟与通知→用户划掉通知→记录服务是否停止及日志。
- iOS（必须，先核对具体符号最低版本与选定 iPhone 系统构建号）：分别测试用户点击触发任务后退后台、从 Live Activity 取消任务、从 app 切换器关闭应用。最后一种情形文档明示取消且不通知应用，不能期待它与其他终止路径具有同一 expirationHandler 回调语义。记录各路径的进度、取消与日志；本轮未执行。
- HarmonyOS（必须）：申请AUDIO_PLAYBACK并实际播放→退后台确认通知→删除通知验证自动停止；另申请DATA_TRANSFER但不实际传输，验证退后台被挂起。

## 证据元数据（不计正文字数）

| ID | 平台 | URL | 章节/符号 | 本地路径 | body SHA-256 | 获取时间(UTC) |
|----|------|-----|-----------|----------|--------------|----------------|
| A1 | Android | https://developer.android.com/reference/android/app/Service | startForeground(int,Notification); onTimeout; FOREGROUND_SERVICE权限说明 | docs-raw/research/2026-09-06/23718a0245a0703b35f163c856bc713db487089958014b7ec3ab2cbfc1cb8643/8840497d51841fe15c7d2a06ec7501a05ee261fcec099c68f95900dd6ec18db1/document.md | 8840497d51841fe15c7d2a06ec7501a05ee261fcec099c68f95900dd6ec18db1 | 2026-09-05T14:47:49.477262+00:00 |
| A2 | Android | https://developer.android.com/develop/background-work/background-tasks | Foreground services; Will there be a bad user experience… | docs-raw/research/2026-09-06/bee3e5ca777d14a871b4edd429f01c8a264e615f60eaa2d5ccf566e96bc2ef8d/3cf8561d01090bcc85e136dca1468e12aeee495556b6329919e228563e640a78/document.md | 3cf8561d01090bcc85e136dca1468e12aeee495556b6329919e228563e640a78 | 2026-09-05T10:15:51.956146+00:00 |
| I1 | iOS | https://developer.apple.com/documentation/backgroundtasks | Topics: Foreground tasks with background support | docs-raw/research/2026-09-06/e707b9e21193d5a79807989a6de50f1c6a6b3178f6e8afb7944d6ce83e307040/c18ed3d47729cc341f5f62231efa84d6a5fcfd5fc00005febf9a78e1c9b245cc/document.md | c18ed3d47729cc341f5f62231efa84d6a5fcfd5fc00005febf9a78e1c9b245cc | 2026-09-05T10:30:00.542329+00:00 |
| I2 | iOS | https://developer.apple.com/documentation/backgroundtasks/performing-long-running-tasks-on-ios-and-ipados | Overview; Note（关闭app取消任务） | docs-raw/research/2026-09-06/e4bce79153e59010356e6cfc3e68ae7a437f6e5e8fb9e8d6c6f755d8b7f82b85/e908838433613e4727aad0d91e4b59b7e4955b68e803b12b7c1579a05675bb1f/document.md | e908838433613e4727aad0d91e4b59b7e4955b68e803b12b7c1579a05675bb1f | 2026-09-05T10:18:40.977833+00:00 |
| H1 | HarmonyOS | https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager | backgroundTaskManager.startBackgroundRunning（权限/系统能力/API版本标注） | docs-raw/research/2026-09-06/aa12024f3842c7f912fbb6b94042ab66e362ee0b1540d565ed29b8c918cdd345/c90d7a65a2cb86c6ffaf74b68304a9573973882780911bf5ab55c29063814f40/document.md | c90d7a65a2cb86c6ffaf74b68304a9573973882780911bf5ab55c29063814f40 | 2026-09-05T10:27:50.968078+00:00 |
| H2 | HarmonyOS | https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/continuous-task | 概述；使用场景；约束与限制 | docs-raw/research/2026-09-06/e15b3ea0c4d2625a248a1de57f7a7a154c4c4163fed8231a2aa4bc67cbd610b6/ce5ab504bc0cc373926da12de86d2e84130a29471e14ea5214655f89b975ec81/document.md | ce5ab504bc0cc373926da12de86d2e84130a29471e14ea5214655f89b975ec81 | 2026-09-04T09:35:09+00:00 |

剩余缺口：I1/I2无最低iOS版本信息；iOS 26前替代机制（background modes）未读；Android FGS类型超时清单未读；HarmonyOS任务类型全表与发行版映射未读；三平台版本基线均未固定。候选包 binding_source_gaps 为空，不代表研究完成。
