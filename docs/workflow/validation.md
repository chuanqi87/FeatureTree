# 验收

```sh
.venv/bin/python -m unittest discover -s tests/backend -t . -q
npm run test --prefix web
npm run build --prefix web
```

后端覆盖不可变对象与篡改、CAS/幂等/指针中断恢复、分页/索引遗漏、声明身份、三类 SDK 与 Native 提取、17 个具名 Agent 的替身全链、领域冻结和真实交付出处、最低可信度与过期评级、人工裁决与回滚错误保全、架构依赖及保留原文库行为。前端包含状态/身份/可信筛选纯逻辑和六页服务端渲染检查。

测试替身的证据只存在于临时目录，绝不计为生产研究或用户确认。真实烟测记录在 .workflow/v2/runs；必须同时核对 source_calls、原始事件、模型用量、结构校验与引用校验。只返回有效 JSON 不代表来源检索已经通过。

完整接管另需三范围真实校准、用户确认、首批正式冻结和发布，以及当前代码对应的 UI/端到端验收。实际完成情况以 docs/migration/v2-progress.md 为准。
