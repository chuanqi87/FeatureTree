"""Large durable deliveries pass the original contract without a JSON chat reply."""

from copy import deepcopy
import json
from pathlib import Path
import sys
import tempfile
import unittest

from jsonschema import ValidationError

from featuretree.core.io import IntegrityError, read_json
from featuretree.workflow.attempt_tools import configure_agent
from featuretree.workflow.backends.delivery import save_chunk, finalize_delivery, read_delivery
from featuretree.workflow.backends.errors import OutputLimitError
from featuretree.workflow.backends.opencode import OpenCodeBackend, parse_events
from tests.fixtures.v2_application import application, run
from tests.fixtures.v2_pipeline import ModelSubstitute


def packet():
    result = {"protocol_version": 2, "run_id": "run_test", "work_id": "w_0",
              "task_id": "w_0--ft-android", "stage_id": "ft-android", "input_hash": "a" * 64,
              "limits": {"max_delivery_chunks": 40, "max_output_tokens": 16000, "first_response_timeout": 5}}
    result["output_schema"] = {"type": "object", "required": [
        "protocol_version", "run_id", "work_id", "task_id", "stage_id", "input_hash", "payload", "outcome", "issues", "source_requests"],
        "properties": {"payload": {"type": "object", "required": ["rows", "spec"], "additionalProperties": False,
            "properties": {"rows": {"type": "array", "minItems": 2, "uniqueItems": True,
                                    "items": {"type": "string"}},
                           "spec": {"type": "object", "required": ["title"],
                                    "properties": {"title": {"type": "string"}}}}}}}
    return result


class FileDeliveryTests(unittest.TestCase):
    def test_full_tree_and_knowledge_chain_validate_file_deliveries(self):
        class FileSubstitute(ModelSubstitute):
            def execute(self, root, agent, packet, folder, timeout, model, variant):
                response, metadata = super().execute(root, agent, packet, folder, timeout, model, variant)
                references = [save_chunk(root, packet, [key], value)["chunk_ref"]
                              for key, value in response["payload"].items()]
                finalize_delivery(root, packet, references, response["outcome"], response["issues"], response["source_requests"])
                restored, _ = read_delivery(root, packet)
                return restored, {**metadata, "transport": "file"}

        with tempfile.TemporaryDirectory() as directory:
            app, snapshot, baseline = application(Path(directory))
            app.runner.executor.backend = FileSubstitute()
            _, check = run(app, snapshot, {"baseline_ref": baseline}, "file-tree")
            tree = app.artifacts.get(check["tree_ref"])
            inputs = {key: check[key] for key in ("tree_ref", "bindings_ref")}
            inputs.update(baseline_ref=baseline, feature_ref=app.artifacts.put(tree["features"][0]))
            _, article = run(app, snapshot, inputs, "file-knowledge", "knowledge")
            self.assertTrue(app.artifacts.get(article["article_ref"])["draft"])

    def test_large_file_combines_chunks_in_explicit_order_and_rejects_tampering(self):
        with tempfile.TemporaryDirectory() as directory:
            root, p = Path(directory), packet()
            values = [str(i) + "x" * 12000 for i in range(12)]
            refs = [save_chunk(root, p, ["rows"], [value])["chunk_ref"] for value in values]
            refs.append(save_chunk(root, p, ["spec", "title"], "Title")["chunk_ref"])
            finalize_delivery(root, p, refs, "pass", [], [])
            response, used = read_delivery(root, p)
            self.assertEqual(values, response["payload"]["rows"])
            self.assertEqual(refs, used)
            self.assertGreater(len(json.dumps(response)), 140000)
            path = root / "delivery" / (refs[0] + ".json")
            record = read_json(path)
            record["value"] = ["changed"]
            path.write_text(json.dumps(record))
            with self.assertRaises(IntegrityError):
                read_delivery(root, p)

    def test_incomplete_and_duplicate_collections_do_not_create_completion_file(self):
        with tempfile.TemporaryDirectory() as directory:
            root, p = Path(directory), packet()
            ref = save_chunk(root, p, ["rows"], ["one"])["chunk_ref"]
            with self.assertRaises(ValidationError):
                finalize_delivery(root, p, [ref], "pass", [], [])
            with self.assertRaises(ValueError):
                finalize_delivery(root, p, [ref, ref], "pass", [], [])
            self.assertFalse((root / "delivery/completed.json").exists())

    def test_wrong_input_and_overlapping_fields_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root, p = Path(directory), packet()
            refs = [save_chunk(root, p, ["rows"], ["one", "two"])["chunk_ref"],
                    save_chunk(root, p, ["spec"], {"title": "Title"})["chunk_ref"]]
            other = deepcopy(p)
            other["input_hash"] = "b" * 64
            with self.assertRaises(IntegrityError):
                finalize_delivery(root, other, refs, "pass", [], [])
            nested = save_chunk(root, p, ["spec", "title"], "Conflicting")["chunk_ref"]
            with self.assertRaisesRegex(ValueError, "Overlapping"):
                finalize_delivery(root, p, [*refs, nested], "pass", [], [])
            with self.assertRaises(ValueError):
                save_chunk(root, p, ["../outside"], "No")

    def test_backend_accepts_file_and_stops_waiting_for_chat(self):
        with tempfile.TemporaryDirectory() as directory:
            root, p = Path(directory), packet()
            p["limits"]["first_response_timeout"] = None
            (root / "task.json").write_text(json.dumps(p))
            executable = root / "fake-opencode"
            project = Path(__file__).resolve().parents[3]
            executable.write_text(f'''#!{sys.executable}
import sys, os, json, time
from pathlib import Path
sys.path.insert(0, {str(project)!r})
from featuretree.workflow.backends.delivery import save_chunk, finalize_delivery
sys.stdin.read()
root = Path(os.environ["FEATURETREE_PACKET"]).parent
p = json.loads((root / "task.json").read_text())
(root / "observed-limit.txt").write_text(os.environ["OPENCODE_EXPERIMENTAL_OUTPUT_TOKEN_MAX"])
refs = [save_chunk(root, p, ["rows"], ["one", "two"])["chunk_ref"], save_chunk(root, p, ["spec", "title"], "Title")["chunk_ref"]]
finalize_delivery(root, p, refs, "pass", [], [])
time.sleep(20)
''')
            executable.chmod(0o755)
            result, metadata = OpenCodeBackend(str(executable)).execute(root, "ft-android", p, root, None, "test/model", None)
            self.assertEqual(["one", "two"], result["payload"]["rows"])
            self.assertEqual("file", metadata["transport"])
            self.assertTrue(metadata["delivery_completed"])
            self.assertEqual("16000", (root / "observed-limit.txt").read_text())

    def test_agent_budget_and_permissions_are_pinned_without_changing_source(self):
        source = '---\nsteps: 24\npermission:\n  "*": deny\n  source_catalog: allow\n---\n禁止写文件'
        configured = configure_agent(source, 96)
        self.assertIn("steps: 96", configured)
        self.assertIn("finish_payload: allow", configured)
        self.assertIn("steps: 24", source)

    def test_output_limit_has_a_distinct_non_retryable_failure(self):
        with self.assertRaises(OutputLimitError) as failure:
            parse_events([json.dumps({"part": {"type": "step-finish", "reason": "length"}})])
        self.assertFalse(failure.exception.retryable)
