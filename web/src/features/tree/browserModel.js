import { treeRows } from '../../shared/model.js';

export function visibleViews(views, status, history) {
  const filtered = views.filter(view => status === 'all' || view.status === status);
  if (history) return filtered;
  const seen = new Set();
  return [...filtered].sort((a, b) => {
    const cancelled = Number(a.run_status === 'cancelled') - Number(b.run_status === 'cancelled');
    return cancelled || b.updated_at.localeCompare(a.updated_at);
  }).filter(view => {
    if (view.status === 'formal') return true;
    const ids = new Set(view.features.map(node => node.id));
    const scope = view.features.filter(node => !ids.has(node.parent_id)).map(node => node.id).sort().join('|');
    if (seen.has(scope)) return false;
    seen.add(scope);
    return true;
  });
}

export function browseNodes(views, query = '') {
  const term = query.trim().toLocaleLowerCase();
  function convert(node, view, ancestors = []) {
    const key = `${view.id}:${node.id}`;
    const children = (node.children || []).map(child => convert(child, view, [...ancestors, key])).filter(Boolean);
    const match = `${node.name} ${node.definition || ''}`.toLocaleLowerCase().includes(term);
    if (term && !match && !children.length) return null;
    // Matching a branch retains its subtree so it can still be explored.
    const descendants = term && match ? (node.children || []).map(child => convertUnfiltered(child, view, [...ancestors, key])) : children;
    return { ...node, key, view, ancestors, children: descendants, isLeaf: node.node_type === 'leaf' };
  }
  function convertUnfiltered(node, view, ancestors) {
    const key = `${view.id}:${node.id}`;
    return { ...node, key, view, ancestors, isLeaf: node.node_type === 'leaf', children: (node.children || []).map(child => convertUnfiltered(child, view, [...ancestors, key])) };
  }
  return views.flatMap(view => treeRows(view.features).map(node => convert(node, view)).filter(Boolean));
}

export function flattenNodes(nodes) {
  return nodes.flatMap(node => [node, ...flattenNodes(node.children || [])]);
}
