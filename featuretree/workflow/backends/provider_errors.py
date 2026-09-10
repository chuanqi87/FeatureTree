"""Provider failures retain useful diagnostics without exposing credentials."""

import json
import re


class ProviderError(RuntimeError):
    def __init__(self, message, status_code=None, retryable=False):
        super().__init__(message)
        self.status_code, self.retryable = status_code, retryable


def provider_error(lines):
    for line in lines:
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if event.get("type") not in ("error", "session.error"):
            continue
        error = event.get("error", event.get("properties", {}))
        data = error.get("data", error) if isinstance(error, dict) else {"message": str(error)}
        message = str(data.get("message", "Provider rejected the request"))[:600]
        if "api key" in message.casefold():
            message = "Provider rejected the configured credentials"
        message = re.sub(r"(?:sk-|Bearer\s+)[A-Za-z0-9_.-]+", "[redacted]", message)
        status = data.get("statusCode")
        return ProviderError(f"Provider HTTP {status}: {message}", status,
                             bool(data.get("isRetryable")) and status not in (401, 402, 403, 404))
    return None
