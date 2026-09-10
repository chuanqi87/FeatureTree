"""Launch a resumable local worker independently of the HTTP server lifetime."""

import subprocess

from featuretree.core.io import write_json
from featuretree.workflow.backends.processes import identity


def launch(application, run_id):
    application.runs.load(run_id)
    folder = application.runs.folder(run_id)
    with (folder / 'worker.log').open('a') as log:
        process = subprocess.Popen([str(application.root / '.venv/bin/python'), '-m', 'featuretree',
                                    '--root', str(application.root), 'workflow', 'run', '--id', run_id],
                                   cwd=application.root, stdout=log, stderr=log, start_new_session=True)
    write_json(folder / 'worker.json', {'pid': process.pid, 'identity': identity(process.pid)})
    return {'run_id': run_id, 'pid': process.pid, 'status': 'accepted'}
