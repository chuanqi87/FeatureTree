import { useCallback, useEffect, useState } from "react";
import { get } from "./api.js";
export function useResource(path, interval = 0) {
  const [result, setResult] = useState({ path: null, data: null });
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const [revision, setRevision] = useState(0);
  const refresh = useCallback(() => setRevision(value => value + 1), []);
  useEffect(() => {
    if (!path) { setResult({ path: null, data: null }); return; }
    const controller = new AbortController();
    setLoading(true); setError(null);
    get(path, controller.signal).then(data => { if (!controller.signal.aborted) setResult({ path, data }); }).catch(error => {
      if (error.name !== "AbortError") setError(error.message);
    }).finally(() => { if (!controller.signal.aborted) setLoading(false); });
    return () => controller.abort();
  }, [path, revision]);
  useEffect(() => {
    if (!interval) return;
    const timer = setInterval(refresh, interval);
    return () => clearInterval(timer);
  }, [interval, refresh]);
  return { data: result.path === path ? result.data : null, error, loading: loading || (!!path && result.path !== path), refresh };
}
