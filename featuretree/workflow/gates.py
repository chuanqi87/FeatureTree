"""Pure candidate validation against the immutable full-tree snapshot."""

from collections import Counter
from pathlib import PurePosixPath

from featuretree.corpus.urls import canonical, platform as url_platform
from featuretree.taxonomy.structure import lint_features
from featuretree.core.schemas import schema_validators
from featuretree.workflow.stages import PLATFORMS
from featuretree.taxonomy.traversal import descendants
from featuretree.workflow.api_inventory import assess_allocations
from featuretree.workflow.terminal import is_terminal_proposal, validate_terminal


def validate_proposal(root, snapshot, work, proposal, scouts):
    base = snapshot["features"]
    nodes = proposal["nodes"]
    if not 1 <= len(nodes) <= work["max_nodes"]:
        raise ValueError("Node budget exceeded or proposal empty")
    validator = schema_validators(root)["feature"]
    for node in nodes:
        validator.validate(node)
    ids = [n["id"] for n in nodes]
    terminal = is_terminal_proposal(work, nodes)
    if terminal:
        validate_terminal(base, work, nodes[0])
    if len(ids) != len(set(ids)) or (set(ids) & base.keys() and not terminal):
        raise ValueError("Duplicate ID or attempt to overwrite an existing node")
    merged = {**base, **{n["id"]: n for n in nodes}}
    selected = descendants(merged, work["node_id"])
    if not set(ids) <= selected:
        raise ValueError("Proposal contains nodes outside the assigned subtree")
    depth = int(base[work["node_id"]]["level"][1:])
    paths = [f["knowledge_path"] for f in merged.values()]
    if len(paths) != len(set(paths)):
        raise ValueError("Knowledge paths collide")
    for n in nodes:
        parent = merged[n["parent"]]
        level = int(n["level"][1:])
        if not terminal and (n["parent"] != work["node_id"] or level != depth + 1):
            raise ValueError(f"Invalid depth: {n['id']}")
        if not terminal and "api_surface" in n:
            raise ValueError("API counts are supplied by the coordinator, not the designer")
        if n["id"].split(".")[0] != work["node_id"].split(".")[0]:
            raise ValueError("Wrong domain namespace")
        if parent.get("granularity") != "branch":
            raise ValueError("Cannot add children to an atomic node")
        if n.get("granularity") not in ("atomic", "branch") or not n.get("sibling_axis"):
            raise ValueError("Every new node requires granularity and sibling_axis")
        if n["knowledge_role"] != ("leaf" if n["granularity"] == "atomic" else "rollup"):
            raise ValueError("Knowledge role must match granularity")
        path = PurePosixPath(n["knowledge_path"])
        expected = "knowledge/" + n["id"].replace(".", "/") + (
            ".yaml" if n["granularity"] == "atomic" else "/_rollup.yaml")
        if str(path) != expected:
            raise ValueError(f"Noncanonical knowledge path: {n['id']}")
        if n.get("anchor_status") != "unverified":
            raise ValueError("Designer must leave anchors unverified")
        bindings = [b for p in PLATFORMS for b in n.get("bindings", {}).get(p, [])]
        for platform, entries in n.get("bindings", {}).items():
            for binding in entries:
                url = canonical(binding.get("url", ""))
                if binding.get("url") and (not url or url_platform(url) != platform):
                    raise ValueError(f"Binding URL outside the platform's official sources: {n['id']}")
        if not any(b["id"].lower() not in {"pending", "unknown"} and canonical(b.get("url", ""))
                   for b in bindings):
            raise ValueError(f"No concrete official API anchor: {n['id']}")
        for target in n.get("related_features", []):
            if target not in merged or target == n["id"]:
                raise ValueError(f"Invalid related feature: {n['id']} -> {target}")
        if "children" in n and set(n["children"]) != {i for i, f in merged.items() if f["parent"] == n["id"]}:
            raise ValueError("Explicit children disagree with parent relationships")
    decisions = proposal["decisions"]
    if Counter(d["node_id"] for d in decisions) != Counter(ids):
        raise ValueError("Each new node needs exactly one stop/expand decision")
    for d in decisions:
        if (d["action"] == "stop") != (merged[d["node_id"]]["granularity"] == "atomic"):
            raise ValueError("Stop/expand decision disagrees with granularity")
    candidates = {c["id"] for scout in scouts for c in scout["candidates"]}
    dispositions = proposal["dispositions"]
    if Counter(d["candidate_id"] for d in dispositions) != Counter(candidates):
        raise ValueError("Every platform candidate needs exactly one disposition")
    for d in dispositions:
        if not set(d["node_ids"]) <= merged.keys():
            raise ValueError("Disposition references an unknown node")
        if d["decision"] in ("adopted", "duplicate") and not d["node_ids"]:
            raise ValueError("Adopted/duplicate candidates must identify their destination")
    issues = lint_features(merged, set())
    relevant = [i for i in issues if i["id"] in selected]
    errors = [i for i in relevant if i["severity"] == "error"]
    if errors:
        raise ValueError(f"Structural gate failed: {errors}")
    return {"issues": relevant, "counts": counts(nodes), "api_assessments": assess_allocations(proposal, scouts),
            "terminal_confirmation": terminal}


def counts(nodes):
    items = list(nodes)
    parents = {n["parent"] for n in items}
    return {"total": len(items), "branches": sum(n.get("granularity") == "branch" for n in items),
            "atomic_leaves": sum(n.get("granularity") == "atomic" for n in items),
            "unexpanded_branches": [n["id"] for n in items if n.get("granularity") == "branch"
                                    and n["id"] not in parents]}
