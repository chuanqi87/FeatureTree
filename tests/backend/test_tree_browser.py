"""Version isolation and exact source lookup for the tree browser."""
import unittest
from unittest.mock import Mock

from featuretree.reporting.tree_browser import TreeBrowser


class TreeBrowserTests(unittest.TestCase):
    def setUp(self):
        self.artifacts = Mock()
        self.versions = Mock()
        self.reader = Mock()
        self.catalog = Mock()
        self.browser = TreeBrowser(self.artifacts, self.versions, self.reader, self.catalog)

    def test_views_do_not_promote_candidates(self):
        self.versions.pin.return_value = None
        self.artifacts.get.return_value = {'features': [{'id': 'leaf'}]}
        result = self.browser.views([{'result_ref': 'candidate', 'tree_ref': 'tree', 'bindings_ref': 'bindings', 'run_id': 'run'}], [{'run_id': 'run', 'status': 'cancelled', 'updated_at': 'today'}])
        self.assertIsNone(result['release_id'])
        self.assertEqual(result['items'][0]['status'], 'candidate')
        self.assertEqual(result['items'][0]['run_status'], 'cancelled')
        self.reader.tree.assert_not_called()

    def test_api_lookup_pins_snapshot_and_selected_feature(self):
        self.artifacts.get.return_value = {'snapshot_id': 'snapshot', 'bindings': [
            {'feature_id': 'a', 'declaration_id': 'api', 'route_id': 'one'},
            {'feature_id': 'a', 'declaration_id': 'api', 'route_id': 'two'},
            {'feature_id': 'b', 'declaration_id': 'unrelated'},
        ]}
        self.catalog.get.return_value = {'id': 'api', 'qualified_name': 'Real.name'}
        view = {'features': [{'id': 'a'}], 'status': 'candidate', 'bindings_ref': 'fixed-bindings'}
        result = self.browser.detail(view, 'a')
        self.catalog.get.assert_called_once_with('snapshot', 'declarations', 'api')
        self.assertEqual(len(result['bindings']), 2)
        self.assertEqual(result['bindings'][0]['api']['qualified_name'], 'Real.name')
        with self.assertRaises(KeyError):
            self.browser.detail(view, 'missing')

    def test_missing_source_remains_explicit(self):
        self.artifacts.get.return_value = {'snapshot_id': 'snapshot', 'bindings': [{'feature_id': 'a', 'declaration_id': 'missing'}]}
        self.catalog.get.side_effect = KeyError('missing')
        result = self.browser.detail({'features': [{'id': 'a'}], 'status': 'formal', 'bindings_ref': 'bindings'}, 'a')
        self.assertIsNone(result['bindings'][0]['api'])
