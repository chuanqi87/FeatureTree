# FeatureTree v2

从 Android、iOS、HarmonyOS 公开系统 API 与官方文档生成平台中立特性树，并为每个叶子生产三端能力对照知识：支持条件、实现依据、差异影响、逐项高中低可信度及人工审核。

17 个具名 Agent 分为建树链和知识链。代码负责输入守恒、粒度计数、质量门、状态、不可变发布与回滚；模型不填权威数量或整体评级。低可信知识可见、可检索并进入人工审核。

当前处于架构切换和真实校准阶段，正式接管门及完成情况见 [切换记录](docs/migration/v2-progress.md)。未经过用户确认的候选树和知识样稿不会被发布为正式知识。

```sh
.venv/bin/pip install -r requirements.txt
npm ci --prefix tools/sdk
npm ci --prefix tools/opencode --ignore-scripts
swift build -c release --package-path tools/sdk/swift
npm ci --prefix web
npm run build --prefix web
.venv/bin/python -m featuretree console serve --port 8765
```

首次使用先建立 Python 虚拟环境。模型执行需要已有 OpenCode 配置，工作单显式指定 provider/model。操作、数据与接口见 [新版操作手册](docs/workflow/operations.md)；模块职责见 [代码地图](docs/architecture/code-map.md)。

当前真实试跑产生了三个范围、六个候选叶子；尚无真实知识样稿。服务商返回 HTTP 402（余额不足），余下审查和知识链已停止。候选的完整路线绑定还需修订，最新正式 SDK 基线也未闭合。详见 [校准交付与缺口](docs/migration/v2-calibration-review.md)。

正式数据唯一入口是 data/CURRENT.json，引用不可变树、绑定、知识和审核投影。data、.workflow/v2、原文库和 archive 中的大数据均独立备份，Git 不构成完整备份。

旧源码在 codex/archive-v1-20260910-091230，旧数据与恢复说明在 archive/v2-cutover-20260910-091230。当前代码不提供旧版写入兼容层，也不会恢复旧树、运行、冻结或评级成功状态。
