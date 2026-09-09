"""Safe authoring initialization and deterministic generated views."""

import csv
import io

from .bindings import build_index
from .comparison import comparison_slots, finding_key, new_knowledge, progress, subject_hash
from .confidence import claim_rows, quality_fields, quality_summary
from .knowledge_validation import require_valid_knowledge
from .paths import EXPORTS_DIR
from .storage import contained_path, write_json, write_text, write_yaml


def create_missing_knowledge(repo):
    features = repo.features()
    platforms = repo.config()["platforms"]
    created = []
    for feature in features.values():
        path = contained_path(repo.root, feature["knowledge_path"], "knowledge")
        if path.exists():
            continue
        doc = new_knowledge(feature, platforms)
        if doc["role"] == "rollup":
            doc["child_index"] = [f["id"] for f in features.values() if f["parent"] == feature["id"]]
        write_yaml(path, doc)
        created.append(feature["id"])
    return created


def csv_text(rows, fields):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue()


def matrix_rows(features, knowledge, platforms):
    support_rows, comparison_rows = [], []
    for fid, feature in sorted(features.items()):
        doc = knowledge[fid]
        summary = progress(feature, doc, platforms)
        for platform in platforms:
            cell = doc["presence"][platform]
            support_rows.append({"feature_id": fid, "parent": feature["parent"] or "",
                                 "level": feature["level"], "name_zh": feature["name"]["zh"],
                                 "role": feature["knowledge_role"], "platform": platform,
                                 "support": cell["status"], "verification": cell["verification"],
                                 "article_status": doc["status"], **summary, **quality_fields(cell)})
        findings = {finding_key(f): f for f in doc["comparisons"]}
        for dimension, pair in comparison_slots(feature, platforms):
            finding = findings.get((dimension, pair), {})
            comparison_rows.append({"feature_id": fid, "name_zh": feature["name"]["zh"],
                                    "dimension": dimension, "platform_a": pair[0], "platform_b": pair[1],
                                    "result": finding.get("result", "unknown"),
                                    "verification": finding.get("verification", "unreviewed"),
                                    "scope": finding.get("scope", ""),
                                    "rationale": finding.get("rationale", ""), **quality_fields(finding)})
    return support_rows, comparison_rows


def tree_view(features, knowledge, platforms):
    # Flat adjacency view is safe to generate even before cycle validation.
    nodes = []
    for fid, feature in sorted(features.items()):
        rows = claim_rows(feature, knowledge[fid], platforms)
        nodes.append({**feature, "subject_hash": subject_hash(feature), "platforms": knowledge[fid]["presence"],
                      "comparison_progress": progress(feature, knowledge[fid], platforms),
                      "quality_summary": quality_summary(rows), "quality_claims": rows,
                      "children": [child for child, cf in features.items() if cf["parent"] == fid]})
    return nodes


def export_views(repo):
    features = repo.features()
    knowledge, paths = repo.knowledge()
    config = repo.config()
    require_valid_knowledge(repo, features, knowledge, paths, config)
    platforms = config["platforms"]
    support, comparisons = matrix_rows(features, knowledge, platforms)
    output = repo.root / EXPORTS_DIR
    write_json(output / "index.json", build_index(features))
    write_json(output / "tree.json", tree_view(features, knowledge, platforms))
    write_text(output / "presence_matrix.csv", csv_text(support, list(support[0])))
    write_text(output / "comparison_matrix.csv", csv_text(comparisons, list(comparisons[0])))
    from .review_scope import build_scope
    write_json(output / "review_queue.json", build_scope(features, knowledge, platforms))
