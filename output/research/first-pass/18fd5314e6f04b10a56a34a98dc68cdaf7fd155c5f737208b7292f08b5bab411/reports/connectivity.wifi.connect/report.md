# Wi-Fi连接建议 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

Android读到Wi-Fi建议API（Android 10+，应用提交建议、平台最终决定，按应用审批，建议不入保存网络列表）；HarmonyOS读到STA候选网络机制（addCandidateConfig+connectToCandidateConfig，需STA能力与GET/SET_WIFI_INFO权限，版本未注明）；iOS两篇冻结来源（Siri事件建议Markup、Wi-Fi Aware点对点配对）均未建立本节点机制。差异假设集中于连接决策归属、审批权限模型与API用例面。全部low，版本基线未固定。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | documented_mechanism | direct | 官方指南明示建议API：应用提交WifiNetworkSuggestion供设备自动连接，平台最终决定接受哪个接入点；建议不是保存网络；按应用（非按网络）用户审批，首次建议触发通知/对话框，用户拒绝即移除CHANGE_WIFI_STATE；Android 11/12增加Passpoint、企业安全强制与MAC随机化等分层行为。 | recommended |
| ios | unknown | indirect | 两篇冻结来源均未建立应用建议/协助连接Wi-Fi接入点的机制：ios-1为Siri日历事件建议Markup（与Wi-Fi无关），ios-2为Wi-Fi Aware点对点设备配对连接（非接入点连接建议）。可能对应的NEHotspotConfiguration等文档不在本轮来源内，无法初判iOS是否提供同类能力。 | unassessed |
| harmonyos | documented_mechanism | direct | STA模式开发指南明示应用侧连接机制：addCandidateConfig()添加候选网络配置，connectToCandidateConfig()连接应用自己添加的候选网络，另有移除/查询候选配置与连接状态事件接口；需STA系统能力与GET_WIFI_INFO、SET_WIFI_INFO权限并先使能WLAN。另一篇为code-linter监听默认网络变化规则，与本节点无关。指南未注明API起始版本。 | recommended |

## android 条件与证据

适用范围：指南写明Android 10 (API 29)+提供该API，Android 11/12有行为分层；快照2026-09-05，version_verified=false，启动日最新正式版基线unresolved，未核对当前API Level状态。
条件：平台最终决定接受哪个接入点（综合本应用与其他应用的输入）；建议不是保存网络、不进保存网络页；添加保存网络需ACTION_WIFI_ADD_NETWORKS并逐次用户批准；用户审批按应用而非按网络；首次建议即通知用户，用户拒绝后移除应用CHANGE_WIFI_STATE权限；setIsAppInteractionRequired(true)注释标明需位置权限；EAP-SIM类企业建议仅限运营商签名应用；Android 11+强制TLS企业建议设置CA证书与服务器域名，旧版不安全建议被忽略
缺口：未读WifiNetworkSuggestion/WifiManager等API参考正文，无法核对最新正式版API状态与后台广播约束；启动日最新正式版基线未固定，2026-09-05快照不能证明覆盖当前版本行为；平板设备形态条件未单独核对；用户断开/恢复自动连接的细节仅来自本指南，未经API参考或发布说明交叉核实
真机分类理由：机制与系统UI行为（通知/对话框、Wi-Fi选择器断开、按应用审批、归因显示）均为文档声明，且未固定版本基线，最新正式版手机上的实际表现需后续真机复核；本轮无任何实测。

