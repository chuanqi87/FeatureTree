"""Knowledge-stage gates and article assembly from reviewed, assessed claims."""

from featuretree.core.content import digest, timestamp
from featuretree.knowledge.claims import validate_claims, validate_evidence
from featuretree.knowledge.ratings import rate_article
from featuretree.knowledge.specifications import validate_spec
from featuretree.workflow.packaging import envelope


def collected(packet):
    claims, evidence = [], {}
    for stage in ("fk-android", "fk-ios", "fk-harmonyos", "fk-compare"):
        output = packet["upstream"].get(stage)
        if output:
            claims.extend(output["claims"])
            for row in output["evidence"]:
                if row["id"] in evidence and row != evidence[row["id"]]:
                    raise ValueError("Evidence identity collision across researchers")
                evidence[row["id"]] = row
    return claims, list(evidence.values())


class KnowledgeHandlers:
    def __init__(self, artifacts, catalog):
        self.artifacts, self.catalog = artifacts, catalog

    def validate(self, stage, response, packet):
        payload = response["payload"]
        if stage == "fk-scope":
            spec = payload["spec"]
            validate_spec(spec, packet["inputs"]["feature_ref"])
            if spec["freeze_ref"] != packet["work"]["inputs"].get("freeze_ref"):
                raise ValueError("Specification changed its pinned freeze")
            if spec["candidate_tree_ref"] != (packet["work"]["inputs"].get("tree_ref") if not spec["freeze_ref"] else None):
                raise ValueError("Calibration specification changed candidate version")
        elif stage in ("fk-android", "fk-ios", "fk-harmonyos"):
            spec = packet["upstream"]["fk-scope"]["spec"]
            platform = payload["platform"]
            scoped = {**spec, "questions": [row for row in spec["questions"]
                                            if row["platforms"] == [platform] and row["kind"] != "comparison"]}
            validate_claims(scoped, payload["claims"])
            self._evidence(payload["evidence"], packet)
        elif stage == "fk-compare":
            combined = {**packet, "upstream": {**packet["upstream"], stage: payload}}
            claims, evidence = collected(combined)
            if any(row["kind"] != "comparison" for row in payload["claims"]):
                raise ValueError("Comparison agent cannot rewrite platform facts")
            validate_claims(packet["upstream"]["fk-scope"]["spec"], claims)
            self._evidence(evidence, packet)
        elif stage == "fk-review":
            claims, _ = collected(packet)
            hashes = {row["claim_id"]: digest(row) for row in claims}
            if len(payload["reviews"]) != len(hashes) or {row["claim_id"] for row in payload["reviews"]} != set(hashes):
                raise ValueError("Independent review omitted or duplicated a conclusion")
            for row in payload["reviews"]:
                if row["claim_hash"] != hashes[row["claim_id"]]:
                    raise ValueError("Review refers to stale content")
                if row["verdict"] in ("invalid", "revise") and response["outcome"] != "revise":
                    raise ValueError("Rejected claims require an explicit revision outcome")
        elif stage == "fk-confidence":
            claims, evidence = collected(packet)
            rate_article(packet["upstream"]["fk-scope"]["spec"], claims,
                         packet["upstream"]["fk-review"]["reviews"], payload["assessments"], evidence)

    def _evidence(self, evidence, packet):
        return validate_evidence(evidence, self.catalog, {packet["work"]["snapshot_id"]},
                                 packet["inputs"]["baseline_ref"])

    def assemble(self, packet, folder):
        spec = packet["upstream"]["fk-scope"]["spec"]
        claims, evidence = collected(packet)
        reviews = packet["upstream"]["fk-review"]["reviews"]
        assessments = packet["upstream"]["fk-confidence"]["assessments"]
        self._evidence(evidence, packet)
        overall, reasons = rate_article(spec, claims, reviews, assessments, evidence)
        inputs = packet["work"]["inputs"]
        article = {"schema_version": 3, "feature_id": spec["feature_id"],
                   "spec_ref": self.artifacts.put(spec), "freeze_ref": spec["freeze_ref"],
                   "candidate_tree_ref": spec["candidate_tree_ref"], "baseline_ref": inputs["baseline_ref"],
                   "snapshot_id": packet["work"]["snapshot_id"], "claims": claims, "reviews": reviews,
                   "assessments": assessments, "evidence": evidence, "overall_confidence": overall,
                   "confidence_reasons": reasons, "dependencies": {**inputs, **packet["upstream_refs"]},
                   "draft": spec["freeze_ref"] is None, "created_at": timestamp()}
        return envelope(packet, {"article_ref": self.artifacts.put(article), "overall_confidence": overall,
                                 "confidence_reasons": reasons, "draft": article["draft"]})
