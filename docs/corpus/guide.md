# 来源建设

一次性历史导入：`sources import --reference /absolute/reference/project`。参考项目原始 JSONL 复制到 data/imports/<hash>，保留原身份、文件哈希和冲突记录；正常运行不依赖参考目录。缺少公开性、SDK 适用性或多语言别名依据的记录保持未知。

SDK 提取：`sources extract --request sdk.json`。请求包含 adapter（android-xml/native/arkts/swift）、sdk_root、patterns、platform、distribution、language、module、sdk_version，可附 clang_args。每个匹配源文件均记录成功/失败、哈希与字节数，原始源文件保存在 data/imports/sdk，防止外部 SDK 升级后无法复核。

Android 适配器读取 api-versions.xml，保留重载、继承和已移除声明。Native 用 Clang AST，保留公开属性、方法、函数等；必需头文件缺失会标失败并降公开性为未知。ArkTS 用 TypeScript AST，继承 systemapi/internal 标记。Swift 使用移植的 SwiftParser，保留私有记录以便处置，提取 public/open、继承适用性和重载；条件编译分支的实际设备适用性仍需核实。适配代码来自参考项目思路，运行路径无参考项目硬依赖。

来源封存不代表完成。来源文件处理、API 处置、官方目录处置及独立用法覆盖分别记账。未处理、进入研究、已关联/辅助、依据排除、证据不足、归属歧义和失败都必须有去向；排除必须有规则、理由和证据。

新官方资料用 sources capture。正文缺失是来源缺口，不是平台不支持。网络采集创建新快照，不能覆盖已封存的源版本。声明相同但 SDK 不同属于版本差异；名称/签名/语言决定身份，SDK 版本不混入展示名。
