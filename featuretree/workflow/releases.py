"""The single publication use case: validate complete immutable manifests, then CAS."""

from typing import Protocol

from featuretree.core.content import digest, identifier, timestamp
from featuretree.core.io import ConflictError, file_lock, read_json, write_json
from featuretree.knowledge.claims import validate_evidence
from featuretree.knowledge.ratings import rate_article
from featuretree.knowledge.reviews import project_reviews
from featuretree.knowledge.specifications import validate_spec
from featuretree.knowledge.validity import stale_reasons
from featuretree.taxonomy.model import validate_tree


class ReleaseService(Protocol):
    def prepare(self, candidate: dict, expected: str | None, key: str) -> dict: ...
    def publish(self, key: str) -> dict: ...
    def rollback(self, target: str, expected: str, key: str) -> dict: ...


class LocalReleaseService:
    def __init__(self, versions, artifacts, schemas, snapshots, catalog, reviews):
        self.versions, self.artifacts, self.schemas = versions, artifacts, schemas
        self.snapshots, self.catalog, self.reviews = snapshots, catalog, reviews

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
            self.schemas.validate("https://featuretree.local/schema/business/v3/freeze", frozen)
            approval = self.artifacts.get(frozen["approval_ref"])
            if approval["decision"] != "approved":
                raise ValueError("Freeze approval is absent")
        articles, stale = {}, {}
        for feature_id, reference in manifest["knowledge_refs"].items():
            article = self.artifacts.get(reference)
            self.schemas.validate("https://featuretree.local/schema/business/v3/article", article)
            if article["draft"] or article["feature_id"] != feature_id:
                raise ValueError("Calibration drafts cannot be published as formal knowledge")
            if article["freeze_ref"] not in freezes:
                raise ValueError("Knowledge freeze is not referenced by the manifest")
            spec = self.artifacts.get(article["spec_ref"])
            frozen = freezes[article["freeze_ref"]]
            frozen_tree = self.artifacts.get(frozen["tree_ref"])
            original_feature = next(row for row in frozen_tree["features"] if row["id"] == feature_id)
            validate_spec(spec, original_feature)
            overall, reasons = rate_article(spec, article["claims"], article["reviews"], article["assessments"], article["evidence"])
            if overall != article["overall_confidence"] or reasons != article["confidence_reasons"]:
                raise ValueError("Article aggregate differs from deterministic rating")
            validate_evidence(article["evidence"], self.catalog, {article["snapshot_id"]}, self.artifacts.get(article["baseline_ref"]))
            causes = stale_reasons(article, nodes.get(feature_id), bindings, frozen, manifest["baseline_ref"], manifest["source_ids"])
            if causes:
                stale[feature_id] = causes
            articles[reference] = article
        projection = project_reviews(articles, self.reviews.events())
        if digest(projection) != manifest["review_projection_ref"]:
            raise ConflictError("Human review history changed; prepare a fresh review projection")
        self.artifacts.verify(manifest["review_projection_ref"])
        return {"stale_knowledge": stale, "review_invalidations": projection["invalidated_claims"],
                "feature_count": len(nodes), "leaf_count": sum(row["node_type"] == "leaf" for row in nodes.values()),
                "knowledge_count": len(articles)}

    def publish(self, key):
        return self.versions.commit(key, self.validate)

    def rollback(self, target, expected, key):
        original = self.versions.get(target)
        candidate = {**original, "kind": "rollback", "rollback_target": target}
        candidate.pop("created_at")
        self.prepare(candidate, expected, key)
        return self.publish(key)
