# 端侧ML运行时 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

三平台均读到官方端侧模型执行机制：Android LiteRT 经 Google Play services 分发并配 delegates/Acceleration Service；iOS Core ML 为平台框架统一调度 CPU/GPU/Neural Engine；HarmonyOS MindSpore Lite 经 NNRt 异构调度、要求 .ms 模型。均属机制级初判，三平台版本基线未固定；包内 ios-2（SwiftData/CoreData）与 harmonyos-2（ML-DSA 密码学）与本节点无关。差异假设聚焦分发方式、模型格式、加速暴露。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | documented_mechanism | direct | 官方文档将 LiteRT 定位为 Android 官方 ML 推理运行时，经 Google Play services 分发运行时与 GPU/NPU delegates，并提供 Acceleration Service 在运行时选择最优硬件配置；androidx 包索引含 camera.mlkit.vision 条目（CameraX 与 ML Kit 集成）。 | recommended |
| ios | documented_mechanism | direct | Core ML 框架页记载：以统一模型表示在设备端做预测与训练/微调，自动利用 CPU/GPU/Neural Engine，模型须为 Core ML 格式（Create ML 训练或 Core ML Tools 转换），支持运行时下载编译模型与模型加密，栈基于 Accelerate/BNNS 与 Metal Performance Shaders。 | recommended |
| harmonyos | documented_mechanism | direct | MindSpore Lite Kit 术语页记载端侧运行机制：Context 配置硬件与线程，模型经转换工具生成 .ms 格式，NNRt 为系统跨芯片推理运行时连通 NPU 等加速芯片，异构推理不支持算子回退 CPU，Float16 仅 CPU/GPU，另有端侧训练流程与离线模型机制。 | recommended |

## android 条件与证据

适用范围：developer.android.com/ai/custom 快照（2026-09-05）；未核对 Android API Level、Google Play services 与 LiteRT 版本要求
条件：运行时与 delegates 经 Google Play services 获取（生态服务，非系统 SDK），以确保最新稳定版并减小应用体积；GPU delegate 已提供；自定义/NPU delegate 依赖合作伙伴经 Play services 分发；Acceleration Service API 在运行时选择最优硬件加速配置，无需关心底层硬件与驱动
缺口：最低 Android 版本/API Level、Play services 与 LiteRT 版本要求未在来源中说明；LiteRT 所用模型格式与转换工具链未在冻结来源中说明；系统 SDK 层推理运行时（如 NNAPI）与 LiteRT/Play services 的关系未覆盖；不依赖 Play services 的运行时打包路径无证据；手机/平板设备形态与后台/内存限制未说明
真机分类理由：LiteRT 运行时与 GPU/NPU delegate 实际可用性、Acceleration Service 选配结果依赖具体设备硬件、驱动与 Play services 版本，静态文档无法核实；本轮仅文档初判，不设计用例。

