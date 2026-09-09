"""Initialize missing stubs, rebuild exports and validate authored data."""

from featuretree.cli.audit import parser as audit_parser, run as audit_run
from featuretree.core.storage import Repository
from featuretree.knowledge.initialization import create_missing_knowledge
from featuretree.reporting.exports import export_views


def main(argv=None):
    args = audit_parser(__doc__).parse_args(argv)
    repo = Repository()
    print(f"Created {len(create_missing_knowledge(repo))} missing knowledge files.")
    export_views(repo)
    return audit_run(args)
