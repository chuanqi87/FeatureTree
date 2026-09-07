"""Small local HTTP adapter; only the UI directory and snapshot are exposed."""

import json
import mimetypes
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote, urlsplit

import yaml

from .viewer import build_draft_snapshot, build_snapshot, json_default


def make_handler(repo, web_root):
    public_root = web_root.resolve()

    class ViewerHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.respond(include_body=True)

        def do_HEAD(self):
            self.respond(include_body=False)

        def respond(self, include_body):
            route = unquote(urlsplit(self.path).path)
            if route in {"/api/tree", "/api/draft-tree"}:
                try:
                    payload = build_draft_snapshot(repo) if route == "/api/draft-tree" else build_snapshot(repo)
                    status = HTTPStatus.OK
                except (ValueError, KeyError, OSError, TypeError, yaml.YAMLError) as error:
                    payload = {"error": str(error)}
                    status = HTTPStatus.INTERNAL_SERVER_ERROR
                body = json.dumps(payload, ensure_ascii=False, default=json_default).encode("utf-8")
                self.send_content(status, body, "application/json; charset=utf-8", include_body)
                return
            target = (public_root / ("index.html" if route == "/" else route.lstrip("/"))).resolve()
            if not target.is_relative_to(public_root) or not target.is_file() or target.suffix not in {".html", ".css", ".js", ".svg"}:
                self.send_content(HTTPStatus.NOT_FOUND, b"Not found", "text/plain", include_body)
                return
            content_type = mimetypes.guess_type(target.name)[0] or "application/octet-stream"
            self.send_content(HTTPStatus.OK, target.read_bytes(), content_type + "; charset=utf-8", include_body)

        def send_content(self, status, body, content_type, include_body):
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'")
            self.end_headers()
            if include_body:
                self.wfile.write(body)

    return ViewerHandler


def create_server(repo, web_root, host="127.0.0.1", port=8765):
    return ThreadingHTTPServer((host, port), make_handler(repo, web_root))
