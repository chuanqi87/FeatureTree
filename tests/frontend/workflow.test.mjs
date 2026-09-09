import assert from "node:assert/strict";
import test from "node:test";
import {
  analysisTargets,
  nodeRuns,
  stageNames,
} from "../../web/src/features/workflow/model.js";

const model = {
  byId: new Map(
    ["sample", "sample.branch", "sample.branch.item", "other"].map((id) => [
      id,
      { id },
    ]),
  ),
  ancestors: new Map([
    ["sample", []],
    ["sample.branch", ["sample"]],
    ["sample.branch.item", ["sample", "sample.branch"]],
    ["other", []],
  ]),
};
test("root analysis resolves real ancestry and deduplicates shared domains", () => {
  assert.deepEqual(
    analysisTargets(
      model,
      ["sample.branch.item", "sample.branch", "other"],
      "root",
    ),
    ["sample", "other"],
  );
  assert.deepEqual(
    analysisTargets(model, ["sample.branch", "missing"], "drilldown"),
    ["sample.branch"],
  );
});
test("node history includes root analysis initiated from that node", () => {
  const runs = [
    { id: "a", nodes: ["sample"], trigger: { source_node: "sample.branch" } },
    { id: "b", nodes: ["other"] },
  ];
  assert.deepEqual(
    nodeRuns(runs, "sample.branch").map((r) => r.id),
    ["a"],
  );
  assert.deepEqual(nodeRuns(runs, "sample.branch.item"), []);
  assert.equal(Object.keys(stageNames).length, 8);
});
