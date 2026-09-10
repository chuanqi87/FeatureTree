import { useState } from "react";
import { Alert, Button, Card, Descriptions, Drawer, Space, Tag, Typography } from "antd";
import { Status, JsonDetails, ResourceState } from "../../shared/components.jsx";
import { useResource } from "../../shared/useResource.js";
import { safeUrl, text } from "../../shared/model.js";
export default function Article({ article, reference, onReview }) {
  const [source, setSource] = useState(null), [offset, setOffset] = useState(0);
  const body = useResource(source ? `source-body/${source.snapshot_id}/${source.document_id}?offset=${offset}` : null);
  if (!article) return <Alert title="知识尚未生产" type="info" />;
  const assessments = new Map(article.assessments.map(row => [row.claim_id, row]));
  const evidence = new Map(article.evidence.map(row => [row.id, row]));
  return <><Space wrap style={{ marginBottom: 20 }}><Tag>{article.draft ? "校准样稿" : "已生成知识"}</Tag><Typography.Text>整体可信度</Typography.Text><Status value={article.overall_confidence} />{onReview && <Button onClick={() => onReview(null)}>进入人工审核</Button>}</Space>
    {article.overall_confidence === "low" && <Alert type="warning" showIcon title="部分必答结论仍有不确定性" description="整体评级取全部必答结论最低档；接受已说明的限制不会自动提高评级。" style={{ marginBottom: 20 }} />}
    {article.claims.map(claim => <Card className="claim" key={claim.claim_id} size="small" title={<Space wrap><Tag>{claim.platforms.join(" ↔ ")}</Tag><Typography.Text>{text(claim.dimension)}</Typography.Text><Status value={claim.result} /></Space>} extra={<Status value={assessments.get(claim.claim_id)?.level} />}>
      <Typography.Paragraph>{claim.statement}</Typography.Paragraph>
      <Descriptions size="small" column={1} items={[{ key: "conditions", label: "适用条件", children: claim.conditions.join("；") || "未额外列出" }, { key: "rating", label: "评级理由", children: assessments.get(claim.claim_id)?.reason }, { key: "gaps", label: "待核实内容", children: claim.gaps.join("；") || "无记录" }, { key: "scope", label: "检查范围", children: claim.coverage_note || "—" }, { key: "premises", label: "推论依据", children: claim.premise_ids.join("；") || "—" }]} />
      {article.confidence_reasons.includes(claim.claim_id) && <Tag color="orange">决定整体评级的结论</Tag>}
      {onReview && assessments.get(claim.claim_id)?.level === "low" && <Button size="small" onClick={() => onReview(claim.claim_id)}>审核这项结论</Button>}
      {claim.evidence_refs.map(id => { const item = evidence.get(id); return item && <div className="evidence" key={id}><Typography.Paragraph>{item.excerpt}</Typography.Paragraph><Space>{safeUrl(item.url) && <Typography.Link href={item.url} target="_blank" rel="noreferrer">官方页面</Typography.Link>}<Button size="small" onClick={() => { setSource(item); setOffset(0); }}>核对封存正文</Button><Typography.Text type="secondary">{item.locator}</Typography.Text></Space></div>; })}
    </Card>)}
    <JsonDetails value={{ article_ref: reference, feature_id: article.feature_id, spec_ref: article.spec_ref, freeze_ref: article.freeze_ref, baseline_ref: article.baseline_ref, dependencies: article.dependencies }} title="版本、来源和阶段追溯" />
    <Drawer title="封存的官方正文" open={!!source} onClose={() => setSource(null)} size="large"><ResourceState resource={body}>{body.data && <><Typography.Text copyable>{body.data.body_sha256}</Typography.Text><pre className="json-view">{body.data.text}</pre><Space><Button disabled={offset === 0} onClick={() => setOffset(0)}>开头</Button><Button disabled={!body.data.next_offset} onClick={() => setOffset(body.data.next_offset)}>继续阅读</Button></Space></>}</ResourceState></Drawer>
  </>;
}
