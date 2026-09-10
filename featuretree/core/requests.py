"""Durable idempotency records for application commands."""

from featuretree.core.content import digest, identifier
from featuretree.core.io import ConflictError, file_lock, read_json, write_json


class RequestStore:
    def __init__(self, directory):
        self.directory = directory

    def execute(self, key, command, operation):
        identifier(key)
        path = self.directory / f"{key}.json"
        with file_lock(self.directory / f"{key}.lock"):
            fingerprint = digest(command)
            if path.exists():
                record = read_json(path)
                if record["command_hash"] != fingerprint:
                    raise ConflictError("Idempotency key was used for different input")
                if record["state"] == "completed":
                    return record["result"]
            write_json(path, {"command_hash": fingerprint, "state": "started"})
            # Operations receive the key and must themselves recover after a crash.
            result = operation(key)
            write_json(path, {"command_hash": fingerprint, "state": "completed", "result": result})
            return result
