"""One validation boundary for consumers of authored knowledge."""

from .evidence import validate_knowledge_evidence
from .storage import ROOT
from .validation import schema_validators, validate_tree


def knowledge_errors(repo, features, knowledge, paths, config):
    validators = schema_validators(ROOT)
    errors = []
    for kind, records in (("feature", features), ("knowledge", knowledge)):
        for fid, record in records.items():
            for error in validators[kind].iter_errors(record):
                errors.append(f"SCHEMA {kind} {fid} {'.'.join(map(str, error.absolute_path))}: {error.message}")
    if not errors:
        errors.extend(validate_tree(features, knowledge, paths, config))
    if not errors:
        errors.extend(validate_knowledge_evidence(features, knowledge, config["platforms"], repo.root))
    return errors


def require_valid_knowledge(repo, features, knowledge, paths, config):
    errors = knowledge_errors(repo, features, knowledge, paths, config)
    if errors:
        raise ValueError("知识数据校验失败：\n" + "\n".join(errors))
