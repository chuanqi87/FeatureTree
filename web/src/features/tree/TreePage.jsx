import { useMemo, useState } from 'react';
import { ApartmentOutlined, FileTextOutlined, FolderOutlined, SearchOutlined } from '@ant-design/icons';
import { Button, Empty, Input, Segmented, Space, Switch, Tag, Tree, Typography } from 'antd';
import { useResource } from '../../shared/useResource.js';
import { ResourceState } from '../../shared/components.jsx';
import { browseNodes, flattenNodes, visibleViews } from './browserModel.js';
import FeatureDetail from './FeatureDetail.jsx';

export default function TreePage({ releaseId }) {
  const resource = useResource(`tree-browser${releaseId ? `?release_id=${releaseId}` : ''}`, 10000);
  const [status, setStatus] = useState('all'), [history, setHistory] = useState(false), [query, setQuery] = useState('');
  const [selected, setSelected] = useState(null), [expanded, setExpanded] = useState([]);
  const views = useMemo(() => visibleViews(resource.data?.items || [], status, history), [resource.data, status, history]);
  const nodes = useMemo(() => browseNodes(views, query), [views, query]);
  const flat = useMemo(() => flattenNodes(nodes), [nodes]);
  const active = flat.find(node => node.key === selected) || null;
  const leaves = visibleViews(resource.data?.items || [], 'all', history).flatMap(view => view.features.filter(node => node.node_type === 'leaf').map(node => ({ ...node, view })));
  function select(node) { setSelected(node.key); setExpanded(keys => [...new Set([...keys, ...node.ancestors, node.key])]); }
  return <>
    <div className="tree-heading"><div><Typography.Title level={2}><ApartmentOutlined /> 特性树</Typography.Title><Typography.Text type="secondary">展开特性，逐层查看子特性、叶子与三端 API。</Typography.Text></div><Space wrap><Tag color="green">正式 {new Set(leaves.filter(node => node.view.status === 'formal').map(node => node.id)).size} 叶子</Tag><Tag color="gold">候选 {new Set(leaves.filter(node => node.view.status === 'candidate').map(node => node.id)).size} 叶子</Tag></Space></div>
    <div className="tree-browser"><aside className="tree-navigation">
      <Input prefix={<SearchOutlined />} placeholder="搜索特性名称或定义" value={query} onChange={event => setQuery(event.target.value)} allowClear />
      <Segmented block value={status} onChange={setStatus} options={[{ value: 'all', label: '全部' }, { value: 'formal', label: '正式' }, { value: 'candidate', label: '候选' }]} />
      <div className="tree-controls"><Button size="small" type="text" onClick={() => setExpanded(flat.filter(node => !node.isLeaf).map(node => node.key))}>全部展开</Button><Button size="small" type="text" onClick={() => { setQuery(''); setExpanded([]); }}>收起</Button></div>
      <ResourceState resource={resource}>{nodes.length ? <Tree blockNode showLine={{ showLeafIcon: false }} showIcon treeData={nodes} expandedKeys={query ? flat.filter(node => node.children.length).map(node => node.key) : expanded} onExpand={setExpanded} selectedKeys={active ? [active.key] : []} onSelect={(_, info) => select(info.node)} icon={node => node.isLeaf ? <FileTextOutlined /> : <FolderOutlined />} titleRender={node => <div className="feature-tree-label"><span>{node.name}</span><span className="tree-node-tags"><Tag color={node.view.status === 'candidate' ? 'gold' : 'green'}>{node.view.status === 'candidate' ? '候选' : '正式'}</Tag><small>{node.isLeaf ? '叶子' : `${node.children.length} 项`}</small>{history && !node.parent_id && <small>{node.view.updated_at ? new Date(node.view.updated_at).toLocaleString('zh-CN') : '当前发布'}{node.view.run_status === 'cancelled' ? ' · 已取消' : ''}</small>}</span></div>} /> : <Empty image={Empty.PRESENTED_IMAGE_SIMPLE} description={query ? '没有匹配的特性' : status === 'formal' ? '尚未正式发布，可切换到全部查看候选' : '暂无特性'} />}</ResourceState>
      <div className="tree-history"><Switch size="small" checked={history} onChange={setHistory} /><Typography.Text type="secondary">显示历史候选快照</Typography.Text><p>默认按相同范围显示较新的未取消候选。候选与正式版本分别标记。</p></div>
    </aside><main className="tree-detail-panel"><FeatureDetail node={active} onSelect={select} /></main></div>
  </>;
}
