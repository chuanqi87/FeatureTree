"""Read-only corpus retrieval and hash-checked anchor detection."""

from contextlib import contextmanager
import hashlib
import re
import sqlite3
from types import SimpleNamespace

from featuretree.corpus.search import search
from featuretree.corpus.urls import canonical


@contextmanager
def corpus_reader(root):
    folder = root / "docs-raw/official"
    database = folder / "corpus.sqlite"
    if not database.is_file():
        yield None
        return
    connection = sqlite3.connect(database.as_uri() + "?mode=ro", uri=True, timeout=10)
    connection.row_factory = sqlite3.Row
    try:
        yield SimpleNamespace(db=connection, root=folder)
    finally:
        connection.close()


def source_context(root, work, platform):
    node = work["subtree"][work["node_id"]]
    query = node["name"]["en"] + " " + " ".join(node["comparison_scope"]["includes"])
    with corpus_reader(root) as corpus:
        if corpus is None:
            return {"query": query, "sources": [], "gap": "Local official corpus unavailable"}
        rows = search(corpus, query, platform, limit=4)
        fields = ("url", "title", "body_path", "body_sha256", "fetched_at", "excerpt", "metadata")
        return {"query": query, "sources": [{k: r.get(k) for k in fields} for r in rows],
                "gap": "Retrieval candidates only; read the actual official body and check applicability"}


def detect_binding(root, corpus, platform, binding):
    url, symbol = binding.get("url", ""), binding["id"]
    detail = {"platform": platform, "url": url, "symbol": symbol, "status": "failed"}
    key = canonical(url)
    if not key or corpus is None:
        return {**detail, "reason": "Official URL or local corpus unavailable"}
    row = corpus.db.execute("SELECT * FROM documents WHERE url=?", (key,)).fetchone()
    if row is None:
        return {**detail, "reason": "URL not found in corpus; does not imply unsupported"}
    if not row["body_path"] or row["status"] != "ready":
        return {**detail, "status": "url_ok", "reason": "Catalog entry only; no ready body"}
    path = (corpus.root / row["body_path"]).resolve()
    if not path.is_relative_to(corpus.root.resolve()) or not path.is_file():
        return {**detail, "reason": "Body absent or outside corpus"}
    body = path.read_bytes()
    if hashlib.sha256(body).hexdigest() != row["body_sha256"]:
        return {**detail, "reason": "Body hash mismatch"}
    found = re.search(r"(?<!\w)" + re.escape(symbol) + r"(?!\w)", body.decode("utf-8", errors="replace")) is not None
    return {**detail, "status": "symbol_ok" if found else "body_ok", "body_path": str(path),
            "body_sha256": row["body_sha256"], "fetched_at": row["fetched_at"],
            "reason": "Exact symbol text detected; public API and version still require review"
                      if found else "Body verified but exact symbol not found"}


def detect_anchors(root, nodes):
    results = []
    ranks = {"failed": 0, "url_ok": 1, "body_ok": 2, "symbol_ok": 3}
    with corpus_reader(root) as corpus:
        for node in nodes:
            details = [detect_binding(root, corpus, p, b) for p, entries in node["bindings"].items()
                       for b in entries]
            status = min((d["status"] for d in details), key=ranks.get) if details else "failed"
            results.append({"id": node["id"], "anchor_status": status, "bindings": details})
    return {"results": results, "interpretation": "Machine anchor detection only, not platform support"}
