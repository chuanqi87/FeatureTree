# 管理台前端

- `main.jsx`：挂载应用与错误边界。
- `app/`：页面装配、导航和全局样式。
- `features/tree/`：特性树、筛选、关系图与节点详情。
- `features/knowledge/`：知识检索的页面和纯搜索逻辑。
- `features/workflow/`：发起分析、任务状态、阶段结果和操作。
- `shared/`：跨功能使用的格式化、质量筛选与展示组件。

功能自身的纯逻辑和组件放在同一功能目录。`shared/` 不反向导入 `features/` 或 `app/`；页面通过回调交互，浏览器不会直接读取项目文件或调用 OpenCode。

纯逻辑测试在 `tests/frontend/`；`web/scripts/check-render.mjs` 验证真实数据的详情面板渲染。
