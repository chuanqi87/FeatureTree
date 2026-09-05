"""Validate a launch-date baseline without guessing current platform releases."""

from datetime import date
import json

from .evidence import confirmed_claim_errors, snapshot_errors
from .research_profile import fingerprint
from .storage import ROOT
from .validation import schema_validators


def baseline_errors(repo, config, policy, run_date):
    path = repo.root / "output/research/baseline.json"
    if not path.exists():
        return [f"Official stable release/SDK baseline for {run_date} has not been resolved: {path.relative_to(repo.root)}"]
    try:
        baseline = json.loads(path.read_text(encoding="utf-8"))
        errors = []
        if baseline.get("run_date") != run_date or baseline.get("policy_hash") != fingerprint(policy):
            errors.append("Run baseline date or research policy changed; resolve the official versions again")
        cells = baseline.get("platforms", {})
        if set(cells) != set(config["platforms"]):
            errors.append("Run baseline must resolve every configured platform")
        validator = schema_validators(ROOT)["knowledge"]
        for platform, cell in cells.items():
            if cell.get("release_channel") != "stable" or not cell.get("latest_stable_rationale", "").strip():
                errors.append(f"{platform}: baseline needs stable release channel and latest_stable_rationale")
            if cell.get("verified_at") != run_date or not cell.get("verified_by", "").strip():
                errors.append(f"{platform}: baseline must be reviewed on the run date")
            date.fromisoformat(cell.get("verified_at", ""))
            context = cell.get("context", {})
            if context.get("device_forms") != policy["primary_device_forms"]:
                errors.append(f"{platform}: baseline device forms do not match the research policy")
            if str(context.get("distribution", "")).casefold() != platform.casefold():
                errors.append(f"{platform}: baseline distribution must match the platform")
            sources = cell.get("evidence", [])
            evidence = {source["id"]: source for source in sources}
            if len(evidence) != len(sources):
                errors.append(f"{platform}: duplicate baseline evidence ids")
            for source in sources:
                errors.extend(f"{platform}: {error.message}" for error in validator.evolve(
                    schema={"$ref": "https://featuretree.local/schema/comparison.schema.json#/$defs/evidence"}).iter_errors(source))
                errors.extend(f"{platform}: {error}" for error in snapshot_errors(source, repo.root))
            errors.extend(f"{platform}: {error.message}" for error in validator.evolve(
                schema={"$ref": "https://featuretree.local/schema/comparison.schema.json#/$defs/context"}).iter_errors(context))
            claim = {"basis": "official_statement", "evidence_refs": list(evidence)}
            errors.extend(confirmed_claim_errors(claim, [platform], {platform: {"context": context}}, evidence))
        if not errors:
            knowledge, _ = repo.knowledge()
            for fid, doc in knowledge.items():
                for platform, presence in doc["presence"].items():
                    relevant = presence["verification"] == "confirmed" or any(
                        finding["verification"] == "confirmed" and platform in finding["platforms"]
                        for finding in doc["comparisons"]) or any(
                        fact["verification"] == "confirmed" and fact["platform"] == platform
                        for fact in doc.get("facts", []))
                    if not relevant:
                        continue
                    context = presence.get("context", {})
                    expected = cells[platform]["context"]
                    for key in ("release", "sdk", "distribution", "device_forms"):
                        if context.get(key) != expected[key]:
                            errors.append(f"{fid}: confirmed {platform} {key} does not match the run baseline")
        return errors
    except (ValueError, OSError, KeyError, TypeError, AttributeError) as exc:
        return [f"Invalid run baseline: {exc}"]
