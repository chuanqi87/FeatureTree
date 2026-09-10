"""Claim completeness and evidence matching, without execution or publishing side effects."""

from featuretree.core.content import digest
from featuretree.corpus.source_policy import official_source_error
from featuretree.knowledge.specifications import question_key


def claim_hash(claim):
    return digest(claim)


def validate_claims(spec, claims):
    questions = {question["id"]: question for question in spec["questions"]}
    by_id, answered = {}, set()
    for claim in claims:
        key = claim["claim_id"]
        if key in by_id:
            raise ValueError("Duplicate claim identity")
        by_id[key] = claim
        question_id = claim["question_id"]
        if question_id not in questions or question_id in answered:
            raise ValueError("Every claim must answer a distinct registered question")
        answered.add(question_id)
        if question_key(claim) != question_key(questions[question_id]):
            raise ValueError("Claim changed the agreed platform scope or dimension")
        allowed = {"support": {"supported", "conditional", "unsupported", "unknown"},
                   "comparison": {"same", "different", "unknown", "not_applicable"},
                   "fact": {"fact", "unknown"}}[claim["kind"]]
        if claim["result"] not in allowed:
            raise ValueError("Result is incompatible with the research question")
        if claim["result"] == "unknown" and not claim["gaps"]:
            raise ValueError("Unknown requires an explicit information gap")
        if claim["result"] in ("same", "unsupported", "not_applicable"):
            if not claim["coverage_note"] or not claim["alternative_paths"]:
                raise ValueError("Same/unsupported/not-applicable requires checked scope and alternatives")
        if claim["result"] != "unknown" and not claim["evidence_refs"] and not claim["premise_ids"]:
            raise ValueError("A substantive assertion needs evidence or explicit premises")
    required = {question["id"] for question in questions.values() if question["required"]}
    if not required <= answered:
        raise ValueError("Required claims cannot be omitted to hide uncertainty")
    active, visited = set(), set()

    def visit(key):
        if key not in by_id:
            raise ValueError("Missing comparison premise")
        if key in active:
            raise ValueError("Cyclic inference premises")
        if key in visited:
            return
        active.add(key)
        for premise in by_id[key]["premise_ids"]:
            visit(premise)
        active.remove(key)
        visited.add(key)

    for key, claim in by_id.items():
        visit(key)
        if claim["kind"] == "comparison" and claim["result"] != "unknown":
            premise_platforms = {platform for premise in claim["premise_ids"]
                                 for platform in by_id[premise]["platforms"]}
            if not set(claim["platforms"]) <= premise_platforms:
                raise ValueError("Comparison must cite fixed facts from both platforms")
    return by_id


def validate_evidence(evidence, reader, allowed_snapshot_ids, baseline):
    seen = set()
    for item in evidence:
        if item["id"] in seen or item["snapshot_id"] not in allowed_snapshot_ids:
            raise ValueError("Duplicate evidence or evidence outside the fixed source snapshots")
        seen.add(item["id"])
        source = reader.get(item["snapshot_id"], "documents", item["document_id"])
        if source["platform"] != item["platform"] or source["status"] != "verified":
            raise ValueError("Evidence platform or captured-body status does not match its source")
        if source["url"] != item["url"] or source["body_sha256"] != item["body_sha256"]:
            raise ValueError("Evidence identity does not match the sealed source")
        distribution = baseline["platforms"][item["platform"]]["distribution"]
        error = official_source_error(item["url"], item["platform"], distribution)
        if error:
            raise ValueError(error)
        chunks, offset = [], 0
        while True:
            page = reader.read_body(item["snapshot_id"], item["document_id"], offset, 24000)
            chunks.append(page["text"])
            if page["next_offset"] is None:
                break
            offset = page["next_offset"]
        if item["excerpt"] not in "".join(chunks):
            raise ValueError("Evidence excerpt is absent from the hashed official body")
        if item["applicability"] == "verified" and baseline["platforms"][item["platform"]]["status"] != "verified_stable":
            raise ValueError("Historical or unknown baseline cannot certify current applicability")
    return seen
