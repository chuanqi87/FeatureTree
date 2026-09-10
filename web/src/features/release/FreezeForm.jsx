import { useState } from "react";
import { Button, Card, Form, Select, message } from "antd";
import { get, post } from "../../shared/api.js";
import { useResource } from "../../shared/useResource.js";

export default function FreezeForm({ candidates, releaseId, approvals, onSaved }) {
  const [selected, setSelected] = useState(null), [busy, setBusy] = useState(false);
  const candidate = candidates.find(row => row.tree_ref === selected);
  const tree = useResource(selected ? `objects/${selected}` : null);
  async function submit(values) {
    setBusy(true);
    try {
      const run = await get(`runs/${candidate.run_id}`);
      const work = run.plan.works.find(row => row.id === candidate.work_id);
      const stages = ["ft-granularity", "ft-coverage", "ft-review", "ft-integrate"];
      const reviews = stages.map(stage => run.state.tasks[`${work.id}--${stage}`].result_ref);
      if (reviews.some(value => !value)) throw new Error("四份独立审查交付尚未完成");
      await post("freezes", { request: { ...values, tree_ref: candidate.tree_ref, bindings_ref: candidate.bindings_ref, baseline_ref: work.inputs.baseline_ref, snapshot_id: work.snapshot_id, review_refs: reviews } }, releaseId);
      message.success("领域已冻结，可以规划对应叶子的正式知识研究"); onSaved();
    } catch (error) { message.error(error.message); } finally { setBusy(false); }
  }
  return <Card title="冻结通过审查的领域" size="small"><Form layout="vertical" onFinish={submit}>
    <Form.Item label="候选树" required><Select value={selected} onChange={setSelected} options={candidates.filter(row => row.tree_ref).map(row => ({ value: row.tree_ref, label: `${row.run_id} / ${row.work_id}` }))} /></Form.Item>
    <Form.Item name="root_ids" label="冻结范围入口" rules={[{ required: true }]}><Select mode="multiple" options={(tree.data?.object?.features || []).map(row => ({ value: row.id, label: row.name }))} /></Form.Item>
    <Form.Item name="approval_ref" label="校准确认记录" rules={[{ required: true }]}><Select options={approvals.map(row => ({ value: row.approval_ref, label: `${row.approval.actor} · ${row.approval.created_at}` }))} /></Form.Item>
    <Button htmlType="submit" disabled={!candidate} loading={busy}>验证并冻结</Button>
  </Form></Card>;
}
