"""One-time explicit import of operator-supplied device test records and raw materials."""
import base64
import hashlib
from pathlib import Path

from featuretree.core.content import timestamp
from featuretree.knowledge.observations import validate_observation


class ObservationService:
    def __init__(self, artifacts, schemas):
        self.artifacts, self.schemas = artifacts, schemas

    def import_record(self, request):
        record = {key: value for key, value in request.items() if key != 'material_paths'}
        materials = []
        for name in request['material_paths']:
            path = Path(name).resolve()
            if not path.is_file() or path.stat().st_size > 50 * 1024 * 1024:
                raise ValueError('Execution material must be an existing file of at most 50 MiB')
            raw = path.read_bytes()
            reference = self.artifacts.put({'kind': 'execution_material', 'name': path.name,
                                            'content_base64': base64.b64encode(raw).decode()})
            materials.append({'name': path.name, 'object_ref': reference, 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)})
        record.update(schema_version=1, kind='device_execution', materials=materials, imported_at=timestamp())
        self.schemas.validate('https://featuretree.local/schema/knowledge/v1/observation', record)
        validate_observation(record, self.artifacts)
        return {'observation_ref': self.artifacts.put(record)}
