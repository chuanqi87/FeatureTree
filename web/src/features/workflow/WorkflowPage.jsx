import { useState } from "react";
import { Alert, Button, Card, Descriptions, Drawer, Form, Input, Modal, Select, Space, Table, Typography, message } from "antd";
import { post } from "../../shared/api.js";
import { useResource } from "../../shared/useResource.js";
import { ArtifactDrawer, JsonDetails, PageHeader, ResourceState, Status } from "../../shared/components.jsx";
export default function WorkflowPage({ releaseId }) {
  const runs = useResource("runs", 4000), sources = useResource("sources");
  const [selected, setSelected] = useState(null), [create, setCreate] = useState(false), [artifact, setArtifact] = useState(null), [stage, setStage] = useState(null), [busy, setBusy] = useState(false);
  const detail = useResource(selected ? `runs/${selected}` : null, selected ? 4000 : 0);
  const [form] = Form.useForm();
  async function act(action, taskId, workId) {
    setBusy(true);
    try { const result = await post(`runs/${selected}/actions`, { action, task_id: taskId, work_id: workId, feedback: [{ reason: "用户要求重新审查当前阶段" }] }, releaseId); if (action === "supplement" && result.run_id) setSelected(result.run_id); detail.refresh(); runs.refresh(); }
    catch (error) { message.error(error.message); } finally { setBusy(false); }
  }
  async function createRun(values) {
    setBusy(true);
    try {
      const result = await post("runs", { request: { pipeline: "taxonomy", model: values.model, scopes: [{ definition: values.definition, snapshot_id: values.snapshot, selection: { query: values.query || "" }, topic_selection: { query: values.query || "" }, inputs: { baseline_ref: values.baseline }, work_type: "skeleton", mode: "calibration" }] } }, releaseId);
      setCreate(false); setSelected(result.run_id); runs.refresh(); message.success("工作单已固定，可检查输入后启动");
    } catch (error) { message.error(error.message); } finally { setBusy(false); }
  }
  const tasks = detail.data ? Object.values(detail.data.state.tasks) : [];
  const selectedStage = tasks.find(row => row.id === stage);
  return <><PageHeader title="具名 Agent 工作流" description="建树链与知识链各司其职，每个阶段都有输入、交付件、问题和返工历史。"><Button type="primary" onClick={() => setCreate(true)}>创建校准工作单</Button></PageHeader>
    <ResourceState resource={runs}><Table rowKey="run_id" size="small" dataSource={runs.data?.items || []} pagination={{ pageSize: 8 }} columns={[{ title: "运行", dataIndex: "run_id", render: value => <Button type="link" onClick={() => setSelected(value)}>{value}</Button> }, { title: "状态", dataIndex: "status", render: value => <Status value={value} /> }, { title: "更新时间", dataIndex: "updated_at" }]} /></ResourceState>
    <ResourceState resource={detail}>{detail.data && <><PageHeader title={detail.data.plan.pipeline === "taxonomy" ? "建树分析链" : "叶子知识链"} description={selected}><Button loading={busy} onClick={() => act("start")}>启动 / 继续</Button><Button danger onClick={() => act("cancel")}>取消运行</Button></PageHeader>
      <Status value={detail.data.state.status} /><div className="stage-grid">{tasks.map(task => <Card key={task.id} size="small" title={detail.data.plan.stage_configs[task.stage_id].definition.agent_name || `代码：${task.stage_id}`} extra={<Status value={task.status} />}>
        <Space orientation="vertical"><Typography.Text type="secondary">{task.reuse_ref ? "已复用兼容交付 · " : ""}{task.work_id} · 修订 {task.revision} · {task.attempts.length} 次尝试</Typography.Text>{task.outcome && <Status value={task.outcome} />}<Space><Button size="small" onClick={() => setStage(task.id)}>查看阶段</Button>{task.reuse_ref && <Button size="small" onClick={() => setArtifact(task.reuse_ref)}>复用依据</Button>}{task.result_ref && <Button size="small" onClick={() => setArtifact(task.result_ref)}>交付件</Button>}</Space></Space>
      </Card>)}</div><JsonDetails value={detail.data.plan.works} title="固定的范围、完整输入 ID 与上游版本" /></>}</ResourceState>
    <Modal title="创建校准工作单" open={create} onCancel={() => setCreate(false)} onOk={() => form.submit()} confirmLoading={busy}><Form form={form} layout="vertical" onFinish={createRun}>
      <Alert type="info" title="该入口产生候选分析；正式知识研究通过冻结叶子工作单创建。" />
      <Form.Item name="snapshot" label="来源快照" rules={[{ required: true }]}><Select options={sources.data?.items.map(row => ({ value: row.id, label: `${row.status} · ${row.id.slice(0, 18)}` }))} /></Form.Item>
      <Form.Item name="definition" label="公共能力范围与边界" rules={[{ required: true }]}><Input.TextArea rows={3} /></Form.Item>
      <Form.Item name="baseline" label="比较基线版本" rules={[{ required: true }, { pattern: /^[a-f0-9]{64}$/, message: "请选择已保存的基线对象版本" }]}><Input placeholder="已核对或明确标为历史的基线对象引用" /></Form.Item>
      <Form.Item name="query" label="来源检索条件（完整匹配集合进入工作单）"><Input placeholder="如 camera、JobScheduler；可先在来源页核对" /></Form.Item>
      <Form.Item name="model" label="已配置的执行模型" rules={[{ required: true }]}><Input placeholder="provider/model" /></Form.Item>
    </Form></Modal>
    <Drawer open={!!stage} title={selectedStage?.stage_id} onClose={() => setStage(null)} size="large">{selectedStage && <><Space wrap><Button onClick={() => act("retry", stage)} disabled={selectedStage.status !== "failed"}>重试执行</Button><Button onClick={() => act("revalidate", stage)} disabled={selectedStage.status !== "failed"}>复核保留答案</Button><Button onClick={() => act("revise", stage)}>定向修订</Button><Button onClick={() => act("supplement", stage, selectedStage.work_id)}>补充已提出的来源</Button></Space><JsonDetails value={detail.data.plan.stage_configs[selectedStage.stage_id].definition} title="Agent 职责、依赖与契约" /><JsonDetails value={selectedStage.attempts} title="每次尝试、实际模型用量与错误" /><JsonDetails value={selectedStage.history} title="被替代的交付件版本" /><JsonDetails value={selectedStage.feedback} title="返工问题" /></>}</Drawer>
    <ArtifactDrawer reference={artifact} onClose={() => setArtifact(null)} />
  </>;
}
