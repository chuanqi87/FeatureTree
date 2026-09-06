# 音频输出路由 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

三平台均读到输出路由机制：Android 为系统输出切换器+AndroidX MediaRouter（选择）与 getRoutedDevice()/OnRoutingChangedListener（查询监听，TV 指南）；iOS 仅读到无版本标注的 AudioToolbox 旧常量（听筒/扬声器覆盖与路由类型枚举）；HarmonyOS 为 AudioRoutingManager 查询监听加 API 20 AudioSessionManager 默认设备设置与含变更原因事件。首轮初判置信度全 low；缺口：iOS 现代 AVAudioSession、Android 手机场景选择 API、HarmonyOS 发行版对应与权限。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | documented_mechanism | direct | 读到选择与监听两组机制：系统输出切换器（Android 11 起，默认列本机扬声器与蓝牙，应用可经 MediaRouter 自定义选项）；AudioTrack.getRoutedDevice() 查询当前路由设备，OnRoutingChangedListener(API 24+)/AudioDeviceCallback(API 23) 监听变化并重建音轨。正文偏远程投播与 Android TV 场景。 | recommended |
| ios | documented_mechanism | direct | 读到 AudioToolbox 旧音频会话机制：PlayAndRecord 类别默认输出听筒，可用 kAudioSessionOverrideAudioRoute_Speaker 覆盖为扬声器；Audio Output Routes 枚举当前路由值（耳机/蓝牙HFP/A2DP/听筒/扬声器/USB/HDMI/AirPlay/LineOut）。页面自称面向 iOS 设备但无版本标注，未读到变化监听与现代选择机制。 | recommended |
| harmonyos | documented_mechanism | direct | AudioRoutingManager 支持查询输出设备（getDevices/OUTPUT_DEVICES_FLAG）、监听 deviceChange 与最高优先级输出设备变化；API 20 起 AudioSessionManager 可设/查本机默认输出设备并监听 currentOutputDeviceChanged（含变更原因与推荐操作）。类型表覆盖听筒/扬声器/有线/蓝牙 SCO/A2DP/USB/星闪。 | recommended |

## android 条件与证据

适用范围：AndroidX MediaRouter 兼容 Android 2.3 (API 9)+；输出切换器 Android 11+；监听方案分 API 21-22/23/24+；直接回放能力查询分 API 23/29/31/33+；未绑定单一最新 SDK 版本，启动日基线未核实
条件：AndroidX MediaRouter 库声称兼容 Android 2.3 (API 9)+，实际远程路由依赖 MediaRouteProvider/Cast 等生态接入；系统输出切换器自 Android 11 起出现在系统媒体播放器，默认列出本机扬声器与已连接蓝牙音频设备；路由/设备监听按 API 级别分层：API 24+ OnRoutingChangedListener、API 23 AudioDeviceCallback、API 21-22 HDMI 插播广播与蓝牙广播；audio-capabilities 指南面向 Android TV 场景（HDMI/家庭影院），手机适用性未在该文核实；isDirectPlaybackSupport() 在 API 33 前会考虑未激活输出路径，API 33+ 仅考虑当前激活路由
缺口：未读手机场景输出设备程序化选择 API 参考（setPreferredDevice/setCommunicationDevice 等），应用能否指定具体输出设备未证实；已读监听与重建流程出自 Android TV 指南，手机/平板行为是否一致未核实；系统 SDK(android.media) 与 AndroidX MediaRouter/Cast 的职责边界及权限要求未在已读正文核对；启动日最新正式版 API level 基线未固定，不能推断最新版本行为
真机分类理由：机制存在性由静态文档确认；路由实际行为（输出切换器 UX、蓝牙/HDMI 热插拔回调时机）依赖真机与外设，后续精研建议真机验证，但非本轮必需