- [Wi-Fi suggestion API for internet connectivity](https://developer.android.com/develop/connectivity/wifi/wifi-suggest)，Wi-Fi suggestion API介绍：Android 10+应用添加网络凭据供自动连接，平台最终决定；建议非保存网络，正文 3–14 行；获取 2026-09-05T10:24:27.826446+00:00；SHA 8cb054e421e109667304d83425fe6974d353f8e49ae7298121bed348f67625d3。
- [Wi-Fi suggestion API for internet connectivity](https://developer.android.com/develop/connectivity/wifi/wifi-suggest)，Android 11/12行为分层：Passpoint建议、TLS企业安全强制、运营商签名EAP-SIM、非持久MAC随机化，正文 16–46 行；获取 2026-09-05T10:24:27.826446+00:00；SHA 8cb054e421e109667304d83425fe6974d353f8e49ae7298121bed348f67625d3。
- [Wi-Fi suggestion API for internet connectivity](https://developer.android.com/develop/connectivity/wifi/wifi-suggest)，首次建议的用户通知按版本区分对话框/通知，连接后设置中显示归因文本，正文 197–208 行；获取 2026-09-05T10:24:27.826446+00:00；SHA 8cb054e421e109667304d83425fe6974d353f8e49ae7298121bed348f67625d3。
- [Wi-Fi suggestion API for internet connectivity](https://developer.android.com/develop/connectivity/wifi/wifi-suggest)，用户拒绝建议通知移除CHANGE_WIFI_STATE权限，可在设置的Wi-Fi控制菜单恢复，正文 220–226 行；获取 2026-09-05T10:24:27.826446+00:00；SHA 8cb054e421e109667304d83425fe6974d353f8e49ae7298121bed348f67625d3。
- [Wi-Fi infrastructure overview](https://developer.android.com/develop/connectivity/wifi/wifi-infrastructure)，Android 10+ Wi-Fi基础设施含建议API、网络请求API与Settings Intent API三种，正文 3–7 行；获取 2026-09-05T10:24:26.486575+00:00；SHA 0fb895414a288c359f762001a71675718110dbe06cc2eff3cd958e3bcb2c7556。
- [Wi-Fi infrastructure overview](https://developer.android.com/develop/connectivity/wifi/wifi-infrastructure)，Suggestion API特征：配置非用户单独拥有、审批按应用而非按网络、面向运营商分流类应用，正文 13–21 行；获取 2026-09-05T10:24:26.486575+00:00；SHA 0fb895414a288c359f762001a71675718110dbe06cc2eff3cd958e3bcb2c7556。

## ios 条件与证据

适用范围：未知：两篇来源均不含本节点相关的iOS版本适用信息（快照2026-09-05，version_verified=false）。
条件：未建立机制证据，无适用条件可记录；ios-2仅描述Wi-Fi Aware点对点配对与连接条件（DeviceDiscoveryUI/AccessorySetupKit配对后建立P2P连接），非本节点的接入点建议场景
缺口：NEHotspotConfiguration/NEHotspotHelper等可能对应的NetworkExtension文档未在冻结来源中，未读取；ios-1（Siri事件建议）与节点主题无关，疑似检索误绑；ios-2的P2P设备连接是否属于本节点'协助连接'范围需父级范围澄清，可能属于兄弟节点；无任何iOS版本适用性与entitlement条件证据
真机分类理由：未建立任何机制证据，无法评估iOS侧真机需求；需先补齐可能对应API的官方文档再分类。

- [Providing Trusted Data](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/providing-trusted-data)，Siri Event Suggestions Markup可信数据要求（日历预订事件签名与准确性），与Wi-Fi连接建议无关，正文 1–8 行；获取 2026-09-05T10:25:47.640825+00:00；SHA b377947a7cea09a685a68356d7b7a7b24ff8921b2d1f5e67343eab585986522c。
- [Connecting devices for peer-to-peer Wi-Fi](https://developer.apple.com/documentation/wifiaware/connecting-paired-devices)，Wi-Fi Aware点对点配对连接：经DeviceDiscoveryUI/AccessorySetupKit配对后建立设备间安全连接，非接入点建议，正文 1–14 行；获取 2026-09-05T10:29:13.547614+00:00；SHA bb7277d30de36cbab44782a36c5b922993da402381ac90f0a7a5295e2c8c468b。

## harmonyos 条件与证据

适用范围：未知：STA指南（快照2026-09-04）未注明API起始版本或HarmonyOS发行版；示例使用@kit.ConnectivityKit，另一篇用@ohos.net.connection；HarmonyOS与OpenHarmony发行版差异未核对。
条件：需要SystemCapability.Communication.WiFi.STA系统能力；需申请ohos.permission.GET_WIFI_INFO；建立连接还需ohos.permission.SET_WIFI_INFO；使用前需先使能设备WLAN；connectToCandidateConfig仅能连接应用自己添加的候选网络；候选配置支持removeCandidateConfig移除与getCandidateConfigs查询
缺口：未读js-apis-wifimanager参考正文，候选网络接口完整签名、权限、API起始版本与错误码未核实；指南未注明HarmonyOS发行版；HarmonyOS与OpenHarmony行为差异未核对；候选网络是否参与系统自动连接选择、是否有用户审批环节，读到的指南正文未说明；手机/平板设备形态条件未单独核对
真机分类理由：候选配置连接的接口流程已读到，但权限弹窗、候选网络实际连接行为与适用HarmonyOS版本均未核实，需后续结合API参考与真机复核；本轮无任何实测。

- [STA模式开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sta-development-guide)，STA模式简介：设备作为客户端连接AP/无线路由器访问网络，正文 3–5 行；获取 2026-09-04T09:35:09+00:00；SHA b65031e7aef2801bfdc9c382a69b3c1a3ddfdde9ecd475ebd2303b0e96498223。
- [STA模式开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sta-development-guide)，接口表：addCandidateConfig添加候选网络配置、connectToCandidateConfig连接应用自己添加的候选网络等，正文 18–29 行；获取 2026-09-04T09:35:09+00:00；SHA b65031e7aef2801bfdc9c382a69b3c1a3ddfdde9ecd475ebd2303b0e96498223。
- [STA模式开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sta-development-guide)，判断Wi-Fi状态：需SystemCapability.Communication.WiFi.STA与ohos.permission.GET_WIFI_INFO，正文 33–39 行；获取 2026-09-04T09:35:09+00:00；SHA b65031e7aef2801bfdc9c382a69b3c1a3ddfdde9ecd475ebd2303b0e96498223。
- [STA模式开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sta-development-guide)，建立Wi-Fi连接步骤：需STA系统能力及GET_WIFI_INFO、SET_WIFI_INFO权限，正文 89–97 行；获取 2026-09-04T09:35:09+00:00；SHA b65031e7aef2801bfdc9c382a69b3c1a3ddfdde9ecd475ebd2303b0e96498223。
- [STA模式开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sta-development-guide)，示例代码：addCandidateConfig(config)后调用connectToCandidateConfig连接指定网络，正文 117–122 行；获取 2026-09-04T09:35:09+00:00；SHA b65031e7aef2801bfdc9c382a69b3c1a3ddfdde9ecd475ebd2303b0e96498223。
- [@correctness/listen-default-network-change](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_listen-default-network-change)，code-linter规则：建议应用监听默认网络变化并切换数据传输，与本节点连接建议机制无直接关系，正文 1–5 行；获取 2026-09-05T10:24:00.241468+00:00；SHA 8bedbec42927fe2e00f5de70274ea8dfd33c3765eaee24815ceb30f09e5b9249。

## 待验证差异假设

- programming_model：连接决策与配置归属模型可能不同：Android应用仅提交建议、由平台最终决定连接且建议不进入保存网络列表（配置非用户单独拥有）；HarmonyOS应用添加自有候选网络配置并主动连接自己添加的候选网络。两平台在谁决定连接、配置归属上可能是不同的机制形态。；待核：HarmonyOS候选网络是否也参与系统自动连接选择，未读js-apis-wifimanager无法确认；HarmonyOS候选配置与系统保存网络的关系未在读到的指南中说明；iOS侧机制未建立证据，无法纳入三方比较。
- permissions_privacy：审批与权限模型可能不同：Android按应用一次性用户审批（首次建议即通知，用户拒绝移除CHANGE_WIFI_STATE，可在设置恢复）；HarmonyOS读到的指南仅声明GET_WIFI_INFO/SET_WIFI_INFO权限与STA系统能力，未描述面向用户的审批或通知环节。；待核：HarmonyOS addCandidateConfig是否有用户确认弹窗，指南正文未说明，需读API参考核实；Android最新版本权限行为未对API参考核实；iOS审批机制无证据，未纳入。
- api_surface：API用例面可能不同：Android按用途分离三种API（建议API、网络请求API、ACTION_WIFI_ADD_NETWORKS添加保存网络），并在指南中说明替代已弃用的addNetwork；HarmonyOS读到的STA指南仅描述候选网络配置一条应用侧路径，未见等价的建议聚合或添加保存网络入口。；待核：HarmonyOS是否有等价的添加系统保存网络或P2P网络请求API，需查js-apis-wifimanager全文；本对比基于单一指南页面，未覆盖HarmonyOS Wi-Fi全部接口面；iOS对应API面未知，未纳入。

范围缺口：iOS冻结来源均不覆盖本节点（Siri事件建议、Wi-Fi Aware P2P），NEHotspotConfiguration等可能相关文档未入包，iOS侧只能unknown；HarmonyOS未读js-apis-wifimanager API参考，候选网络接口版本、权限细节与系统级行为未核实；Android未读WifiNetworkSuggestion/WifiManager API参考，最新正式版行为未核实；版本基线unresolved：全部结论仅基于2026-09-04/05快照，不声称覆盖启动日最新正式版；Wi-Fi Aware点对点连接与本节点（接入点连接建议）的边界需父级范围澄清

后续优先级：P1；存在关键缺口与高风险映射：iOS无任何本节点相关证据且可能对应文档缺失；HarmonyOS核心API参考未读、版本未注明；Android建议模型与HarmonyOS候选配置模型是否可比需精研核实，映射错误会直接影响比较结论。

逐条引用及原文摘录见同目录 normalized.json。
