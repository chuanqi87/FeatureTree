"""Self-contained integration fixtures with synthetic provenance, never real release data."""
from copy import deepcopy
from pathlib import Path
import shutil

from featuretree.console.application import Application
from featuretree.corpus.importers import json_lines
from tests.fixtures.v2 import PROJECT
from tests.fixtures.v2_pipeline import ModelSubstitute, baseline, source_fixture


def application(root):
    shutil.copytree(PROJECT / 'config/v2', root / 'config/v2')
    shutil.copytree(PROJECT / '.opencode/agents', root / '.opencode/agents')
    app = Application(root, ModelSubstitute())
    store, original, catalog = source_fixture(root, app.schemas)
    base = baseline()
    for platform, item in base['platforms'].items():
        doc = catalog.get(original['id'], 'documents', 'doc_' + platform)
        evidence = {'id': 'baseline_' + platform, 'platform': platform, 'snapshot_id': original['id'],
                    'document_id': doc['id'], 'url': doc['url'], 'body_sha256': doc['body_sha256'],
                    'excerpt': 'Fixture official documentation for ' + platform, 'locator': 'body',
                    'applicability': 'verified', 'source_revision': 'synthetic-test'}
        item.update(status='verified_stable', verified_at=base['created_at'], evidence_refs=[app.artifacts.put(evidence)])
    baseline_ref = app.artifacts.put(base)
    snapshot = store.seal({kind: json_lines(store.path(original['id'], kind)) for kind in original['records']},
                          files=[], status='verified', baseline_ref=baseline_ref)
    return app, snapshot, baseline_ref


def run(app, snapshot, inputs, key, pipeline='taxonomy', mode='calibration'):
    request = {'pipeline': pipeline, 'model': 'test/substitute', 'scopes': [{
        'definition': 'Synthetic integration scope', 'snapshot_id': snapshot['id'], 'selection': {},
        'topic_selection': {}, 'inputs': inputs, 'mode': mode, 'enumeration_complete': True}]}
    state = app.planner.create(request, key)
    state = app.runner.run(state['run_id'])
    if not all(task['status'] == 'completed' for task in state['tasks'].values()):
        raise AssertionError(state)
    final = 'ft-check' if pipeline == 'taxonomy' else 'fk-assemble'
    payload = app.artifacts.get(state['tasks']['w_0000--' + final]['result_ref'])['payload']
    return state, payload


def publishable(app, snapshot, baseline_ref):
    state, check = run(app, snapshot, {'baseline_ref': baseline_ref}, 'tree')
    tree = app.artifacts.get(check['tree_ref'])
    inputs = {key: check[key] for key in ('tree_ref', 'bindings_ref')}
    inputs.update(feature_ref=app.artifacts.put(tree['features'][0]), baseline_ref=baseline_ref)
    _, draft = run(app, snapshot, inputs, 'draft', 'knowledge')
    policy_refs = {name + '_policy_ref': app.artifacts.put(__import__('json').loads((app.root / 'config/v2/rules' / (name + '.json')).read_text())) for name in ('granularity', 'confidence')}
    approval = app.calibration.approve({'actor': 'test-human', 'decision': 'approved',
        'tree_ref': check['tree_ref'], 'sample_article_refs': [draft['article_ref']],
        'scope_ids': [tree['features'][0]['id']], **policy_refs}, 'approval')
    freeze = app.freezes.prepare({'tree_ref': check['tree_ref'], 'bindings_ref': check['bindings_ref'],
        'baseline_ref': baseline_ref, 'snapshot_id': snapshot['id'], 'root_ids': [tree['features'][0]['id']],
        'approval_ref': approval['approval_ref'], 'review_refs': [state['tasks']['w_0000--' + stage]['result_ref']
        for stage in ('ft-granularity', 'ft-coverage', 'ft-review', 'ft-integrate')]})
    inputs['freeze_ref'] = freeze['freeze_ref']
    _, article = run(app, snapshot, inputs, 'formal', 'knowledge', 'formal')
    candidate = {'tree_ref': check['tree_ref'], 'bindings_ref': check['bindings_ref'],
        'baseline_ref': baseline_ref, 'source_ids': [snapshot['id']], 'freeze_refs': [freeze['freeze_ref']],
        'knowledge_refs': {tree['features'][0]['id']: article['article_ref']}}
    return candidate
