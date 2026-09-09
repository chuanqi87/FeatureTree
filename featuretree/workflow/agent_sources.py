"""Bounded official-corpus lookup for the OpenCode read-only custom tool."""

import argparse
import json

from featuretree.core.storage import ROOT
from featuretree.corpus.search import locate
from featuretree.workflow.retrieval import select_sources, source_packet
from featuretree.workflow.sources import corpus_reader
from featuretree.workflow.stages import PLATFORMS


def lookup(root, platform, query):
    if platform not in PLATFORMS or not 1 <= len(query.strip()) <= 180:
        raise ValueError("Use one platform and a short API/module query")
    with corpus_reader(root) as corpus:
        if corpus is None:
            return {"sources": [], "gaps": ["Official corpus unavailable; no support conclusion"]}
        selected, exclusions = select_sources(corpus, [query], platform, limit=2)
        sources = [source_packet(corpus, row, q) for q, row in selected]
        return {"query": query, "platform": platform, "sources": sources,
                "catalog": locate(corpus, query, platform, limit=6), "exclusions": exclusions,
                "interpretation": "Read-only source candidates, not verified platform claims"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("platform", choices=PLATFORMS)
    parser.add_argument("query")
    args = parser.parse_args()
    print(json.dumps(lookup(ROOT, args.platform, args.query), ensure_ascii=False))


if __name__ == "__main__":
    main()
