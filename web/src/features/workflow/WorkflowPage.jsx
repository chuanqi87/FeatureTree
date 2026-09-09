import { Alert, Button, Card, Space, Typography } from "antd";
import { PlusOutlined, ReloadOutlined } from "@ant-design/icons";
import RunList from "./RunList.jsx";
import RunDetails from "./RunDetails.jsx";

export default function WorkflowPage({
  workflow,
  model,
  onCreate,
  onSelect,
  onPublished,
}) {
  return (
    <div className="workflow-page">
      <div className="page-heading">
        <div>
          <Typography.Title level={3}>分析任务</Typography.Title>
          <Typography.Text type="secondary">
            按节点发起、跟踪和验收能力树分析
          </Typography.Text>
        </div>
        <Space>
          <Button icon={<ReloadOutlined />} onClick={workflow.refresh}>
            刷新
          </Button>
          <Button
            type="primary"
            icon={<PlusOutlined />}
            onClick={onCreate}
            disabled={!model || !workflow.config?.available}
          >
            新建分析
          </Button>
        </Space>
      </div>
      {workflow.error && (
        <Alert
          type="error"
          showIcon
          title="任务数据读取失败"
          description={workflow.error}
        />
      )}
      <Card title="任务列表">
        <RunList
          runs={workflow.runs}
          loading={workflow.loading}
          model={model}
          onSelect={onSelect}
        />
      </Card>
      <RunDetails
        key={workflow.detail?.id || "empty"}
        run={workflow.detail}
        workflow={workflow}
        model={model}
        onPublished={onPublished}
      />
    </div>
  );
}
