"""Read-only tree browsing projections; candidate and published versions stay distinct."""


class TreeBrowser:
    def __init__(self, artifacts, versions, reader, catalog):
        self.artifacts = artifacts
        self.versions = versions
        self.reader = reader
        self.catalog = catalog

    def views(self, candidates, runs, release_id=None):
        items = []
        manifest = self.versions.pin(release_id)
        if manifest:
            items.append({"id": manifest["release_id"], "status": "formal",
                          "tree_ref": manifest["tree_ref"], "bindings_ref": manifest["bindings_ref"],
                          "features": self.reader.tree(manifest["release_id"])["features"],
                          "updated_at": "", "run_status": "published"})
        states = {row["run_id"]: row for row in runs}
        for candidate in candidates:
            if not candidate.get("tree_ref"):
                continue
            state = states[candidate["run_id"]]
            items.append({"id": candidate["result_ref"], "status": "candidate",
                          "tree_ref": candidate["tree_ref"], "bindings_ref": candidate["bindings_ref"],
                          "features": self.artifacts.get(candidate["tree_ref"])["features"],
                          "run_id": candidate["run_id"], "run_status": state["status"],
                          "updated_at": state["updated_at"]})
        return {"release_id": manifest["release_id"] if manifest else None, "items": items}

    def detail(self, view, feature_id):
        feature = next((row for row in view["features"] if row["id"] == feature_id), None)
        if feature is None:
            raise KeyError(feature_id)
        bundle = self.artifacts.get(view["bindings_ref"])
        bindings = [row for row in bundle["bindings"] if row["feature_id"] == feature_id]
        records = {}
        for row in bindings:
            api_id = row["declaration_id"]
            if api_id not in records:
                try:
                    records[api_id] = self.catalog.get(bundle["snapshot_id"], "declarations", api_id)
                except KeyError:
                    records[api_id] = None
        return {"feature": feature, "status": view["status"], "snapshot_id": bundle["snapshot_id"],
                "bindings": [{**row, "api": records[row["declaration_id"]]} for row in bindings]}
