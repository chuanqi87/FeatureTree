import { Alert, Badge, Button, Card, Space, Tag, Typography } from "antd";
import { ReloadOutlined } from "@ant-design/icons";
import OverviewStats from "./OverviewStats.jsx";
import ExplorerFilters from "./ExplorerFilters.jsx";
import TreeToolbar from "./TreeToolbar.jsx";
import NodeTable from "./NodeTable.jsx";
import TreeGraph from "./TreeGraph.jsx";
import ReviewScopePreview from "./ReviewScopePreview.jsx";

export default function TreePage({
  explorer,
  tableMaximized,
  onToggleMaximize,
  onAnalyze,
}) {
  const { model, stats, domain, loading, error } = explorer;
  return (
    <>
      <div className="page-heading">
        <div>
          <Space>
            <Typography.Title level={3}>特性树管理</Typography.Title>
            <Tag color="blue">
              {domain ? model?.byId.get(domain)?.name.zh : "全部领域"}
            </Tag>
          </Space>
        </div>
        <Space>
          <Button
            icon={<ReloadOutlined />}
            onClick={explorer.refresh}
            loading={loading}
          >
            刷新数据
          </Button>
        </Space>
      </div>
      <OverviewStats stats={stats} model={model} domain={domain} />
      {error && (
        <Alert
          type="error"
          showIcon
          title={
            model ? "刷新失败，仍显示上一次读取的数据" : "无法读取项目数据"
          }
          description={error}
          action={
            <Button size="small" onClick={explorer.refresh}>
              重试
            </Button>
          }
        />
      )}
      <ExplorerFilters explorer={explorer} />
      <Card className="tree-card" styles={{ body: { padding: 0 } }}>
        <TreeToolbar
          explorer={explorer}
          maximized={tableMaximized}
          onToggleMaximize={() => onToggleMaximize()}
        />
        {explorer.view === "table" ? (
          <NodeTable explorer={explorer} onAnalyze={onAnalyze} />
        ) : (
          <TreeGraph
            rows={explorer.tree.rows}
            selected={explorer.selected}
            onSelect={explorer.selectNode}
          />
        )}
        <div className="table-footer">
          <Space>
            <Badge status="default" />
            <Typography.Text type="secondary">
              支持情况与确认状态分别记录，待确认不表示不支持。
            </Typography.Text>
          </Space>
          <Typography.Text type="secondary">
            {model
              ? `读取时间：${new Date(model.generated_at).toLocaleTimeString("zh-CN", { hour12: false })}`
              : "正在读取数据"}
          </Typography.Text>
        </div>
      </Card>
      <ReviewScopePreview explorer={explorer} />
    </>
  );
}
