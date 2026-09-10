"""Preserve other domains across a source supplement only with unchanged dependencies."""

from featuretree.core.content import digest


def validate_preserved_sources(previous, snapshot_id, revised_feature_ids, revised_topic_ids, catalog):
    old = previous["snapshot_id"]
    retained = [row for row in previous["bindings"] if row["feature_id"] not in revised_feature_ids]
    ids = {"declarations": sorted({row["declaration_id"] for row in retained}),
           "documents": sorted({reference for row in retained for reference in row["evidence_refs"]}),
           "topics": sorted({row["id"] for row in previous["topics"]} - set(revised_topic_ids))}
    ids["documents"] = sorted(set(ids["documents"]) | {reference for route in previous.get("routes", [])
        if route["feature_id"] not in revised_feature_ids for reference in route["evidence_refs"]})
    for kind, references in ids.items():
        for reference in references:
            try:
                before, after = catalog.get(old, kind, reference), catalog.get(snapshot_id, kind, reference)
            except KeyError as error:
                raise ValueError("Source supplement removed a preserved domain dependency; replan that domain") from error
            if digest(before) != digest(after):
                raise ValueError(f"Source supplement changed preserved {kind} {reference}; include its domain in explicit revision work")
            if kind == "documents":
                catalog.read_body(snapshot_id, reference, 0, 1)
    return {"previous_snapshot_id": old, "snapshot_id": snapshot_id, "verified_unchanged_ids": ids}
