"""One-time historical import; no reference-project path is a runtime dependency."""

import json
from contextlib import closing
from pathlib import Path
import shutil
import sqlite3

from featuretree.core.content import digest, file_digest
from featuretree.core.io import IntegrityError, read_json
from featuretree.corpus.identity import normalize_legacy

TARGETS = {
    "android-l1.jsonl": "java", "android-native-l1.jsonl": "c",
    "harmonyos-l1.jsonl": "arkts", "harmonyos-native-l1.jsonl": "c",
    "ios-darwin-l1.jsonl": "c", "ios-objc-l1.jsonl": "objc", "ios-swift-l1.jsonl": "swift",
}


def json_lines(path):
    with path.open() as stream:
        for line in stream:
            if line.strip():
                yield json.loads(line)


def preserve_input(path, directory):
    fingerprint = file_digest(path)
    target = directory / fingerprint / path.name
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists():
        shutil.copy2(path, target)
    if file_digest(target) != fingerprint:
        raise IntegrityError("Imported historical bytes failed verification")
    return target, {"path": str(target), "sha256": fingerprint, "bytes": target.stat().st_size,
                    "status": "extracted", "reason": "Historical import; release and public applicability unverified"}


def import_reference(reference, snapshots, import_directory, document_root):
    """Preserve original bytes/IDs, and explicitly account for duplicate declarations."""
    inputs, files, mapping, families, conflicts = [], [], {}, [], []
    for filename, language in TARGETS.items():
        source = reference / "apidata" / filename
        if not source.exists():
            raise FileNotFoundError(f"Required historical input missing: {source}")
        path, record = preserve_input(source, import_directory)
        inputs.append((path, record["sha256"], language))
        files.append(record)
    topic_inputs = []
    for platform in ("android", "apple", "harmonyos"):
        path, record = preserve_input(reference / "ontology/official/evidence" / f"{platform}.jsonl", import_directory)
        topic_inputs.append(path)
        files.append(record)
        _, catalog_file = preserve_input(reference / "ontology/official" / f"{platform}.json", import_directory)
        files.append(catalog_file)

    def declarations():
        seen = {}
        for path, fingerprint, language in inputs:
            for original in json_lines(path):
                row = normalize_legacy(original, fingerprint, language)
                mapping[original["id"]] = row["id"]
                if row["id"] in seen:
                    conflicts.append({"id": row["id"], "original_id": original["id"],
                                      "first_original_id": seen[row["id"]],
                                      "reason": "Same canonical identity; original bytes retained for alias/content audit"})
                    continue
                seen[row["id"]] = original["id"]
                families.append({"id": "family_" + digest(row["id"]), "declaration_ids": [row["id"]],
                                 "basis": "Conservative one-declaration family; no unverified alias collapse",
                                 "evidence_refs": [], "unresolved_aliases": []})
                yield row

    def topics():
        for path in topic_inputs:
            for original in json_lines(path):
                association = original.get("evidence", {}).get("api_association", {})
                description = original.get("description") or {}
                yield {"id": "topic_" + digest(original["official_node_id"]),
                       "platform": "ios" if original["platform"] == "apple" else original["platform"],
                       "original_id": original["official_node_id"],
                       "path": [item["name"] for item in original.get("official_path", [])],
                       "title": original["name"], "url": description.get("source_url", ""),
                       "summary": description.get("text", ""),
                       "summary_strength": "title_only" if original.get("quality", {}).get("description_strength") == "title-only" else "summary",
                       "declaration_ids": sorted({mapping[value] for value in association.get("materialized_api_ids", []) if value in mapping}),
                       "evidence_refs": []}

    provenance = {"kind": "legacy_reference_import", "original_inputs": files,
                  "identity_collisions": conflicts,
                  "constraints": ["Historical SDKs, including HarmonyOS Beta; not a formal baseline",
                                  "API associations are official-topic containment hints, not capability bindings",
                                  "Publicness, aliases, SDK file completeness and iOS applicability need audit"]}
    return snapshots.seal({"declarations": declarations(), "families": iter(families),
                           "topics": topics(), "documents": official_documents(document_root)},
                          files=files, status="historical", extractor_versions={"legacy-normalizer": "1"},
                          provenance=provenance)


def official_documents(document_root):
    """Read the existing corpus with a read-only SQLite connection, verifying every body."""
    database = document_root / "corpus.sqlite"
    if not database.exists():
        return
    with closing(sqlite3.connect(database.as_uri() + "?mode=ro", uri=True)) as db:
        db.row_factory = sqlite3.Row
        for item in db.execute("SELECT * FROM documents ORDER BY id"):
            row = dict(item)
            body = row.get("body_path")
            status = "unprocessed"
            reason = row.get("error") or "No captured body"
            actual_hash = None
            if body:
                path = (document_root / body).resolve()
                if not path.is_relative_to(document_root.resolve()):
                    raise IntegrityError("Corpus body path escapes the official source root")
                if path.exists():
                    actual_hash = file_digest(path)
                    status = "verified" if actual_hash == row["body_sha256"] else "failed"
                    reason = "Body hash checked; platform release remains unverified" if status == "verified" else "Body hash mismatch"
                else:
                    status, reason = "failed", "Captured body file missing"
            yield {"id": row["id"], "platform": row["platform"], "title": row["title"],
                   "url": row["url"], "body_path": body, "body_sha256": row.get("body_sha256"),
                   "actual_sha256": actual_hash, "raw_path": row.get("raw_path"),
                   "raw_sha256": row.get("raw_sha256"), "fetched_at": row.get("fetched_at"),
                   "status": status, "reason": reason, "metadata": json.loads(row.get("metadata") or "{}")}
