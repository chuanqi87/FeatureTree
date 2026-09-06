"""Resumable bounded worker pool; one author per node and no automatic model retry."""

from datetime import datetime, timezone
import fcntl
import time

from ..research_profile import fingerprint
from ..storage import contained_path, read_yaml, write_json
from .report import write_report
from .tasks import RUNS_DIR, check_task, load_task

BACKEND_ACTIVE = {"queued", "running", "starting"}


def utcnow():
    return datetime.now(timezone.utc).isoformat()


def load_manifest(repo, path):
    path = contained_path(repo.root, str(path), RUNS_DIR)
    manifest = read_yaml(path)
    expected = fingerprint({k: v for k, v in manifest.items() if k != "run_id"})
    if path.name != "manifest.json" or manifest["run_id"] != expected or path.parent.name != expected:
        raise ValueError("First-pass manifest identity/path mismatch")
    if not 1 <= manifest["concurrency"]["smoke"] <= manifest["concurrency"]["steady"] <= 8:
        raise ValueError("First-pass concurrency must stay within 1..8")
    ids = [row["feature_id"] for row in manifest["tasks"]]
    if len(ids) != len(set(ids)) or sorted(ids) != sorted(manifest["scope"]):
        raise ValueError("Manifest must assign every selected node exactly once")
    if not manifest["smoke_features"] or not set(manifest["smoke_features"]) <= set(ids):
        raise ValueError("Invalid smoke selection")
    return path, manifest


def initial_state(manifest):
    return {"run_id": manifest["run_id"], "status": "prepared", "started_at": None,
            "concurrency": manifest["concurrency"]["smoke"], "smoke_ids": [],
            "nodes": {row["feature_id"]: {"status": "pending", "attempts": 0} for row in manifest["tasks"]}}


def queued_nodes(manifest, state):
    leaves_remaining = any(row["role"] == "leaf" and state["nodes"][row["feature_id"]]["status"] in {"pending", "running"}
                           for row in manifest["tasks"])
    return [row for row in manifest["tasks"] if state["nodes"][row["feature_id"]]["status"] == "pending"
            and (not leaves_remaining or row["role"] == "leaf")]


def update_job(repo, directory, bridge, fid, record, now, deadline):
    snapshot = bridge.status(record["job_id"])
    record["backend"] = snapshot
    elapsed = now - record["launched_epoch"]
    timed_out = elapsed >= record["hard_seconds"] or now >= deadline
    if snapshot["status"] in BACKEND_ACTIVE and not timed_out:
        return
    if snapshot["status"] in BACKEND_ACTIVE:
        bridge.cancel(record["job_id"])
        record["cancelled_by_runner"] = "deadline" if now >= deadline else "task_timeout"
    record.update(status="failed", finished_at=utcnow(), elapsed_seconds=round(elapsed, 2))
    try:
        check = check_task(repo, directory / "tasks" / fid / "task.json")
        record["check"] = check
        if check["delivery_valid"]:
            record["status"] = "delivered_partial" if timed_out or snapshot["status"] != "completed" else "delivered"
        else:
            record["error"] = "; ".join(check["errors"])
    except (ValueError, OSError, KeyError, TypeError, IndexError, AttributeError) as exc:
        record["error"] = str(exc)


def poll_active(repo, directory, bridge, state, now, deadline):
    changed = False
    for fid, record in state["nodes"].items():
        if record["status"] == "running":
            try:
                previous = record["status"]
                update_job(repo, directory, bridge, fid, record, now, deadline)
                changed |= record["status"] != previous
                if record["status"] != previous:
                    state["consecutive_failures"] = state.get("consecutive_failures", 0) + 1 if record["status"] == "failed" else 0
                    if state["consecutive_failures"] >= 3:
                        state["backoff_until"] = time.time() + 120
                    if state["consecutive_failures"] >= 8:
                        state.update(status="stopped_backend_failures", attention="Eight consecutive failures; stop new dispatch and inspect backend/format")
                record.pop("poll_error", None)
            except Exception as exc:
                record["poll_error"] = str(exc)
                # Do not relaunch an unknown-state job. Deadline cancellation still applies.
                if now >= deadline or now - record["launched_epoch"] >= record["hard_seconds"]:
                    try:
                        bridge.cancel(record["job_id"])
                        record.update(status="failed", error="Status unavailable; cancelled at time limit", finished_at=utcnow())
                        changed = True
                    except Exception as cancel_error:
                        state["attention"] = f"Cancellation requires attention: {record['job_id']}: {cancel_error}"
    return changed


