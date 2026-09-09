"""Pure tree and comparison projections shared by exports and the console."""

import csv
import io
from featuretree.knowledge.comparison import comparison_slots, finding_key, progress, subject_hash
from featuretree.knowledge.confidence import claim_rows, quality_fields, quality_summary


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
