"""Strict envelopes plus stage-specific semantic contract checks."""

from jsonschema import Draft202012Validator
from featuretree.corpus.urls import canonical, platform as url_platform

from featuretree.workflow.stages import CHECKS, PLATFORMS
from featuretree.workflow.state import digest, read_json


def output_schema(root, stage):
    schema = read_json(root / "config/workflow/contracts.json")
    kind = "scout" if stage in PLATFORMS else "review" if stage == "integrate" else stage
    return {"$schema": schema["$schema"], "$defs": schema["$defs"],
            **schema["envelope"], "properties": {**schema["envelope"]["properties"],
            "payload": {"$ref": f"#/$defs/{kind}"}}}


def validate_result(root, packet, result):
    Draft202012Validator(output_schema(root, packet["stage"])).validate(result)
    for key in ("task_id", "input_hash", "stage"):
        if result[key] != packet[key]:
            raise ValueError(f"Envelope mismatch: {key}")
    payload = result["payload"]
    stage = packet["stage"]
    if stage in PLATFORMS:
        ids = [c["id"] for c in payload["candidates"]]
        if len(ids) != len(set(ids)) or any(not i.startswith(stage + ":") for i in ids):
            raise ValueError("Candidate IDs must be unique and platform-prefixed")
        if len(ids) > packet["work"]["max_nodes"]:
            raise ValueError("Candidate budget exceeded; split the task")
        if (not ids or any(c["public_api"] == "unknown" for c in payload["candidates"])) and not payload["gaps"]:
            raise ValueError("Missing/uncertain platform candidates require explicit gaps")
        for candidate in payload["candidates"]:
            url = canonical(candidate["binding"]["url"])
            if not url or url_platform(url) != stage:
                raise ValueError("Candidate anchor must be an official URL for the assigned platform")
    if stage in ("review", "integrate"):
        checks = payload["checks"]
        if set(checks) != set(CHECKS):
            raise ValueError(f"Review must cover {CHECKS}")
        if payload["reviewed_hash"] != digest(packet["inputs"]):
            raise ValueError("Review is not bound to the supplied inputs")
        if payload["verdict"] == "pass" and (any(v["status"] != "pass" for v in checks.values())
                or any(i["severity"] == "blocking" for i in payload["issues"])):
            raise ValueError("Passing review contains unresolved blocking checks")
        if payload["verdict"] == "revise" and not payload["issues"]:
            raise ValueError("Revision requires actionable issues")
