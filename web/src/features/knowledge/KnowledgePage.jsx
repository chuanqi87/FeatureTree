import { useState } from "react";
import { Button, Checkbox, Drawer, Input, Table, Tag } from "antd";
import { useResource } from "../../shared/useResource.js";
import { PageHeader, ResourceState, Status } from "../../shared/components.jsx";
import { trusted } from "../../shared/model.js";
import Article from "./Article.jsx";
import KnowledgePlan from "./KnowledgePlan.jsx";
export default function KnowledgePage({ releaseId, navigate }) {
  const tree = useResource(`tree${releaseId ? `?release_id=${releaseId}` : ""}`), candidates = useResource("candidates", 10000);
  const [selected, setSelected] = useState(null), [onlyTrusted, setOnlyTrusted] = useState(false), [search, setSearch] = useState("");
  const detail = useResource(selected ? selected.candidate ? `objects/${selected.article_ref}` : `knowledge/${selected.id}?release_id=${releaseId}` : null);
  const rows = [...(tree.data?.features || []).filter(row => row.node_type === "leaf").map(row => ({ ...row, draft: false, candidate: false, article_ref: row.knowledge?.article_ref })), ...(candidates.data?.items || []).filter(row => row.article_ref).map(row => ({ id: row.article_ref, name: row.feature_name || row.feature_id || `${row.run_id} / ${row.work_id}`, article_ref: row.article_ref, draft: row.draft, candidate: true, knowledge: { confidence: row.overall_confidence, validity: "candidate" } }))]
    .filter(row => row.name.toLowerCase().includes(search.toLowerCase()) && (!onlyTrusted || trusted(row.knowledge)));
  return <><PageHeader title="叶子知识" description="逐项比较三端能力结果与接口形态，保留条件、原文依据和具体不确定性。"><KnowledgePlan candidates={candidates.data?.items || []} releaseId={releaseId} onCreated={() => navigate("workflow")} /></PageHeader>
    <div className="toolbar"><Input.Search placeholder="搜索叶子名称" style={{ maxWidth: 400 }} onSearch={setSearch} /><Checkbox checked={onlyTrusted} onChange={event => setOnlyTrusted(event.target.checked)}>只看当前有效的高中可信知识</Checkbox></div>
    <ResourceState resource={tree}><Table rowKey="id" dataSource={rows} columns={[{ title: "能力叶子", dataIndex: "name", render: (name, row) => <Button type="link" onClick={() => setSelected(row)}>{name}</Button> }, { title: "版本", render: (_, row) => <Tag>{row.draft ? "校准样稿" : row.candidate ? "正式候选（待发布）" : "正式"}</Tag> }, { title: "有效性", render: (_, row) => <Status value={row.knowledge?.validity || "not_produced"} /> }, { title: "可信度", render: (_, row) => row.knowledge?.confidence ? <Status value={row.knowledge.confidence} /> : "待评级" }]} /></ResourceState>
    <Drawer title={selected?.name} open={!!selected} onClose={() => setSelected(null)} size="large"><ResourceState resource={detail}>{detail.data && <Article article={selected?.candidate ? detail.data.object : detail.data.article} reference={selected?.article_ref} onReview={claimId => navigate("review", { article_ref: selected?.article_ref, claim_id: claimId })} />}</ResourceState></Drawer>
  </>;
}
