"""The single publication use case: validate complete immutable manifests, then CAS."""

from typing import Protocol

from featuretree.core.content import digest, identifier, timestamp
from featuretree.core.io import ConflictError, file_lock, read_json, write_json
from featuretree.knowledge.reviews import project_reviews
from featuretree.knowledge.validity import stale_reasons
from featuretree.taxonomy.model import validate_tree
from featuretree.workflow.knowledge_validation import validate_article


class ReleaseService(Protocol):
    def prepare(self, candidate: dict, expected: str | None, key: str) -> dict: ...
    def publish(self, key: str) -> dict: ...
    def rollback(self, target: str, expected: str, key: str) -> dict: ...


class LocalReleaseService:
    def __init__(self, versions, artifacts, schemas, snapshots, catalog, reviews, freezes):
        self.versions, self.artifacts, self.schemas = versions, artifacts, schemas
        self.snapshots, self.catalog, self.reviews = snapshots, catalog, reviews
        self.freezes = freezes

    def prepare(self, candidate, expected, key):
        identifier(key)
        request_path = self.versions.directory / "release_requests" / f"{key}.json"
        request_hash = digest({"candidate": candidate, "expected": expected})
        with file_lock(request_path.with_suffix(".lock")):
            if request_path.exists():
                request = read_json(request_path)
                if request["request_hash"] != request_hash:
                    raise ConflictError("Publication key already belongs to another request")
            else:
                request = {"request_hash": request_hash, "created_at": candidate.get("created_at", timestamp())}
                write_json(request_path, request, immutable=True)
            transaction_path = self.versions.directory / "transactions" / f"{key}.json"
            if transaction_path.exists():
                return read_json(transaction_path)
            return self._prepare({**candidate, "created_at": request["created_at"]}, expected, key)

    def _prepare(self, candidate, expected, key):
        articles = {reference: self.artifacts.get(reference) for reference in candidate["knowledge_refs"].values()}
        projection = project_reviews(articles, self.reviews.events())
        body = {"schema_version": 1, "parent_id": expected,
                **{name: candidate[name] for name in ("tree_ref", "bindings_ref", "baseline_ref", "source_ids", "freeze_refs", "knowledge_refs")},
                "review_projection_ref": self.artifacts.put(projection),
                "created_at": candidate["created_at"], "kind": candidate.get("kind", "publish"),
                "rollback_target": candidate.get("rollback_target")}
        body["validation_ref"] = self.artifacts.put(self.validate(body))
        body["release_id"] = "r_" + digest(body)[:32]
        self.schemas.validate("https://featuretree.local/schema/release/v1/manifest", body)
        return self.versions.prepare(body, expected, key)

    def validate(self, manifest):
        tree = self.artifacts.get(manifest["tree_ref"])
        bindings = self.artifacts.get(manifest["bindings_ref"])
        baseline = self.artifacts.get(manifest["baseline_ref"])
        for name, value in (("tree", tree), ("bindings", bindings), ("baseline", baseline)):
            self.schemas.validate(f"https://featuretree.local/schema/business/v3/{name}", value)
        nodes = validate_tree(tree)
        if bindings["tree_ref"] != manifest["tree_ref"]:
            raise ValueError("Tree/binding version mismatch")
        for source_id in manifest["source_ids"]:
            self.snapshots.get(source_id)
        freezes = {reference: self.artifacts.get(reference) for reference in manifest["freeze_refs"]}
        if not freezes:
            raise ValueError("Formal publication requires a user-approved frozen domain")
        for frozen in freezes.values():
            self.freezes.validate(frozen)
        if not any(frozen["tree_ref"] == manifest["tree_ref"] and frozen["bindings_ref"] == manifest["bindings_ref"]
                   and frozen["baseline_ref"] == manifest["baseline_ref"] for frozen in freezes.values()):
            raise ValueError("Published tree/bindings need a matching independently reviewed domain freeze")
        if bindings["snapshot_id"] not in manifest["source_ids"]:
            raise ValueError("The active binding source is absent from the release manifest")
        articles, stale = {}, {}
        for feature_id, reference in manifest["knowledge_refs"].items():
            article = self.artifacts.get(reference)
            self.schemas.validate("https://featuretree.local/schema/business/v3/article", article)
            if article["draft"] or article["feature_id"] != feature_id:
                raise ValueError("Calibration drafts cannot be published as formal knowledge")
            validate_article(article, self.artifacts, self.schemas, self.catalog, self.freezes.provenance)
            if article["freeze_ref"] not in freezes:
                raise ValueError("Knowledge freeze is not referenced by the manifest")
            frozen = freezes[article["freeze_ref"]]
            causes = stale_reasons(article, nodes.get(feature_id), bindings, frozen, manifest["baseline_ref"], manifest["source_ids"], self.catalog)
            if causes:
                stale[feature_id] = causes
            articles[reference] = article
        projection = project_reviews(articles, self.reviews.events())
        if digest(projection) != manifest["review_projection_ref"]:
            raise ConflictError("Human review history changed; prepare a fresh review projection")
        self.artifacts.verify(manifest["review_projection_ref"])
        invalid_refs = {row["article_ref"] for row in projection["invalidated_claims"]}
        summaries = {article["feature_id"]: {"article_ref": reference,
                     "confidence": article["overall_confidence"], "dragging_claims": article["confidence_reasons"],
                     "validity": "stale" if article["feature_id"] in stale else "invalidated" if reference in invalid_refs else "current",
                     "review_id": next((row["id"] for row in projection["tickets"] if row["article_ref"] == reference), None)}
                     for reference, article in articles.items()}
        return {"stale_knowledge": stale, "review_invalidations": projection["invalidated_claims"],
                "knowledge_summaries": summaries,
                "feature_count": len(nodes), "leaf_count": sum(row["node_type"] == "leaf" for row in nodes.values()),
                "knowledge_count": len(articles)}

    def publish(self, key):
        def validate_prepared(manifest):
            if digest(self.validate(manifest)) != manifest["validation_ref"]:
                raise ConflictError("Prepared validation projection changed; prepare a fresh release")
        # Review events and the publication pointer are committed under one ordering.
        with file_lock(self.reviews.directory / "review.lock"):
            return self.versions.commit(key, validate_prepared)

    def rollback(self, target, expected, key):
        original = self.versions.get(target)
        candidate = {**original, "kind": "rollback", "rollback_target": target}
        candidate.pop("created_at")
        self.prepare(candidate, expected, key)
        return self.publish(key)

    def rebase(self, transaction_key, expected, key):
        """Merge a knowledge-only candidate onto an unrelated newer publication."""
        identifier(transaction_key)
        transaction = read_json(self.versions.directory / "transactions" / f"{transaction_key}.json")
        proposed = self.versions.get(transaction["release_id"])
        if transaction["expected"] is None or expected is None:
            raise ConflictError("Initial publications cannot be rebased as knowledge-only updates")
        base = self.versions.pin(transaction["expected"])
        current = self.versions.pin(expected)
        if not base or not current or self.versions.current_id() != expected:
            raise ConflictError("Rebase needs an existing, current expected release")
        structural = ("tree_ref", "bindings_ref", "baseline_ref", "source_ids", "freeze_refs")
        if any(proposed[name] != base[name] for name in structural):
            raise ConflictError("Tree/source changes require integration review against the new tree before replanning")
        keys = set(base["knowledge_refs"]) | set(proposed["knowledge_refs"])
        changed = {feature: proposed["knowledge_refs"].get(feature) for feature in keys
                   if base["knowledge_refs"].get(feature) != proposed["knowledge_refs"].get(feature)}
        merged = dict(current["knowledge_refs"])
        nodes = validate_tree(self.artifacts.get(current["tree_ref"]))
        bindings = self.artifacts.get(current["bindings_ref"])
        for feature, reference in changed.items():
            now = current["knowledge_refs"].get(feature)
            if now not in (base["knowledge_refs"].get(feature), reference):
                raise ConflictError("Another publication changed the same leaf knowledge")
            if reference is None:
                merged.pop(feature, None)
                continue
            article = self.artifacts.get(reference)
            frozen = self.artifacts.get(article["freeze_ref"])
            if stale_reasons(article, nodes.get(feature), bindings, frozen, current["baseline_ref"], current["source_ids"], self.catalog):
                raise ConflictError("The proposed knowledge has related dependency changes and needs research revision")
            merged[feature] = reference
        candidate = {**{name: current[name] for name in structural}, "knowledge_refs": merged}
        return self.prepare(candidate, expected, key)
