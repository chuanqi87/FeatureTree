"""Stage packets carry fixed source scope and only committed upstream artifacts."""

from featuretree.core.content import digest


def build_packet(plan, task, state, registry, artifacts):
    work = next(work for work in plan["works"] if work["id"] == task["work_id"])
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
              "model": plan["model"], "variant": plan["variant"], "limits": plan["budget"],
              "output_schema": config["output_schema"],
              "source_access": {"platform": config["definition"]["platform"],
                                "snapshot_id": work["snapshot_id"],
                                "api_ids": work["api_ids"], "topic_ids": work["topic_ids"]}}
    fixed_claims = [claim for key, payload in upstream.items()
                    if key in ("fk-android", "fk-ios", "fk-harmonyos", "fk-compare")
                    for claim in payload["claims"]]
    if fixed_claims:
        packet["fixed_claim_hashes"] = {claim["claim_id"]: digest(claim) for claim in fixed_claims}
    packet["input_hash"] = digest(packet)
    return packet


def envelope(packet, payload, outcome="pass", issues=()):
    return {**{key: packet[key] for key in ("protocol_version", "run_id", "work_id", "task_id", "stage_id", "input_hash")},
            "payload": payload, "outcome": outcome, "issues": list(issues), "source_requests": []}
