"""Read-only projection of live attempts, recovery work and committed checkpoints."""
import json
from datetime import datetime, timezone

from featuretree.core.io import read_json


def optional_json(path):
    try:
        return read_json(path)
    except (OSError, ValueError):
        return {}


def event_tail(path):
    """Expose operational events only; never publish model reasoning or tool bodies."""
    if not path.exists():
        return []
    with path.open('rb') as stream:
        stream.seek(max(0, path.stat().st_size - 131072))
        lines = stream.read().decode('utf-8', errors='replace').splitlines()
    result = []
    for line in lines:
        try:
            event = json.loads(line)
        except ValueError:
            continue
        part = event.get('part', {})
        if event.get('type') not in ('step_start', 'step_finish', 'tool_use', 'error'):
            continue
        result.append({'type': event['type'], 'timestamp': event.get('timestamp'),
                       'tool': part.get('tool'), 'status': part.get('state', {}).get('status'),
                       'reason': part.get('reason')})
    return result[-12:]


def stage_activity(folder, task, artifacts, process_identity):
    directory = folder / 'attempts' / task['id']
    progress_paths = list(directory.glob('*/batch-progress.json'))
    latest = max(progress_paths, key=lambda p: p.stat().st_mtime) if progress_paths else None
    progress = optional_json(latest) if latest else {}
    accepted = {}
    errors = []
    for path in (folder / 'batch-checkpoints' / task['id']).glob('*.json'):
        try:
            receipt = read_json(path)
            packet = artifacts.get(receipt['input_ref'])
            if packet.get('batch_revision', packet['revision']) != task.get('batch_revision', task['revision']):
                continue
            response = artifacts.get(receipt['result_ref'])
            metadata = artifacts.get(receipt['metadata_ref'])
            if metadata.get('validation') != 'accepted' or response['input_hash'] != packet['input_hash'] or receipt['input_hash'] != packet['input_hash']:
                raise ValueError('Checkpoint identity or validation mismatch')
            index = packet['batch']['index']
            accepted[index] = {'batch': index + 1, 'result_ref': receipt['result_ref'],
                'outcome': response['outcome'], 'api_count': len(packet['work']['api_ids']),
                'topic_count': len(packet['work']['topic_ids']), 'fact_count': len(response['payload'].get('facts', []))}
        except (OSError, ValueError, KeyError) as error:
            errors.append({'file': path.name, 'error': type(error).__name__})
    events = list(directory.glob('**/events.jsonl'))
    current = max(events, key=lambda p: p.stat().st_mtime) if events else None
    live = None
    if current:
        record = optional_json(current.parent / 'process.json')
        alive = bool(record and process_identity(record.get('pid')) == record.get('identity') and record.get('identity'))
        parent = current.parent
        while parent != directory and not (parent / 'input.json').exists():
            parent = parent.parent
        packet = optional_json(parent / 'input.json')
        workspace = parent / 'workspace'
        ids = packet.get('work', {})
        live = {'process_alive': alive, 'batch': packet.get('batch', {}).get('index', -1) + 1,
                'recovery': 'recovery' in str(current.relative_to(directory)),
                'last_activity_at': datetime.fromtimestamp(current.stat().st_mtime, timezone.utc).isoformat(),
                'api_ids': ids.get('api_ids', []), 'topic_ids': ids.get('topic_ids', []),
                'source_calls': len(list((workspace / 'source_calls').glob('*.json'))),
                'payload_chunks': len([p for p in (workspace / 'delivery').glob('*.json') if len(p.stem) == 64]),
                'file_completed': ((workspace / 'delivery/result.json').exists() or
                                   (workspace / 'delivery/completed.json').exists()),
                'events': event_tail(current)}
    status = 'running' if live and live['process_alive'] else progress.get('status', task['status'])
    if status == 'running' and live and not live['process_alive']:
        status = 'awaiting_inspection'
    return {'status': status, 'scheduler_status': task['status'], 'progress': progress,
            'completed': len(accepted), 'total': progress.get('total', len(accepted)),
            'accepted': sorted(accepted.values(), key=lambda row: row['batch']),
            'live': live, 'checkpoint_errors': errors}


def workflow_activity(folder, state, artifacts, process_identity):
    stages = {key: stage_activity(folder, task, artifacts, process_identity) for key, task in state['tasks'].items()}
    return {'observed_at': datetime.now(timezone.utc).isoformat(), 'stages': stages,
            'completed_batches': sum(row['completed'] for row in stages.values()),
            'total_batches': sum(row['total'] for row in stages.values()),
            'active_stages': sum(row['status'] == 'running' for row in stages.values())}
