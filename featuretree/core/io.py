"""Durable local IO; immutable writes never replace an existing object."""

from contextlib import contextmanager
import fcntl
import json
import os
from pathlib import Path
import tempfile

from featuretree.core.content import canonical_bytes


class ConflictError(ValueError):
    """The caller's expected version or idempotent request no longer matches."""


class IntegrityError(ValueError):
    """Stored bytes or referenced content do not match their sealed identity."""


def read_json(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise IntegrityError(f"Duplicate JSON key: {key}")
            result[key] = value
        return result
    return json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=unique)


def sync_directory(path):
    descriptor = os.open(path, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def write_bytes(path, content, *, immutable=False):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".pending-", delete=False) as stream:
        temporary = Path(stream.name)
        stream.write(content)
        stream.flush()
        os.fsync(stream.fileno())
    try:
        if immutable:
            try:
                os.link(temporary, path)
            except FileExistsError:
                if path.read_bytes() != content:
                    raise IntegrityError(f"Immutable content collision: {path}") from None
        else:
            os.replace(temporary, path)
        sync_directory(path.parent)
    finally:
        temporary.unlink(missing_ok=True)


def write_json(path, value, *, immutable=False):
    write_bytes(path, canonical_bytes(value) + b"\n", immutable=immutable)


@contextmanager
def file_lock(path, *, blocking=True):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a+b") as stream:
        flags = fcntl.LOCK_EX | (0 if blocking else fcntl.LOCK_NB)
        try:
            fcntl.flock(stream.fileno(), flags)
        except BlockingIOError:
            raise ConflictError(f"Operation already running: {path.name}") from None
        try:
            yield
        finally:
            fcntl.flock(stream.fileno(), fcntl.LOCK_UN)