- [Routing between devices](https://developer.android.com/media/routing)，MediaRouter support library — AndroidX MediaRouter 定义与 API 9+ 兼容声明，正文 28–42 行；获取 2026-09-05T10:34:03.777638+00:00；SHA 0ff572490f79345e16f4e1225c3f4f8fa107c7c43f1fc3d63a21942d0e4f1ad3。
- [Routing between devices](https://developer.android.com/media/routing)，The output switcher — Android 11 起系统输出切换器、默认选项与应用自定义路由选项，正文 43–65 行；获取 2026-09-05T10:34:03.777638+00:00；SHA 0ff572490f79345e16f4e1225c3f4f8fa107c7c43f1fc3d63a21942d0e4f1ad3。
- [Audio capabilities](https://developer.android.com/training/tv/playback/audio-capabilities)，Create a track with the right format — AudioTrack 创建后调用 getRoutedDevice() 确定默认输出设备，正文 31–37 行；获取 2026-09-05T10:38:51.192367+00:00；SHA c43a928604ae9d14079f3b9a052dc586da2c0d0437dfeb572e09873fe69f7c1d。
- [Audio capabilities](https://developer.android.com/training/tv/playback/audio-capabilities)，Intercept audio device changes — 按 API 级别的设备变化监听方案（24+/23/21-22），正文 208–225 行；获取 2026-09-05T10:38:51.192367+00:00；SHA c43a928604ae9d14079f3b9a052dc586da2c0d0437dfeb572e09873fe69f7c1d。

## ios 条件与证据

适用范围：已读 AudioToolbox 常量页面未标注任何 iOS 版本可用性或弃用信息；适用 iOS 版本范围未核实，不能推断为最新 iOS 行为
条件：kAudioSessionOverrideAudioRoute_* 覆盖仅作用于 kAudioSessionCategory_PlayAndRecord 类别，且为听筒/扬声器二选一；Audio Output Routes 字符串用作 kAudioSession_AudioRouteKey_Outputs 数组中 kAudioSession_AudioRouteKey_Type 的取值，用于描述当前路由；两页均为 AudioToolbox 音频会话 API 文档，未标注 iOS 版本可用性或弃用状态；页面文字自称面向 iOS 设备（an iOS device），无 availability 元数据佐证具体版本
缺口：现代 AVAudioSession 正文（currentRoute、routeChangeNotification、overrideOutputAudioPort、defaultToSpeaker 等）未读，现代监听与选择机制未证实；已读页面无版本可用性/弃用标注，AudioToolbox 常量在当前 iOS 的适用性未核实；Apple 文档含多平台内容，虽页面自称 iOS 设备，但未做逐符号 availability 核对；听筒/扬声器覆盖之外的选择能力（如指定蓝牙/USB 输出）在已读正文缺失
真机分类理由：已读常量属旧音频会话 API 且无版本标注，其在当前 iOS 真机上的可用性与现代 AVAudioSession 等价行为需运行验证；本轮仅静态初判

- [Audio Session Category Route Overrides](https://developer.apple.com/documentation/audiotoolbox/1618372-audio-session-category-route-ove)，Discussion/Constants — PlayAndRecord 默认听筒与 kAudioSessionOverrideAudioRoute_Speaker 扬声器覆盖，正文 3–19 行；获取 2026-09-05T10:43:04.637471+00:00；SHA 966bf4c8a9a8e9c0cd70bb6e9487848329c7a2f324ee27db27fc2985e2623033。
- [Audio Output Routes](https://developer.apple.com/documentation/audiotoolbox/audio-output-routes)，Discussion — iOS 设备输出路由值用于 kAudioSession_AudioRouteKey_Outputs，正文 1–8 行；获取 2026-09-05T10:44:12.152355+00:00；SHA 9f241ad895346346a7645df613f14d28d10011d88eeaffc1c5667fd428034312。
- [Audio Output Routes](https://developer.apple.com/documentation/audiotoolbox/audio-output-routes)，Constants — 输出路由类型枚举（LineOut/Headphones/BluetoothHFP/BluetoothA2DP/BuiltInReceiver/BuiltInSpeaker/USBAudio/HDMI/AirPlay），正文 11–47 行；获取 2026-09-05T10:44:12.152355+00:00；SHA 9f241ad895346346a7645df613f14d28d10011d88eeaffc1c5667fd428034312。

## harmonyos 条件与证据

适用范围：AudioRoutingManager 查询/监听接口锚点示 API 9/10 起；AudioSessionManager 输出设备管理自 API version 20 起；对应 HarmonyOS 商用发行版未在已读正文标注，最新正式版未核实
条件：AudioRoutingManager 为主体机制：getDevices(OUTPUT_DEVICES_FLAG)、on('deviceChange')、getPreferOutputDeviceForRendererInfo 及对应监听；AudioSessionManager 输出设备管理（setDefaultOutputDevice/getDefaultOutputDevice/currentOutputDeviceChanged）自 API version 20 起；应用级 setDefaultOutputDevice 会覆盖 AudioRenderer 的 setDefaultOutputDevice 设置，取消需传 audio.DeviceType.DEFAULT 交还系统；deviceChange 为全量设备连接变化监听，文档不建议作为应用自动暂停依据，应按输出设备变更原因处理；支持的输出设备类型表含 EARPIECE/SPEAKER/WIRED_HEADSET/WIRED_HEADPHONES/BLUETOOTH_SCO/BLUETOOTH_A2DP/USB_HEADSET/NEARLINK(星闪)
缺口：API 9/10/20 对应的 HarmonyOS 商用发行版与手机/平板基线未在已读正文标注，最新正式版未核实；已读段落未出现权限要求说明（蓝牙/USB/星闪设备可见性是否需要权限）；AudioRenderer.setDefaultOutputDevice 等流级选择接口正文未读，与 AudioSession 级覆盖关系细节待核；NEARLINK(星闪) 等类型的实际可路由设备范围与真机行为未验证
真机分类理由：机制文档较完整，但 API 20 输出设备管理在不同 HarmonyOS 版本与真机外设（蓝牙/有线/星闪）上的实际切换行为未验证；行为确认建议真机，非本轮必需

- [查询和监听音频输出设备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-output-device-management)，引言 — 两种输出设备管理方式；AudioSessionManager 自 API version 20 提供部分输出设备管理接口，正文 3–8 行；获取 2026-09-04T09:35:09+00:00；SHA fa27296f4926a8a33df0a19bd42b8905477a7f7e1f2e21eed34dda86e19ef00b。
- [查询和监听音频输出设备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-output-device-management)，支持的音频输出设备类型 — 类型与取值表，正文 26–39 行；获取 2026-09-04T09:35:09+00:00；SHA fa27296f4926a8a33df0a19bd42b8905477a7f7e1f2e21eed34dda86e19ef00b。
- [查询和监听音频输出设备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-output-device-management)，监听设备连接状态变化 — deviceChange 全量监听及不建议作自动暂停依据，正文 60–64 行；获取 2026-09-04T09:35:09+00:00；SHA fa27296f4926a8a33df0a19bd42b8905477a7f7e1f2e21eed34dda86e19ef00b。
- [查询和监听音频输出设备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-output-device-management)，获取最高优先级输出设备信息 — getPreferOutputDeviceForRendererInfo，正文 84–88 行；获取 2026-09-04T09:35:09+00:00；SHA fa27296f4926a8a33df0a19bd42b8905477a7f7e1f2e21eed34dda86e19ef00b。
- [查询和监听音频输出设备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-output-device-management)，设置本机默认音频输出设备 — setDefaultOutputDevice 覆盖与取消语义，正文 156–162 行；获取 2026-09-04T09:35:09+00:00；SHA fa27296f4926a8a33df0a19bd42b8905477a7f7e1f2e21eed34dda86e19ef00b。
- [查询和监听音频输出设备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-output-device-management)，监听输出设备变化 — currentOutputDeviceChanged 事件含变更原因及推荐后续操作，正文 228–232 行；获取 2026-09-04T09:35:09+00:00；SHA fa27296f4926a8a33df0a19bd42b8905477a7f7e1f2e21eed34dda86e19ef00b。

## 待验证差异假设

- programming_model：应用侧选择输出设备的编程模型可能不同：Android 读到系统输出切换器（Android 11 起用户主导，应用经 MediaRouter 自定义选项）；iOS 读到的 AudioToolbox 常量仅支持 PlayAndRecord 类别听筒/扬声器二选一覆盖；HarmonyOS 提供 AudioSessionManager.setDefaultOutputDevice（API 20+）设置应用级默认输出设备并覆盖渲染器级设置。三者选择粒度、入口与持久性待精研确认。；待核：iOS 现代 AVAudioSession（defaultToSpeaker、overrideOutputAudioPort 等）是否提供等价或更强的选择能力未读正文；Android 应用能否经系统 API 程序化指定具体输出设备（setPreferredDevice/setCommunicationDevice）未读正文；HarmonyOS 应用级默认设备跨 activateAudioSession 生效的语义与 iOS/Android 会话级覆盖如何对应未比较。
- limits_precision：输出路由变化事件的信息粒度可能不同：HarmonyOS currentOutputDeviceChanged 事件携带 changeReason（设备不可用/新设备可用/强选/会话激活/更高优先级流等）及系统推荐后续操作，且文档明示 deviceChange 全量监听不宜作自动暂停依据；Android 读到的 OnRoutingChangedListener/AudioDeviceCallback 回调路由或设备列表变化，应用需自行重建音轨且可能在回调前出错。变更原因语义与推荐行为粒度差异待核。；待核：iOS 路由变化通知（如 AVAudioSession routeChangeNotification 的 reason）未读正文，无法三方比较；Android 更高版本 API 是否提供携带原因的路由变化事件未核实；HarmonyOS 各 changeReason 的实际触发条件与真机行为未验证。
- api_surface：可枚举的输出设备类型集合可能不同：iOS 路由值含 AirPlay、HDMI、LineOut、USB（30-pin）等；HarmonyOS 类型表含听筒、扬声器、有线耳机（带/不带麦克风）、蓝牙 SCO/A2DP、USB 耳机及星闪（NEARLINK=31）；Android 已读正文仅列输出切换器默认项（本机扬声器、已连接蓝牙音频）。假设三平台类型常量集与生态（AirPlay/Cast vs 星闪）不同，实际可路由范围待核。；待核：Android AudioDeviceInfo 设备类型全集未读正文，不能据已读片段推断其枚举范围；各类型在实际设备上的可路由性（如 iPad HDMI、星闪耳机、AirPlay 目标）未验证；类型枚举语义是否对齐（如 USBAudio 与 USB_HEADSET、AirPlay 与 Cast 生态差异）未比较。

范围缺口：iOS 未读现代 AVAudioSession 正文，本轮 iOS 结论仅基于无版本标注的 AudioToolbox 旧常量页，存在以旧 API 映射现代行为的风险；Android 未读手机场景输出设备选择 API 参考与权限条件，已读监听指南面向 Android TV；HarmonyOS API 9/10/20 与具体商用发行版（含手机/平板基线）对应未标注，权限要求未在已读段落出现；三平台启动日最新正式版基线均未固定（version_baseline unresolved），本包结论不构成最新版本支持判断；harmonyos-2 为音频调试快照文档（API 26.0.0 起，仅供人工调试），不作为输出路由管理机制证据；真机路由行为未验证

后续优先级：P1；iOS 证据全部来自无版本标注的旧 AudioToolbox 页面，存在以旧 API 映射现代 iOS 行为的高风险；Android 缺手机场景程序化选择 API 正文；HarmonyOS API 版本与发行版对应及权限未核实。这些关键缺口直接影响编程模型与 api_surface 比较结论，需优先精研。

逐条引用及原文摘录见同目录 normalized.json。
