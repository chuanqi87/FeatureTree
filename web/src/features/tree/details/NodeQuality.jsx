import { Alert, Space, Table, Tag, Typography } from "antd";
import { label } from "../../../shared/format.js";
import { ConfidenceTag } from "../../../shared/components/QualityTags.jsx";
import QualityTags from "../../../shared/components/QualityTags.jsx";
import {
  StatusTag,
  ValueFields,
} from "../../../shared/components/ValueFields.jsx";
import Section from "./Section.jsx";

export function NodeQuality({ node, model, onSelect }) {
  return (
    <div className="detail-stack">
      <Alert
        type="info"
        showIcon
        title="置信度与真机复核分别判断"
        description="高可信：证据充分且结论已确认；中可信：有官方依据但推论或条件仍需复核；低可信：关键缺口或冲突；未评估：尚未评级。评级不是概率，实测通过只覆盖列出的样本。"
      />
      <Section title="本节点知识项分布">
        <QualityTags summary={node.quality_summary} />
      </Section>
      <Table
        rowKey="claim_id"
        size="small"
        dataSource={node.quality_claims ?? []}
        pagination={{ pageSize: 8, showSizeChanger: false }}
        columns={[
          {
            title: "知识项",
            key: "claim",
            render: (_, row) => (
              <Space orientation="vertical" size={2}>
                <Typography.Text>
                  {label(row.kind)} · {label(row.dimension)}
                </Typography.Text>
                <Typography.Text type="secondary">
                  {row.platforms.map(label).join(" ↔ ")}
                </Typography.Text>
                <StatusTag value={row.verification} />
              </Space>
            ),
          },
          {
            title: "置信度",
            dataIndex: "confidence",
            render: (level) => <ConfidenceTag level={level} />,
          },
          {
            title: "真机复核",
            key: "device",
            render: (_, row) => (
              <Space orientation="vertical" size={2}>
                <Tag>{label(row.device_requirement)}</Tag>
                <Typography.Text>{label(row.device_state)}</Typography.Text>
              </Space>
            ),
          },
        ]}
        expandable={{
          expandedRowRender: (row) => (
            <ValueFields value={row} model={model} onSelect={onSelect} />
          ),
        }}
      />
      <Typography.Paragraph type="secondary">
        展开知识项可查看评级原因、证据、缺口、实测步骤与材料。未转成结构化 facts
        的历史正文不继承这些评级。
      </Typography.Paragraph>
    </div>
  );
}
