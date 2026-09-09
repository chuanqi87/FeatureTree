import { useEffect, useRef, useState } from "react";
import { Button, Table, Tag, Tooltip, Typography } from "antd";
import { FileOutlined, FolderOpenOutlined } from "@ant-design/icons";
import { StatusTag } from "./ValueFields.jsx";
import QualityTags from "./QualityTags.jsx";

export default function NodeTable({ explorer }) {
  const {
    model,
    data,
    loading,
    selected,
    selectNode,
    expandedKeys,
    expandNode,
    tableRef,
  } = explorer;
  const container = useRef(null);
  const [height, setHeight] = useState(500);
  useEffect(() => {
    const region = container.current;
    const header = region.querySelector(".ant-table-header");
    const updateHeight = () => {
      const headerHeight = header?.getBoundingClientRect().height ?? 0;
      setHeight(Math.max(1, Math.floor(region.clientHeight - headerHeight)));
    };
    const observer = new ResizeObserver(updateHeight);
    observer.observe(region);
    if (header) observer.observe(header);
    updateHeight();
    return () => observer.disconnect();
  }, []);
  const columns = [
    {
      title: "特性节点",
      key: "name",
      width: 330,
      fixed: "left",
      render: (_, node) => (
        <div className="node-cell">
          <span className="node-type-icon">
            {node.knowledge_role === "rollup" ? <FolderOpenOutlined /> : <FileOutlined />}
          </span>
          <div>
            <Button
              type="link"
              className="node-title"
              onClick={() => selectNode(node.id)}
            >
              {node.name.zh}
            </Button>
            <Typography.Text className="node-id" type="secondary">
              {node.id}
            </Typography.Text>
          </div>
        </div>
      ),
    },
    {
      title: "层级",
      dataIndex: "level",
      width: 76,
      align: "center",
      render: (level) => (
        <Tag color={level === "L1" ? "blue" : undefined}>{level}</Tag>
      ),
    },
    {
      title: "类型",
      key: "role",
      width: 94,
      render: (_, node) => (
        <Typography.Text>
          {node.knowledge_role === "rollup" ? "分支节点" : "叶子节点"}
        </Typography.Text>
      ),
    },
    {
      title: "能力定义",
      dataIndex: "definition",
      width: 280,
      render: (text) => (
        <Tooltip title={text} placement="topLeft">
          <div className="definition-cell">{text}</div>
        </Tooltip>
      ),
    },
    {
      title: "平台支持",
      key: "platforms",
      children: Object.entries(model?.platforms ?? {}).map(
        ([key, platform]) => ({
          title: platform.name,
          key,
          width: 104,
          align: "center",
          render: (_, node) => (
            <Tooltip
              title={`复核状态：${node.platforms[key]?.verification === "in_review" ? "确认中" : node.platforms[key]?.verification === "confirmed" ? "已确认" : "未复核"}`}
            >
              <span>
                <StatusTag value={node.platforms[key]?.status ?? "unknown"} />
              </span>
            </Tooltip>
          ),
        }),
      ),
    },
    {
      title: "确认进度",
      key: "progress",
      width: 125,
      render: (_, node) => (
        <div className="progress-cell">
          <StatusTag value={node.comparison_progress.state} />
          <Typography.Text type="secondary">
            {node.comparison_progress.confirmed_support +
              node.comparison_progress.confirmed_comparisons}{" "}
            /{" "}
            {node.comparison_progress.total_support +
              node.comparison_progress.total_comparisons}{" "}
            项
          </Typography.Text>
        </div>
      ),
    },
    {
      title: "置信度 / 真机复核",
      key: "quality",
      width: 220,
      render: (_, node) => <QualityTags summary={node.quality_summary} />,
    },
    {
      title: "操作",
      key: "action",
      width: 94,
      fixed: "right",
      render: (_, node) => (
        <Button type="link" size="small" onClick={() => selectNode(node.id)}>
          查看详情
        </Button>
      ),
    },
  ];
  return (
    <div className="table-region" ref={container}>
      <Table
        ref={tableRef}
        className="feature-table"
        columns={columns}
        dataSource={data}
        rowKey="id"
        loading={loading}
        pagination={false}
        size="middle"
        scroll={{ x: 1630, y: height }}
        expandable={{
          childrenColumnName: "treeChildren",
          expandedRowKeys: expandedKeys,
          onExpand: expandNode,
          indentSize: 20,
        }}
        rowClassName={(node) =>
          `${node.id === selected ? "selected-row" : ""} ${node.match ? "matching-row" : ""}`
        }
        onRow={(node) => ({ onDoubleClick: () => selectNode(node.id) })}
        locale={{ emptyText: "没有匹配的节点，请调整搜索或筛选条件" }}
      />
    </div>
  );
}
