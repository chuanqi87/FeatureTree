"""Unlimited execution must wait without dropping validated prior research."""
from copy import deepcopy
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from featuretree.core.content import digest
from featuretree.core.io import IntegrityError, read_json
from featuretree.workflow.attempt_tools import configure_agent
from featuretree.workflow.backends.monitor import wait_for_model
from featuretree.workflow.batch_execution import verify_receipt
from featuretree.workflow.checkpoint_reuse import revalidate_checkpoint
from tests.fixtures.v2_batches import batched_application, BatchModel


class UnlimitedTests(unittest.TestCase):
    def test_no_deadline_still_waits_for_process_completion(self):
        with tempfile.TemporaryDirectory() as directory:
            events = Path(directory) / 'events.jsonl'
            events.write_text('')
            process = subprocess.Popen([sys.executable, '-c', 'import sys,time;sys.stdin.read();time.sleep(1.1)'], stdin=subprocess.PIPE, text=True)
            result = wait_for_model(process, 'test', events, None, None)
            self.assertEqual(0, process.returncode)
            self.assertIsNone(result['first_response_seconds'])
        self.assertNotIn('steps:', configure_agent('---\nsteps: 2\n---\nResearch', None))

    def test_execution_policy_change_reuses_revalidated_original(self):
        with tempfile.TemporaryDirectory() as directory:
            app, state = batched_application(Path(directory), BatchModel(fail_index=1))
            app.runner.run(state['run_id'])
            path = next((app.runs.folder(state['run_id']) / 'batch-checkpoints').rglob('*.json'))
            old = read_json(path)
            packet = deepcopy(app.artifacts.get(old['input_ref']))
            packet.update(run_id='replacement', limits={**packet['limits'], 'timeout_seconds':None})
            packet.pop('input_hash'); packet['input_hash'] = digest(packet)
            receipt = revalidate_checkpoint(old, packet, app.artifacts, app.runner.executor.handlers)
            response = verify_receipt(receipt, packet, app.artifacts, app.runner.executor.handlers)
            self.assertEqual(app.artifacts.get(old['result_ref'])['payload'], response['payload'])
            packet['model'] = 'different/model'
            with self.assertRaises(IntegrityError):
                revalidate_checkpoint(old, packet, app.artifacts, app.runner.executor.handlers)
