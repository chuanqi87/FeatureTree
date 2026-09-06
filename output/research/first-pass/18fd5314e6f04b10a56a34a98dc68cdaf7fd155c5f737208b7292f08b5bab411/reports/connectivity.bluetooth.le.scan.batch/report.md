# BLE批量扫描结果 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

三平台冻结源均未明示BLE扫描结果的硬件/系统级批量投递机制。Android指南仅展示逐条onScanResult交付，ScanSettings未提批量参数；iOS两源离题（MDM分批检索、MIDI连接）；HarmonyOS回调为数组（Array<ScanResult>/ScanReport）疑可聚合交付，但批量语义与节能意图未文档化。全部low置信，差异假设1条，需补API参考正文。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | unknown | missing | 冻结指南仅展示BluetoothLeScanner.startScan+ScanCallback.onScanResult逐条交付结果；提及ScanSettings但未列批量/延迟上报参数；android-2的batched仅位置域(FLP setMaxWaitTime)，非BLE。未读到BLE批量交付机制。 | unassessed |
| ios | unknown | missing | 两源均离题：ios-1为DeviceManagement服务端记录分批检索(batchToken)；ios-2为Core MIDI连接BLE MIDI外设的步骤，仅泛称Scan for and connect，均未描述BLE扫描结果回调形态或批量交付。 | unassessed |
| harmonyos | possible_mapping | indirect | BLE指南结果经'BLEDeviceFind'事件上报：API 15+回调ScanReport（示例scanReport.scanResult为数组），API 14及以前回调Array<ble.ScanResult>，单次事件可含多条结果，疑与聚合交付对应；但指南未说明批量语义/节能意图，ScanOptions.interval含义未解释。 | recommended |

## android 条件与证据

适用范围：指南未标注API Level；android-2适用Android 8.0 (API 26)+且属位置域；启动日基线未固定，不能断言最新正式版行为
条件：需Bluetooth开启，否则getBluetoothLeScanner()返回null（正文明示）；指南提示扫描耗电，建议找到即停并设时限；android-2所载batched机制属位置服务(FLP)，不可推及BLE
缺口：冻结源无ScanSettings/ScanCallback API参考正文，是否存在批量上报/延迟参数及其API Level未核实；硬件offload批量扫描的设备/芯片支持条件未读到；不能据此断言Android支持或不支持BLE批量交付
真机分类理由：未读到批量交付机制的文档描述，无法判断真机验证需求；需先补ScanSettings/ScanCallback参考正文

