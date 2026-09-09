"""Synthetic workflow tests: these fixtures make no claims about real platforms."""

import threading
import time
from featuretree.taxonomy.authoring import feature, bind
from featuretree.workflow.stages import CHECKS, PLATFORMS


def fixture_proposal(work):
    root = work["node_id"]
    depth = int(work["subtree"][root]["level"][1:])
    nodes = []
    for suffix in ("first", "second"):
        fid = root + "." + suffix
        nodes.append(feature(fid, parent=root, level=f"L{depth+1}", zh=f"测试分支{suffix}",
            en=f"Fixture {suffix}", definition=f"Synthetic scope {suffix}", includes=[suffix],
            sibling_axis="synthetic task category", bindings=bind("android", "class", "FixtureApi",
                "https://developer.android.com/reference/fixture")))
    return {"nodes": nodes,
            "api_allocations": [{"node_id": n["id"], "platforms": {p: {
                "api_ids": ["FixtureApi.run"] if i == 0 else [], "completeness": "partial" if i == 0 else "unknown",
                "reason": "Synthetic API allocation"} for p in PLATFORMS}} for i, n in enumerate(nodes)],
            "dispositions": [{"candidate_id": f"{p}:candidate", "decision": "adopted",
                              "node_ids": [nodes[0]["id"]], "reason": "Synthetic mapping"} for p in PLATFORMS],
            "decisions": [{"node_id": n["id"], "action": "expand", "reason": "Fixture pending branch"}
                          for n in nodes], "gaps": ["Fixture only; not real capability research"]}


class FixtureBackend:
    def __init__(self, fail_once=None, reject_once=None, mutate=None):
        self.fail_once = fail_once
        self.reject_once = reject_once
        self.mutate = mutate
        self.calls = []
        self.active = 0
        self.peak = 0
        self.guard = threading.Lock()

    def execute(self, root, agent, packet, folder, timeout, model, variant):
        with self.guard:
            self.calls.append(packet["task_id"])
            self.active += 1
            self.peak = max(self.peak, self.active)
        try:
            time.sleep(0.01)
            stage = packet["stage"]
            if self.fail_once == stage:
                self.fail_once = None
                raise RuntimeError("Synthetic transient failure")
            if stage == "scope":
                payload = {"axis": "Task category", "groups": [{"name": "Fixture", "definition": "Fixture"}],
                           "boundaries": ["Fixture boundary"], "questions": []}
            elif stage in PLATFORMS:
                urls = {"android": "https://developer.android.com/reference/fixture",
                        "ios": "https://developer.apple.com/documentation/fixture",
                        "harmonyos": "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fixture"}
                payload = {"candidates": [{"id": stage + ":candidate", "name": "Fixture", "definition": "Fixture",
                    "binding": {"kind": "class", "id": "FixtureApi", "url": urls[stage]},
                    "distribution": stage, "device_forms": ["phone"], "conditions": [],
                    "public_api": "unknown", "rationale": "Synthetic candidate",
                    "api_ids": ["FixtureApi.run"], "api_completeness": "partial"}], "queries": ["fixture"],
                    "gaps": ["Synthetic candidate has no real public API evidence"],
                    "apis": [{"id": "FixtureApi.run", "kind": "method", "url": urls[stage], "evidence": "Synthetic only"}]}
            elif stage == "synthesize":
                payload = fixture_proposal(packet["work"])
            else:
                reject = self.reject_once == stage
                self.reject_once = None if reject else self.reject_once
                payload = {"reviewed_hash": packet["reviewed_hash"], "verdict": "revise" if reject else "pass",
                           "checks": {k: {"status": "pass", "reason": "Synthetic reviewed check"} for k in CHECKS},
                           "issues": [{"node_id": packet["work"]["node_id"] or "sample", "code": "fixture",
                                       "severity": "blocking", "message": "Synthetic issue",
                                       "requested_change": "Fix fixture boundary"}] if reject else []}
            result = {"schema_version": 1, "task_id": packet["task_id"], "input_hash": packet["input_hash"],
                      "stage": stage, "payload": payload}
            if self.mutate:
                self.mutate(result)
            return result, {"backend": "synthetic-fixture", "usage": []}
        finally:
            with self.guard:
                self.active -= 1
