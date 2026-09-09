"""Bounded DAG execution; only this coordinator writes the run manifest."""

from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait

from featuretree.core.storage import write_json
from featuretree.workflow.stages import PLATFORMS
from featuretree.workflow.state import artifact, digest, load_run, lock, now, run_path, save_state
from featuretree.workflow.contracts import validate_result
from featuretree.workflow.gates import validate_proposal
from featuretree.workflow.backends.base import Backend
from featuretree.workflow.packets import snapshot_for, make_packet
from featuretree.workflow.backends.processes import terminate_recorded
from featuretree.workflow.sources import detect_anchors


def execute_attempt(root, packet, folder, state, backend, snapshot):
    stage = packet["stage"]
    if stage == "anchors":
        payload = detect_anchors(root, packet["inputs"]["synthesize"]["nodes"])
        result = {"schema_version": 1, "task_id": packet["task_id"], "input_hash": packet["input_hash"],
                  "stage": stage, "payload": payload}
        metadata = {"backend": "local-corpus-detector"}
    else:
        result, metadata = backend.execute(root, "ft-" + stage, packet, folder, state["timeout"],
                                            state["model"], state["variant"])
        validate_result(root, packet, result)
        if stage == "synthesize":
            validate_proposal(root, snapshot, packet["work"], result["payload"],
                              [packet["inputs"][p] for p in PLATFORMS])
    write_json(folder / "result.json", result)
    write_json(folder / "metadata.json", metadata)
    return result, metadata


def execute_run(root, run_id, backend: Backend, on_event=print):
    folder = run_path(root, run_id)
    with lock(folder / "run.lock"):
        folder, state = load_run(root, run_id)
        if state.get("published") or (folder / "publication.json").exists():
            raise ValueError("Run already publishing/published; use publish to recover")
        snapshot = snapshot_for(folder, state)
        for task in state["tasks"].values():
            if task["status"] == "succeeded":
                artifact(folder, task)
            if task["status"] == "running":
                attempt_dir = folder / "attempts" / task["id"] / str(task["attempts"][-1]["number"])
                terminate_recorded(attempt_dir / "process.json")
                task["attempts"][-1].update(status="interrupted", error="Coordinator interrupted", ended_at=now())
                task["status"] = "pending" if len(task["attempts"]) < task["allowance"] else "failed"
        save_state(folder, state)
        running = {}
        with ThreadPoolExecutor(max_workers=state["workers"]) as pool:
            while True:
                for task in state["tasks"].values():
                    if len(running) >= state["workers"]:
                        break
                    if task["status"] != "pending":
                        continue
                    deps = [state["tasks"][tid] for tid in task["dependencies"]]
                    if not all(t["status"] == "succeeded" for t in deps):
                        continue
                    attempt = {"number": len(task["attempts"]) + 1, "started_at": now(), "status": "running"}
                    attempt_dir = folder / "attempts" / task["id"] / str(attempt["number"])
                    attempt_dir.mkdir(parents=True)
                    try:
                        packet = make_packet(root, folder, state, task, snapshot)
                        write_json(attempt_dir / "input.json", packet)
                    except Exception as exc:
                        attempt.update(status="failed", error=str(exc), ended_at=now())
                        task["attempts"].append(attempt)
                        task["status"] = "failed"
                        on_event(f"{task['id']}: failed to prepare: {exc}")
                        save_state(folder, state)
                        continue
                    task["attempts"].append(attempt)
                    task["status"] = "running"
                    save_state(folder, state)
                    on_event(f"{task['id']}: running attempt {attempt['number']}")
                    future = pool.submit(execute_attempt, root, packet, attempt_dir, state, backend, snapshot)
                    running[future] = (task, attempt_dir)
                if not running:
                    break
                done, _ = wait(running, return_when=FIRST_COMPLETED, timeout=30)
                if not done:
                    on_event(f"Waiting for {len(running)} active OpenCode task(s)")
                for future in done:
                    task, attempt_dir = running.pop(future)
                    attempt = task["attempts"][-1]
                    try:
                        result, metadata = future.result()
                        blocked = result["payload"].get("verdict") == "revise"
                        task.update(status="blocked" if blocked else "succeeded",
                                    result_path=str((attempt_dir / "result.json").relative_to(folder)),
                                    result_hash=digest(result))
                        attempt.update(status=task["status"], metadata=metadata)
                    except Exception as exc:
                        attempt.update(status="failed", error=f"{type(exc).__name__}: {exc}")
                        task["status"] = "pending" if len(task["attempts"]) < task["allowance"] else "failed"
                    attempt["ended_at"] = now()
                    save_state(folder, state)
                    on_event(f"{task['id']}: {task['status']}")
        return state


