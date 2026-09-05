# 试点笔记：distributed.softbus.fabric（2026-09-06）

性质：限量证据/边界诊断试点，非完整节点研究。模型固定 volcengine/glm-5.3，未使用子代理；模型与费用在本环境不可观测。未读取 output/research/tasks 旧任务包，未写 candidate.yaml，未填比较槽位，未读校验实现代码。全局版本基线未完成：所引证据 version_verified 均为 false，本文不产生 confirmed/高/中可信结论，不声称任何平台独有、不支持或完全等价。

## 一、节点范围

多设备间远端能力调用、消息与数据流传输、连接中断处理；排除单一厂商总线内部机制。本试点重点：示意 SysCap 绑定是否有官方公开 API 对应；HarmonyOS 与 OpenHarmony 证据分离；发现/连接/会话/任务接续是否同层级可比。

## 二、三条文档观察（证据元数据见文末表）

- Android[A1][A2]：Cross device SDK 为 Developer Preview（0.1.0-preview01），官方明示不用于生产应用；单一 SDK 内以 Discovery 与 Sessions 两类入口统一覆盖设备发现、加密双向通信、多设备会话（迁移或扩展跨设备体验）；运行条件依赖 Google Play Services Beta、Quick Share 开启、至少两台设备同主 Google 账号且邻近。
- iOS[I1]：Swift Distributed 框架（availability 元数据 iOS 16.0+）提供分布式 actor 跨进程/跨设备远端调用的语言级抽象与 Remote Call 协议族；传输需自备 DistributedActorSystem 实现（生产级为独立集群运行时库），系统未内置对应总线。候选中无发现/会话层公开 API（如 MultipeerConnectivity）正文，记为缺口，非判定不支持。
- HarmonyOS[H1][H2]（均取自华为官网 HarmonyOS 文档，未使用 OpenHarmony 仓库）：发现与会话分属不同公开模块，同属 @kit.DistributedServiceKit 但 SysCap 与起始版本不同——distributedDeviceManager（API 10 起，SystemCapability.DistributedHardware.DeviceManager）负责发现/认证/状态监听；abilityConnectionManager（API 18 起，SystemCapability.DistributedSched.AppCollaboration）管理会话全生命周期（创建→连接→传输→断开→销毁），官方描述基于 sessionId 经"软总线通道"传输文本。两者在不支持分布式业务的 Wearable 上调用均返回 801。示意 SysCap SystemCapability.DistributedHardware.DistributedHardware 在全部已缓存 HarmonyOS 正文中未出现（仅见 DeviceManager），绑定缺口成立；syscap-list 指南页补抓返回 404（1 次补抓预算已用，404 不证明页面不存在）。

## 三、两个具体待证差异/反例

1. 分层可比性：Android 官方将发现、安全通信、会话并入同一 SDK 同层并列；HarmonyOS 拆为多模块、多 SysCap、不同起始版本（10 与 18），任务接续（自由流转/接续）另有体系且本次仅有 best-practices 搜索片段未读正文；iOS 语言级远端调用与发现/会话框架疑似分层但无正文。反例风险：把"软总线织物"当作三平台同层单一能力比较可能不成立。
2. 断连处理契约与运行行为：Android 官方仅给测试前提与"开关飞行模式重置 Quick Share 状态"的排障建议；HarmonyOS 有断开/销毁事件与 801 设备能力差异的明示契约；iOS 无跨设备断连正文。实际断连重连时序、后台存活与接续恢复三平台均待真机证实；iOS 分布式 actor 在 iPhone 跨设备场景的可用性亦无官方 iOS 正文支持。

## 四、先补文档

① iOS MultipeerConnectivity 等发现/会话框架正文与 iOS 适用性；② HarmonyOS 任务接续/自由流转指南与 IPC Kit RPC 跨设备正文；③ 经官网导航重找 SysCap 清单页，核实示意 SysCap 是否为正式 SysCap；④ Android Cross device SDK 各 API 参考（Discovery/Sessions 类）与 Play services 版本条件；⑤ OpenHarmony 如需单独结论，只用 OpenHarmony 仓库取证，不与 HarmonyOS 混用。

## 五、真机复核计划（均未实测，不写 pass；断连时序/设备差异属运行观测，定级必须）

- Android：两台同主账号、开 Quick Share、装 Play Services Beta 的手机；用 Discovery/Sessions 建会话传输；中途断网再恢复；记录失败回调与重建结果。
- HarmonyOS：两台已组网可信手机；distributedDeviceManager 取对端后 createAbilityConnectionSession 建会话传文本；断开连接；记录 disconnect 事件与重连结果；另在 Wearable 验证 801。
- iOS：两台 iPhone，自实现传输层跑分布式 actor 远端调用；断网恢复；记录调用错误与恢复；前置依赖①补文档。
- 建议抽样：权限拒绝场景错误码表现（201/801 静态契约较明确）。

## 六、阶段结果

low／未正式确认。全部观察未核实版本适用性与设备条件，无知识项升级。

---

## 证据元数据（不计入 1200 字）

