"""Retry malformed responses from retained bytes, without repeating source research."""

import hashlib
import json
import re

from featuretree.workflow.state import digest, read_json


class ResponseFormatError(ValueError):
    """A completed response exists but is not valid JSON; eligible for format repair."""


class MissingStructuredAnswer(ValueError):
    retryable = False


def has_repairable_answer(text):
    """Classify an existing answer for repair; never extract it to accept a result."""
    fences = re.findall(r"```(?:json)?\s*\n(.*?)\n```", text, re.DOTALL)
    if len(fences) > 1:
        return False
    # A prose prefix or unescaped quote inside an answer is a repairable format
    # problem. Require an actual envelope-shaped answer, not a planning summary.
    starts = list(re.finditer(r'(?m)^\s*\{\s*"schema_version"\s*:', text))
    if len(starts) > 1:
        return False
    candidates = [text.lstrip(), *fences]
    if starts:
        candidates.append(text[starts[0].start():].strip())
    for candidate in candidates:
        try:
            value, end = json.JSONDecoder().raw_decode(candidate)
        except ValueError:
            if (candidate.rstrip().endswith("}")
                    and all(re.search(r'"' + key + r'"\s*:', candidate) for key in
                            ("schema_version", "task_id", "input_hash", "stage", "payload"))
                    and re.search(r'"payload"\s*:\s*\{', candidate)):
                return True
            continue
        if candidate[end:].lstrip().startswith(("{", "[")):
            continue
        if isinstance(value, dict) and isinstance(value.get("payload"), dict) and all(key in value for key in ("schema_version", "task_id", "input_hash", "stage")):
            return True
    return False


def repair_packet(folder, task):
    if not task["attempts"]:
        return None
    previous = task["attempts"][-1]
    metadata = previous.get("metadata", {})
    if metadata.get("error_type") != "ResponseFormatError":
        return None
    attempt = folder / "attempts" / task["id"] / str(previous["number"])
    raw = (attempt / "response.json").read_bytes()
    if hashlib.sha256(raw).hexdigest() != metadata.get("response_sha256"):
        raise ValueError("Retained malformed response was modified")
    packet = read_json(attempt / "input.json")
    original_hash = packet.pop("input_hash")
    if digest(packet) != original_hash:
        raise ValueError("Retained input packet was modified")
    packet["previous_error"] = previous["error"]
    packet["response_repair"] = {
        "source_attempt": previous["number"], "source_input_hash": original_hash,
        "response_sha256": metadata["response_sha256"], "text": raw.decode("utf-8"),
        "instruction": "只修复 JSON 传输格式；复用原研究内容，不追加检索、不新增结论。信封使用当前 input_hash。"
    }
    return packet
