"""User-facing commands for the tree-design workflow."""

from featuretree.workflow.backends.opencode import OpenCodeBackend

import argparse
import json
from pathlib import Path
import subprocess
from jsonschema import ValidationError
from featuretree.core.storage import ROOT
from featuretree.workflow.state import read_json
from featuretree.workflow.engine import execute_run
from featuretree.workflow.recovery import reset_tasks
from featuretree.workflow.planning import make_plan
from featuretree.workflow.publication import publish, report
from featuretree.workflow.backends.diagnostics import doctor


def main(argv=None):
    parser = argparse.ArgumentParser(description="Standard node-scoped OpenCode tree workflow")
    parser.add_argument("--root", type=Path, default=ROOT)
    commands = parser.add_subparsers(dest="command", required=True)
    plan = commands.add_parser("plan", help="Snapshot existing branches and prepare a batch without invoking models")
    plan.add_argument("--node", action="append", required=True)
    plan.add_argument("--baseline", type=Path, required=True)
    for flag, default in (("depth", 1), ("max-nodes", 12), ("workers", 3), ("timeout", 600),
                          ("max-attempts", 2), ("max-revisions", 2)):
        plan.add_argument("--" + flag, type=int, default=default)
    plan.add_argument("--model")
    plan.add_argument("--variant")
    plan.add_argument("--max-input-chars", type=int, default=500000)
    plan.add_argument("--first-response-timeout", type=int, default=120,
                      help="Stop without automatic retry if no model text/tool event arrives in this many seconds")
    for command in ("run", "report", "publish", "retry"):
        commands.add_parser(command).add_argument("run_id")
    revise = commands.add_parser("revise")
    revise.add_argument("run_id")
    revise.add_argument("--node", action="append", required=True)
    check = commands.add_parser("doctor")
    check.add_argument("--smoke", action="store_true", help="Invoke one real OpenCode model protocol test")
    check.add_argument("--timeout", type=int, default=120)
    check.add_argument("--model")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    try:
        if args.command == "plan":
            state = make_plan(root, args.node, read_json(args.baseline), args.depth, args.max_nodes,
                              args.workers, args.timeout, args.max_attempts, args.max_revisions,
                              args.model, args.variant, args.max_input_chars, args.first_response_timeout)
            result = {"run_id": state["id"], "nodes": state["nodes"], "tasks": len(state["tasks"]),
                      "next": f"python scripts/workflow.py run {state['id']}"}
        elif args.command == "doctor":
            result = doctor(root, args.smoke, args.timeout, args.model)
        elif args.command == "run":
            execute_run(root, args.run_id, OpenCodeBackend())
            result = report(root, args.run_id)
        elif args.command == "report":
            result = report(root, args.run_id)
        elif args.command == "publish":
            result = publish(root, args.run_id)
        else:
            reset_tasks(root, args.run_id, args.node if args.command == "revise" else None)
            result = {"run_id": args.run_id, "next": f"python scripts/workflow.py run {args.run_id}"}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 2 if args.command == "run" and not result["ready_to_publish"] else 0
    except (ValueError, OSError, ValidationError, subprocess.SubprocessError) as exc:
        parser.exit(2, f"workflow: {exc}\n")
