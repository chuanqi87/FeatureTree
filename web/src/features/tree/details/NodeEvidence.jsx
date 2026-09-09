import { Space } from "antd";
import { FileTextOutlined } from "@ant-design/icons";
import {
  EmptyRecord,
  ValueFields,
} from "../../../shared/components/ValueFields.jsx";
import Section from "./Section.jsx";

export function NodeEvidence({ node, model, onSelect }) {
  const evidence = node.knowledge.evidence ?? [];
  return evidence.length ? (
    <div className="detail-stack">
      {evidence.map((item, i) => (
        <Section
          key={item.id ?? i}
          title={
            <Space>
              <FileTextOutlined />
              {item.title ?? item.id ?? `证据 ${i + 1}`}
            </Space>
          }
        >
          <ValueFields value={item} model={model} onSelect={onSelect} />
        </Section>
      ))}
    </div>
  ) : (
    <EmptyRecord>尚未记录证据</EmptyRecord>
  );
}
