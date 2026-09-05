import json
import tempfile
import unittest
from pathlib import Path

from featuretree.bindings import build_index
from featuretree.comparison import new_knowledge
from featuretree.generation import create_missing_knowledge, export_views, matrix_rows
from featuretree.inventory import classify_scope, prepare_row
from featuretree.mapping import map_row, propose_mapping
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
        for platform in self.config["platforms"]:
            write_json(self.root / f"inventory/{platform}/catalog.json", [])
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

    def test_backup_and_unmapped_files_do_not_count_as_inventory(self):
        for platform in self.config["platforms"]:
            write_json(self.root / f"inventory/{platform}/catalog.json", [])
            write_json(self.root / f"inventory/{platform}/catalog.seed-backup.json", [{"visibility": "public"}])
        write_json(self.root / "inventory/unmapped/android.json", [{"visibility": "public"}])
        self.assertEqual(self.repo.inventory(), [])

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


class MappingTests(unittest.TestCase):
    def setUp(self):
        self.rules = read_yaml(ROOT / "config/mapping-rules.yaml")["rules"]
        self.features = Repository().features()

    def row(self, native, platform="harmonyos"):
        return {"native_id": native, "platform": platform, "scope": "included", "mappings": []}

    def test_specific_job_rule_precedes_app_rule(self):
        row = self.row("android.app.job", "android")
        self.assertEqual(propose_mapping(row, self.features, self.rules)[0]["feature_id"], "app.background.deferred_work")

    def test_socket_is_not_http(self):
        row = self.row("@ohos.net.socket")
        self.assertEqual(propose_mapping(row, self.features, self.rules)[0]["feature_id"], "network.socket.tcp_udp")

    def test_unknown_module_stays_unmapped(self):
        self.assertEqual(propose_mapping(self.row("@ohos.unknownCapability"), self.features, self.rules), [])

    def test_missing_rule_target_does_not_fall_back(self):
        rules = [{"platform": "harmonyos", "pattern": "socket", "feature_id": "network.missing", "relationship": "capability"}]
        with self.assertRaises(ValueError):
            propose_mapping(self.row("@ohos.net.socket"), self.features, rules)

    def test_confirmed_manual_mapping_survives_rule_refresh(self):
        row = self.row("@ohos.net.socket")
        row["mappings"] = [{"feature_id": "network.socket", "method": "manual", "verification": "confirmed"}]
        self.assertEqual(map_row(row, self.features, self.rules)["mappings"], row["mappings"])

    def test_system_and_standard_library_scope_excluded(self):
        for native in ["apis-camera-kit/js-apis-camera-sys.md", "java.util"]:
            row = {**self.row(native), "title": "sample", "visibility": "public"}
            self.assertEqual(classify_scope(row)[0], "excluded")

    def test_catalog_proxy_remains_catalog_candidate(self):
        row = self.row("apis-camera-kit/js-apis-cameraPicker.md")
        row["parent"] = "apis-camera-kit"
        mapping = propose_mapping(row, self.features, self.rules)[0]
        self.assertEqual(mapping["feature_id"], "media.capture.camera")
        self.assertEqual(mapping["relationship"], "catalog")
        self.assertEqual(mapping["verification"], "candidate")

    def test_reverse_index_does_not_cap_or_discard_many_to_many(self):
        rows = []
        for i in range(20):
            rows.append({**self.row(f"module{i}"), "kind": "module", "url": "https://example.com", "visibility": "public",
                         "mappings": [{"feature_id": fid, "method": "rule", "verification": "candidate", "relationship": "catalog"}
                                      for fid in ["network", "network.socket"]]})
        self.assertEqual(len(build_index({}, rows)), 40)

    def test_reharvest_preserves_manual_scope_and_mapping(self):
        row = {**self.row("corebluetooth", "ios"), "title": "Core Bluetooth", "kind": "framework", "visibility": "public"}
        previous = {**row, "scope": "excluded", "scope_method": "manual", "scope_reason": "本批次不纳入",
                    "mappings": [{"feature_id": "connectivity", "method": "manual"}]}
        refreshed = prepare_row(row, ROOT, previous)
        self.assertEqual(refreshed["scope"], "excluded")
        self.assertEqual(refreshed["mappings"], previous["mappings"])
