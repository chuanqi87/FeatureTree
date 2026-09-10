import { useState } from "react";
import { Alert, Button, Card, Checkbox, Form, Input, Select, message } from "antd";
import { get, post } from "../../shared/api.js";
import { useResource } from "../../shared/useResource.js";
import { JsonDetails } from "../../shared/components.jsx";

export default function CalibrationApproval({ candidates, releaseId, onSaved }) {
  const [treeRef, setTreeRef] = useState(null), [busy, setBusy] = useState(false), [accepted, setAccepted] = useState(false);
  const tree = useResource(treeRef ? `objects/${treeRef}` : null);
  const config = useResource("config");
  const trees = candidates.filter(row => row.tree_ref);
  const samples = candidates.filter(row => row.article_ref && row.draft);
  async function submit(values) {
    setBusy(true);
    try {
      const policy = await post("policies/snapshot", {}, releaseId);
      await post("calibrations/approve", { request: { ...values, tree_ref: treeRef, ...policy, decision: "approved" } }, releaseId);
      message.success("已记录具体版本的校准确认"); onSaved();
    } catch (error) { message.error(error.message); } finally { setBusy(false); }
  }
  return <Card title="确认校准成果" size="small"><Alert type="info" showIcon title="请先检查候选骨架、代表叶子、知识样稿和评级标准，再确认。确认不自动冻结或发布。" />
    <Form layout="vertical" onFinish={submit}>
      <Form.Item label="已审查的候选树" required><Select value={treeRef} onChange={setTreeRef} options={trees.map(row => ({ value: row.tree_ref, label: `${row.run_id} / ${row.work_id}` }))} /></Form.Item>
      <Form.Item name="scope_ids" label="本次确认的领域入口" rules={[{ required: true }]}><Select mode="multiple" options={(tree.data?.object?.features || []).map(row => ({ value: row.id, label: row.name }))} /></Form.Item>
      <Form.Item name="sample_article_refs" label="已审查的代表知识样稿" rules={[{ required: true }]}><Select mode="multiple" options={samples.map(row => ({ value: row.article_ref, label: `${row.run_id} / ${row.feature_id}` }))} /></Form.Item>
      <JsonDetails title="粒度与评级规则" value={config.data?.policies} />
      <Form.Item name="actor" label="审核人" rules={[{ required: true }]}><Input /></Form.Item>
      <Checkbox checked={accepted} onChange={event => setAccepted(event.target.checked)}>我已审查上述具体成果与规则，并确认其作为后续扩展依据</Checkbox>
      <div style={{ marginTop: 12 }}><Button htmlType="submit" loading={busy} disabled={!accepted || !treeRef}>记录校准确认</Button></div>
    </Form>
  </Card>;
}
