import { tool } from "@opencode-ai/plugin";
import { execFile } from "node:child_process";
import { promisify } from "node:util";
import path from "node:path";

const executeFile = promisify(execFile);

export default tool({
  description: "只读查询本项目官方 API 资料库，返回精确正文路径、哈希、行号摘录与目录线索。未找到不代表不支持。",
  args: {
    platform: tool.schema.enum(["android", "ios", "harmonyos"]),
    query: tool.schema.string().min(1).max(180).describe("单一具体 API/模块符号或短能力词，不要拼接多个问题"),
  },
  async execute(args, context) {
    const { stdout } = await executeFile(
      path.join(context.directory, ".venv/bin/python"),
      ["-m", "featuretree.workflow.agent_sources", args.platform, args.query],
      { cwd: context.directory, timeout: 20000, maxBuffer: 128 * 1024 },
    );
    return stdout;
  },
});
