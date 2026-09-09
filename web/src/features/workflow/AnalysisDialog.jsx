import { useEffect, useState } from "react";
import {
  Alert,
  Collapse,
  Form,
  Input,
  InputNumber,
  Modal,
  Select,
  Space,
  Tag,
  Typography,
} from "antd";
import { analysisTargets } from "./model.js";

export default function AnalysisDialog({
  selection,
  model,
  workflow,
  onClose,
  onCreated,
}) {
  const [form] = Form.useForm();
  const [error, setError] = useState("");
  const nodes = Form.useWatch("nodes", form) || [];
  const baselineId = Form.useWatch("baseline_id", form);
  const action = selection.action;
  const targets = analysisTargets(model, nodes, action);
  const preset = workflow.config?.baselines.find((b) => b.id === baselineId);
  const unknown =
    preset &&
    Object.values(preset.baseline.platforms).some(
      (p) => p.status !== "verified",
    );
  useEffect(() => {
    if (!workflow.config) return;
    form.setFieldsValue({
      ...workflow.config.defaults,
      nodes: [selection.nodeId],
      depth: 1,
      baseline_id: workflow.config.baselines[0]?.id,
    });
    // Initialize this dialog once; background status polling must not reset edits.
  }, [form, selection.nodeId, action, Boolean(workflow.config)]);

  async function submit() {
    try {
      const values = await form.validateFields();
      setError("");
      const run = await workflow.create({
        ...values,
        action,
        source_node: selection.nodeId,
      });
      onCreated(run.id);
    } catch (problem) {
      if (problem.message) setError(problem.message);
    }
  }
  const budget = (
    <div className="workflow-form-grid">
      <Form.Item
        name="max_nodes"
        label="每节点直接子能力预算"
        rules={[{ required: true }]}
      >
        <InputNumber min={1} max={200} />
      </Form.Item>
      <Form.Item name="workers" label="并发执行数" rules={[{ required: true }]}>
        <InputNumber min={1} max={workflow.config?.slots || 6} />
      </Form.Item>
      <Form.Item
        name="timeout"
        label="单阶段超时（秒）"
        rules={[{ required: true }]}
      >
        <InputNumber min={30} max={7200} />
      </Form.Item>
      <Form.Item
        name="first_response_timeout"
        label="首次响应等待（秒）"
        tooltip="在此时间内没有模型文本或工具结果会停止，不自动重复消耗同一调用。已有活动的研究仍受单阶段超时限制。"
        rules={[{ required: true }]}
      >
        <InputNumber min={1} max={7200} />
      </Form.Item>
      <Form.Item name="model" label="模型">
        <Input placeholder="留空使用 OpenCode 默认模型" />
      </Form.Item>
      <Form.Item name="variant" label="推理配置">
        <Input placeholder="如 high；需同时指定模型" />
      </Form.Item>
    </div>
  );
  return (
    <Modal
      open
      title={action === "root" ? "根节点分析" : "下钻分析"}
      width={720}
      onCancel={onClose}
      onOk={submit}
      okText="开始分析"
      confirmLoading={workflow.busy}
      okButtonProps={{
        disabled: !workflow.config?.available || !targets.length,
      }}
    >
      <Typography.Paragraph type="secondary">
        {action === "root"
          ? "先研究所属 L1 领域的三端实现 API，再设计直接 L2 特性。"
          : "先研究所选分支的三端实现 API，再决定继续细分或确认停止；可多选并行。"}
      </Typography.Paragraph>
      {error && (
        <Alert type="error" showIcon title="未能开始分析" description={error} />
      )}
      {workflow.config && !workflow.config.available && (
        <Alert type="error" showIcon title="本机尚未找到 OpenCode" />
      )}
      <Form form={form} layout="vertical">
        <Form.Item
          name="nodes"
          label="选择分析节点"
          rules={[{ required: true, type: "array", min: 1 }]}
        >
          <Select
            mode="multiple"
            showSearch
            optionFilterProp="label"
            options={model.nodes
              .filter((n) => action === "root" || n.granularity === "branch")
              .map((n) => ({ value: n.id, label: `${n.name.zh} · ${n.id}` }))}
          />
        </Form.Item>
        <div className="workflow-targets">
          <Typography.Text strong>实际执行范围：</Typography.Text>
          <Space wrap>
            {targets.map((id) => (
              <Tag key={id} color="blue">
                {model.byId.get(id).name.zh} · {id}
              </Tag>
            ))}
          </Space>
        </div>
        <div className="workflow-form-grid">
          <Form.Item
            name="depth"
            label="每轮一层（父层先验收）"
            rules={[{ required: true }]}
          >
            <InputNumber min={1} max={1} disabled />
          </Form.Item>
          <Form.Item
            name="baseline_id"
            label="版本基线"
            rules={[{ required: true }]}
          >
            <Select
              options={workflow.config?.baselines.map((b) => ({
                value: b.id,
                label: b.label,
              }))}
            />
          </Form.Item>
        </div>
        {preset && (
          <Typography.Paragraph type="secondary">
            基线日期：{preset.baseline.as_of}。
            {unknown
              ? "平台版本尚待核实，结果用于树设计。"
              : "使用已保存的平台版本基线。"}
          </Typography.Paragraph>
        )}
        <Collapse
          items={[{ key: "budgets", label: "执行参数", children: budget }]}
        />
      </Form>
      <Typography.Paragraph className="workflow-explanation" type="secondary">
        各平台分别去重计数，目标约 40 个 API，任一端超过 50 必须拆分。清单不完整不能认定已拆分完成。
      </Typography.Paragraph>
    </Modal>
  );
}
