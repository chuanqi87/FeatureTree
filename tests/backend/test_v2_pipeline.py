import tempfile
from pathlib import Path
import unittest
from copy import deepcopy

from featuretree.core.content import digest
from featuretree.core.io import ConflictError
from featuretree.knowledge.ratings import rate_article
from featuretree.knowledge.reviews import ReviewLedger, project_reviews
from featuretree.workflow.execution import AttemptExecutor
from featuretree.workflow.handlers import StageHandlers
from featuretree.workflow.planner import Planner
from featuretree.workflow.registry import PipelineRegistry
from featuretree.workflow.run_store import RunStore
from featuretree.workflow.runner import Runner
from tests.fixtures.v2 import PROJECT, schemas, stores
from tests.fixtures.v2_pipeline import ModelSubstitute, baseline, source_fixture


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.schemas = schemas()
        self.objects, self.versions = stores(self.root)
        self.snapshots, self.snapshot, self.catalog = source_fixture(self.root, self.schemas)
        self.runs = RunStore(self.root / ".workflow/v2/runs")
        self.registry = PipelineRegistry.load(PROJECT / "config/v2/pipelines.json")
        self.planner = Planner(PROJECT, self.registry, self.schemas, self.objects, self.catalog, self.runs)
        self.backend = ModelSubstitute()
        executor = AttemptExecutor(self.root, self.objects, self.backend, StageHandlers(self.objects, self.catalog))
        self.runner = Runner(self.runs, self.objects, executor)

    def plan(self, pipeline, key, inputs=None):
        return self.planner.create({"pipeline": pipeline, "model": "test/fake", "scopes": [{
            "definition": "Fixture scope", "snapshot_id": self.snapshot["id"], "selection": {},
        "topic_selection": {}, "inputs": inputs or {"baseline_ref": self.objects.put(baseline())}, "mode": "calibration", "work_type": "refine",
            "enumeration_complete": True}]}, key)

    def pipeline_article(self):
        tree_run = self.plan("taxonomy", "tree")
        state = self.runner.run(tree_run["run_id"])
        self.assertTrue(all(task["status"] == "completed" for task in state["tasks"].values()), str(state))
        check = self.objects.get(state["tasks"]["w_0000--ft-check"]["result_ref"])["payload"]
        tree = self.objects.get(check["tree_ref"])
        inputs = {"tree_ref": check["tree_ref"], "bindings_ref": check["bindings_ref"],
                  "feature_ref": self.objects.put(tree["features"][0]), "baseline_ref": self.objects.put(baseline())}
        knowledge_run = self.plan("knowledge", "knowledge", inputs)
        state = self.runner.run(knowledge_run["run_id"])
        self.assertTrue(all(task["status"] == "completed" for task in state["tasks"].values()), str(state))
        assembled = self.objects.get(state["tasks"]["w_0000--fk-assemble"]["result_ref"])["payload"]
        return assembled["article_ref"], self.objects.get(assembled["article_ref"]), state

    def test_seventeen_named_agents_produce_versioned_deliveries(self):
        reference, article, state = self.pipeline_article()
        self.assertEqual(17, len({agent for agent, _ in self.backend.calls}))
        self.assertEqual("low", article["overall_confidence"])
        self.assertTrue(article["draft"])
        self.assertEqual(9, len(article["claims"]))
        self.assertEqual("waiting_human", state["status"])
        self.assertIsNone(self.versions.current_id())
        self.schemas.validate("https://featuretree.local/schema/business/v3/article", article)

    def test_source_cursor_pins_scope_and_enumeration_has_no_gaps(self):
        sid = self.snapshot["id"]
        first = self.catalog.page(sid, {}, limit=1)
        with self.assertRaises(ConflictError):
            self.catalog.page(sid, {"platforms": ["ios"]}, first["next_cursor"], 1)
        self.assertEqual(3, len(self.catalog.enumerate_ids(sid, {})))

    def test_unknown_cannot_gain_high_confidence_or_disappear(self):
        _, article, _ = self.pipeline_article()
        spec = self.objects.get(article["spec_ref"])
        changed = deepcopy(article["assessments"])
        changed[0]["level"] = "high"
        with self.assertRaises(ValueError):
            rate_article(spec, article["claims"], article["reviews"], changed, article["evidence"])
        with self.assertRaises(ValueError):
            rate_article(spec, article["claims"][1:], article["reviews"][1:], article["assessments"][1:], [])

    def test_human_acceptance_is_versioned_idempotent_and_does_not_raise_rating(self):
        reference, article, _ = self.pipeline_article()
        ledger = ReviewLedger(self.root / "data/reviews", self.objects, self.schemas)
        claim = article["claims"][0]
        decision = {"claim_id": claim["claim_id"], "claim_hash": digest(claim), "action": "accept_limitations",
                    "reason": "Unknown baseline is explicitly documented", "actor": "fixture-human",
                    "evidence_refs": [], "target_stage": None, "replacement": None}
        first = ledger.append(reference, reference, decision, "decision")
        self.assertEqual(first, ledger.append(reference, reference, decision, "decision"))
        self.assertEqual(1, len(ledger.events()))
        with self.assertRaises(ConflictError):
            ledger.append(reference, "b" * 64, decision, "stale")
        projection = project_reviews({reference: article}, ledger.events())
        accepted = next(row for row in projection["tickets"][0]["items"] if row["claim_id"] == claim["claim_id"])
        self.assertEqual("decided", accepted["state"])
        self.assertEqual("low", self.objects.get(reference)["overall_confidence"])

    def test_unrelated_stage_artifact_survives_directed_revision(self):
        planned = self.plan("taxonomy", "tree")
        state = self.runner.run(planned["run_id"])
        original = state["tasks"]["w_0000--ft-android"]["result_ref"]
        revised = self.runner.action(planned["run_id"], "revise", task_id="w_0000--ft-design",
                                     feedback=[{"reason": "Narrow goal"}])
        self.assertEqual(original, revised["tasks"]["w_0000--ft-android"]["result_ref"])
        self.assertIsNone(revised["tasks"]["w_0000--ft-bind"]["result_ref"])
        self.assertTrue(revised["tasks"]["w_0000--ft-bind"]["history"])

    def test_machine_semantic_failure_repairs_only_responsible_stage(self):
        original = self.backend.execute
        failed = []
        def execute(root, agent, packet, folder, timeout, model, variant):
            result, metadata = original(root, agent, packet, folder, timeout, model, variant)
            if agent == 'ft-bind' and not failed:
                failed.append(True)
                result['payload']['bindings'][0]['role'] = 'supporting'
            return result, metadata
        self.backend.execute = execute
        planned = self.plan('taxonomy', 'semantic-machine')
        state = self.runner.run(planned['run_id'])
        self.assertTrue(all(task['status'] == 'completed' for task in state['tasks'].values()), str(state))
        self.assertEqual(2, len(state['tasks']['w_0000--ft-bind']['attempts']))
        self.assertEqual(1, len(state['tasks']['w_0000--ft-android']['attempts']))
        self.assertEqual(1, state['semantic_rounds']['w_0000--ft-bind'])

    def test_cross_domain_integration_waits_for_all_local_reviews_and_is_invalidated(self):
        scope = {'definition': 'Fixture', 'snapshot_id': self.snapshot['id'], 'selection': {},
                 'inputs': {'baseline_ref': self.objects.put(baseline())}, 'enumeration_complete': True, 'mode': 'calibration'}
        planned = self.planner.create({'pipeline': 'taxonomy', 'model': 'test/fake', 'scopes': [scope, scope]}, 'two-domains')
        state = self.runner.run(planned['run_id'])
        calls = [name for name, _ in self.backend.calls]
        self.assertGreater(calls.index('ft-integrate'), max(index for index, name in enumerate(calls) if name == 'ft-review'))
        original = state['tasks']['w_0001--ft-android']['result_ref']
        revised = self.runner.action(planned['run_id'], 'revise', task_id='w_0000--ft-design', feedback=[{'reason': 'Boundary changed'}])
        self.assertIsNone(revised['tasks']['w_0001--ft-integrate']['result_ref'])
        self.assertEqual(original, revised['tasks']['w_0001--ft-android']['result_ref'])