def dispatch_pending(repo, path, manifest, state, pending, active, bridge):
    changed = False
    state_path = path.parent / "state.json"
    for row in pending[:max(0, state["concurrency"] - active)]:
        if state["status"] != "running":
            break
        fid = row["feature_id"]
        task_path = path.parent / "tasks" / fid / "task.json"
        try:
            task = load_task(repo, task_path)
            if task["task_id"] != row["task_id"] or task["model"] != manifest["model"]:
                raise ValueError("Manifest/task/model mismatch")
        except Exception as exc:
            state.update(status="stopped_input_change", attention=str(exc))
            break
        record = state["nodes"][fid]
        record.update(status="launching", attempts=1, launched_epoch=time.time(), hard_seconds=task["budget"]["hard_seconds"])
        write_json(state_path, state)
        try:
            job_id = bridge.launch(task_path, manifest["model"])
            record.update(status="running", job_id=job_id)
        except Exception as exc:
            record.update(status="launch_uncertain", error=str(exc))
            state["status"] = "launch_uncertain"
            # CLI may have submitted before its response was lost; never retry automatically.
            break
        changed = True
        write_json(state_path, state)
    return changed


def run_batch(repo, manifest_path, bridge, poll_seconds=20):
    path, manifest = load_manifest(repo, manifest_path)
    state_path = path.parent / "state.json"
    with (path.parent / "runner.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        state = read_yaml(state_path) if state_path.exists() else initial_state(manifest)
        if state["run_id"] != manifest["run_id"]:
            raise ValueError("State belongs to another run")
        if any(row["status"] == "launching" for row in state["nodes"].values()):
            state.update(status="launch_uncertain", attention="Interrupted while launching; reconcile missing job receipt before any new dispatch")
            write_json(state_path, state)
        if state["status"] in {"completed", "deadline_reached", "stopped_smoke_failure", "launch_uncertain", "stopped_input_change", "stopped_backend_failures"}:
            return write_report(repo, path, manifest, state)
        state.update(status="running", started_at=state["started_at"] or utcnow())
        deadline = datetime.fromisoformat(manifest["deadline"].replace("Z", "+00:00")).timestamp()
        if not state["smoke_ids"]:
            state["smoke_ids"] = manifest["smoke_features"]
        while True:
            now = time.time()
            changed = poll_active(repo, path.parent, bridge, state, now, deadline)
            active = sum(r["status"] == "running" for r in state["nodes"].values())
            smoke_done = all(state["nodes"][fid]["status"] not in {"pending", "running"} for fid in state["smoke_ids"])
            if smoke_done:
                passed = sum(state["nodes"][fid].get("check", {}).get("delivery_valid", False) for fid in state["smoke_ids"])
                if passed < max(1, len(state["smoke_ids"]) - 1):
                    state["status"] = "stopped_smoke_failure"
                else:
                    state["concurrency"] = 2 if state.get("consecutive_failures", 0) >= 3 else manifest["concurrency"]["steady"]
            if now >= deadline:
                state["status"] = "deadline_reached"
            pending = queued_nodes(manifest, state)
            if now < state.get("backoff_until", 0):
                pending = []
            if not smoke_done:
                pending = [row for row in pending if row["feature_id"] in state["smoke_ids"]]
            changed |= dispatch_pending(repo, path, manifest, state, pending, active, bridge)
            active = sum(r["status"] == "running" for r in state["nodes"].values())
            pending_count = sum(r["status"] == "pending" for r in state["nodes"].values())
            if not active and not pending_count and state["status"] == "running":
                state["status"] = "completed"
            state["updated_at"] = utcnow()
            write_json(state_path, state)
            if changed or state["status"] != "running":
                write_report(repo, path, manifest, state)
            if state["status"] != "running" and not active:
                return write_report(repo, path, manifest, state)
            time.sleep(poll_seconds)
