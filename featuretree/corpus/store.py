"""Durable queue and immutable source snapshots; SQLite writes stay on one thread."""

from datetime import datetime, timezone
import gzip
import hashlib
import json
from pathlib import Path
import sqlite3
from itertools import zip_longest
from urllib.parse import urlsplit

from featuretree.corpus.urls import canonical, document_id, kind, platform


def now():
    return datetime.now(timezone.utc).isoformat()


class Corpus:
    def __init__(self, root):
        self.root = Path(root).resolve()
        self.root.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(self.root / 'corpus.sqlite', timeout=60)
        self.db.row_factory = sqlite3.Row
        self.db.execute('PRAGMA journal_mode=WAL')
        self.db.executescript('''
        CREATE TABLE IF NOT EXISTS documents (
            id TEXT PRIMARY KEY, url TEXT UNIQUE NOT NULL, platform TEXT NOT NULL,
            kind TEXT NOT NULL, title TEXT DEFAULT '', priority INTEGER DEFAULT 50,
            depth INTEGER DEFAULT 0, discovered_from TEXT DEFAULT '', status TEXT DEFAULT 'pending',
            attempts INTEGER DEFAULT 0, error TEXT DEFAULT '', http_status INTEGER,
            snapshot TEXT, body_path TEXT, raw_path TEXT, raw_sha256 TEXT, body_sha256 TEXT,
            fetched_at TEXT, metadata TEXT DEFAULT '{}', bytes INTEGER DEFAULT 0);
        CREATE INDEX IF NOT EXISTS queue ON documents(status, priority, platform);
        CREATE TABLE IF NOT EXISTS snapshots (
            id TEXT NOT NULL, sha256 TEXT NOT NULL, fetched_at TEXT NOT NULL,
            fetch_url TEXT, raw_path TEXT, body_path TEXT, body_sha256 TEXT,
            PRIMARY KEY(id,sha256));
        CREATE VIRTUAL TABLE IF NOT EXISTS search_words USING fts5(id UNINDEXED, title, body, tokenize='unicode61');
        CREATE VIRTUAL TABLE IF NOT EXISTS search_chars USING fts5(id UNINDEXED, title, body, tokenize='trigram');
        CREATE VIRTUAL TABLE IF NOT EXISTS catalog_search USING fts5(title,url,tokenize='unicode61');
        CREATE TRIGGER IF NOT EXISTS catalog_insert AFTER INSERT ON documents BEGIN
            INSERT INTO catalog_search(rowid,title,url) VALUES(new.rowid,new.title,new.url);
        END;
        CREATE TRIGGER IF NOT EXISTS catalog_update AFTER UPDATE OF title ON documents BEGIN
            DELETE FROM catalog_search WHERE rowid=old.rowid;
            INSERT INTO catalog_search(rowid,title,url) VALUES(new.rowid,new.title,new.url);
        END;
        ''')
        if not self.db.execute('SELECT 1 FROM catalog_search LIMIT 1').fetchone():
            self.db.execute('INSERT OR IGNORE INTO catalog_search(rowid,title,url) SELECT rowid,title,url FROM documents')
            self.db.commit()

    def close(self):
        self.db.commit()
        self.db.close()

    def add(self, url, title='', priority=50, depth=0, source=''):
        url = canonical(url)
        if not url:
            return False
        self.db.execute('''INSERT INTO documents(id,url,platform,kind,title,priority,depth,discovered_from)
            VALUES(?,?,?,?,?,?,?,?) ON CONFLICT(url) DO UPDATE SET
            priority=MIN(priority,excluded.priority),depth=MIN(depth,excluded.depth)''',
            (document_id(url), url, platform(url), kind(url), title, priority, depth, source))
        return True

    def pending(self, platforms, limit, max_priority=100, retry=False):
        statuses = "('pending','failed')" if retry else "('pending')"
        queues=[]
        for target in platforms:
            queues.append([dict(r) for r in self.db.execute(f'''SELECT * FROM documents WHERE platform=?
                AND status IN {statuses} AND attempts < 4 AND priority <= ?
                ORDER BY priority,attempts,url LIMIT ?''',(target,max_priority,limit))])
        return [r for batch in zip_longest(*queues) for r in batch if r is not None][:limit]

    def save(self, row, raw, content, fetch_url, fetched_at=None, *, count_attempt=True):
        digest = hashlib.sha256(raw).hexdigest()
        relative = Path('snapshots') / row['platform'] / row['id'][:2] / row['id'] / digest
        folder = self.root / relative
        folder.mkdir(parents=True, exist_ok=True)
        body = content.body.encode()
        body_hash = hashlib.sha256(body).hexdigest()
        raw_path, body_path = relative / 'source.gz', relative / f'document-{body_hash}.md'
        if not (self.root / raw_path).exists():
            (self.root / raw_path).write_bytes(gzip.compress(raw, mtime=0))
        (self.root / body_path).write_bytes(body)
        timestamp = fetched_at or now()
        metadata = {**content.metadata, 'retrieved_url': fetch_url, 'version_verified': False,
                    'scope': 'Apple multiplatform; verify iOS applicability' if urlsplit(row['url']).hostname=='developer.apple.com' else row['platform']}
        (folder/f'metadata-{body_hash}.json').write_text(json.dumps({'url':row['url'], 'fetched_at':timestamp,
            'raw_sha256':digest,'body_sha256':body_hash,**metadata},ensure_ascii=False,indent=2)+'\n')
        self.db.execute('''UPDATE documents SET status=?,title=?,snapshot=?,raw_path=?,body_path=?,
            raw_sha256=?,body_sha256=?,fetched_at=?,metadata=?,bytes=?,error='',http_status=200,
            attempts=attempts+? WHERE id=?''', (content.quality,content.title,digest,str(raw_path),str(body_path),
            digest,body_hash,timestamp,json.dumps(metadata,ensure_ascii=False),len(raw),int(count_attempt),row['id']))
        self.db.execute('INSERT OR IGNORE INTO snapshots VALUES(?,?,?,?,?,?,?)',
            (row['id'],digest,timestamp,fetch_url,str(raw_path),str(body_path),body_hash))
        search_rowid = self.db.execute('SELECT rowid FROM documents WHERE id=?',(row['id'],)).fetchone()[0]
        for table in ('search_words','search_chars'):
            self.db.execute(f'DELETE FROM {table} WHERE rowid=?',(search_rowid,))
            if content.quality=='ready':
                self.db.execute(f'INSERT INTO {table}(rowid,id,title,body) VALUES(?,?,?,?)',
                    (search_rowid,row['id'],content.title,content.body))

    def fail(self, row, message, status=None):
        # Another worker may have saved a body after this request was queued.
        self.db.execute('''UPDATE documents SET status=CASE WHEN snapshot IS NOT NULL THEN status ELSE ? END,
            error=?,http_status=CASE WHEN snapshot IS NOT NULL THEN http_status ELSE ? END,
            attempts=attempts+1 WHERE id=?''',
            ('not_found' if status in (404,410) else 'blocked' if status in (401,403) else 'failed',message,status,row['id']))

    def get(self, url):
        # Previously captured sources remain readable if discovery rules become narrower.
        row = self.db.execute('SELECT * FROM documents WHERE url=?',(url,)).fetchone()
        if row is None:
            row = self.db.execute('SELECT * FROM documents WHERE url=?',(canonical(url),)).fetchone()
        return dict(row) if row else None

    def stats(self):
        return [dict(r) for r in self.db.execute('''SELECT platform,status,count(*) AS count,
            sum(bytes) AS raw_bytes FROM documents GROUP BY platform,status ORDER BY platform,status''')]

    def body(self, row):
        path = (self.root / row['body_path']).resolve()
        if not path.is_relative_to(self.root):
            raise ValueError('Document path escapes corpus')
        body = path.read_bytes()
        if hashlib.sha256(body).hexdigest() != row['body_sha256']:
            raise ValueError(f"Document hash mismatch: {row['url']}")
        return body.decode()
