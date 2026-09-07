# 特性树结构验收报告

- generated_at: 2026-09-06T15:43:07.423735+00:00
- total_nodes: 1517
- atomic: 1246
- branch: 271
- L1 domains: 29
- tree_lint errors: 0 / warnings: 16
- legacy mapped: 212/212 missing: 0
- anchor_status counts: {'unverified': 590, 'failed': 670, 'url_ok': 232, 'body_ok': 10, 'symbol_ok': 15}

## 领域节点数

| domain | nodes |
| --- | ---: |
| a11y | 40 |
| ai | 49 |
| app | 78 |
| commerce | 35 |
| connectivity | 52 |
| device | 63 |
| digital_wellbeing | 40 |
| distributed | 56 |
| documents | 45 |
| enterprise | 40 |
| games | 40 |
| graphics | 79 |
| health_home | 45 |
| identity | 24 |
| input | 70 |
| interop | 28 |
| location | 62 |
| media | 82 |
| network | 63 |
| notifications | 64 |
| observability | 44 |
| print_scan | 25 |
| runtime | 40 |
| security | 69 |
| sensors | 60 |
| storage | 66 |
| telecom | 44 |
| ui | 85 |
| web | 29 |

## 层级分布

- L1: 29
- L2: 178
- L3: 1138
- L4: 172

## 跨域边界抽查

### midi
- `connectivity.peripherals.midi`
- `media.audio.midi`
- `sensors.environment.humidity`

### screen_record
- `graphics.capture.screen_record`
- `media.recording.screen`

### clipboard
- `distributed.share_experience.clipboard`
- `input.clipboard`
- `input.clipboard.change_listen`
- `input.clipboard.clear`
- `input.clipboard.delayed`
- `input.clipboard.paste_button`
- `input.clipboard.read_write`
- `input.clipboard.sensitive_flag`
- `input.clipboard.types`
- `security.data_protection.clipboard_redact`

### pdf
- `documents.generate.html_to_pdf`
- `documents.generate.image_pdf`
- `documents.generate.pdf_create`
- `documents.parse.pdf`
- `graphics.pdf`
- `graphics.pdf.document_view`
- `graphics.pdf.page_render`
- `print_scan.print.pdf_output`
- `storage.document.pdf_mutate`
- `storage.document.pdf_view`

### haptics
- `a11y.hearing.music_haptics`
- `input.gamepad.vibration`
- `sensors.haptics`
- `sensors.haptics.audio_coupled`
- `sensors.haptics.cancel`
- `sensors.haptics.capability`
- `sensors.haptics.effects`
- `sensors.haptics.engine`
- `sensors.haptics.intensity`
- `sensors.haptics.pattern`
- `sensors.haptics.primitive`
- `sensors.haptics.ui_feedback`
- `sensors.haptics.vibrate`

### cloud_sync
- `distributed.data_sync.cloud_bridge`
- `storage.cloud.sync`

### certificates
- `enterprise.device_policy.certificates`
- `security.certificates`
- `security.certificates.ct`
- `security.certificates.parse`
- `security.certificates.pinning`
- `security.certificates.storage`
- `security.certificates.user_install`

## 验收结论

- 结构：`tree_lint` 无 error，29 个 L1 均有子树。
- 旧 212 ID：全部有 legacy 去向（见 `legacy-disposition.md`）。
- 锚点：大量 `unverified`/`failed` 为设计阶段预期；`verify_anchors.py` 已跑通并回写 `anchor_status`，失败节点保留待模型/人工补核。
- 规模：约 1517 总节点 / 1246 atomic，低于规划信号 2000，但是完整可浏览骨架；后续按域加深，不推翻 ID。
- **ID 冻结：允许知识生产启动；锚点状态可继续原地更新。**

## lint 警告摘要

- wide_branch: 10
- duplicate_name: 5
- single_child_branch: 1
