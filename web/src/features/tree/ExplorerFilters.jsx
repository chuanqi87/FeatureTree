import { useEffect, useRef } from "react";
import {
  Button,
  Card,
  Form,
  Input,
  InputNumber,
  Select,
  Typography,
} from "antd";
import { SearchOutlined } from "@ant-design/icons";
import {
  confidenceOptions,
  deviceReviewOptions,
} from "../../shared/quality.js";

export default function ExplorerFilters({ explorer }) {
  const { query, progressState, domain, model } = explorer;
  const search = useRef(null);
  useEffect(() => {
    const onKey = (event) => {
      if (
        event.key === "/" &&
        !["INPUT", "TEXTAREA"].includes(document.activeElement.tagName) &&
        !document.activeElement.isContentEditable
      ) {
        event.preventDefault();
        search.current?.focus();
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, []);
  return (
    <Card className="filter-card" size="small">
      <Form layout="inline" className="filter-form">
        <Form.Item label="特性领域">
          <Select
            showSearch
            optionFilterProp="label"
            value={domain}
            onChange={explorer.changeDomain}
            options={[
              { value: "", label: "全部领域" },
              ...(model?.roots ?? []).map((id) => ({
                value: id,
                label: model.byId.get(id).name.zh,
              })),
            ]}
          />
        </Form.Item>
        <Form.Item label="节点搜索">
          <Input
            ref={search}
            value={query}
            prefix={<SearchOutlined />}
            allowClear
            placeholder="名称、ID、别名或知识内容"
            onChange={(event) => explorer.setQuery(event.target.value)}
            onKeyDown={(event) => {
              if (event.key === "Escape") explorer.setQuery("");
            }}
          />
        </Form.Item>
        <Form.Item label="确认状态">
          <Select
            value={progressState}
            onChange={explorer.setProgressState}
            options={[
              { value: "", label: "全部状态" },
              { value: "not_started", label: "待确认" },
              { value: "in_progress", label: "确认中" },
              { value: "complete", label: "已完成" },
            ]}
          />
        </Form.Item>
        <Form.Item label="知识置信度">
          <Select
            aria-label="知识置信度"
            value={explorer.confidence}
            onChange={explorer.setConfidence}
            options={confidenceOptions}
          />
        </Form.Item>
        <Form.Item label="真机复核">
          <Select
            aria-label="真机复核"
            value={explorer.deviceReview}
            onChange={explorer.setDeviceReview}
            options={deviceReviewOptions}
            style={{ width: 210 }}
          />
        </Form.Item>
        <Form.Item label="节点类型">
          <Select
            aria-label="节点类型"
            value={explorer.role}
            onChange={explorer.setRole}
            options={[
              { value: "", label: "全部类型" },
              { value: "leaf", label: "仅叶子节点" },
              { value: "rollup", label: "仅分支节点" },
            ]}
          />
        </Form.Item>
        <Form.Item label="导出预算（知识项）">
          <InputNumber
            aria-label="导出预算"
            min={1}
            precision={0}
            value={explorer.reviewLimit}
            onChange={explorer.setReviewLimit}
            placeholder="不限"
          />
        </Form.Item>
        <Form.Item>
          <Button onClick={explorer.resetFilters}>重置</Button>
        </Form.Item>
      </Form>
      <Typography.Paragraph type="secondary" style={{ margin: "12px 0 0" }}>
        两项筛选作用于同一条结论。高可信不等于已实测；未评估不等于无需实测。优先级：实测不符
        → 必须复核 → 建议抽样 → 补证据/评级。
      </Typography.Paragraph>
    </Card>
  );
}
