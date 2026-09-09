"""Create immutable node work orders and a deterministic dependency graph."""

from datetime import date
import uuid

from jsonschema import Draft202012Validator

from featuretree.core.storage import Repository, write_json
from featuretree.workflow.stages import PLATFORMS, STAGES
from featuretree.taxonomy.traversal import descendants
from featuretree.workflow.state import digest, now, read_json, rule_hash, save_state


def make_plan(root, nodes, baseline, depth=1, max_nodes=12, workers=3,
              timeout=600, max_attempts=2, max_revisions=2, model=None, variant=None,
              max_input_chars=500000, first_response_timeout=120):
    if not (depth == 1 and 1 <= max_nodes <= 200 and 1 <= workers <= 16
            and 1 <= timeout <= 7200 and 1 <= max_attempts <= 5 and 0 <= max_revisions <= 5
            and 10000 <= max_input_chars <= 2000000 and 1 <= first_response_timeout <= 7200):
        raise ValueError("Invalid execution budget")
    if variant and not model:
        raise ValueError("Pin --model when specifying --variant")
    Draft202012Validator(read_json(root / "config/workflow/baseline.schema.json")).validate(baseline)
    date.fromisoformat(baseline["as_of"])
    features = Repository(root).features()
    if not nodes or len(set(nodes)) != len(nodes):
        raise ValueError("Select at least one unique node")
    for node in nodes:
        if node not in features or features[node].get("granularity") != "branch":
            raise ValueError(f"Select an existing branch: {node}")
        if (set(nodes) - {node}) & descendants(features, node):
            raise ValueError("Ancestor and descendant work orders cannot overlap")
    run_id = "run-" + uuid.uuid4().hex[:12]
    folder = root / ".workflow/runs" / run_id
    folder.mkdir(parents=True)
    snapshot = {"features": features, "baseline": baseline,
                "tree_files": {str(p.relative_to(root)): p.read_text()
                               for p in sorted((root / "taxonomy").glob("*.yaml"))}}
    write_json(folder / "snapshot.json", snapshot)
    tasks = {}
    for node in nodes:
        for stage in STAGES:
            deps = [] if stage in PLATFORMS else [f"{node}/{p}" for p in PLATFORMS] if stage == "scope" else (
                [f"{node}/{p}" for p in ("scope", *PLATFORMS)] if stage == "synthesize" else
                [f"{node}/synthesize"] if stage == "review" else [f"{node}/review", f"{node}/synthesize"])
            tid = f"{node}/{stage}"
            tasks[tid] = {"id": tid, "node": node, "stage": stage, "dependencies": deps,
                          "status": "pending", "attempts": [], "allowance": max_attempts}
    tasks["batch/integrate"] = {"id": "batch/integrate", "node": None, "stage": "integrate",
        "dependencies": [f"{n}/{s}" for n in nodes for s in ("synthesize", "review", "anchors")],
        "status": "pending", "attempts": [], "allowance": max_attempts}
    state = {"schema_version": 1, "id": run_id, "root": str(root.resolve()), "created_at": now(),
             "snapshot_hash": digest(snapshot), "tree_hash": digest(features), "rule_hash": rule_hash(root),
             "nodes": nodes, "depth": depth, "max_nodes": max_nodes, "workers": workers,
             "timeout": timeout, "max_attempts": max_attempts, "max_revisions": max_revisions,
             "first_response_timeout": min(timeout, first_response_timeout),
             "revisions": {n: 0 for n in nodes}, "model": model, "variant": variant,
             "max_input_chars": max_input_chars, "tasks": tasks}
    save_state(folder, state)
    return state


def work_order(snapshot, state, node):
    features = snapshot["features"]
    selected = descendants(features, node) if node else set(features)
    ancestors = []
    parent = features[node]["parent"] if node else None
    while parent:
        ancestors.append(features[parent])
        parent = features[parent]["parent"]
    neighbors = {k for k, f in features.items() if f["level"] == "L1" or
                 (node and f["parent"] == features[node]["parent"])}
    catalog = lambda f: {k: f[k] for k in ("id", "parent", "name")}
    boundary = lambda f: {**catalog(f), **({"definition": f["definition"],
        "comparison_scope": f["comparison_scope"]} if f["id"] in neighbors else {})}
    return {"node_id": node, "depth": state["depth"], "max_nodes": state["max_nodes"],
            "baseline": snapshot["baseline"], "ancestors": ancestors,
            "api_policy": {"target_per_platform": 40, "must_split_above": 50, "max_api_records": 200,
                           "incomplete_counts_are_lower_bounds": True},
            "subtree": {k: features[k] if node else boundary(features[k]) for k in sorted(selected)},
            "boundaries": [boundary(f) for k, f in features.items() if k not in selected]}