- [Use LiteRT on Android](https://developer.android.com/ai/custom)，Use LiteRT on Android — LiteRT for ML runtime（Android's official ML inference runtime），正文 11–14 行；获取 2026-09-05T10:22:20.093171+00:00；SHA a719227240bafc60d95ae81535e82db8f84d454bf2ab3a517d8462f7b1ebc9b0。
- [Use LiteRT on Android](https://developer.android.com/ai/custom)，Hardware Acceleration with LiteRT Delegates，正文 16–25 行；获取 2026-09-05T10:22:20.093171+00:00；SHA a719227240bafc60d95ae81535e82db8f84d454bf2ab3a517d8462f7b1ebc9b0。
- [Use LiteRT on Android](https://developer.android.com/ai/custom)，Enabled by Google Play services，正文 27–31 行；获取 2026-09-05T10:22:20.093171+00:00；SHA a719227240bafc60d95ae81535e82db8f84d454bf2ab3a517d8462f7b1ebc9b0。
- [Use LiteRT on Android](https://developer.android.com/ai/custom)，Acceleration Service，正文 42–46 行；获取 2026-09-05T10:22:20.093171+00:00；SHA a719227240bafc60d95ae81535e82db8f84d454bf2ab3a517d8462f7b1ebc9b0。
- [Package Index](https://developer.android.com/reference/androidx/packages)，androidx.camera.mlkit.vision 包条目（CameraX 与 ML Kit 集成），正文 79–79 行；获取 2026-09-05T10:40:25.979792+00:00；SHA 86b6e1ac7ed814a469280beb09b79706e1b00f948eb9039db22674103450fd08。

## ios 条件与证据

适用范围：developer.apple.com/documentation/coreml 快照（2026-09-05，版权 2026）；框架落地页无 iOS 最低版本元数据，符号级 availability 未核对
条件：模型须为 Core ML 格式：Create ML 训练或经 Core ML Tools 从其他框架转换；推理与微调在设备端执行，文档称无需网络连接；支持在用户设备上运行时动态下载并编译模型；提供 compute device/plan/policy 与 MLTensor API
缺口：框架落地页无 iOS 最低可用版本，需逐符号核对 availability（Apple 目录含多平台）；CoreAI（最新架构与推理技术）与 Core ML 的边界、版本与适用条件未在来源中说明；后台执行限制与内存/模型大小上限未覆盖；权限要求仅有设备端执行/无需网络的间接描述，无正式权限章节
真机分类理由：Neural Engine 可用性、compute plan 实际调度与运行时下载编译行为依赖具体设备与 iOS 版本，需实机核实；本轮仅文档初判，未核对符号级 availability。

- [Core ML](https://developer.apple.com/documentation/coreml)，Core ML — Overview（integrate machine learning models, all on a person's device），正文 5–7 行；获取 2026-09-05T10:30:09.483693+00:00；SHA 061586425e89ed4fd991720b514b87d6cdbed8bd532cfb90de007d8fd3c1b992。
- [Core ML](https://developer.apple.com/documentation/coreml)，Overview — Create ML/Core ML Tools 模型格式与设备端再训练，正文 13–13 行；获取 2026-09-05T10:30:09.483693+00:00；SHA 061586425e89ed4fd991720b514b87d6cdbed8bd532cfb90de007d8fd3c1b992。
- [Core ML](https://developer.apple.com/documentation/coreml)，Overview — CPU/GPU/Neural Engine 优化与设备端隐私，正文 15–15 行；获取 2026-09-05T10:30:09.483693+00:00；SHA 061586425e89ed4fd991720b514b87d6cdbed8bd532cfb90de007d8fd3c1b992。
- [Core ML](https://developer.apple.com/documentation/coreml)，Overview — 框架栈：Vision/NaturalLanguage/Speech/SoundAnalysis 之基础，构建于 Accelerate/BNNS 与 Metal Performance Shaders，正文 17–17 行；获取 2026-09-05T10:30:09.483693+00:00；SHA 061586425e89ed4fd991720b514b87d6cdbed8bd532cfb90de007d8fd3c1b992。
- [Core ML](https://developer.apple.com/documentation/coreml)，Topics — Core ML models / MLModel，正文 41–43 行；获取 2026-09-05T10:30:09.483693+00:00；SHA 061586425e89ed4fd991720b514b87d6cdbed8bd532cfb90de007d8fd3c1b992。
- [Core ML](https://developer.apple.com/documentation/coreml)，Topics — App integration: Downloading and Compiling a Model on the User's Device，正文 89–91 行；获取 2026-09-05T10:30:09.483693+00:00；SHA 061586425e89ed4fd991720b514b87d6cdbed8bd532cfb90de007d8fd3c1b992。

## harmonyos 条件与证据

适用范围：developer.huawei.com harmonyos-guides 快照（2026-09-04）；适用 HarmonyOS API 版本与发行版（HarmonyOS/OpenHarmony）未标注
条件：模型须由转换工具从 ONNX/CAFFE/TFLITE/TF/PyTorch/MindIR 转为 .ms 端侧格式，或使用硬件厂商离线模型；NPU 加速须配置 NNRt；异构推理中不支持的算子回退 CPU 执行；Float16 推理仅 CPU/GPU 设备可用；算子支持以 ONNX Opset18 支持列表为准
缺口：术语页非 API 参考：js-apis-mindspore-lite 等接口、权限、错误码正文未读取；适用 HarmonyOS API 版本与发行版（HarmonyOS/OpenHarmony）未标注；手机/平板设备形态、后台与内存限制未覆盖；包内 harmonyos-2（ML-DSA 签名验签）为后量子密码主题，与本节点无关，不能作为本节点证据
真机分类理由：NNRt/NPU 加速与算子回退行为依赖具体芯片与设备，术语页不含设备与版本条件，需实机核实；本轮仅文档初判，不设计用例。

- [MindSpore Lite Kit术语](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-term)，Context；上下文（运行时配置对象：硬件设备类型、线程数、绑核），正文 5–7 行；获取 2026-09-04T09:35:09+00:00；SHA 32347d31529b1e6f0530ee424ea29d9eff897a46e67837bc6d04f6993fabf273。
- [MindSpore Lite Kit术语](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-term)，Float16；半精度（仅 CPU/GPU 设备可用），正文 19–19 行；获取 2026-09-04T09:35:09+00:00；SHA 32347d31529b1e6f0530ee424ea29d9eff897a46e67837bc6d04f6993fabf273。
- [MindSpore Lite Kit术语](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-term)，Heterogeneous Inference；异构推理（NNRt 加速芯片与 CPU 分派、回退），正文 23–25 行；获取 2026-09-04T09:35:09+00:00；SHA 32347d31529b1e6f0530ee424ea29d9eff897a46e67837bc6d04f6993fabf273。
- [MindSpore Lite Kit术语](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-term)，Model Conversion；模型转换（ONNX/CAFFE/TFLITE/TF/PyTorch/MindIR 转 .ms），正文 29–31 行；获取 2026-09-04T09:35:09+00:00；SHA 32347d31529b1e6f0530ee424ea29d9eff897a46e67837bc6d04f6993fabf273。
- [MindSpore Lite Kit术语](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-term)，NNRt；神经网络运行时（HarmonyOS 跨芯片推理运行时，连通上层框架与加速芯片），正文 43–45 行；获取 2026-09-04T09:35:09+00:00；SHA 32347d31529b1e6f0530ee424ea29d9eff897a46e67837bc6d04f6993fabf273。
- [MindSpore Lite Kit术语](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-term)，On-device Training；端侧训练（独立训练开发流程与 API 体系），正文 53–55 行；获取 2026-09-04T09:35:09+00:00；SHA 32347d31529b1e6f0530ee424ea29d9eff897a46e67837bc6d04f6993fabf273。

## 待验证差异假设

- availability：运行时获取与更新机制的文档描述不同：Android 官方文档明示 LiteRT 运行时与 delegates 经 Google Play services 分发并保持最新稳定版（生态服务路径）；HarmonyOS 文档将 NNRt 描述为系统级跨芯片推理运行时；iOS Core ML 以平台框架栈描述（构建于 Accelerate/BNNS 与 MPS），未提及外部服务分发依赖。；待核：LiteRT 是否存在不依赖 Google Play services 的打包/回退路径；MindSpore Lite Kit 的具体获取方式（SDK/Kit 版本、商用与开源发行版差异）未在来源中说明；Core ML 与 NNRt 的运行时更新是否随系统版本发布，需版本级证据。
- programming_model：模型格式与转换要求不同（文档明示）：iOS 要求 Core ML 格式（Create ML 训练或 Core ML Tools 转换）；HarmonyOS 要求经模型转换工具生成 MindSpore Lite 的 .ms 端侧格式（源自 ONNX/CAFFE/TFLITE/TF/PyTorch/MindIR）；Android 冻结来源未说明 LiteRT 模型格式，暂不纳入本假设比较。；待核：LiteRT 所用模型格式与转换工具链需补 Android 来源后才能三平台比较；各格式算子覆盖与量化支持差异：HarmonyOS 提及训练后量化（INT8）与 ONNX Opset18 支持列表，iOS 快照未说明量化细节。
- api_surface：硬件加速的暴露方式不同：Android 经 Play services 分发 LiteRT delegates（GPU 已支持、自定义 NPU delegate 依赖合作伙伴）并以 Acceleration Service 运行时选择最优配置；iOS 由 Core ML 统一调度 CPU/GPU/Neural Engine 并暴露 compute device/plan/policy API；HarmonyOS 经 NNRt 异构调度、不支持算子回退 CPU，且 Float16 推理仅 CPU/GPU 可用。；待核：三平台 NPU/Neural Engine 的算子覆盖范围与回退行为是否可比；各平台精度模式（FP16/INT8）支持矩阵需逐平台核对 API 参考；Acceleration Service 与 NNRt 的硬件选择策略能否类比，需行为级证据。

范围缺口：三平台版本基线均未固定：Android API Level/Play services 版本、iOS 符号级 availability、HarmonyOS API 版本与发行版标注缺失；lifecycle_background 与 limits_precision 维度（后台执行、内存/模型大小上限、精度矩阵）在三平台冻结来源中均无正文；permissions_privacy 维度仅 iOS 有设备端执行/无需网络的间接描述，其余平台无权限章节正文；Android 侧 ML Kit 与 LiteRT 关系、系统 SDK 层运行时未覆盖；包内 ios-2（SwiftData/CoreData 持久化）与 harmonyos-2（ML-DSA 密码学）为不相关来源；device_forms 维度（手机/平板）三平台来源均未说明适用设备形态

后续优先级：P1；分发机制差异（Android 生态服务 vs iOS/HarmonyOS 系统集成）与模型格式映射属高风险比较点，且三平台 API 参考级证据（LiteRT 版本要求与模型格式、Core ML 符号 availability、MindSpore Lite API 文档与版本）全部缺失，需正式精研优先核对。

逐条引用及原文摘录见同目录 normalized.json。
