import { useState } from "react";
import { Alert, Button, Card, Drawer, Input, Select, Space, Statistic, Table, Tabs, Typography } from "antd";
import { useResource } from "../../shared/useResource.js";
import { PageHeader, ResourceState, Status, JsonDetails } from "../../shared/components.jsx";
import { safeUrl } from "../../shared/model.js";
export default function SourcesPage() {
  const sources = useResource("sources");
  const [manifestOpen, setManifestOpen] = useState(false);
  const [snapshot, setSnapshot] = useState(null), [kind, setKind] = useState("apis"), [platform, setPlatform] = useState(null), [query, setQuery] = useState(""), [cursor, setCursor] = useState(null), [record, setRecord] = useState(null);
  const id = snapshot || sources.data?.items[0]?.id;
  const params = new URLSearchParams({ snapshot_id: id || "", query, limit: "50", ...(platform ? { platform } : {}), ...(cursor ? { cursor } : {}) });
  const records = useResource(id ? `${kind}?${params}` : null);
  const body = useResource(record && kind === "documents" && record.status === "verified" ? `source-body/${id}/${record.id}` : null);
  const manifest = useResource(manifestOpen && id ? `sources/${id}` : null);
  const selected = sources.data?.items.find(row => row.id === id);
  return <><PageHeader title="来源与 API 目录" description="声明、官方主题和正文分别记录。目录处理完成不代表功能覆盖完成。" />
    <ResourceState resource={sources}><Select style={{ width: "100%" }} value={id} onChange={value => { setSnapshot(value); setCursor(null); }} placeholder="选择封存来源快照" options={sources.data?.items.map(row => ({ value: row.id, label: `${row.status} · ${row.id}` }))} /></ResourceState>
    {selected && <div className="stat-grid" style={{ marginTop: 20 }}>{Object.entries(selected.counts).map(([key, value]) => <Card key={key} size="small"><Statistic title={{ declarations: "规范 API 声明", families: "计数符号族", topics: "官方目录主题", documents: "文档目录项" }[key]} value={value} /></Card>)}</div>}
    {selected?.gaps.length > 0 && <Alert type="warning" showIcon title={`该快照保留 ${selected.gaps.length} 项来源缺口`} description={selected.gaps[0].reason} />}
    <Button style={{ marginTop: 12 }} onClick={() => setManifestOpen(true)}>查看来源范围、SDK 文件与提取记录</Button>
    <Tabs activeKey={kind} onChange={value => { setKind(value); setCursor(null); setRecord(null); }} items={[{ key: "apis", label: "API 声明" }, { key: "topics", label: "官方目录" }, { key: "documents", label: "文档与采集状态" }]} />
    <div className="toolbar"><Select allowClear placeholder="全部平台" style={{ width: 160 }} onChange={value => { setPlatform(value); setCursor(null); }} options={["android", "ios", "harmonyos"].map(value => ({ value, label: value }))} /><Input.Search placeholder="按符号、主题或文档标题检索" style={{ maxWidth: 450 }} onSearch={value => { setQuery(value); setCursor(null); }} /></div>
    <ResourceState resource={records}><Table rowKey="id" dataSource={records.data?.items || []} pagination={false} columns={[
      { title: "名称", render: (_, row) => <Button type="link" onClick={() => setRecord(row)}>{row.qualified_name || row.title}</Button> }, { title: "平台", dataIndex: "platform" },
      { title: "公开性 / 状态", render: (_, row) => <Status value={row.visibility || row.status || row.summary_strength} /> }, { title: "SDK / 原始身份", render: (_, row) => row.sdk_version || row.original_id || "—" },
    ]} /><Space style={{ marginTop: 16 }}><Button onClick={() => setCursor(null)} disabled={!cursor}>首页</Button><Button onClick={() => setCursor(records.data.next_cursor)} disabled={!records.data?.next_cursor}>下一页</Button><Typography.Text type="secondary">分页始终固定当前快照</Typography.Text></Space></ResourceState>
    <Drawer open={manifestOpen} title="来源封存清单与缺口" onClose={() => setManifestOpen(false)} size="large"><ResourceState resource={manifest}>{manifest.data && <JsonDetails value={manifest.data} title="范围、文件哈希、提取器版本与处置" />}</ResourceState></Drawer>
    <Drawer open={!!record} title={record?.qualified_name || record?.title} onClose={() => setRecord(null)} size="large">{record && <>{safeUrl(record.url) && <Typography.Link href={record.url} target="_blank" rel="noreferrer">官方原文</Typography.Link>}<JsonDetails value={record} title="来源身份、可用性与原始声明" /><ResourceState resource={body}>{body.data && <pre className="json-view">{body.data.text}</pre>}</ResourceState></>}</Drawer>
  </>;
}
