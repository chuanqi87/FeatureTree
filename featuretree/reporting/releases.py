"""Release-pinned projections. Tree requests never load complete knowledge bodies."""

from featuretree.core.io import write_json, write_bytes
from featuretree.core.content import identifier
from featuretree.reporting.markdown import article_markdown
import yaml
from featuretree.taxonomy.model import change_impact


class ReleaseReader:
    def __init__(self, versions, artifacts):
        self.versions, self.artifacts = versions, artifacts

    def current(self):
        manifest = self.versions.pin()
        if manifest is None:
            return {"release_id": None, "status": "not_published", "summary": {}}
        return {"release_id": manifest["release_id"], "status": "published",
                "summary": self.artifacts.get(manifest["validation_ref"])}

    def tree(self, release_id=None):
        manifest = self.versions.pin(release_id)
        if manifest is None:
            return {"release_id": None, "features": [], "summary": {}}
        tree = self.artifacts.get(manifest["tree_ref"])
        report = self.artifacts.get(manifest["validation_ref"])
        summaries = report["knowledge_summaries"]
        return {"release_id": manifest["release_id"], "features": [{**node,
                "knowledge": summaries.get(node["id"], {"validity": "not_produced", "confidence": None})}
                for node in tree["features"]], "summary": report}

    def feature(self, feature_id, release_id=None):
        manifest = self.versions.pin(release_id)
        if not manifest:
            raise KeyError("No published tree")
        tree = self.artifacts.get(manifest["tree_ref"])
        node = next((row for row in tree["features"] if row["id"] == feature_id), None)
        if node is None:
            raise KeyError(feature_id)
        bindings = self.artifacts.get(manifest["bindings_ref"])
        selected = [row for row in bindings["bindings"] if row["feature_id"] == feature_id]
        return {"release_id": manifest["release_id"], "feature": node,
                "bindings": selected, "freeze_refs": [reference for reference in manifest["freeze_refs"]
                if feature_id in self.artifacts.get(reference)["leaf_ids"]]}

    def knowledge(self, feature_id, release_id=None):
        manifest = self.versions.pin(release_id)
        reference = manifest["knowledge_refs"].get(feature_id) if manifest else None
        if not reference:
            return {"release_id": manifest["release_id"] if manifest else None, "feature_id": feature_id,
                    "status": "not_produced", "article": None}
        report = self.artifacts.get(manifest["validation_ref"])
        return {"release_id": manifest["release_id"], "article_ref": reference,
                "summary": report["knowledge_summaries"][feature_id], "article": self.artifacts.get(reference)}

    def compare(self, before_id, after_id):
        before, after = self.versions.get(before_id), self.versions.get(after_id)
        before_knowledge, after_knowledge = before["knowledge_refs"], after["knowledge_refs"]
        keys = set(before_knowledge) | set(after_knowledge)
        return {"before": before_id, "after": after_id,
                "tree": change_impact(self.artifacts.get(before["tree_ref"]), self.artifacts.get(after["tree_ref"])),
                "knowledge_changes": sorted(key for key in keys if before_knowledge.get(key) != after_knowledge.get(key))}

    def export(self, directory, release_id=None):
        manifest = self.versions.pin(release_id)
        if not manifest:
            raise ValueError("No release is available to export")
        target = directory / manifest["release_id"]
        tree = self.tree(manifest["release_id"])
        write_json(target / "manifest.json", manifest)
        write_json(target / "tree.json", tree)
        write_bytes(target / "tree.yaml", yaml.safe_dump(tree, allow_unicode=True, sort_keys=False).encode())
        names = {row["id"]: row["name"] for row in tree["features"]}
        for feature_id in manifest["knowledge_refs"]:
            identifier(feature_id)
            projection = self.knowledge(feature_id, manifest["release_id"])
            write_json(target / "knowledge" / f"{feature_id}.json", projection)
            write_bytes(target / "knowledge" / f"{feature_id}.yaml", yaml.safe_dump(projection, allow_unicode=True, sort_keys=False).encode())
            write_bytes(target / "knowledge" / f"{feature_id}.md", article_markdown(projection, names.get(feature_id, feature_id)).encode())
        return {"release_id": manifest["release_id"], "directory": str(target)}
