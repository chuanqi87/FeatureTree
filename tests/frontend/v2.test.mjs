import assert from 'node:assert/strict';
import test from 'node:test';
import { treeRows, trusted, safeUrl } from '../../web/src/shared/model.js';

test('tree identity survives moving a node and empty branches remain branches', () => {
  const rows = treeRows([{ id: 'a', parent_id: null, node_type: 'branch' }, { id: 'b', parent_id: null, node_type: 'branch' }, { id: 'stable', parent_id: 'b', node_type: 'leaf' }]);
  assert.equal(rows[0].node_type, 'branch');
  assert.equal(rows[1].children[0].id, 'stable');
});
test('low, stale and manually invalidated articles are not trusted results', () => {
  assert.equal(trusted({ validity: 'current', confidence: 'high' }), true);
  for (const summary of [{ validity: 'current', confidence: 'low' }, { validity: 'stale', confidence: 'high' }, { validity: 'invalidated', confidence: 'high' }, { validity: 'candidate', confidence: 'high' }]) assert.equal(trusted(summary), false);
});
test('source links cannot execute injected scripts', () => {
  assert.equal(safeUrl('javascript:alert(1)'), null);
  assert.equal(safeUrl('data:text/html,test'), null);
  assert.equal(safeUrl('https://developer.android.com/reference/test'), 'https://developer.android.com/reference/test');
});
