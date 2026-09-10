"""Validate a complete article without changing facts, review history or publication."""

from featuretree.knowledge.claims import validate_evidence
from featuretree.knowledge.observations import validate_observation
from featuretree.knowledge.ratings import rate_article
from featuretree.knowledge.specifications import validate_spec
from featuretree.workflow.article_provenance import validate_article_provenance


def validate_article(article, artifacts, schemas, catalog, provenance):
    schemas.validate("https://featuretree.local/schema/business/v3/article", article)
    validate_article_provenance(article, artifacts, provenance)
    spec = artifacts.get(article["spec_ref"])
    tree_ref = (artifacts.get(article["freeze_ref"])["tree_ref"] if article["freeze_ref"] else article["candidate_tree_ref"])
    feature = next((row for row in artifacts.get(tree_ref)["features"] if row["id"] == article["feature_id"]), None)
    if feature is None:
        raise ValueError("Article feature is absent from its frozen or candidate tree")
    validate_spec(spec, feature)
    context = article["rating_context"]
    if context["snapshot_id"] != article["snapshot_id"] or context["inputs"]["baseline_ref"] != article["baseline_ref"]:
        raise ValueError("Article rating context differs from its dependency version")
    observations = {ref: validate_observation(artifacts.get(ref), artifacts) for ref in article["observation_refs"]}
    overall, reasons = rate_article(spec, article["claims"], article["reviews"], article["assessments"], article["evidence"], context, observations)
    if (overall, reasons) != (article["overall_confidence"], article["confidence_reasons"]):
        raise ValueError("Article aggregate differs from deterministic rating")
    validate_evidence(article["evidence"], catalog, {article["snapshot_id"]}, artifacts.get(article["baseline_ref"]))
    return {"valid": True, "overall_confidence": overall, "confidence_reasons": reasons, "draft": article["draft"]}
