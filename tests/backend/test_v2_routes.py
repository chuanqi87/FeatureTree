from copy import deepcopy
import unittest

from featuretree.taxonomy.coverage import size_report
from featuretree.taxonomy.routes import binding_hash, validate_routes


class RouteTests(unittest.TestCase):
    def setUp(self):
        self.apis = {key: {"platform": "android"} for key in ("submit", "callback", "alternative")}
        self.bindings = [{"declaration_id": key, "feature_id": "leaf", "usage": "goal", "role": "core",
                          "route_id": "alternative" if key == "alternative" else "default"} for key in self.apis]
        self.routes = [{"id": key, "feature_id": "leaf", "platform": "android", "completeness": "complete", "gaps": [],
                       "steps": [{"description": api, "api_ids": [api]} for api in ids]}
                       for key, ids in (("default", ["submit", "callback"]), ("alternative", ["alternative"]))]
        self.families = [{"id": key, "declaration_ids": [key]} for key in self.apis]

    def test_steps_count_together_and_alternative_route_is_separate(self):
        validate_routes({"leaf": {}}, self.apis, self.bindings, self.routes)
        report = size_report(self.apis, self.families, self.bindings, enumeration_complete=True, routes=self.routes)["leaf"]
        self.assertEqual([1, 2], [route['core_family_count'] for route in report['routes']])
        self.assertEqual(3, report['all_api_count'])
        self.assertFalse(report['counts_are_lower_bounds'])
        partial = deepcopy(self.routes); partial[0].update(completeness='partial', gaps=['Missing completion signaling'])
        self.assertTrue(size_report(self.apis, self.families, self.bindings, enumeration_complete=True, routes=partial)['leaf']['counts_are_lower_bounds'])
        self.assertNotEqual(binding_hash({'bindings': self.bindings, 'routes': self.routes}, 'leaf'),
                            binding_hash({'bindings': self.bindings, 'routes': partial}, 'leaf'))

    def test_omitted_step_and_supporting_only_complete_route_are_rejected(self):
        broken = deepcopy(self.routes); broken[0]['steps'].pop()
        with self.assertRaisesRegex(ValueError, 'exactly its bound APIs'):
            validate_routes({'leaf': {}}, self.apis, self.bindings, broken)
        supporting = [{**row, 'role': 'supporting'} for row in self.bindings]
        with self.assertRaisesRegex(ValueError, 'Supporting steps alone'):
            validate_routes({'leaf': {}}, self.apis, supporting, self.routes)
