"""Cross-domain preservation and related-source invalidation regressions."""
import unittest
from copy import deepcopy
from featuretree.core.content import digest
from featuretree.taxonomy.model import semantic_hash, validate_tree
from featuretree.taxonomy.revisions import apply_proposal, merge_binding_scope
from featuretree.knowledge.validity import stale_reasons


def leaf(key, parent=None):
    return {'id': key, 'parent_id': parent, 'name': key, 'node_type': 'leaf', 'success_criteria': ['goal']}


class RevisionTests(unittest.TestCase):
    def test_source_supplement_preserves_only_unchanged_neighbor_dependencies(self):
        from featuretree.taxonomy.source_migration import validate_preserved_sources
        previous = {'snapshot_id': 'old', 'bindings': [{'feature_id': 'neighbor', 'declaration_id': 'api', 'evidence_refs': ['doc']}],
                    'topics': [{'id': 'topic'}]}
        class Catalog:
            def get(self, snapshot, kind, key):
                return {'id': key}
            def read_body(self, *args):
                return {}
        receipt = validate_preserved_sources(previous, 'new', ['revised'], [], Catalog())
        self.assertEqual(['api'], receipt['verified_unchanged_ids']['declarations'])
        class Changed(Catalog):
            def get(self, snapshot, kind, key):
                return {'id': key, 'changed': snapshot == 'new' and kind == 'declarations'}
        with self.assertRaisesRegex(ValueError, 'changed preserved declarations'):
            validate_preserved_sources(previous, 'new', ['revised'], [], Changed())

    def test_domain_edit_preserves_neighbor_and_shared_api_binding(self):
        base = {'schema_version': 3, 'features': [leaf('a'), leaf('b')], 'lineage': []}
        proposal = {'features': [{**leaf('a'), 'name': 'renamed'}], 'changes': []}
        tree, scope = apply_proposal(base, proposal, ['a'])
        self.assertEqual(leaf('b'), next(row for row in tree['features'] if row['id'] == 'b'))
        self.assertEqual({'a'}, scope)
        binding = {'feature_id': 'b', 'declaration_id': 'api', 'role': 'core', 'usage': 'shared', 'route_id': 'r', 'evidence_refs': ['doc']}
        disposition = {'id': 'api', 'status': 'assigned', 'reason': 'used', 'rule': 'bound', 'evidence_refs': ['doc']}
        previous = {'bindings': [binding], 'declarations': [disposition], 'topics': []}
        proposed = {'bindings': [], 'api_dispositions': [{**disposition, 'status': 'excluded'}], 'topic_dispositions': []}
        merged = merge_binding_scope(previous, proposed, scope)
        self.assertEqual([binding], merged['bindings'])
        self.assertEqual('assigned', merged['declarations'][0]['status'])

    def test_edit_cannot_escape_domain_and_split_lineage_survives_later_merge(self):
        base = {'schema_version': 3, 'features': [leaf('a'), leaf('b')], 'lineage': []}
        with self.assertRaises(ValueError): apply_proposal(base, {'features': [{**leaf('b'), 'name': 'escaped'}], 'changes': []}, ['a'])
        split, _ = apply_proposal(base, {'features': [leaf('c'), leaf('d')], 'changes': [
            {'operation': 'split', 'subject_ids': ['a'], 'candidate_ids': ['c', 'd'], 'reason': 'independent goals'}]}, ['a'])
        merged, _ = apply_proposal(split, {'features': [leaf('e')], 'changes': [
            {'operation': 'merge', 'subject_ids': ['c', 'd'], 'candidate_ids': ['e'], 'reason': 'one goal'}]}, ['c', 'd'])
        self.assertEqual(2, len(merged['lineage']))
        self.assertEqual({'b', 'e'}, set(validate_tree(merged)))

    def test_related_document_change_invalidates_even_if_old_snapshot_is_retained(self):
        feature = leaf('a'); binding = {'feature_id': 'a', 'declaration_id': 'api'}
        from featuretree.taxonomy.routes import binding_hash
        frozen = {'semantic_hashes': {'a': semantic_hash(feature)}, 'binding_hashes': {'a': binding_hash({'bindings': [binding]}, 'a')}}
        article = {'feature_id': 'a', 'snapshot_id': 'old', 'baseline_ref': 'base',
                   'evidence': [{'document_id': 'doc', 'body_sha256': 'old-body'}]}
        bindings = {'snapshot_id': 'new', 'bindings': [binding]}
        class Catalog:
            def get(self, snapshot, kind, key):
                return {'id': key} if kind == 'declarations' else {'status': 'verified', 'body_sha256': 'new-body'}
        self.assertEqual(['evidence_content_changed'], stale_reasons(article, feature, bindings, frozen, 'base', ['old', 'new'], Catalog()))
        class Unrelated(Catalog):
            def get(self, snapshot, kind, key):
                return {'id': key} if kind == 'declarations' else {'status': 'verified', 'body_sha256': 'old-body'}
        self.assertEqual([], stale_reasons(article, feature, bindings, frozen, 'base', ['old', 'new'], Unrelated()))
