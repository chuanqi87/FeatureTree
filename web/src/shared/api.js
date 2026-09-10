export async function get(path, signal) {
  const response = await fetch(`/api/v2/${path}`, { signal });
  const value = await response.json();
  if (!response.ok) throw new Error(value.error || `请求失败 (${response.status})`);
  return value;
}
export async function post(path, body, expectedReleaseId, key = crypto.randomUUID()) {
  const config = await get("config");
  const response = await fetch(`/api/v2/${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json", "X-FeatureTree-Token": config.write_token, "Idempotency-Key": key },
    body: JSON.stringify({ expected_release_id: expectedReleaseId, ...body }),
  });
  const value = await response.json();
  if (!response.ok) throw new Error(value.error || `操作失败 (${response.status})`);
  return value;
}
