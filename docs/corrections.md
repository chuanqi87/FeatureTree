# 基于本地文档的历史纠错记录

以下是 v1 阶段的修订历史，保留以追溯正文来源。它不代表 v2 结构化确认结果；当前状态见 output/reports/progress.md。

种子知识在抓取官方文档后发现的问题与修正（持续追加）。

## 2026-09-05

### 文档证据落地

| 来源 | 本地路径 |
| --- | --- |
| OpenHarmony 52 Kit Readme | `docs-raw/harmonyos/api-index/kits/` |
| `@ohos.bluetooth.ble` | `docs-raw/harmonyos/api-index/modules/js-apis-bluetooth-ble.md` |
| `notificationManager` | `docs-raw/harmonyos/api-index/modules/js-apis-notificationManager.md` |
| `@ohos.app.ability.Want` | `docs-raw/harmonyos/api-index/modules/js-apis-app-ability-want.md` |
| Core Bluetooth / UserNotifications 等 | `docs-raw/ios/frameworks/`（36） |
| Android BLE / Intent Guide | `docs-raw/android/guide-pages/` |

### 已修正的知识错误

1. **鸿蒙 BLE 入口**：不是笼统的 `@ohos.bluetooth.ble`「有过滤就 full」——实为 `@kit.ConnectivityKit` 的 `ble.startBLEScan(ScanFilter[], ScanOptions?)`，且**单路扫描**、权限 `ACCESS_BLUETOOTH`、SysCap `Communication.Bluetooth.Core`。
2. **iOS 后台 BLE**：补充官方 Overview——iOS 26+ Live Activity + CBManager 可放宽后台扫描；iPad-on-Mac 不支持 Core Bluetooth 后台模式。
3. **Want vs Intent**：Want 文档确认是 Ability 间载体，并有 **IPC 100KB/200KB** 上限；不能当 Intent Filter 等价物。
4. **本地通知**：鸿蒙应用 `notificationManager.publish` + 常需 `requestEnableNotification`，勿与 Push Kit 混绑。

### inventory 覆盖（harvest 后）

见 `inventory/mapping_summary.json`。iOS 仍有 ~70 条未映射（多为 macOS/Web/商店 API，需人工决定是否入树）。
