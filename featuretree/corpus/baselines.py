"""Release/SDK provenance checks independent from knowledge conclusions."""

from featuretree.corpus.source_policy import official_source_error


def validate_declaration_baseline(declarations, baseline):
    for declaration in declarations:
        entry = baseline["platforms"][declaration["platform"]]
        versions = entry.get("sdk_components", [entry["sdk"]])
        if declaration["sdk_version"] not in versions:
            raise ValueError("API declaration SDK version differs from the fixed stable baseline")
        if declaration["visibility"] != "public":
            raise ValueError("A bound formal API must have verified public visibility")


def validate_baseline(baseline, artifacts, reader):
    for platform, entry in baseline["platforms"].items():
        if entry["status"] != "verified_stable" or not entry["verified_at"] or not entry["evidence_refs"]:
            raise ValueError("A formal baseline requires dated stable release and SDK verification")
        for reference in entry["evidence_refs"]:
            evidence = artifacts.get(reference)
            if evidence["platform"] != platform:
                raise ValueError("Baseline evidence belongs to another platform")
            error = official_source_error(evidence["url"], platform, entry["distribution"])
            if error:
                raise ValueError(error)
            source = reader.get(evidence["snapshot_id"], "documents", evidence["document_id"])
            if source["url"] != evidence["url"] or source["body_sha256"] != evidence["body_sha256"]:
                raise ValueError("Baseline evidence identity differs from the sealed official body")
            chunks, offset = [], 0
            while True:
                page = reader.read_body(evidence["snapshot_id"], evidence["document_id"], offset, 24000)
                chunks.append(page["text"])
                if page["next_offset"] is None:
                    break
                offset = page["next_offset"]
            if not evidence["excerpt"] or evidence["excerpt"] not in "".join(chunks):
                raise ValueError("Baseline quotation is not present in the official source")
