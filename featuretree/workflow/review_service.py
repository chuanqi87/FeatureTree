"""Human decisions schedule targeted revisions and preserve ratings until re-assessment."""

from typing import Protocol

from featuretree.core.content import digest
from featuretree.core.io import ConflictError, read_json, write_json


class ReviewService(Protocol):
    def submit(self, article_ref: str, current_ref: str, decision: dict, key: str) -> dict: ...


class LocalReviewService:
    def __init__(self, ledger, artifacts, runner, releases, structure_revisions):
        self.ledger, self.artifacts, self.runner, self.releases = ledger, artifacts, runner, releases
        self.structure_revisions = structure_revisions

    def submit(self, article_ref, current_ref, decision, key):
        prior = self.ledger.prior_request(article_ref, decision, key)
        if prior:
            existing_effect = self.ledger.directory / "effects" / f"{prior['event_id']}.json"
            if existing_effect.exists():
                return read_json(existing_effect)
        article = self.artifacts.get(article_ref)
        current = self.releases.versions.pin()
        changed = not article["draft"] and current and current["knowledge_refs"].get(article["feature_id"]) != article_ref
        if article["draft"]:
            origin = self.artifacts.get(article["dependencies"]["fk-scope"])
            _, state = self.runner.runs.load(origin["run_id"])
            assembled = state["tasks"][origin["work_id"] + "--fk-assemble"]["result_ref"]
            changed = not assembled or self.artifacts.get(assembled)["payload"]["article_ref"] != article_ref
        if changed:
            if not prior:
                raise ConflictError("Knowledge changed or is being revised; review its current version")
            # A prior event survived a crash. Do not revise a superseding article or
            # issue a second revision after the first one already invalidated it.
            result = {**prior, "confidence_changed": False, "revision": None,
                      "effect_status": "target_superseded", "reason": "Recorded decision retained; current knowledge was not overwritten"}
            write_json(existing_effect, result, immutable=True)
            return result
        receipt = self.ledger.append(article_ref, current_ref, decision, key)
        effect_path = self.ledger.directory / "effects" / f"{receipt['event_id']}.json"
        if effect_path.exists():
            return read_json(effect_path)
        result = {**receipt, "confidence_changed": False, "revision": None}
        if decision["action"] in ("correct", "request_research", "add_evidence"):
            claim = next(row for row in article["claims"] if row["claim_id"] == decision["claim_id"])
            target = decision.get("target_stage") or ("fk-compare" if claim["kind"] == "comparison"
                                                     else "fk-" + claim["platforms"][0])
            source_response = self.artifacts.get(article["dependencies"]["fk-scope"])
            run_id, work_id = source_response["run_id"], source_response["work_id"]
            _, state = self.runner.runs.load(run_id)
            task_id = work_id + "--" + target
            if target.startswith("ft-"):
                result["revision"] = self.structure_revisions.create(article_ref, receipt["event_ref"], decision)
            else:
                if task_id not in state["tasks"]:
                    raise ValueError("Human re-research target is not part of this knowledge pipeline")
                marker = receipt["event_ref"]
                if not any(item.get("human_event_ref") == marker for item in state["tasks"][task_id]["feedback"]):
                    self.runner.action(run_id, "revise", task_id=task_id,
                                       feedback=[{"human_event_ref": marker, **decision}])
                result["revision"] = {"run_id": run_id, "task_id": task_id, "status": "planned"}
        current = self.releases.versions.pin()
        if current and article_ref in current["knowledge_refs"].values():
            candidate = {**current}
            candidate.pop("created_at")
            publication_key = "review_" + digest(receipt["event_id"])[:32]
            self.releases.prepare(candidate, current["release_id"], publication_key)
            result["publication"] = self.releases.publish(publication_key)
        write_json(effect_path, result, immutable=True)
        return result
