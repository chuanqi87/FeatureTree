# 电池状态 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

Android 训练文档给出机制：BatteryManager 粘性广播查询电量/充电状态，清单 receiver 监听 POWER_CONNECTED/DISCONNECTED，Android 8.0 起禁止持续监听电量并推荐 WorkManager 约束；HarmonyOS @ohos.batteryInfo（API 6+）同步查询电量/充电/充电器类型，workScheduler（API 9+）支持电量条件触发；iOS 冻结来源仅 MDM/HIDDriverKit 内容，应用级电池 API 缺失，保留 unknown。全部 low 置信。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | documented_mechanism | direct | 训练文档明示机制：BatteryManager 以粘性 Intent 广播电量与充电详情，registerReceiver 传 null 即取当前状态（EXTRA_STATUS/PLUGGED/LEVEL/SCALE）；充电变化经清单 receiver 监听 ACTION_POWER_CONNECTED/DISCONNECTED；Android 8.0 起不能持续监听电量，推荐 WorkManager BatteryNotLow 约束。 | recommended |
| ios | unknown | missing | 冻结来源均不涉及 iOS 应用级电池状态：ios-1 为 MDM NotNow 命令响应处理（仅 macOS Power Nap 提及电池供电），ios-2 为 HIDDriverKit 的 HID 电池 Usage 常量列表；未读到应用级电池查询/监听 API 正文，无法建立信号。 | unassessed |
| harmonyos | documented_mechanism | direct | @ohos.batteryInfo 提供电池状态与充放电状态同步查询：batterySOC（0-100）、chargingStatus、pluggedType（NONE/AC/USB/WIRELESS）、电压/温度等，首批 API 6；并定义 COMMON_EVENT_BATTERY_CHANGED 事件查询键（API 9+）；workScheduler 可设 isCharging/batteryLevel/batteryStatus 为延迟任务触发条件（API 9+）。 | recommended |

## android 条件与证据

适用范围：训练文档正文未标注各 API 的 API Level，仅明示 Android 8.0 起限制清单注册的电池广播接收器；最新正式版适用性未核实（本包 baseline 未固定）
条件：读取当前状态：context.registerReceiver(null, IntentFilter(ACTION_BATTERY_CHANGED)) 获取粘性广播；充电/电量字段经 BatteryManager extras（EXTRA_STATUS、EXTRA_PLUGGED、EXTRA_LEVEL、EXTRA_SCALE）提取，百分比由 level/scale 计算；监听充电变化需在 manifest 注册 receiver 并声明 ACTION_POWER_CONNECTED/ACTION_POWER_DISCONNECTED；持续监听电量自 Android 8.0 起不可行，官方推荐改用 WorkManager BatteryNotLow 约束
缺口：未读到 BatteryManager 常量与 ACTION_BATTERY_CHANGED 的 API 参考正文，API Level 与权限要求未核实；训练文档仅示例 USB/AC 充电判断，是否存在无线等更多充电类型常量未在正文出现；手机/平板设备形态适用条件未在正文声明；最新正式版下粘性广播与 WorkManager 约束的行为未核实
真机分类理由：充电状态转换、粘性广播与 WorkManager 约束行为随系统版本与设备状态变化，正式确认建议真机验证；本轮仅文档初判，未实测。

