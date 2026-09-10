"""Tree-stage responsibilities and deterministic derivation of candidate artifacts."""

from featuretree.core.content import digest
from featuretree.core.io import read_json, write_json
from featuretree.taxonomy.coverage import disposition_report, size_report, validate_bindings
from featuretree.taxonomy.model import assign_identities, validate_tree
from featuretree.taxonomy.revisions import apply_proposal, merge_binding_scope
from featuretree.taxonomy.routes import validate_routes
from featuretree.taxonomy.source_migration import validate_preserved_sources
from featuretree.workflow.packaging import envelope


def candidate_tree(packet):
    return candidate_scope(packet)[0]


def candidate_scope(packet):
    base = packet["inputs"].get("tree_ref", {"schema_version": 3, "features": [], "lineage": []})
    return apply_proposal(base, packet["upstream"]["ft-design"], packet["work"].get("scope_root_ids", []))


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
                expected = set(packet["work"].get("source_groups", {}).get(kind, {}).get(platform, ids) if platform else ids)
                if set(records) != expected:
                    raise ValueError("Query index omitted canonical input IDs; source index must be rebuilt")
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
            if platform != packet["source_access"]["platform"]:
                raise ValueError("Platform researcher changed its assigned platform")
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
            all_facts = [fact["id"] for key, result in packet["upstream"].items()
                         if key in ("ft-android", "ft-ios", "ft-harmonyos") for fact in result["facts"]]
            facts = set(all_facts)
            if len(facts) != len(all_facts):
                raise ValueError("Platform fact identities collide; repair their provenance before alignment")
            matched = {key for relation in payload["relationships"] for key in relation["fact_ids"]}
            unmatched = set(payload["unmatched_fact_ids"])
            if matched & unmatched or matched | unmatched != facts:
                raise ValueError("Alignment must account for every platform fact without losing unmatched items")
        elif stage == "ft-design":
            if payload["work_type"] != packet["work"]["work_type"]:
                raise ValueError("Design agent changed its assigned work type")
            validate_tree(candidate_tree({**packet, "upstream": {**packet["upstream"], stage: payload}}))
        elif stage == "ft-bind":
            tree, scope = candidate_scope(packet)
            nodes = {key: row for key, row in validate_tree(tree).items() if key in scope}
            apis = self.input_records(packet)
            validate_bindings(nodes, apis, payload["bindings"], payload["api_dispositions"])
            validate_routes(nodes, apis, payload["bindings"], payload["routes"])
            disposition_report(packet["work"]["topic_ids"], payload["topic_dispositions"])
            for binding in payload["bindings"]:
                self.references(binding["evidence_refs"], packet, apis[binding["declaration_id"]]["platform"])
            for route in payload["routes"]:
                self.references(route["evidence_refs"], packet, route["platform"])
        elif stage == "ft-granularity":
            report = packet["upstream"]["ft-check"]
            leaves = set(report["leaf_ids"])
            decisions = payload["decisions"]
            if {row["feature_id"] for row in decisions} != leaves or len(decisions) != len(leaves):
                raise ValueError("Every leaf requires exactly one granularity judgment")
            for row in decisions:
                if row["verdict"] == "appropriate" and report["counts"].get(row["feature_id"], {}).get("counts_are_lower_bounds", True):
                    raise ValueError("Incomplete API enumeration cannot prove appropriate granularity")
        elif stage in ("ft-review", "ft-integrate"):
            report = packet["upstream"]["ft-check"]
            subjects = {row["subject_id"] for row in payload["reviews"]}
            if not set(report["leaf_ids"]) <= subjects:
                raise ValueError("Independent review must cover every candidate leaf")
            if response["outcome"] == "pass" and any(row["verdict"] != "pass" for row in payload["reviews"]):
                raise ValueError("Review verdicts disagree with the passing outcome")
        elif stage == "ft-coverage":
            report = packet["upstream"]["ft-check"]
            expected = set(report["api_coverage"]["unresolved_ids"]) | set(report["topic_coverage"]["unresolved_ids"])
            if not expected <= set(payload["unresolved_ids"]):
                raise ValueError("Coverage reviewer dropped unresolved inputs")

    def check(self, packet, folder):
        tree, scope = candidate_scope(packet)
        nodes = {key: row for key, row in validate_tree(tree).items() if key in scope}
        bound = packet["upstream"]["ft-bind"]
        apis = self.input_records(packet)
        api_report = validate_bindings(nodes, apis, bound["bindings"], bound["api_dispositions"])
        validate_routes(nodes, apis, bound["bindings"], bound["routes"])
        topic_report = disposition_report(packet["work"]["topic_ids"], bound["topic_dispositions"])
        families = [row for row in self.catalog.enumerate_records(packet["work"]["snapshot_id"], {}, "families")
                    if set(row["declaration_ids"]) & set(apis)]
        counts = size_report(apis, families, bound["bindings"], enumeration_complete=
                             api_report["complete"] and packet["work"].get("enumeration_complete", False), routes=bound["routes"])
        mapping_path = folder.parents[2] / f"{packet['work_id']}-identities.json"
        mapping = read_json(mapping_path) if mapping_path.exists() else {}
        existing = [row["id"] for row in packet["inputs"].get("tree_ref", {}).get("features", [])]
        features, mapping = assign_identities(tree["features"], mapping, existing)
        write_json(mapping_path, mapping)
        resolved_tree = {**tree, "features": features,
                         "lineage": [{**row, "new_ids": [mapping.get(key, key) for key in row["new_ids"]]}
                                     for row in tree["lineage"]]}
        tree_ref = self.artifacts.put(resolved_tree)
        previous = packet["inputs"].get("bindings_ref", {})
        if previous and previous["snapshot_id"] != packet["work"]["snapshot_id"]:
            migration = validate_preserved_sources(previous, packet["work"]["snapshot_id"], scope,
                                                   packet["work"]["topic_ids"], self.catalog)
            write_json(folder / "source-migration.json", migration, immutable=True)
        combined = merge_binding_scope(previous, bound, scope)
        bindings = {"schema_version": 3, "snapshot_id": packet["work"]["snapshot_id"], "tree_ref": tree_ref,
                    **combined, "bindings": [{**row, "feature_id": mapping.get(row["feature_id"], row["feature_id"])}
                                              for row in combined["bindings"]],
                    "routes": [{**row, "feature_id": mapping.get(row["feature_id"], row["feature_id"])} for row in combined["routes"]]}
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
