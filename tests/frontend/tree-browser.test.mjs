import test from 'node:test';
import assert from 'node:assert/strict';
import { visibleViews, browseNodes, flattenNodes } from '../../web/src/features/tree/browserModel.js';

const features = [
  { id: 'scope', name: '文件', parent_id: null, node_type: 'branch' },
  { id: 'nested', name: '文档', parent_id: 'scope', node_type: 'branch' },
  { id: 'leaf', name: '读取', parent_id: 'nested', node_type: 'leaf' },
];
const view = (id, status = 'candidate', updated_at = '2026-09-10', run_status = 'waiting_revision') => ({ id, status, updated_at, run_status, features });

test('published and candidate versions retain distinct node identities', () => {
  const nodes = flattenNodes(browseNodes(visibleViews([view('release', 'formal'), view('draft')], 'all', false)));
  assert.equal(nodes.filter(node => node.id === 'leaf').length, 2);
  assert.equal(new Set(nodes.map(node => node.key)).size, 6);
  assert.deepEqual(nodes.find(node => node.key === 'draft:leaf').ancestors, ['draft:scope', 'draft:nested']);
});
test('latest active candidate per scope is default; history preserves older and cancelled snapshots', () => {
  const views = [view('old', 'candidate', '2026-09-08'), view('new'), view('cancelled', 'candidate', '2026-09-11', 'cancelled')];
  assert.deepEqual(visibleViews(views, 'all', false).map(row => row.id), ['new']);
  assert.equal(visibleViews(views, 'all', true).length, 3);
  assert.equal(visibleViews(views, 'formal', false).length, 0);
});
test('leaf search preserves ancestors and branch search retains descendants', () => {
  assert.deepEqual(flattenNodes(browseNodes([view('draft')], '读取')).map(node => node.id), ['scope', 'nested', 'leaf']);
  assert.equal(flattenNodes(browseNodes([view('draft')], '文件')).length, 3);
  assert.deepEqual(browseNodes([view('draft')], '相机'), []);
});
