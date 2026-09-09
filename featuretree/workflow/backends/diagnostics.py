"""User-facing commands for the tree-design workflow."""

import json
import subprocess
from featuretree.core.storage import write_json
from featuretree.workflow.stages import STAGES
from featuretree.workflow.state import digest
from featuretree.workflow.contracts import output_schema, validate_result
from featuretree.workflow.backends.opencode import OpenCodeBackend


def doctor(root, smoke=False, timeout=120, model=None):
    version = subprocess.run(["opencode", "--version"], capture_output=True, text=True, timeout=15, check=True)
    agents = {}
    for stage in (*STAGES[:-1], "integrate"):
        name = "ft-" + stage
        check = subprocess.run(["opencode", "debug", "agent", name, "--pure"], cwd=root, capture_output=True,
                               text=True, timeout=30, check=True)
        data = json.loads(check.stdout)
        if data.get("name") != name:
            raise ValueError(f"OpenCode did not load agent: {name}")
        if any(data.get("tools", {}).get(t) for t in ("bash", "edit", "write", "task", "question")):
            raise ValueError(f"OpenCode agent has unexpected write or delegation permissions: {name}")
        agents[name] = {"mode": data.get("mode"), "loaded": True}
    result = {"opencode_version": version.stdout.strip(), "agents": agents, "model_smoke": "not_requested"}
    if smoke:
        from datetime import datetime
        folder = root / ".workflow/smoke" / datetime.now().strftime("%Y%m%d-%H%M%S-%f")
        folder.mkdir(parents=True)
        packet = {"schema_version": 1, "task_id": "smoke/scope", "stage": "scope",
                  "instruction": "协议烟测，不做实际平台研究。为测试分支提出两个抽象能力分组，标明仅为协议测试。",
                  "work": {"node_id": "test", "depth": 1, "subtree": {"test": {
                      "id": "test", "name": {"zh": "协议测试", "en": "Protocol test"},
                      "definition": "仅用于测试 JSON 协议", "granularity": "branch"}}, "max_nodes": 2},
                  "inputs": {}, "output_schema": output_schema(root, "scope")}
        packet["input_hash"] = digest(packet)
        write_json(folder / "input.json", packet)
        output, metadata = OpenCodeBackend().execute(root, "ft-scope", packet, folder, timeout, model, None)
        validate_result(root, packet, output)
        write_json(folder / "result.json", output)
        write_json(folder / "metadata.json", metadata)
        result.update(model_smoke="passed", smoke_artifacts=str(folder))
    return result
