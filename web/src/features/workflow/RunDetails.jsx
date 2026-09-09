import { useState } from "react";
import {
  Alert,
  Button,
  Card,
  Descriptions,
  Space,
  Table,
  Typography,
} from "antd";
import { stageNames } from "./model.js";
import { RunStatus } from "./RunList.jsx";
import StageResult from "./StageResult.jsx";

export default function RunDetails({ run, workflow, model, onPublished }) {
  const [error, setError] = useState("");
  if (!run) return null;
  async function act(action) {
    setError("");
    try {
      await workflow.act(
        run.id,
        action,
        action === "revise" ? { nodes: run.nodes } : {},
      );
      if (action === "publish") onPublished();
    } catch (problem) {
      setError(problem.message);
    }
  }
  return (
    <div className="workflow-detail-stack">
      <Card
        title={
          <Space wrap>
            任务详情 <RunStatus status={run.status} />
          </Space>
        }
        extra={
          <Space wrap>
            {Object.entries({
              start: "开始 / 恢复执行",
              retry: "重试失败阶段",
              revise: "按审查意见返工",
              publish: "合并到正式树",
            })
              .filter(([action]) => run.actions[action])
              .map(([action, label]) => (
                <Button
                  key={action}
                  type={
                    action === "publish" || action === "start"
                      ? "primary"
                      : "default"
                  }
                  loading={workflow.busy}
                  onClick={() => act(action)}
                >
                  {label}
                </Button>
              ))}
          </Space>
        }
      >
        {error && (
          <Alert type="error" showIcon title="操作未完成" description={error} />
        )}
        {run.stale_rules && (
          <Alert
            type="warning"
            showIcon
            title="工作流规则已更新"
            description="此任务的历史结果仍可查看，请新建分析任务以使用当前规则。"
          />
        )}
        {run.execution_error && (
          <Alert
            type="error"
            showIcon
            title="执行进程未启动"
            description={run.execution_error}
          />
        )}
        <Typography.Paragraph copyable={{ text: run.id }} type="secondary">
          {run.id}
        </Typography.Paragraph>
        <Descriptions
          size="small"
          column={2}
          items={[
            {
              key: "nodes",
              label: "分析范围",
              children: run.nodes
                .map((id) => model?.byId.get(id)?.name.zh || id)
                .join("、"),
            },
            { key: "depth", label: "下钻层数", children: run.depth },
            {
              key: "budget",
              label: "执行预算",
              children: `${run.workers} 并发 · 每节点最多 ${run.max_nodes} 个候选`,
            },
            {
              key: "model",
              label: "模型",
              children: run.model || "OpenCode 默认模型",
            },
            {
              key: "baseline",
              label: "基线日期",
              children: run.baseline.as_of,
            },
            {
              key: "versions",
              label: "平台版本",
              children: Object.entries(run.baseline.platforms)
                .map(
                  ([p, b]) =>
                    `${p}: ${b.status === "verified" ? b.release : "待核实"}`,
                )
                .join(" / "),
            },
          ]}
        />
      </Card>
      <Card title="执行阶段" styles={{ body: { padding: 0 } }}>
        <Table
          size="small"
          rowKey="id"
          dataSource={run.tasks}
          pagination={false}
          columns={[
            {
              title: "阶段",
              key: "stage",
              render: (_, task) => (
                <div>
                  {stageNames[task.stage] || task.stage}
                  <div>
                    <Typography.Text type="secondary">
                      {task.node || "整批任务"}
                    </Typography.Text>
                  </div>
                </div>
              ),
            },
            {
              title: "状态",
              dataIndex: "status",
              render: (s) => <RunStatus status={s} />,
            },
            {
              title: "尝试次数",
              key: "attempts",
              render: (_, t) => t.attempts.length,
            },
          ]}
          expandable={{
            expandedRowRender: (task) => <StageResult task={task} />,
            rowExpandable: (task) =>
              Boolean(task.payload || task.attempts.length),
          }}
        />
      </Card>
      <Card title={`候选结果 · ${run.additions.total} 个节点`}>
        <Typography.Paragraph type="secondary">
          {run.additions.branches} 个分支、{run.additions.atomic_leaves}{" "}
          个能力叶子。阶段完成数量不代表能力覆盖率。
        </Typography.Paragraph>
        <Table
          size="small"
          rowKey="id"
          dataSource={run.nodes_proposed}
          pagination={{ pageSize: 8, hideOnSinglePage: true }}
          scroll={{ x: 620 }}
          columns={[
            {
              title: "节点",
              key: "name",
              width: 210,
              render: (_, n) => (
                <>
                  {n.name.zh}
                  <div>
                    <Typography.Text type="secondary">{n.id}</Typography.Text>
                  </div>
                </>
              ),
            },
            { title: "层级", dataIndex: "level", width: 70 },
            {
              title: "类型",
              dataIndex: "granularity",
              width: 80,
              render: (v) => (v === "atomic" ? "能力叶子" : "分支"),
            },
            { title: "定义", dataIndex: "definition" },
          ]}
          locale={{ emptyText: "候选结构尚未生成" }}
        />
      </Card>
    </div>
  );
}
