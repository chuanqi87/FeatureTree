"""One-time v1 -> v2 conversion, preserving assertions as unverified history."""

import copy
import hashlib
import json

from .inventory import prepare_row
from .storage import read_yaml, write_json, write_yaml

SUBJECTS = {
    "ui.declarative.vs_imperative": ("状态驱动界面更新", "State-driven UI Updates",
        "将应用状态变化同步为界面变化，并维护状态与显示的一致性。",
        ["状态与界面绑定", "更新触发与更新范围", "状态保存与组件生命周期的协作"], ["按钮等具体控件的属性全集"]),
    "runtime.concurrency.overview": ("异步任务调度与协作", "Asynchronous Task Coordination",
        "创建、调度和协调异步任务，处理取消、结果传递与共享状态。",
        ["任务调度", "取消与结果传递", "共享状态协调"], ["特定语言语法与标准库全集"]),
    "interop.action_dispatch.component_intent": ("目标组件调用", "Target Component Invocation",
        "定位并调用应用组件，传递调用参数并处理无法找到目标等结果。",
        ["显式指定目标组件", "按声明的能力解析目标", "参数传递与调用结果"],
        ["仅通过 URL 打开资源", "智能助理触发的系统能力注册"]),
    "distributed.softbus": ("跨设备通信", "Cross-device Communication",
        "建立设备间通信会话，传输数据并调用远端能力。",
        ["设备间会话", "跨设备数据传输与远端调用"], ["应用界面与任务接续"]),
    "distributed.softbus.fabric": ("跨设备调用与数据传输", "Cross-device Calls and Data Transfer",
        "在多个设备之间调用远端能力、传输消息或数据流，并处理连接中断。",
        ["远端能力调用", "消息与数据流传输", "连接中断处理"], ["某一厂商总线实现的内部机制"]),
}

SCOPES = {
    "connectivity.bluetooth.le.scan": (["发现附近 BLE 广播设备", "开始与停止扫描", "接收扫描结果"], ["建立连接", "读取 GATT 数据"]),
    "connectivity.bluetooth.le.scan.filter": (["按条件筛选扫描结果", "过滤条件的组合与执行位置"], ["批量结果交付", "后台执行资格"]),
    "connectivity.bluetooth.le.scan.batch": (["将扫描结果聚合后批量交付"], ["过滤条件种类"]),
    "connectivity.bluetooth.le.scan.background": (["非前台状态下发现 BLE 设备", "挂起、唤醒和停止条件"], ["后台任务框架全集"]),
    "ui.controls.button": (["表达可点击操作", "触发动作和表达交互状态"], ["每个框架的属性与修饰符全集"]),
    "ui.imperative": (["显式创建、更新与销毁界面对象"], ["与声明式框架的总体比较文章"]),
}


def attach_snapshot(evidence, root):
    tail = evidence["url"].rstrip("/").split("/")[-1]
    candidates = [f"docs-raw/ios/frameworks/{tail.lower()}.md",
                  f"docs-raw/android/guide-pages/{tail}.md",
                  f"docs-raw/harmonyos/api-index/modules/{tail}"]
    for relative in candidates:
        path = root / relative
        if path.is_file():
            evidence["local_path"] = relative
            evidence["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
            break


def migrate_nodes(repo):
    platforms = repo.config()["platforms"]
    dimensions = list(repo.config()["dimensions"])
    inventory_ids = {(r["platform"], r["native_id"]) for p in platforms
                     for r in json.loads((repo.root / f"inventory/{p}/catalog.json").read_text())}
    migrated = 0
    for path in sorted((repo.root / "taxonomy").glob("*.yaml")):
        if path.name.startswith("_"):
            continue
        domain = read_yaml(path)
        changed = False
        for feature in domain["features"]:
            if feature.get("schema_version") == 2:
                continue
            fid = feature["id"]
            knowledge_path = repo.root / feature["knowledge_path"]
            knowledge = read_yaml(knowledge_path)
            knowledge["legacy_presence"] = copy.deepcopy(knowledge["presence"])
            if knowledge["definition"] != feature["definition"]:
                knowledge["legacy_definition"] = knowledge["definition"]
            feature.pop("status_by_platform")
            feature.pop("knowledge_status")
            if fid in SUBJECTS:
                zh, en, definition, includes, excludes = SUBJECTS[fid]
                knowledge["legacy_definition"] = knowledge["definition"]
                feature["aliases"] = list(dict.fromkeys(feature.get("aliases", []) + [feature["name"]["zh"]]))
                feature.update(name={"zh": zh, "en": en}, definition=definition)
                feature["comparison_scope"] = {"includes": includes, "excludes": excludes}
                feature["notes"] = "保留历史 ID 以维持引用；节点名称和比较对象已中立化。"
            else:
                includes, excludes = SCOPES.get(fid, ([feature["definition"]], []))
                feature["comparison_scope"] = {"includes": includes, "excludes": excludes}
            if fid == "ui.imperative":
                feature["knowledge_role"] = "leaf"
            feature["schema_version"] = 2
            feature["comparison_dimensions"] = dimensions[:]
            # Remove imported catalog copies. The complete index joins inventory directly.
            for platform, bindings in list(feature.get("bindings", {}).items()):
                kept = [b for b in bindings if b.get("role") != "related"
                        or (platform, b["id"]) not in inventory_ids]
                if kept:
                    feature["bindings"][platform] = kept
                else:
                    del feature["bindings"][platform]
            knowledge.update(schema_version=2, definition=feature["definition"],
                             role=feature["knowledge_role"], comparisons=[],
                             presence={p: {"status": "unknown", "verification": "unreviewed"} for p in platforms})
            knowledge["migration_notes"] = [
                "v1 有无与 analog/unique 断言保存在 legacy_presence，不作为已确认结论。",
                "原正文、编辑状态及 baseline 保留；需按当前比较范围与固定版本逐项复核。",
            ]
            evidence = knowledge.setdefault("evidence", [])
            for index, item in enumerate(evidence, 1):
                item["id"] = f"{item['platform']}-{index}"
                attach_snapshot(item, repo.root)
            write_yaml(knowledge_path, knowledge)
            migrated += 1
            changed = True
        if changed:
            write_yaml(path, domain)
    return migrated


def migrate_inventory(repo):
    counts = {}
    for platform in repo.config()["platforms"]:
        path = repo.root / f"inventory/{platform}/catalog.json"
        rows = json.loads(path.read_text())
        migrated = [row if row.get("schema_version") == 2 else prepare_row(row, repo.root) for row in rows]
        if any(row.get("schema_version") != 2 for row in rows):
            write_json(path, migrated)
        counts[platform] = len(rows)
    return counts
