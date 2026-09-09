# 后端代码入口

后端按职责分成 8 个包。目录内放实现，项目根的 `scripts/` 只负责命令转发。完整说明见 [代码地图](../docs/architecture/code-map.md)。

| 包 | 负责什么 | 从哪里开始读 |
| --- | --- | --- |
| `cli/` | 解析参数、装配服务与后端 | [main.py](cli/main.py) |
| `console/` | HTTP 接口、节点执行用例、任务展示 | [server.py](console/server.py)、[service.py](console/service.py) |
| `workflow/` | 工作单、DAG、验收、恢复与发布 | [planning.py](workflow/planning.py)、[engine.py](workflow/engine.py) |
| `taxonomy/` | 树结构、粒度、锚点绑定、节点构造 | [structure.py](taxonomy/structure.py) |
| `knowledge/` | 知识空壳、比较、置信度、证据校验 | [validation.py](knowledge/validation.py) |
| `corpus/` | 官方语料存储、下载、检索与证据导出 | [store.py](corpus/store.py)、[search.py](corpus/search.py) |
| `reporting/` | 树视图、矩阵、复核清单、质量报告 | [views.py](reporting/views.py)、[exports.py](reporting/exports.py) |
| `core/` | 仓库读写、路径、Schema 加载 | [storage.py](core/storage.py) |

查看全部命令：`.venv/bin/python -m featuretree --help`。

`knowledge/` 是正在使用的数据规则，不是旧模型执行器；`reporting/` 是按需导出工具，不负责分析调度。旧执行器仅在项目根 `archive/` 中。
