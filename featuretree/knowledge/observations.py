"""Validate imported execution material; never infer device execution from document review."""
import base64
import hashlib


def validate_observation(observation, artifacts):
    if observation['kind'] != 'device_execution' or not observation['materials']:
        raise ValueError('A device observation requires actual retained execution material')
    for material in observation['materials']:
        retained = artifacts.get(material['object_ref'])
        if retained['kind'] != 'execution_material':
            raise ValueError('A document or model response is not device execution material')
        raw = base64.b64decode(retained['content_base64'], validate=True)
        if hashlib.sha256(raw).hexdigest() != material['sha256'] or len(raw) != material['bytes']:
            raise ValueError('Execution material hash or length mismatch')
    return observation
