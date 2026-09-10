"""Deterministic platform research partitions and lossless stage consolidation."""

from copy import deepcopy

from featuretree.core.content import digest
from featuretree.workflow.packaging import envelope


PLATFORM_RESEARCH = {"ft-android", "ft-ios", "ft-harmonyos"}


def minimum_limit(*values):
    bounded = [value for value in values if value is not None]
    return min(bounded) if bounded else None


def research_batches(packet):
    limit = packet["limits"].get("source_batch_size")
    if packet["stage_id"] not in PLATFORM_RESEARCH or not limit:
        return []
    platform = packet["source_access"]["platform"]
    apis = packet["work"].get("research_order", {}).get(platform, sorted(packet["work"]["api_ids"]))
    if len(set(apis)) != len(apis) or set(apis) != set(packet["work"]["api_ids"]):
        raise ValueError("Research order must preserve every platform API exactly once")
    inputs = [("api_ids", key) for key in apis] + [("topic_ids", key) for key in sorted(packet["work"]["topic_ids"])]
    if len(inputs) <= limit:
        return []
    count = (len(inputs) + limit - 1) // limit
    batches = []
    for index, offset in enumerate(range(0, len(inputs), limit)):
        child = deepcopy(packet)
        child.pop("input_hash")
        # A retry preserves the research revision; semantic changes invalidate its checkpoints.
        child["revision"] = packet.get("batch_revision", packet["revision"])
        child.pop("retained_candidate", None)
        child.pop("response_repair", None)
        platform = child["source_access"]["platform"]
        for kind in ("api_ids", "topic_ids"):
            keys = [key for collection, key in inputs[offset:offset + limit] if collection == kind]
            child["work"][kind] = keys
            child["source_access"][kind] = keys
        child["work"]["selection"] = {"ids": child["work"]["api_ids"]}
        child["work"]["topic_selection"] = {"ids": child["work"]["topic_ids"]}
        child["work"]["research_order"] = {platform: child["work"]["api_ids"]}
        child["work"]["source_groups"] = {
            "declarations": {platform: child["work"]["api_ids"]},
            "topics": {platform: child["work"]["topic_ids"]}}
        child["work"]["enumeration_complete"] = False
        child["batch"] = {"index": index, "count": count,
                          "parent_scope_hash": digest(packet["work"]),
                          "instruction": "这是代码分配的单批研究，只处置本批 API/主题，勿尝试遍历整个领域。批次不是叶子边界；跨批实现链留待对齐阶段整合。范围外依赖记缺口，不猜测不支持。使用交付工具写文件。"}
        child["limits"]["timeout_seconds"] = minimum_limit(packet["limits"]["timeout_seconds"], packet["limits"]["batch_timeout_seconds"])
        child["limits"]["max_tool_calls"] = minimum_limit(packet["limits"]["max_tool_calls"], packet["limits"]["batch_max_tool_calls"])
        child["input_hash"] = digest(child)
        batches.append(child)
    return batches


def merge_research(packet, responses):
    batches = research_batches(packet)
    if len(batches) != len(responses):
        raise ValueError("Cannot merge incomplete research batches")
    payload = {"platform": packet["source_access"]["platform"], "facts": [],
               "api_dispositions": [], "topic_dispositions": []}
    issues, requests, outcomes = [], [], []
    for index, (batch, original) in enumerate(zip(batches, responses)):
        if original["input_hash"] != batch["input_hash"] or original["stage_id"] != packet["stage_id"]:
            raise ValueError("Research batch does not match the fixed input partition")
        response = deepcopy(original)
        # Facts are local names assigned independently by the same named platform agent.
        mapping = {fact["id"]: f"{packet['stage_id']}--batch_{index:04d}--{fact['id']}" for fact in response["payload"]["facts"]}
        for fact in response["payload"]["facts"]:
            fact["id"] = mapping[fact["id"]]
        for issue in response["issues"]:
            issue["id"] = f"{packet['stage_id']}--batch_{index:04d}--{issue['id']}"
            issue["subject_ids"] = [mapping.get(key, key) for key in issue["subject_ids"]]
        for request in response["source_requests"]:
            request["subject_ids"] = [mapping.get(key, key) for key in request["subject_ids"]]
        for key in ("facts", "api_dispositions", "topic_dispositions"):
            payload[key].extend(response["payload"][key])
        issues.extend(response["issues"])
        requests.extend(response["source_requests"])
        outcomes.append(response["outcome"])
    rank = {"pass": 0, "completed_with_gaps": 1, "needs_sources": 2, "revise": 3}
    result = envelope(packet, payload, max(outcomes, key=rank.__getitem__), issues)
    result["source_requests"] = requests
    return result


def research_identity(packet):
    value = deepcopy(packet)
    for key in ("input_hash", "run_id", "task_id", "work_id", "revision", "batch_revision",
                "revision_feedback", "stage_fingerprint", "implementation_files", "limits"):
        value.pop(key, None)
    value["work"].pop("revision_of", None)
    if "batch" in value:
        value["batch"].pop("parent_scope_hash", None)
    return value
