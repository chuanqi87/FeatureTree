"""Node-triggered workflow commands, with bounded background execution."""

from featuretree.console.launcher import ProcessLauncher

from datetime import date
import re
import subprocess

from featuretree.core.storage import Repository, write_json
from featuretree.taxonomy.traversal import ancestor_chain
from featuretree.workflow.state import digest, lock, read_json, rule_hash, run_path, save_state
from featuretree.console.runs import details, read_state, summarize
from featuretree.workflow.recovery import reset_tasks
from featuretree.workflow.planning import make_plan
from featuretree.workflow.publication import publish


class RunConflict(ValueError):
    pass


class WorkflowConsole:
    def __init__(self, root, launcher=None, slots=6):
        self.root = root.resolve()
        self.launcher = launcher or ProcessLauncher()
        self.slots = slots

    def options(self):
        baseline = read_json(self.root / "config/workflow/baseline.example.json")
        baseline["as_of"] = date.today().isoformat()
        presets = [{"id": "design-unknown", "label": "设计基线（版本待核实）", "baseline": baseline}]
        for path in sorted((self.root / "config/workflow/baselines").glob("*.json")):
            presets.append({"id": path.stem, "label": path.stem, "baseline": read_json(path)})
        return {"available": self.launcher.available(), "slots": self.slots, "baselines": presets,
                "defaults": {"depth": 1, "max_nodes": 12, "workers": min(3, self.slots), "timeout": 600,
                             "first_response_timeout": 120}}

    def states(self):
        result = []
        for path in sorted((self.root / ".workflow/runs").glob("*/state.json"), reverse=True):
            try:
                result.append(read_state(self.root, path.parent.name))
            except (ValueError, OSError, KeyError):
                continue
        return result

    def list_runs(self, node=None):
        current_rules = rule_hash(self.root)
        rows = [summarize(folder, state, current_rules, self.launcher.active(folder))
                for folder, state in self.states() if node is None or node in state["nodes"]
                or node == (state.get("trigger") or {}).get("source_node")]
        return sorted(rows, key=lambda r: r["created_at"], reverse=True)

    def get_run(self, run_id):
        folder, state = read_state(self.root, run_id)
        summary = summarize(folder, state, rule_hash(self.root), self.launcher.active(folder))
        return details(folder, state, summary)

    def resolve_targets(self, nodes, action):
        features = Repository(self.root).features()
        if not isinstance(nodes, list) or not nodes or any(not isinstance(n, str) or n not in features for n in nodes):
            raise ValueError("请选择当前树中存在的节点")
        targets = []
        for node in nodes:
            if action == "root":
                node = ancestor_chain(features, node)[-1]
            if node not in targets:
                targets.append(node)
        return targets

    def check_capacity(self, nodes, workers, exclude=None):
        active = [s for f, s in self.states() if s["id"] != exclude and self.launcher.active(f)]
        features = Repository(self.root).features()
        scopes = set(nodes) | {n for state in active for n in state["nodes"]}
        ancestors = {node: set(ancestor_chain(features, node)) for node in scopes}
        for state in active:
            if any(a in ancestors[b] or b in ancestors[a] for a in nodes for b in state["nodes"]):
                raise RunConflict(f"相关节点已有执行中的任务：{state['id']}，请查看该任务")
        if sum(s["workers"] for s in active) + workers > self.slots:
            raise RunConflict(f"当前执行容量已满（最多 {self.slots} 个并发单元），请等待现有任务完成")

    def start(self, run_id):
        folder = run_path(self.root, run_id)
        try:
            self.launcher.start(self.root, run_id)
            (folder / "console-error.json").unlink(missing_ok=True)
        except (OSError, subprocess.SubprocessError) as exc:
            write_json(folder / "console-error.json", {"error": str(exc)})
            raise ValueError(f"任务已保存为 {run_id}，执行进程启动失败：{exc}") from exc

    def create(self, body):
        allowed = {"nodes", "action", "source_node", "baseline_id", "request_id", "depth",
                   "max_nodes", "workers", "timeout", "first_response_timeout", "model", "variant", "parent_run"}
        if set(body) - allowed:
            raise ValueError("包含未知的执行参数")
        action = body.get("action", "drilldown")
        if action not in ("drilldown", "root"):
            raise ValueError("不支持的分析类型")
        request_id = body.get("request_id", "")
        if not isinstance(request_id, str) or not re.fullmatch(r"[a-zA-Z0-9_-]{16,80}", request_id):
            raise ValueError("缺少有效的请求编号")
        options = self.options()
        values = {k: body.get(k, v) for k, v in options["defaults"].items()}
        if any(type(v) is not int for v in values.values()):
            raise ValueError("层数、节点预算、并发数和超时必须为整数")
        model, variant = body.get("model") or None, body.get("variant") or None
        if model is not None and (not isinstance(model, str) or not re.fullmatch(r"[\w.-]+/[\w.:/-]+", model)):
            raise ValueError("模型格式应为 provider/model")
        if variant is not None and (not isinstance(variant, str) or not re.fullmatch(r"[\w.-]{1,60}", variant)):
            raise ValueError("无效的推理配置")
        baselines = {p["id"]: p["baseline"] for p in options["baselines"]}
        baseline = baselines.get(body.get("baseline_id"))
        parent_run = body.get("parent_run")
        if parent_run:
            parent = self.get_run(parent_run)
            allowed_nodes = {r["node_id"] for r in parent["next_work_orders"]}
            if not parent.get("published") or not set(body.get("nodes", [])) <= allowed_nodes or action != "drilldown":
                raise ValueError("下一层只能分析已合并父批次的待展开分支")
            baseline = parent["baseline"]
        if baseline is None:
            raise ValueError("请选择可用的版本基线")
        with lock(self.root / ".workflow/console.lock"):
            for _, state in self.states():
                if state.get("request_id") == request_id:
                    if state["request_hash"] != digest(body):
                        raise RunConflict("相同请求编号不能用于不同参数")
                    return self.get_run(state["id"])
            if not options["available"]:
                raise ValueError("未找到 OpenCode，请先在本机配置后重新启动管理台")
            nodes = self.resolve_targets(body.get("nodes"), action)
            self.check_capacity(nodes, values["workers"])
            state = make_plan(self.root, nodes, baseline, **values, model=model, variant=variant)
            state.update(request_id=request_id, request_hash=digest(body), parent_run=parent_run,
                         trigger={"action": action, "source_node": body.get("source_node")})
            save_state(run_path(self.root, state["id"]), state)
            self.start(state["id"])
            return self.get_run(state["id"])

    def act(self, run_id, action, body):
        if set(body) - {"nodes"}:
            raise ValueError("包含未知的任务操作参数")
        if action == "revise" and not body.get("nodes"):
            raise ValueError("请指定需要返工的节点")
        with lock(self.root / ".workflow/console.lock"):
            run = self.get_run(run_id)
            if action not in run["actions"] or not run["actions"][action]:
                raise RunConflict("任务状态已变化或规则已更新，请刷新后重试")
            if action == "publish":
                publish(self.root, run_id)
            else:
                if not self.launcher.available():
                    raise ValueError("未找到 OpenCode")
                self.check_capacity(run["nodes"], run["workers"], exclude=run_id)
                if action in ("retry", "revise"):
                    reset_tasks(self.root, run_id, body.get("nodes") if action == "revise" else None)
                self.start(run_id)
            return self.get_run(run_id)
