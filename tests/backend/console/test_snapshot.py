"""Snapshot integrity and local HTTP boundaries for the viewer."""

import json
import tempfile
import threading
import unittest
from datetime import date
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import urlopen

from featuretree.knowledge.comparison import new_knowledge
from featuretree.core.storage import ROOT, Repository, write_yaml
from featuretree.console.snapshot import build_snapshot, json_default
from featuretree.console.server import create_server
from tests.fixtures.knowledge import feature


class ViewerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = Repository(self.root)
        self.config = {"platforms": {"android": {"name": "Android"}, "ios": {"name": "iOS"}},
                       "dimensions": {"availability": "支持范围"}}
        self.feature = feature()
        self.doc = new_knowledge(self.feature, self.config["platforms"])
        self.doc.update(legacy_presence={"android": {"status": "full"}}, api_surface="author text")
        write_yaml(self.root / "config/comparison.yaml", self.config)
        self.save()

    def save(self):
        write_yaml(self.root / "taxonomy/sample.yaml", {"features": [self.feature]})
        write_yaml(self.root / "knowledge/sample.yaml", self.doc)

    def test_reads_authored_sources_without_requiring_generated_bindings(self):
        snapshot = build_snapshot(self.repo)
        node = snapshot["nodes"][0]
        self.assertEqual(node["knowledge"], self.doc)
        self.assertEqual(node["platforms"]["android"]["status"], "unknown")
        self.assertEqual(node["comparison_progress"]["confirmed_support"], 0)
        self.assertFalse((self.root / "output").exists())
        self.doc["api_surface"] = "new author text"
        self.save()
        self.assertEqual(build_snapshot(self.repo)["nodes"][0]["knowledge"]["api_surface"], "new author text")

    def test_invalid_parent_is_reported_instead_of_silently_hiding_nodes(self):
        self.feature["parent"] = "missing"
        self.save()
        with self.assertRaisesRegex(ValueError, "Missing parent"):
            build_snapshot(self.repo)

    def test_repository_snapshot_contains_every_node_and_full_knowledge(self):
        repo = Repository()
        features = repo.features()
        docs, _ = repo.knowledge()
        snapshot = build_snapshot(repo)
        self.assertEqual({n["id"] for n in snapshot["nodes"]}, set(features))
        for node in snapshot["nodes"]:
            self.assertEqual(node["knowledge"], docs[node["id"]])
        self.assertEqual(snapshot["roots"][0], "app")

    def test_empty_repository_and_yaml_dates_serialize(self):
        write_yaml(self.root / "taxonomy/sample.yaml", {"features": []})
        (self.root / "knowledge/sample.yaml").unlink()
        self.assertEqual(build_snapshot(self.repo)["nodes"], [])
        self.assertEqual(json.loads(json.dumps({"date": date(2026, 9, 5)}, default=json_default))["date"], "2026-09-05")

    def test_http_serves_ui_and_live_data_without_exposing_repository(self):
        server = create_server(self.repo, ROOT / "web", port=0)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        origin = f"http://127.0.0.1:{server.server_port}"
        with urlopen(origin + "/") as response:
            self.assertEqual(response.status, 200)
            self.assertIn("text/html", response.headers["Content-Type"])
        with urlopen(origin + "/api/tree") as response:
            self.assertEqual(len(json.load(response)["nodes"]), 1)
            self.assertEqual(response.headers["Cache-Control"], "no-store")
        for path in ["/api/draft-tree", "/../README.md", "/%2e%2e/config/comparison.yaml", "/.git/config", "/knowledge/sample.yaml"]:
            with self.assertRaises(HTTPError) as error:
                urlopen(origin + path)
            self.assertEqual(error.exception.code, 404)
            error.exception.close()
        self.feature["parent"] = "missing"
        self.save()
        with self.assertRaises(HTTPError) as error:
            urlopen(origin + "/api/tree")
        self.assertEqual(error.exception.code, 500)
        self.assertIn("Missing parent", json.load(error.exception)["error"])
        error.exception.close()
