"""Commands to prepare, execute and inspect the isolated preliminary batch."""

import argparse
from collections import Counter
import json
import subprocess
import sys

from ..storage import Repository, read_yaml, write_json
from .bridge import AgentBridge
from .report import write_report
from .runner import initial_state, load_manifest, run_batch
from .tasks import check_task, prepare_batch


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    prepare = commands.add_parser("prepare")
    prepare.add_argument("--model", required=True)
    prepare.add_argument("--deadline", required=True)
    prepare.add_argument("--feature", action="append")
    prepare.add_argument("--existing-nodes-only", action="store_true", help="Explicitly opt into fixed-tree knowledge research on authored taxonomy nodes")
    check = commands.add_parser("check")
    check.add_argument("task")
    run = commands.add_parser("run")
    run.add_argument("manifest")
    run.add_argument("--launcher", required=True)
    run.add_argument("--background", action="store_true")
    run.add_argument("--poll-seconds", type=int, default=20)
    run.add_argument("--existing-nodes-only", action="store_true")
    for command in ("status", "report"):
        commands.add_parser(command).add_argument("manifest")
    args = parser.parse_args(argv)
    repo = Repository()
    try:
        if args.command in {"prepare", "run"} and not args.existing_nodes_only:
            raise ValueError(
                "Fixed-tree research is not tree building. "
                "Author taxonomy via docs/tree-design.md; knowledge research requires --existing-nodes-only"
            )
        if args.command == "prepare":
            path = prepare_batch(repo, args.model, args.deadline, args.feature)
            print(json.dumps({"manifest": str(path), "model_calls": 0}))
            return 0
        if args.command == "check":
            result = check_task(repo, args.task)
            print(json.dumps(result, ensure_ascii=False))
            return 0 if result["delivery_valid"] else 2
        path, manifest = load_manifest(repo, args.manifest)
        if args.command == "run":
            if not 1 <= args.poll_seconds <= 60:
                raise ValueError("Poll interval must be 1..60 seconds")
            bridge = AgentBridge(repo, args.launcher)
            if args.background:
                command = [sys.executable, str(repo.root / "scripts/research_first_pass.py"), "run", str(path),
                           "--launcher", str(bridge.launcher), "--poll-seconds", str(args.poll_seconds), "--existing-nodes-only"]
                with (path.parent / "runner.log").open("a", encoding="utf-8") as log:
                    process = subprocess.Popen(command, cwd=repo.root, stdin=subprocess.DEVNULL,
                                               stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
                result = {"pid": process.pid, "manifest": str(path), "status": "runner_spawned"}
                write_json(path.parent / "runner-process.json", result)
            else:
                result = run_batch(repo, path, bridge, args.poll_seconds)
        else:
            state_path = path.parent / "state.json"
            state = read_yaml(state_path) if state_path.exists() else initial_state(manifest)
            if args.command == "report":
                result = write_report(repo, path, manifest, state)
            else:
                result = {"run_id": manifest["run_id"], "status": state["status"], "deadline": manifest["deadline"],
                          "updated_at": state.get("updated_at"), "concurrency": state["concurrency"],
                          "counts": dict(Counter(row["status"] for row in state["nodes"].values())),
                          "attention": state.get("attention"), "active": [
                              {"feature_id": fid, "job_id": row.get("job_id"), "phase": row.get("backend", {}).get("phase")}
                              for fid, row in state["nodes"].items() if row["status"] == "running"]}
        print(json.dumps(result, ensure_ascii=False), flush=True)
        return 0
    except Exception as exc:
        print(json.dumps({"error": str(exc), "production_accepted": False}), flush=True)
        return 2
