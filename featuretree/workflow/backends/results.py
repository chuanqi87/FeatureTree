"""Read completed files or legacy chat envelopes; retain diagnostics on every failure."""

import hashlib
import json

from featuretree.core.io import read_json, write_json
from featuretree.workflow.backends.delivery import assemble_chunks, read_delivery
from featuretree.workflow.backends.errors import MissingStructuredAnswer, ResponseFormatError, has_repairable_answer
from featuretree.workflow.backends.events import event_summary, parse_events
from featuretree.workflow.backends.monitor import ExecutionInterrupted
from featuretree.workflow.backends.provider_errors import provider_error


def chat_response(lines, root, folder, packet, metadata):
    final, usage = parse_events(lines)
    metadata.update(usage, output_chars=len(final), transport="chat")
    (folder / "response.json").write_text(final, encoding="utf-8")
    try:
        result = read_json(folder / "response.json")
    except json.JSONDecodeError as exc:
        metadata["response_sha256"] = hashlib.sha256(final.encode()).hexdigest()
        if has_repairable_answer(final):
            raise ResponseFormatError(f"Completed answer is not valid JSON: {exc}. Repair retained response only.") from exc
        raise MissingStructuredAnswer("No complete structured answer was produced; inspect scope/tool budget before retrying") from exc
    if not isinstance(result, dict):
        raise ResponseFormatError("Final response must be a JSON object")
    if "payload_chunks" in result:
        write_json(folder / "delivery-manifest.json", result, immutable=True)
        result, references = assemble_chunks(result, root, packet)
        metadata["payload_chunk_refs"] = references
    return result


def collect_result(root, folder, packet, returncode, metadata):
    lines = (folder / "events.jsonl").read_text().splitlines()
    metadata.update(event_summary(lines))
    try:
        if (root / "delivery/completed.json").is_file():
            result, references = read_delivery(root, packet)
            metadata.update(payload_chunk_refs=references, transport="file")
        else:
            if returncode < 0:
                raise ExecutionInterrupted(f"OpenCode terminated by signal {-returncode}; automatic retry stopped")
            error = provider_error(lines)
            if error:
                metadata["provider_status"] = error.status_code
                raise error
            if returncode:
                raise ValueError(f"OpenCode exited {returncode}; inspect {folder / 'stderr.log'}")
            result = chat_response(lines, root, folder, packet, metadata)
        metadata["recovery"] = "format_repair" if packet.get("response_repair") else None
        write_json(folder / "response.json", result)
        return result, metadata
    except Exception as error:
        metadata["error_type"] = type(error).__name__
        error.metadata = metadata
        raise
    finally:
        write_json(folder / "metadata.json", metadata)
