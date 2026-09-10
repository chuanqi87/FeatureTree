# 比较契约

业务契约 v3，Schema 在 config/v2/schemas/business-v3-{spec,claim,assessment,article}.schema.json。

支持结论为 supported、conditional、unsupported、unknown。比较结论为 same、different、unknown、not_applicable。公共问题以 kind、platforms、dimension 唯一标识；必答项必须完整回答，未知同样是一条需要评级的结论。

capability_result 描述场景是否达到相同可观察目标；api_surface 描述编程接口的形态。每组平台对独立比较，事实和推论通过 premise_ids 连接，依赖必须存在且无环。

证据定位保留 snapshot_id、document_id、url、body_sha256、excerpt、locator、platform、applicability、source_revision。来源不足和范围不适用是不同结果。输出文章通过固定结论集合生成，不另设可绕过依据和评级的自由断言正文。
