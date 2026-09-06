"""Coordinator-owned review records bound to current, machine-checked artifacts."""

import argparse
import json

from .research_contract import file_hash
from .research_probe import check_probe
from .research_profile import fingerprint
from .research_review import review_errors, review_template
from .research_tasks import check_task, load_task
from .storage import Repository, contained_path, read_yaml, write_json, write_text

REVIEWS_DIR = "output/research/acceptance"


def inspect_submission(repo, path):
    path = contained_path(repo.root, str(path), "output/research")
    if path.name == "probe.json":
        check = check_probe(repo, path)
        package = read_yaml(path)
        passed = check["response_contract_valid"]
        package_id = package["probe_id"]
    elif path.name == "task.json":
        package = load_task(repo, path)
        check = check_task(repo, path)
        passed = check.get("structurally_valid", check.get("delivery_valid", False))
        package_id = package["task_id"]
    else:
        raise ValueError("Select a task.json or probe.json package")
    if not passed:
        raise ValueError("Machine checks failed; fix delivery before requesting content acceptance")
    contract = package.get("handoff")
    if not contract or contract.get("schema_version") != 1:
        raise ValueError("Historical package lacks standardized acceptance; prepare a new task")
    artifacts = {name: file_hash(contained_path(path.parent, name, ".")) for name in contract["outputs"]}
    if any(value is None for value in artifacts.values()):
        raise ValueError("Required artifact is missing")
    binding = {"package_id": package_id, "package_sha256": file_hash(path),
               "inputs_hash": fingerprint(package["inputs"]), "artifact_sha256": artifacts,
               "handoff_hash": fingerprint(contract)}
    return binding, contract


def snapshot_submission(repo, path, binding):
    """Preserve exact UTF-8 artifacts before a revision replaces working copies."""
    path = contained_path(repo.root, str(path), "output/research")
    directory = repo.root / REVIEWS_DIR / "submissions" / fingerprint(binding)
    files = {path.name: binding["package_sha256"], **binding["artifact_sha256"]}
    for name, expected in files.items():
        source = contained_path(path.parent, name, ".")
        destination = contained_path(directory, name, ".")
        if file_hash(source) != expected:
            raise ValueError("Submission changed during review initialization")
        if destination.exists() and file_hash(destination) != expected:
            raise ValueError("Archived submission was altered; do not overwrite")
        write_text(destination, source.read_bytes().decode("utf-8"))
        if file_hash(destination) != expected:
            raise ValueError("Submission archive hash mismatch")
    write_json(directory / "binding.json", binding)
    return directory


def initialize_review(repo, package_path, author_id, reviewer_id):
    binding, contract = inspect_submission(repo, package_path)
    review = review_template(binding, contract, author_id, reviewer_id)
    snapshot_submission(repo, package_path, binding)
    review_id = fingerprint({"binding": binding, "author_id": author_id, "reviewer_id": reviewer_id})
    path = repo.root / REVIEWS_DIR / review_id / "review.json"
    if not path.exists():
        write_json(path, review)
    return path


def check_acceptance(repo, package_path, review_path):
    binding, contract = inspect_submission(repo, package_path)
    path = contained_path(repo.root, str(review_path), REVIEWS_DIR)
    review = read_yaml(path)
    errors = review_errors(review, binding, contract)
    accepted = not errors and review["decision"] == "pass"
    result = {"binding": binding, "review_sha256": file_hash(path), "review_record_valid": not errors,
              "content_accepted": accepted, "production_accepted": False, "errors": errors,
              "state": "invalid_review" if errors else {
                  "pending": "awaiting_review", "pass": "content_accepted", "revise": "needs_revision",
                  "blocked": "blocked"}[review["decision"]]}
    directory = path.parent / "checks" / fingerprint(result)
    write_json(directory / "result.json", result)
    write_text(directory / "review.json", path.read_bytes().decode("utf-8"))
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    init = commands.add_parser("init")
    init.add_argument("package")
    init.add_argument("--author-id", required=True)
    init.add_argument("--reviewer-id", required=True)
    check = commands.add_parser("check")
    check.add_argument("package")
    check.add_argument("review")
    args = parser.parse_args(argv)
    repo = Repository()
    try:
        if args.command == "init":
            print(initialize_review(repo, args.package, args.author_id, args.reviewer_id))
            return 0
        result = check_acceptance(repo, args.package, args.review)
        print(json.dumps(result, ensure_ascii=False))
        return 0 if result["content_accepted"] else 2
    except (ValueError, OSError, KeyError, TypeError, AttributeError, IndexError) as exc:
        print(json.dumps({"content_accepted": False, "production_accepted": False, "error": str(exc)}))
        return 2
