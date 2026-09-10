"""Bounded collection and replanning with a new immutable evidence snapshot."""
from featuretree.core.content import digest
from featuretree.core.io import ConflictError, file_lock, read_json, write_json
from featuretree.corpus.capture import capture_sources


class SourceSupplementService:
    def __init__(self, root, runs, planner, artifacts, snapshots):
        self.root, self.runs, self.planner, self.artifacts, self.snapshots = root, runs, planner, artifacts, snapshots

    def supplement(self, run_id, work_id, key, source_requests=None):
        plan, state = self.runs.load(run_id)
        work = next(row for row in plan['works'] if row['id'] == work_id)
        if any(row['status'] == 'running' for row in state['tasks'].values()):
            raise ConflictError('Stop the current run before replacing its source inputs')
        if plan['budget']['max_source_rounds'] is not None and work.get('source_round', 0) >= plan['budget']['max_source_rounds']:
            raise ValueError('Source research budget exhausted; retain the explicit gap or create a reviewed budget revision')
        requests = source_requests if source_requests is not None else [request for task in state['tasks'].values()
            if task['work_id'] == work_id and task['result_ref']
            for request in self.artifacts.get(task['result_ref'])['source_requests']]
        requests = list({digest(row): row for row in requests}.values())
        if not requests or sum(len(row['source_urls']) for row in requests) > 24:
            raise ValueError('Source collection needs explicit bounded requests (at most 24 official URLs)')
        path = self.runs.folder(run_id) / 'source_revisions' / f'{digest(key)}.json'
        fingerprint = digest({'work_id': work_id, 'requests': requests})
        with file_lock(path.with_suffix('.lock')):
            if path.exists():
                receipt = read_json(path)
                if receipt['input_hash'] != fingerprint:
                    raise ConflictError('Source revision key was reused')
            else:
                snapshot = capture_sources(self.snapshots, self.root / 'docs-raw/official', requests, work['snapshot_id'])
                receipt = {'input_hash': fingerprint, 'snapshot_id': snapshot['id'], 'source_round': work.get('source_round', 0) + 1,
                           'parent_run_id': run_id, 'parent_work_id': work_id, 'requests': requests, 'collection_gaps': snapshot['gaps']}
                write_json(path, receipt)
            if 'run_id' not in receipt:
                global_review = any(row['definition'].get('dependency_scope') == 'run' for row in plan['stage_configs'].values())
                neighbors = plan['works'] if global_review else [work]
                scopes = [{'definition': row['scope'], 'snapshot_id': receipt['snapshot_id'],
                    'selection': {'ids': row['api_ids']}, 'topic_selection': {'ids': row['topic_ids']},
                    'inputs': row['inputs'], 'mode': row['mode'], 'work_type': row['work_type'],
                    'scope_root_ids': row.get('scope_root_ids', []),
                    'enumeration_complete': row['enumeration_complete'], 'source_round': receipt['source_round'],
                    'revision_of': {'run_id': run_id, 'work_id': row['id'], 'reason': 'supplemental_sources'}} for row in neighbors]
                child = self.planner.create({'pipeline': plan['pipeline'], 'model': plan['model'], 'variant': plan['variant'],
                                             'budget': plan['budget'], 'scopes': scopes}, 'sources_' + digest(key))
                receipt['run_id'] = child['run_id']; write_json(path, receipt)
            return receipt
