# USB主机模式 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

Android 指南直接描述应用级 USB 主机模式（API 12+、硬件相关、需用户授权）；iOS 冻结来源仅 USBDriverKit 驱动级符号目录、无 iOS 适用性标注；HarmonyOS 有 USB 服务术语表与旧 @ohos.usb 主机 API 的 API 9 废弃记录，现行 API 面未覆盖。三条差异假设涉及 API 表面、可用性条件与设备匹配层级。全部 low 置信初判，基线未固定。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | documented_mechanism | direct | 官方指南明示主机模式：设备作为 USB 主机供电并枚举设备；android.hardware.usb 包提供 UsbManager/UsbDevice/UsbDeviceConnection 等类，经 intent-filter 或枚举发现设备，requestPermission 用户授权后进行 bulk/control 传输；支持始于 Android 3.1 (API 12)，最终取决于硬件。 | recommended |
| ios | possible_mapping | indirect | 冻结来源仅为 USBDriverKit 两页符号目录（Registry Property Names、Macros），列出 kUSBHost* 匹配/端口/控制器属性与 entitlement 常量，属系统驱动层资料；无 iOS availability 标注，也无应用级 USB 主机接口正文，不能据此判断 iOS 支持与否。 | unassessed |
| harmonyos | documented_mechanism | indirect | USB 服务开发术语表定义 Host（可为智能手机/平板）/Device/Endpoint/Pipe 与四种传输模式；API diff 显示旧 @ohos.usb 模块主机侧 API（getDevices/connectDevice/requestRight/bulkTransfer 等）及 USB 公共事件废弃自 API 9；现行主机 API 表面未包含在冻结来源。 | recommended |

## android 条件与证据

适用范围：指南正文写明 Android 3.1 (API level 12)+；未固定最新正式版与手机基线，当前 API Level 可见性未核对
条件：设备需具备 USB 主机硬件能力；官方注明支持最终取决于设备硬件；minSdk ≥ API 12；manifest 需声明 android.hardware.usb.host feature；intent-filter 命中可自动获得权限直至设备断开，否则需 requestPermission() 弹窗授权；经 UsbManager 枚举/发现设备，在 UsbDeviceConnection 上 bulkTransfer/controlTransfer 同步或 UsbRequest 异步传输
缺口：未核对启动日最新正式 Android 版本与代表手机机型的主机硬件支持；未读取 UsbManager 等具体 API 参考页核实当前 API Level 的可见性与签名变更；后台/生命周期维度（后台访问限制等）未在本两篇指南正文覆盖
真机分类理由：官方明示主机模式支持最终取决于设备硬件，正式确认需在代表手机上实测；本轮为静态文档初判，未执行任何实测。

