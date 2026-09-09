"""API size gates measure per-platform evidence, never model-provided totals."""

from copy import deepcopy
import unittest

from featuretree.workflow.api_inventory import api_key, api_index, size_decision, assess_allocations
from featuretree.workflow.state import read_json, load_run, artifact
from featuretree.workflow.planning import make_plan
from featuretree.workflow.engine import execute_run
from featuretree.workflow.publication import publish, report
from featuretree.core.storage import Repository, read_yaml, write_yaml
from tests.backend.workflow.test_execution import WorkflowTests
from tests.fixtures.workflow import FixtureBackend


class ApiSizeTests(unittest.TestCase):
    def surface(self, counts=(40, 40, 40), completeness='complete'):
        return {p: {'count': n, 'completeness': completeness} for p, n in zip(('android','ios','harmonyos'), counts)}

    def test_thresholds_use_each_platform_not_the_sum(self):
        self.assertEqual(size_decision(self.surface()), 'leaf_eligible')
        for number in (41, 50):
            self.assertEqual(size_decision(self.surface((1, number, 1))), 'split_recommended')
        self.assertEqual(size_decision(self.surface((1, 1, 51))), 'must_split')
        self.assertEqual(size_decision(self.surface((0, 2, 3), 'partial')), 'needs_research')

    def test_overload_and_separator_normalization_does_not_inflate_counts(self):
        self.assertEqual(api_key('Thing#call(String value)'), api_key('Thing.call(int)'))
        self.assertEqual(api_key('Thing::call()'), 'Thing.call')
        scout = {'apis': [{'id': f'Thing.call({arg})', 'kind':'method', 'url':'https://developer.android.com/reference/Thing', 'evidence':'Fixture'} for arg in ('int', 'String')],
                 'candidates':[{'api_ids':['Thing.call(int)','Thing.call(String)'], 'api_completeness':'complete', 'public_api':'yes'}]}
        self.assertEqual(len(api_index(scout, 'android')), 1)

    def test_empty_or_uncertain_inventory_cannot_claim_complete(self):
        with self.assertRaisesRegex(ValueError, 'positively'):
            api_index({'apis': [], 'candidates':[{'api_ids':[], 'api_completeness':'complete','public_api':'unknown'}]}, 'ios')


class ApiWorkflowTests(unittest.TestCase):
    setUp = WorkflowTests.setUp
    plan = WorkflowTests.plan
    run_batch = WorkflowTests.run_batch
    # Reuse the isolated fixture setup, but do not duplicate its inherited tests.
    def test_platform_implementation_precedes_structural_design(self):
        run, backend = self.run_batch()
        self.assertGreaterEqual(backend.calls.index('sample/scope'), 3)
        folder, state = load_run(self.root, run)
        packet = read_json(folder/'attempts/sample/scope/1/input.json')
        self.assertTrue(all(p in packet['inputs'] for p in ('android','ios','harmonyos')))
        self.assertEqual(state['depth'], 1)
        with self.assertRaises(ValueError):
            self.plan(depth=2)

    def test_fabricated_or_dropped_api_allocations_are_rejected(self):
        run, _ = self.run_batch()
        folder, state = load_run(self.root, run)
        proposal = artifact(folder, state['tasks']['sample/synthesize'])['payload']
        scouts = [artifact(folder, state['tasks']['sample/'+p])['payload'] for p in ('android','ios','harmonyos')]
        for ids in ([], ['Fabricated.call']):
            changed = deepcopy(proposal)
            changed['api_allocations'][0]['platforms']['android']['api_ids'] = ids
            with self.assertRaises(ValueError):
                assess_allocations(changed, scouts)
        changed = deepcopy(proposal)
        changed['api_allocations'][0]['platforms']['android']['completeness'] = 'complete'
        with self.assertRaisesRegex(ValueError, 'completeness'):
            assess_allocations(changed, scouts)

    def terminal_run(self):
        initial, _ = self.run_batch()
        publish(self.root, initial)
        original = Repository(self.root).features()['sample.first']
        def terminal(result):
            payload = result['payload']
            if result['stage'] in ('android','ios','harmonyos'):
                payload['candidates'][0].update(public_api='yes', api_completeness='complete')
            if result['stage'] == 'synthesize':
                node = deepcopy(original)
                node.update(granularity='atomic', knowledge_role='leaf', leaf_at_this_level=True,
                            knowledge_path='knowledge/sample/first.yaml', anchor_status='unverified')
                payload['nodes'] = [node]
                payload['decisions'] = [{'node_id':node['id'],'action':'stop','reason':'Independent complete fixture <=40'}]
                for disposition in payload['dispositions']:
                    disposition['node_ids'] = [node['id']]
                allocation = payload['api_allocations'][0]
                allocation['node_id'] = node['id']
                for value in allocation['platforms'].values(): value['completeness'] = 'complete'
                payload['api_allocations'] = [allocation]
        return self.run_batch(FixtureBackend(mutate=terminal), nodes=['sample.first'])[0]

    def test_small_existing_branch_stops_without_an_artificial_child_and_migrates_stub(self):
        run = self.terminal_run()
        summary = report(self.root, run)
        self.assertTrue(summary['ready_to_publish'])
        self.assertEqual(summary['additions']['total'], 0)
        self.assertEqual(summary['updated_nodes'], ['sample.first'])
        self.assertEqual(summary['next_work_orders'], [])
        publish(self.root, run)
        self.assertEqual(len(Repository(self.root).features()), 4)
        node = Repository(self.root).features()['sample.first']
        self.assertEqual(node['granularity'], 'atomic')
        self.assertEqual(node['api_surface']['android']['count'], 1)
        self.assertFalse((self.root/'knowledge/sample/first/_rollup.yaml').exists())
        self.assertEqual(read_yaml(self.root/'knowledge/sample/first.yaml')['role'], 'leaf')
        self.assertTrue(publish(self.root, run))

    def test_terminal_confirmation_does_not_overwrite_existing_research(self):
        run = self.terminal_run()
        path = self.root/'knowledge/sample/first/_rollup.yaml'
        doc = read_yaml(path); doc['evidence'] = [{'user': 'Existing research'}]; write_yaml(path, doc)
        with self.assertRaisesRegex(ValueError, 'existing knowledge research'):
            publish(self.root, run)
        self.assertTrue(path.exists())
        self.assertFalse((self.root/'knowledge/sample/first.yaml').exists())
