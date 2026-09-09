"""Load JSON Schemas and validate authored records without orchestration."""

import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource
from featuretree.core.paths import SCHEMA_DIR


def schema_validators(root: Path):
    schemas = {p.stem.split(".")[0]: json.loads(p.read_text(encoding="utf-8"))
               for p in (root / SCHEMA_DIR).glob("*.schema.json")}
    registry = Registry().with_resources(
        (s["$id"], Resource.from_contents(s)) for s in schemas.values())
    for schema in schemas.values():
        Draft202012Validator.check_schema(schema)
    return {name: Draft202012Validator(s, registry=registry, format_checker=FormatChecker())
            for name, s in schemas.items()}


def validate_schemas(validators, features, knowledge):
    errors = []
    groups = [("feature", features.items()), ("knowledge", knowledge.items())]
    for kind, records in groups:
        for key, record in records:
            for error in validators[kind].iter_errors(record):
                location = ".".join(map(str, error.absolute_path))
                errors.append(f"SCHEMA {kind} {key} {location}: {error.message}")
    return errors
