"""Thin command adapters for explicit application use cases."""

from featuretree.core.io import read_json
from featuretree.corpus.importers import import_reference, json_lines
from featuretree.taxonomy.model import change_impact, validate_tree
from featuretree.console.api import Api
from featuretree.console.server import serve


def execute(app, args, key):
    request = read_json(args.request) if args.request else {}
    group, action = args.group, args.action
    expected = args.expected if args.expected not in (None, 'none') else None if args.expected == 'none' else app.versions.current_id()
    api = Api(app)
    def post(route, body):
        return api.post(route.split('/'), {'expected_release_id': expected, **body}, key)
    if group == 'console':
        return serve(app, args.port)
    if group == 'sources':
        if action == 'extract':
            from featuretree.corpus.sdk import extract_sdk
            return extract_sdk(app.root, request, app.snapshots)
        if action == 'capture':
            from featuretree.corpus.capture import capture_sources
            return capture_sources(app.snapshots, app.root / 'docs-raw/official', request['source_requests'], request.get('parent_snapshot_id'))
        if action == 'import':
            if not args.reference:
                raise ValueError('--reference is required for a one-time historical import')
            return import_reference(args.reference, app.snapshots, app.root / 'data/imports', app.root / 'docs-raw/official')
        if action == 'validate':
            return app.snapshots.verify(args.snapshot)
        if action == 'report':
            return app.snapshots.get(args.snapshot) if args.snapshot else api.get(['sources'], {})
        if action == 'query':
            selection = {'query': args.query}
            if args.platform:
                selection['platforms'] = [args.platform]
            return app.catalog.page(args.snapshot, selection, args.cursor, args.limit)
        if action == 'seal':
            from pathlib import Path
            collections = {name: json_lines(Path(path)) for name, path in request['collections'].items()}
            return app.snapshots.seal(collections, files=request['files'], baseline_ref=request.get('baseline_ref'),
                                      status=request.get('status', 'candidate'), gaps=request.get('gaps', []),
                                      extractor_versions=request.get('extractor_versions', {}), provenance=request.get('provenance', {}))
    if group in ('workflow', 'knowledge') and action == 'plan':
        if group == 'knowledge' and 'scopes' not in request:
            return post('knowledge/plans', {'request': request})
        return post('runs', {'request': request})
    if group == 'workflow':
        if action == 'replan':
            return post(f'runs/{args.id}/actions', {'action': action, 'request': request})
        if action in ('run', 'resume'):
            return app.runner.run(args.id)
        if action == 'report':
            return app.run_detail(args.id) if args.id else api.get(['runs'], {})
        return post(f'runs/{args.id}/actions', {'action': action, **request})
    if group == 'taxonomy':
        if action == 'approve-calibration':
            return post('calibrations/approve', {'request': request})
        if action == 'policies':
            return post('policies/snapshot', {})
        if action == 'check':
            nodes = validate_tree(app.artifacts.get(args.id))
            return {'valid': True, 'feature_count': len(nodes)}
        if action == 'diff':
            return change_impact(app.artifacts.get(args.before), app.artifacts.get(args.after))
        if action == 'freeze':
            return post('freezes', {'request': request})
    if group == 'knowledge':
        if action == 'import-observation':
            return app.observations.import_record(request)
        if action == 'show':
            return app.reader.knowledge(args.id, args.after)
        if action == 'impact':
            manifest = app.versions.pin(args.after)
            return app.releases.validate(manifest)
        if action == 'check':
            from featuretree.workflow.knowledge_validation import validate_article
            article = app.artifacts.get(args.id)
            return {**validate_article(article, app.artifacts, app.schemas, app.catalog, app.provenance), 'article_ref': args.id}
    if group == 'review':
        if action == 'queue':
            return app.review_queue()
        if action == 'show':
            return api.get(['reviews', args.id], {})
        return post(f'reviews/{args.id}/decisions', request)
    if group == 'release':
        if action == 'prepare':
            return post('releases/prepare', {'candidate': request})
        if action == 'publish':
            return post('releases/publish', {'transaction_key': args.id})
        if action == 'rebase':
            return post('releases/rebase', {'transaction_key': args.id})
        if action == 'rollback':
            return post('releases/rollback', {'target_release_id': args.id})
        if action == 'show':
            return app.versions.get(args.id) if args.id else app.reader.current()
        if action == 'compare':
            return app.reader.compare(args.before, args.after)
        if action == 'export':
            return app.reader.export(app.root / 'output/exports', args.id)
    raise ValueError('Unsupported command')
