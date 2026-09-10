"""v2 route dispatch. HTTP details and business use cases remain separate."""

from featuretree.core.io import ConflictError
from featuretree.console.launcher import launch


class Api:
    def __init__(self, application):
        self.app = application

    def get(self, parts, query):
        app = self.app
        release_id = query.get('release_id')
        if parts == ['current']:
            return app.reader.current()
        if parts == ['config']:
            from featuretree.core.io import read_json
            return {'pipelines': app.registry.configuration, 'protocol_version': 2,
                    'policies': {name: read_json(app.root / 'config/v2/rules' / f'{name}.json') for name in ('granularity', 'confidence')}}
        if parts == ['tree']:
            return app.reader.tree(release_id)
        if len(parts) == 2 and parts[0] == 'features':
            return app.reader.feature(parts[1], release_id)
        if len(parts) == 2 and parts[0] == 'knowledge':
            return app.reader.knowledge(parts[1], release_id)
        if parts == ['sources']:
            return {'items': [{key: row[key] for key in ('id', 'created_at', 'status', 'counts', 'baseline_ref', 'gaps')}
                              for row in app.snapshots.list()]}
        if len(parts) == 2 and parts[0] == 'sources':
            return app.snapshots.get(parts[1])
        if parts in (['apis'], ['topics'], ['documents']):
            selection = {}
            if query.get('platform'):
                selection['platforms'] = [query['platform']]
            if query.get('query'):
                selection['query'] = query['query']
            return app.catalog.page(query['snapshot_id'], selection, query.get('cursor'),
                                    int(query.get('limit', 50)), {'apis': 'declarations'}.get(parts[0], parts[0]))
        if len(parts) == 3 and parts[0] == 'source-body':
            return app.catalog.read_body(parts[1], parts[2], int(query.get('offset', 0)))
        if parts == ['runs']:
            return {'items': [{key: row[key] for key in ('run_id', 'status', 'updated_at')}
                              for row in app.runs.list()]}
        if len(parts) == 2 and parts[0] == 'runs':
            return app.run_detail(parts[1])
        if parts == ['candidates']:
            return {'items': app.candidates()}
        if parts == ['calibrations']:
            return {'items': app.calibration.list()}
        if parts == ['freezes']:
            return {'items': app.freezes.list()}
        if parts == ['releases', 'compare']:
            return app.reader.compare(query['before'], query['after'])
        if len(parts) == 2 and parts[0] == 'objects':
            return {'object_ref': parts[1], 'object': app.artifacts.get(parts[1]), 'status': 'explicit_artifact_view'}
        if parts == ['reviews']:
            return app.review_queue()
        if len(parts) == 2 and parts[0] == 'reviews':
            row = next((row for row in app.review_queue()['tickets'] if row['id'] == parts[1]), None)
            if row is None:
                raise KeyError(parts[1])
            return {**row, 'article': app.artifacts.get(row['article_ref'])}
        if parts == ['releases']:
            current = app.versions.current_id()
            return {'current_release_id': current, 'items': [{**app.versions.get(path.parent.name),
                    'status': 'published' if app.versions._contains(current, path.parent.name) else 'candidate'}
                    for path in sorted((app.root / 'data/releases').glob('*/manifest.json'))]}
        if len(parts) == 2 and parts[0] == 'releases':
            return app.versions.get(parts[1])
        raise KeyError('/'.join(parts))

    def post(self, parts, body, key):
        app = self.app
        if 'expected_release_id' not in body:
            raise ValueError('Write commands require expected_release_id, including null before first publication')
        def operation(request_key):
            if app.versions.current_id() != body['expected_release_id']:
                raise ConflictError('Current release changed; refresh the proposed operation')
            return self._post(parts, body, request_key)
        return app.requests.execute(key, {'route': parts, 'body': body}, operation)

    def _post(self, parts, body, key):
        app = self.app
        if parts == ['runs']:
            return app.planner.create(body['request'], key)
        if parts == ['knowledge', 'plans']:
            return app.knowledge_planning.create(body['request'], key)
        if len(parts) == 3 and parts[0] == 'runs' and parts[2] == 'actions':
            if body['action'] == 'replan':
                return app.replanning.create(parts[1], body['request'], key)
            if body['action'] == 'supplement':
                return app.source_supplement.supplement(parts[1], body['work_id'], key, body.get('source_requests'))
            if body['action'] in ('start', 'resume'):
                return launch(app, parts[1])
            return app.runner.action(parts[1], body['action'], task_id=body.get('task_id'), feedback=body.get('feedback', []))
        if parts == ['freezes']:
            return app.freezes.prepare(body['request'])
        if parts == ['calibrations', 'approve']:
            return app.calibration.approve(body['request'], key)
        if parts == ['policies', 'snapshot']:
            from featuretree.core.io import read_json
            return {name + '_policy_ref': app.artifacts.put(read_json(app.root / 'config/v2/rules' / f'{name}.json'))
                    for name in ('granularity', 'confidence')}
        if parts == ['releases', 'prepare']:
            return app.releases.prepare(body['candidate'], body['expected_release_id'], key)
        if parts == ['releases', 'publish']:
            return app.releases.publish(body['transaction_key'])
        if parts == ['releases', 'rollback']:
            return app.releases.rollback(body['target_release_id'], body['expected_release_id'], key)
        if parts == ['releases', 'rebase']:
            return app.releases.rebase(body['transaction_key'], body['expected_release_id'], key)
        if parts == ['releases', 'export']:
            return app.reader.export(app.root / 'output/exports', body['release_id'])
        if len(parts) == 3 and parts[0] == 'reviews' and parts[2] == 'decisions':
            ticket = self.get(parts[:2], {})
            if body['article_ref'] != ticket['article_ref']:
                raise ConflictError('Review article version changed')
            result = app.reviews.submit(body['article_ref'], ticket['article_ref'], body['decision'], key)
            revision = result.get('revision')
            if revision and revision.get('run_id'):
                result['worker'] = launch(app, revision['run_id'])
            return result
        raise KeyError('/'.join(parts))
