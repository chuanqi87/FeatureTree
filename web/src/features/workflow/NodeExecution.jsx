import { Alert, Button, Card, Space, Typography } from "antd";
import { nodeRuns } from "./model.js";
import RunList from "./RunList.jsx";

export default function NodeExecution({
  node,
  model,
  workflow,
  onAnalyze,
  onSelectRun,
}) {
  const runs = nodeRuns(workflow.runs, node.id);
  return (
    <Card
      title="节点分析"
      extra={
        <Space wrap>
          <Button
            type="primary"
            onClick={() => onAnalyze(node.id, "drilldown")}
            disabled={
              node.granularity !== "branch" || !workflow.config?.available
            }
          >
            下钻分析
          </Button>
          <Button
            onClick={() => onAnalyze(node.id, "root")}
            disabled={!workflow.config?.available}
          >
            根节点分析
          </Button>
        </Space>
      }
    >
      <Typography.Paragraph type="secondary">
        下钻分析细化当前分支；根节点分析从所属 L1
        领域开始。执行期间可关闭详情，任务会继续运行。
      </Typography.Paragraph>
      {node.granularity !== "branch" && (
        <Typography.Paragraph type="secondary">
          当前节点已标为能力叶子，可从所属根节点发起结构分析。
        </Typography.Paragraph>
      )}
      {workflow.error && <Alert type="error" showIcon title={workflow.error} />}
      <RunList
        compact
        runs={runs}
        model={model}
        onSelect={onSelectRun}
        loading={workflow.loading}
      />
    </Card>
  );
}
