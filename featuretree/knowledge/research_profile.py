"""Persisted research policy; concrete versions must be resolved from official sources."""

import hashlib
import json

from featuretree.core.storage import read_yaml


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def research_policy(repo):
    path = repo.root / "config/research.yaml"
    return read_yaml(path) if path.exists() else {}


def policy_errors(policy):
    expected = {
        "schema_version": 1,
        "version_policy": "latest_stable_on_run_date",
        "other_device_forms": "separate_findings",
        "preview_releases": "exclude_from_primary_comparison",
        "ecosystem_versions": "pin_per_node",
        "distribution_policy": "separate_harmonyos_and_openharmony",
        "baseline_resolution": "read_official_release_sources_at_run_start",
    }
    errors = [f"Research policy {key} must be {value!r}" for key, value in expected.items()
              if policy.get(key) != value]
    forms = policy.get("primary_device_forms")
    if not isinstance(forms, list) or not forms or any(not isinstance(form, str) or not form.strip() for form in forms):
        errors.append("Research policy needs explicit primary_device_forms")
    return errors
