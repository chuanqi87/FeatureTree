import { Space, Tag, Tooltip, Typography } from "antd";
import { label } from "../format.js";

export function ConfidenceTag({ level = "unassessed" }) {
  return <Tag color={{ high: "green", medium: "gold", low: "red" }[level]}>{label(level)}</Tag>;
}

export default function QualityTags({ summary }) {
  if (!summary) return <ConfidenceTag />;
  const counts = Object.entries(summary.counts).filter(([, count]) => count);
  return (
    <Tooltip title="本节点逐项统计，不继承子节点评级；未填比较项计为未评估，不取平均分。">
      <Space orientation="vertical" size={2}>
        {counts.map(([level, count]) => <span key={level}><ConfidenceTag level={level} />{count} 项</span>)}
        <Typography.Text type="secondary">
          必须待做 {summary.required_pending} · 建议 {summary.recommended_pending} · 不符 {summary.device_states.failed ?? 0}
        </Typography.Text>
      </Space>
    </Tooltip>
  );
}
