# OpenCode 执行依赖

当前执行后端与插件固定为 1.18.29。安装：`npm ci --prefix tools/opencode --ignore-scripts --no-audit --no-fund`。

每次 Agent 调用拥有独立的提示、task.json、工具文件、OpenCode 会话和响应目录；仅 node_modules 通过相对符号链接共享，避免每次复制约 61 MB 依赖。package.json 与锁文件仍复制到该次工作区，锁文件哈希进入工作单和实际执行元数据。运行前核对 CLI 与插件版本，漂移时拒绝执行并要求验证后重新计划。

Provider 凭证沿用用户 OpenCode 配置，不复制到运行记录。HTTP 401/402/403/404 不自动重试；错误类别和服务端状态保留，诊断文字过滤凭证。余额恢复或更换模型后使用新修订工作单承接，不能修改旧工作单的模型和指纹。
