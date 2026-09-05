# app.background.foreground_task 研究试点笔记（2026-09-06）

- 性质：限量报告型试点，仅证据/边界诊断。模型固定 volcengine/glm-5.3，不使用子代理；模型/费用不可观测。
- 未读取 output/research/tasks 旧任务包，未写 candidate.yaml，未填24条比较，未读校验实现代码。
- **阶段结果：low / 未正式确认**。全局版本基线未完成，所有项均未核对最低版本适用性；差异仅为候选，不声称任何平台独有或不支持。

## 节点范围

定义"向用户明示的长时后台工作（如下载、导航）"。判断：这是**场景级**比较单元而非同一API概念。三平台均有"用户可感知、系统明示约束"的长时后台机制，但形态不同：Android前台服务（FGS）、iOS连续后台任务（BGContinuedProcessingTask，属"Foreground tasks with background support"主题）及更早background modes、HarmonyOS长时任务（ContinuousTask）。比较维度应落在：用户明示载体（通知/Live Activity）、触发条件、取消语义、数量与时长配额、系统一致性管控。

## 文档观察（每平台1条，证据见表）

1. **Android**［A1,A2］：`Service.startForeground`将已启动服务转前台并提供持续通知；targeting P+须声明`FOREGROUND_SERVICE`权限，Q+须指定`foregroundServiceType`，targeting S+不允许从后台启动FGS（存在豁免）；`onTimeout`回调存在，说明类型级超时；指南将FGS定位为"不可中断立即运行"的任务类别。
2. **iOS**［I1,I2］：BackgroundTasks框架明设"Foreground tasks with background support"：BGContinuedProcessingTask前台开始、可后台继续；**须响应用户动作发起**；系统以Live Activity展示进度，用户可取消；用户在app切换器关闭应用时系统取消运行中任务且不通知应用；后台GPU需entitlement。**两篇均未标注最低iOS版本（缺口）**。iOS存在替代机制，不能判unsupported。
3. **HarmonyOS**［H1,H2］：长时任务经`backgroundTaskManager.startBackgroundRunning`申请，需`ohos.permission.KEEP_BACKGROUND_RUNNING`权限并在module.json5声明backgroundModes；申请成功后通知栏消息与任务绑定，**用户删除通知即停止任务**；系统做一致性校验：业务与申请类型不符、未执行或已结束时退后台被挂起/终止；API 9起支持，API 21起一个UIAbility最多10个。

## 待证差异/反例（2个）

- **D1 用户侧取消入口**：iOS明示"关闭app→任务取消"；HarmonyOS明示"删通知→任务停止"；Android未见"用户移除通知即停止FGS"的对等明示（需补FGS文档核实；缺失不构成不支持结论）。
- **D2 触发约束与存活落差**：iOS必须用户动作在前台发起；Android有后台启动豁免（如高优先FCM）；HarmonyOS未明示必须用户触发。**反例**：HarmonyOS明示DATA_TRANSFER托管给@ohos.request时退后台仍被挂起——申请成功≠后台存活，文档限制与真机存活必须分开验证。

## 先补文档 vs 真机

**先补文档**：Android FGS类型清单与类型超时（dataSync等）、用户移除通知对FGS的影响、Android 14+启动限制；iOS BGContinuedProcessingTask符号availability与最低系统版本、iOS 26前background modes替代路径；HarmonyOS长时任务类型全表、ACL权限（TASK_KEEPING）、HarmonyOS发行版与API version映射。

**真机复核（均未实测，不写pass）**：
- Android（建议）：前台启动dataSync FGS→退后台记录存活30分钟与通知→用户划掉通知→记录服务是否停止及日志。
- iOS（必须，iOS 26+真机）：用户点击触发视频导出任务→退后台观察Live Activity→app切换器关闭应用→验证任务取消与expirationHandler行为（文档称不通知应用）。
- HarmonyOS（必须）：申请AUDIO_PLAYBACK并实际播放→退后台确认通知→删除通知验证自动停止；另申请DATA_TRANSFER但不实际传输，验证退后台被挂起。

