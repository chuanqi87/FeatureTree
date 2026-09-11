"""OpenCode event decoding and token diagnostics, independent of business validation."""

import json
from featuretree.workflow.backends.errors import MissingStructuredAnswer


def parse_events(lines):
    messages = {}
    session_id = None
    completed = False
    usage = []
    for line in lines:
        if not line.strip():
            continue
        event = json.loads(line)
        if event.get("type") in ("error", "session.error"):
            raise ValueError(f"OpenCode reported an error: {event.get('error', event.get('properties'))}")
        part = event.get("part", {})
        session_id = event.get("sessionID") or part.get("sessionID") or session_id
        if part.get("type") == "text":
            message = part.get("messageID", "final")
            messages.setdefault(message, {})[part.get("id", "text")] = part["text"]
        if part.get("type") == "step-start":
            completed = False
        if part.get("type") == "step-finish":
            completed = part.get("reason") == "stop"
            usage.append({k: part[k] for k in ("cost", "tokens", "reason") if k in part})
            if part.get("reason") in ("error", "content-filter"):
                raise ValueError(f"Incomplete model output: {part.get('reason')}")
    if not completed or not messages:
        raise MissingStructuredAnswer("OpenCode produced no delivery file or completed structured response; inspect retained events and workspace")
    final = "\n".join(list(messages.values())[-1].values()).strip()
    # Accept a single fenced object; never heuristically extract a substring from prose.
    if final.startswith("```json\n") and final.endswith("\n```"):
        final = final[8:-4]
    elif final.startswith("```\n") and final.endswith("\n```"):
        final = final[4:-4]
    return final, {"session_id": session_id, "usage": usage}


def event_summary(lines):
    usage, session_id = [], None
    for line in lines:
        try:
            event = json.loads(line)
        except ValueError:
            continue  # A process stopped after file commit can leave a partial trailing event.
        part = event.get("part", {})
        session_id = event.get("sessionID") or part.get("sessionID") or session_id
        if part.get("type") == "step-finish":
            usage.append({key: part[key] for key in ("cost", "tokens", "reason") if key in part})
    return {"session_id": session_id, "usage": usage,
            "output_limit_reached": any(step.get("reason") == "length" for step in usage)}
