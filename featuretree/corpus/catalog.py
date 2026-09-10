"""Stable snapshot pagination; indexed offsets always resolve to canonical JSONL bytes."""

import base64
from contextlib import closing
import json
from pathlib import Path
import sqlite3
from typing import Protocol

from featuretree.core.content import digest, file_digest
from featuretree.core.io import ConflictError, IntegrityError, file_lock


class ApiCatalog(Protocol):
    def page(self, snapshot_id: str, selection: dict, cursor=None, limit=100, kind="declarations") -> dict: ...
    def enumerate_ids(self, snapshot_id: str, selection: dict, kind="declarations") -> list[str]: ...


class SourceReader(Protocol):
    def get(self, snapshot_id: str, kind: str, record_id: str) -> dict: ...
    def read_body(self, snapshot_id: str, document_id: str, offset=0, limit=12000) -> dict: ...


class IndexedCatalog:
    def __init__(self, snapshots, index_directory: Path, document_root: Path):
        self.snapshots = snapshots
        self.directory = index_directory
        self.document_root = document_root.resolve()

    def _index(self, snapshot_id):
        manifest = self.snapshots.get(snapshot_id)
        path = self.directory / f"{snapshot_id}.sqlite"
        self.directory.mkdir(parents=True, exist_ok=True)
        with file_lock(self.directory / f"{snapshot_id}.lock"):
            if path.exists():
                with closing(sqlite3.connect(path)) as db:
                    try:
                        marker = db.execute("SELECT fingerprint FROM metadata").fetchone()
                        if marker and marker[0] == digest(manifest):
                            return path
                    except sqlite3.DatabaseError:
                        pass
                path.unlink()
            self.snapshots.verify(snapshot_id)
            temporary = path.with_suffix(".building")
            temporary.unlink(missing_ok=True)
            with closing(sqlite3.connect(temporary)) as db:
                db.executescript("""
                    CREATE TABLE records(kind TEXT,id TEXT,platform TEXT,module TEXT,
                        search TEXT,offset INTEGER,size INTEGER,hash TEXT,PRIMARY KEY(kind,id));
                    CREATE INDEX platform_records ON records(kind,platform,id);
                    CREATE TABLE metadata(fingerprint TEXT);
                """)
                for kind in manifest["records"]:
                    with self.snapshots.path(snapshot_id, kind).open("rb") as stream:
                        while True:
                            offset = stream.tell()
                            line = stream.readline()
                            if not line:
                                break
                            row = json.loads(line)
                            module = (row.get("availability") or {}).get("module_id", "")
                            search = " ".join(str(row.get(key, "")) for key in
                                              ("qualified_name", "signature", "documentation", "title", "url", "summary"))
                            db.execute("INSERT INTO records VALUES(?,?,?,?,?,?,?,?)", (
                                kind, row["id"], row.get("platform", ""), module, search,
                                offset, len(line), digest(row)))
                db.execute("INSERT INTO metadata VALUES(?)", (digest(manifest),))
                db.commit()
            temporary.replace(path)
        return path

    def _read(self, snapshot_id, kind, index_row):
        with self.snapshots.path(snapshot_id, kind).open("rb") as stream:
            stream.seek(index_row["offset"])
            record = json.loads(stream.read(index_row["size"]))
        if record["id"] != index_row["id"] or digest(record) != index_row["hash"]:
            raise IntegrityError("Index/source record mismatch; rebuild index after auditing source")
        return record

    def page(self, snapshot_id, selection, cursor=None, limit=100, kind="declarations"):
        if kind not in ("declarations", "families", "topics", "documents"):
            raise ValueError("Invalid catalog collection")
        if not 1 <= limit <= 500:
            raise ValueError("Page size must be between 1 and 500")
        if set(selection) - {"platforms", "modules", "query", "ids"}:
            raise ValueError("Unknown source selection filter")
        scope = digest({"snapshot_id": snapshot_id, "selection": selection, "kind": kind})
        after = ""
        if cursor:
            try:
                state = json.loads(base64.urlsafe_b64decode(cursor))
            except (ValueError, TypeError):
                raise ValueError("Invalid pagination cursor") from None
            if state["scope"] != scope:
                raise ConflictError("Cursor belongs to another snapshot or selection")
            after = state["after"]
        clauses, parameters = ["kind=?", "id> ?"], [kind, after]
        for key, column in [("platforms", "platform"), ("modules", "module"), ("ids", "id")]:
            if key in selection:
                values = selection[key]
                if not isinstance(values, list) or not all(isinstance(x, str) for x in values):
                    raise ValueError("Selection filters must be string lists")
                if not values:
                    clauses.append("0")
                else:
                    clauses.append(f"{column} IN ({','.join('?' for _ in values)})")
                    parameters.extend(values)
        if selection.get("query"):
            clauses.append("instr(lower(search),lower(?))>0")
            parameters.append(selection["query"])
        with closing(sqlite3.connect(self._index(snapshot_id))) as db:
            db.row_factory = sqlite3.Row
            rows = db.execute("SELECT * FROM records WHERE " + " AND ".join(clauses) +
                              " ORDER BY id LIMIT ?", [*parameters, limit + 1]).fetchall()
        next_cursor = None
        if len(rows) > limit:
            next_cursor = base64.urlsafe_b64encode(json.dumps(
                {"scope": scope, "after": rows[limit - 1]["id"]}).encode()).decode()
        return {"snapshot_id": snapshot_id, "selection_hash": scope,
                "items": [self._read(snapshot_id, kind, row) for row in rows[:limit]],
                "next_cursor": next_cursor}

    def enumerate_ids(self, snapshot_id, selection, kind="declarations"):
        result, cursor = [], None
        while True:
            page = self.page(snapshot_id, selection, cursor, 500, kind)
            result.extend(row["id"] for row in page["items"])
            cursor = page["next_cursor"]
            if cursor is None:
                return result

    def get(self, snapshot_id, kind, record_id):
        page = self.page(snapshot_id, {"ids": [record_id]}, kind=kind)
        if not page["items"]:
            raise KeyError(f"Unknown {kind} record: {record_id}")
        return page["items"][0]

    def read_body(self, snapshot_id, document_id, offset=0, limit=12000):
        if offset < 0 or not 1 <= limit <= 24000:
            raise ValueError("Invalid document window")
        record = self.get(snapshot_id, "documents", document_id)
        path = (self.document_root / record["body_path"]).resolve()
        if not path.is_relative_to(self.document_root):
            raise IntegrityError("Document path escapes the registered corpus")
        if file_digest(path) != record["body_sha256"]:
            raise IntegrityError("Document body changed since source sealing")
        body = path.read_text()
        return {"snapshot_id": snapshot_id, "document_id": document_id, "offset": offset,
                "text": body[offset:offset + limit], "total_characters": len(body),
                "next_offset": offset + limit if offset + limit < len(body) else None,
                "body_sha256": record["body_sha256"], "url": record["url"]}
