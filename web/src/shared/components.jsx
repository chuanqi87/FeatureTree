import { Alert, Button, Collapse, Drawer, Empty, Space, Spin, Tag, Typography } from "antd";
import { useResource } from "./useResource.js";
import { text } from "./model.js";
export function Status({ value }) {
  const colors = { high: "green", medium: "gold", low: "red", failed: "red", stale: "orange", invalidated: "red", running: "blue", completed: "green", published: "green" };
  return <Tag color={colors[value]}>{text(value)}</Tag>;
}
export function ResourceState({ resource, children }) {
  if (resource.error) return <Alert type="error" showIcon title={resource.error} action={<Button onClick={resource.refresh}>重试</Button>} />;
  if (resource.loading && !resource.data) return <Spin />;
  return children;
}
export function JsonDetails({ value, title = "完整交付件" }) {
  return <Collapse items={[{ key: "json", label: title, children: <pre className="json-view">{JSON.stringify(value, null, 2)}</pre> }]} />;
}
export function ArtifactDrawer({ reference, onClose }) {
  const resource = useResource(reference ? `objects/${reference}` : null);
  return <Drawer open={!!reference} title="不可变交付件" size="large" onClose={onClose}>
    <ResourceState resource={resource}>{resource.data && <><Typography.Paragraph copyable>{reference}</Typography.Paragraph><pre className="json-view">{JSON.stringify(resource.data.object, null, 2)}</pre></>}</ResourceState>
  </Drawer>;
}
export function PageHeader({ title, description, children }) {
  return <div className="page-header"><div><Typography.Title level={3}>{title}</Typography.Title><Typography.Text type="secondary">{description}</Typography.Text></div><Space wrap>{children}</Space></div>;
}
