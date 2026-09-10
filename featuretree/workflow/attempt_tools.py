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
    header = re.sub(r"^steps:\s*\d+\s*$", f"steps: {steps}", header, flags=re.MULTILINE)
    if "  submit_payload: allow" not in header:
        header = header.replace("  source_catalog: allow", "  source_catalog: allow\n  submit_payload: allow\n  finish_payload: allow")
    body = parts[2].replace("只输出一个符合 output_schema 的 JSON 信封", "使用 submit_payload 分批写入内容，再用 finish_payload 写入符合 output_schema 的 JSON 信封；最终聊天只简短说明完成")
    body = body.replace("禁止写文件", "禁止任意写文件，仅允许 submit_payload 和 finish_payload 写当前交付文件")
    return "---" + header + "---" + body


def delivery_adapter(root, *, finalize=False):
    arguments = ('chunk_refs: tool.schema.array(tool.schema.string()), outcome: tool.schema.enum(["pass", "completed_with_gaps", "needs_sources", "revise"]), issues_json: tool.schema.string(), source_requests_json: tool.schema.string()'
                 if finalize else 'path: tool.schema.array(tool.schema.string()), value_json: tool.schema.string()')
    description = ("Finish the delivery JSON file from chunk_refs in order. issues_json and source_requests_json are JSON arrays (use [] when empty). This validates schema, not business conclusions. Once successful, stop; the executor reads the file."
                   if finalize else "Write an immutable payload chunk in this attempt. Arrays append in finish_payload reference order. At most 24000 characters per value; prefer 20 items per call. Return chunk_ref for finish_payload.")
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
