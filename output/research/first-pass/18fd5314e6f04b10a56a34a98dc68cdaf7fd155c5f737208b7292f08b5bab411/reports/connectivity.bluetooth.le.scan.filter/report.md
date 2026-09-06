# BLE扫描过滤 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

三平台均读到文档化BLE扫描过滤机制：Android ScanFilter(API 21+，UUID/名称/MAC/服务数据/厂商数据+mask组合，API 33增广播数据类型过滤)；HarmonyOS ble.ScanFilter(字段+mask+rssiThreshold，明示硬件过滤匹配模式与全系统共享过滤器配额)；iOS读文仅见scanForPeripherals按服务UUID扫描。过滤执行位置三平台静态文档均未完整说明，iOS过滤面宽度是最大缺口；均为初判low。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | documented_mechanism | direct | 官方ScanFilter(API 21起)以Builder组合过滤条件：服务UUID(+mask)、设备名、MAC、service data(+mask)、manufacturer data(+mask)等，API 33增加广播数据类型/数据/mask getter；指南确认startScan(List<ScanFilter>,ScanSettings,ScanCallback)限制扫描目标。 | recommended |
| ios | documented_mechanism | indirect | CBCentralManager页列出scanForPeripherals(withServices:options:)按所广播服务扫描并配套Peripheral Scanning Options键；示例文章按服务UUID数组发起扫描并在回调中匹配。读文未显示名称/MAC/厂商数据/RSSI等扫描期过滤字段。 | recommended |
| harmonyos | documented_mechanism | direct | ble.startBLEScan/BleScanner.startScan接收ScanFilter数组：deviceId/address(23+)、name、serviceUuid(+mask)、serviceSolicitationUuid(+mask)、serviceData(+mask)、manufactureId/data(+mask)、rssiThreshold(23+)；matchMode标注为硬件的过滤匹配模式，过滤器资源全系统应用共享。 | recommended |

## android 条件与证据

适用范围：Android系统SDK：ScanFilter及基础过滤字段自API 21起，getAdvertisingData/getAdvertisingDataMask等广播数据相关getter标注API 33起；启动日最新API Level未核对。
条件：基础过滤字段需API level 21+，广播数据类型相关getter需API 33+；蓝牙需已启用，否则getBluetoothLeScanner()返回null(指南注记)；同一时间只能扫描BLE或经典蓝牙之一，不能同时进行
缺口：过滤执行位置(蓝牙控制器/协议栈/框架层)在读过的两篇正文中均未说明；扫描所需运行时权限(如BLUETOOTH_SCAN类)未在读文正文出现，未核对；matches()本地判断与系统扫描过滤的组合语义未读；最新API Level及生态侧(如AndroidX/Play services)替代方案未核对
真机分类理由：过滤执行位置、mask匹配语义及不同芯片回退行为在读文档未覆盖，节点定义中的执行位置与结果语义需真机验证。

