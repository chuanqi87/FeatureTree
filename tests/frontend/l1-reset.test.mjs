import assert from "node:assert/strict";
import { test } from "node:test";
import {
  createModel,
  treeStats,
  visibleTree,
} from "../../web/src/features/tree/model.js";

test("unexpanded L1 domains remain branches in statistics and filtering", () => {
  const model = createModel({
    roots: ["sample"],
    nodes: [
      {
        id: "sample",
        parent: null,
        level: "L1",
        children: [],
        knowledge_role: "rollup",
        granularity: "branch",
        comparison_progress: { state: "unreviewed" },
      },
    ],
  });
  assert.equal(treeStats(model, "").total, 1);
  assert.equal(treeStats(model, "").leaves, 0);
  const options = { domain: "", query: "", collapsed: new Set() };
  assert.equal(visibleTree(model, { ...options, role: "leaf" }).rows.length, 0);
  assert.equal(
    visibleTree(model, { ...options, role: "rollup" }).rows.length,
    1,
  );
});
