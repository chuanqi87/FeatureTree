"""Attempt-local payload chunks; assembly changes transport, never business rules."""

from copy import deepcopy
import re

from featuretree.core.content import digest
from featuretree.core.io import IntegrityError, file_lock, read_json, write_json


def field_schema(packet, path):
    if not isinstance(path, list) or not path or len(path) > 8:
        raise ValueError("A payload field path of one to eight property names is required")
    schema = packet["output_schema"]["properties"]["payload"]
    for key in path:
        if not isinstance(key, str) or key not in schema.get("properties", {}):
            raise ValueError("Chunk path must name a declared payload property")
        schema = schema["properties"][key]
    return schema


def save_chunk(workspace, packet, path, value):
    schema = field_schema(packet, path)
    # Validate individual array items now; collection cardinality is checked after assembly.
    from jsonschema import Draft202012Validator
    item_schema = {key: item for key, item in schema.items() if key not in
                   ("minItems", "maxItems", "uniqueItems")} if schema.get("type") == "array" else schema
    Draft202012Validator(item_schema).validate(value)
    chunk = {"input_hash": packet["input_hash"], "path": path, "value": value}
    reference = digest(chunk)
    directory = workspace / "delivery"
    with file_lock(directory / "chunks.lock"):
        if (directory / "completed.json").exists():
            raise ValueError("Delivery is already finalized; create a new revision")
        target = directory / (reference + ".json")
        if packet["limits"]["max_delivery_chunks"] is not None and not target.exists() and len(list(directory.glob("*.json"))) >= packet["limits"]["max_delivery_chunks"]:
            raise ValueError("Payload chunk budget exhausted")
        write_json(target, chunk, immutable=True)
    return {"chunk_ref": reference, "path": path,
            "item_count": len(value) if isinstance(value, list) else 1}


def assemble_chunks(response, workspace, packet):
    if "payload_chunks" not in response:
        return response, []
    if "payload" in response:
        raise ValueError("Use either payload or payload_chunks, never both")
    references = response["payload_chunks"]
    if (not isinstance(references, list) or not references
            or (packet["limits"]["max_delivery_chunks"] is not None and len(references) > packet["limits"]["max_delivery_chunks"])
            or any(not isinstance(ref, str) or not re.fullmatch(r"[0-9a-f]{64}", ref) for ref in references)
            or len(set(references)) != len(references)):
        raise ValueError("Invalid or duplicate payload chunk references")
    payload, assigned = {}, {}
    for ref in references:
        chunk = read_json(workspace / "delivery" / (ref + ".json"))
        if digest(chunk) != ref or chunk["input_hash"] != packet["input_hash"]:
            raise IntegrityError("Payload chunk identity or input fingerprint mismatch")
        schema = field_schema(packet, chunk["path"])
        path, value = tuple(chunk["path"]), chunk["value"]
        for prior in assigned:
            if prior != path and (prior[:len(path)] == path or path[:len(prior)] == prior):
                raise ValueError("Overlapping payload paths cannot overwrite submitted content")
        target = payload
        for name in path[:-1]:
            target = target.setdefault(name, {})
        if path in assigned:
            if schema.get("type") != "array" or not isinstance(value, list):
                raise ValueError("Only array fields can span multiple chunks")
            target[path[-1]].extend(deepcopy(value))
        else:
            target[path[-1]] = deepcopy(value)
            assigned[path] = True
    merged = {key: value for key, value in response.items() if key != "payload_chunks"}
    merged["payload"] = payload
    return merged, references


def finalize_delivery(workspace, packet, references, outcome, issues, source_requests):
    from jsonschema import Draft202012Validator
    manifest = {key: packet[key] for key in
                ("protocol_version", "run_id", "work_id", "task_id", "stage_id", "input_hash")}
    manifest.update(payload_chunks=references, outcome=outcome, issues=issues, source_requests=source_requests)
    response, _ = assemble_chunks(manifest, workspace, packet)
    Draft202012Validator(packet["output_schema"]).validate(response)
    record = {"manifest": manifest, "response": response}
    with file_lock(workspace / "delivery/chunks.lock"):
        write_json(workspace / "delivery/completed.json", record, immutable=True)
    return {"status": "file_written", "response_hash": digest(response),
            "path": "delivery/completed.json", "validation": "schema_only; business_validation_pending"}


def read_delivery(workspace, packet):
    from jsonschema import Draft202012Validator
    record = read_json(workspace / "delivery/completed.json")
    for key in ("protocol_version", "run_id", "work_id", "task_id", "stage_id", "input_hash"):
        if record["manifest"][key] != packet[key]:
            raise IntegrityError("Completed delivery belongs to a different task input")
    response, references = assemble_chunks(record["manifest"], workspace, packet)
    if digest(response) != digest(record["response"]):
        raise IntegrityError("Completed delivery differs from its immutable payload chunks")
    Draft202012Validator(packet["output_schema"]).validate(response)
    return response, references


def delivery_prompt():
    return """使用文件交付模式：submit_payload 分批写 JSON 内容，finish_payload 写成最终交付文件。
工具 path 是 payload 内字段路径（如 ["facts"]、["api_dispositions"] 或 ["spec","questions"]）；
value_json 是该字段的 JSON 值。建议数组按每批约 20 项提交，可多次追加同一数组。
非数组字段只提交一次，不能同时提交父字段及其子字段。每次工具返回不可变 chunk_ref。
最后调用 finish_payload，chunk_refs 填所有选用的 chunk_ref（按追加顺序），填写 outcome、issues_json、source_requests_json。
代码自动填写固定任务身份并将完整 JSON 写入 delivery/completed.json，执行同一完整 schema、输入守恒和证据校验。
最终聊天仅需说已完成，不要返回整份 JSON 或复述文件。分批存入不表示通过审核；不得遗漏输入，不得用空列表冒充已分析。
必须预留最后一步调用 finish_payload。文件完成后无需继续检索或解释。\n"""
