/** Keyword retrieval over current node definitions, knowledge and comparisons. */
import { label } from "../../shared/format.js";

const normalize = (value) => String(value ?? "").toLocaleLowerCase();
const genericTerms = new Set([
  "差异",
  "支持",
  "情况",
  "平台",
  "特性",
  "节点",
  "什么",
  "哪些",
]);
const searchableFields = [
  "programming_model",
  "lifecycle_background",
  "permissions_privacy",
  "limits_precision",
  "api_surface",
  "architecture_diff",
  "device_forms",
  "unique_extensions",
  "porting_traps",
  "baseline",
];

function queryTerms(query) {
  const text = normalize(query).replace(
    /有哪些|有什么|是什么|请问|告诉我|介绍一下/g,
    " ",
  );
  const terms = text.match(/[a-z0-9_@./+-]+/g) ?? [];
  for (const phrase of text.match(/[\u4e00-\u9fff]+/g) ?? []) {
    if (phrase.length === 1) terms.push(phrase);
    else
      for (let i = 0; i < phrase.length - 1; i++)
        terms.push(phrase.slice(i, i + 2));
  }
  const unique = [...new Set(terms)];
  const specific = unique.filter((term) => !genericTerms.has(term));
  return specific.length ? specific : unique;
}

function readable(value) {
  if (Array.isArray(value))
    return value.map(readable).filter(Boolean).join("；");
  if (value && typeof value === "object")
    return Object.entries(value)
      .map(([key, item]) => `${label(key)}：${readable(item)}`)
      .join("；");
  return String(value ?? "");
}

function fragment(section, field, value) {
  const text = readable(value);
  if (!text.trim() || /\bstub\b|待按域填写|待填写|待补充/i.test(text))
    return null;
  return { section, field, text, searchable: normalize(text) };
}

export function buildKnowledgeIndex(model) {
  return (model?.nodes ?? []).map((node) => {
    const fragments = [
      fragment("能力定义", "definition", node.definition),
      fragment("比较范围", "comparison_scope", node.comparison_scope),
      fragment("别名", "aliases", node.aliases),
      ...searchableFields.map((field) =>
        fragment(label(field), field, node.knowledge[field]),
      ),
      fragment("精选 API 绑定", "bindings", node.bindings),
      ...(node.knowledge.comparisons ?? []).map((finding, index) => ({
        ...fragment(
          `跨平台比较 · ${label(finding.dimension)}`,
          `comparisons[${index}]`,
          `${finding.platforms.map(label).join(" ↔ ")}；${label(finding.result)}；${finding.scope ?? ""}；${finding.rationale ?? ""}`,
        ),
        verification: finding.verification,
        confidence: finding.assessment?.confidence ?? "unassessed",
      })),
      ...(node.knowledge.facts ?? []).map((fact, index) => ({
        ...fragment(
          `平台事实 · ${label(fact.platform)}`,
          `facts[${index}]`,
          fact.statement,
        ),
        verification: fact.verification,
        confidence: fact.assessment?.confidence ?? "unassessed",
      })),
    ]
      .filter((item) => item?.text)
      .map((item) => ({
        confidence: "unassessed",
        ...item,
        sourcePath: [
          "definition",
          "comparison_scope",
          "aliases",
          "bindings",
        ].includes(item.field)
          ? `taxonomy/${node.id.split(".")[0]}.yaml`
          : node.knowledge_path,
      }));
    return {
      node,
      fragments,
      identity: normalize(
        [node.id, node.name.zh, node.name.en, ...(node.aliases ?? [])].join(
          " ",
        ),
      ),
      searchable: normalize(
        [
          node.id,
          node.name.zh,
          node.name.en,
          ...fragments.map((item) => item.text),
        ].join(" "),
      ),
    };
  });
}

export function searchKnowledge(index, query) {
  const terms = queryTerms(query.trim());
  if (!terms.length) return [];
  const weights = new Map(
    terms.map((term) => [
      term,
      1 +
        Math.log(
          (index.length + 1) /
            (index.filter((item) => item.searchable.includes(term)).length + 1),
        ),
    ]),
  );
  const totalWeight = [...weights.values()].reduce(
    (sum, weight) => sum + weight,
    0,
  );
  const scoreText = (text) =>
    terms.reduce(
      (score, term) => score + (text.includes(term) ? weights.get(term) : 0),
      0,
    );
  return index
    .flatMap((record) => {
      const matched = scoreText(record.searchable);
      if (!matched || matched / totalWeight < 0.2) return [];
      const snippets = record.fragments
        .map((item) => ({ ...item, score: scoreText(item.searchable) }))
        .filter((item) => item.score > 0)
        .sort((a, b) => b.score - a.score)
        .slice(0, 3);
      const exactName = [
        record.node.name.zh,
        record.node.name.en,
        record.node.id,
      ].some((name) => normalize(query).includes(normalize(name)));
      return [
        {
          node: record.node,
          snippets,
          score:
            scoreText(record.identity) * 5 + matched + (exactName ? 30 : 0),
        },
      ];
    })
    .sort((a, b) => b.score - a.score || a.node.id.localeCompare(b.node.id));
}
