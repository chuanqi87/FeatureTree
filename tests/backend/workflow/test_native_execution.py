"""Native OpenCode tool execution retains process, delivery and business validation gates."""

import json
from pathlib import Path
import sys
import tempfile
import unittest

from featuretree.core.io import read_json, write_json
from featuretree.workflow.backends.errors import MissingStructuredAnswer
from featuretree.workflow.backends.events import parse_events
from featuretree.workflow.backends.monitor import ExecutionInterrupted
from featuretree.workflow.backends.opencode import OpenCodeBackend
from featuretree.workflow.backends.provider_errors import ProviderError
from featuretree.workflow.backends.results import collect_result
from tests.fixtures.v2_application import application, run
from tests.fixtures.v2_pipeline import ModelSubstitute


class NativeExecutionTests(unittest.TestCase):
    def test_native_process_reads_packet_writes_file_and_exits_after_length(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            packet = {"limits": {"max_output_tokens": None}, "payload": {"answer": "original"}}
            write_json(root / "task.json", packet)
            executable = root / "fake-opencode"
            executable.write_text(f'''#!{sys.executable}
import json, os, sys
from pathlib import Path
root = Path.cwd()
prompt = sys.stdin.read()
assert "task.json" in prompt and "original" not in prompt
assert "--pure" not in sys.argv and "--auto" in sys.argv and "--thinking" in sys.argv
configured_root = Path(sys.argv[sys.argv.index("--dir") + 1])
assert configured_root.resolve() == root.resolve()
assert str(configured_root / "task.json") in prompt and str(configured_root / "delivery/result.json") in prompt
assert "OPENCODE_EXPERIMENTAL_OUTPUT_TOKEN_MAX" not in os.environ
config = json.loads(os.environ["OPENCODE_CONFIG_CONTENT"])
assert config["permission"]["*"] == "allow" and config["tools"]["*"] is True
packet = json.loads(Path(os.environ["FEATURETREE_PACKET"]).read_text())
(root / "delivery").mkdir()
(root / "delivery/result.json").write_text(json.dumps(packet))
print(json.dumps({{"part": {{"type": "step-finish", "reason": "length", "tokens": {{"output": 32000}}}}}}))
# Model tools may edit the output before exiting. Do not accept the first file write.
packet["payload"]["answer"] = "edited and checked"
(root / "delivery/result.json").write_text(json.dumps(packet))
''')
            executable.chmod(0o755)
            result, metadata = OpenCodeBackend(str(executable)).execute(
                root, "ft-ios", packet, root, 5, "test/model", None)
            self.assertEqual("edited and checked", result["payload"]["answer"])
            self.assertEqual("workspace_file", metadata["transport"])
            self.assertTrue(metadata["output_limit_reached"])
            self.assertEqual(0, metadata["exit_code"])

    def test_file_cannot_mask_failed_process_or_provider(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_json(root / "delivery/result.json", {"payload": {}})
            (root / "events.jsonl").write_text("")
            for code, expected in [(1, ValueError), (-9, ExecutionInterrupted)]:
                with self.subTest(code=code), self.assertRaises(expected):
                    collect_result(root, root, {}, code, {})
            (root / "events.jsonl").write_text(json.dumps({"type": "error", "error": {
                "data": {"statusCode": 402, "message": "Insufficient balance"}}}))
            with self.assertRaises(ProviderError):
                collect_result(root, root, {}, 0, {})

    def test_truncated_or_missing_file_is_not_accepted_on_zero_exit(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "events.jsonl").write_text(json.dumps({"part": {
                "type": "step-finish", "reason": "length"}}))
            with self.assertRaises(MissingStructuredAnswer):
                collect_result(root, root, {}, 0, {})
            (root / "delivery").mkdir()
            (root / "delivery/result.json").write_text('{"payload":')
            with self.assertRaises(MissingStructuredAnswer):
                collect_result(root, root, {}, 0, {})
            self.assertEqual('{"payload":', (root / "response.json").read_text())
            self.assertTrue(read_json(root / "metadata.json")["output_limit_reached"])

    def test_prior_length_does_not_poison_later_completed_chat(self):
        lines = [json.dumps({"part": part}) for part in [
            {"type": "step-finish", "reason": "length"},
            {"type": "step-start"}, {"type": "text", "text": '{"payload":{}}'},
            {"type": "step-finish", "reason": "stop"}]]
        response, _ = parse_events(lines)
        self.assertEqual({"payload": {}}, json.loads(response))

    def test_native_files_complete_tree_and_knowledge_with_original_validators(self):
        class NativeSubstitute(ModelSubstitute):
            def execute(self, root, agent, packet, folder, timeout, model, variant):
                response, metadata = super().execute(root, agent, packet, folder, timeout, model, variant)
                write_json(root / "delivery/result.json", response)
                (folder / "events.jsonl").write_text(json.dumps({"part": {
                    "type": "step-finish", "reason": "length"}}))
                return collect_result(root, folder, packet, 0, metadata)

        with tempfile.TemporaryDirectory() as directory:
            app, snapshot, baseline = application(Path(directory))
            app.runner.executor.backend = NativeSubstitute()
            state, check = run(app, snapshot, {"baseline_ref": baseline}, "native-tree")
            plan, _ = app.runs.load(state["run_id"])
            self.assertIsNone(plan["budget"]["source_batch_size"])
            for stage in plan["stage_configs"].values():
                if stage["agent_text"]:
                    self.assertIn('"*": allow', stage["agent_text"])
                    self.assertNotIn("禁止写文件", stage["agent_text"])
            tree = app.artifacts.get(check["tree_ref"])
            inputs = {key: check[key] for key in ("tree_ref", "bindings_ref")}
            inputs.update(baseline_ref=baseline, feature_ref=app.artifacts.put(tree["features"][0]))
            _, article = run(app, snapshot, inputs, "native-knowledge", "knowledge")
            self.assertTrue(app.artifacts.get(article["article_ref"])["draft"])

    def test_native_file_still_requires_fixed_identity(self):
        class WrongIdentity(ModelSubstitute):
            def execute(self, root, agent, packet, folder, timeout, model, variant):
                response, metadata = super().execute(root, agent, packet, folder, timeout, model, variant)
                response["input_hash"] = "0" * 64
                write_json(root / "delivery/result.json", response)
                (folder / "events.jsonl").write_text("")
                return collect_result(root, folder, packet, 0, metadata)

        with tempfile.TemporaryDirectory() as directory:
            app, snapshot, baseline = application(Path(directory))
            app.runner.executor.backend = WrongIdentity()
            state = app.planner.create({"pipeline": "taxonomy", "model": "test/model",
                "budget": {"max_attempts": 1}, "scopes": [{"definition": "Synthetic scope",
                    "snapshot_id": snapshot["id"], "selection": {}, "inputs": {"baseline_ref": baseline}}]},
                "wrong-identity")
            state = app.runner.run(state["run_id"])
            self.assertFalse(any(task.get("result_ref") for task in state["tasks"].values()))
            self.assertTrue(any(task["status"] == "failed" for task in state["tasks"].values()))
