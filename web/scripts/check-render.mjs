import assert from 'node:assert/strict';
import { createElement } from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import { createServer } from 'vite';
const server = await createServer({ server: { middlewareMode: true }, appType: 'custom' });
try {
  const components = ['tree/TreePage', 'sources/SourcesPage', 'workflow/WorkflowPage', 'knowledge/KnowledgePage', 'review/ReviewPage', 'release/ReleasePage'];
  for (const component of components) {
    const module = await server.ssrLoadModule(`/src/features/${component}.jsx`);
    const html = renderToStaticMarkup(createElement(module.default, { releaseId: null, navigate() {}, onPublished() {} }));
    assert(!html.includes('[object Object]'));
    assert(html.length > 200);
  }
  const { default: Article } = await server.ssrLoadModule('/src/features/knowledge/Article.jsx');
  const article = { draft: true, overall_confidence: 'low', claims: [{ claim_id: 'unknown', platforms: ['android'], dimension: 'capability_result', result: 'unknown', statement: '<img src=x onerror=alert(1)>', conditions: [], gaps: ['Unknown baseline'], coverage_note: '', premise_ids: [], evidence_refs: [] }], assessments: [{ claim_id: 'unknown', level: 'low', reason: 'Unverified applicability' }], evidence: [], confidence_reasons: ['unknown'], dependencies: {} };
  const html = renderToStaticMarkup(createElement(Article, { article, reference: 'example' }));
  assert(html.includes('校准样稿'));
  assert(html.includes('决定整体评级的结论'));
  assert(html.includes('&lt;img'));
  assert(!html.includes('<img src=x'));
  const { default: BatchProgress } = await server.ssrLoadModule('/src/features/workflow/BatchProgress.jsx');
  const progress = renderToStaticMarkup(createElement(BatchProgress, { progress: { completed: 2, total: 5, reused: 1, current: 3, status: 'failed' } }));
  assert(progress.includes('已校验批次 2 / 5'));
  assert(progress.includes('复用 1 批'));
  assert(progress.includes('第 3 批失败，已完成批次保留'));
  assert.equal(renderToStaticMarkup(createElement(BatchProgress)), '');
  const { default: LiveActivity, ActivityOverview } = await server.ssrLoadModule('/src/features/workflow/LiveActivity.jsx');
  const activity = { status: 'running', scheduler_status: 'failed', checkpoint_errors: [], completed: 1, total: 16, accepted: [{ batch: 1, api_count: 32, topic_count: 0, fact_count: 8, outcome: 'completed_with_gaps', result_ref: 'abc' }], live: { recovery: true, process_alive: true, batch: 2, last_activity_at: '2026-09-10T13:00:00Z', api_ids: ['API'], topic_ids: [], source_calls: 5, payload_chunks: 2, events: [] } };
  const liveHtml = renderToStaticMarkup(createElement(LiveActivity, { activity, onArtifact() {} }));
  assert(liveHtml.includes('恢复续跑'));
  assert(liveHtml.includes('原尝试失败'));
  assert(liveHtml.includes('查看内容'));
  const overview = renderToStaticMarkup(createElement(ActivityOverview, { activity: { active_stages: 3, completed_batches: 7, total_batches: 56, observed_at: '2026-09-10T13:00:00Z' }, model: 'test/model' }));
  assert(overview.includes('7 / 56'));
  console.log('Rendered six v2 pages and a low-confidence article; escaped source text and draft status verified.');
} finally { await server.close(); }
