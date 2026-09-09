import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { test } from "node:test";
import { fileURLToPath } from "node:url";
import {
  createModel,
  visibleTree,
  graphLayout,
  treeStats,
  tableData,
} from "../../web/src/features/tree/model.js";
import { safeUrl } from "../../web/src/shared/format.js";
import {
  buildKnowledgeIndex,
  searchKnowledge,
} from "../../web/src/features/knowledge/search.js";
import {
  matchingClaims,
  reviewSelection,
} from "../../web/src/shared/quality.js";

const root = fileURLToPath(new URL("../..", import.meta.url));
const snapshot = JSON.parse(
  execFileSync(
    `${root}/.venv/bin/python`,
    [
      "-c",
      "import json; from tests.fixtures.viewer import snapshot; print(json.dumps(snapshot()))",
    ],
    { cwd: root, maxBuffer: 20_000_000 },
  ),
);
const model = createModel(snapshot);
const options = { domain: "", query: "", collapsed: new Set() };
const knowledgeIndex = buildKnowledgeIndex(model);

test("natural-language keyword query ranks the relevant difference node first", () => {
  const results = searchKnowledge(knowledgeIndex, "样例扫描过滤有哪些差异？");
  assert.equal(results[0].node.id, "sample.group.stage.operation.filter");
  const comparison = results[0].snippets.find((item) =>
    item.field.startsWith("comparisons["),
  );
  assert(comparison);
  assert.equal(comparison.verification, "in_review");
  assert.equal(comparison.sourcePath, results[0].node.knowledge_path);
});

test("knowledge search finds API text and preserves source locations", () => {
  const results = searchKnowledge(knowledgeIndex, "readSampleRecord");
  assert.equal(results[0].node.id, "sample.group.stage.operation.filter");
  assert(
    results[0].snippets.some((item) => item.field === "programming_model"),
  );
  assert.equal(results[0].node.platforms.ios.status, "unknown");
});

test("search ignores archived support claims and handles empty and unknown queries", () => {
  const snapshot = structuredClone(model.nodes[0]);
  snapshot.knowledge.legacy_presence = {
    android: { rationale: "ARCHIVEDONLYWORD" },
  };
  const index = buildKnowledgeIndex({ nodes: [snapshot] });
  assert.equal(searchKnowledge(index, "ARCHIVEDONLYWORD").length, 0);
  for (const query of ["", "   ", "?！", "ZXQ987火星量子打印装置"]) {
    assert.equal(searchKnowledge(knowledgeIndex, query).length, 0);
  }
});

test("full tree includes every record once, with depths derived from parent relationships", () => {
  const { rows } = visibleTree(model, options);
  assert.equal(rows.length, snapshot.nodes.length);
  assert.equal(
    new Set(rows.map((row) => row.node.id)).size,
    snapshot.nodes.length,
  );
  for (const row of rows)
    assert.equal(row.depth + 1, Number(row.node.level.slice(1)));
  assert.equal(treeStats(model, "").depth, 5);
});

test("deep knowledge search retains the entire ancestor path even when collapsed", () => {
  const collapsed = new Set(snapshot.nodes.map((node) => node.id));
  const { rows } = visibleTree(model, {
    ...options,
    query: "readSampleRecord",
    collapsed,
  });
  const target = "sample.group.stage.operation.filter";
  assert(rows.some((row) => row.node.id === target));
  for (const parent of model.ancestors.get(target))
    assert(rows.some((row) => row.node.id === parent));
  assert.equal(rows.find((row) => row.node.id === target).depth, 4);
});

test("domain scoping, collapse and empty results do not leak unrelated nodes", () => {
  const { rows } = visibleTree(model, {
    ...options,
    domain: "sample",
    collapsed: new Set(["sample.group"]),
  });
  assert(
    rows.every(
      (row) =>
        row.node.id === "sample" ||
        model.ancestors.get(row.node.id).includes("sample"),
    ),
  );
  assert(
    !rows.some((row) => row.node.id === "sample.group.stage.operation.filter"),
  );
  assert.equal(
    visibleTree(model, { ...options, query: "definitely-absent-987654321" })
      .rows.length,
    0,
  );
  assert.equal(
    visibleTree(model, { ...options, collapsed: new Set(model.roots) }).rows
      .length,
    model.roots.length,
  );
});

test("graph has every visible node and separates every sibling card", () => {
  const { rows } = visibleTree(model, options);
  const { positions } = graphLayout(rows);
  assert.equal(positions.size, rows.length);
  for (const node of model.nodes) {
    const parent = positions.get(node.id);
    for (const child of node.children)
      assert(positions.get(child).x > parent.x);
  }
  for (const depth of new Set(rows.map((row) => row.depth))) {
    const column = [...positions.values()]
      .filter((p) => p.row.depth === depth)
      .sort((a, b) => a.y - b.y);
    for (let index = 1; index < column.length; index++)
      assert(column[index].y - column[index - 1].y >= 62);
  }
});

