import {
  Alert,
  Button,
  Descriptions,
  Progress,
  Space,
  Table,
  Tag,
  Typography,
} from "antd";
import { label } from "../../../shared/format.js";
import {
  StatusTag,
  ValueFields,
} from "../../../shared/components/ValueFields.jsx";
import Section from "./Section.jsx";

export function NodeOverview({ node, model, onSelect }) {
  const p = node.comparison_progress;
  const done = p.confirmed_support + p.confirmed_comparisons;
  const total = p.total_support + p.total_comparisons;
  const platformColumns = [
    { title: "平台", dataIndex: "name" },
    {
      title: "支持情况",
      dataIndex: "status",
      render: (value) => <StatusTag value={value} />,
    },
    {
      title: "复核状态",
      dataIndex: "verification",
      render: (value) => <StatusTag value={value} />,
    },
  ];
  const platformRows = Object.entries(model.platforms).map(
    ([key, platform]) => ({ key, name: platform.name, ...node.platforms[key] }),
  );
  return (
    <div className="detail-stack">
      <Section title="基本信息">
        <Typography.Paragraph className="ability-definition">
          {node.definition}
        </Typography.Paragraph>
        <Descriptions
          bordered
          size="small"
          column={2}
          items={[
            {
              key: "role",
              label: "节点类型",
              children: label(node.knowledge_role),
            },
            {
              key: "depth",
              label: "当前层级",
              children: <Tag color="blue">{node.level}</Tag>,
            },
            { key: "layer", label: "所属层", children: label(node.layer) },
            {
              key: "privacy",
              label: "隐私类别",
              children: label(node.privacy_class),
            },
            {
              key: "device",
              label: "设备形态",
              children: (node.device_forms ?? []).map(label).join(" / "),
            },
            {
              key: "status",
              label: "知识状态",
              children: <StatusTag value={node.knowledge.status} />,
            },
            {
              key: "alias",
              label: "别名",
              span: 2,
              children: node.aliases?.join("、") || "—",
            },
            {
              key: "path",
              label: "知识文件",
              span: 2,
              children: (
                <Typography.Text copyable className="file-path">
                  {node.knowledge_path}
                </Typography.Text>
              ),
            },
          ]}
        />
      </Section>
      <Section title="平台支持">
        <Table
          rowKey="key"
          dataSource={platformRows}
          columns={platformColumns}
          size="small"
          pagination={false}
          expandable={{
            rowExpandable: (record) =>
              Object.keys(node.platforms[record.key]).some(
                (key) => !["status", "verification"].includes(key),
              ),
            expandedRowRender: (record) => (
              <ValueFields
                value={node.platforms[record.key]}
                model={model}
                onSelect={onSelect}
              />
            ),
          }}
        />
        <Alert
          type="info"
          showIcon
          title="待确认不表示不支持；支持情况与复核状态分别记录。"
          className="section-alert"
        />
      </Section>
      <Section title="确认进度">
        <div className="progress-heading">
          <Typography.Text strong>
            {done} / {total} 项已确认
          </Typography.Text>
          <StatusTag value={p.conclusion} />
        </div>
        <Progress percent={total ? Math.round((done / total) * 100) : 0} />
        <Descriptions
          column={2}
          size="small"
          items={[
            {
              key: "support",
              label: "平台支持",
              children: `${p.confirmed_support} / ${p.total_support}`,
            },
            {
              key: "comparison",
              label: "维度比较",
              children: `${p.confirmed_comparisons} / ${p.total_comparisons}`,
            },
          ]}
        />
      </Section>
      <Section title="比较范围">
        <Descriptions
          column={1}
          bordered
          size="small"
          items={[
            {
              key: "includes",
              label: "纳入范围",
              children: (
                <ValueFields
                  value={node.comparison_scope.includes}
                  model={model}
                  onSelect={onSelect}
                />
              ),
            },
            {
              key: "excludes",
              label: "排除范围",
              children: (
                <ValueFields
                  value={node.comparison_scope.excludes}
                  model={model}
                  onSelect={onSelect}
                />
              ),
            },
            {
              key: "dimensions",
              label: "比较维度",
              children: (
                <Space size={[4, 8]} wrap>
                  {node.comparison_dimensions.map((key) => (
                    <Tag key={key}>{model.dimensions[key] || key}</Tag>
                  ))}
                </Space>
              ),
            },
          ]}
        />
      </Section>
      <Section title={`直接子节点（${node.children.length}）`}>
        {node.children.length ? (
          <Space orientation="vertical" className="full-width">
            {node.children.map((id) => (
              <Button key={id} type="link" onClick={() => onSelect(id)}>
                {model.byId.get(id).name.zh}
                <Tag>{model.byId.get(id).level}</Tag>
              </Button>
            ))}
          </Space>
        ) : (
          <Typography.Text type="secondary">
            {node.knowledge_role === "rollup"
              ? "领域分支尚未展开，子能力待生成。"
              : "叶子节点，没有子节点。"}
          </Typography.Text>
        )}
      </Section>
    </div>
  );
}
