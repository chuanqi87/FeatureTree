from pathlib import Path
import tempfile
import unittest
from tests.fixtures.v2_application import application, run


class ReplanningTests(unittest.TestCase):
    def test_compatible_platform_facts_are_reused_with_original_author_provenance(self):
        with tempfile.TemporaryDirectory() as directory:
            app, snapshot, baseline = application(Path(directory))
            old, _ = run(app, snapshot, {'baseline_ref': baseline}, 'original')
            result = app.replanning.create(old['run_id'], {'fresh_stages': ['ft-design'], 'reason': 'Calibrate node boundaries'}, 'replacement')
            original_ref = old['tasks']['w_0000--ft-android']['result_ref']
            self.assertEqual(original_ref, result['tasks']['w_0000--ft-android']['result_ref'])
            self.assertTrue(result['tasks']['w_0000--ft-android']['reuse_ref'])
            self.assertIsNone(result['tasks']['w_0000--ft-design']['result_ref'])
            self.assertEqual(result, app.replanning.create(old['run_id'], {'fresh_stages': ['ft-design'], 'reason': 'Calibrate node boundaries'}, 'replacement'))
            app.runner.run(result['run_id'])
            self.assertEqual(1, len([name for name, _ in app.runner.executor.backend.calls if name == 'ft-android']))
            response, packet = app.provenance.require(original_ref, 'ft-android')
            self.assertEqual(old['run_id'], response['run_id'])
            self.assertEqual(old['run_id'], packet['run_id'])

    def test_model_change_is_a_new_plan_and_keeps_original_settings(self):
        with tempfile.TemporaryDirectory() as directory:
            app, snapshot, baseline = application(Path(directory))
            old, _ = run(app, snapshot, {'baseline_ref': baseline}, 'original')
            result = app.replanning.create(old['run_id'], {'fresh_stages': ['ft-design'],
                'reason': 'Explicit provider change', 'model': 'test/replacement'}, 'new-provider')
            self.assertEqual('test/substitute', app.runs.load(old['run_id'])[0]['model'])
            self.assertEqual('test/replacement', app.runs.load(result['run_id'])[0]['model'])
