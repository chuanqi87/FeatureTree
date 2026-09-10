"""Reconstruct publication assertions from accepted independent knowledge deliveries."""

from featuretree.core.content import digest


def validate_article_provenance(article, artifacts, provenance):
    stages = ("fk-scope", "fk-android", "fk-ios", "fk-harmonyos", "fk-compare", "fk-review", "fk-confidence")
    deliveries, packets = {}, {}
    for stage in stages:
        reference = article["dependencies"][stage]
        deliveries[stage], packets[stage] = provenance.require(reference, stage)
    origin = deliveries["fk-scope"]
    for stage, packet in packets.items():
        if (packet["run_id"], packet["work_id"]) != (origin["run_id"], origin["work_id"]):
            raise ValueError("Knowledge deliveries were combined from different research work units")
        if packet["work"]["inputs"] != article["rating_context"]["inputs"] or packet["work"]["snapshot_id"] != article["snapshot_id"]:
            raise ValueError("Knowledge stage used a different fixed feature, baseline or source context")
        if any(article["dependencies"].get(name) != ref for name, ref in packet["upstream_refs"].items()):
            raise ValueError("Knowledge stage did not consume the published upstream delivery versions")
        if not article["draft"] and not packet.get("implementation_files"):
            raise ValueError("Formal knowledge requires pinned executable provenance")
    if digest(deliveries["fk-scope"]["payload"]["spec"]) != article["spec_ref"]:
        raise ValueError("Article specification differs from its accepted scope delivery")
    claims, evidence = [], {}
    for stage in ("fk-android", "fk-ios", "fk-harmonyos", "fk-compare"):
        payload = deliveries[stage]["payload"]
        claims.extend(payload["claims"])
        for item in payload["evidence"]:
            if item["id"] in evidence and evidence[item["id"]] != item:
                raise ValueError("Evidence identity collision in article provenance")
            evidence[item["id"]] = item
    if claims != article["claims"] or list(evidence.values()) != article["evidence"]:
        raise ValueError("Published assertions differ from accepted platform or comparison deliveries")
    for stage, key in (("fk-review", "reviews"), ("fk-confidence", "assessments")):
        if deliveries[stage]["payload"][key] != article[key]:
            raise ValueError("Published review or rating was changed outside its responsible stage")
    confidence_packet = packets["fk-confidence"]
    if confidence_packet["rating_context"] != article["rating_context"]:
        raise ValueError("Article rating inputs differ from the independent assessment attempt")
    refs = confidence_packet["inputs"].get("observations_ref", {}).get("observation_refs", [])
    if sorted(refs) != article["observation_refs"]:
        raise ValueError("Article execution observations were changed after assessment")
    return True
