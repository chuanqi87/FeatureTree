# 试点笔记：distributed.softbus.fabric（2026-09-06）

复核版：原始模型交付保存在 `output/research/pilot-originals/2026-09-06/`。协调者撤回了未被证明的 iOS 否定推断、模块级错误码概括，并将预览 SDK 和非手机测试移出主比较范围；证据元数据已由缓存自动核验导出。本文仍未通过正式知识验收。

性质：限量证据/边界诊断试点，非完整节点研究。模型固定 volcengine/glm-5.3，未使用子代理；模型与费用在本环境不可观测。未读取 output/research/tasks 旧任务包，未写 candidate.yaml，未填比较槽位，未读校验实现代码。全局版本基线未完成：所引证据 version_verified 均为 false，本文不产生 confirmed/高/中可信结论，不声称任何平台独有、不支持或完全等价。

## 一、节点范围

多设备间远端能力调用、消息与数据流传输、连接中断处理；排除单一厂商总线内部机制。本试点重点：示意 SysCap 绑定是否有官方公开 API 对应；HarmonyOS 与 OpenHarmony 证据分离；发现/连接/会话/任务接续是否同层级可比。

## 二、三条文档观察（证据元数据见文末表）

- Android[A1][A2]：Cross device SDK 为 Developer Preview（0.1.0-preview01），官方明示不用于生产应用；单一 SDK 内以 Discovery 与 Sessions 两类入口统一覆盖设备发现、加密双向通信、多设备会话（迁移或扩展跨设备体验）；运行条件依赖 Google Play Services Beta、Quick Share 开启、至少两台设备同主 Google 账号且邻近。
- iOS[I1]：Swift Distributed 正文描述分布式 actor 与 ActorSystem 承担网络、序列化等职责的语言级抽象。框架 availability 元数据中的 iOS 16.0+ 不能独立证明某套传输实现可直接用于 iPhone 间通信。该页更不能证明 iOS 系统没有其他发现、会话或传输能力；MultipeerConnectivity 等场景框架尚未读取，保持未知。
- HarmonyOS[H1][H2]（华为官网 HarmonyOS 文档，非 OpenHarmony 仓库）：发现与会话分属不同公开模块，同属 @kit.DistributedServiceKit，但 SysCap 与起始版本不同：distributedDeviceManager（API 10 起，SystemCapability.DistributedHardware.DeviceManager）负责发现/认证/状态监听；abilityConnectionManager（API 18 起，SystemCapability.DistributedSched.AppCollaboration）提供会话创建、连接、传输、断开、销毁等接口。H2 的 createAbilityConnectionSession 在不支持分布式业务的 Wearable 等所列条件下可报 801，不能推广为两个模块的所有调用都返回 801；例如销毁接口列出不同错误码。示意绑定 SystemCapability.DistributedHardware.DistributedHardware 在本次缓存检索中未找到，属于待核实绑定，不证明能力不存在；补抓 syscap-list 一次返回 404，同样不构成不存在证据。

## 三、两个具体待证差异/反例

1. 分层可比性：Android 官方将发现、安全通信、会话并入同一 SDK 同层并列；HarmonyOS 拆为多模块、多 SysCap、不同起始版本（10 与 18），任务接续（自由流转/接续）另有体系且本次仅有 best-practices 搜索片段未读正文；iOS 语言级远端调用与发现/会话框架疑似分层但无正文。反例风险：把"软总线织物"当作三平台同层单一能力比较可能不成立。
2. 断连处理契约与运行行为：Android 官方仅给测试前提与"开关飞行模式重置 Quick Share 状态"的排障建议；HarmonyOS 有断开/销毁事件与 801 设备能力差异的明示契约；iOS 无跨设备断连正文。实际断连重连时序、后台存活与接续恢复三平台均待真机证实；iOS 分布式 actor 在 iPhone 跨设备场景的可用性亦无官方 iOS 正文支持。

## 四、先补文档

① iOS MultipeerConnectivity 等发现/会话框架正文与 iOS 适用性；② HarmonyOS 任务接续/自由流转指南与 IPC Kit RPC 跨设备正文；③ 经官网导航重找 SysCap 清单页，核实示意 SysCap 是否为正式 SysCap；④ Android 正式可用的同场景方案正文；本次 Cross device SDK 0.1.0-preview01 官方明确为预览且不供生产，只能进入预览附录，不代表最新正式版主比较已覆盖；⑤ OpenHarmony 如需单独结论，只用 OpenHarmony 仓库取证，不与 HarmonyOS 混用。

## 五、真机复核计划（均未实测，不写 pass；断连时序/设备差异属运行观测，定级必须）

- Android：先补齐正式方案，再制定两台手机的连接、传输、断网恢复计划。使用 Play Services Beta / Cross device SDK Preview 的实验单列预览附录，不作为主范围的必测项。
- HarmonyOS：在正式手机发行版与 API 配对核实后，用两台符合组网条件的手机测试发现、建会话、传输和断开恢复；记录具体方法、权限、系统构建号和事件。Wearable 的 801 验证只列非手机附录。
- iOS：先读场景框架并选定可比的公开方案，再制定两台 iPhone 的连接与断网恢复计划；当前证据不足以要求用户先自建 actor 传输层。
- 建议抽样：权限拒绝场景错误码表现（201/801 静态契约较明确）。

