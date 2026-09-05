"""Check candidate packages against current inputs and immutable source files."""

import gzip
import hashlib
import json
from pathlib import Path

from .corpus.context import CONTEXT_VERSION, context_input_hash
from .source_policy import ios_applicability, official_source_error
from .storage import contained_path


def context_errors(bundle, feature, config, policy, corpus, verified_files):
    errors = []
    if not isinstance(bundle, dict) or not isinstance(bundle.get("platforms"), dict):
        return ["Context package must contain a platforms object"]
    if bundle.get("feature_id") != feature["id"] or bundle.get("context_version") != CONTEXT_VERSION:
        errors.append("Missing or incompatible context package")
    if bundle.get("context_input_hash") != context_input_hash(feature, config, policy):
        errors.append("Stale context: node, bindings, comparison configuration or research policy changed")
    if bundle.get("claim_ready") is not False:
        errors.append("Candidate context must never assert claim_ready")
    if set(bundle.get("platforms", {})) != set(config["platforms"]):
        errors.append("Context platform set does not match the comparison registry")
    for platform, candidates in bundle.get("platforms", {}).items():
        if not isinstance(candidates, dict) or not isinstance(candidates.get("documents"), list):
            errors.append(f"{platform}: invalid candidate documents")
            continue
        for source in candidates.get("documents", []):
            if not isinstance(source, dict):
                errors.append(f"{platform}: invalid candidate source")
                continue
            try:
                row = corpus.get(source["url"])
                if not row or row["status"] != "ready" or row["platform"] != platform:
                    raise ValueError("Source is no longer a ready document for this platform")
                policy_error = official_source_error(row["url"], platform, platform)
                if policy_error:
                    raise ValueError(policy_error)
                for key in ("raw_sha256", "body_sha256", "fetched_at"):
                    if row[key] != source[key]:
                        raise ValueError(f"Stale source {key}; rebuild context")
                if platform == "ios" and ios_applicability(json.loads(row["metadata"])) == "explicitly_non_ios":
                    raise ValueError("Explicitly non-iOS source in iOS candidate package")
                for field, column in (("local_path", "body_path"), ("raw_path", "raw_path")):
                    expected = (corpus.root / row[column]).resolve()
                    if not expected.is_relative_to(corpus.root) or Path(source[field]).resolve() != expected:
                        raise ValueError("Context source path does not match the corpus")
                key = (row["raw_path"], row["raw_sha256"], row["body_path"], row["body_sha256"])
                if key not in verified_files:
                    body = corpus.body(row)
                    raw = gzip.decompress((corpus.root / row["raw_path"]).read_bytes())
                    if hashlib.sha256(raw).hexdigest() != row["raw_sha256"]:
                        raise ValueError("Raw response hash mismatch")
                    verified_files[key] = body.splitlines()
                lines = verified_files[key]
                for excerpt in source.get("excerpts", []):
                    start, end = excerpt["start_line"], excerpt["end_line"]
                    if not 1 <= start <= end <= len(lines) or excerpt["text"] != "\n".join(lines[start-1:end]):
                        raise ValueError("Context excerpt does not match original line range")
            except (KeyError, TypeError, ValueError, OSError, EOFError) as exc:
                errors.append(f"{platform}: {source.get('url')}: {exc}")
    return errors


def read_context(directory, fid):
    path = contained_path(Path(directory), fid + ".json", ".")
    return json.loads(path.read_text(encoding="utf-8"))
