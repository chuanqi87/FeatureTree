"""Export selected immutable evidence bytes; authors never need to retype hashes."""

import argparse
from datetime import date
import gzip
import hashlib
import json
import shutil

from .corpus.store import Corpus
from .research_profile import fingerprint
from .storage import ROOT, contained_path, write_json


def export_source(corpus, root, url, run_date):
    date.fromisoformat(run_date)
    row = corpus.get(url)
    if not row or row["status"] != "ready":
        raise ValueError(f"No ready official body for {url}")
    corpus.body(row)  # verifies the normalized body before returning any reference
    raw = contained_path(corpus.root, row["raw_path"], "snapshots")
    if hashlib.sha256(gzip.decompress(raw.read_bytes())).hexdigest() != row["raw_sha256"]:
        raise ValueError(f"Raw snapshot hash mismatch: {url}")
    directory = root / "docs-raw/research" / run_date / row["id"] / row["body_sha256"]
    directory.mkdir(parents=True, exist_ok=True)
    body = contained_path(corpus.root, row["body_path"], "snapshots")
    for source, target in ((body, directory / "document.md"), (raw, directory / "source.gz")):
        if target.exists():
            if source.read_bytes() != target.read_bytes():
                raise ValueError(f"Refusing to replace immutable snapshot: {target}")
        else:
            shutil.copyfile(source, target)
    record = {"id": row["id"], "url": row["url"], "platform": row["platform"],
              "title": row["title"], "local_path": (directory / "document.md").relative_to(root).as_posix(),
              "sha256": row["body_sha256"], "raw_sha256": row["raw_sha256"],
              "raw_path": (directory / "source.gz").relative_to(root).as_posix(),
              "fetched_at": row["fetched_at"], "version_verified": False,
              "notice": "Snapshot integrity only; read body and independently verify locator, excerpt and applicability."}
    metadata_path = directory / "source.json"
    if metadata_path.exists() and json.loads(metadata_path.read_text(encoding="utf-8")) != record:
        raise ValueError(f"Refusing to replace immutable metadata: {metadata_path}")
    write_json(metadata_path, record)
    return record


def note_urls(path):
    """Only extract URL cells from evidence tables, never execute source content."""
    urls = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("|"):
            urls.update(cell.strip() for cell in line.split("|") if cell.strip().startswith("https://"))
    return sorted(urls)


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
