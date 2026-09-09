import TreePage from "./TreePage.jsx";
import KnowledgeSearch from "./KnowledgeSearch.jsx";
import { useEffect, useState } from "react";
import {
  Alert,
  Avatar,
  Badge,
  Breadcrumb,
  Button,
  ConfigProvider,
  Layout,
  Menu,
  Space,
  Typography,
} from "antd";
import {
  ApartmentOutlined,
  AppstoreOutlined,
  FileSearchOutlined,
  DatabaseOutlined,
  MenuFoldOutlined,
  MenuUnfoldOutlined,
} from "@ant-design/icons";
import zhCN from "antd/locale/zh_CN";
import { useExplorer } from "./useExplorer.js";
import NodeDetails from "./NodeDetails.jsx";

const { Header, Sider, Content } = Layout;

export default function App() {
  const [page, setPage] = useState(() => {
    const selected = new URLSearchParams(location.hash.slice(1)).get("page");
    return selected === "evaluation" ? selected : "tree";
  });
  const explorer = useExplorer();
  const { model, loading, error } = explorer;
  useEffect(() => {
    const onHash = () =>
      setPage(
        new URLSearchParams(location.hash.slice(1)).get("page") === "evaluation"
          ? new URLSearchParams(location.hash.slice(1)).get("page")
          : "tree",
      );
    window.addEventListener("hashchange", onHash);
    return () => window.removeEventListener("hashchange", onHash);
  }, []);
  function navigate(next) {
    setPage(next);
    setTableMaximized(false);
    explorer.setDrawerOpen(false);
    history.replaceState(
      null,
      "",
      next === "evaluation" ? "#page=evaluation" : "#page=tree",
    );
  }
  function openNode(id) {
    setPage("tree");
    explorer.selectNode(id);
  }
  const [collapsed, setCollapsed] = useState(false);
  const [tableMaximized, setTableMaximized] = useState(false);
  useEffect(() => {
    if (!tableMaximized) return;
    const onKey = (event) => {
      if (event.key === "Escape" && !explorer.drawerOpen)
        setTableMaximized(false);
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [tableMaximized, explorer.drawerOpen]);
  const navigation = [
    { key: "tree", icon: <AppstoreOutlined />, label: "特性树" },
    { key: "evaluation", icon: <FileSearchOutlined />, label: "知识评测" },
  ];
  return (
    <ConfigProvider
      locale={zhCN}
      theme={{
        token: {
          colorPrimary: "#1677ff",
          borderRadius: 6,
          fontSize: 14,
          colorBgLayout: "#f0f2f5",
          fontFamily:
            '-apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif',
        },
        components: {
          Layout: { headerBg: "#fff", siderBg: "#001529" },
          Menu: { darkItemBg: "#001529", darkSubMenuItemBg: "#001529" },
          Table: { headerBg: "#fafafa" },
        },
      }}
    >
      <Layout
        className={`admin-layout${tableMaximized ? " table-maximized" : ""}`}
      >
        <Sider
          width={224}
          collapsedWidth={64}
          collapsed={collapsed}
          breakpoint="lg"
          onBreakpoint={setCollapsed}
          className="admin-sider"
        >
          <div className="admin-logo">
            <ApartmentOutlined />
            {!collapsed && <strong>FeatureTree</strong>}
          </div>
          {!collapsed && <div className="sider-caption">跨平台特性管理</div>}
          <Menu
            theme="dark"
            mode="inline"
            selectedKeys={[page]}
            items={navigation}
            onClick={({ key }) => navigate(key)}
            className="domain-menu"
          />
          {!collapsed && (
            <div className="sider-footer">
              <DatabaseOutlined />
              <span>本地知识库 · 只读模式</span>
            </div>
          )}
        </Sider>
        <Layout className="admin-main">
          <Header className="admin-header">
            <Space size={20}>
              <Button
                type="text"
                icon={collapsed ? <MenuUnfoldOutlined /> : <MenuFoldOutlined />}
                onClick={() => setCollapsed(!collapsed)}
                aria-label={collapsed ? "展开导航" : "收起导航"}
              />
              <Breadcrumb
                items={[
                  { title: "工作空间" },
                  { title: "特性管理" },
                  { title: page === "tree" ? "特性树" : "知识评测" },
                ]}
              />
            </Space>
            <Space size={20}>
              <Badge status="success" text="本地数据" />
              <span className="header-divider" />
              <Space>
                <Avatar
                  size="small"
                  shape="square"
                  icon={<DatabaseOutlined />}
                  className="workspace-avatar"
                />
                <Typography.Text>当前项目</Typography.Text>
              </Space>
            </Space>
          </Header>
          <Content className="admin-content">
            <section className="content-page" hidden={page !== "tree"}>
              {page === "tree" && (
                <TreePage
                  explorer={explorer}
                  tableMaximized={tableMaximized}
                  onToggleMaximize={() =>
                    setTableMaximized((current) => !current)
                  }
                />
              )}
            </section>
            <section className="content-page" hidden={page !== "evaluation"}>
              {error && (
                <Alert
                  type="error"
                  showIcon
                  title="知识数据读取失败"
                  description={error}
                  action={<Button onClick={explorer.refresh}>重试</Button>}
                />
              )}
              <KnowledgeSearch
                model={model}
                loading={loading}
                onOpenNode={openNode}
              />
            </section>
          </Content>
        </Layout>
      </Layout>
      <NodeDetails explorer={explorer} />
    </ConfigProvider>
  );
}