## 证据元数据（不计正文字数）

| ID | 平台 | URL | 章节/符号 | 本地路径 | body SHA-256 | 获取时间(UTC) |
|----|------|-----|-----------|----------|--------------|----------------|
| A1 | Android | https://developer.android.com/reference/android/app/Service | startForeground(int,Notification); onTimeout; FOREGROUND_SERVICE权限说明 | docs-raw/official/snapshots/android/23/23718a0245a0703b35f163c856bc713db487089958014b7ec3ab2cbfc1cb8643/7f56c0ba023f8b331fb20a225daa38e7babb5e2ce235308893f43154da8ab0c6/document-8840497d….md | 8840497d51841fe15c7d2a06ec7501a05ee261fcec099c68f95900dd6ec18db1 | 2026-09-05T14:47:49Z |
| A2 | Android | https://developer.android.com/develop/background-work/background-tasks | Foreground services; Will there be a bad user experience… | docs-raw/official/snapshots/android/be/bee3e5ca777d14a871b4edd429f01c8a264e615f60eaa2d5ccf566e96bc2ef8d/97c3b755a0df759781b89f38e4534a6efa48bde9f777d2010e01c6c5a2966005/document-3cf8561d….md | 3cf8561d01090bcc85e136dca1468e12aeee495556b6329919e228563e640a78 | 2026-09-05T10:15:51Z |
| I1 | iOS | https://developer.apple.com/documentation/backgroundtasks | Topics: Foreground tasks with background support | docs-raw/official/snapshots/ios/e7/e707b9e21193d5a79807989a6de50f1c6a6b3178f6e8afb7944d6ce83e307040/77c8aaabf6f97a09a6da5ad4be7f9c5a3081a50b5924bcb4a41ddebb7b65431b/document-c18ed3d4….md | c18ed3d47729cc341f5f62231efa84d6a5fcfd5fc00005febf9a78e1c9b245cc | 2026-09-05T10:30:00Z |
| I2 | iOS | https://developer.apple.com/documentation/backgroundtasks/performing-long-running-tasks-on-ios-and-ipados | Overview; Note（关闭app取消任务） | docs-raw/official/snapshots/ios/e4/e4bce79153e59010356e6cfc3e68ae7a437f6e5e8fb9e8d6c6f755d8b7f82b85/3de20d4abcaef707801d51ee10d264c208d885a98139e05241d0a153625a3048/document.md | e908838433613e4727aad0d91e4b59b7e4955b68e803b12b7c1579a05675bb1f | 2026-09-05T10:18:40Z |
| H1 | HarmonyOS | https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager | backgroundTaskManager.startBackgroundRunning（权限/系统能力/API版本标注） | docs-raw/official/snapshots/harmonyos/aa/aa12024f3842c7f912fbb6b94042ab66e362ee0b1540d565ed29b8c918cdd345/99f921885319f3e808b4da7d03a2395558b6ab3586cf9e8ee8bf4f2f75144803/document-c90d7a65….md | c90d7a65a2cb86c6ffaf74b68304a9573973882780911bf5ab55c29063814f40 | 2026-09-05T10:27:50Z |
| H2 | HarmonyOS | https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/continuous-task | 概述；使用场景；约束与限制 | docs-raw/official/snapshots/harmonyos/e1/e15b3ea0c4d2625a248a1de57f7a7a154c4c4163fed8231a2aa4bc67cbd610b6/bc64536b1981b3fccd2cc15eb281128fa3fbff6ee0e53cb3e7b93de6b7b054bd/document.md | ce5ab504bc0cc373926da12de86d2e84130a29471e14ea5214655f89b975ec81 | 2026-09-04T09:35:09Z（fetch复用既有快照） |

剩余缺口：I1/I2无最低iOS版本信息；iOS 26前替代机制（background modes）未读；Android FGS类型超时清单未读；HarmonyOS任务类型全表与发行版映射未读；三平台版本基线均未固定。候选包 binding_source_gaps 为空，不代表研究完成。
