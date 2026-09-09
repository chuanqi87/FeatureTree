"""Confirm an existing empty branch as a leaf without inventing a same-meaning child."""

MUTABLE = {"granularity", "knowledge_role", "knowledge_path", "leaf_at_this_level", "anchor_status"}


def is_terminal_proposal(work, nodes):
    return len(nodes) == 1 and nodes[0]["id"] == work["node_id"]


def validate_terminal(base, work, node):
    original = base[work["node_id"]]
    if original["level"] == "L1" or any(n["parent"] == original["id"] for n in base.values()):
        raise ValueError("Only an empty non-L1 branch can stop without creating children")
    if node.get("granularity") != "atomic" or not node.get("leaf_at_this_level"):
        raise ValueError("Stopping the current branch requires an explicit atomic leaf")
    if {k: v for k, v in node.items() if k not in MUTABLE} != {
            k: v for k, v in original.items() if k not in MUTABLE}:
        raise ValueError("Terminal confirmation cannot rename or redefine the selected node")

