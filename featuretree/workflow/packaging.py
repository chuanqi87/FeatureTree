"""Stage packets carry fixed source scope and only committed upstream artifacts."""

from featuretree.core.content import digest
from featuretree.knowledge.ratings import assessment_fingerprint
from copy import deepcopy


def build_packet(plan, task, state, registry, artifacts):
    work = deepcopy(next(work for work in plan["works"] if work["id"] == task["work_id"]))
    platform = plan["stage_configs"][task["stage_id"]]["definition"]["platform"]
    if platform:
        work["api_ids"] = work["source_groups"]["declarations"][platform]
        work["topic_ids"] = work["source_groups"]["topics"][platform]
        work["source_groups"] = {kind: {platform: rows[platform]} for kind, rows in work["source_groups"].items()}
    upstream, upstream_refs = {}, {}
    for stage_id in sorted(registry.ancestors(task["stage_id"])):
        dependency = state["tasks"][work["id"] + "--" + stage_id]
        reference = dependency["result_ref"]
        if not reference:
            raise ValueError("Required upstream artifact is absent")
        response = artifacts.get(reference)
        upstream[stage_id] = response["payload"]
        upstream_refs[stage_id] = reference
    config = plan["stage_configs"][task["stage_id"]]
    inputs = {name: artifacts.get(reference) for name, reference in work["inputs"].items() if reference}
    packet = {"protocol_version": 2, "run_id": plan["run_id"], "work_id": work["id"],
              "task_id": task["id"], "stage_id": task["stage_id"], "work": work,
              "revision": task["revision"], "revision_feedback": task["feedback"],
              "upstream": upstream, "upstream_refs": upstream_refs, "inputs": inputs,
              "rules": config["rules"], "stage_fingerprint": config["fingerprint"],
              "implementation_files": config.get("implementation_files", {}),
              "model": plan["model"], "variant": plan["variant"], "limits": plan["budget"],
              "output_schema": config["output_schema"],
              "issue_routes": plan["registry"]["issue_routes"],
              "source_access": {"platform": config["definition"]["platform"],
                                "snapshot_id": work["snapshot_id"],
                                "api_ids": work["api_ids"], "topic_ids": work["topic_ids"]}}
    retained = [row["retained_response_ref"] for row in task["feedback"] if row.get("retained_response_ref")]
    if retained:
        packet["retained_candidate"] = artifacts.get(retained[-1])
    fixed_claims = [claim for key, payload in upstream.items()
                    if key in ("fk-android", "fk-ios", "fk-harmonyos", "fk-compare")
                    for claim in payload["claims"]]
    if fixed_claims:
        packet["fixed_claim_hashes"] = {claim["claim_id"]: digest(claim) for claim in fixed_claims}
    if config["definition"].get("dependency_scope") == "run":
        packet["neighbor_deliveries"] = []
        for neighbor in plan["works"]:
            check_ref = state["tasks"][neighbor["id"] + "--ft-check"]["result_ref"]
            review_ref = state["tasks"][neighbor["id"] + "--ft-review"]["result_ref"]
            check = artifacts.get(check_ref)["payload"]
            packet["neighbor_deliveries"].append({"work_id": neighbor["id"], "scope": neighbor["scope"],
                "check_ref": check_ref, "review_ref": review_ref, "tree_ref": check["tree_ref"],
                "tree": artifacts.get(check["tree_ref"]), "review": artifacts.get(review_ref)["payload"]})
        packet["source_access"]["api_ids"] = sorted({key for row in plan["works"] for key in row["api_ids"]})
        packet["source_access"]["topic_ids"] = sorted({key for row in plan["works"] for key in row["topic_ids"]})
    if task["stage_id"] in ("fk-confidence", "fk-assemble"):
        policy = plan["stage_configs"]["fk-confidence"]["rules"]["confidence"]
        context = {"inputs": work["inputs"], "snapshot_id": work["snapshot_id"], "policy": policy}
        evidence = {row["id"]: row for stage in ("fk-android", "fk-ios", "fk-harmonyos", "fk-compare")
                    for row in upstream[stage]["evidence"]}
        packet["rating_context"] = context
        packet["assessment_input_fingerprint"] = assessment_fingerprint(
            upstream["fk-scope"]["spec"], fixed_claims, upstream["fk-review"]["reviews"], list(evidence.values()), context)
    packet["input_hash"] = digest(packet)
    return packet


def envelope(packet, payload, outcome="pass", issues=()):
    return {**{key: packet[key] for key in ("protocol_version", "run_id", "work_id", "task_id", "stage_id", "input_hash")},
            "payload": payload, "outcome": outcome, "issues": list(issues), "source_requests": []}
