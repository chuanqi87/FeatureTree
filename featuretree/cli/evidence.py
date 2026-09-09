"""Export selected immutable evidence bytes; authors never need to retype hashes."""

import argparse
from datetime import date
import json
from featuretree.corpus.store import Corpus
from featuretree.knowledge.research_profile import fingerprint
from featuretree.core.storage import ROOT, contained_path, write_json
from featuretree.corpus.evidence import export_source, note_urls


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", nargs="*")
    parser.add_argument("--notes", action="append", default=[])
    parser.add_argument("--run-date", default=date.today().isoformat())
    args = parser.parse_args(argv)
    urls = set(args.url)
    try:
        for note in args.notes:
            urls.update(note_urls(contained_path(ROOT, note, "output/research")))
        if not urls:
            raise ValueError("Select at least one URL or evidence-table note")
        corpus = Corpus(ROOT / "docs-raw/official")
        try:
            records = [export_source(corpus, ROOT, url, args.run_date) for url in sorted(urls)]
        finally:
            corpus.close()
        manifest = {"sources": records, "semantic_review_passed": False, "version_verified": False}
        path = ROOT / "output/research/source-indexes" / (fingerprint(manifest) + ".json")
        write_json(path, manifest)
        print(json.dumps({"index": str(path), "sources": len(records), "version_verified": False}))
        return 0
    except (ValueError, OSError, KeyError) as exc:
        print(json.dumps({"error": str(exc)}))
        return 2
