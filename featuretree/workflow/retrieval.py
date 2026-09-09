"""Bounded, scope-directed retrieval of hash-checked official source excerpts."""

import hashlib

from featuretree.corpus.context import excerpts
from featuretree.corpus.search import search, terms
from featuretree.knowledge.source_policy import ios_applicability, official_source_error
from featuretree.workflow.queries import compact_query


def research_queries(work, platform, scope):
    node = work["subtree"][work["node_id"]]
    planned = (scope or {}).get("research_queries", {}).get(platform, [])
    fallback = [b["id"] for b in node.get("bindings", {}).get(platform, [])]
    fallback.extend([node["name"]["en"], node["name"]["zh"], *node["comparison_scope"]["includes"]])
    return list(dict.fromkeys(q.strip() for q in (planned or fallback) if q.strip()))[:4]


def query_rank(row, query):
    title = row["title"].casefold()
    query = query.casefold().lstrip("@")
    # Exact API/module names outrank incidental mentions in change logs.
    exact = query in title
    tokens = terms(query)
    matches = sum(token in title for token in tokens)
    return (exact, matches, row["retrieval_score"])


def select_sources(corpus, queries, platform, limit=6, gaps=None):
    pools, excluded = [], []
    for query in queries:
        rows = search(corpus, query, platform, limit=12)
        accepted = []
        for row in sorted(rows, key=lambda r: query_rank(r, query), reverse=True):
            reason = official_source_error(row["url"], platform, platform)
            if platform == "ios" and ios_applicability(row["metadata"]) == "explicitly_non_ios":
                reason = "Explicit non-iOS availability"
            if reason:
                excluded.append({"url": row["url"], "reason": reason})
            else:
                accepted.append((query, row))
        pools.append(accepted)
        if not accepted and gaps is not None:
            gaps.append(f"No ready local source for query: {query}; does not imply unsupported")
    chosen, seen = [], set()
    # Round-robin keeps a broad printing query from consuming the scanning budget.
    for index in range(2):
        for pool in pools:
            if index >= len(pool):
                continue
            query, row = pool[index]
            identity = row["body_sha256"] or row["url"]
            if identity in seen:
                continue
            chosen.append((query, row))
            seen.add(identity)
            if len(chosen) == limit:
                return chosen, excluded
    return chosen, excluded


def source_packet(corpus, row, query):
    path = (corpus.root / row["body_path"]).resolve()
    if not path.is_relative_to(corpus.root.resolve()) or not path.is_file():
        raise ValueError("Body absent or outside corpus")
    body = path.read_bytes()
    if hashlib.sha256(body).hexdigest() != row["body_sha256"]:
        raise ValueError("Body hash mismatch")
    text = body.decode("utf-8", errors="replace")
    fields = ("url", "title", "body_sha256", "fetched_at", "metadata")
    return {**{key: row.get(key) for key in fields}, "body_path": str(path),
            "query": query, "excerpt": row.get("excerpt", ""),
            "excerpts": excerpts(text, query, budget=2400), "total_lines": len(text.splitlines()),
            "interpretation": "Verified snapshot bytes, not a verified platform claim"}


def build_context(corpus, work, platform, scope=None):
    planned = research_queries(work, platform, scope)
    queries = list(dict.fromkeys(compact_query(query) for query in planned))
    result = {"query": " | ".join(queries), "queries": queries, "sources": [],
              "planned_queries": planned,
              "exclusions": [], "gaps": [],
              "gap": "Read relevant surrounding sections and verify public API, device and release applicability"}
    if corpus is None:
        result["gaps"].append("Local official corpus unavailable")
        return result
    selected, result["exclusions"] = select_sources(corpus, queries, platform, gaps=result["gaps"])
    for query, row in selected:
        try:
            result["sources"].append(source_packet(corpus, row, query))
        except (ValueError, OSError) as exc:
            result["gaps"].append(f"{row['url']}: {exc}")
    return result
