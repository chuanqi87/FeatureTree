"""Traceable API allocation and per-platform granularity gates; no model totals."""

import re
from collections import Counter

from featuretree.corpus.urls import canonical, platform as url_platform
from featuretree.workflow.stages import PLATFORMS

TARGET = 40
SPLIT_ABOVE = 50
COMPLETENESS = {"unknown": 0, "partial": 1, "complete": 2}


def api_key(symbol):
    """One qualified symbol family; overload signatures do not inflate counts."""
    return re.sub(r"\([^()]*\)$", "", re.sub(r"\s+", "", symbol)).replace("::", ".").replace("#", ".")


def api_index(scout, platform):
    index = {}
    for api in scout["apis"]:
        key = api_key(api["id"])
        if not key or not canonical(api["url"]) or url_platform(api["url"]) != platform:
            raise ValueError("API record needs a concrete symbol and same-platform official URL")
        if key in index and index[key]["kind"] != api["kind"]:
            raise ValueError("Conflicting API identity")
        index.setdefault(key, {**api, "id": key})
    referenced = set()
    for candidate in scout["candidates"]:
        keys = {api_key(i) for i in candidate["api_ids"]}
        if not keys <= index.keys():
            raise ValueError("Candidate references an API absent from its inventory")
        if candidate["api_completeness"] == "complete" and (
                candidate["public_api"] != "yes" or not keys):
            raise ValueError("Complete inventory requires positively identified public APIs; absence stays unknown")
        referenced.update(keys)
    if referenced != index.keys():
        raise ValueError("API inventory contains unassigned APIs")
    return index


def size_decision(platforms):
    maximum = max(p["count"] for p in platforms.values())
    if maximum > SPLIT_ABOVE:
        return "must_split"
    if maximum > TARGET:
        return "split_recommended"
    if any(p["completeness"] != "complete" for p in platforms.values()):
        return "needs_research"
    return "leaf_eligible"


def assess_allocations(proposal, scouts):
    """Every counted API comes from a mapped platform candidate; retain evidence."""
    nodes = {n["id"]: n for n in proposal["nodes"]}
    allocations = proposal["api_allocations"]
    if Counter(a["node_id"] for a in allocations) != Counter(nodes.keys()):
        raise ValueError("Each proposed node needs exactly one API allocation")
    by_node = {a["node_id"]: a["platforms"] for a in allocations}
    dispositions = {d["candidate_id"]: d for d in proposal["dispositions"]}
    surfaces = {node: {} for node in nodes}
    for platform, scout in zip(PLATFORMS, scouts):
        index = api_index(scout, platform)
        assigned = {node: set() for node in nodes}
        completeness = {node: [] for node in nodes}
        for candidate in scout["candidates"]:
            disposition = dispositions[candidate["id"]]
            if disposition["decision"] not in ("adopted", "duplicate"):
                continue
            keys = {api_key(i) for i in candidate["api_ids"]}
            covered = set()
            for node in disposition["node_ids"]:
                if node not in nodes:
                    raise ValueError("Adopted API paths must target a node in this proposal")
                selected = {api_key(i) for i in by_node[node][platform]["api_ids"]}
                covered.update(keys & selected)
                assigned[node].update(keys)
                completeness[node].append(candidate["api_completeness"])
            if not keys <= covered:
                raise ValueError("Mapped candidate APIs were silently omitted from child allocations")
        for node in nodes:
            allocation = by_node[node][platform]
            keys = {api_key(i) for i in allocation["api_ids"]}
            if not keys <= assigned[node]:
                raise ValueError("Node API allocation is not backed by its mapped candidates")
            ceiling = min((COMPLETENESS[c] for c in completeness[node]), default=0)
            if COMPLETENESS[allocation["completeness"]] > ceiling:
                raise ValueError("Node inventory completeness exceeds its platform evidence")
            surfaces[node][platform] = {"count": len(keys), "completeness": allocation["completeness"],
                                       "apis": [index[key] for key in sorted(keys)]}
    results = []
    for node, surface in surfaces.items():
        decision = size_decision(surface)
        if nodes[node]["granularity"] == "atomic" and decision != "leaf_eligible":
            raise ValueError(f"Cannot stop at {node}: {decision}; target <=40 per platform, >50 must split")
        results.append({"node_id": node, "platforms": surface, "decision": decision,
                        "next_action": "analyze" if nodes[node]["granularity"] == "branch" else "stop"})
    return results
