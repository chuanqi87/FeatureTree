"""Create only missing knowledge stubs without overwriting authored content."""

from featuretree.knowledge.comparison import new_knowledge
from featuretree.core.storage import contained_path, write_yaml


def create_missing_knowledge(repo):
    features = repo.features()
    platforms = repo.config()["platforms"]
    created = []
    for feature in features.values():
        path = contained_path(repo.root, feature["knowledge_path"], "knowledge")
        if path.exists():
            continue
        doc = new_knowledge(feature, platforms)
        if doc["role"] == "rollup":
            doc["child_index"] = [f["id"] for f in features.values() if f["parent"] == feature["id"]]
        write_yaml(path, doc)
        created.append(feature["id"])
    return created
