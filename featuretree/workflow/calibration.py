"""Record an explicit human calibration decision against concrete reviewable artifacts."""

from featuretree.core.content import digest, timestamp
from featuretree.core.io import ConflictError, file_lock, read_json, write_json
from featuretree.knowledge.ratings import rate_article
from featuretree.knowledge.observations import validate_observation
from featuretree.taxonomy.model import validate_tree


class CalibrationService:
    def __init__(self, directory, artifacts, schemas):
        self.directory, self.artifacts, self.schemas = directory, artifacts, schemas

    def list(self):
        return [read_json(path) for path in sorted(self.directory.glob("*.json"))]

    def approve(self, request, key):
        path = self.directory / f"{digest(key)}.json"
        with file_lock(path.with_suffix(".lock")):
            if path.exists():
                receipt = read_json(path)
                if receipt["request_hash"] != digest(request):
                    raise ConflictError("Calibration decision key was reused")
                return receipt
            nodes = validate_tree(self.artifacts.get(request["tree_ref"]))
            if not request["sample_article_refs"] or not request["scope_ids"] or not set(request["scope_ids"]) <= set(nodes):
                raise ValueError("Approval needs a concrete skeleton, scope and representative knowledge samples")
            for reference in request["sample_article_refs"]:
                article = self.artifacts.get(reference)
                self.schemas.validate("https://featuretree.local/schema/business/v3/article", article)
                if not article["draft"] or article["candidate_tree_ref"] != request["tree_ref"]:
                    raise ValueError("Calibration sample does not belong to the reviewed candidate tree")
                result = rate_article(self.artifacts.get(article["spec_ref"]), article["claims"], article["reviews"],
                                      article["assessments"], article["evidence"], article["rating_context"],
                                      {ref: validate_observation(self.artifacts.get(ref), self.artifacts) for ref in article["observation_refs"]})
                if result != (article["overall_confidence"], article["confidence_reasons"]):
                    raise ValueError("Calibration sample rating is inconsistent")
            for name in ("granularity_policy_ref", "confidence_policy_ref"):
                policy = self.artifacts.get(request[name])
                if not policy.get("id"):
                    raise ValueError("Calibration policy needs a versioned identity")
            approval = {**request, "schema_version": 3, "created_at": timestamp(), "id": "calibration_" + digest(key)}
            self.schemas.validate("https://featuretree.local/schema/business/v3/calibration-approval", approval)
            receipt = {"approval_ref": self.artifacts.put(approval), "request_hash": digest(request), "approval": approval}
            write_json(path, receipt, immutable=True)
            return receipt
