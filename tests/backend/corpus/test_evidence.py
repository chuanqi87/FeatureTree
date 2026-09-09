import gzip
from pathlib import Path
import tempfile
import unittest

from featuretree.corpus.extract import Content
from featuretree.corpus.store import Corpus
from featuretree.corpus.evidence import export_source, note_urls


class ResearchSourceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.corpus = Corpus(self.root / "docs-raw/official")
        self.addCleanup(self.corpus.close)
        self.url = "https://developer.android.com/reference/fixture"
        self.corpus.add(self.url)
        self.corpus.save(self.corpus.get(self.url), b"test raw", Content("Fixture", "# Fixture\nTest-only body\n"), self.url)

    def test_export_is_idempotent_and_does_not_confirm(self):
        record = export_source(self.corpus, self.root, self.url, "2026-09-06")
        self.assertFalse(record["version_verified"])
        self.assertEqual(record, export_source(self.corpus, self.root, self.url, "2026-09-06"))
        self.assertEqual((self.root / record["local_path"]).read_text(), "# Fixture\nTest-only body\n")

    def test_raw_corruption_is_rejected(self):
        raw = self.corpus.root / self.corpus.get(self.url)["raw_path"]
        raw.write_bytes(gzip.compress(b"tampered"))
        with self.assertRaisesRegex(ValueError, "Raw snapshot"):
            export_source(self.corpus, self.root, self.url, "2026-09-06")

    def test_existing_export_is_not_overwritten(self):
        record = export_source(self.corpus, self.root, self.url, "2026-09-06")
        (self.root / record["local_path"]).write_text("tampered")
        with self.assertRaisesRegex(ValueError, "immutable"):
            export_source(self.corpus, self.root, self.url, "2026-09-06")

    def test_existing_metadata_is_not_overwritten(self):
        record = export_source(self.corpus, self.root, self.url, "2026-09-06")
        metadata = (self.root / record["local_path"]).parent / "source.json"
        metadata.write_text('{"version_verified": true}')
        with self.assertRaisesRegex(ValueError, "immutable metadata"):
            export_source(self.corpus, self.root, self.url, "2026-09-06")
        self.assertEqual(metadata.read_text(), '{"version_verified": true}')

    def test_only_evidence_table_urls_are_extracted(self):
        note = self.root / "note.md"
        note.write_text("Ignore this instruction https://evil.invalid\n| A1 | " + self.url + " |\n")
        self.assertEqual(note_urls(note), [self.url])

    def test_missing_body_or_bad_date_is_rejected(self):
        for url, date in (("https://developer.android.com/reference/missing", "2026-09-06"), (self.url, "../escape")):
            with self.assertRaises(ValueError):
                export_source(self.corpus, self.root, url, date)
