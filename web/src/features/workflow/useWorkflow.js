import { useCallback, useEffect, useRef, useState } from "react";

async function request(path, options = {}) {
  const response = await fetch(`/api/workflow/${path}`, {
    cache: "no-store",
    ...options,
  });
  const result = await response.json();
  if (!response.ok)
    throw new Error(result.error || `请求失败（${response.status}）`);
  return result;
}

export function useWorkflow() {
  const [config, setConfig] = useState(null);
  const [runs, setRuns] = useState([]);
  const [selected, setSelected] = useState(
    () => new URLSearchParams(location.hash.slice(1)).get("run") || "",
  );
  const [detail, setDetail] = useState(null);
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);
  const [loading, setLoading] = useState(true);
  const generation = useRef(0);
  const submission = useRef(null);

  useEffect(() => {
    const onHash = () => {
      const params = new URLSearchParams(location.hash.slice(1));
      if (params.get("page") === "workflow")
        setSelected(params.get("run") || "");
    };
    window.addEventListener("hashchange", onHash);
    return () => window.removeEventListener("hashchange", onHash);
  }, []);

  const refresh = useCallback(
    async (signal) => {
      const version = ++generation.current;
      try {
        const [settings, listing, current] = await Promise.all([
          request("config", { signal }),
          request("runs", { signal }),
          selected
            ? request(`runs/${encodeURIComponent(selected)}`, { signal })
            : Promise.resolve(null),
        ]);
        if (version !== generation.current) return;
        setConfig(settings);
        setRuns(listing.runs);
        setDetail(current);
        setError("");
      } catch (problem) {
        if (problem.name !== "AbortError" && version === generation.current)
          setError(problem.message);
      } finally {
        if (version === generation.current) setLoading(false);
      }
    },
    [selected],
  );

  useEffect(() => {
    setDetail(null);
    const controller = new AbortController();
    refresh(controller.signal);
    const timer = setInterval(() => refresh(controller.signal), 4000);
    return () => {
      controller.abort();
      clearInterval(timer);
      generation.current += 1;
    };
  }, [refresh]);

  async function post(path, body) {
    if (!config) throw new Error("执行配置尚未加载，请稍后重试");
    setBusy(true);
    try {
      const result = await request(path, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-Workflow-Token": config.csrf_token,
        },
        body: JSON.stringify(body),
      });
      generation.current += 1;
      setSelected(result.id);
      setDetail(result);
      setRuns((rows) => [result, ...rows.filter((r) => r.id !== result.id)]);
      return result;
    } finally {
      setBusy(false);
    }
  }

  async function create(body) {
    const key = JSON.stringify(body);
    if (submission.current?.key !== key)
      submission.current = { key, id: crypto.randomUUID() };
    const result = await post("runs", {
      ...body,
      request_id: submission.current.id,
    });
    submission.current = null;
    return result;
  }

  return {
    config,
    runs,
    selected,
    detail,
    error,
    busy,
    loading,
    create,
    select: setSelected,
    refresh: () => refresh(),
    act: (id, action, body = {}) =>
      post(`runs/${encodeURIComponent(id)}/${action}`, body),
  };
}