| ID | 平台 | URL | 章节/符号 | 本地路径（仓库根相对） | body SHA-256 | raw SHA-256 | 获取时间（UTC） |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A1 | Android | https://developer.android.com/guide/topics/connectivity/cross-device-sdk/get-started | "Cross device APIs"、"Dependencies and permissions" | docs-raw/official/snapshots/android/8f/8fab9fb440a6f4bafdda693f3acbe07366b0d108b94f79c77f3876032c2bdad3/cdae76137de45f3e3989e03729bbbaccdef731bdd8a22f9125d1a5190357efde/document-274acded9cdf371ea9536e781c213a6f61bf6fc3c0d2cf09f1da3ed732e606d2.md | 274acded9cdf371ea9536e781c213a6f61bf6fc3c0d2cf09f1da3ed732e606d2 | cdae76137de45f3e3989e03729bbbaccdef731bdd8a22f9125d1a5190357efde | 2026-09-05T10:30:02Z |
| A2 | Android | https://developer.android.com/guide/topics/connectivity/cross-device-sdk/testing-debugging | "Preconditions"、"Tips for Debugging" | docs-raw/official/snapshots/android/f4/f48c81be175798996364e5e7d0275ce0cda96611ec853f088c8a1b533874844e/705ccf5b110e32d23c21da4759d2bb2b2a0d2d90caa6bc52627bcf5b92a5be29/document-5144c8beb92b52089bb950b6716fdab160a5fbd5412fe3f02f790247fac24b0e.md | 5144c8beb92b52089bb950b6716fdab160a5fbd5412fe3f02f790247fac24b0e | 705ccf5b110e32d23c21da4759d2bb2b2a0d2d90caa6bc52627bcf5b92a5be29 | 2026-09-05T10:30:02Z |
| I1 | iOS | https://developer.apple.com/documentation/distributed | "Overview"、Topics: Distributed Actors / Remote Calls / Local Testing | docs-raw/official/snapshots/ios/be/be6e12ff2f3756792da2610f42117a10a921a63e5c8d562e37954e4dea131fe9/1432c2bb6c10391de31f0db3e3ee19802b83b5332b978f69742deb38883aeb99/document-2828c121373f1d00d24ef8b59cccb0b1df5d17424b19448d3367d05957c1c30d.md | 2828c121373f1d00d24ef8b59cccb0b1df5d17424b19448d3367d05957c1c30d | 1432c2bb6c10391de31f0db3e3ee19802b83b5332b978f69742deb38883aeb99 | 2026-09-05T10:32:17Z |
| H1 | HarmonyOS | https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager | 模块说明、createDeviceManager、getAvailableDeviceList、on('deviceStateChange') | docs-raw/official/snapshots/harmonyos/b0/b000ec1dec713199bab86be675d9257eb03962374d8bfb04bd763b23e5174240/f7754bcab32e4e4134e58b39a674d385833fec7f0aca70edd81412fcaf4222ba/document-b907c0c758a1bf41e6f5b998e08f7b4c78bdb107db3cec7cd9f7bffedb297ec9.md | b907c0c758a1bf41e6f5b998e08f7b4c78bdb107db3cec7cd9f7bffedb297ec9 | f7754bcab32e4e4134e58b39a674d385833fec7f0aca70edd81412fcaf4222ba | 2026-09-05T10:27:17Z |
| H2 | HarmonyOS | https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributed-abilityconnectionmanager | 模块说明（逻辑分层架构）、createAbilityConnectionSession | docs-raw/official/snapshots/harmonyos/ea/eabe7e0963cc3bade4cb9f99ed0e73d0a5f54bad44bce8c1ad1debfe1971549f/f149885b5afcadf310fad6ec4e260d690773a2221c74ec8c8288f8086f433543/document-6363d152b7a623359f8b3dbec275c173225452d464d3143cd1d026ee5528c889.md | 6363d152b7a623359f8b3dbec275c173225452d464d3143cd1d026ee5528c889 | f149885b5afcadf310fad6ec4e260d690773a2221c74ec8c8288f8086f433543 | 2026-09-05T10:27:16Z |

阅读量核对：Android 2 篇、iOS 1 篇、HarmonyOS 2 篇，共 5 篇（上限 6）；补抓 URL 1 次（syscap-list，HTTP 404，2026-09-06）。

### 补查线索（仅用于发现，不作为观察证据）

- SysCap 使用指南（https://developer.huawei.com/consumer/cn/doc/harmonyos-references/syscap ，库内已读开头）：SysCap 标识一组开放能力 API 集合，可用 canIUse 判断；未列出 DistributedHardware 相关项。
- 全库检索：SystemCapability.DistributedHardware.* 在缓存正文中仅出现 DeviceManager 一种。
- 搜索命中未读正文：ipc-rpc-overview（"RPC 使用软总线驱动"）、bpta-hopping（自由流转底层依托分布式软总线）、js-apis-proxychannelmanager（代理通道，基于软总线进程）、js-apis-data-rdb（其中标注旧 @ohos.distributedHardware.deviceManager 为系统接口仅系统应用可用，系与 OpenHarmony 资料混用的风险点）。
