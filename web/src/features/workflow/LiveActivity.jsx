import { Alert, Button, Card, Collapse, Descriptions, Progress, Space, Table, Tag, Typography } from "antd";

const labels = { running: "正在执行", failed: "执行失败", completed: "执行结束", awaiting_inspection: "进程已停止，待核查", waiting: "等待依赖" };
export function ActivityOverview({ activity, model }) {
  if (!activity) return null;
  return <Card size="small" title="实时执行总览">
    <Space wrap><Tag color="blue">{activity.active_stages} 个阶段正在执行</Tag><span>已校验 {activity.completed_batches} / {activity.total_batches} 批</span><span>{model}</span></Space>
    <Progress percent={activity.total_batches ? Math.round(activity.completed_batches / activity.total_batches * 100) : 0} />
    <Typography.Text type="secondary">每 4 秒刷新 · 最近观测 {new Date(activity.observed_at).toLocaleTimeString()} · 批次通过校验不代表知识审核完成</Typography.Text>
  </Card>;
}
export function ActivityBadge({ activity }) {
  if (!activity) return null;
  return <Tag color={activity.status === "running" ? "blue" : activity.status === "failed" ? "red" : undefined}>{activity.live?.recovery && "恢复续跑 · "}{labels[activity.status] || activity.status}</Tag>;
}
export default function LiveActivity({ activity, onArtifact }) {
  if (!activity) return null;
  const live = activity.live;
  return <Space orientation="vertical" style={{ width: "100%" }}>
    <ActivityBadge activity={activity} />
    {activity.scheduler_status === "failed" && activity.status === "running" && <Alert type="info" title="原尝试失败，恢复任务正在执行。通过校验的批次将由正常重试流程接回。" />}
    {activity.checkpoint_errors.length > 0 && <Alert type="error" title="部分检查点读取或身份校验异常，未计入完成数" />}
    {live && <Descriptions size="small" column={2} items={[
      { key: "batch", label: "当前批次", children: live.batch || "阶段任务" },
      { key: "process", label: "进程", children: live.process_alive ? "运行中" : "已结束" },
      { key: "time", label: "最新日志", children: new Date(live.last_activity_at).toLocaleString() },
      { key: "sources", label: "来源工具调用", children: live.source_calls },
      { key: "chunks", label: "已写交付块", children: live.payload_chunks },
      { key: "file", label: "交付文件", children: live.file_completed ? "已写入，验收状态见下表" : "尚未完成" },
    ]} />}
    {live && <Collapse items={[
      { key: "inputs", label: `当前研究输入：${live.api_ids.length} 个 API、${live.topic_ids.length} 个主题`, children: <div style={{ maxHeight: 260, overflow: "auto" }}>{[...live.api_ids, ...live.topic_ids].map(id => <Typography.Paragraph key={id} copyable>{id}</Typography.Paragraph>)}</div> },
      { key: "events", label: "最近执行活动", children: <Table size="small" pagination={false} rowKey={(_, i) => i} dataSource={live.events} columns={[{ title: "时间", dataIndex: "timestamp", render: value => value ? new Date(value).toLocaleTimeString() : "—" }, { title: "事件", dataIndex: "type" }, { title: "工具", dataIndex: "tool" }, { title: "状态", render: (_, row) => row.status || row.reason || "—" }]} /> },
    ]} />}
    <Typography.Text strong>已校验产物 · {activity.completed} / {activity.total} 批</Typography.Text>
    <Table size="small" rowKey="batch" dataSource={activity.accepted} pagination={{ pageSize: 6 }} columns={[
      { title: "批次", dataIndex: "batch" }, { title: "API", dataIndex: "api_count" }, { title: "主题", dataIndex: "topic_count" }, { title: "事实", dataIndex: "fact_count" },
      { title: "结论状态", dataIndex: "outcome" }, { title: "产物", render: (_, row) => <Button size="small" onClick={() => onArtifact(row.result_ref)}>查看内容</Button> },
    ]} />
  </Space>;
}
