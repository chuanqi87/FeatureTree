"""Use the operator's existing proxy configuration, including macOS settings."""

import os
from urllib.parse import urlsplit
from urllib import request


def request_proxies(url):
    host = urlsplit(url).hostname
    if host and request.proxy_bypass(host):
        return {}
    keys = ("http", "https", "all")
    proxies = request.getproxies()
    # A NO_PROXY-only environment masks SystemConfiguration in Python's getproxies.
    explicit = any(key.lower() in ("http_proxy", "https_proxy", "all_proxy") for key in os.environ)
    system_reader = getattr(request, "getproxies_macosx_sysconf", None)
    if not explicit and not any(key in proxies for key in keys) and system_reader:
        system_bypass = getattr(request, "proxy_bypass_macosx_sysconf", lambda _: False)
        if host and system_bypass(host):
            return {}
        proxies = system_reader()
    return {key: value for key, value in proxies.items() if key in keys}
