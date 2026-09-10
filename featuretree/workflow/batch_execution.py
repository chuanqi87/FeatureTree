"""Sequential bounded model calls with verified, retryable research checkpoints."""

from jsonschema import Draft202012Validator

from featuretree.core.content import timestamp
from featuretree.core.io import IntegrityError, read_json, write_json
from featuretree.workflow.backends.monitor import ExecutionInterrupted
from featuretree.workflow.batch_packets import merge_research


class BatchExecutionError(ValueError):
    retryable = False


def verify_receipt(receipt, packet, artifacts, handlers=None):
    stored = artifacts.get(receipt["input_ref"])
    if stored != packet or receipt["input_hash"] != packet["input_hash"]:
        raise IntegrityError("Checkpoint input differs from the fixed batch")
    response = artifacts.get(receipt["result_ref"])
    metadata = artifacts.get(receipt["metadata_ref"])
    if metadata.get("validation") != "accepted" or metadata.get("input_hash") != packet["input_hash"]:
        raise IntegrityError("Checkpoint has no accepted batch validation")
    for key in ("protocol_version", "run_id", "work_id", "task_id", "stage_id", "input_hash"):
        if response[key] != packet[key]:
            raise IntegrityError("Checkpoint response identity mismatch")
    Draft202012Validator(packet["output_schema"]).validate(response)
    if handlers:
        handlers.validate(packet["stage_id"], response, packet)
    if metadata.get("original_receipt"):
        from featuretree.workflow.batch_packets import research_identity
        origin = metadata["original_receipt"]
        original_packet = artifacts.get(origin["input_ref"])
        original = verify_receipt(origin, original_packet, artifacts, handlers)
        if research_identity(original_packet) != research_identity(packet) or any(
                original[key] != response[key] for key in ("payload", "outcome", "issues", "source_requests")):
            raise IntegrityError("Revalidated checkpoint differs from its original research")
    return response


class BatchExecutor:
    def __init__(self, artifacts, handlers, execute_single):
        self.artifacts, self.handlers, self.execute_single = artifacts, handlers, execute_single

    def execute(self, plan, task, packet, batches, folder):
        run_folder = folder.parents[2]
        receipts, responses, fresh, reused = [], [], [], 0
        progress = {"total": len(batches), "completed": 0, "reused": 0, "status": "running"}

        def report(**changes):
            progress.update(changes, updated_at=timestamp())
            write_json(folder / "batch-progress.json", progress)

        for index, batch in enumerate(batches):
            if (run_folder / "CANCEL.json").exists():
                report(status="cancelled")
                raise ExecutionInterrupted("Cancelled before starting the next research batch")
            report(current=index + 1, api_count=len(batch["work"]["api_ids"]),
                   topic_count=len(batch["work"]["topic_ids"]))
            checkpoint = run_folder / "batch-checkpoints" / task["id"] / (batch["input_hash"] + ".json")
            try:
                if checkpoint.exists():
                    receipt = read_json(checkpoint)
                    response = verify_receipt(receipt, batch, self.artifacts, self.handlers)
                    reused += 1
                else:
                    directory = folder / "batches" / f"{index:04d}"
                    reference, metadata = self.execute_single(plan, task, batch, directory)
                    receipt = {"input_hash": batch["input_hash"], "input_ref": self.artifacts.put(batch),
                               "result_ref": reference, "metadata_ref": self.artifacts.put(metadata),
                               "origin": str(directory.relative_to(run_folder))}
                    response = verify_receipt(receipt, batch, self.artifacts, self.handlers)
                    write_json(checkpoint, receipt, immutable=True)
                    fresh.append(receipt)
                receipts.append(receipt)
                responses.append(response)
                report(completed=len(receipts), reused=reused)
            except Exception as error:
                report(status="failed", error=str(error), error_type=type(error).__name__)
                failure = BatchExecutionError(f"Research batch {index + 1}/{len(batches)} failed: {error}; accepted checkpoints were retained")
                failure.metadata = {"batch_progress": progress, "batch_receipts": receipts,
                                    "cause_type": type(error).__name__, "cause": getattr(error, "metadata", {}),
                                    "usage": self.usage(fresh) + getattr(error, "metadata", {}).get("usage", [])}
                raise failure from error
        report(status="completed")
        return merge_research(packet, responses), {"executor": "platform_batch_merge", "transport": "batch_files",
            "model": plan["model"], "batch_receipts": receipts, "batch_progress": progress,
            "usage": self.usage(fresh)}

    def usage(self, receipts):
        return [usage for receipt in receipts
                for usage in self.artifacts.get(receipt["metadata_ref"]).get("usage", [])]
