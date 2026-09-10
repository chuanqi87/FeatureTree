import { useState } from "react";
import { Alert, Button, Form, Input, Modal, Select, message } from "antd";
import { get, post } from "../../shared/api.js";
import { useResource } from "../../shared/useResource.js";
export default function KnowledgePlan({ candidates, releaseId, onCreated }) {
  const freezes = useResource("freezes");
  const [open, setOpen] = useState(false), [source, setSource] = useState(null), [busy, setBusy] = useState(false);
  const options = [...(freezes.data?.items || []).map(row => ({ value: row.freeze_ref, label: `正式冻结 · ${row.freeze.leaf_ids.length} 个叶子`, freeze_ref: row.freeze_ref, ...row.freeze })), ...candidates.filter(row => row.tree_ref).map(row => ({ value: row.tree_ref, label: `校准候选 · ${row.run_id}/${row.work_id}`, ...row }))];
  const selected = options.find(row => row.value === source);
  const tree = useResource(selected ? `objects/${selected.tree_ref}` : null);
  async function submit(values) {
    setBusy(true);
    try {
      let request;
      if (selected.freeze_ref) request = { freeze_ref: selected.freeze_ref, ...values };
      else {
        const run = await get(`runs/${selected.run_id}`);
        request = { tree_ref: selected.tree_ref, bindings_ref: selected.bindings_ref, baseline_ref: run.plan.works.find(row => row.id === selected.work_id).inputs.baseline_ref, ...values };
      }
      const result = await post("knowledge/plans", { request }, releaseId);
      message.success(`已创建叶子研究：${result.run_id}`); setOpen(false); onCreated();
    } catch (error) { message.error(error.message); } finally { setBusy(false); }
  }
  return <><Button type="primary" onClick={() => setOpen(true)}>规划叶子知识</Button><Modal title="规划具名 Agent 知识研究" open={open} onCancel={() => setOpen(false)} footer={null}>
    <Alert type="info" title="冻结范围产生正式候选知识；未冻结的树只产生校准样稿。" />
    <Form layout="vertical" onFinish={submit}>
      <Form.Item label="固定的树或冻结范围" required><Select options={options} value={source} onChange={setSource} /></Form.Item>
      <Form.Item name="feature_ids" label="研究叶子" rules={[{ required: true }]}><Select mode="multiple" options={(tree.data?.object?.features || []).filter(row => row.node_type === "leaf" && (!selected?.leaf_ids || selected.leaf_ids.includes(row.id))).map(row => ({ value: row.id, label: row.name }))} /></Form.Item>
      <Form.Item name="model" label="执行模型" rules={[{ required: true }]}><Input placeholder="provider/model" /></Form.Item>
      <Button htmlType="submit" type="primary" disabled={!selected} loading={busy}>创建固定工作单</Button>
    </Form>
  </Modal></>;
}
