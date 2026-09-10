"""Tree-stage responsibilities and deterministic derivation of candidate artifacts."""

from featuretree.core.content import digest
from featuretree.core.io import read_json, write_json
from featuretree.taxonomy.coverage import disposition_report, size_report, validate_bindings
from featuretree.taxonomy.model import assign_identities, validate_tree
from featuretree.workflow.packaging import envelope


def candidate_tree(packet):
    payload = packet["upstream"]["ft-design"]
    existing = {row["id"]: row for row in packet["inputs"].get("tree_ref", {}).get("features", [])}
    changes = payload["changes"]
    for change in changes:
        if change["operation"] in ("split", "merge"):
            for key in change["subject_ids"]:
                existing.pop(key, None)
    existing.update({row["id"]: row for row in payload["features"]})
    return {"schema_version": 3, "features": list(existing.values()),
            "lineage": [{"operation": row["operation"], "old_ids": row["subject_ids"],
                         "new_ids": row["candidate_ids"], "reason": row["reason"]}
                        for row in changes if row["operation"] in ("split", "merge")]}


class TreeHandlers:
    def __init__(self, artifacts, catalog):
        self.artifacts, self.catalog = artifacts, catalog

    def input_records(self, packet, platform=None, kind="declarations"):
        key = "api_ids" if kind == "declarations" else "topic_ids"
        ids = packet["work"][key]
        selection = {"ids": ids}
        if platform:
            selection["platforms"] = [platform]
        records, cursor = {}, None
        while True:
            page = self.catalog.page(packet["work"]["snapshot_id"], selection, cursor, 500, kind)
            records.update({row["id"]: row for row in page["items"]})
            cursor = page["next_cursor"]
            if cursor is None:
                return records

    def references(self, references, packet, platform=None):
        for reference in references:
            record = self.catalog.get(packet["work"]["snapshot_id"], "documents", reference)
            if record["status"] != "verified":
                raise ValueError("Evidence reference has no verified captured body")
            if platform and record["platform"] != platform:
                raise ValueError("Platform facts cite another platform's source")

    def validate(self, stage, response, packet):
        payload = response["payload"]
        if stage in ("ft-android", "ft-ios", "ft-harmonyos"):
            platform = payload["platform"]
            apis = self.input_records(packet, platform)
            topics = self.input_records(packet, platform, "topics")
            disposition_report(apis, payload["api_dispositions"])
            disposition_report(topics, payload["topic_dispositions"])
            seen = set()
            for fact in payload["facts"]:
                if fact["id"] in seen or not set(fact["api_ids"]) <= set(apis):
                    raise ValueError("Duplicate fact or API outside platform input scope")
                seen.add(fact["id"])
                if not fact["evidence_refs"] and not fact["gaps"]:
                    raise ValueError("Platform fact needs evidence or explicit gap")
                self.references(fact["evidence_refs"], packet, platform)
        elif stage == "ft-align":
            facts = {fact["id"] for key, result in packet["upstream"].items()
                     if key in ("ft-android", "ft-ios", "ft-harmonyos") for fact in result["facts"]}
            matched = {key for relation in payload["relationships"] for key in relation["fact_ids"]}
            unmatched = set(payload["unmatched_fact_ids"])
            if matched & unmatched or matched | unmatched != facts:
                raise ValueError("Alignment must account for every platform fact without losing unmatched items")
        elif stage == "ft-design":
            if payload["work_type"] != packet["work"]["work_type"]:
                raise ValueError("Design agent changed its assigned work type")
            validate_tree(candidate_tree({**packet, "upstream": {**packet["upstream"], stage: payload}}))
        elif stage == "ft-bind":
            nodes = validate_tree(candidate_tree(packet))
            apis = self.input_records(packet)
            validate_bindings(nodes, apis, payload["bindings"], payload["api_dispositions"])
            disposition_report(packet["work"]["topic_ids"], payload["topic_dispositions"])
            for binding in payload["bindings"]:
                self.references(binding["evidence_refs"], packet, apis[binding["declaration_id"]]["platform"])
        elif stage == "ft-granularity":
            report = packet["upstream"]["ft-check"]
            leaves = set(report["leaf_ids"])
            decisions = payload["decisions"]
            if {row["feature_id"] for row in decisions} != leaves or len(decisions) != len(leaves):
                raise ValueError("Every leaf requires exactly one granularity judgment")
            for row in decisions:
                if row["verdict"] == "appropriate" and report["counts"].get(row["feature_id"], {}).get("counts_are_lower_bounds", True):
                    raise ValueError("Incomplete API enumeration cannot prove appropriate granularity")

    def check(self, packet, folder):
        tree = candidate_tree(packet)
        nodes = validate_tree(tree)
        bound = packet["upstream"]["ft-bind"]
        apis = self.input_records(packet)
        api_report = validate_bindings(nodes, apis, bound["bindings"], bound["api_dispositions"])
        topic_report = disposition_report(packet["work"]["topic_ids"], bound["topic_dispositions"])
        families = [{"id": "family_" + digest(key), "declaration_ids": [key]} for key in apis]
        # Conservative singleton families until a reviewed alias record is supplied.
        counts = size_report(apis, families, bound["bindings"], enumeration_complete=api_report["complete"])
        mapping_path = folder.parents[2] / f"{packet['work_id']}-identities.json"
        mapping = read_json(mapping_path) if mapping_path.exists() else {}
        existing = [row["id"] for row in packet["inputs"].get("tree_ref", {}).get("features", [])]
        features, mapping = assign_identities(tree["features"], mapping, existing)
        write_json(mapping_path, mapping)
        resolved_tree = {**tree, "features": features,
                         "lineage": [{**row, "new_ids": [mapping.get(key, key) for key in row["new_ids"]]}
                                     for row in tree["lineage"]]}
        tree_ref = self.artifacts.put(resolved_tree)
        bindings = {"schema_version": 3, "snapshot_id": packet["work"]["snapshot_id"], "tree_ref": tree_ref,
                    "bindings": [{**row, "feature_id": mapping.get(row["feature_id"], row["feature_id"])} for row in bound["bindings"]],
                    "declarations": bound["api_dispositions"], "topics": bound["topic_dispositions"]}
        leaves = [key for key, node in nodes.items() if node["node_type"] == "leaf"]
        missing_public = [key for key in leaves if not any(
            row["feature_id"] == key and row["role"] == "core" and apis[row["declaration_id"]]["visibility"] == "public"
            for row in bound["bindings"])]
        return envelope(packet, {"tree_ref": tree_ref, "bindings_ref": self.artifacts.put(bindings),
                                 "identity_mapping": mapping, "leaf_ids": leaves, "counts": counts,
                                 "api_coverage": api_report, "topic_coverage": topic_report,
                                 "missing_public_realization": missing_public,
                                 "scope_only": True},
                        "pass" if api_report["complete"] and topic_report["complete"] and not missing_public else "completed_with_gaps")
