"""Write validated view projections to rebuildable export artifacts."""

from featuretree.taxonomy.bindings import build_index
from featuretree.knowledge.validation import require_valid_knowledge
from featuretree.core.paths import EXPORTS_DIR
from featuretree.core.storage import write_json, write_text
from featuretree.reporting.views import csv_text, matrix_rows, tree_view


def export_views(repo):
    features = repo.features()
    knowledge, paths = repo.knowledge()
    config = repo.config()
    require_valid_knowledge(repo, features, knowledge, paths, config)
    platforms = config["platforms"]
    support, comparisons = matrix_rows(features, knowledge, platforms)
    output = repo.root / EXPORTS_DIR
    write_json(output / "index.json", build_index(features))
    write_json(output / "tree.json", tree_view(features, knowledge, platforms))
    write_text(output / "presence_matrix.csv", csv_text(support, list(support[0])))
    write_text(output / "comparison_matrix.csv", csv_text(comparisons, list(comparisons[0])))
    from featuretree.reporting.review import build_scope
    write_json(output / "review_queue.json", build_scope(features, knowledge, platforms))
