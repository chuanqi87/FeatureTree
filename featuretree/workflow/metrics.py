"""Timing and provider-reported usage; missing measurements remain unknown."""

from datetime import datetime, timezone


def timestamp(value):
    return datetime.fromisoformat(value) if value else None


def task_metrics(task, active=False, at=None):
    at = at or datetime.now(timezone.utc)
    durations = []
    for attempt in task["attempts"]:
        elapsed = attempt.get("metadata", {}).get("elapsed_seconds")
        if elapsed is None:
            start = timestamp(attempt.get("started_at"))
            end = timestamp(attempt.get("ended_at"))
            if not end and active and attempt["status"] == "running":
                end = at
            elapsed = max(0, (end - start).total_seconds()) if start and end else None
        if elapsed is not None:
            durations.append(elapsed)
    last = task["attempts"][-1] if task["attempts"] else {}
    return {"elapsed_seconds": round(sum(durations), 1) if durations else None,
            "first_response_seconds": last.get("metadata", {}).get("first_response_seconds"),
            "retryable": last.get("retryable"),
            "reused": last.get("metadata", {}).get("model_invoked") is False,
            "input_chars": last.get("metadata", {}).get("input_chars")}


def execution_metrics(state, active=None, at=None):
    at = at or datetime.now(timezone.utc)
    tasks = list(state["tasks"].values())
    active = any(t["status"] == "running" for t in tasks) if active is None else active
    attempts = [a for t in tasks for a in t["attempts"]]
    starts = [timestamp(a["started_at"]) for a in attempts if a.get("started_at")]
    ends = [timestamp(a["ended_at"]) for a in attempts if a.get("ended_at")]
    end = at if active else max(ends) if ends else None
    wall = max(0, (end - min(starts)).total_seconds()) if starts and end else None
    usage = [step for a in attempts for step in a.get("metadata", {}).get("usage", [])]
    totals = [step.get("tokens", {}).get("total") for step in usage]
    costs = [step.get("cost") for step in usage]
    measured = [task_metrics(t, active, at)["elapsed_seconds"] for t in tasks]
    return {"wall_seconds": round(wall, 1) if wall is not None else None,
            "stage_seconds": round(sum(s for s in measured if s is not None), 1),
            "model_calls": sum(a.get("metadata", {}).get("model_invoked", True)
                               for t in tasks if t["stage"] != "anchors" for a in t["attempts"]),
            "reported_total_tokens": sum(totals) if totals and all(v is not None for v in totals) else None,
            "reported_cost": sum(costs) if costs and all(v is not None for v in costs) else None,
            "usage_note": "Provider-reported usage; zero cost does not prove the run was free"}
