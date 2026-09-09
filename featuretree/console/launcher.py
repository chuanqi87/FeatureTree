"""Launch detached workflow coordinators without blocking HTTP requests."""

import shutil
import subprocess
import sys
import threading
from featuretree.core.storage import write_json
from featuretree.console.runs import active_process
from featuretree.workflow.state import run_path
from featuretree.workflow.backends.processes import identity


class ProcessLauncher:
    def available(self):
        return shutil.which("opencode") is not None

    def active(self, folder):
        return active_process(folder)

    def start(self, root, run_id):
        folder = run_path(root, run_id)
        with (folder / "console-runner.log").open("ab") as log:
            process = subprocess.Popen([sys.executable, str(root / "scripts/workflow.py"),
                "--root", str(root), "run", run_id], cwd=root, stdin=subprocess.DEVNULL,
                stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
        write_json(folder / "console-process.json", {"pid": process.pid, "identity": identity(process.pid)})
        threading.Thread(target=process.wait, daemon=True).start()