test("Ant Design tree data retains every node and original child IDs", () => {
  const data = tableData(visibleTree(model, options).rows);
  const visit = (nodes) =>
    nodes.flatMap((node) => [node, ...visit(node.treeChildren ?? [])]);
  const records = visit(data);
  assert.equal(records.length, snapshot.nodes.length);
  for (const node of records) {
    assert.deepEqual(node.children, model.byId.get(node.id).children);
    assert.deepEqual(
      (node.treeChildren ?? []).map((child) => child.id),
      node.children,
    );
  }
});

test("status filter retains paths and does not interpret legacy claims as confirmed", () => {
  const result = visibleTree(model, {
    ...options,
    progressState: "in_progress",
    collapsed: new Set(model.roots),
  });
  assert(result.matchCount > 0);
  assert(
    result.rows.some(
      (row) => row.node.id === "sample.group.stage.operation.filter",
    ),
  );
  for (const row of result.rows.filter((row) => row.match))
    assert.equal(row.node.comparison_progress.state, "in_progress");
  assert.equal(
    visibleTree(model, { ...options, progressState: "complete" }).matchCount,
    0,
  );
});

test("unsafe URLs cannot become active source links", () => {
  assert.equal(safeUrl("javascript:alert(1)"), null);
  assert.equal(safeUrl("data:text/html,<script>bad()</script>"), null);
  assert.equal(
    safeUrl("https://developer.android.com/"),
    "https://developer.android.com/",
  );
});

test("quality filters require both conditions on the same claim", () => {
  const node = {
    quality_claims: [
      {
        confidence: "high",
        device_requirement: "not_required",
        device_state: "not_required",
      },
      {
        confidence: "low",
        device_requirement: "required",
        device_state: "pending",
      },
    ],
  };
  assert.equal(
    matchingClaims(node, { confidence: "high", deviceReview: "required" })
      .length,
    0,
  );
  assert.equal(
    matchingClaims(node, { confidence: "low", deviceReview: "required" })
      .length,
    1,
  );
  node.quality_claims[1].device_state = "passed";
  assert.equal(matchingClaims(node, { deviceReview: "required" }).length, 0);
  assert.equal(matchingClaims(node, { deviceReview: "passed" }).length, 1);
});

test("scope export excludes navigation ancestors and observes claim budget", () => {
  const filters = {
    ...options,
    domain: "sample",
    role: "leaf",
    confidence: "unassessed",
  };
  const tree = visibleTree(model, filters);
  assert(tree.rows.some((row) => !row.match));
  const scope = reviewSelection(model, tree.matchedIds, filters, 5);
  assert.equal(scope.selected_claims, 5);
  assert(scope.omitted_claims > 0);
  assert(scope.claims.every((claim) => claim.role === "leaf"));
  assert(!scope.feature_ids.includes("sample"));
  const collapsed = visibleTree(model, {
    ...filters,
    collapsed: new Set(model.roots),
  });
  assert.deepEqual(collapsed.matchedIds, tree.matchedIds);
});

test("an exact feature ID does not export parents mentioning it in child_index", () => {
  const id = "sample.group.stage.operation.filter";
  const filters = { ...options, query: id };
  const result = visibleTree(model, filters);
  assert.deepEqual(result.matchedIds, [id]);
  assert.equal(result.rows.length, 5);
  const scope = reviewSelection(model, result.matchedIds, filters, 5);
  assert.deepEqual(scope.feature_ids, [id]);
  assert.equal(scope.total_matching_claims, 24);
});

test("unassessed fixtures are never treated as high confidence or no device review", () => {
  const fixture = structuredClone(snapshot.nodes[0]);
  fixture.parent = null;
  fixture.children = [];
  fixture.quality_claims = [
    {
      confidence: "unassessed",
      device_requirement: "unassessed",
      device_state: "unassessed",
    },
  ];
  fixture.knowledge = { programming_model: "LEGACYPROSE", comparisons: [] };
  const ungraded = createModel({
    ...snapshot,
    roots: [fixture.id],
    nodes: [fixture],
  });
  assert.equal(
    visibleTree(ungraded, { ...options, confidence: "high" }).matchCount,
    0,
  );
  assert.equal(
    visibleTree(ungraded, { ...options, deviceReview: "not_required" })
      .matchCount,
    0,
  );
  assert.equal(
    visibleTree(ungraded, { ...options, confidence: "unassessed" }).matchCount,
    1,
  );
  const snippets = searchKnowledge(
    buildKnowledgeIndex(ungraded),
    "LEGACYPROSE",
  )[0].snippets;
  assert(snippets.every((snippet) => snippet.confidence === "unassessed"));
});
