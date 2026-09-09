import { Card, Statistic, Tooltip } from "antd";
import {
  ApartmentOutlined,
  BranchesOutlined,
  FileOutlined,
  CheckCircleOutlined,
} from "@ant-design/icons";

export default function OverviewStats({ stats, model, domain }) {
  return (
    <div className="stat-grid">
      {[
        {
          title: "比较节点",
          value: stats?.total,
          icon: <ApartmentOutlined />,
          color: "blue",
          note: `${domain ? 1 : (model?.roots.length ?? 0)} 个领域 · 最深 L${stats?.depth ?? "—"}`,
        },
        {
          title: "分支节点",
          value: stats ? stats.total - stats.leaves : null,
          icon: <BranchesOutlined />,
          color: "purple",
          note: "领域与分类分支，包含尚待生成子能力的入口",
        },
        {
          title: "叶子节点",
          value: stats?.leaves,
          icon: <FileOutlined />,
          color: "cyan",
          note: "独立的最小比较单元",
        },
        {
          title: "确认中",
          value: stats?.reviewing,
          icon: <CheckCircleOutlined />,
          color: "orange",
          note: `${stats?.complete ?? 0} 个节点已完成确认`,
        },
      ].map((item) => (
        <Card key={item.title} className="stat-card" size="small">
          <div className="stat-content">
            <Statistic title={item.title} value={item.value ?? "—"} />
            <Tooltip title={item.note}>
              <span
                className={`stat-icon ${item.color}`}
                aria-label={item.note}
              >
                {item.icon}
              </span>
            </Tooltip>
          </div>
        </Card>
      ))}
    </div>
  );
}
