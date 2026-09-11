"""Generate narrowly scoped OpenCode tool adapters for an isolated attempt."""

import json
import re


def configure_agent(text, steps):
    parts = text.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        raise ValueError("Agent requires YAML front matter")
    header = parts[1]
    if not re.search(r"^steps:\s*\d+\s*$", header, re.MULTILINE):
        raise ValueError("Agent must declare its step budget")
    header = re.sub(r"^steps:\s*\d+\s*$", f"steps: {steps}" if steps is not None else "", header, flags=re.MULTILINE)
    return "---" + header + "---" + parts[2]



def delivery_adapter(root, *, finalize=False):
    arguments = ('chunk_refs: tool.schema.array(tool.schema.string()), outcome: tool.schema.enum(["pass", "completed_with_gaps", "needs_sources", "revise"]), issues_json: tool.schema.string(), source_requests_json: tool.schema.string()'
                 if finalize else 'path: tool.schema.array(tool.schema.string()), value_json: tool.schema.string()')
    description = ("Finish the delivery JSON file from chunk_refs in order. issues_json and source_requests_json are JSON arrays (use [] when empty). This validates schema, not business conclusions. Once successful, stop; the executor reads the file."
                   if finalize else "Write an immutable payload chunk in this attempt. Arrays append in finish_payload reference order. Prefer 20 items per call; no enforced chunk size limit. Return chunk_ref for finish_payload.")
    return '''import { tool } from "@opencode-ai/plugin";
import { spawn } from "node:child_process";
export default tool({
  description: DESCRIPTION,
  args: {ARGUMENTS},
  async execute(args) {
    if (!process.env.FEATURETREE_PACKET) throw new Error("No pinned FeatureTree packet");
    return await new Promise((resolve, reject) => {
      const child = spawn(PYTHON, ["-m", "featuretree.workflow.delivery_tool", "--packet",
        process.env.FEATURETREE_PACKET], {cwd: PROJECT, stdio: ["pipe", "pipe", "pipe"]});
      let out = "", err = "";
      child.stdout.on("data", chunk => {out += chunk;});
      child.stderr.on("data", chunk => {err += chunk;});
      child.on("error", reject);
      child.on("close", code => code === 0 ? resolve(out) : reject(new Error(err.slice(-4000))));
      child.stdin.end(JSON.stringify(args));
    });
  }
});
'''.replace("PYTHON", json.dumps(str(root / ".venv/bin/python"))).replace("PROJECT", json.dumps(str(root))).replace("DESCRIPTION", json.dumps(description)).replace("ARGUMENTS", arguments)
