import { Alert, Button, Input, Modal, Space, Typography } from "antd";
import { downloadReviewScope } from "../../shared/quality.js";

export default function ReviewScopePreview({ explorer }) {
  const scope = explorer.reviewScope;
  if (!scope || !explorer.reviewPreviewOpen) return null;
  const json = JSON.stringify(scope, null, 2);
  return (
    <Modal
      title="复核范围清单"
      centered
      open={explorer.reviewPreviewOpen}
      onCancel={() => explorer.setReviewPreviewOpen(false)}
      width={760}
      footer={
        <Space>
          <Button onClick={() => explorer.setReviewPreviewOpen(false)}>
            关闭
          </Button>
          <Button type="primary" onClick={() => downloadReviewScope(scope)}>
            下载 JSON
          </Button>
        </Space>
      }
    >
      <Alert
        type="info"
        showIcon
        title={`已选 ${scope.selected_claims} 项 / 匹配 ${scope.total_matching_claims} 项，未选 ${scope.omitted_claims} 项`}
        description="这只是范围清单，不会启动分析或真机测试。若浏览器未保存下载文件，可复制下方 JSON。"
      />
      <Typography.Paragraph style={{ marginTop: 16 }}>
        涉及 {scope.feature_ids.length}{" "}
        个节点；按复核优先级排序，不代表随机抽样。
      </Typography.Paragraph>
      <Typography.Paragraph copyable={{ text: json }}>
        复制清单 JSON
      </Typography.Paragraph>
      <Input.TextArea
        aria-label="复核清单 JSON"
        readOnly
        value={json}
        autoSize={{ minRows: 8, maxRows: 12 }}
      />
    </Modal>
  );
}
