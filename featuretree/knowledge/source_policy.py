"""Source identity checks, independent of retrieval and claim interpretation."""

import re
from urllib.parse import urlsplit


def official_source_error(url, platform, distribution):
    try:
        parsed = urlsplit(url)
        port = parsed.port
    except (ValueError, TypeError):
        return "Invalid official source URL"
    host = (parsed.hostname or "").lower()
    if parsed.scheme != "https" or parsed.username or parsed.password or port not in (None, 443):
        return "Evidence requires an official HTTPS URL"
    allowed = {
        "android": {"developer.android.com", "source.android.com", "developers.google.com", "firebase.google.com"},
        "ios": {"developer.apple.com", "support.apple.com", "www.apple.com", "developers.google.com", "firebase.google.com"},
        "harmonyos": {"developer.huawei.com"},
    }
    openharmony = host == "github.com" and parsed.path.startswith("/openharmony/docs/")
    if openharmony:
        if platform != "harmonyos":
            return f"OpenHarmony evidence cannot confirm {platform}"
        if distribution.casefold() != "openharmony":
            return "OpenHarmony evidence cannot confirm a HarmonyOS distribution"
        if not re.match(r"/openharmony/docs/blob/[a-f0-9]{40}/", parsed.path):
            return "OpenHarmony evidence requires an immutable commit URL"
        return None
    if host not in allowed.get(platform, set()):
        return f"Source is not an allowed official source for {platform}: {host}"
    if platform == "ios" and host == "developer.apple.com" and re.match(
            r"/documentation/(?:visionos|macos|watchos|tvos|ipados)(?:/|$)", parsed.path, re.I):
        return "Explicit non-iOS documentation path; use the iOS-specific or shared framework source"
    if platform == "android" and host in {"firebase.google.com", "developers.google.com"}:
        if re.search(r"/(?:ios(?:-[^/]+)?|ios-sdk|swift|web|unity|flutter)(?:/|$)", parsed.path, re.I):
            return "Explicit non-Android ecosystem documentation; retrieve the Android-specific source"
    if platform == "ios" and host in {"firebase.google.com", "developers.google.com"}:
        if re.search(r"/(?:android|web|unity|flutter)(?:/|$)", parsed.path, re.I):
            return "Explicit non-iOS ecosystem documentation; retrieve the iOS-specific source"
    return None


def ios_applicability(metadata):
    """Only reject explicit non-iOS availability; absent metadata stays unknown."""
    availability = metadata.get("availability") or metadata.get("platforms") or []
    names = []
    for item in availability:
        if isinstance(item, str):
            names.append(item.split(":", 1)[0].strip().casefold())
        elif isinstance(item, dict):
            names.append(str(item.get("name", item.get("platform", ""))).casefold())
    if "ios" in names:
        return "ios_listed_version_unverified"
    known = {"macos", "mac catalyst", "maccatalyst", "watchos", "tvos", "visionos", "ipados"}
    if names and all(name in known for name in names):
        return "explicitly_non_ios"
    return "unknown"
