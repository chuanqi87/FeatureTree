"""A deterministic model substitute with explicit uncertainty, not production evidence."""

from copy import deepcopy
import hashlib

from featuretree.core.content import digest
from featuretree.corpus.catalog import IndexedCatalog
from featuretree.corpus.snapshots import SnapshotStore
from featuretree.knowledge.specifications import PLATFORMS
from featuretree.workflow.packaging import envelope


def feature(key="candidate"):
    return {"id": key, "parent_id": None, "name": "Example capability", "definition": "One observable goal",
            "includes": ["One outcome"], "excludes": ["Other outcomes"], "node_type": "leaf",
            "comparison_dimensions": ["capability_result", "api_surface"], "success_criteria": ["Goal succeeds"]}


def disposition(key):
    return {"id": key, "status": "assigned", "reason": "Documented goal", "rule": "public-sdk",
            "evidence_refs": ["doc_" + key.split("_")[-1]]}


def source_fixture(root, schemas):
    snapshot_store = SnapshotStore(root / "data/sources", schemas)
    documents, declarations, topics, families = [], [], [], []
    official_root = root / "docs-raw/official"
    official_root.mkdir(parents=True)
    for platform in PLATFORMS:
        body = "Fixture official documentation for " + platform
        path = official_root / f"{platform}.md"
        path.write_text(body)
        documents.append({"id": "doc_" + platform, "platform": platform, "title": "Example",
                          "url": {"android": "https://developer.android.com/reference/example",
                                  "ios": "https://developer.apple.com/documentation/example",
                                  "harmonyos": "https://developer.huawei.com/consumer/cn/doc/example"}[platform],
                          "body_path": path.name, "body_sha256": hashlib.sha256(body.encode()).hexdigest(),
                          "status": "verified", "metadata": {}})
        declarations.append({"schema_version": 3, "id": "api_" + platform, "platform": platform,
                             "distribution": platform + " SDK", "language": "c", "qualified_name": "example.run",
                             "signature": "()", "kind": "function", "visibility": "public",
                             "availability": {"module_id": "example"}, "sdk_version": "historical",
                             "source_path": "example.h", "source_line": 1, "source_hash": "a" * 64,
                             "original_id": "legacy_" + platform, "documentation": body,
                             "evidence_refs": ["doc_" + platform]})
        families.append({"id": "family_" + platform, "declaration_ids": ["api_" + platform],
                         "basis": "one declaration", "evidence_refs": [], "unresolved_aliases": []})
        topics.append({"id": "topic_" + platform, "platform": platform, "original_id": "legacy-topic_" + platform,
                       "path": ["example"], "title": "Example", "url": documents[-1]["url"], "summary": body,
                       "summary_strength": "body", "declaration_ids": ["api_" + platform],
                       "evidence_refs": ["doc_" + platform]})
    snapshot = snapshot_store.seal({"declarations": declarations, "families": families,
                                   "topics": topics, "documents": documents}, files=[], status="historical")
    return snapshot_store, snapshot, IndexedCatalog(snapshot_store, root / "data/indexes", official_root)


def baseline():
    return {"schema_version": 3, "id": "baseline_test", "created_at": "2026-09-10T00:00:00+00:00",
            "platforms": {platform: {"release": "historical", "sdk": "historical", "distribution": platform + " SDK",
                                     "device_forms": ["phone"], "verified_at": None, "evidence_refs": [],
                                     "status": "historical"} for platform in PLATFORMS}, "scope": "Test only"}


def specification(packet):
    from itertools import combinations
    questions = []
    for platform in PLATFORMS:
        questions.append({"id": "support_" + platform, "kind": "support", "platforms": [platform],
                          "dimension": "availability", "question": "Is the outcome supported?", "required": True,
                          "applicability_reason": "Mandatory platform support", "scenario": "Default",
                          "success_criteria": ["Outcome reached"]})
    for left, right in combinations(PLATFORMS, 2):
        for dimension in ("capability_result", "api_surface"):
            questions.append({"id": f"{left}_{right}_{dimension}", "kind": "comparison", "platforms": [left, right],
                              "dimension": dimension, "question": "How do the platforms differ?", "required": True,
                              "applicability_reason": "Mandatory pair comparison", "scenario": "Default",
                              "success_criteria": ["Compare the specified dimension"]})
    return {"schema_version": 3, "feature_id": packet["inputs"]["feature_ref"]["id"],
            "freeze_ref": packet["work"]["inputs"].get("freeze_ref"),
            "candidate_tree_ref": None if packet["work"]["inputs"].get("freeze_ref") else packet["work"]["inputs"].get("tree_ref"),
            "questions": questions, "scope": "Fixture knowledge sample", "rule_id": "confidence-v3-minimum-v1"}


