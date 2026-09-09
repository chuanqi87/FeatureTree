import { Alert, Collapse } from "antd";
import { ValueFields } from "../../../shared/components/ValueFields.jsx";
import Section from "./Section.jsx";

export function NodeSource({ node, model, onSelect }) {
  const { knowledge, ...feature } = node;
  return (
    <div className="detail-stack">
      <Alert
        type="info"
        showIcon
        title="展示节点和知识记录的全部字段，包含扩展属性。"
      />
      <Section title="树节点 · 全部字段">
        <ValueFields value={feature} model={model} onSelect={onSelect} />
      </Section>
      <Section title="知识记录 · 全部字段">
        <ValueFields value={knowledge} model={model} onSelect={onSelect} />
      </Section>
      <Collapse
        items={[
          {
            key: "json",
            label: "查看完整 JSON",
            children: (
              <pre className="raw-json">{JSON.stringify(node, null, 2)}</pre>
            ),
          },
        ]}
      />
    </div>
  );
}
