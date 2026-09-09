import { Alert, Descriptions, List, Space, Tag, Typography } from "antd";
import { checkNames } from "./model.js";
import { safeUrl } from "../../shared/format.js";

export default function StageResult({ task }) {
  const result = task.payload;
  const last = task.attempts.at(-1);
  return (
    <div className="workflow-stage-result">
      {(task.artifact_error || last?.error) && (
        <Alert
          type="error"
          showIcon
          title="执行问题"
          description={task.artifact_error || last.error}
        />
      )}
      {!result && !last?.error && (
        <Typography.Text type="secondary">该阶段尚未返回结果。</Typography.Text>
      )}
      {result?.axis && (
        <Typography.Paragraph>
          <strong>划分轴：</strong>
          {result.axis}
        </Typography.Paragraph>
      )}
      {result?.groups && (
        <List
          size="small"
          dataSource={result.groups}
          renderItem={(g) => (
            <List.Item>
              <List.Item.Meta title={g.name} description={g.definition} />
            </List.Item>
          )}
        />
      )}
      {result?.candidates && (
        <List
          size="small"
          dataSource={result.candidates}
          renderItem={(c) => (
            <List.Item>
              <List.Item.Meta
                title={
                  <Space wrap>
                    {c.name}
                    <Tag>{c.distribution}</Tag>
                  </Space>
                }
                description={
                  <>
                    {c.definition}
                    <br />
                    {safeUrl(c.binding.url) ? (
                      <Typography.Link
                        href={safeUrl(c.binding.url)}
                        target="_blank"
                        rel="noopener noreferrer"
                      >
                        {c.binding.id}
                      </Typography.Link>
                    ) : (
                      c.binding.id
                    )}
                    <div>{c.conditions.join("；")}</div>
                  </>
                }
              />
            </List.Item>
          )}
        />
      )}
      {result?.checks && (
        <Descriptions
          column={1}
          size="small"
          bordered
          items={Object.entries(result.checks).map(([key, check]) => ({
            key,
            label: checkNames[key] || key,
            children: (
              <>
                <Tag color={check.status === "pass" ? "success" : "warning"}>
                  {check.status === "pass" ? "通过" : "待处理"}
                </Tag>
                {check.reason}
              </>
            ),
          }))}
        />
      )}
      {result?.issues?.map((issue, index) => (
        <Alert
          key={index}
          type={issue.severity === "blocking" ? "error" : "warning"}
          showIcon
          title={`${issue.node_id} · ${issue.message}`}
          description={issue.requested_change}
        />
      ))}
      {result?.results && (
        <List
          size="small"
          dataSource={result.results}
          renderItem={(item) => (
            <List.Item>
              <List.Item.Meta
                title={`${item.id} · ${item.anchor_status}`}
                description={item.bindings
                  .map((b) => `${b.platform}: ${b.symbol} — ${b.reason}`)
                  .join("；")}
              />
            </List.Item>
          )}
        />
      )}
      {(result?.gaps || result?.questions || []).map((gap, index) => (
        <Typography.Paragraph key={index} type="secondary">
          待核实：{gap}
        </Typography.Paragraph>
      ))}
      {result?.nodes && (
        <Typography.Text>
          生成 {result.nodes.length} 个候选节点，见下方候选结果。
        </Typography.Text>
      )}
    </div>
  );
}
