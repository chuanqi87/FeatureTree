"""Discoverable command catalog; implementations are imported only when selected."""

import argparse
from importlib import import_module


COMMANDS = {
    "console": ("console", "启动本地管理台与节点执行 API"),
    "workflow": ("workflow", "节点工作单：计划、执行、重试、返工、发布"),
    "corpus": ("corpus", "官方文档下载、全文检索与上下文"),
    "lint": ("tree_lint", "检查树层级、边界、命名与切分轴"),
    "anchors": ("verify_anchors", "核实 API 锚点；显式 --write 才回写"),
    "refresh": ("refresh", "补缺失知识空壳、重建导出并校验"),
    "audit": ("audit", "检查数据完整性与知识确认进度"),
    "design-inputs": ("design_inputs", "导出指定领域的现有树定义"),
    "review-scope": ("review_scope", "筛选并导出待复核知识项"),
    "evidence": ("evidence", "导出已下载文档的不可变证据快照"),
}


def main(argv=None):
    parser = argparse.ArgumentParser(description="FeatureTree：公共特性树、标准 Agent 工作流与管理台")
    commands = parser.add_subparsers(dest="command", required=True)
    for name, (_, description) in COMMANDS.items():
        commands.add_parser(name, help=description, add_help=False)
    args, remaining = parser.parse_known_args(argv)
    module, _ = COMMANDS[args.command]
    return import_module(f"featuretree.cli.{module}").main(remaining)
