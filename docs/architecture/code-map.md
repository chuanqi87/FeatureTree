# FeatureTree v2 代码地图

最终产物是叶子知识。树、API 绑定、规格、结论、审查和评级都按内容版本追溯；正式消费者固定一次发布，不拼接不同批次的可变文件。

| 模块 | 所有者职责 | 主要实现 |
|---|---|---|
| core | 通用内容身份、不可变对象、原子写入、CAS 指针 | content、io、artifacts、contracts、versions、requests |
| corpus | 官方资料、声明、符号族、目录、来源清单和分页 | snapshots、catalog、identity、importers、sdk、extractors、capture、source_policy |
| taxonomy | 树身份与结构、API 用途、处置守恒、路线规模 | model、coverage、routes、revisions、source_migration |
| knowledge | 研究问题、结论依据、评级上限、审核事件和失效 | specifications、claims、ratings、reviews、validity、observations |
| workflow | 工作单、DAG、独立调用、机器门、冻结与发布用例 | registry、planner、run_store、runner、execution、packaging、tree_handlers、knowledge_handlers、provenance、calibration、freezes、releases、review_service |
| reporting | 指定发布的轻量树、知识和差异投影 | releases、markdown |
| console | HTTP、本机写入校验、任务进程和应用装配 | application、api、recovery、server、launcher |
| cli | 参数解析和调用用例 | main、commands |

依赖：corpus→core；taxonomy→core/corpus；knowledge→core/corpus/taxonomy；workflow、reporting→前述四层；console→workflow/reporting；cli 装配。`tests/backend/test_architecture.py` 检查反向依赖、循环、核心反向引用脚本/测试、跨测试套件导入和前端共享层依赖。

前端维持 app/features/shared。六个功能域分别是 tree、sources、workflow、knowledge、review、release；共享层只提供请求、状态、展示和纯计算。树接口只返回节点与知识摘要；完整知识、绑定和正文按需读取。

OpenCode 是唯一模型执行后端。每次调用使用独立目录和固定 Agent 文本，通过 `OPENCODE_CONFIG_DIR` 加载该次调用的 source_catalog、submit_payload 和 finish_payload。来源只读，交付工具仅能在当前尝试目录分批写入不可变内容并完成 JSON 文件；任意文件写入、shell、委派仍禁用。文件完成即读取并执行完整业务校验，无须等待聊天返回长 JSON。不会修改用户全局 OpenCode 配置。
