import { lazy, Suspense, useState } from "react";
import { Alert, ConfigProvider, Layout, Menu, Space, Tag, Typography } from "antd";
import { ApartmentOutlined, BookOutlined, DatabaseOutlined, DeploymentUnitOutlined, SafetyCertificateOutlined, SendOutlined } from "@ant-design/icons";
import zhCN from "antd/locale/zh_CN";
import { useResource } from "../shared/useResource.js";
const TreePage = lazy(() => import("../features/tree/TreePage.jsx"));
const SourcesPage = lazy(() => import("../features/sources/SourcesPage.jsx"));
const WorkflowPage = lazy(() => import("../features/workflow/WorkflowPage.jsx"));
const KnowledgePage = lazy(() => import("../features/knowledge/KnowledgePage.jsx"));
const ReviewPage = lazy(() => import("../features/review/ReviewPage.jsx"));
const ReleasePage = lazy(() => import("../features/release/ReleasePage.jsx"));
const pages = [
  ["tree", "特性树", ApartmentOutlined, TreePage], ["sources", "来源与 API", DatabaseOutlined, SourcesPage],
  ["workflow", "Agent 工作流", DeploymentUnitOutlined, WorkflowPage], ["knowledge", "叶子知识", BookOutlined, KnowledgePage],
  ["review", "人工审核", SafetyCertificateOutlined, ReviewPage], ["release", "发布版本", SendOutlined, ReleasePage],
];
export default function App() {
  const [page, setPage] = useState("tree");
  const [context, setContext] = useState(null);
  function navigate(target, nextContext = null) { setContext(nextContext); setPage(target); }
  const current = useResource("current", 10000);
  const releaseId = current.data?.release_id ?? null;
  const Component = pages.find(row => row[0] === page)[3];
  return <ConfigProvider locale={zhCN} theme={{ token: { colorPrimary: "#2463b4", borderRadius: 7 } }}>
    <Layout className="admin-layout"><Layout.Sider width={220} breakpoint="lg" collapsedWidth={64}>
      <div className="logo"><ApartmentOutlined /><strong>FeatureTree <small>v2</small></strong></div>
      <Menu theme="dark" selectedKeys={[page]} items={pages.map(([key, label, Icon]) => ({ key, label, icon: <Icon /> }))} onClick={({ key }) => navigate(key)} />
      <div className="sider-note">API → 公共叶子 → 三端知识<br />证据 · 审查 · 可信度</div>
    </Layout.Sider><Layout><Layout.Header className="topbar"><Typography.Text strong>跨平台能力知识工作台</Typography.Text><Space><Tag>{releaseId ? "正式发布" : "尚未正式发布"}</Tag><Typography.Text type="secondary">{releaseId?.slice(0, 14) || "校准与架构切换阶段"}</Typography.Text></Space></Layout.Header>
      <Layout.Content className="workspace">{current.error && <Alert type="error" title={current.error} />}
        <Suspense fallback={<p>正在加载功能区…</p>}><Component releaseId={releaseId} onPublished={current.refresh} navigate={navigate} context={context} /></Suspense>
      </Layout.Content></Layout></Layout>
  </ConfigProvider>;
}
