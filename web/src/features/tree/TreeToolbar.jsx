import { Button, Space, Tabs, Tag, Tooltip, Typography } from "antd";
import {
  ClusterOutlined,
  FullscreenExitOutlined,
  FullscreenOutlined,
  TableOutlined,
} from "@ant-design/icons";

export default function TreeToolbar({ explorer, maximized, onToggleMaximize }) {
  return (
    <div className="table-tabs">
      <Tabs
        activeKey={explorer.view}
        onChange={explorer.setView}
        items={[
          { key: "table", label: "树形表格", icon: <TableOutlined /> },
          { key: "graph", label: "关系图", icon: <ClusterOutlined /> },
        ]}
        tabBarExtraContent={{
          left: (
            <Space className="tree-title">
              <Typography.Text strong>
                {explorer.domain
                  ? explorer.model?.byId.get(explorer.domain)?.name.zh
                  : "全部特性"}
              </Typography.Text>
              <Tag>{explorer.tree.scopeCount}</Tag>
            </Space>
          ),
          right: (
            <Space size={8}>
              <Typography.Text type="secondary" className="visible-count">
                {explorer.filtering
                  ? `${explorer.tree.matchCount} 个匹配 · 保留祖先路径`
                  : `${explorer.tree.rows.length} 个节点`}
              </Typography.Text>
              <Button
                size="small"
                onClick={explorer.exportReviewScope}
                disabled={!explorer.reviewScope?.selected_claims}
              >
                导出复核清单（{explorer.reviewScope?.selected_claims ?? 0}/
                {explorer.reviewScope?.total_matching_claims ?? 0} 项）
              </Button>
              <Button
                size="small"
                onClick={explorer.expandAll}
                disabled={explorer.filtering}
              >
                全部展开
              </Button>
              <Button
                size="small"
                onClick={explorer.collapseAll}
                disabled={explorer.filtering}
              >
                全部收起
              </Button>
              <Tooltip title={maximized ? "退出最大化（Esc）" : "最大化表格"}>
                <Button
                  size="small"
                  icon={
                    maximized ? (
                      <FullscreenExitOutlined />
                    ) : (
                      <FullscreenOutlined />
                    )
                  }
                  aria-label={maximized ? "退出最大化" : "最大化表格"}
                  aria-pressed={maximized}
                  onClick={onToggleMaximize}
                />
              </Tooltip>
            </Space>
          ),
        }}
      />
    </div>
  );
}
