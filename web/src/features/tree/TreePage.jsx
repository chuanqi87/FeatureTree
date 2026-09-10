import { useMemo, useState } from "react";
import { Alert, Button, Descriptions, Drawer, Empty, Select, Space, Table, Tag, Typography } from "antd";
import { useResource } from "../../shared/useResource.js";
import { PageHeader, ResourceState, Status, JsonDetails } from "../../shared/components.jsx";
import { treeRows } from "../../shared/model.js";
export default function TreePage({ releaseId, navigate }) {
  const candidates = useResource("candidates", 10000);
  const [candidate, setCandidate] = useState(null);
  const [selected, setSelected] = useState(null);
  const tree = useResource(candidate ? `objects/${candidate}` : `tree${releaseId ? `?release_id=${releaseId}` : ""}`);
  const features = candidate ? tree.data?.object.features || [] : tree.data?.features || [];
  const rows = useMemo(() => treeRows(features), [features]);
  const detail = useResource(selected && !candidate ? `features/${selected}?release_id=${releaseId}` : null);
  const node = features.find(row => row.id === selected);
  return <><PageHeader title="平台中立特性树" description="每个叶子定义一条可独立比较的知识；来源与知识按需展开。"><Button onClick={() => navigate("workflow")}>创建分析任务</Button></PageHeader>
    <div className="toolbar"><Select style={{ minWidth: 340 }} value={candidate || "formal"} onChange={value => { setCandidate(value === "formal" ? null : value); setSelected(null); }} options={[{ value: "formal", label: "正式版本" }, ...(candidates.data?.items || []).filter(row => row.tree_ref).map(row => ({ value: row.tree_ref, label: `候选 · ${row.run_id} / ${row.work_id}` }))]} /></div>
    {candidate && <Alert type="info" showIcon title="候选快照：尚未冻结，不能计为正式特性或知识" />}
    <ResourceState resource={tree}><Table rowKey="id" dataSource={rows} pagination={false} locale={{ emptyText: <Empty description="尚未发布特性树。可查看候选快照，或开始校准分析。" /> }} columns={[
      { title: "特性 / 能力范围", dataIndex: "name", render: (name, row) => <Button type="link" onClick={() => setSelected(row.id)}>{name}</Button> },
      { title: "节点类型", dataIndex: "node_type", render: value => <Tag>{value === "leaf" ? "能力叶子" : "待展开分支"}</Tag> },
      { title: "知识状态", render: (_, row) => <Status value={row.knowledge?.validity || "not_produced"} /> },
      { title: "可信度", render: (_, row) => row.knowledge?.confidence ? <Status value={row.knowledge.confidence} /> : "待评级" },
    ]} /></ResourceState>
    <Drawer title={node?.name || "节点详情"} open={!!selected} onClose={() => setSelected(null)} size="large">
      {node && <><Descriptions column={1} items={[{ key: "id", label: "稳定身份", children: <Typography.Text copyable>{node.id}</Typography.Text> }, { key: "definition", label: "定义", children: node.definition }, { key: "include", label: "包含范围", children: node.includes.join("；") }, { key: "exclude", label: "排除范围", children: node.excludes.join("；") }, { key: "success", label: "成功标准", children: node.success_criteria.join("；") }]} />
      <Space style={{ margin: "20px 0" }}><Button onClick={() => navigate("knowledge")}>查看叶子知识</Button><Tag>{candidate ? "候选" : detail.data?.freeze_refs.length ? "已冻结" : "未冻结"}</Tag></Space>
      <ResourceState resource={detail}>{detail.data && <JsonDetails value={detail.data.bindings} title="API 绑定与具体实现路线" />}</ResourceState></>}
    </Drawer>
  </>;
}
