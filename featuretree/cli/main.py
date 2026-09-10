"""v2 command-line parsing and dependency assembly only."""

import argparse
import json
from pathlib import Path
from uuid import uuid4

from featuretree.cli.commands import execute
from featuretree.console.application import Application

GROUPS = {
    'sources': ('import', 'extract', 'capture', 'seal', 'validate', 'query', 'report'),
    'workflow': ('plan', 'replan', 'run', 'resume', 'retry', 'revise', 'revalidate', 'supplement', 'cancel', 'report'),
    'taxonomy': ('check', 'diff', 'freeze', 'approve-calibration', 'policies'),
    'knowledge': ('plan', 'show', 'check', 'impact', 'import-observation'),
    'review': ('queue', 'show', 'decide', 'research'),
    'release': ('prepare', 'publish', 'rebase', 'show', 'compare', 'rollback', 'export'),
    'console': ('serve',),
}


def main(argv=None):
    parser = argparse.ArgumentParser(description='FeatureTree v2：来源、具名 Agent、叶子知识与人工审核')
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    groups = parser.add_subparsers(dest='group', required=True)
    for name, operations in GROUPS.items():
        group = groups.add_parser(name)
        group.add_argument('action', choices=operations)
        group.add_argument('--id')
        group.add_argument('--request', type=Path, help='包含完整工作单或操作参数的 JSON 文件')
        group.add_argument('--key', default=None, help='重复操作使用相同幂等键')
        group.add_argument('--expected', help='预期正式发布 ID；none 表示尚未发布')
        group.add_argument('--snapshot')
        group.add_argument('--query', default='')
        group.add_argument('--platform', choices=('android', 'ios', 'harmonyos'))
        group.add_argument('--cursor')
        group.add_argument('--limit', type=int, default=50)
        group.add_argument('--reference', type=Path)
        group.add_argument('--before')
        group.add_argument('--after')
        group.add_argument('--port', type=int, default=8765)
    args = parser.parse_args(argv)
    application = Application(args.root)
    try:
        result = execute(application, args, args.key or uuid4().hex)
    except (ValueError, KeyError, FileNotFoundError) as error:
        parser.exit(2, f'{type(error).__name__}: {error}\n')
    if result is not None:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0
