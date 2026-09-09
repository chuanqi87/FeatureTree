import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import { createServer } from "vite";
import { createModel } from "../model.js";

const root = fileURLToPath(new URL("../..", import.meta.url));
const snapshot = JSON.parse(
  execFileSync(
    `${root}/.venv/bin/python`,
    [
      "-c",
      "import json; from featuretree.storage import Repository; from featuretree.viewer import build_snapshot, json_default; print(json.dumps(build_snapshot(Repository()), default=json_default))",
    ],
    { cwd: root, maxBuffer: 20_000_000 },
  ),
);
const model = createModel(snapshot);
const server = await createServer({
  server: { middlewareMode: true },
  appType: "custom",
});
try {
  const detail = await server.ssrLoadModule("/src/NodeDetails.jsx");
  let count = 0;
  for (const node of model.nodes) {
    for (const component of [
      "NodeOverview",
      "NodeKnowledge",
      "NodeEvidence",
      "NodeSource",
      "NodeQuality",
    ]) {
      const html = renderToStaticMarkup(
        createElement(detail[component], { node, model, onSelect: () => {} }),
      );
      assert(!html.includes("[object Object]"));
      if (component === "NodeOverview") {
        assert(
          html.includes("待确认") ||
            node.comparison_progress.state === "complete",
        );
        assert(!html.includes("完整支持"));
        if (node.knowledge_role === "rollup" && !node.children.length) {
          assert(html.includes("子能力待生成"));
          assert(!html.includes("叶子节点，没有子节点"));
        }
      }
      if (component === "NodeSource") {
        assert(html.includes("树节点 · 全部字段"));
        assert(html.includes("知识记录 · 全部字段"));
        assert(html.includes(node.id));
      }
      count++;
    }
  }
  const { ValueFields } = await server.ssrLoadModule("/src/ValueFields.jsx");
  const html = renderToStaticMarkup(
    createElement(ValueFields, {
      value: {
        title: "<img src=x onerror=alert(1)>",
        url: "javascript:alert(1)",
      },
      model,
      onSelect: () => {},
    }),
  );
  assert(!html.includes("<img"));
  assert(!html.includes('href="javascript:'));
  assert(html.includes("&lt;img"));
  console.log(
    `Rendered ${count} Ant Design detail panels across ${model.nodes.length} nodes; source text escaping passed.`,
  );
} finally {
  await server.close();
}
