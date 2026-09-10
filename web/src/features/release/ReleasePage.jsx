import { useState } from "react";
import { Alert, Button, Card, Descriptions, Input, Space, Table, Typography, message } from "antd";
import { useResource } from "../../shared/useResource.js";
import { post } from "../../shared/api.js";
import { PageHeader, ResourceState, Status, ArtifactDrawer, JsonDetails } from "../../shared/components.jsx";
import CalibrationApproval from "./CalibrationApproval.jsx";
import FreezeForm from "./FreezeForm.jsx";
import CandidatePublication from "./CandidatePublication.jsx";
export default function ReleasePage({ releaseId, onPublished, navigate }) {
  const releases = useResource("releases", 10000), candidates = useResource("candidates", 10000);
  const approvals = useResource("calibrations"), freezes = useResource("freezes");
  const [artifact, setArtifact] = useState(null), [transaction, setTransaction] = useState(""), [busy, setBusy] = useState(false), [compared, setCompared] = useState(null);
  const difference = useResource(compared && releaseId ? `releases/compare?before=${releaseId}&after=${compared}` : null);
  async function rebase() {
    setBusy(true);
    try { const result = await post("releases/rebase", { transaction_key: transaction }, releaseId); setTransaction(result.key); releases.refresh(); message.success("已保留无关更新并重新准备，请查看差异后发布"); }
    catch (error) { message.error(error.message); } finally { setBusy(false); }
  }
  async function exportRelease(id) {
    try { const result = await post("releases/export", { release_id: id }, releaseId); message.success(`已导出 JSON、YAML 和 Markdown：${result.directory}`, 8); }
    catch (error) { message.error(error.message); }
  }
  async function publish() {
    setBusy(true);
    try { await post("releases/publish", { transaction_key: transaction }, releaseId); releases.refresh(); onPublished(); message.success("正式指针已切换"); }
    catch (error) { message.error(error.message); } finally { setBusy(false); }
  }
  async function rollback(id) {
    setBusy(true);
    try { await post("releases/rollback", { target_release_id: id }, releaseId); releases.refresh(); onPublished(); message.success("已创建回滚版本；人工审核历史保留"); }
    catch (error) { message.error(error.message); } finally { setBusy(false); }
  }
  return <><PageHeader title="不可变发布版本" description="所有正式消费者固定同一发布指针。回滚创建新清单，保留历史审核与错误标记。" />
    {!releaseId && <Alert type="info" showIcon title="尚未满足正式接管门槛" description="需要三端稳定版来源、完整归属、独立审查，以及公共骨架、代表叶子、知识样稿和评级标准的人工确认。" style={{ marginBottom: 20 }} />}
    <Card title="已准备的发布事务" size="small" style={{ marginBottom: 20 }}><Space wrap><Space.Compact style={{ width: "100%", maxWidth: 640 }}><Input value={transaction} onChange={event => setTransaction(event.target.value)} placeholder="输入已完成验证的发布事务键" /><Button type="primary" disabled={!transaction} loading={busy} onClick={publish}>提交发布</Button></Space.Compact><Button disabled={!transaction || !releaseId} loading={busy} onClick={rebase}>基于最新版本重新准备知识更新</Button></Space></Card>
    <div className="stage-grid"><CalibrationApproval candidates={candidates.data?.items || []} releaseId={releaseId} onSaved={approvals.refresh} /><FreezeForm candidates={candidates.data?.items || []} releaseId={releaseId} approvals={approvals.data?.items || []} onSaved={freezes.refresh} /><CandidatePublication candidates={candidates.data?.items || []} freezes={freezes.data?.items || []} releaseId={releaseId} onPrepared={key => { setTransaction(key); releases.refresh(); }} /></div>
    <ResourceState resource={releases}><Table rowKey="release_id" dataSource={releases.data?.items || []} columns={[{ title: "发布版本", dataIndex: "release_id", render: value => <Typography.Text copyable>{value}</Typography.Text> }, { title: "状态", render: (_, row) => <Status value={row.status} /> }, { title: "类型", dataIndex: "kind" }, { title: "操作", render: (_, row) => <Space><Button onClick={() => setArtifact(row.tree_ref)}>树快照</Button><Button disabled={!releaseId} onClick={() => setCompared(row.release_id)}>与当前版本比较</Button><Button onClick={() => exportRelease(row.release_id)}>导出</Button><Button onClick={() => setArtifact(row.validation_ref)}>验收报告</Button><Button disabled={row.release_id === releaseId || row.status !== "published"} loading={busy} onClick={() => rollback(row.release_id)}>回滚到此内容</Button></Space> }]} /></ResourceState>
    <Card title="待审查的候选产物" style={{ marginTop: 24 }}><Alert type="warning" title="候选产物不代表正式知识；请先检查阶段交付件和来源缺口。" /><Table rowKey="result_ref" size="small" dataSource={candidates.data?.items || []} columns={[{ title: "运行 / 工作单", render: (_, row) => `${row.run_id} / ${row.work_id}` }, { title: "产物类型", render: (_, row) => row.article_ref ? row.draft ? "知识样稿" : "待发布知识" : "候选树与绑定" }, { title: "审查", render: (_, row) => <Button onClick={() => setArtifact(row.article_ref || row.result_ref)}>查看交付件</Button> }]} /><Button onClick={() => navigate("workflow")}>查看具名 Agent 审查与返工</Button></Card>
    {compared && <Card title="与当前正式版本的差异"><ResourceState resource={difference}>{difference.data && <JsonDetails value={difference.data} title="节点变化与知识版本变化" />}</ResourceState></Card>}
    <ArtifactDrawer reference={artifact} onClose={() => setArtifact(null)} />
  </>;
}
