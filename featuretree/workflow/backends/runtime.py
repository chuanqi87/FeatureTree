"""Share pinned dependency code while retaining isolated tools, prompts and sessions."""

import os
import subprocess
from featuretree.core.content import file_digest
from featuretree.core.io import ConflictError, read_json, write_bytes


def prepare_runtime(executable, directory, workspace):
    package = read_json(directory / "package.json")
    expected = package["dependencies"]["@opencode-ai/plugin"]
    actual = subprocess.run([executable, "--version"], capture_output=True, text=True, timeout=15, check=True).stdout.strip()
    if actual != expected:
        raise ConflictError(f"OpenCode {actual} differs from the pinned plugin {expected}; update and verify the runtime before replanning")
    modules = directory / "node_modules"
    installed = read_json(modules / "@opencode-ai/plugin/package.json")
    if installed["version"] != expected:
        raise ConflictError("Install the pinned runtime with npm ci --prefix tools/opencode --ignore-scripts")
    target = workspace / ".opencode"
    target.mkdir(parents=True, exist_ok=True)
    for name in ("package.json", "package-lock.json"):
        write_bytes(target / name, (directory / name).read_bytes(), immutable=True)
    link = target / "node_modules"
    if link.exists():
        if not link.is_symlink() or link.resolve() != modules.resolve():
            raise ConflictError("Attempt workspace already contains a different dependency runtime")
    else:
        link.symlink_to(os.path.relpath(modules.resolve(), target.resolve()), target_is_directory=True)
    return {"opencode_version": actual, "plugin_version": expected,
            "package_lock_sha256": file_digest(directory / "package-lock.json")}
