import { Card } from "antd";

export default function Section({ title, children }) {
  return (
    <Card size="small" title={title} className="detail-card">
      {children}
    </Card>
  );
}
