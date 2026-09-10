// Derive parallel lanes from the pinned dependency graph, preserving registry order.
export function pipelineLayers(plan) {
  const depths = new Map();
  const layers = [];
  for (const id of plan.pipeline_stages) {
    const dependencies = plan.stage_configs[id].definition.dependencies;
    if (dependencies.some(id => !depths.has(id))) throw new Error("工作流依赖顺序无效");
    const depth = dependencies.length ? 1 + Math.max(...dependencies.map(id => depths.get(id))) : 0;
    depths.set(id, depth);
    (layers[depth] ||= []).push(id);
  }
  return layers;
}
