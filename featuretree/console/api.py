"""Same-origin HTTP boundary for local workflow controls."""

from http import HTTPStatus
import json
import secrets
from urllib.parse import parse_qs, urlsplit

from jsonschema import ValidationError

from featuretree.console.service import RunConflict


class WorkflowAPI:
    def __init__(self, service):
        self.service = service
        self.token = secrets.token_urlsafe(32)

    def trusted_host(self, request):
        # Vite's development proxy preserves its original loopback Host header.
        ports = {request.server.server_port, 5173}
        return request.headers.get("Host") in {f"{h}:{p}" for h in ("127.0.0.1", "localhost") for p in ports}

    def handle(self, request, method):
        url = urlsplit(request.path)
        parts = url.path.strip("/").split("/")
        if parts[:2] != ["api", "workflow"]:
            return False
        status = HTTPStatus.OK
        try:
            if not self.trusted_host(request):
                raise PermissionError("管理接口仅接受本机地址访问")
            if method == "GET" and parts == ["api", "workflow", "config"]:
                result = {**self.service.options(), "csrf_token": self.token}
            elif method == "GET" and parts == ["api", "workflow", "runs"]:
                result = {"runs": self.service.list_runs(parse_qs(url.query).get("node", [None])[0])}
            elif method == "GET" and len(parts) == 4 and parts[2] == "runs":
                result = self.service.get_run(parts[3])
            elif method == "POST":
                self.authorize(request)
                body = self.read_body(request)
                if parts == ["api", "workflow", "runs"]:
                    result = self.service.create(body)
                elif len(parts) == 5 and parts[2] == "runs" and parts[4] in ("start", "retry", "revise", "publish"):
                    result = self.service.act(parts[3], parts[4], body)
                else:
                    raise FileNotFoundError("没有这个执行接口")
                status = HTTPStatus.ACCEPTED
            else:
                raise FileNotFoundError("没有这个执行接口")
        except PermissionError as exc:
            result, status = {"error": str(exc)}, HTTPStatus.FORBIDDEN
        except RunConflict as exc:
            result, status = {"error": str(exc)}, HTTPStatus.CONFLICT
        except FileNotFoundError:
            result, status = {"error": "未找到指定的任务或配置"}, HTTPStatus.NOT_FOUND
        except (ValueError, TypeError, KeyError, ValidationError) as exc:
            result, status = {"error": exc.message if isinstance(exc, ValidationError) else str(exc)}, HTTPStatus.BAD_REQUEST
        except OSError as exc:
            result, status = {"error": str(exc)}, HTTPStatus.INTERNAL_SERVER_ERROR
        request.send_content(status, json.dumps(result, ensure_ascii=False).encode(),
                             "application/json; charset=utf-8", True)
        return True

    def authorize(self, request):
        origin = request.headers.get("Origin")
        if origin and origin not in {f"http://{h}:{p}" for h in ("127.0.0.1", "localhost")
                                    for p in (request.server.server_port, 5173)}:
            raise PermissionError("拒绝跨站执行请求")
        if not secrets.compare_digest(request.headers.get("X-Workflow-Token", ""), self.token):
            raise PermissionError("执行凭证已失效，请刷新管理台")
        if request.headers.get_content_type() != "application/json":
            raise ValueError("执行请求必须为 JSON")

    def read_body(self, request):
        length = int(request.headers.get("Content-Length", "0"))
        if not 0 < length <= 65536:
            raise ValueError("请求内容大小无效")
        body = json.loads(request.rfile.read(length))
        if not isinstance(body, dict):
            raise ValueError("请求内容必须是对象")
        return body
