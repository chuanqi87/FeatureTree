# 文档导航

第一次接手项目，先读 [代码地图](architecture/code-map.md)，再读 [工作流设计](workflow/design.md)。日常执行看 [管理台操作](workflow/management-console.md) 或 [命令手册](workflow/operations.md)。

| 目录 | 内容 | 何时阅读 |
| --- | --- | --- |
| `architecture/` | 目录职责、依赖方向、入口与旧文件去向 | 修改代码、定位实现 |
| `workflow/` | Agent 分工、批量执行、管理台、验收记录 | 执行与维护节点分析 |
| `taxonomy/` | 树层级、粒度、命名和范围规则 | 设计或验收候选树 |
| `corpus/` | 官方资料入口、下载和检索 | 检查 API 锚点、寻找证据 |
| `knowledge/` | 比较模型、来源适用性、置信度、研究规范 | 当前用于契约校验；树冻结后指导正文生产 |

- 工作流：[设计](workflow/design.md) · [命令操作](workflow/operations.md) · [管理台](workflow/management-console.md) · [首轮验证记录](workflow/validation.md)
- 特性树：[设计规则](taxonomy/design.md)
- 官方语料：[工具指南](corpus/guide.md) · [三端文档入口](corpus/entrypoints.md)
- 知识证据：[比较模型](knowledge/comparison-model.md) · [置信度](knowledge/confidence.md) · [研究规范](knowledge/research-runbook.md) · [来源规则](knowledge/sources.md)

`archive/` 的文档描述历史实现，不参与当前工作流。`workflow/validation.md` 是带时间的验证记录，不作为实时测试数量或树完成度声明。
