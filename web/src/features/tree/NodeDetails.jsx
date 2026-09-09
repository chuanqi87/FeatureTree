import { useState } from "react";
import { Breadcrumb, Button, Drawer, Space, Tabs, Tag, Typography } from "antd";
import { AimOutlined } from "@ant-design/icons";
import { StatusTag } from "../../shared/components/ValueFields.jsx";
import { NodeOverview } from "./details/NodeOverview.jsx";
export { NodeOverview } from "./details/NodeOverview.jsx";
import { NodeKnowledge } from "./details/NodeKnowledge.jsx";
export { NodeKnowledge } from "./details/NodeKnowledge.jsx";
import { NodeEvidence } from "./details/NodeEvidence.jsx";
export { NodeEvidence } from "./details/NodeEvidence.jsx";
import { NodeSource } from "./details/NodeSource.jsx";
export { NodeSource } from "./details/NodeSource.jsx";
import { NodeQuality } from "./details/NodeQuality.jsx";
import NodeExecution from "../workflow/NodeExecution.jsx";
export { NodeQuality } from "./details/NodeQuality.jsx";

export default function NodeDetails({
  explorer,
  workflow,
  onAnalyze,
  onSelectRun,
}) {
  const { model, selected, drawerOpen, setDrawerOpen, selectNode, locateNode } =
    explorer;
  const [tab, setTab] = useState("overview");
  const node = model?.byId.get(selected);
  if (!node) return null;
  const props = { node, model, onSelect: selectNode };
  return (
    <Drawer
      open={drawerOpen}
      onClose={() => setDrawerOpen(false)}
      title="节点详情"
      size="min(780px, 100vw)"
      extra={
        <Space>
          <Button
            type="primary"
            disabled={node.granularity !== "branch"}
            onClick={() => onAnalyze(node.id, "drilldown")}
          >
            下钻分析
          </Button>
          <Button onClick={() => onAnalyze(node.id, "root")}>根节点分析</Button>
          <Button icon={<AimOutlined />} onClick={() => locateNode()}>
            定位到树中
          </Button>
        </Space>
      }
      styles={{ body: { padding: 24, background: "#f5f5f5" } }}
    >
      <Breadcrumb
        className="node-breadcrumb"
        items={[...model.ancestors.get(selected), selected].map((id) => ({
          title: (
            <Button type="link" size="small" onClick={() => selectNode(id)}>
              {model.byId.get(id).name.zh}
            </Button>
          ),
        }))}
      />
      <div className="detail-title">
        <Typography.Title level={3}>{node.name.zh}</Typography.Title>
        <Space>
          <Tag color="blue">{node.level}</Tag>
          <StatusTag value={node.knowledge_role} />
          <StatusTag value={node.comparison_progress.state} />
        </Space>
      </div>
      <Typography.Paragraph type="secondary">
        {node.name.en}
      </Typography.Paragraph>
      <Typography.Paragraph copyable={{ text: node.id }} className="detail-id">
        {node.id}
      </Typography.Paragraph>
      <Tabs
        activeKey={tab}
        onChange={setTab}
        items={[
          {
            key: "execution",
            label: "分析与执行",
            children: (
              <NodeExecution
                node={node}
                model={model}
                workflow={workflow}
                onAnalyze={onAnalyze}
                onSelectRun={onSelectRun}
              />
            ),
          },
          {
            key: "overview",
            label: "节点概览",
            children: <NodeOverview {...props} />,
          },
          {
            key: "knowledge",
            label: "知识与比较",
            children: <NodeKnowledge {...props} />,
          },
          {
            key: "quality",
            label: "置信度与复核",
            children: <NodeQuality {...props} />,
          },
          {
            key: "evidence",
            label: `证据（${node.knowledge.evidence?.length ?? 0}）`,
            children: <NodeEvidence {...props} />,
          },
          {
            key: "source",
            label: "原始数据",
            children: <NodeSource {...props} />,
          },
        ]}
      />
    </Drawer>
  );
}
