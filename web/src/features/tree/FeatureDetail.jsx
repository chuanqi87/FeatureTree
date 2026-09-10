import { Alert, Button, Card, Collapse, Descriptions, Empty, Space, Tabs, Tag, Typography } from 'antd';
import { useResource } from '../../shared/useResource.js';
import { JsonDetails, ResourceState, Status } from '../../shared/components.jsx';
import { safeUrl } from '../../shared/model.js';
import Article from '../knowledge/Article.jsx';

const platforms = [['android', 'Android'], ['ios', 'iOS'], ['harmonyos', 'HarmonyOS']];

function ApiList({ bindings, platform }) {
  const rows = bindings.filter(row => (row.api?.platform || 'unknown') === platform);
  if (!rows.length) return <Empty image={Empty.PRESENTED_IMAGE_SIMPLE} description="尚未关联 API，不能据此判断平台不支持" />;
  return <div className="api-list">{rows.map((row, index) => <Card size="small" key={`${row.declaration_id}:${row.route_id}:${index}`}>
    <Space wrap><Tag color={row.role === 'core' ? 'blue' : 'default'}>{row.role === 'core' ? '核心 API' : '辅助 API'}</Tag><Typography.Text strong className="api-name">{row.api?.qualified_name || '来源记录待补齐'}</Typography.Text></Space>
    <Typography.Paragraph className="api-usage">{row.usage}</Typography.Paragraph>
    {row.api && <Space wrap><Tag>{row.api.sdk_version}</Tag>{row.api.availability?.since && <Tag>起始版本 {row.api.availability.since}</Tag>}<Tag>公开性：{({ public: '公开', unknown: '待核实', private: '非公开' })[row.api.visibility] || row.api.visibility}</Tag>{row.api.availability?.historical && <Tag color="orange">历史来源</Tag>}{safeUrl(row.api.url) && <Typography.Link href={row.api.url} target="_blank" rel="noreferrer">官方文档</Typography.Link>}</Space>}
    <Collapse ghost items={[{ key: 'source', label: '查看声明与实现路线', children: <><Typography.Paragraph code className="api-signature">{row.api?.signature || row.declaration_id}</Typography.Paragraph><Descriptions size="small" column={1} items={[{ key: 'route', label: '实现路线', children: row.route_id }, { key: 'file', label: '来源文件', children: row.api?.source_path || '缺失' }]} /><JsonDetails title="来源记录与证据引用" value={row} /></> }]} />
  </Card>)}</div>;
}

function FeatureKnowledge({ node }) {
  const article = useResource(node.view.status === 'formal' && node.node_type === 'leaf' ? `knowledge/${node.id}?release_id=${node.view.id}` : null);
  if (node.view.status !== 'formal') return <Empty image={Empty.PRESENTED_IMAGE_SIMPLE} description="候选节点尚未发布正式知识；可在叶子知识页查看已生成的样稿" />;
  return <ResourceState resource={article}>{article.data && <Article article={article.data.article} reference={article.data.article_ref} />}</ResourceState>;
}

export default function FeatureDetail({ node, onSelect }) {
  const detail = useResource(node ? `tree-browser/${node.view.id}/${node.id}${node.view.status === 'formal' ? `?release_id=${node.view.id}` : ''}` : null);
  if (!node) return <div className="tree-detail-empty"><Empty description="从左侧选择特性，查看子特性和关联 API" /></div>;
  const bindings = detail.data?.bindings || [];
  const candidate = node.view.status === 'candidate';
  const scope = <Descriptions column={1} size="small" items={[
    { key: 'include', label: '包含范围', children: <ul>{(node.includes || []).map(item => <li key={item}>{item}</li>)}</ul> },
    { key: 'exclude', label: '排除范围', children: <ul>{(node.excludes || []).map(item => <li key={item}>{item}</li>)}</ul> },
    { key: 'success', label: '成功标准', children: <ul>{(node.success_criteria || []).map(item => <li key={item}>{item}</li>)}</ul> },
  ]} />;
  const apiTabs = [...platforms, ...(bindings.some(row => !row.api || !platforms.some(([id]) => id === row.api.platform)) ? [['unknown', '来源待核实']] : [])].map(([id, label]) => ({ key: id, label: `${label} · ${new Set(bindings.filter(row => (row.api?.platform || 'unknown') === id).map(row => row.declaration_id)).size}`, children: <ApiList bindings={bindings} platform={id} /> }));
  return <div className="feature-detail">
    <div className="feature-breadcrumb">{node.view.features.filter(feature => node.ancestors.includes(`${node.view.id}:${feature.id}`)).map(feature => feature.name).join(' / ') || '特性树'} / {node.name}</div>
    <Space wrap><Tag color={candidate ? 'gold' : 'green'}>{candidate ? '候选' : '正式'}</Tag><Tag>{node.node_type === 'leaf' ? '叶子节点' : '分支'}</Tag>{candidate && <Status value={node.view.run_status} />}</Space>
    <Typography.Title level={3}>{node.name}</Typography.Title><Typography.Paragraph>{node.definition}</Typography.Paragraph>
    {candidate && <Alert type="warning" showIcon title="候选内容，尚未正式发布" description="关联 API 表示当前研究的实现依据，路线完整性和能力结论仍需审查。" />}
    {node.node_type !== 'leaf' && <section className="child-features"><Typography.Title level={5}>子特性 · {node.children.length}</Typography.Title>{node.children.length ? node.children.map(child => <Button block className="child-feature" key={child.key} onClick={() => onSelect(child)}><span>{child.name}</span><Tag>{child.isLeaf ? '叶子' : '分支'}</Tag><span>→</span></Button>) : <Empty image={Empty.PRESENTED_IMAGE_SIMPLE} description="该分支尚待展开" />}</section>}
    <Tabs key={node.key} defaultActiveKey={node.isLeaf ? 'apis' : 'scope'} items={[
      { key: 'apis', label: `关联 API${detail.data ? ` · ${new Set(bindings.map(row => row.declaration_id)).size}` : ''}`, children: <ResourceState resource={detail}><Tabs items={apiTabs} /></ResourceState> },
      { key: 'scope', label: '能力范围', children: scope },
      ...(node.isLeaf ? [{ key: 'knowledge', label: '三端知识', children: <FeatureKnowledge node={node} /> }] : []),
    ]} />
    <Collapse ghost items={[{ key: 'version', label: '版本与追溯', children: <JsonDetails title="固定版本信息" value={{ status: node.view.status, feature_id: node.id, tree_ref: node.view.tree_ref, bindings_ref: node.view.bindings_ref, snapshot_id: detail.data?.snapshot_id, run_id: node.view.run_id, updated_at: node.view.updated_at }} /> }]} />
  </div>;
}
