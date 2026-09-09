import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { createModel, visibleTree, tableData, treeStats } from "./model.js";
import { reviewSelection } from "../../shared/quality.js";

const hashNode = () =>
  new URLSearchParams(window.location.hash.slice(1)).get("node") || "";

export function useExplorer() {
  const [model, setModel] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [domain, setDomain] = useState("");
  const [query, setQuery] = useState("");
  const [progressState, setProgressState] = useState("");
  const [confidence, setConfidence] = useState("");
  const [deviceReview, setDeviceReview] = useState("");
  const [role, setRole] = useState("");
  const [reviewLimit, setReviewLimit] = useState(null);
  const [reviewPreviewOpen, setReviewPreviewOpen] = useState(false);
  const [collapsed, setCollapsed] = useState(new Set());
  const [selected, setSelected] = useState(hashNode);
  const [drawerOpen, setDrawerOpen] = useState(false);
  const [view, setView] = useState("table");
  const tableRef = useRef(null);

  const refresh = useCallback(async () => {
    setLoading(true);
    try {
      const response = await fetch("/api/tree", { cache: "no-store" });
      const snapshot = await response.json();
      if (!response.ok)
        throw new Error(snapshot.error || `读取失败（${response.status}）`);
      const next = createModel(snapshot);
      setModel(next);
      setDomain((current) => (next.byId.has(current) ? current : ""));
      setSelected((current) =>
        next.byId.has(current) ? current : next.roots[0] || "",
      );
      setError("");
    } catch (problem) {
      setError(problem.message);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    setModel(null);
    setError("");
    refresh();
  }, [refresh]);

  const selectNode = useCallback(
    (id) => {
      if (!model?.byId.has(id)) return;
      setSelected(id);
      setDrawerOpen(true);
      window.history.replaceState(null, "", `#node=${encodeURIComponent(id)}`);
    },
    [model],
  );

  useEffect(() => {
    const onHash = () => selectNode(hashNode());
    window.addEventListener("hashchange", onHash);
    return () => window.removeEventListener("hashchange", onHash);
  }, [selectNode]);

  const filtering = Boolean(
    query.trim() || progressState || confidence || deviceReview || role,
  );
  const tree = useMemo(
    () =>
      model
        ? visibleTree(model, {
            domain,
            query,
            collapsed,
            progressState,
            confidence,
            deviceReview,
            role,
          })
        : { rows: [], matchedIds: [], matchCount: 0, scopeCount: 0 },
    [
      model,
      domain,
      query,
      collapsed,
      progressState,
      confidence,
      deviceReview,
      role,
    ],
  );
  const data = useMemo(
    () =>
      model
        ? tableData(
            visibleTree(model, {
              domain,
              query,
              collapsed: new Set(),
              progressState,
              confidence,
              deviceReview,
              role,
            }).rows,
          )
        : [],
    [model, domain, query, progressState, confidence, deviceReview, role],
  );
  const reviewScope = useMemo(
    () =>
      model
        ? reviewSelection(
            model,
            tree.matchedIds,
            { domain, query, progressState, confidence, deviceReview, role },
            reviewLimit,
          )
        : null,
    [
      model,
      tree,
      domain,
      query,
      progressState,
      confidence,
      deviceReview,
      role,
      reviewLimit,
    ],
  );
  const expandedKeys = useMemo(
    () =>
      model
        ? model.nodes
            .filter(
              (node) =>
                node.children.length && (filtering || !collapsed.has(node.id)),
            )
            .map((node) => node.id)
        : [],
    [model, collapsed, filtering],
  );
  const stats = useMemo(
    () => (model ? treeStats(model, domain) : null),
    [model, domain],
  );

  function changeDomain(id) {
    setDomain(id);
    setDrawerOpen(false);
    tableRef.current?.scrollTo({ top: 0 });
  }

  function resetFilters() {
    setQuery("");
    setProgressState("");
    setConfidence("");
    setDeviceReview("");
    setRole("");
    setReviewLimit(null);
  }

  function locateNode(id = selected) {
    if (!model?.byId.has(id)) return;
    resetFilters();
    setDomain("");
    setView("table");
    setDrawerOpen(false);
    setSelected(id);
    setCollapsed((current) => {
      const next = new Set(current);
      model.ancestors.get(id).forEach((parent) => next.delete(parent));
      return next;
    });
    window.requestAnimationFrame(() => tableRef.current?.scrollTo({ key: id }));
  }

  function expandNode(expanded, node) {
    if (filtering) return;
    setCollapsed((current) => {
      const next = new Set(current);
      if (expanded) next.delete(node.id);
      else next.add(node.id);
      return next;
    });
  }

  return {
    model,
    loading,
    error,
    domain,
    query,
    progressState,
    confidence,
    deviceReview,
    role,
    reviewLimit,
    reviewScope,
    reviewPreviewOpen,
    setReviewPreviewOpen,
    selected,
    drawerOpen,
    view,
    tableRef,
    filtering,
    tree,
    data,
    expandedKeys,
    stats,
    refresh,
    selectNode,
    changeDomain,
    resetFilters,
    locateNode,
    expandNode,
    setQuery,
    setProgressState,
    setConfidence,
    setDeviceReview,
    setRole,
    setReviewLimit,
    exportReviewScope: () => setReviewPreviewOpen(true),
    setDrawerOpen,
    setView,
    expandAll: () => setCollapsed(new Set()),
    collapseAll: () =>
      setCollapsed(
        new Set(
          model?.nodes
            .filter((node) => node.children.length)
            .map((node) => node.id),
        ),
      ),
  };
}
