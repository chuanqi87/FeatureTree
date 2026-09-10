"""SDK file inventory and deterministic extraction; every selected file has a disposition."""

from pathlib import Path
from collections import Counter

from featuretree.core.content import digest, file_digest
from featuretree.core.io import IntegrityError, write_bytes
from featuretree.corpus.extractors.android import extract as android_xml
from featuretree.corpus.extractors.native import extract as native_headers
from featuretree.corpus.extractors.syntax import arkts, swift
from featuretree.corpus.identity import declaration_id

ADAPTERS = {"android-xml": android_xml, "native": native_headers, "arkts": arkts, "swift": swift}


def extract_sdk(project_root, request, snapshot_store):
    adapter = request["adapter"]
    if adapter not in ADAPTERS:
        raise ValueError("Unknown registered SDK extraction adapter")
    sdk_root = Path(request["sdk_root"]).resolve()
    files = sorted({path for pattern in request["patterns"] for path in sdk_root.glob(pattern) if path.is_file()})
    if not files:
        raise ValueError("No SDK files match the explicit inventory selection")
    for path in files:
        if not path.resolve().is_relative_to(sdk_root):
            raise ValueError("SDK inventory escapes its registered root")
    options = {**request, "sdk_root": sdk_root, "project_root": project_root}
    declarations, ledger, gaps, originals, retained_files = {}, [], [], [], []
    for path in files:
        relative = str(path.relative_to(sdk_root))
        source_hash = file_digest(path)
        retained = project_root / "data/imports/sdk" / source_hash / path.name
        write_bytes(retained, path.read_bytes(), immutable=True)
        if file_digest(retained) != source_hash:
            raise IntegrityError("SDK source changed while archiving; extraction stopped")
        retained_files.append({"path": str(retained.relative_to(project_root)), "sha256": source_hash})
        try:
            records, errors = ADAPTERS[adapter](path, options)
        except (ValueError, OSError, RuntimeError) as error:
            records, errors = [], [f"{type(error).__name__}: {error}"]
        for record in records:
            identity = declaration_id(request["platform"], request["distribution"], request["language"],
                                      record["qualified_name"], record["signature"])
            declaration = {"schema_version": 3, "id": identity, "platform": request["platform"],
                           "distribution": request["distribution"], "language": request["language"],
                           "sdk_version": request["sdk_version"], "source_path": relative,
                           "source_hash": source_hash, "original_id": identity,
                           "evidence_refs": [], **record}
            if identity in declarations:
                originals.append({"id": identity, "path": relative, "source_hash": source_hash,
                                  "record": declaration, "status": "alias_or_redeclaration_requires_audit"})
            else:
                declarations[identity] = declaration
        ledger.append({"path": relative, "sha256": source_hash, "bytes": path.stat().st_size,
                       "status": "failed" if errors else "extracted", "reason": "; ".join(errors)})
        if file_digest(path) != source_hash:
            raise IntegrityError("SDK source changed during extraction")
        if errors:
            gaps.append({"id": "source_gap_" + digest(relative), "kind": "source", "severity": "blocking",
                         "target_stage": "sources", "subject_ids": [relative], "reason": "; ".join(errors),
                         "evidence_refs": []})
    families = [{"id": "family_" + digest(key), "declaration_ids": [key],
                 "basis": "One canonical declaration; language/overload aliases not presumed",
                 "evidence_refs": [], "unresolved_aliases": [row["path"] for row in originals if row["id"] == key]}
                for key in declarations]
    manifest = snapshot_store.seal({"declarations": declarations.values(), "families": families}, files=ledger,
                                   status="candidate", baseline_ref=request.get("baseline_ref"),
                                   extractor_versions={adapter: "1"}, gaps=gaps,
                                   provenance={"sdk_root": str(sdk_root), "patterns": request["patterns"],
                                               "retained_files": retained_files,
                                               "adapter_options": request, "duplicate_records": originals,
                                               "visibility_counts": dict(Counter(row["visibility"] for row in declarations.values()))})
    return manifest
