"""Revalidate committed research when only execution policy changes between runs."""

from featuretree.workflow.batch_packets import research_identity

from featuretree.core.io import IntegrityError
from featuretree.workflow.packaging import envelope


def revalidate_checkpoint(receipt, packet, artifacts, handlers):
    from featuretree.workflow.batch_execution import verify_receipt
    original = artifacts.get(receipt["input_ref"])
    response = verify_receipt(receipt, original, artifacts, handlers)
    if research_identity(original) != research_identity(packet):
        raise IntegrityError("Checkpoint research inputs changed; execution-policy reuse is not allowed")
    adapted = envelope(packet, response["payload"], response["outcome"], response["issues"])
    adapted["source_requests"] = response["source_requests"]
    metadata = {"validation": "accepted", "input_hash": packet["input_hash"],
                "executor": "execution_policy_checkpoint_revalidation", "usage": [],
                "original_receipt": receipt}
    result = {"input_hash": packet["input_hash"], "input_ref": artifacts.put(packet),
              "result_ref": artifacts.put(adapted), "metadata_ref": artifacts.put(metadata),
              "origin": receipt["origin"]}
    verify_receipt(result, packet, artifacts, handlers)
    return result
