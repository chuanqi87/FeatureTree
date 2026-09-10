import concurrent.futures
import tempfile
from pathlib import Path
import unittest
from unittest.mock import patch

from featuretree.core.content import digest
from featuretree.core.io import ConflictError, IntegrityError, read_json, write_json
from tests.fixtures.v2 import stores, schemas


class StorageTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.objects, self.versions = stores(self.root)

    def manifest(self, name, parent=None):
        return {"release_id": name, "parent_id": parent, "value": self.objects.put({"a": name})}

    def validate(self, manifest):
        self.objects.verify(manifest["value"])

    def publish(self, name, parent=None):
        self.versions.prepare(self.manifest(name, parent), parent, name)
        return self.versions.commit(name, self.validate)

    def test_canonical_identity_and_corruption_detection(self):
        self.assertEqual(digest({"a": 1, "b": 2}), digest({"b": 2, "a": 1}))
        reference = self.objects.put({"value": 1})
        self.assertEqual(reference, self.objects.put({"value": 1}))
        self.objects.path(reference).write_text('{"value":2}')
        with self.assertRaises(IntegrityError):
            self.objects.get(reference)
        with self.assertRaises(IntegrityError):
            self.objects.put({"value": 1})

    def test_prepare_is_invisible_and_idempotent(self):
        manifest = self.manifest("r_one")
        first = self.versions.prepare(manifest, None, "one")
        self.assertIsNone(self.versions.pin())
        self.assertEqual(first, self.versions.prepare(manifest, None, "one"))
        with self.assertRaises(ConflictError):
            self.versions.prepare(self.manifest("r_two"), None, "one")
        self.versions.commit("one", self.validate)
        self.assertEqual("r_one", self.versions.pin()["release_id"])

    def test_conflicting_candidates_never_overwrite_current(self):
        for name in ["r_one", "r_two"]:
            self.versions.prepare(self.manifest(name), None, name)
        with concurrent.futures.ThreadPoolExecutor(2) as pool:
            futures = [pool.submit(self.versions.commit, name, self.validate)
                       for name in ["r_one", "r_two"]]
            errors = [future.exception() for future in futures]
        self.assertEqual(1, sum(isinstance(error, ConflictError) for error in errors))
        self.validate(self.versions.pin())

    def test_recover_after_pointer_swap_and_later_publication(self):
        self.versions.prepare(self.manifest("r_one"), None, "one")
        original = write_json

        def fail_receipt(path, value, **kwargs):
            if path.name == "one.json" and value.get("state") == "committed":
                raise OSError("simulated crash")
            return original(path, value, **kwargs)

        with patch("featuretree.core.versions.write_json", side_effect=fail_receipt):
            with self.assertRaises(OSError):
                self.versions.commit("one", self.validate)
        self.assertEqual("r_one", self.versions.current_id())
        self.publish("r_two", "r_one")
        receipt = self.versions.commit("one", self.validate)
        self.assertEqual("committed", receipt["state"])
        self.assertEqual("r_two", self.versions.current_id())

    def test_missing_content_cannot_be_published(self):
        manifest = self.manifest("r_one")
        self.versions.prepare(manifest, None, "one")
        self.objects.path(manifest["value"]).unlink()
        with self.assertRaises(FileNotFoundError):
            self.versions.commit("one", self.validate)
        self.assertIsNone(self.versions.current_id())

    def test_schema_registry_rejects_v1_and_extra_model_authority(self):
        registry = schemas()
        self.assertIn("https://featuretree.local/schema/business/v3/article", registry.schemas)
        with self.assertRaises(ValueError):
            registry.validate("https://featuretree.local/schema/workflow/v2/fk-confidence",
                              {"protocol_version": 1, "overall_confidence": "high"})
