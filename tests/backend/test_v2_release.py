import tempfile
from pathlib import Path
from copy import deepcopy
import unittest

from featuretree.core.content import digest
from featuretree.core.io import ConflictError
from tests.fixtures.v2_application import application, publishable


class ReleaseIntegrationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.app, self.snapshot, self.baseline = application(Path(temporary.name))
        self.candidate = publishable(self.app, self.snapshot, self.baseline)

    def test_full_chain_freeze_publish_low_visible_and_rollback_keeps_human_rejection(self):
        app = self.app
        transaction = app.releases.prepare(self.candidate, None, 'first')
        self.assertIsNone(app.versions.current_id())
        self.assertEqual(transaction, app.releases.prepare(self.candidate, None, 'first'))
        receipt = app.releases.publish('first')
        self.assertEqual(receipt, app.releases.publish('first'))
        feature, ref = next(iter(self.candidate['knowledge_refs'].items()))
        self.assertEqual('low', app.reader.knowledge(feature)['article']['overall_confidence'])
        self.assertEqual(1, len([row for row in app.review_queue()['tickets'] if row['article_ref'] == ref]))
        claim = app.artifacts.get(ref)['claims'][0]
        decision = {'claim_id': claim['claim_id'], 'claim_hash': digest(claim), 'action': 'correct',
                    'reason': 'Synthetic correction', 'actor': 'test-human', 'evidence_refs': [],
                    'target_stage': 'fk-android', 'replacement': {'statement': 'Requires re-research'}}
        result = app.reviews.submit(ref, ref, decision, 'review')
        self.assertEqual('planned', result['revision']['status'])
        self.assertEqual('invalidated', app.reader.knowledge(feature)['summary']['validity'])
        app.releases.rollback(transaction['release_id'], app.versions.current_id(), 'rollback')
        self.assertEqual('invalidated', app.reader.knowledge(feature)['summary']['validity'])
        self.assertEqual(1, len(app.ledger.events()))

    def test_cannot_forge_freeze_hash_or_publish_draft(self):
        app = self.app
        candidate = deepcopy(self.candidate)
        frozen = app.artifacts.get(candidate['freeze_refs'][0])
        frozen['semantic_hashes'] = {key: 'a' * 64 for key in frozen['leaf_ids']}
        candidate['freeze_refs'] = [app.artifacts.put(frozen)]
        with self.assertRaises(ValueError): app.releases.prepare(candidate, None, 'forged')
        candidate = deepcopy(self.candidate)
        feature, ref = next(iter(candidate['knowledge_refs'].items()))
        article = app.artifacts.get(ref); article['draft'] = True
        candidate['knowledge_refs'][feature] = app.artifacts.put(article)
        with self.assertRaises(ValueError): app.releases.prepare(candidate, None, 'draft')

    def test_evidence_policy_change_rejects_stale_assessment(self):
        candidate = deepcopy(self.candidate)
        feature, ref = next(iter(candidate['knowledge_refs'].items()))
        article = self.app.artifacts.get(ref)
        article['rating_context']['policy']['id'] = 'changed-policy'
        candidate['knowledge_refs'][feature] = self.app.artifacts.put(article)
        with self.assertRaises(ValueError): self.app.releases.prepare(candidate, None, 'stale-rating')

    def test_review_between_preparation_and_commit_requires_repreparation(self):
        app = self.app
        app.releases.prepare(self.candidate, None, 'first')
        ref = next(iter(self.candidate['knowledge_refs'].values()))
        claim = app.artifacts.get(ref)['claims'][0]
        app.ledger.append(ref, ref, {'claim_id': claim['claim_id'], 'claim_hash': digest(claim), 'action': 'accept_limitations',
            'reason': 'Known limitation', 'actor': 'test-human', 'evidence_refs': [], 'target_stage': None, 'replacement': None}, 'decision')
        with self.assertRaises(ConflictError): app.releases.publish('first')
        self.assertIsNone(app.versions.current_id())

    def test_knowledge_rebase_preserves_unrelated_release_without_reresearch(self):
        app = self.app
        empty = {**self.candidate, 'knowledge_refs': {}}
        first = app.releases.prepare(empty, None, 'empty')
        app.releases.publish('empty')
        proposed = app.releases.prepare(self.candidate, first['release_id'], 'knowledge')
        newer = app.releases.prepare(empty, first['release_id'], 'unrelated')
        app.releases.publish('unrelated')
        with self.assertRaises(ConflictError): app.releases.publish('knowledge')
        rebased = app.releases.rebase('knowledge', newer['release_id'], 'rebased')
        app.releases.publish('rebased')
        self.assertEqual(self.candidate['knowledge_refs'], app.versions.pin()['knowledge_refs'])
        self.assertNotEqual(proposed['release_id'], rebased['release_id'])
        with self.assertRaises(ConflictError): app.releases.rebase('empty', rebased['release_id'], 'bad-first-rebase')

    def test_unreviewed_tree_mutation_cannot_reuse_old_freeze(self):
        candidate = deepcopy(self.candidate)
        tree = self.app.artifacts.get(candidate['tree_ref'])
        tree['features'][0]['definition'] += ' Unreviewed semantic change.'
        candidate['tree_ref'] = self.app.artifacts.put(tree)
        bindings = self.app.artifacts.get(candidate['bindings_ref'])
        bindings['tree_ref'] = candidate['tree_ref']
        candidate['bindings_ref'] = self.app.artifacts.put(bindings)
        with self.assertRaisesRegex(ValueError, 'matching independently reviewed'):
            self.app.releases.prepare(candidate, None, 'unreviewed-tree')

    def test_structural_review_creates_an_executable_scoped_tree_order(self):
        app = self.app
        app.releases.prepare(self.candidate, None, 'first'); app.releases.publish('first')
        feature, reference = next(iter(self.candidate['knowledge_refs'].items()))
        claim = app.artifacts.get(reference)['claims'][0]
        decision = {'claim_id': claim['claim_id'], 'claim_hash': digest(claim), 'action': 'request_research',
                    'reason': 'The observed goals need separate leaf boundaries', 'actor': 'test-human',
                    'evidence_refs': [], 'target_stage': 'ft-design', 'replacement': None}
        result = app.reviews.submit(reference, reference, decision, 'structure-review')
        plan, state = app.runs.load(result['revision']['run_id'])
        self.assertEqual('planned', state['status'])
        self.assertEqual('taxonomy', plan['pipeline'])
        self.assertEqual([feature], plan['works'][0]['scope_root_ids'])
        self.assertEqual('revise', plan['works'][0]['work_type'])
        self.assertEqual(result, app.reviews.submit(reference, reference, decision, 'structure-review'))

    def test_decision_metadata_is_not_overridable_and_crash_retry_keeps_superseding_draft(self):
        app = self.app
        draft = next(row for row in app.candidates() if row.get('article_ref') and app.artifacts.get(row['article_ref'])['draft'])
        reference = draft['article_ref']
        claim = app.artifacts.get(reference)['claims'][0]
        decision = {'claim_id': claim['claim_id'], 'claim_hash': digest(claim), 'action': 'request_research',
                    'reason': 'Synthetic uncertainty', 'actor': 'test-human', 'evidence_refs': [],
                    'target_stage': 'fk-android', 'replacement': None}
        with self.assertRaisesRegex(ValueError, 'metadata'):
            app.ledger.append(reference, reference, {**decision, 'previous_event_ref': None}, 'injected')
        receipt = app.ledger.append(reference, reference, decision, 'interrupted-decision')
        app.runner.action(draft['run_id'], 'revise', task_id=draft['work_id'] + '--fk-android',
                          feedback=[{'human_event_ref': receipt['event_ref']}])
        result = app.reviews.submit(reference, reference, decision, 'interrupted-decision')
        self.assertEqual('target_superseded', result['effect_status'])
        self.assertEqual(1, len(app.ledger.events()))
        self.assertEqual(result, app.reviews.submit(reference, reference, decision, 'interrupted-decision'))
