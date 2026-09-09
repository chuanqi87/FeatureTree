import { useMemo, useState } from "react";
import {
  Alert,
  Button,
  Card,
  Empty,
  Input,
  Pagination,
  Space,
  Tag,
  Typography,
} from "antd";
import { buildKnowledgeIndex, searchKnowledge } from "./search.js";
import { StatusTag } from "../../shared/components/ValueFields.jsx";
import { ConfidenceTag } from "../../shared/components/QualityTags.jsx";

const PAGE_SIZE = 10;

export default function KnowledgeSearch({ model, loading, onOpenNode }) {
  const [input, setInput] = useState("");
  const [query, setQuery] = useState("");
  const [page, setPage] = useState(1);
  const index = useMemo(() => buildKnowledgeIndex(model), [model]);
  const results = useMemo(() => searchKnowledge(index, query), [index, query]);
  const submit = (value) => {
    setInput(value);
    setQuery(value.trim());
    setPage(1);
  };
  const visible = results.slice((page - 1) * PAGE_SIZE, page * PAGE_SIZE);

  return (
    <section className="knowledge-search">
      <div className="page-heading">
        <Space>
          <Typography.Title level={3}>知识评测</Typography.Title>
          <Tag color="blue">知识检索</Tag>
        </Space>
        <Typography.Text type="secondary">
          {model?.nodes.length ?? 0} 个节点
        </Typography.Text>
      </div>
      <Card className="knowledge-query-card">
        <Typography.Paragraph type="secondary">
          输入问题或关键词，检索当前特性树、知识正文和跨平台差异记录。
        </Typography.Paragraph>
        <Input.Search
          size="large"
          value={input}
          onChange={(event) => setInput(event.target.value)}
          onSearch={submit}
          allowClear
          enterButton="检索"
          loading={loading}
          disabled={!model}
          placeholder="例如：BLE 扫描过滤有哪些差异？"
          aria-label="检索问题或关键词"
        />
        <Space className="search-examples" wrap>
          <Typography.Text type="secondary">试试：</Typography.Text>
          {["BLE 扫描过滤有哪些差异？", "后台任务", "跨应用调用"].map(
            (example) => (
              <Button
                key={example}
                size="small"
                type="link"
                disabled={!model}
                onClick={() => submit(example)}
              >
                {example}
              </Button>
            ),
          )}
        </Space>
      </Card>
      <Alert
        type="info"
        showIcon
        title="结果来自现有知识记录。检索命中不代表结论已核实，历史支持判断不参与本次检索。"
      />
      <div className="knowledge-results" aria-live="polite">
        {!query ? (
          <Empty
            image={Empty.PRESENTED_IMAGE_SIMPLE}
            description="输入问题或关键词开始检索"
          />
        ) : !results.length ? (
          <Empty
            image={Empty.PRESENTED_IMAGE_SIMPLE}
            description={`没有找到与“${query}”相关的内容，试试节点名称、API 名称或更短的关键词。`}
          />
        ) : (
          <>
            <Typography.Paragraph type="secondary">
              “{query}”找到 {results.length} 个相关节点，按关键词相关度排序。
            </Typography.Paragraph>
            {visible.map(({ node, snippets }) => (
              <Card
                key={node.id}
                className="knowledge-result"
                size="small"
                title={
                  <Space wrap>
                    <Button
                      type="link"
                      className="search-result-title"
                      onClick={() => onOpenNode(node.id)}
                    >
                      {node.name.zh}
                    </Button>
                    <Tag>{node.level}</Tag>
                    <StatusTag value={node.comparison_progress.state} />
                  </Space>
                }
                extra={
                  <Button
                    type="link"
                    size="small"
                    onClick={() => onOpenNode(node.id)}
                  >
                    查看节点
                  </Button>
                }
              >
                <Typography.Paragraph
                  type="secondary"
                  className="search-result-id"
                >
                  {node.id}
                </Typography.Paragraph>
                <Typography.Paragraph>{node.definition}</Typography.Paragraph>
                {snippets
                  .filter((item) => item.field !== "definition")
                  .map((item) => (
                    <div className="search-fragment" key={item.field}>
                      <Space wrap>
                        <Typography.Text strong>{item.section}</Typography.Text>
                        <ConfidenceTag level={item.confidence} />
                        {item.verification && (
                          <StatusTag value={item.verification} />
                        )}
                      </Space>
                      <Typography.Paragraph
                        ellipsis={{
                          rows: 3,
                          expandable: true,
                          symbol: "展开片段",
                        }}
                      >
                        {item.text}
                      </Typography.Paragraph>
                      <Typography.Text
                        type="secondary"
                        className="search-field"
                      >
                        来源：{item.sourcePath} · {item.field}
                      </Typography.Text>
                    </div>
                  ))}
                <Typography.Text type="secondary" className="search-source">
                  知识记录：{node.knowledge_path}
                </Typography.Text>
              </Card>
            ))}
          </>
        )}
      </div>
      {results.length > PAGE_SIZE && (
        <Pagination
          current={page}
          pageSize={PAGE_SIZE}
          total={results.length}
          showSizeChanger={false}
          onChange={setPage}
        />
      )}
    </section>
  );
}
