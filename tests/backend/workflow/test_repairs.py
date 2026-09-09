"""Malformed completed answers retain provenance and avoid repeating source research."""

import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from featuretree.core.storage import write_json
from featuretree.workflow.state import digest, read_json
from featuretree.workflow.packets import make_packet
from featuretree.workflow.repairs import ResponseFormatError, has_repairable_answer
from featuretree.workflow.backends.opencode import OpenCodeBackend
import sys


class RepairTests(unittest.TestCase):
    def test_completed_malformed_response_keeps_timing_and_original_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            program = root / 'fake-opencode'
            answer = 'A preface\n```json\n' + json.dumps(dict(schema_version=1,task_id='sample/scope',input_hash='test',stage='scope',payload={})) + '\n```'
            events = [dict(part=dict(type='text', text=answer)),
                      dict(part=dict(type='step-finish', reason='stop', tokens=dict(total=12)))]
            program.write_text(f'#!{sys.executable}\nimport sys\nsys.stdin.read()\n' +
                               '\n'.join(f'print({json.dumps(json.dumps(e))})' for e in events))
            program.chmod(0o755)
            with self.assertRaises(ResponseFormatError) as failed:
                OpenCodeBackend(str(program)).execute(root, 'ft-scope', {}, root, 5, None, None)
            metadata = failed.exception.metadata
            self.assertGreater(metadata['elapsed_seconds'], 0)
            self.assertEqual(metadata['usage'][0]['tokens']['total'], 12)
            self.assertEqual(metadata['response_sha256'], hashlib.sha256(answer.encode()).hexdigest())
            self.assertEqual((root / 'response.json').read_text(), answer)

    def test_step_budget_summary_and_ambiguous_answers_are_not_format_repairs(self):
        self.assertFalse(has_repairable_answer('最大步骤数已耗尽。尚未输出符合 Schema 的 JSON。'))
        self.assertFalse(has_repairable_answer('{"payload":'))
        response = json.dumps(dict(schema_version=1,task_id='sample/scope',input_hash='test',stage='scope',payload={}))
        self.assertTrue(has_repairable_answer(response + '\nCompleted'))
        self.assertFalse(has_repairable_answer(response + response))
        self.assertFalse(has_repairable_answer('```json\n'+response+'\n```\n```json\n'+response+'\n```'))

    def test_prose_prefix_and_unescaped_quotes_still_identify_a_retained_answer(self):
        response = '{"schema_version":1,"task_id":"node/review","input_hash":"hash","stage":"review","payload":{"reason":"The "quote" needs escaping"}}'
        self.assertTrue(has_repairable_answer('Read permission was denied.\n\n'+response))
        self.assertFalse(has_repairable_answer('未完成。下一步输出 schema_version/task_id/input_hash/stage/payload。'))

    def test_repair_reuses_verified_input_and_never_retrieves_again(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            folder = root / 'attempts/sample/android/1'
            folder.mkdir(parents=True)
            raw = 'preface {"payload": {}}'
            (folder / 'response.json').write_text(raw)
            original = {'task_id': 'sample/android', 'stage': 'android', 'inputs': {'scope': {'axis': 'frozen'}}}
            original['input_hash'] = digest(original)
            write_json(folder / 'input.json', original)
            task = {'id': 'sample/android', 'attempts': [dict(number=1, error='format', metadata={
                'error_type': 'ResponseFormatError', 'response_sha256': hashlib.sha256(raw.encode()).hexdigest()})]}
            with patch('featuretree.workflow.packets.source_context', side_effect=AssertionError('Unexpected retrieval')):
                packet = make_packet(root, root, {'max_input_chars': 10000}, task, {})
            self.assertEqual(packet['inputs'], original['inputs'])
            self.assertEqual(packet['response_repair']['text'], raw)
            self.assertNotEqual(packet['input_hash'], original['input_hash'])
            packet_hash = packet.pop('input_hash')
            self.assertEqual(digest(packet), packet_hash)
            (folder / 'response.json').write_text('modified')
            with self.assertRaisesRegex(ValueError, 'response was modified'):
                make_packet(root, root, {'max_input_chars': 10000}, task, {})
            (folder / 'response.json').write_text(raw)
            original['inputs']['scope']['axis'] = 'changed'
            write_json(folder / 'input.json', original)
            with self.assertRaisesRegex(ValueError, 'input packet was modified'):
                make_packet(root, root, {'max_input_chars': 10000}, task, {})

    def test_review_source_references_reject_tampered_platform_inputs(self):
        from featuretree.core.storage import ROOT
        from featuretree.workflow.planning import make_plan
        from featuretree.workflow.engine import execute_run
        from featuretree.workflow.packets import platform_source_refs
        from tests.fixtures.console import workspace
        from tests.fixtures.workflow import FixtureBackend

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workspace(root)
            state = make_plan(root, ['sample'], read_json(ROOT/'config/workflow/baseline.example.json'))
            execute_run(root, state['id'], FixtureBackend(), lambda _: None)
            folder = root/'.workflow/runs'/state['id']
            completed = read_json(folder/'state.json')
            self.assertEqual(set(platform_source_refs(folder, completed, 'sample')), {'android','ios','harmonyos'})
            path = folder/'attempts/sample/android/1/input.json'
            packet = read_json(path)
            packet['sources']['gap'] = 'tampered source context'
            write_json(path, packet)
            with self.assertRaisesRegex(ValueError, 'source input was modified'):
                platform_source_refs(folder, completed, 'sample')
