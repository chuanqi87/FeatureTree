"""Loopback-only v2 HTTP server with host, origin and per-process write-token checks."""

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import secrets
from urllib.parse import parse_qs, unquote, urlsplit

from featuretree.core.io import ConflictError
from featuretree.console.api import Api


class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Content-Security-Policy', "frame-ancestors 'none'")
        self.send_header('X-Frame-Options', 'DENY')
        self.send_header('Referrer-Policy', 'no-referrer')
        super().end_headers()
    def __init__(self, *args, application, token, **kwargs):
        self.api, self.token = Api(application), token
        super().__init__(*args, directory=str(application.root / 'web/dist'), **kwargs)

    def _host_allowed(self):
        try:
            host = urlsplit('http://' + self.headers.get('Host', ''))
            return host.hostname in ('localhost', '127.0.0.1', '::1') and host.port == self.server.server_port
        except ValueError:
            return False

    def _send(self, status, value):
        content = json.dumps(value, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Content-Length', str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def _route(self):
        parsed = urlsplit(self.path)
        if not parsed.path.startswith('/api/v2/'):
            raise KeyError('Only v2 API routes are supported')
        return [unquote(part) for part in parsed.path[len('/api/v2/'):].split('/') if part], {
            key: values[-1] for key, values in parse_qs(parsed.query).items()}

    def do_GET(self):
        if not self._host_allowed():
            return self._send(403, {'error': 'Loopback Host required'})
        if not self.path.startswith('/api/'):
            return super().do_GET()
        try:
            parts, query = self._route()
            result = self.api.get(parts, query)
            if parts == ['config']:
                result['write_token'] = self.token
            return self._send(200, result)
        except Exception as error:
            return self._error(error)

    def do_POST(self):
        origin = self.headers.get('Origin')
        expected = 'http://' + self.headers.get('Host', '')
        if (not self._host_allowed() or (origin and origin != expected)
                or self.headers.get('X-FeatureTree-Token') != self.token
                or self.headers.get('Sec-Fetch-Site') in ('cross-site', 'same-site')):
            return self._send(403, {'error': 'Local origin and write token required'})
        try:
            if self.headers.get('Content-Type', '').split(';')[0] != 'application/json':
                raise ValueError('JSON content type required')
            length = int(self.headers.get('Content-Length', 0))
            if not 0 < length <= 2 * 1024 * 1024:
                raise ValueError('Invalid request body size')
            body = json.loads(self.rfile.read(length))
            key = self.headers.get('Idempotency-Key')
            if not key:
                raise ValueError('Idempotency-Key required')
            parts, _ = self._route()
            result = self.api.post(parts, body, key)
            asynchronous = parts in (['runs'], ['knowledge', 'plans']) or (len(parts) == 3 and parts[0] == 'runs' and body.get('action') in ('start', 'resume'))
            return self._send(202 if asynchronous else 200, result)
        except Exception as error:
            return self._error(error)

    def _error(self, error):
        status = 409 if isinstance(error, ConflictError) else 404 if isinstance(error, (KeyError, FileNotFoundError)) else 400 if isinstance(error, ValueError) else 500
        self._send(status, {'error': str(error), 'type': type(error).__name__})


def serve(application, port=8765):
    server = ThreadingHTTPServer(('127.0.0.1', port), partial(Handler, application=application, token=secrets.token_urlsafe(32)))
    print(f'FeatureTree v2: http://127.0.0.1:{server.server_port}', flush=True)
    try:
        server.serve_forever()
    finally:
        server.server_close()
