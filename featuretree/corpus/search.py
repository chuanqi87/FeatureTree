"""Lexical retrieval over official full text, returning traceable candidates only."""

import json
import re


STOPWORDS = {'and','or','the','with','for','from','of','to','in','on','a','an','by'}


def terms(query):
    return [term for term in re.findall(r'[A-Za-z0-9_]+|[\u4e00-\u9fff]+',query)
            if len(term)>1 and term.lower() not in STOPWORDS][:24]


def search(corpus, query, platform, limit=8):
    if platform not in ('android','ios','harmonyos') or not 1<=limit<=100:
        raise ValueError('Invalid platform or result limit')
    tokens = terms(query)
    if not tokens:
        return []
    results = {}
    for table in ('search_words','search_chars'):
        selected = tokens if table=='search_words' else [t for t in tokens if len(t)>=3]
        if not selected:
            continue
        expression = ' OR '.join('"'+t.replace('"','""')+'"' for t in selected)
        rows = corpus.db.execute(f'''SELECT d.*,bm25({table},0.0,6.0,1.0) AS rank,
            snippet({table},2,'','', ' … ',40) AS excerpt FROM {table}
            JOIN documents d ON d.rowid={table}.rowid WHERE {table} MATCH ?
            AND d.platform=? AND d.status='ready' ORDER BY rank LIMIT ?''',(expression,platform,limit*3))
        for index,row in enumerate(rows):
            candidate = dict(row)
            # Reciprocal rank avoids comparing incomparable tokenizer BM25 scales.
            weight = 1/(1+index)
            if row['url'] not in results:
                candidate['retrieval_score'] = weight
                results[row['url']] = candidate
            else:
                results[row['url']]['retrieval_score'] += weight
    ranked = sorted(results.values(),key=lambda r:(-r['retrieval_score'],r['url']))[:limit]
    for row in ranked:
        row['metadata'] = json.loads(row['metadata'])
        row['body_path'] = str(corpus.root/row['body_path'])
        row['raw_path'] = str(corpus.root/row['raw_path'])
        row['evidence_status'] = 'retrieval_candidate_not_verified_claim'
    return ranked


def locate(corpus, query, platform, limit=12):
    """Find official URLs even when their full bodies have not been downloaded."""
    if platform not in ('android','ios','harmonyos') or not 1<=limit<=100:
        raise ValueError('Invalid platform or result limit')
    selected=terms(query)
    if not selected:
        return []
    expression=' OR '.join('"'+term+'"' for term in selected)
    rows=corpus.db.execute('''SELECT d.url,d.title,d.kind,d.status,d.error,d.discovered_from,
        bm25(catalog_search,5.0,1.0) AS rank FROM catalog_search
        JOIN documents d ON d.rowid=catalog_search.rowid
        WHERE catalog_search MATCH ? AND d.platform=? ORDER BY rank LIMIT ?''',(expression,platform,limit))
    return [dict(row) for row in rows]
