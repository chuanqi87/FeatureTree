# 全量分析启动检查

检查时间：2026-09-05T15:46:41.105391+00:00；运行日期：2026-09-05。

研究输入可用：True。全量分析放行：False。

范围：启动日最新正式版，手机优先；其他形态单独记录。

节点 212：{'rollup': 106, 'leaf': 106}；候选原文及原始响应校验 2528 份。
绑定资料缺口 1 条；缺少平台候选的节点 0 个。
尚需审查排除边界的节点 201 个。

## 尚未满足的全量启动条件

- Official stable release/SDK baseline for 2026-09-05 has not been resolved: output/research/baseline.json
- Pilot connectivity.bluetooth.le.scan.filter: missing or stale pilot review; reviewer and scope/evidence review notes required; every investigated claim needs confidence and physical-device review assessment
- Pilot app.background.foreground_task: missing or stale pilot review; reviewer and scope/evidence review notes required; every investigated claim needs confidence and physical-device review assessment
- Pilot distributed.softbus.fabric: missing or stale pilot review; reviewer and scope/evidence review notes required; every investigated claim needs confidence and physical-device review assessment
- Pilot security.permissions.runtime: missing or stale pilot review; reviewer and scope/evidence review notes required; every investigated claim needs confidence and physical-device review assessment
- Pilot ui.declarative.vs_imperative: missing or stale pilot review; reviewer and scope/evidence review notes required; every investigated claim needs confidence and physical-device review assessment

逐节点缺口、研究步骤、平台对及输入指纹见 readiness.json。

启动顺序：固定官方版本基线 → 完成五个高风险试点 → 叶子研究 → 父节点范围复核 → 按有效证据汇总洞察。
候选、目录映射、历史正文和哈希通过均不代表事实已经核实。

## 目录与范围的剩余缺口

| 平台 | 范围待定 | 已纳入但未映射 |
| --- | ---: | ---: |
| android | 0 | 112 |
| ios | 154 | 0 |
| harmonyos | 0 | 280 |

这些目录统计不等于 SDK 全覆盖，需在发现阶段继续处理；叶子与父级汇总应分别计数。
