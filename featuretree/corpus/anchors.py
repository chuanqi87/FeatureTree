"""Verify taxonomy binding URLs/symbols against the local official corpus."""

from __future__ import annotations
import re
import sqlite3
from pathlib import Path
from featuretree.core.storage import ROOT


def _norm_url(url: str) -> str:
    return (url or "").strip().split("#", 1)[0].rstrip("/")


def _symbol_tokens(symbol: str) -> list[str]:
    text = symbol or ""
    parts = re.split(r"[\s,;/|（）()]+", text)
    tokens = []
    for part in parts:
        part = part.strip()
        if len(part) < 3:
            continue
        if re.search(r"[\u4e00-\u9fff]", part):
            continue
        tokens.append(part)
    return tokens


class CorpusIndex:
    def __init__(self, db_path: Path):
        self.conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        self.by_url = {}
        for url, status, body_path, body_sha in self.conn.execute(
            "SELECT url, status, body_path, body_sha256 FROM documents"
        ):
            self.by_url[_norm_url(url)] = {
                "status": status,
                "body_path": body_path,
                "body_sha256": body_sha,
            }

    def lookup(self, url: str) -> dict | None:
        key = _norm_url(url)
        if key in self.by_url:
            return self.by_url[key]
        alt = key.replace("harmonyos-guides-V5", "harmonyos-guides").replace("-V5", "")
        return self.by_url.get(alt)

    def body_text(self, body_path: str | None) -> str:
        if not body_path:
            return ""
        path = Path(body_path)
        if not path.is_absolute():
            path = ROOT / path
        if not path.is_file():
            alt = ROOT / "docs-raw/official" / body_path
            path = alt if alt.is_file() else path
        try:
            return path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            return ""


def verify_feature(feature: dict, corpus: CorpusIndex) -> tuple[str, list[dict]]:
    bindings = feature.get("bindings") or {}
    details = []
    ranks = []
    rank_order = {"failed": 0, "unverified": 1, "url_ok": 2, "body_ok": 3, "symbol_ok": 4}
    for platform, entries in bindings.items():
        if not isinstance(entries, list):
            continue
        for entry in entries:
            if not isinstance(entry, dict):
                continue
            url = entry.get("url") or ""
            symbol = entry.get("id") or ""
            note = entry.get("note") or ""
            if "未查到" in note and not url:
                details.append({"platform": platform, "status": "unverified", "symbol": symbol, "reason": note})
                ranks.append("unverified")
                continue
            if not url:
                details.append({"platform": platform, "status": "failed", "symbol": symbol, "reason": "missing url"})
                ranks.append("failed")
                continue
            row = corpus.lookup(url)
            if row is None:
                details.append({"platform": platform, "status": "failed", "symbol": symbol,
                                "reason": "url not in corpus catalog", "url": url})
                ranks.append("failed")
                continue
            if row["status"] != "ready" or not row["body_path"]:
                details.append({"platform": platform, "status": "url_ok", "symbol": symbol,
                                "reason": f"catalog status={row['status']}", "url": url})
                ranks.append("url_ok")
                continue
            body = corpus.body_text(row["body_path"])
            if not body:
                details.append({"platform": platform, "status": "url_ok", "symbol": symbol,
                                "reason": "ready but body unreadable", "url": url})
                ranks.append("url_ok")
                continue
            tokens = _symbol_tokens(symbol)
            if not tokens:
                details.append({"platform": platform, "status": "body_ok", "symbol": symbol,
                                "reason": "body present; symbol too generic to match", "url": url})
                ranks.append("body_ok")
                continue
            hits = [token for token in tokens if token in body]
            if hits:
                details.append({"platform": platform, "status": "symbol_ok", "symbol": symbol,
                                "reason": f"tokens in body: {hits[:5]}", "url": url})
                ranks.append("symbol_ok")
            else:
                details.append({"platform": platform, "status": "body_ok", "symbol": symbol,
                                "reason": "body present; symbol tokens not found", "url": url})
                ranks.append("body_ok")
    if not ranks:
        return "unverified", details
    return min(ranks, key=lambda item: rank_order[item]), details
