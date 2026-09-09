# 测试导航

| 路径 | 负责验证 |
| --- | --- |
| `backend/test_architecture.py` | 包依赖方向、循环依赖、薄入口和样例隔离 |
| `backend/cli/` | 统一命令、原有脚本入口和无副作用帮助页 |
| `backend/taxonomy/` | 仓库、树关系、遍历和导出 |
| `backend/knowledge/` | 比较结论、证据、置信度与真机复核 |
| `backend/corpus/` | 文档索引、检索、下载与证据导出 |
| `backend/workflow/` | DAG、重试返工、产物防篡改、发布、规则指纹 |
| `backend/console/` | 快照与执行 HTTP API、安全边界和容量 |
| `frontend/` | 树模型、知识搜索、范围筛选和任务选择 |
| `fixtures/` | 合成树、知识、模型替身和临时管理台 |

```bash
.venv/bin/python -m unittest discover -s tests -q
npm --prefix web test
npm --prefix web run build
```

隔离浏览器验证服务：`.venv/bin/python -m tests.fixtures.console`。它在临时目录创建树，使用合成模型结果，不写正式数据、不调用付费模型。样例不代表真实平台支持情况。
