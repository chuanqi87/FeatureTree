from functools import partial
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer
import json
from pathlib import Path
import tempfile
from threading import Thread
import unittest

from featuretree.console.server import Handler
from tests.fixtures.v2_application import application


class QuietHandler(Handler):
    def log_message(self, *args):
        pass


class HttpContractTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(); self.addCleanup(temp.cleanup)
        self.app, self.snapshot, self.baseline = application(Path(temp.name))
        self.server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, application=self.app, token='test-token'))
        worker = Thread(target=self.server.serve_forever, daemon=True); worker.start()
        self.addCleanup(self.server.server_close); self.addCleanup(self.server.shutdown)

    def request(self, method, path, data=None, headers=None):
        connection = HTTPConnection('127.0.0.1', self.server.server_port, timeout=5)
        self.addCleanup(connection.close)
        connection.request(method, path, json.dumps(data) if data is not None else None, headers or {})
        response = connection.getresponse(); return response.status, json.loads(response.read())

    def test_empty_current_is_explicit_and_legacy_api_not_available(self):
        status, body = self.request('GET', '/api/v2/current')
        self.assertEqual(200, status); self.assertIsNone(body['release_id'])
        self.assertEqual(404, self.request('GET', '/api/tree')[0])
        self.assertEqual(403, self.request('GET', '/api/v2/config', headers={'Host': 'evil.example'})[0])

    def test_cross_site_and_missing_write_token_rejected(self):
        headers = {'Content-Type': 'application/json', 'Idempotency-Key': 'test'}
        self.assertEqual(403, self.request('POST', '/api/v2/runs', {}, headers)[0])
        headers.update({'X-FeatureTree-Token': 'test-token', 'Origin': 'https://evil.example'})
        self.assertEqual(403, self.request('POST', '/api/v2/runs', {}, headers)[0])

    def test_create_is_202_idempotent_and_stale_write_is_409(self):
        headers = {'Content-Type': 'application/json', 'Idempotency-Key': 'plan', 'X-FeatureTree-Token': 'test-token'}
        body = {'expected_release_id': None, 'request': {'pipeline': 'taxonomy', 'model': 'test/substitute', 'scopes': [{
            'definition': 'Test', 'snapshot_id': self.snapshot['id'], 'selection': {}, 'inputs': {'baseline_ref': self.baseline}}]}}
        first = self.request('POST', '/api/v2/runs', body, headers)
        second = self.request('POST', '/api/v2/runs', body, headers)
        self.assertEqual(202, first[0]); self.assertEqual(first[1]['run_id'], second[1]['run_id'])
        body['expected_release_id'] = 'r_stale'; headers['Idempotency-Key'] = 'stale'
        self.assertEqual(409, self.request('POST', '/api/v2/runs', body, headers)[0])
