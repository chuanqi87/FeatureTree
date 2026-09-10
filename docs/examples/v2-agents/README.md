# 17 个 Agent 的可执行契约样例

每个 JSON 包含完整输入工作单和对应输出信封，由真实调度器调用确定性模型替身生成。示例使用临时资料库和合成正文，不能导入正式来源或充当真实平台知识、用户确认、真机结果。

建树交付：

| Agent | 样例 | 责任 |
|---|---|---|
| ft-android | [输入/输出](ft-android.json) | Android 事实及输入处置 |
| ft-ios | [输入/输出](ft-ios.json) | iOS 事实及输入处置 |
| ft-harmonyos | [输入/输出](ft-harmonyos.json) | HarmonyOS 事实及输入处置 |
| ft-align | [输入/输出](ft-align.json) | 三端目标对应和未匹配事实 |
| ft-design | [输入/输出](ft-design.json) | 公共节点边界与结构提案 |
| ft-bind | [输入/输出](ft-bind.json) | API 用法、完整路线和处置账本 |
| ft-granularity | [输入/输出](ft-granularity.json) | 粒度及路线独立性审查 |
| ft-coverage | [输入/输出](ft-coverage.json) | 遗漏及未决处置审查 |
| ft-review | [输入/输出](ft-review.json) | 局部独立审查 |
| ft-integrate | [输入/输出](ft-integrate.json) | 跨域审查及冻结建议 |

知识交付：

| Agent | 样例 | 责任 |
|---|---|---|
| fk-scope | [输入/输出](fk-scope.json) | 必答问题、场景与成功标准 |
| fk-android | [输入/输出](fk-android.json) | Android 逐题结论 |
| fk-ios | [输入/输出](fk-ios.json) | iOS 逐题结论 |
| fk-harmonyos | [输入/输出](fk-harmonyos.json) | HarmonyOS 逐题结论 |
| fk-compare | [输入/输出](fk-compare.json) | 三组平台对比较 |
| fk-review | [输入/输出](fk-review.json) | 固定结论的独立审查 |
| fk-confidence | [输入/输出](fk-confidence.json) | 逐项评级，整体由代码取最低档 |

重新生成：`.venv/bin/python tools/verify_v2_contracts.py`。该命令在临时目录中验证完整链路，仅更新本目录的例子，不发起付费模型调用，不修改生产 data 或 CURRENT。输入包含当次代码、规则及 Schema 指纹；时间戳和示例 ID 可以变化。