- [Find BLE devices](https://developer.android.com/develop/connectivity/bluetooth/ble/find-ble-devices)，Find BLE devices: startScan与ScanCallback说明，结果经回调返回且扫描耗电，正文 3–9 行；获取 2026-09-05T09:34:20.942633+00:00；SHA 054735bff9d159c01230ee1c49befcabfb5998fadf842a227d0b8fb196d8328b。
- [Find BLE devices](https://developer.android.com/develop/connectivity/bluetooth/ble/find-ble-devices)，BluetoothLeScanner仅在Bluetooth开启时可用，否则返回null，正文 76–82 行；获取 2026-09-05T09:34:20.942633+00:00；SHA 054735bff9d159c01230ee1c49befcabfb5998fadf842a227d0b8fb196d8328b。
- [Find BLE devices](https://developer.android.com/develop/connectivity/bluetooth/ble/find-ble-devices)，startScan(List<ScanFilter>, ScanSettings, ScanCallback)：ScanSettings仅称指定扫描参数，未提批量，正文 84–89 行；获取 2026-09-05T09:34:20.942633+00:00；SHA 054735bff9d159c01230ee1c49befcabfb5998fadf842a227d0b8fb196d8328b。
- [Find BLE devices](https://developer.android.com/develop/connectivity/bluetooth/ble/find-ble-devices)，ScanCallback实现示例：onScanResult(callbackType, result)逐条交付单条结果，正文 91–108 行；获取 2026-09-05T09:34:20.942633+00:00；SHA 054735bff9d159c01230ee1c49befcabfb5998fadf842a227d0b8fb196d8328b。
- [Background Location Limits](https://developer.android.com/about/versions/oreo/background-location-limits)，Background Location Limits：batched版本仅指FLP位置API，属位置域而非BLE，正文 55–61 行；获取 2026-09-05T10:22:11.511764+00:00；SHA 72cdbe99befb06edc2826ff13e795d6b2d01a3ff58f5a946e3a2b658898265e2。

## ios 条件与证据

适用范围：ios-2提及macOS 13+/iOS 16+自动重连行为（非扫描交付）；扫描结果交付的iOS版本信息缺失；基线未固定
条件：ios-1内容属MDM服务端API域，与本节点无关；ios-2属Core MIDI域，仅涉BLE MIDI外设连接
缺口：缺Core Bluetooth扫描回调（如didDiscover）正文；iOS是否有扫描结果聚合/合并上报选项及其版本未核实；Apple目录需逐符号核对iOS适用性
真机分类理由：无BLE扫描结果交付机制的证据，无法评估真机验证需求

- [Retrieving a large record set](https://developer.apple.com/documentation/devicemanagement/retrieving-a-large-record-set)，Retrieving a large record set: batchToken分批响应机制，属DeviceManagement服务端域，正文 23–31 行；获取 2026-09-05T10:52:51.279362+00:00；SHA ae24a60596cf6fca40f798412e92d4ac363ebd41858528da740ab4d2df6e4432。
- [MIDI Bluetooth](https://developer.apple.com/documentation/coremidi/midi-bluetooth)，MIDI Bluetooth: 扫描并连接BLE MIDI外设的步骤，未描述扫描结果交付方式，正文 5–17 行；获取 2026-09-05T10:19:31.589071+00:00；SHA ab572b5edaf882af58dfc263216a20694da4a1d8d1ea7aa9ae1a4f2090cbdae3。

## harmonyos 条件与证据

适用范围：指南区分API version 15+（多路扫描）与API 14及以前（单路）；未标对应HarmonyOS发行版；version_verified=false，基线未固定
条件：需申请ohos.permission.ACCESS_BLUETOOTH（正文明示）；API 15+为BleScanner多路扫描；API 14及以前仅单路；扫描消耗蓝牙硬件资源与功耗，不再需要时须主动停止
缺口：未读js-apis-bluetooth-ble参考中ScanReport/ScanOptions字段语义正文，interval是否为上报间隔未核实；未读到批量交付的节能意图或硬件offload说明；harmonyos-2属星闪(NearLink，起始版本26.0.0)而非BLE，不构成本节点证据
真机分类理由：数组回调是否真实聚合多条结果、触发时机与功耗收益均未文档化，需真机观察交付粒度与节奏方可确认映射；具体用例留待精研

- [查找设备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ble-development-guide)，查找设备: API 15+扫描方式，on('BLEDeviceFind')回调参数为ble.ScanReport，正文 24–43 行；获取 2026-09-04T09:35:09+00:00；SHA 3ce4e86ba3a2e5d84424810429f8401b638ad97757d3d6bd83948ab2bcafd65d。
- [查找设备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ble-development-guide)，API 14及以前扫描方式，ble.on('BLEDeviceFind')回调参数为Array<ble.ScanResult>，正文 45–59 行；获取 2026-09-04T09:35:09+00:00；SHA 3ce4e86ba3a2e5d84424810429f8401b638ad97757d3d6bd83948ab2bcafd65d。
- [查找设备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ble-development-guide)，ScanOptions示例含interval/dutyMode/matchMode，指南未解释interval含义，正文 85–90 行；获取 2026-09-04T09:35:09+00:00；SHA 3ce4e86ba3a2e5d84424810429f8401b638ad97757d3d6bd83948ab2bcafd65d。
- [查找设备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ble-development-guide)，停止扫描：扫描流程消耗蓝牙硬件资源并影响功耗，正文 129–131 行；获取 2026-09-04T09:35:09+00:00；SHA 3ce4e86ba3a2e5d84424810429f8401b638ad97757d3d6bd83948ab2bcafd65d。
- [查找设备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ble-development-guide)，完整示例：scanReport.scanResult为数组（有length并按下标取结果），正文 424–431 行；获取 2026-09-04T09:35:09+00:00；SHA 3ce4e86ba3a2e5d84424810429f8401b638ad97757d3d6bd83948ab2bcafd65d。
- [@ohos.nearlink.scan (星闪扫描能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-nearlink-scan)，星闪scan.onDeviceFound回调返回ScanResults[]数组（NearLink非BLE，起始26.0.0），正文 135–141 行；获取 2026-09-05T10:27:41.923311+00:00；SHA 26b516e7ab32f640db28d4ad857026f0c79f928bba92974e4ef01aa1d0356013。

## 待验证差异假设

- programming_model：文档层面扫描结果交付粒度不同：HarmonyOS BLE指南回调签名为数组（Array<ble.ScanResult>，ScanReport.scanResult亦为数组），单次事件可含多条结果；Android指南仅展示onScanResult单条交付且未展示批量回调。这是否为可配置批量交付机制、Android是否另有批量参数，待读API参考核实。；待核：Android ScanSettings/ScanCallback是否存在延迟或批量上报参数（需读API参考）；HarmonyOS数组回调是否真实聚合多条结果及触发时机（interval语义待核）；两平台批量交付（若有）是否以节能为设计目的（需官方明示）。

范围缺口：本节点定义为硬件/系统批量投递扫描结果以节能；三平台冻结源均未读到硬件offload或节能意图的明示说明；Android：ScanSettings/ScanCallback API参考正文不在冻结源中，批量参数与API Level未核实；iOS：Core Bluetooth扫描回调与结果交付正文缺失，无法建立任何映射；HarmonyOS：ScanReport/ScanOptions字段语义需读js-apis-bluetooth-ble参考；星闪文档不适用本BLE节点

后续优先级：P1；三平台冻结源均未明示本节点核心机制（硬件/系统批量投递以节能）：iOS零相关证据，Android缺关键API参考，HarmonyOS映射未确认且interval语义待核——属关键缺口兼高风险映射，优先精研。

逐条引用及原文摘录见同目录 normalized.json。
