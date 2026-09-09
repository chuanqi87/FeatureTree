"""Wall duration is distinct from the sum of concurrent stage durations."""

import unittest

from featuretree.workflow.metrics import execution_metrics


class MetricsTests(unittest.TestCase):
    def test_concurrent_stages_and_unknown_usage(self):
        attempt = {"status": "succeeded", "started_at": "2026-09-09T00:00:00+00:00",
                   "ended_at": "2026-09-09T00:00:05+00:00"}
        state = {"tasks": {p: {"stage": p, "status": "succeeded", "attempts": [attempt]}
                           for p in ("android", "ios")}}
        metrics = execution_metrics(state)
        self.assertEqual(metrics["wall_seconds"], 5)
        self.assertEqual(metrics["stage_seconds"], 10)
        self.assertEqual(metrics["model_calls"], 2)
        self.assertIsNone(metrics["reported_total_tokens"])
        self.assertIsNone(metrics["reported_cost"])

    def test_reused_artifacts_are_not_counted_as_model_calls(self):
        state = {'tasks': {'node/scope': {'stage': 'scope', 'status': 'succeeded', 'attempts': [
            {'status': 'succeeded', 'metadata': {'model_invoked': False, 'elapsed_seconds': 0}}
        ]}}}
        self.assertEqual(execution_metrics(state, active=False)['model_calls'], 0)
