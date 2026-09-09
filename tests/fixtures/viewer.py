"""Synthetic multi-level content for UI tests, independent of authored project data."""

from featuretree.knowledge.comparison import new_knowledge
from featuretree.reporting.views import tree_view
from tests.fixtures.knowledge import feature


def snapshot():
    platforms = {p: {"name": p} for p in ("android", "ios", "harmonyos")}
    dimensions = ["availability", "programming_model", "lifecycle_background",
                  "permissions_privacy", "limits_precision", "device_forms", "api_surface"]
    chain = ["sample", "sample.group", "sample.group.stage",
             "sample.group.stage.operation", "sample.group.stage.operation.filter"]
    features = {}
    for index, fid in enumerate(chain + ["unrelated"]):
        branch = fid in chain[:-1]
        node = feature()
        node.update(id=fid, parent=chain[index - 1] if 0 < index < len(chain) else None,
                    level=f"L{index + 1}" if index < len(chain) else "L1",
                    knowledge_role="rollup" if branch else "leaf",
                    knowledge_path=f"knowledge/{fid.replace('.', '/')}.yaml",
                    name={"zh": "样例扫描过滤" if fid == chain[-1] else fid, "en": fid},
                    comparison_dimensions=dimensions)
        features[fid] = node
    docs = {fid: new_knowledge(node, platforms) for fid, node in features.items()}
    target = docs[chain[-1]]
    target.update(status="draft", programming_model="Synthetic readSampleRecord fixture for UI tests.")
    target["comparisons"] = [{"dimension": "programming_model", "platforms": ["android", "ios"],
                              "result": "unknown", "verification": "in_review",
                              "scope": "样例扫描过滤", "rationale": "样例扫描过滤差异仅为测试数据。"}]
    return {"roots": ["sample", "unrelated"], "platforms": platforms,
            "dimensions": {key: key for key in dimensions},
            "nodes": [{**node, "knowledge": docs[node["id"]]}
                      for node in tree_view(features, docs, platforms)]}