def unknown_claim(question):
    return {"claim_id": "claim_" + question["id"], "question_id": question["id"], "kind": question["kind"],
            "platforms": question["platforms"], "dimension": question["dimension"], "result": "unknown",
            "statement": "Current SDK applicability has not been verified", "conditions": [], "evidence_refs": [],
            "premise_ids": [], "coverage_note": "", "alternative_paths": [], "gaps": ["Baseline unverified"], "context": []}


class ModelSubstitute:
    def __init__(self):
        self.calls = []

    def execute(self, root, agent, packet, folder, timeout, model, variant):
        self.calls.append((agent, packet["input_hash"]))
        platform = packet["source_access"]["platform"]
        if agent in ("ft-android", "ft-ios", "ft-harmonyos"):
            payload = {"platform": platform, "facts": [{"id": "fact_" + platform,
                       "api_ids": ["api_" + platform], "goal": "Example goal", "statement": "Example behavior",
                       "conditions": [], "implementation_steps": ["Call example.run"],
                       "evidence_refs": ["doc_" + platform], "gaps": []}],
                       "api_dispositions": [disposition("api_" + platform)],
                       "topic_dispositions": [disposition("topic_" + platform)]}
        elif agent == "ft-align":
            payload = {"relationships": [{"id": "alignment", "fact_ids": ["fact_" + p for p in PLATFORMS],
                        "relationship": "common_goal", "goal": "Example goal", "common_scope": "One outcome",
                        "differences": [], "evidence_refs": ["doc_" + p for p in PLATFORMS]}], "unmatched_fact_ids": []}
        elif agent == "ft-design":
            payload = {"work_type": packet["work"]["work_type"], "features": [feature()],
                       "changes": [{"operation": "add", "subject_ids": [], "candidate_ids": ["candidate"], "reason": "One goal"}]}
        elif agent == "ft-bind":
            payload = {"routes": [{"id": "default", "feature_id": "candidate", "platform": p, "goal": "One outcome",
                        "conditions": [], "steps": [{"description": "Invoke the fixture API", "api_ids": ["api_" + p]}],
                        "completeness": "complete", "gaps": [], "evidence_refs": ["doc_" + p]} for p in PLATFORMS],
                       "bindings": [{"declaration_id": "api_" + p, "feature_id": "candidate", "usage": "One outcome",
                        "role": "core", "route_id": "default", "evidence_refs": ["doc_" + p]} for p in PLATFORMS],
                       "api_dispositions": [disposition("api_" + p) for p in PLATFORMS],
                       "topic_dispositions": [disposition("topic_" + p) for p in PLATFORMS]}
        elif agent == "ft-granularity":
            payload = {"decisions": [{"feature_id": "candidate", "verdict": "appropriate", "reason": "One comparable goal",
                        "suggestion": "", "policy_id": "granularity-candidate-v1"}]}
        elif agent == "ft-coverage":
            payload = {"findings": [], "unresolved_ids": []}
        elif agent in ("ft-review", "ft-integrate"):
            payload = {"reviews": [{"subject_id": "candidate", "verdict": "pass", "reason": "Fixture checked", "evidence_refs": []}]}
            if agent == "ft-integrate":
                payload.update(freeze_recommendation="eligible", scope_ids=["candidate"])
        elif agent == "fk-scope":
            payload = {"spec": specification(packet)}
        elif agent in ("fk-android", "fk-ios", "fk-harmonyos", "fk-compare"):
            questions = packet["upstream"]["fk-scope"]["spec"]["questions"]
            selected = [question for question in questions if
                        (question["kind"] == "comparison" if agent == "fk-compare" else question["platforms"] == [platform])]
            payload = {"claims": [unknown_claim(question) for question in selected], "evidence": []}
            if agent != "fk-compare":
                payload["platform"] = platform
        elif agent == "fk-review":
            payload = {"reviews": [{"claim_id": key, "claim_hash": value, "verdict": "tentative",
                        "reason": "Unknown is accurately represented", "evidence_refs": []}
                                   for key, value in packet["fixed_claim_hashes"].items()]}
        elif agent == "fk-confidence":
            payload = {"assessments": [{"claim_id": key, "claim_hash": value, "level": "low", "reason": "Baseline unknown",
                        "gaps": ["Baseline unknown"], "requires_runtime_observation": False, "runtime_evidence_refs": [],
                        "rule_id": "confidence-v3-minimum-v1", "assessor": "fk-confidence"}
                                      for key, value in packet["fixed_claim_hashes"].items()]}
            for assessment in payload["assessments"]:
                assessment["input_fingerprint"] = packet["assessment_input_fingerprint"]
        else:
            raise AssertionError(agent)
        return envelope(packet, payload), {"model": model, "usage": [{"tokens": {"input": 1, "output": 1}}]}