## 六、阶段结果

low／未正式确认。全部观察未核实版本适用性与设备条件，无知识项升级。

---

## 证据元数据（不计入 1200 字）

| ID | 平台 | URL | 章节/符号 | 本地路径（仓库根相对） | body SHA-256 | raw SHA-256 | 获取时间（UTC） |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A1 | Android | https://developer.android.com/guide/topics/connectivity/cross-device-sdk/get-started | "Cross device APIs"、"Dependencies and permissions" | docs-raw/research/2026-09-06/8fab9fb440a6f4bafdda693f3acbe07366b0d108b94f79c77f3876032c2bdad3/274acded9cdf371ea9536e781c213a6f61bf6fc3c0d2cf09f1da3ed732e606d2/document.md | 274acded9cdf371ea9536e781c213a6f61bf6fc3c0d2cf09f1da3ed732e606d2 | cdae76137de45f3e3989e03729bbbaccdef731bdd8a22f9125d1a5190357efde | 2026-09-05T10:30:02.235345+00:00 |
| A2 | Android | https://developer.android.com/guide/topics/connectivity/cross-device-sdk/testing-debugging | "Preconditions"、"Tips for Debugging" | docs-raw/research/2026-09-06/f48c81be175798996364e5e7d0275ce0cda96611ec853f088c8a1b533874844e/5144c8beb92b52089bb950b6716fdab160a5fbd5412fe3f02f790247fac24b0e/document.md | 5144c8beb92b52089bb950b6716fdab160a5fbd5412fe3f02f790247fac24b0e | 705ccf5b110e32d23c21da4759d2bb2b2a0d2d90caa6bc52627bcf5b92a5be29 | 2026-09-05T10:30:02.797052+00:00 |
| I1 | iOS | https://developer.apple.com/documentation/distributed | "Overview"、Topics: Distributed Actors / Remote Calls / Local Testing | docs-raw/research/2026-09-06/be6e12ff2f3756792da2610f42117a10a921a63e5c8d562e37954e4dea131fe9/2828c121373f1d00d24ef8b59cccb0b1df5d17424b19448d3367d05957c1c30d/document.md | 2828c121373f1d00d24ef8b59cccb0b1df5d17424b19448d3367d05957c1c30d | 1432c2bb6c10391de31f0db3e3ee19802b83b5332b978f69742deb38883aeb99 | 2026-09-05T10:32:17.185988+00:00 |
| H1 | HarmonyOS | https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager | 模块说明、createDeviceManager、getAvailableDeviceList、on('deviceStateChange') | docs-raw/research/2026-09-06/b000ec1dec713199bab86be675d9257eb03962374d8bfb04bd763b23e5174240/b907c0c758a1bf41e6f5b998e08f7b4c78bdb107db3cec7cd9f7bffedb297ec9/document.md | b907c0c758a1bf41e6f5b998e08f7b4c78bdb107db3cec7cd9f7bffedb297ec9 | f7754bcab32e4e4134e58b39a674d385833fec7f0aca70edd81412fcaf4222ba | 2026-09-05T10:27:17.190280+00:00 |
| H2 | HarmonyOS | https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributed-abilityconnectionmanager | 模块说明（逻辑分层架构）、createAbilityConnectionSession | docs-raw/research/2026-09-06/eabe7e0963cc3bade4cb9f99ed0e73d0a5f54bad44bce8c1ad1debfe1971549f/6363d152b7a623359f8b3dbec275c173225452d464d3143cd1d026ee5528c889/document.md | 6363d152b7a623359f8b3dbec275c173225452d464d3143cd1d026ee5528c889 | f149885b5afcadf310fad6ec4e260d690773a2221c74ec8c8288f8086f433543 | 2026-09-05T10:27:16.527781+00:00 |

阅读量核对：Android 2 篇、iOS 1 篇、HarmonyOS 2 篇，共 5 篇（上限 6）；补抓 URL 1 次（syscap-list，HTTP 404，2026-09-06）。

### 补查线索（仅用于发现，不作为观察证据）

- SysCap 使用指南（https://developer.huawei.com/consumer/cn/doc/harmonyos-references/syscap ，库内已读开头）：SysCap 标识一组开放能力 API 集合，可用 canIUse 判断；未列出 DistributedHardware 相关项。
- 全库检索：SystemCapability.DistributedHardware.* 在缓存正文中仅出现 DeviceManager 一种。
- 搜索命中未读正文：ipc-rpc-overview（"RPC 使用软总线驱动"）、bpta-hopping（自由流转底层依托分布式软总线）、js-apis-proxychannelmanager（代理通道，基于软总线进程）、js-apis-data-rdb（其中标注旧 @ohos.distributedHardware.deviceManager 为系统接口仅系统应用可用，系与 OpenHarmony 资料混用的风险点）。
