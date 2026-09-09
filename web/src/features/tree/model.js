/** Pure tree indexing, search, visibility and layout; no DOM or IO. */
import { matchingClaims } from "../../shared/quality.js";
export function createModel(snapshot) {
  const byId = new Map(snapshot.nodes.map((node) => [node.id, node]));
  const roots = snapshot.roots.filter((id) => byId.has(id));
  const descendants = new Map();
  const ancestors = new Map();
  function visit(id, parents) {
    const node = byId.get(id);
    ancestors.set(id, parents);
    const ids = node.children.flatMap((child) => [
      child,
      ...visit(child, [...parents, id]),
    ]);
    descendants.set(id, ids);
    return ids;
  }
  roots.forEach((id) => visit(id, []));
  const searchIndex = new Map(
    snapshot.nodes.map((node) => [
      node.id,
      JSON.stringify(node).toLocaleLowerCase(),
    ]),
  );
  return { ...snapshot, byId, roots, descendants, ancestors, searchIndex };
}

export function scopeIds(model, domain) {
  return domain && model.byId.has(domain)
    ? [domain, ...model.descendants.get(domain)]
    : model.nodes.map((node) => node.id);
}

export function visibleTree(
  model,
  {
    domain,
    query,
    collapsed,
    progressState = "",
    confidence = "",
    deviceReview = "",
    role = "",
  },
) {
  const terms = query.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
  const exactId = model.byId.has(query.trim()) ? query.trim() : "";
  const filtering =
    terms.length > 0 ||
    Boolean(progressState || confidence || deviceReview || role);
  const inScope = new Set(scopeIds(model, domain));
  const matches = new Set(
    [...inScope].filter(
      (id) =>
        (exactId
          ? id === exactId
          : terms.every((term) => model.searchIndex.get(id).includes(term))) &&
        (!progressState ||
          model.byId.get(id).comparison_progress.state === progressState) &&
        (!role || model.byId.get(id).knowledge_role === role) &&
        (!(confidence || deviceReview) ||
          matchingClaims(model.byId.get(id), { confidence, deviceReview })
            .length > 0),
    ),
  );
  const allowed = new Set(matches);
  if (filtering)
    matches.forEach((id) =>
      model.ancestors.get(id).forEach((parent) => {
        if (inScope.has(parent)) allowed.add(parent);
      }),
    );
  const rows = [];
  function visit(id, depth) {
    if (!allowed.has(id)) return;
    const node = model.byId.get(id);
    const children = node.children.filter((child) => allowed.has(child));
    const expanded = children.length > 0 && (filtering || !collapsed.has(id));
    rows.push({
      node,
      depth,
      expanded,
      match: filtering && matches.has(id),
    });
    if (expanded) children.forEach((child) => visit(child, depth + 1));
  }
  const roots = (domain ? [domain] : model.roots).filter((id) =>
    allowed.has(id),
  );
  roots.forEach((id) => visit(id, 0));
  return {
    rows,
    matchedIds: [...matches],
    matchCount: matches.size,
    scopeCount: inScope.size,
  };
}

export function tableData(rows) {
  const records = new Map(
    rows.map((row) => [
      row.node.id,
      { ...row.node, treeChildren: [], match: row.match },
    ]),
  );
  const roots = [];
  for (const row of rows) {
    const record = records.get(row.node.id);
    const parent = records.get(row.node.parent);
    if (parent) parent.treeChildren.push(record);
    else roots.push(record);
  }
  for (const record of records.values())
    if (!record.treeChildren.length) delete record.treeChildren;
  return roots;
}

export function treeStats(model, domain) {
  const nodes = scopeIds(model, domain).map((id) => model.byId.get(id));
  return {
    total: nodes.length,
    leaves: nodes.filter((node) => node.knowledge_role === "leaf").length,
    depth: Math.max(
      0,
      ...nodes.map((node) => model.ancestors.get(node.id).length + 1),
    ),
    reviewing: nodes.filter(
      (node) => node.comparison_progress.state === "in_progress",
    ).length,
    complete: nodes.filter(
      (node) => node.comparison_progress.state === "complete",
    ).length,
  };
}

export function graphLayout(rows) {
  const ids = new Set(rows.map((row) => row.node.id));
  const positions = new Map();
  const rowById = new Map(rows.map((row) => [row.node.id, row]));
  let cursor = 40;
  function place(id) {
    const row = rowById.get(id);
    const children = row.expanded
      ? row.node.children.filter((child) => ids.has(child))
      : [];
    const childPositions = children.map(place);
    const y = children.length
      ? (childPositions[0].y + childPositions.at(-1).y) / 2
      : cursor;
    if (!children.length) cursor += 90;
    const position = { x: 36 + row.depth * 292, y, row };
    positions.set(id, position);
    return position;
  }
  rows
    .filter((row) => row.depth === 0)
    .forEach((row) => {
      place(row.node.id);
      cursor += 36;
    });
  return {
    positions,
    width: Math.max(360, ...[...positions.values()].map((p) => p.x + 280)),
    height: Math.max(220, cursor + 40),
  };
}
