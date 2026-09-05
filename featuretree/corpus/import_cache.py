"""Reuse verified official responses while preserving their original capture time."""

import hashlib
import json
from pathlib import Path

from .extract import parse
from .urls import canonical


def import_response(corpus, url, path, expected_hash, fetched_at, content_type):
    retrieved_url = url
    url = canonical(url)
    if not url or not path.is_file():
        return 'missing'
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected_hash:
        return 'hash_mismatch'
    corpus.add(url, priority=15, source=str(path))
    row = corpus.get(url)
    if row['status'] in ('ready','thin'):
        return 'already_present'
    try:
        content = parse(raw,url,content_type)
    except (ValueError,UnicodeError) as error:
        return 'parse_error: '+str(error)
    corpus.save(row,raw,content,retrieved_url,fetched_at)
    return content.quality


def import_previous(corpus, previous_root, progress=print):
    root = Path(previous_root)
    manifest = root/'ontology/official/evidence/harmonyos.manifest.json'
    data = json.loads(manifest.read_text())
    counts = {}
    for i, source in enumerate(data['remote_inputs'],1):
        path = root/'.firecrawl/harmonyos-evidence-cache'/(hashlib.sha256(source['url'].encode()).hexdigest()+'.md')
        result = import_response(corpus,source['url'],path,source['sha256'],data['generated_at'],'text/markdown')
        counts[result] = counts.get(result,0)+1
        if i%100==0:
            corpus.db.commit()
            progress({'imported':i,'results':counts})
    corpus.db.commit()
    taxonomy = json.loads((root/'ontology/official/harmonyos.json').read_text())
    for source in taxonomy['source_inputs']:
        if not source['url'].endswith('.md'):
            continue
        path = root/'.firecrawl/harmonyos-taxonomy-cache'/(hashlib.sha256(source['url'].encode()).hexdigest()+'.md')
        result = import_response(corpus,source['url'],path,source['content_sha256'],taxonomy['fetched_at'],'text/markdown')
        counts[result] = counts.get(result,0)+1
    corpus.db.commit()
    return counts


def import_probes(corpus, repo_root):
    path = Path(repo_root)/'docs-raw/source-probes/2026-09-05/manifest.json'
    counts = {}
    for source in json.loads(path.read_text())['responses']:
        if source.get('status') != 200 or source.get('method') != 'GET':
            continue
        result = import_response(corpus,source['url'],Path(repo_root)/source['local_path'],
                                 source['sha256'],source['checked_at'],source['content_type'])
        counts[result] = counts.get(result,0)+1
    corpus.db.commit()
    return counts
