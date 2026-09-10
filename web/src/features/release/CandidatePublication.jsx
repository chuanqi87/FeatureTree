import { useState } from "react";
import { Button, Card, Form, Select, message } from "antd";
import { get, post } from "../../shared/api.js";
export default function CandidatePublication({ candidates, freezes, releaseId, onPrepared }) {
  const [freezeRef, setFreezeRef] = useState(null), [busy, setBusy] = useState(false);
  async function prepare(values) {
    setBusy(true);
    try {
      const frozen = freezes.find(row => row.freeze_ref === freezeRef).freeze;
      const previous = releaseId ? await get(`releases/${releaseId}`) : { source_ids: [], freeze_refs: [], knowledge_refs: {} };
      const selected = candidates.filter(row => values.article_refs.includes(row.article_ref));
      const candidate = { tree_ref: frozen.tree_ref, bindings_ref: frozen.bindings_ref, baseline_ref: frozen.baseline_ref, source_ids: [...new Set([...previous.source_ids, frozen.snapshot_id])], freeze_refs: [...new Set([...previous.freeze_refs, freezeRef])], knowledge_refs: { ...previous.knowledge_refs, ...Object.fromEntries(selected.map(row => [row.feature_id, row.article_ref])) } };
      const result = await post("releases/prepare", { candidate }, releaseId);
      onPrepared(result.key); message.success("候选版本已通过准备校验，请检查差异后提交发布");
    } catch (error) { message.error(error.message); } finally { setBusy(false); }
  }
  return <Card title="准备正式发布" size="small"><Form layout="vertical" onFinish={prepare}>
    <Form.Item label="冻结范围" required><Select value={freezeRef} onChange={setFreezeRef} options={freezes.map(row => ({ value: row.freeze_ref, label: `${row.freeze.leaf_ids.length} 个叶子 · ${row.freeze.created_at}` }))} /></Form.Item>
    <Form.Item name="article_refs" label="已经完成评级的正式知识" rules={[{ required: true }]}><Select mode="multiple" options={candidates.filter(row => row.article_ref && !row.draft).map(row => ({ value: row.article_ref, label: `${row.feature_id} · ${row.overall_confidence}` }))} /></Form.Item>
    <Button htmlType="submit" disabled={!freezeRef} loading={busy}>准备发布</Button>
    {releaseId && <p>本次使用所选冻结树与绑定，保留现有知识并合并所选文章；提交前请检查结构变化及失效报告。</p>}
  </Form></Card>;
}
