import { Button, Descriptions, Empty, Tag, Typography } from "antd";
import { label, safeUrl } from "../format.js";

export function StatusTag({ value }) {
  const color = [
    "confirmed",
    "complete",
    "supported",
    "full",
    "confirmed_same",
  ].includes(value)
    ? "success"
    : [
          "in_review",
          "in_progress",
          "conditional",
          "partial",
          "different",
          "has_confirmed_differences",
        ].includes(value)
      ? "warning"
      : ["unsupported", "rejected"].includes(value)
        ? "error"
        : undefined;
  return <Tag color={color}>{label(value)}</Tag>;
}

export function ValueFields({ value, model, onSelect }) {
  if (value === null || value === undefined)
    return <Typography.Text type="secondary">未记录</Typography.Text>;
  if (typeof value === "boolean") return value ? "是" : "否";
  if (Array.isArray(value)) {
    if (!value.length)
      return <Typography.Text type="secondary">暂无记录</Typography.Text>;
    return (
      <div className="value-items">
        {value.map((item, index) => (
          <div className="value-item" key={index}>
            <ValueFields value={item} model={model} onSelect={onSelect} />
          </div>
        ))}
      </div>
    );
  }
  if (typeof value === "object") {
    const entries = Object.entries(value);
    if (!entries.length)
      return <Typography.Text type="secondary">暂无记录</Typography.Text>;
    return (
      <Descriptions
        column={1}
        size="small"
        bordered
        className="value-fields"
        items={entries.map(([key, item]) => ({
          key,
          label: label(key),
          children: (
            <ValueFields value={item} model={model} onSelect={onSelect} />
          ),
        }))}
      />
    );
  }
  if (model?.byId.has(value))
    return (
      <Button
        type="link"
        className="reference-button"
        onClick={() => onSelect(value)}
      >
        {model.byId.get(value).name.zh} ↗
      </Button>
    );
  const url = safeUrl(value);
  if (url)
    return (
      <Typography.Link href={url} target="_blank" rel="noopener noreferrer">
        {String(value)}
      </Typography.Link>
    );
  return <span className="field-text">{label(value)}</span>;
}

export function EmptyRecord({ children }) {
  return <Empty image={Empty.PRESENTED_IMAGE_SIMPLE} description={children} />;
}
