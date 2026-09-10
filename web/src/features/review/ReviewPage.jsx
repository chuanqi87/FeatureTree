import { useEffect, useState } from "react";
import { Alert, Button, Drawer, Form, Input, Select, Space, Table, Typography, message } from "antd";
import { useResource } from "../../shared/useResource.js";
import { post } from "../../shared/api.js";
import { PageHeader, ResourceState, Status, JsonDetails } from "../../shared/components.jsx";
import Article from "../knowledge/Article.jsx";
export default function ReviewPage({ releaseId, onPublished, context }) {
  const queue = useResource("reviews", 8000);
  const [selected, setSelected] = useState(null), [claim, setClaim] = useState(null), [busy, setBusy] = useState(false);
  const detail = useResource(selected ? `reviews/${selected}` : null);
  const [form] = Form.useForm();
  useEffect(() => {
    if (!context?.article_ref || !queue.data) return;
    const ticket = queue.data.tickets.find(row => row.article_ref === context.article_ref);
    if (ticket) { setSelected(ticket.id); setClaim(context.claim_id || null); }
  }, [context, queue.data?.release_id]);
  async function submit(values) {
    setBusy(true);
    try {
      const item = detail.data.items.find(row => row.claim_id === claim);
      await post(`reviews/${selected}/decisions`, { article_ref: detail.data.article_ref, decision: { claim_id: claim, claim_hash: item.claim_hash, action: values.action, reason: values.reason, actor: values.actor, evidence_refs: values.evidence ? values.evidence.split(/\s+/).filter(Boolean) : [], target_stage: values.target || null, replacement: values.correction ? { statement: values.correction } : null } }, releaseId);
      message.success("裁决已保存；需要重研的结论已交回责任阶段"); detail.refresh(); queue.refresh(); onPublished(); setClaim(null);
    } catch (error) { message.error(error.message); } finally { setBusy(false); }
  }
  return <><PageHeader title="人工审核" description="低可信知识按版本进入队列；每项裁决绑定具体结论指纹，过期提交会被拒绝。" />
    <ResourceState resource={queue}><Table rowKey="id" dataSource={queue.data?.tickets || []} columns={[{ title: "叶子 / 知识版本", render: (_, row) => <Button type="link" onClick={() => { setSelected(row.id); setClaim(null); }}>{row.feature_id}</Button> }, { title: "知识类型", render: (_, row) => row.draft ? "校准样稿" : "正式知识" }, { title: "审核状态", dataIndex: "state", render: value => <Status value={value} /> }, { title: "待处理结论", render: (_, row) => row.items.filter(item => item.state !== "decided").length }, { title: "版本", render: (_, row) => <Typography.Text copyable>{row.article_ref.slice(0, 16)}</Typography.Text> }]} /></ResourceState>
    <Drawer title="逐结论审核" open={!!selected} onClose={() => setSelected(null)} size="large"><ResourceState resource={detail}>{detail.data && <>
      <Table rowKey="claim_id" size="small" pagination={false} dataSource={detail.data.items} columns={[{ title: "结论", dataIndex: "claim_id" }, { title: "状态", dataIndex: "state", render: value => <Status value={value} /> }, { title: "操作", render: (_, row) => <Button onClick={() => { setClaim(row.claim_id); form.resetFields(); }}>填写裁决</Button> }]} />
      {claim && <Form form={form} layout="vertical" onFinish={submit} style={{ margin: "20px 0" }} initialValues={{ action: "accept_limitations" }}>
        <Alert type="info" title="接受已说明的限制可以结束审核，但保持低可信。修正或补充证据将重新触发研究与评级。" />
        <Form.Item name="action" label="裁决动作" rules={[{ required: true }]}><Select options={[['accept_limitations','接受已说明的限制'],['request_research','要求指定阶段重研'],['correct','修正结论'],['add_evidence','补充证据'],['unknown','仍无法判断'],['defer','暂缓'],['start','开始审核']].map(([value,label]) => ({value,label}))} /></Form.Item>
        <Form.Item name="reason" label="理由 / 待核实问题" rules={[{ required: true }]}><Input.TextArea rows={3} /></Form.Item>
        <Form.Item name="actor" label="审核人" rules={[{ required: true }]}><Input /></Form.Item>
        <Form.Item name="target" label="责任阶段（留空则按结论类型分配）"><Select allowClear options={["fk-scope","fk-android","fk-ios","fk-harmonyos","fk-compare","fk-confidence","ft-design"].map(value => ({ value, label: value }))} /></Form.Item>
        <Form.Item name="correction" label="修正后的表述"><Input.TextArea /></Form.Item><Form.Item name="evidence" label="补充的封存证据引用"><Input.TextArea placeholder="多个引用以空白分隔" /></Form.Item>
        <Space><Button type="primary" htmlType="submit" loading={busy}>提交版本化裁决</Button><Button onClick={() => setClaim(null)}>取消填写</Button></Space>
      </Form>}
      <JsonDetails value={detail.data.items.map(row => row.last_event).filter(Boolean)} title="已记录的人工裁决" /><Article article={detail.data.article} reference={detail.data.article_ref} />
    </>}</ResourceState></Drawer>
  </>;
}
