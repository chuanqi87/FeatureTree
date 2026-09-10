export const labels = {
  high: "高", medium: "中", low: "低", unknown: "未知", supported: "支持", conditional: "有条件支持",
  unsupported: "不支持", same: "相同", different: "有差异", not_applicable: "不适用", fact: "平台事实",
  pending: "待审核", in_review: "审核中", decided: "已裁决", research_requested: "已要求重研", deferred: "暂缓",
  planned: "已计划", running: "执行中", waiting: "等待依赖", ready: "可执行", completed: "已交付", failed: "执行失败",
  waiting_sources: "等待资料", waiting_revision: "等待修订", waiting_human: "等待人工", ready_to_publish: "可发布",
  published: "已发布", cancelled: "已取消", blocked: "阻断", interrupted: "已中断", pass: "通过",
  completed_with_gaps: "带缺口交付", revise: "需要修订", needs_sources: "需要来源", historical: "历史输入",
  verified: "已核验", candidate: "候选", current: "有效", stale: "失效待更新", invalidated: "人工指出问题",
  not_produced: "待生产", capability_result: "能力结果", api_surface: "接口形态",
};
export const text = value => labels[value] || value || "—";
export function treeRows(features) {
  const nodes = new Map(features.map(row => [row.id, { ...row, key: row.id, children: [] }]));
  const roots = [];
  for (const node of nodes.values()) {
    if (node.parent_id && nodes.has(node.parent_id)) nodes.get(node.parent_id).children.push(node);
    else roots.push(node);
  }
  for (const node of nodes.values()) if (!node.children.length) delete node.children;
  return roots;
}
export function trusted(summary) {
  return summary?.validity === "current" && ["high", "medium"].includes(summary.confidence);
}
export function safeUrl(value) {
  try { const url = new URL(value); return ["https:", "http:"].includes(url.protocol) ? value : null; } catch { return null; }
}
