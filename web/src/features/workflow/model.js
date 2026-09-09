/** Presentation and target resolution shared by the console and tests. */
export const workflowStates = {
  planned: ["待执行", "default"],
  running: ["执行中", "processing"],
  completed: ["待合并", "success"],
  published: ["已合并", "success"],
  failed: ["执行失败", "error"],
  blocked: ["需返工", "warning"],
  interrupted: ["执行中断", "warning"],
  publishing_interrupted: ["合并待恢复", "warning"],
  pending: ["等待依赖", "default"],
  succeeded: ["已完成", "success"],
};
export const stageNames = {
  scope: "根据 API 划分下一层",
  android: "Android 实现路径与 API 清单",
  ios: "iOS 实现路径与 API 清单",
  harmonyos: "HarmonyOS 实现路径与 API 清单",
  synthesize: "子特性与 API 分配",
  review: "局部审查",
  anchors: "锚点检测",
  integrate: "整批跨域审查",
};
export const checkNames = {
  coverage: "候选覆盖",
  axis: "划分轴",
  boundaries: "范围边界",
  granularity: "能力粒度",
  naming: "命名",
  anchors: "API 锚点",
  dispositions: "候选去向",
};

export function analysisTargets(model, ids, action) {
  const result = new Set();
  for (const id of ids) {
    if (!model?.byId.has(id)) continue;
    result.add(action === "root" ? (model.ancestors.get(id)?.[0] ?? id) : id);
  }
  return [...result];
}

export function nodeRuns(runs, nodeId) {
  return runs.filter(
    (run) => run.nodes.includes(nodeId) || run.trigger?.source_node === nodeId,
  );
}
export function duration(seconds) {
  if (seconds == null) return "—";
  return seconds < 60
    ? `${seconds.toFixed(1)} 秒`
    : `${Math.floor(seconds / 60)} 分 ${Math.round(seconds % 60)} 秒`;
}
