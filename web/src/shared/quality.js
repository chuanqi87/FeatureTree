/** Shared claim-level filters and export selection; ancestor rows are navigation only. */
export const confidenceOptions = [
  { value: "", label: "全部置信度" },
  { value: "high", label: "含高可信结论" },
  { value: "medium", label: "含中可信结论" },
  { value: "low", label: "含低可信结论" },
  { value: "unassessed", label: "含未评估项" },
];

export const deviceReviewOptions = [
  { value: "", label: "全部复核需求" },
  { value: "required", label: "必须真机复核 · 待做" },
  { value: "recommended", label: "建议抽样 · 待做" },
  { value: "failed", label: "实测不符 · 优先排查" },
  { value: "passed", label: "计划样本已通过" },
  { value: "not_required", label: "无需真机复核" },
  { value: "unassessed", label: "复核需求未评估" },
];

export function matchingClaims(
  node,
  { confidence = "", deviceReview = "" } = {},
) {
  return (node.quality_claims ?? []).filter((claim) => {
    if (confidence && claim.confidence !== confidence) return false;
    if (["required", "recommended"].includes(deviceReview))
      return (
        claim.device_requirement === deviceReview &&
        claim.device_state === "pending"
      );
    return !deviceReview || claim.device_state === deviceReview;
  });
}

export function reviewSelection(model, matchedIds, filters, limit = null) {
  const claims = [...matchedIds].flatMap((id) =>
    matchingClaims(model.byId.get(id), filters),
  );
  claims.sort(
    (a, b) =>
      a.priority - b.priority ||
      a.feature_id.localeCompare(b.feature_id, "en") ||
      a.claim_id.localeCompare(b.claim_id, "en"),
  );
  const selected = limit ? claims.slice(0, limit) : claims;
  return {
    schema_version: 1,
    generated_at: new Date().toISOString(),
    filters: { ...filters, limit },
    total_matching_claims: claims.length,
    selected_claims: selected.length,
    omitted_claims: claims.length - selected.length,
    feature_ids: [...new Set(selected.map((c) => c.feature_id))].sort(),
    claims: selected,
    notice:
      "仅导出真正匹配的知识项，不包括用于导航的祖先。未启动研究或真机测试；样本通过不能外推全部机型。",
  };
}

export function downloadReviewScope(scope) {
  const url = URL.createObjectURL(
    new Blob([JSON.stringify(scope, null, 2)], { type: "application/json" }),
  );
  const link = document.createElement("a");
  link.href = url;
  link.download = "featuretree-review-scope.json";
  document.body.append(link);
  link.click();
  link.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}
