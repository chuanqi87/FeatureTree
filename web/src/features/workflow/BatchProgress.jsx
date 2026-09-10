import { Typography } from "antd";

export default function BatchProgress({ progress }) {
  if (!progress) return null;
  return <Typography.Text type={progress.status === "failed" ? "danger" : "secondary"}>
    已校验批次 {progress.completed} / {progress.total}
    {progress.reused > 0 && ` · 复用 ${progress.reused} 批`}
    {progress.status === "running" && ` · 当前第 ${progress.current} 批`}
    {progress.status === "failed" && ` · 第 ${progress.current} 批失败，已完成批次保留`}
  </Typography.Text>;
}
