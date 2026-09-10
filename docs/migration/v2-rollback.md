# v2 恢复与回滚

## 恢复旧版资料

源码归档分支 `codex/archive-v1-20260910-091230` 固定在 `8d8ac2522002ed059615d8f85fd8b19a234516e0`。需要阅读或运行旧版时，在独立 checkout 恢复该分支，不在当前 master 接回旧执行入口。

数据归档位于 `archive/v2-cutover-20260910-091230/legacy/`；原旧运行和输出另保存在同目录的 `retired-originals/`。按照 `manifest.json` 的相对路径、字节数和 SHA-256 逐项核对，再恢复到独立旧版 checkout。原文库清单位于 `official-corpus-manifest.jsonl`，正文保留在原位。完整恢复步骤见归档的 `RESTORE.md`。这些被 Git 忽略的数据需要单独备份，归档分支不能代替数据备份。

## 回滚 v2 正式发布

1. `python -m featuretree release show` 核对当前发布。
2. `python -m featuretree release compare --before <当前发布> --after <目标发布>` 查看差异。
3. `python -m featuretree release rollback --id <目标发布> --expected <当前发布> --key <稳定请求键>` 创建并提交回滚清单。
4. 再读取当前树与审核投影。目标知识若已被人工指出错误，回滚不会清除该错误记录。

回滚不会修改历史清单、知识或审核事件，不直接把 CURRENT 指针改成旧值。重复提交同一请求键返回原回执；目标或预期版本变化时使用新的请求键。

## 发布中断和并发冲突

`data/transactions/<键>.json` 记录准备或已提交状态。中断后再次执行同一个 `release publish --id <键>`；程序在发布锁内检查当前指针，识别已切换但未写回执的事务。读者固定一个发布 ID，仅看到完整旧版或完整新版。

如果另一发布抢先提交，返回版本冲突。纯知识更新可用 `release rebase --id <原事务键> --expected <最新发布> --key <新键>` 重建候选：无关知识保留，相同叶子或相关依赖变化拒绝覆盖。树、绑定和来源结构变更须重新生成针对当前树的整合审查，不能强制覆盖指针。

## 工作流恢复

运行目录保留计划、每次输入、模型原始输出、用量、事件、产物引用和问题。`workflow resume --id <运行>` 仅调度未完成依赖；中断的调用保留为 interrupted，需要显式重试。`workflow revalidate` 对保留的完整答案重新执行机器校验，不重新调用模型。已变化的执行器指纹要求重新计划。

不要编辑封存对象或 response 原文来把失败改为成功；修订通过新尝试或新运行记录。索引可以重建，业务对象和审核事件不能从缓存推断恢复。
