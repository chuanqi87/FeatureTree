"""Append-only human decisions, tied to exact article and claim versions."""

from featuretree.core.content import digest, identifier, timestamp
from featuretree.core.io import ConflictError, file_lock, read_json, write_json
from featuretree.knowledge.claims import claim_hash


def ticket_id(article_ref):
    return "review_" + digest(article_ref)


class ReviewLedger:
    def __init__(self, directory, artifacts, schemas):
        self.directory, self.artifacts, self.schemas = directory, artifacts, schemas

    def events(self):
        result, previous = [], None
        for path in sorted(self.directory.glob("events/*.json")):
            record = read_json(path)
            event = self.artifacts.get(record["event_ref"])
            if event["previous_event_ref"] != previous:
                raise ValueError("Human review event chain is incomplete or reordered")
            previous = record["event_ref"]
            result.append(event)
        return result

    def prior_request(self, article_ref, decision, key):
        identifier(key)
        allowed = {"claim_id", "claim_hash", "action", "reason", "actor", "evidence_refs", "target_stage", "replacement"}
        if set(decision) != allowed:
            raise ValueError("A human decision cannot change event identity, history or target article metadata")
        fingerprint = digest({"article_ref": article_ref, "decision": decision})
        path = self.directory / "requests" / f"{key}.json"
        if path.exists():
            receipt = read_json(path)
            if receipt["request_hash"] != fingerprint:
                raise ConflictError("Human decision key reused with different content")
            return receipt
        event_id = "human_" + digest(key)
        event = next((row for row in self.events() if row["event_id"] == event_id), None)
        if event:
            if event["article_ref"] != article_ref or any(event[field] != value for field, value in decision.items()):
                raise ConflictError("Recorded human event differs from retry")
            return {"request_hash": fingerprint, "event_id": event_id, "event_ref": digest(event), "ticket_id": event["ticket_id"]}
        return None

    def append(self, article_ref, current_article_ref, decision, key):
        identifier(key)
        with file_lock(self.directory / "review.lock"):
            prior = self.prior_request(article_ref, decision, key)
            if prior:
                write_json(self.directory / "requests" / f"{key}.json", prior, immutable=True)
                return prior
            receipt_path = self.directory / "requests" / f"{key}.json"
            request_hash = digest({"article_ref": article_ref, "decision": decision})
            if current_article_ref != article_ref:
                raise ConflictError("Knowledge version changed; inspect the current version before submitting")
            article = self.artifacts.get(article_ref)
            claims = {row["claim_id"]: row for row in article["claims"]}
            claim = claims.get(decision["claim_id"])
            if claim is None or claim_hash(claim) != decision["claim_hash"]:
                raise ConflictError("Claim fingerprint changed")
            events = self.events()
            event_id = "human_" + digest(key)
            previous = digest(events[-1]) if events else None
            event = {"schema_version": 3, "event_id": event_id, "ticket_id": ticket_id(article_ref),
                     "article_ref": article_ref, "created_at": timestamp(),
                     "previous_event_ref": previous, **decision}
            self.schemas.validate("https://featuretree.local/schema/business/v3/review-event", event)
            reference = self.artifacts.put(event)
            write_json(self.directory / "events" / f"{len(events)+1:012d}.json",
                       {"event_ref": reference}, immutable=True)
            receipt = {"request_hash": request_hash, "event_ref": digest(event),
                       "ticket_id": event["ticket_id"], "event_id": event["event_id"]}
            write_json(receipt_path, receipt, immutable=True)
            return receipt


def project_reviews(articles, events):
    latest, rejected = {}, set()
    for event in events:
        latest[(event["article_ref"], event["claim_id"])] = event
        if event["action"] in ("correct", "request_research"):
            rejected.add((event["claim_id"], event["claim_hash"]))
    tickets = []
    invalidated = []
    for reference, article in articles.items():
        items = []
        for claim in article["claims"]:
            event = latest.get((reference, claim["claim_id"]))
            invalid = (claim["claim_id"], claim_hash(claim)) in rejected
            if invalid:
                invalidated.append({"article_ref": reference, "claim_id": claim["claim_id"]})
            if article["overall_confidence"] != "low" and not invalid:
                continue
            action = event["action"] if event else None
            state = {"start": "in_review", "defer": "deferred", "accept_limitations": "decided",
                     "unknown": "decided", "correct": "research_requested",
                     "add_evidence": "research_requested", "request_research": "research_requested"}.get(action, "pending")
            items.append({"claim_id": claim["claim_id"], "claim_hash": claim_hash(claim),
                          "state": state, "invalidated": invalid, "last_event": event})
        if items:
            state = next((state for state in ("research_requested", "in_review", "pending", "deferred")
                          if any(item["state"] == state for item in items)), "decided")
            tickets.append({"id": ticket_id(reference), "article_ref": reference,
                            "feature_id": article["feature_id"], "draft": article["draft"], "state": state, "items": items})
    return {"tickets": tickets, "invalidated_claims": invalidated,
            "event_head": digest(events[-1]) if events else None, "event_count": len(events)}
