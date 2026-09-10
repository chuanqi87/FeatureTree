"""Immutable manifests and a single atomic pointer, with recoverable compare-and-swap."""

from featuretree.core.content import digest, identifier
from featuretree.core.io import ConflictError, IntegrityError, file_lock, read_json, write_json


class VersionStore:
    def __init__(self, directory, artifacts):
        self.directory = directory
        self.artifacts = artifacts

    def current_id(self):
        path = self.directory / "CURRENT.json"
        if not path.exists():
            return None
        pointer = read_json(path)
        manifest = self.get(pointer["release_id"])
        if digest(manifest) != pointer["manifest_hash"]:
            raise IntegrityError("Current manifest does not match its pointer")
        return manifest["release_id"]

    def get(self, release_id):
        identifier(release_id)
        path = self.directory / "releases" / release_id / "manifest.json"
        record = read_json(path)
        manifest = self.artifacts.get(record["object_ref"])
        if manifest["release_id"] != release_id:
            raise IntegrityError("Manifest identity mismatch")
        return manifest

    def pin(self, release_id=None):
        release_id = release_id or self.current_id()
        return self.get(release_id) if release_id else None

    def prepare(self, manifest, expected, key):
        identifier(key)
        request_hash = digest({"manifest": manifest, "expected": expected})
        transaction_path = self.directory / "transactions" / f"{key}.json"
        with file_lock(self.directory / "release.lock"):
            if transaction_path.exists():
                transaction = read_json(transaction_path)
                if transaction["request_hash"] != request_hash:
                    raise ConflictError("Publication key already belongs to another candidate")
                return transaction
            if self.current_id() != expected:
                raise ConflictError("Current release changed before preparation")
            if manifest["parent_id"] != expected:
                raise ConflictError("Manifest parent must match expected release")
            reference = self.artifacts.put(manifest)
            write_json(self.directory / "releases" / manifest["release_id"] / "manifest.json",
                       {"object_ref": reference}, immutable=True)
            transaction = {"key": key, "request_hash": request_hash, "state": "prepared",
                           "expected": expected, "release_id": manifest["release_id"],
                           "manifest_hash": reference}
            write_json(transaction_path, transaction)
            return transaction

    def commit(self, key, validate):
        """Revalidate under the publication lock; readers see the old or full new version."""
        identifier(key)
        path = self.directory / "transactions" / f"{key}.json"
        with file_lock(self.directory / "release.lock"):
            transaction = read_json(path)
            target = transaction["release_id"]
            current = self.current_id()
            if transaction["state"] == "committed":
                return transaction
            # Recover a crash after pointer replacement, even if another release followed it.
            if self._contains(current, target):
                transaction["state"] = "committed"
                write_json(path, transaction)
                return transaction
            if current != transaction["expected"]:
                raise ConflictError("Publication conflict: current release changed")
            manifest = self.get(target)
            if digest(manifest) != transaction["manifest_hash"]:
                raise IntegrityError("Prepared manifest changed")
            validate(manifest)
            write_json(self.directory / "CURRENT.json",
                       {"release_id": target, "manifest_hash": transaction["manifest_hash"]})
            transaction["state"] = "committed"
            write_json(path, transaction)
            return transaction

    def _contains(self, current, target):
        seen = set()
        while current:
            if current in seen:
                raise IntegrityError("Cyclic release history")
            if current == target:
                return True
            seen.add(current)
            current = self.get(current)["parent_id"]
        return False
