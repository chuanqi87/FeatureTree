import { Button, Progress, Space, Table, Tag, Typography } from "antd";
import { workflowStates } from "./model.js";

export function RunStatus({ status }) {
  const [label, color] = workflowStates[status] || [status, "default"];
  return <Tag color={color}>{label}</Tag>;
}

export default function RunList({
  runs,
  model,
  onSelect,
  loading,
  compact = false,
}) {
  const columns = [
    {
      title: "分析范围",
      key: "scope",
      render: (_, run) => (
        <div>
          <Button
            type="link"
            className="workflow-run-link"
            onClick={() => onSelect(run.id)}
          >
            {run.nodes
              .map((id) => model?.byId.get(id)?.name.zh || id)
              .join("、")}
          </Button>
          <div>
            <Typography.Text type="secondary">
              {run.trigger?.action === "root" ? "根节点分析" : "下钻分析"} ·{" "}
              {run.depth} 层
            </Typography.Text>
          </div>
        </div>
      ),
    },
    {
      title: "状态",
      key: "state",
      width: 145,
      render: (_, run) => (
        <Space orientation="vertical" size={2}>
          <RunStatus status={run.status} />
          {run.stale_rules && <Tag>规则已更新</Tag>}
        </Space>
      ),
    },
    {
      title: "阶段进度",
      key: "progress",
      width: 150,
      render: (_, run) => (
        <div>
          <Progress
            size="small"
            percent={Math.round(
              (run.state_counts.succeeded / Math.max(1, run.total_tasks)) * 100,
            )}
            showInfo={false}
          />
          <Typography.Text type="secondary">
            {run.state_counts.succeeded} / {run.total_tasks} 个阶段
          </Typography.Text>
        </div>
      ),
    },
    ...(!compact
      ? [
          {
            title: "创建时间",
            dataIndex: "created_at",
            width: 180,
            render: (value) =>
              new Date(value).toLocaleString("zh-CN", { hour12: false }),
          },
        ]
      : []),
  ];
  return (
    <Table
      rowKey="id"
      columns={columns}
      dataSource={runs}
      loading={loading}
      size="small"
      pagination={runs.length > 10 ? { pageSize: 10 } : false}
      scroll={{ x: 540 }}
      locale={{ emptyText: "还没有分析任务。从节点详情发起一次分析。" }}
    />
  );
}
