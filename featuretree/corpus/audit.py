"""Export reproducible corpus counts and integrity results without semantic coverage claims."""

import gzip
import hashlib
import json
from os.path import relpath
from pathlib import Path

from ..storage import ROOT
from .store import now


def verify_catalogs(root):
    errors=[];count=0
    for metadata_path in (root/'catalogs').rglob('*.meta.json'):
        try:
            meta=json.loads(metadata_path.read_text())
            raw_path=metadata_path.with_name(metadata_path.name.removesuffix('.meta.json'))
            if not raw_path.exists():
                raw_path=raw_path.with_name(raw_path.name+'.gz')
            raw=raw_path.read_bytes()
            if raw_path.suffix=='.gz':
                raw=gzip.decompress(raw)
            if hashlib.sha256(raw).hexdigest()!=meta['sha256']:
                raise ValueError('Catalog hash mismatch')
            count+=1
        except (ValueError,OSError,EOFError,KeyError) as error:
            errors.append({'path':str(metadata_path),'error':str(error)})
    return count,errors


def audit(corpus, output, verify_files=False):
    output=Path(output);output.mkdir(parents=True,exist_ok=True)
    errors=[];captured=0
    with (output/'documents.jsonl').open('w') as manifest:
        for record in corpus.db.execute('SELECT * FROM documents ORDER BY platform,url'):
            row=dict(record)
            manifest.write(json.dumps(row,ensure_ascii=False)+'\n')
            if not row['snapshot']:
                continue
            captured+=1
            if verify_files:
                try:
                    corpus.body(row)
                    raw=gzip.decompress((corpus.root/row['raw_path']).read_bytes())
                    if hashlib.sha256(raw).hexdigest()!=row['raw_sha256']:
                        raise ValueError('Raw response hash mismatch')
                except (ValueError,OSError,EOFError) as error:
                    errors.append({'url':row['url'],'error':str(error)})
    catalog_count,catalog_errors=verify_catalogs(corpus.root) if verify_files else (0,[])
    errors.extend(catalog_errors)
    stage=[dict(r) for r in corpus.db.execute('''SELECT platform,status,count(*) AS count
        FROM documents WHERE priority<=40 GROUP BY platform,status ORDER BY platform,status''')]
    report={'generated_at':now(),'captured_documents':captured,'statistics':corpus.stats(),
            'verified_catalog_snapshots':catalog_count,
            'priority_documents':stage,'integrity_verified':verify_files,'integrity_errors':errors,
            'all_discovered_bodies_captured':not corpus.db.execute("SELECT 1 FROM documents WHERE status NOT IN ('ready','thin','excluded') LIMIT 1").fetchone(),
            'complete_offline_mirror':False,
            'semantic_or_version_verification_complete':False,
            'definitions':{'ready':'Readable official body indexed; claims and versions still require verification',
                           'thin':'Captured but insufficient standalone text; retained for navigation',
                           'partial':'Structured source captured; normalized rendering has unsupported types',
                           'pending':'Discovered URL not yet fetched',
                           'not_found':'Requested body representations returned 404/410; this does not prove the navigation page or platform capability is absent',
                           'failed':'Network or parsing error; inspect error and retry',
                           'blocked':'Remote authentication/access response; no bypass attempted',
                           'excluded':'Non-document resource excluded by the official document URL rules'},
            'priority_scope':'Current guides, framework/Kit/module pages and explicitly cited sources; deeper symbol pages and historical Android API diffs may be retrieved on demand.'}
    (output/'summary.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    lines=['# 官方文档准备进度','',f"核验时间：{report['generated_at']}",'',
           f'已保存原始响应的文档：{captured}。',
           f"全文完整性校验：{'通过' if verify_files and not errors else '失败' if errors else '未执行'}。",'',
           '| 平台 | 状态 | 数量 | 原始正文大小（字节） |','| --- | --- | ---: | ---: |']
    lines.extend(f"| {r['platform']} | {r['status']} | {r['count']} | {r['raw_bytes'] or 0} |" for r in report['statistics'])
    guide_path = Path(relpath(ROOT/'docs/official-corpus.md', output.resolve())).as_posix()
    lines.extend(['','ready 表示正文可读取和检索，不代表知识、版本或平台支持已确认。',
                  'thin 表示已下载但正文较少；partial 表示结构化原文已保存、规范化渲染有未支持类型。',
                  'pending / failed / not_found / blocked 不计入已完成正文。',
                  'not_found 仅表示尝试的正文表示返回 404/410，不证明官网页面或平台能力不存在。',
                  '本资料库不是已验证的全站离线镜像；目录发现和正文下载也不构成每个知识节点的证据覆盖证明。',
                  f'本次目录来源、下载范围和使用命令见 [官方资料库]({guide_path})。',
                  '逐 URL 状态、路径、哈希、错误和优先级可由 audit 命令导出为 documents.jsonl，该导出可删除重建。',''])
    (output/'progress.md').write_text('\n'.join(lines))
    return {k:v for k,v in report.items() if k not in ('definitions','priority_scope')}
