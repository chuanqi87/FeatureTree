"""Identify and reap a recorded worker without killing a reused process ID."""

import os
import signal
import subprocess
import time

from featuretree.core.io import read_json


def identity(pid):
    result = subprocess.run(["ps", "-p", str(pid), "-o", "lstart=", "-o", "command="],
                            capture_output=True, text=True, timeout=5)
    return result.stdout.strip() if result.returncode == 0 else None


def terminate_recorded(path):
    if not path.is_file():
        return
    record = read_json(path)
    pid = record["pid"]
    if not record["identity"] or identity(pid) != record["identity"]:
        return  # Original worker exited, or the OS has reused its PID.
    try:
        if os.getpgid(pid) != pid:
            raise ValueError("Recorded worker is no longer its own process group leader")
        os.killpg(pid, signal.SIGTERM)
        deadline = time.monotonic() + 3
        while time.monotonic() < deadline:
            if identity(pid) != record["identity"]:
                return
            time.sleep(0.05)
        os.killpg(pid, signal.SIGKILL)
    except ProcessLookupError:
        return