- [Monitor the Battery Level and Charging State](https://developer.android.com/training/monitoring-device-state/battery-monitoring)，Monitor the Battery Level and Charging State > Determine the current charging state（粘性广播查询），正文 16–25 行；获取 2026-09-05T10:38:26.943637+00:00；SHA 4bfe5a6748112e208e87f4fec16aa464c428d07e45cb83f6cd1b986bcba3fe51。
- [Monitor the Battery Level and Charging State](https://developer.android.com/training/monitoring-device-state/battery-monitoring)，充电状态与充电类型提取（EXTRA_STATUS、BATTERY_PLUGGED_USB/AC），正文 42–70 行；获取 2026-09-05T10:38:26.943637+00:00；SHA 4bfe5a6748112e208e87f4fec16aa464c428d07e45cb83f6cd1b986bcba3fe51。
- [Monitor the Battery Level and Charging State](https://developer.android.com/training/monitoring-device-state/battery-monitoring)，Monitor changes in charging state（清单 receiver），正文 76–94 行；获取 2026-09-05T10:38:26.943637+00:00；SHA 4bfe5a6748112e208e87f4fec16aa464c428d07e45cb83f6cd1b986bcba3fe51。
- [Monitor the Battery Level and Charging State](https://developer.android.com/training/monitoring-device-state/battery-monitoring)，Determine the current battery level（EXTRA_LEVEL/EXTRA_SCALE），正文 98–123 行；获取 2026-09-05T10:38:26.943637+00:00；SHA 4bfe5a6748112e208e87f4fec16aa464c428d07e45cb83f6cd1b986bcba3fe51。
- [Monitor the Battery Level and Charging State](https://developer.android.com/training/monitoring-device-state/battery-monitoring)，React to significant changes in battery level（Android 8.0 限制与 WorkManager BatteryNotLow），正文 125–144 行；获取 2026-09-05T10:38:26.943637+00:00；SHA 4bfe5a6748112e208e87f4fec16aa464c428d07e45cb83f6cd1b986bcba3fe51。

## ios 条件与证据

适用范围：无法判断：冻结来源无 iOS 应用级电池 API 正文，ios-2 未含 iOS availability 元数据，iOS 适用版本未知
条件：ios-1 讨论的是设备管理服务 NotNow 命令重试机制，不涉及应用可用的电池状态接口；ios-2 列出的是 HIDDriverKit 驱动层 kHIDUsage_BS_* 常量，面向 HID 设备驱动而非应用电池状态查询
缺口：缺 iOS 应用级电池电量/充电状态查询与监听 API 的官方正文，无法初判信号；未核对 iOS 适用性与最低系统版本（Apple 目录含多平台，需逐符号核对）；不得据此推断 iOS 不支持本特性
真机分类理由：未读到 iOS 应用级电池 API 正文，无法评估真机需求；待补齐来源后另行评估。

- [Battery System](https://developer.apple.com/documentation/hiddriverkit/battery-system-enum)，Battery System（HIDDriverKit HID Usage 常量目录，非应用 API），正文 1–3 行；获取 2026-09-05T10:51:49.215071+00:00；SHA 83dc022018040665e725a721b0e42bdb6a6d359e9eece54cc179264eaa186089。
- [Handling NotNow status responses](https://developer.apple.com/documentation/devicemanagement/handling-notnow-status-responses)，Handling NotNow status responses（MDM 命令处理，非电池 API），正文 1–9 行；获取 2026-09-05T10:50:23.316952+00:00；SHA b6f3c7f96446115d97c1eab190ba00886a60c5619f67ea8659e09b9809ee6b63。

## harmonyos 条件与证据

适用范围：batteryInfo 首批 API 6 起，isBatteryPresent 7+、batteryCapacityLevel 与事件查询键 9+、nowCurrent 12+；workScheduler 首批 API 9、earliestStartTime 22+；为华为文档站正文，具体 HarmonyOS/OpenHarmony 发行版与最新正式版未核实
条件：查询接口经 @kit.BasicServicesKit 导入，系统能力 SystemCapability.PowerManager.BatteryManager.Core；电量/充电状态为同步只读属性（batterySOC、chargingStatus、pluggedType 等）；变更监听指向 COMMON_EVENT_BATTERY_CHANGED 通用事件，本包未含其订阅 API 正文；workScheduler 电池触发条件仅适用于 Stage 模型延迟任务，循环任务间隔至少 2 小时
缺口：未读到 COMMON_EVENT_BATTERY_CHANGED 的订阅/监听 API 正文，监听机制为基于查询键表的推断；batterySOC 精度（整数/浮点、舍入规则）未说明；HarmonyOS 与 OpenHarmony 发行版归属及最新正式版适用性未核实；正文未声明权限要求与手机/平板设备形态条件
真机分类理由：电量百分比精度、充电状态枚举实际取值与电池事件触发时机需真机核对；本轮仅文档初判，未实测。

- [@ohos.batteryInfo (电量信息)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-battery-info)，@ohos.batteryInfo 模块说明与导入（首批 API 6，@kit.BasicServicesKit），正文 1–11 行；获取 2026-09-05T10:27:02.324405+00:00；SHA 44649031c909b6364c125f846336597edf59d51d7252c984f3e95143221a8549。
- [@ohos.batteryInfo (电量信息)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-battery-info)，常量表（batterySOC、chargingStatus、pluggedType、batteryCapacityLevel 9+、nowCurrent 12+），正文 13–31 行；获取 2026-09-05T10:27:02.324405+00:00；SHA 44649031c909b6364c125f846336597edf59d51d7252c984f3e95143221a8549。
- [@ohos.batteryInfo (电量信息)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-battery-info)，BatteryPluggedType / BatteryChargeState 枚举（AC/USB/WIRELESS），正文 68–94 行；获取 2026-09-05T10:27:02.324405+00:00；SHA 44649031c909b6364c125f846336597edf59d51d7252c984f3e95143221a8549。
- [@ohos.batteryInfo (电量信息)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-battery-info)，CommonEventBatteryChangedKey（COMMON_EVENT_BATTERY_CHANGED 查询键，API 9+），正文 128–144 行；获取 2026-09-05T10:27:02.324405+00:00；SHA 44649031c909b6364c125f846336597edf59d51d7252c984f3e95143221a8549。
- [@ohos.resourceschedule.workScheduler (延迟任务调度)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-workscheduler)，WorkInfo 触发条件（isCharging、chargerType、batteryLevel、batteryStatus），正文 480–513 行；获取 2026-09-05T10:27:51.356781+00:00；SHA 7f62e34902bf04c4bca602623ce49d1ec62844b657344601a11dbfd9368943b0。
- [@ohos.resourceschedule.workScheduler (延迟任务调度)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-workscheduler)，BatteryStatus 枚举（BATTERY_STATUS_LOW/OKAY/LOW_OR_OKAY），正文 542–552 行；获取 2026-09-05T10:27:51.356781+00:00；SHA 7f62e34902bf04c4bca602623ce49d1ec62844b657344601a11dbfd9368943b0。

## 待验证差异假设

- programming_model：查询模型假设：Android 经 registerReceiver(null, ACTION_BATTERY_CHANGED) 读粘性广播 extras（STATUS/PLUGGED/LEVEL/SCALE）并由 level/scale 计算百分比；HarmonyOS 直接同步读属性 batterySOC/chargingStatus/pluggedType。can 层面两者均提供查询接口，但接口形态与精度表达待核。；待核：batterySOC 是否整数百分比、与 Android level/scale 计算的精度差异未读；两平台状态值/广播的刷新时机未读；iOS 无相关来源，无法纳入本假设比较。
- lifecycle_background：监听模型假设：Android 需清单注册 receiver 监听 ACTION_POWER_CONNECTED/DISCONNECTED，且 Android 8.0 起不能以清单 receiver 持续监听电量，官方推荐 WorkManager BatteryNotLow 约束交系统决策；HarmonyOS workScheduler 以 isCharging/batteryLevel/batteryStatus 为延迟任务触发条件由系统调度。两者均向系统托管条件演化，但条件粒度与回调形态不同。；待核：HarmonyOS BATTERY_STATUS_LOW 阈值与 Android BatteryNotLow 阈值是否对应；HarmonyOS COMMON_EVENT_BATTERY_CHANGED 订阅机制未读，与 Android 广播监听是否等价待核；iOS 后台电池监听约束无来源，无法比较。
- api_surface：充电类型枚举覆盖假设：读到的 Android 训练正文仅示例 BATTERY_PLUGGED_USB/BATTERY_PLUGGED_AC 两类判断；HarmonyOS batteryInfo.pluggedType 与 workScheduler ChargingType 明示 AC/USB/WIRELESS（含无线）。Android 是否另有无线充电常量未在本文档出现，枚举覆盖差异待 API 参考核实。；待核：Android BatteryManager 是否定义 BATTERY_PLUGGED_WIRELESS 等常量需 API 参考正文确认；iOS 充电类型查询能力无来源。

范围缺口：iOS 应用级电池电量/充电状态 API 正文完全缺失（冻结来源为 MDM 与 HIDDriverKit 内容），iOS 侧信号 unknown；Android 仅有训练指南，缺 BatteryManager 常量、ACTION_BATTERY_CHANGED 及相关广播 action 的 API 参考正文（API Level、权限、充电类型全集）；HarmonyOS COMMON_EVENT_BATTERY_CHANGED 订阅 API 正文与 batterySOC 精度未入包；三平台手机/平板设备形态条件与最新正式版基线均未核实，全部结论为 low 置信初判

后续优先级：P1；iOS 侧零相关证据为关键缺口，且监听机制（清单广播/系统托管条件/通用事件）与充电类型枚举存在高风险跨平台映射；精研需优先补齐 iOS 来源、核对 Android/HarmonyOS API 参考与发行版基线。

逐条引用及原文摘录见同目录 normalized.json。
