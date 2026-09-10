# SDK 语法适配器

- Android XML 与 Native/ObjC Clang 适配器在 featuretree/corpus/extractors。
- arkts.mjs 使用 TypeScript 5.9.3 AST；移植参考项目的 AST/JSDoc 方法，显式保留 systemapi 与解析失败，不包含目标版本和目录常量。
- swift/ 的 SwiftParser 提取器移植自 harmony-knowledge/tools/pipeline/extract/apple/apple-swift。原版本标注和条件编译分支保留；适配器将平台适用性标为待核，不自动认证公开性或稳定基线。
- 运行时仅依赖本项目内的适配器和用户传入 SDK 路径，不读取参考项目。

安装：npm ci --prefix tools/sdk；Python 依赖见 requirements.txt。
Swift：swift build -c release --package-path tools/sdk/swift。
所有失败按源文件记录，不能把部分 AST 当作完整覆盖。