- [ScanFilter](https://developer.android.com/reference/android/bluetooth/le/ScanFilter)，ScanFilter类页顶部：Added in API level 21，正文 3–3 行；获取 2026-09-05T10:15:50.957098+00:00；SHA f708ed450c66bbc3093a6f6dffdfe3117ea2ce352deea39caa16100d8b7695b8。
- [ScanFilter](https://developer.android.com/reference/android/bluetooth/le/ScanFilter)，ScanFilter类说明与支持的过滤字段列表(服务UUID/名称/MAC/服务数据/厂商数据/广播数据类型)，正文 39–42 行；获取 2026-09-05T10:15:50.957098+00:00；SHA f708ed450c66bbc3093a6f6dffdfe3117ea2ce352deea39caa16100d8b7695b8。
- [ScanFilter](https://developer.android.com/reference/android/bluetooth/le/ScanFilter)，Public methods表：各mask getter、getServiceSolicitationUuidMask、matches(ScanResult)，正文 70–92 行；获取 2026-09-05T10:15:50.957098+00:00；SHA f708ed450c66bbc3093a6f6dffdfe3117ea2ce352deea39caa16100d8b7695b8。
- [ScanFilter](https://developer.android.com/reference/android/bluetooth/le/ScanFilter)，getAdvertisingData：Added in API level 33，正文 189–205 行；获取 2026-09-05T10:15:50.957098+00:00；SHA f708ed450c66bbc3093a6f6dffdfe3117ea2ce352deea39caa16100d8b7695b8。
- [Find BLE devices](https://developer.android.com/develop/connectivity/bluetooth/ble/find-ble-devices)，startScan(List<ScanFilter>,ScanSettings,ScanCallback)用过滤器列表限制扫描目标，正文 84–89 行；获取 2026-09-05T09:34:20.942633+00:00；SHA 054735bff9d159c01230ee1c49befcabfb5998fadf842a227d0b8fb196d8328b。
- [Find BLE devices](https://developer.android.com/develop/connectivity/bluetooth/ble/find-ble-devices)，Note：蓝牙未启用时getBluetoothLeScanner()返回null，正文 76–82 行；获取 2026-09-05T09:34:20.942633+00:00；SHA 054735bff9d159c01230ee1c49befcabfb5998fadf842a227d0b8fb196d8328b。

## ios 条件与证据

适用范围：CoreBluetooth(Apple平台目录)：本快照正文无availability元数据，iOS适用版本未确认，不能默认目录内容全部适用iOS；启动日最新iOS版本未核对。
条件：调用CBCentralManager方法前状态须为poweredOn(中央设备支持BLE且蓝牙可用)；扫描经scanForPeripherals(withServices:options:)进行，读文所示过滤入口为服务UUID参数与扫描选项
缺口：scanForPeripherals(withServices:options:)方法页与Peripheral Scanning Options正文未读，services参数精确语义(如nil行为)未确认；读文未显示名称/MAC/厂商数据等扫描期过滤字段，未检索到不等于不支持；iOS availability未核对(快照无版本元数据，需DocC符号数据)；过滤执行位置与结果语义在读文未说明
真机分类理由：扫描过滤实际覆盖面与services参数行为缺方法页正文，真机验证可补文档缺口并确认结果语义。

- [CBCentralManager](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager)，Overview：poweredOn前不可调用central manager方法，正文 9–13 行；获取 2026-09-05T09:37:28.075444+00:00；SHA bd120cd884675f212e867a2abedf93e30cc55883cfe5b8ce325d112749b30e7a。
- [CBCentralManager](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager)，Scanning or Stopping Scans：scanForPeripherals(withServices:options:)与Peripheral Scanning Options条目，正文 63–71 行；获取 2026-09-05T09:37:28.075444+00:00；SHA bd120cd884675f212e867a2abedf93e30cc55883cfe5b8ce325d112749b30e7a。
- [Measuring distance between devices using Channel Sounding](https://developer.apple.com/documentation/corebluetooth/measuring-distance-between-devices-using-channel-sounding)，示例：按服务UUID扫描scanForPeripherals(withServices:)并在didDiscover回调匹配标识符，正文 114–129 行；获取 2026-09-05T10:19:05.331144+00:00；SHA 5f487d233d657d69e686f035fe7f2ee761b8ed7f3a2c0db6a1f5ddab99f7719c。

## harmonyos 条件与证据

适用范围：HarmonyOS API参考@ohos.bluetooth.ble：ScanFilter多数字段标注元服务API 12起可用，address/rssiThreshold标注API 23+，BleScanner.startScan为15+，ScanOptions.isExtended起始版本26.0.0；未固定具体HarmonyOS发行版基线。
条件：需ohos.permission.ACCESS_BLUETOOTH权限，指导要求运行时requestPermissionsFromUser获取用户授权；仅可在Stage模型下使用；startBLEScan只支持单路扫描，多路需BleScanner(15+)；蓝牙关闭时返回错误码2900003；BleScanner.startScan围栏模式下filters不可为null，且建议单应用过滤器不超过3个否则可能2900009
缺口：哪些过滤字段强制在硬件执行、哪些回退软件过滤未逐条说明；address/rssiThreshold的API 23+对应的具体HarmonyOS正式发行版未固定；OpenHarmony同名ScanFilter字段与HarmonyOS差异未分开核对；未在ScanFilter配置实际MAC地址时返回虚拟MAC地址，对按地址过滤的跨会话稳定性影响需确认
真机分类理由：硬件过滤器配额(≤3建议/2900009)、围栏模式约束与虚拟MAC地址行为均为运行时行为，静态文档不足以确认实际结果语义。

- [@ohos.bluetooth.ble (蓝牙ble模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble)，ble.startBLEScan签名、filters参数(符合过滤条件的设备被保留)、权限与Stage模型约束，正文 288–311 行；获取 2026-09-05T09:34:21.800954+00:00；SHA f1d80db2df10406273b22c90053098e4370a49f6924dd1618d93759c7d19ce2f。
- [@ohos.bluetooth.ble (蓝牙ble模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble)，ScanFilter接口字段定义：deviceId/address23+/name/serviceUuid+mask/serviceSolicitationUuid+mask/serviceData+mask/manufactureId+data+mask/rssiThreshold23+，正文 5775–5797 行；获取 2026-09-05T09:34:21.800954+00:00；SHA f1d80db2df10406273b22c90053098e4370a49f6924dd1618d93759c7d19ce2f。
- [@ohos.bluetooth.ble (蓝牙ble模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble)，BleScanner.startScan15+：过滤器资源为所有应用共享，建议单应用不超过3个，超限返回2900009，正文 5244–5247 行；获取 2026-09-05T09:34:21.800954+00:00；SHA f1d80db2df10406273b22c90053098e4370a49f6924dd1618d93759c7d19ce2f。
- [@ohos.bluetooth.ble (蓝牙ble模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble)，ScanOptions：matchMode为硬件的过滤匹配模式，正文 5807–5814 行；获取 2026-09-05T09:34:21.800954+00:00；SHA f1d80db2df10406273b22c90053098e4370a49f6924dd1618d93759c7d19ce2f。
- [@ohos.bluetooth.ble (蓝牙ble模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble)，ScanResult.deviceId：扫描未在ScanFilter配置实际MAC地址时获取的是虚拟MAC地址，正文 5643–5643 行；获取 2026-09-05T09:34:21.800954+00:00；SHA f1d80db2df10406273b22c90053098e4370a49f6924dd1618d93759c7d19ce2f。
- [广播开发指导](https://developer.huawei.com/consumer/cn/doc/atomic-guides/atomic-bluetooth-advertising)，开发指导：module.json5添加ACCESS_BLUETOOTH权限并经requestPermissionsFromUser获取用户授权，正文 24–26 行；获取 2026-09-05T10:40:21.206677+00:00；SHA bfb2a0ed9cfd4f60953945e725b606000cffd24a1cf39bf26c86e70baa25c7fd。

## 待验证差异假设

- api_surface：扫描期过滤条件丰富度可能不同：Android ScanFilter与HarmonyOS ble.ScanFilter均文档化UUID(+mask)/名称/地址/服务数据/厂商数据等多类条件，iOS读到的CBCentralManager页仅显示scanForPeripherals按服务UUID过滤加扫描选项，未显示名称/MAC/厂商数据字段。假设iOS扫描期官方过滤面较窄(can差异)，待方法页正文核实，不据此断言不支持。；待核：iOS scanForPeripherals方法页与Peripheral Scanning Options正文未读，services参数nil行为及是否有其他过滤键未确认；Android/HarmonyOS各字段实际生效与组合条件未实测验证。
- limits_precision：过滤执行位置与资源模型可能不同：HarmonyOS明示matchMode为硬件的过滤匹配模式，且过滤器资源为所有应用共享、单应用建议不超过3个否则2900009；Android两篇读文只描述过滤条件未说明执行位置或数量上限；iOS读文同样未说明。假设HarmonyOS文档化硬件过滤与共享配额而Android/iOS在读资料中未明示(未明示不等于无此机制)。；待核：Android ScanFilter是否卸载到蓝牙控制器执行，需BluetoothLeScanner/ScanSettings或AOSP文档核实；iOS系统栈过滤执行位置未读；HarmonyOS各过滤字段是否全部硬件执行、软件回退行为未说明。
- api_surface：扫描期RSSI门限过滤能力可能不同：HarmonyOS ScanFilter提供rssiThreshold(API 23+)按信号强度过滤广播报文；Android读到的ScanFilter方法与字段列表无RSSI条件；iOS读文无RSSI过滤入口。假设HarmonyOS有文档化的扫描期RSSI门限过滤，Android/iOS是否具备等价能力在读资料中未证明(不能推出不支持)。；待核：Android/iOS是否经其他API提供扫描期RSSI过滤未检索；HarmonyOS rssiThreshold标注API 23+对应的具体发行版本未固定。

范围缺口：Android BluetoothLeScanner/ScanSettings正文未读，过滤执行位置与硬件卸载语义未覆盖；iOS scanForPeripherals(withServices:options:)方法页、Peripheral Scanning Options与didDiscover回调正文未读；三平台启动日最新正式版与手机基线未固定，iOS符号availability未核对；OpenHarmony与HarmonyOS发行版的ScanFilter字段差异未分开核对；harmonyos-2为广播/扫描入门指导，不含过滤字段细节，仅用于权限授权流程佐证

后续优先级：P1；iOS扫描过滤面宽度缺方法页正文即存在高风险映射，且节点定义要求的过滤执行位置与结果语义在三平台静态文档均未完整覆盖，属关键缺口，精研应优先补读方法页并固定版本基线。

逐条引用及原文摘录见同目录 normalized.json。