- [USB host overview](https://developer.android.com/develop/connectivity/usb/host)，USB host overview 开篇：主机模式下设备作为主机、供电并枚举设备，Android 3.1+ 支持，正文 3–4 行；获取 2026-09-05T10:24:24.592107+00:00；SHA 0868a2e76353e7c86a6652d42ba51ac12d0735b14d4218ddbdc35f7a3e798002。
- [USB host overview](https://developer.android.com/develop/connectivity/usb/host)，Table 1. USB Host APIs：UsbManager/UsbDevice/UsbInterface/UsbEndpoint/UsbDeviceConnection/UsbRequest/UsbConstants，正文 13–21 行；获取 2026-09-05T10:24:24.592107+00:00；SHA 0868a2e76353e7c86a6652d42ba51ac12d0735b14d4218ddbdc35f7a3e798002。
- [USB host overview](https://developer.android.com/develop/connectivity/usb/host)，Android manifest requirements：uses-feature android.hardware.usb.host、minSdk 12、USB_DEVICE_ATTACHED intent-filter 与 meta-data，正文 28–42 行；获取 2026-09-05T10:24:24.592107+00:00；SHA 0868a2e76353e7c86a6652d42ba51ac12d0735b14d4218ddbdc35f7a3e798002。
- [USB host overview](https://developer.android.com/develop/connectivity/usb/host)，Obtain permission to communicate with a device：通信前必须有用户权限，未获授权将运行时报错，正文 222–235 行；获取 2026-09-05T10:24:24.592107+00:00；SHA 0868a2e76353e7c86a6652d42ba51ac12d0735b14d4218ddbdc35f7a3e798002。
- [USB host and accessory overview](https://developer.android.com/develop/connectivity/usb)，USB accessory 与 host 模式自 Android 3.1 (API level 12) 起直接支持，正文 34–36 行；获取 2026-09-05T10:24:23.812131+00:00；SHA 2ca38dc2f30b309efbc89f30641b788fecf2abc1c08a94c92fd0f28e93dd538c。
- [USB host and accessory overview](https://developer.android.com/develop/connectivity/usb)，Note：host/accessory 支持最终取决于设备硬件，可用 uses-feature 过滤，正文 40–43 行；获取 2026-09-05T10:24:23.812131+00:00；SHA 2ca38dc2f30b309efbc89f30641b788fecf2abc1c08a94c92fd0f28e93dd538c。

## ios 条件与证据

适用范围：两页符号目录均无版本/平台标注（页脚仅版权信息）；USBDriverKit 的 iOS 适用性与最低版本未核对
条件：来源为 USBDriverKit 驱动扩展层符号目录，非面向普通应用的主机模式 API 指南；符号页无 iOS availability 元数据，iOS 适用性未核对，目录可能面向 macOS 驱动开发；内容涉及主机匹配、端口、集线器、主机控制器注册表属性及 entitlement 常量，偏系统驱动开发
缺口：缺少 iOS 应用级 USB 主机模式官方正文（ExternalAccessory/MFi 等均未入冻结来源）；USBDriverKit 各符号的 iOS availability 未核对，不能推断 iOS 支持/不支持；驱动级机制与普通应用可用能力的边界（entitlement 门槛）未查证
真机分类理由：当前证据不足以确定 iOS 是否存在应用级主机模式接口，无法评估真机验证的必要性与可行性；需先补官方文档证据再评估。

- [Registry Property Names](https://developer.apple.com/documentation/usbdriverkit/registry-property-names)，Services：kIOUSBHostDeviceClassName/kIOUSBHostInterfaceClassName 符号条目，正文 7–11 行；获取 2026-09-05T10:28:04.869653+00:00；SHA 6af4706ff53e0c8f06336862591af5077dad44dbb3a1682301f9d7bfadf4f4b1。
- [Registry Property Names](https://developer.apple.com/documentation/usbdriverkit/registry-property-names)，Host Matching Properties：kUSBHostMatchingPropertyVendorID/ProductID/DeviceClass/ProductIDMask/ProductIDArray 等注册表匹配属性，正文 13–43 行；获取 2026-09-05T10:28:04.869653+00:00；SHA 6af4706ff53e0c8f06336862591af5077dad44dbb3a1682301f9d7bfadf4f4b1。
- [Registry Property Names](https://developer.apple.com/documentation/usbdriverkit/registry-property-names)，Host Properties：kUSBHostPropertyForcePower/LocationID/WakePowerSupply/BusCurrentPoolID 等，正文 45–65 行；获取 2026-09-05T10:28:04.869653+00:00；SHA 6af4706ff53e0c8f06336862591af5077dad44dbb3a1682301f9d7bfadf4f4b1。
- [USBDriverKit Macros](https://developer.apple.com/documentation/usbdriverkit/usbdriverkit-macros)，Macros：IOUSBHostFamilyBit/iokit_usbhost_err 等，及 kIOUSBBillboardEntitlement/kIOUSBHostVMEntitlement/kIOUSBTransportDextEntitlement 等 entitlement 常量，正文 5–49 行；获取 2026-09-05T10:28:05.366444+00:00；SHA 293b8c2b40a237a84c0907d38a3ea1f2aaeed1957cc449e5060deae5d01df713。

## harmonyos 条件与证据

适用范围：diff 正文未标明所属发行版与新旧版本对，仅显示废弃自 API 9；对应 HarmonyOS/OpenHarmony 具体版本未核实
条件：术语表属 USB 服务开发文档，描述主机/设备/端点/管道与传输机制（Host 可为智能手机、平板）；旧 @ohos.usb 主机侧 API（getDevices/connectDevice/hasRight/requestRight/claimInterface/controlTransfer/bulkTransfer/closePipe 等）标记废弃自 API 9；COMMON_EVENT_USB_DEVICE_ATTACHED/DETACHED 等公共事件同标废弃自 API 9；现行替代 API 的权限模型、版本与设备条件未知（冻结来源未含）
缺口：缺少当前 HarmonyOS 版本 USB 主机模式开发指南与现行 API 参考（替代 @ohos.usb 的新表面）正文；diff 页未标明发行版与版本对，需核实其对应 HarmonyOS/OpenHarmony 版本；现行权限模型（requestRight 的替代）与手机/平板设备条件未核实
真机分类理由：旧 API 已废弃、现行表面未读，正式确认需在 HarmonyOS 手机上核实现行主机 API 与硬件支持；本轮为文档初判，未实测。

- [USB服务开发术语](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/usb-glossary)，Host（主机）定义：控制和管理 USB 总线的设备，如 PC 机、智能手机、平板等，正文 37–39 行；获取 2026-09-04T09:35:09+00:00；SHA c3ae6d18ab988ad2300c2c07cbcc1a7a018c27c1a33e9630d2212e8eda4d0541。
- [USB服务开发术语](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/usb-glossary)，Endpoint（端点）：设备与主机间数据传输逻辑终点，IN/OUT 方向，正文 31–33 行；获取 2026-09-04T09:35:09+00:00；SHA c3ae6d18ab988ad2300c2c07cbcc1a7a018c27c1a33e9630d2212e8eda4d0541。
- [USB服务开发术语](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/usb-glossary)，USBConfiguration（配置）：功能集合包含 Interface/Endpoint，同一时间仅激活一个配置，正文 71–75 行；获取 2026-09-04T09:35:09+00:00；SHA c3ae6d18ab988ad2300c2c07cbcc1a7a018c27c1a33e9630d2212e8eda4d0541。
- [Basic Services Kit](https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-basicserviceskit-hdc)，API废弃版本变更：usb.getDevices/connectDevice/hasRight/requestRight 废弃自 API 9（api/@ohos.usb.d.ts），正文 293–296 行；获取 2026-09-05T11:01:20.129458+00:00；SHA cd7d32de8beb58705509333a25586045304d5124ce968dd2b84d3f225e330f88。
- [Basic Services Kit](https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-basicserviceskit-hdc)，API废弃版本变更：claimInterface/releaseInterface/setConfiguration/setInterface/controlTransfer/bulkTransfer/closePipe 废弃自 API 9，正文 297–305 行；获取 2026-09-05T11:01:20.129458+00:00；SHA cd7d32de8beb58705509333a25586045304d5124ce968dd2b84d3f225e330f88。
- [Basic Services Kit](https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-basicserviceskit-hdc)，API废弃版本变更：COMMON_EVENT_USB_DEVICE_ATTACHED/DETACHED 公共事件废弃自 API 9（api/@ohos.commonEvent.d.ts），正文 135–136 行；获取 2026-09-05T11:01:20.129458+00:00；SHA cd7d32de8beb58705509333a25586045304d5124ce968dd2b84d3f225e330f88。

## 待验证差异假设

- api_surface：应用级主机 API 表面：Android 自 API 12 起提供类模型（UsbManager/UsbDevice/UsbDeviceConnection/UsbRequest）；HarmonyOS 旧 @ohos.usb 函数式主机 API（getDevices/connectDevice/bulkTransfer 等）标记废弃自 API 9，现行表面与形态待查，两端接口组织方式可能不同。；待核：HarmonyOS 现行主机 API（如替代 @ohos.usb 的新模块）的形态、所属 Kit 与版本适用范围；废弃 API 在当前 HarmonyOS 手机上是否仍可调用；两端在异步/等时传输等能力上的对应关系未核对。
- availability：可用性条件：Android 官方明示主机模式支持最终取决于设备硬件并要求 manifest uses-feature 声明；iOS 冻结来源仅有 USBDriverKit 驱动级符号目录且无 iOS availability 标注，应用级主机可用性未知，两平台可用的条件层级不同。；待核：iOS 是否存在面向普通应用的主机模式接口（需补 ExternalAccessory 等官方正文）；USBDriverKit 符号的 iOS availability 与 entitlement 门槛；iPhone/iPad 对 USB 配件主机模式的官方支持口径。
- programming_model：设备识别/匹配机制层级：Android 在应用层以 intent-filter + XML 资源（vendor-id/product-id/class/subclass/protocol）过滤 USB 设备；Apple USBDriverKit 在驱动注册表层以 kUSBHostMatchingProperty* 属性匹配，层级与使用者不同，映射关系待确认。；待核：iOS 应用层是否存在等价的设备过滤/附件通知机制；匹配属性集合差异（ProductIDMask/ProductIDArray 等）在 Android 侧的对应项；驱动级匹配机制能否被 iOS 普通应用利用。

范围缺口：iOS 应用级 USB 主机模式无冻结来源正文，本轮无法建立支持判断（unknown 方向保留）；HarmonyOS 现行主机 API 表面与开发指南缺失，仅能确认历史 @ohos.usb API 废弃自 API 9；Android 未做具体 API 参考页与最新正式版本基线核对；三平台手机基线未固定，所有结论为 low 置信 first_pass 初判

后续优先级：P1；iOS 应用级接口证据缺失与 HarmonyOS 现行 API 面缺失属关键缺口/高风险映射，需优先补读三平台现行官方文档；Android 侧条件较清晰但仍需基线核对后再评估真机验证。

逐条引用及原文摘录见同目录 normalized.json。
