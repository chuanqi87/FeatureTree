import { Button, Card, Space, Table, Tag, Typography } from "antd";

const labels = {
  must_split: "超过 50，必须拆分",
  split_recommended: "超过 40，继续细分",
  needs_research: "API 清单未完整",
  leaf_eligible: "规模允许停止，仍需能力边界验收",
};

export default function ApiAssessment({ run, workflow, onError }) {
  const rows = run.api_assessments || [];
  if (!rows.length) return null;
  const next = run.next_work_orders || [];
  async function analyzeNext() {
    try {
      await workflow.create({
        parent_run: run.id,
        nodes: next.map((row) => row.node_id),
        action: "drilldown",
        depth: 1,
        model: run.model,
        max_nodes: run.max_nodes,
        workers: run.workers,
        timeout: run.timeout,
        first_response_timeout: run.first_response_timeout || 120,
      });
    } catch (error) {
      onError(error.message);
    }
  }
  return (
    <Card title="按平台评估 API 规模">
      <Typography.Paragraph type="secondary">
        各平台独立去重计数，目标 ≤40，任一端 &gt;50 必须拆分。“≥”表示清单不完整，不能据此判定为末级能力。
      </Typography.Paragraph>
      <Table
        size="small"
        rowKey="node_id"
        dataSource={rows}
        pagination={false}
        columns={[
          { title: "节点", dataIndex: "node_id" },
          ...["android", "ios", "harmonyos"].map((platform) => ({
            title: platform,
            key: platform,
            render: (_, row) => {
              const value = row.platforms[platform];
              return `${value.completeness === "complete" ? "" : "≥"}${value.count}`;
            },
          })),
          { title: "评估", key: "decision", render: (_, row) => <Tag>{labels[row.decision]}</Tag> },
        ]}
        expandable={{
          expandedRowRender: (row) => (
            <Space direction="vertical">
              {Object.entries(row.platforms).map(([platform, value]) => (
                <Typography.Paragraph key={platform}>
                  <strong>{platform}：</strong>{value.apis.map((api) => api.id).join("、") || "尚无已识别 API"}
                </Typography.Paragraph>
              ))}
            </Space>
          ),
        }}
      />
      {next.length > 0 && (
        <Typography.Paragraph>
          {run.published
            ? <Button onClick={analyzeNext} loading={workflow.busy}>并行分析下一层的 {next.length} 个分支</Button>
            : "本层验收并合并后，可将这些分支一起派发到下一批分析。"}
        </Typography.Paragraph>
      )}
    </Card>
  );
}
