"""Explicit schema identities; runtime never guesses a protocol from file names."""

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

from featuretree.core.io import read_json


class SchemaRegistry:
    def __init__(self, directory):
        schemas = [read_json(path) for path in sorted(directory.rglob("*.schema.json"))]
        self.schemas = {}
        for schema in schemas:
            Draft202012Validator.check_schema(schema)
            key = schema["$id"]
            if key in self.schemas:
                raise ValueError(f"Duplicate schema identity: {key}")
            self.schemas[key] = schema
        registry = Registry().with_resources(
            (key, Resource.from_contents(value)) for key, value in self.schemas.items())
        self.validators = {key: Draft202012Validator(value, registry=registry,
                                                   format_checker=FormatChecker())
                           for key, value in self.schemas.items()}

    def validate(self, schema_id, value):
        if schema_id not in self.validators:
            raise ValueError(f"Unregistered schema: {schema_id}")
        errors = sorted(self.validators[schema_id].iter_errors(value), key=lambda e: str(e.path))
        if errors:
            raise ValueError("; ".join(f"{schema_id} /{'/'.join(map(str, e.path))}: {e.message}"
                                       for e in errors[:12]))

    def get(self, schema_id):
        return self.schemas[schema_id]

    def expanded(self, schema_id):
        def expand(value):
            if isinstance(value, list):
                return [expand(item) for item in value]
            if not isinstance(value, dict):
                return value
            if "$ref" in value:
                return expand(self.schemas[value["$ref"]])
            return {key: expand(item) for key, item in value.items() if key != "$id"}
        return expand(self.get(schema_id))
