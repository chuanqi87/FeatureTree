import json
import tempfile
import unittest
from pathlib import Path

from featuretree.bindings import build_index
from featuretree.comparison import new_knowledge
from featuretree.generation import create_missing_knowledge, export_views, matrix_rows
from featuretree.storage import ROOT, Repository, read_yaml, write_json, write_yaml
from featuretree.validation import validate_tree
from tests.test_comparison import feature


class RepositoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = Repository(self.root)
        self.config = {"platforms": {"android": {}, "ios": {}}, "dimensions": {"availability": "支持"}}
        write_yaml(self.root / "config/comparison.yaml", self.config)
        write_yaml(self.root / "taxonomy/sample.yaml", {"domain": "sample", "features": [feature()]})

    def test_generator_preserves_draft_comments_and_edits_byte_for_byte(self):
        path = self.root / "knowledge/sample.yaml"
        doc = new_knowledge(feature(), self.config["platforms"])
        doc.update(status="draft", api_surface="人工修订内容")
        write_yaml(path, doc)
        original = path.read_bytes() + b"\n# Author comment\n"
        path.write_bytes(original)
        self.assertEqual(create_missing_knowledge(self.repo), [])
        self.assertEqual(path.read_bytes(), original)

    def test_missing_knowledge_is_created_as_unknown(self):
        self.assertEqual(create_missing_knowledge(self.repo), ["sample"])
        doc = read_yaml(self.root / "knowledge/sample.yaml")
        self.assertEqual(doc["presence"]["android"]["status"], "unknown")

    def test_export_views_uses_output_without_overwriting_sources_or_reports(self):
        create_missing_knowledge(self.repo)
        history = self.root / "output/reports/migration_verification.json"
        write_json(history, {"historical_assertions_preserved": True})
        protected = [history, self.root / "taxonomy/sample.yaml", self.root / "knowledge/sample.yaml"]
        original = {path: path.read_bytes() for path in protected}

        export_views(self.repo)

        output = self.root / "output/exports"
        self.assertEqual({path.name for path in output.iterdir()},
                         {"index.json", "tree.json", "presence_matrix.csv", "comparison_matrix.csv", "review_queue.json"})
        self.assertEqual(json.loads((output / "tree.json").read_text())[0]["id"], "sample")
        self.assertFalse((self.root / "bindings").exists())
        self.assertEqual({path: path.read_bytes() for path in protected}, original)

    def test_duplicate_yaml_keys_and_feature_ids_fail(self):
        path = self.root / "bad.yaml"
        path.write_text("id: first\nid: second\n")
        with self.assertRaises(ValueError):
            read_yaml(path)
        write_yaml(self.root / "taxonomy/sample.yaml", {"features": [feature(), feature()]})
        with self.assertRaises(ValueError):
            self.repo.features()

    def test_cycle_and_depth_mismatch_fail(self):
        a, b = feature(), feature()
        a["parent"] = "sample.child"
        b.update(id="sample.child", parent="sample")
        features = {a["id"]: a, b["id"]: b}
        errors = validate_tree(features, {}, {}, self.config)
        self.assertTrue(any("cycle" in e for e in errors))
        self.assertTrue(any("depth" in e for e in errors))

    def test_all_node_roles_are_exported(self):
        parent, child = feature(), feature()
        parent["knowledge_role"] = "rollup"
        child.update(id="sample.child", level="L2", parent="sample")
        features = {f["id"]: f for f in [parent, child]}
        docs = {fid: new_knowledge(f, self.config["platforms"]) for fid, f in features.items()}
        support, comparisons = matrix_rows(features, docs, self.config["platforms"])
        self.assertEqual({r["feature_id"] for r in support}, set(features))
        self.assertEqual(len(comparisons), 2)

    def test_pending_l1_is_valid_but_empty_nested_rollup_is_not(self):
        parent = feature()
        parent.update(knowledge_role="rollup", granularity="branch")
        docs = {"sample": new_knowledge(parent, self.config["platforms"])}
        paths = {"sample": parent["knowledge_path"]}
        self.assertEqual(validate_tree({"sample": parent}, docs, paths, self.config), [])

        child = feature()
        child.update(id="sample.child", parent="sample", level="L2", knowledge_role="rollup",
                     granularity="branch", knowledge_path="knowledge/sample/child.yaml")
        docs[child["id"]] = new_knowledge(child, self.config["platforms"])
        paths[child["id"]] = child["knowledge_path"]
        errors = validate_tree({"sample": parent, child["id"]: child}, docs, paths, self.config)
        self.assertIn("Rollup has no children: sample.child", errors)


class BindingTests(unittest.TestCase):
    def test_reverse_index_keeps_all_authored_associations(self):
        features = {
            f"sample.item{i}": {"bindings": {"android": [{"id": "SharedApi", "kind": "class", "url": "https://example.com/api"}]}}
            for i in range(20)
        }
        rows = build_index(features)
        self.assertEqual(len(rows), 20)
        self.assertEqual({row["feature_id"] for row in rows}, set(features))
        self.assertTrue(all(row["sources"][0]["origin"] == "taxonomy" for row in rows))
