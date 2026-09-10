"""Bounded source requests create a new snapshot; sealed snapshots are never amended."""

from contextlib import closing
from featuretree.core.content import digest, file_digest
from featuretree.core.io import file_lock
from featuretree.corpus.download import Fetcher
from featuretree.corpus.importers import json_lines, official_documents
from featuretree.corpus.source_policy import official_source_error
from featuretree.corpus.store import Corpus
from featuretree.corpus.urls import canonical


def capture_sources(snapshot_store, document_root, source_requests, parent_id=None, fetcher=None):
    fetcher = fetcher or Fetcher()
    gaps, captured = [], []
    with file_lock(document_root / "capture-v2.lock"):
        corpus = Corpus(document_root)
        try:
            for request in source_requests:
                for url in request["source_urls"]:
                    error = official_source_error(url, request["platform"], request.get("distribution", "HarmonyOS"))
                    normalized = canonical(url)
                    if error or not normalized:
                        raise ValueError(error or "URL is outside the official documentation registry")
                    corpus.add(normalized)
                    row = corpus.get(normalized)
                    result = fetcher.fetch(row)
                    if "error" in result:
                        corpus.fail(row, result["error"], result["http_status"])
                        gaps.append({"id": "capture_" + digest(normalized), "kind": "source", "severity": "gap",
                                     "target_stage": "sources", "subject_ids": [row["id"]],
                                     "reason": result["error"], "evidence_refs": []})
                    else:
                        corpus.save(row, **result)
                        captured.append(row["id"])
                if not request["source_urls"]:
                    gaps.append({"id": "search_" + digest(request), "kind": "source", "severity": "gap",
                                 "target_stage": "sources", "subject_ids": request["subject_ids"],
                                 "reason": "Request needs an official URL; discovery is not evidence of support",
                                 "evidence_refs": []})
        finally:
            corpus.close()
    collections = {"documents": official_documents(document_root)}
    parent = snapshot_store.get(parent_id) if parent_id else None
    if parent:
        for kind in ("declarations", "families", "topics"):
            collections[kind] = json_lines(snapshot_store.path(parent_id, kind))
    unresolved = [gap for gap in (parent["gaps"] if parent else [])
                  if not gap["id"].startswith("capture_") or not set(gap["subject_ids"]) <= set(captured)]
    return snapshot_store.seal(collections, files=parent["files"] if parent else [],
                                baseline_ref=parent["baseline_ref"] if parent else None,
                                status="candidate", gaps=[*unresolved, *gaps],
                                extractor_versions={**(parent["extractor_versions"] if parent else {}), "capture": "1"},
                                provenance={"parent_snapshot_id": parent_id, "requests": source_requests, "captured_document_ids": captured})
