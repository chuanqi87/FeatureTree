import { Alert, Card, Collapse, Space } from "antd";
import { label } from "../../format.js";
import { EmptyRecord, StatusTag, ValueFields } from "../ValueFields.jsx";
import Section from "./Section.jsx";

export function NodeKnowledge({ node, model, onSelect }) {
  const doc = node.knowledge;
  const comparisons = doc.comparisons ?? [];
  const excluded = new Set([
    "feature_id",
    "role",
    "status",
    "definition",
    "presence",
    "comparisons",
    "evidence",
    "schema_version",
    "child_index",
    "legacy_presence",
    "legacy_definition",
    "migration_notes",
  ]);
  const history = Object.fromEntries(
    ["legacy_presence", "legacy_definition", "migration_notes"]
      .filter((key) => key in doc)
      .map((key) => [key, doc[key]]),
  );
  return (
    <div className="detail-stack">
      <Alert
        type="info"
        showIcon
        title={
          <Space>
            知识正文状态：
            <StatusTag value={doc.status} />
          </Space>
        }
        description="正文整理状态不代表结论已确认或高可信。逐项评级及真机计划见‘置信度与复核’；未转为结构化事实的历史正文仍未评估。"
      />
      <Section title={`平台比较记录（${comparisons.length}）`}>
        {comparisons.length ? (
          comparisons.map((finding, i) => (
            <Card
              key={i}
              size="small"
              className="finding-card"
              title={model.dimensions[finding.dimension] ?? finding.dimension}
              extra={<StatusTag value={finding.verification} />}
            >
              <ValueFields value={finding} model={model} onSelect={onSelect} />
            </Card>
          ))
        ) : (
          <EmptyRecord>尚未填写差异记录，结论为待确认</EmptyRecord>
        )}
      </Section>
      {Object.entries(doc)
        .filter(([key]) => !excluded.has(key))
        .map(([key, value]) => (
          <Section key={key} title={label(key)}>
            <ValueFields value={value} model={model} onSelect={onSelect} />
          </Section>
        ))}
      <Section title="精选 API 绑定">
        <ValueFields
          value={node.bindings ?? {}}
          model={model}
          onSelect={onSelect}
        />
      </Section>
      <Collapse
        items={[
          {
            key: "history",
            label: "历史判断与迁移记录",
            children: (
              <>
                <Alert
                  type="warning"
                  showIcon
                  title="历史记录不计入当前支持结论和确认进度。"
                  className="section-alert"
                />
                <ValueFields
                  value={history}
                  model={model}
                  onSelect={onSelect}
                />
              </>
            ),
          },
        ]}
      />
    </div>
  );
}
