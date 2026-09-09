"""Pure traversal of authored parent relationships."""


def ancestor_chain(features, node):
    """Return self through root, rejecting missing parents and cycles."""
    chain, seen = [], set()
    while node is not None:
        if node in seen:
            raise ValueError(f"Tree cycle at {node}")
        if node not in features:
            raise ValueError(f"Missing tree node: {node}")
        chain.append(node)
        seen.add(node)
        node = features[node]["parent"]
    return chain


def descendants(features, node):
    selected = {node}
    while True:
        added = {fid for fid, f in features.items() if f.get("parent") in selected}
        if added <= selected:
            return selected
        selected |= added
