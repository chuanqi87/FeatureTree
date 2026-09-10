"""Normalize official document identities without losing version parameters."""

import hashlib
import re
from urllib.parse import parse_qsl, quote, unquote, urlencode, urljoin, urlsplit, urlunsplit


ANDROID_PREFIXES = ('/reference', '/develop', '/guide', '/training', '/topic', '/jetpack',
                    '/ndk', '/about', '/privacy', '/identity', '/health', '/games', '/design',
                    '/quality', '/distribute', '/google', '/build', '/studio', '/get-started',
                    '/media','/ai','/kotlin','/tools','/work','/agi','/docs','/security','/sdk/api_diff',
                    '/social-and-messaging','/large-screens','/tv','/wear','/chrome-os','/compose',
                    '/assistant','/multidevice','/xr','/adaptive-apps','/quick-guides','/cars',
                    '/health-and-fitness','/build-for-billions','/privacy-and-security',
                    '/developer-verification','/design-for-safety','/guides','/google-play',
                    '/health-ai-developer-foundations','/quality-guidelines','/googlebook',
                    '/compose-camp','/multidevice-development','/ai-in-android','/health-connect',
                    '/security-and-privacy','/blog')
VERSION_PARAMS = {'language', 'version', 'versionId', 'topicVersion', 'apiLevel'}


def canonical(url, base=''):
    try:
        parsed = urlsplit(urljoin(base, url))
        port = parsed.port
    except (ValueError,TypeError):
        return None
    if parsed.scheme not in ('https', 'http') or parsed.username or parsed.password:
        return None
    host = (parsed.hostname or '').lower()
    if port not in (None, 443, 80):
        return None
    path = parsed.path.rstrip('/') or '/'
    if host == 'developer.apple.com':
        path = path.lower()
        if path.startswith('/tutorials/data/documentation/') and path.endswith('.json'):
            path = path.removeprefix('/tutorials/data').removesuffix('.json')
        if path.endswith('.md'):
            path = path[:-3]
        if not path.startswith('/documentation/') and path not in ('/news', '/news/releases'):
            return None
    elif host == 'developer.android.com':
        if not any(path == prefix or path.startswith(prefix + '/') for prefix in ANDROID_PREFIXES):
            return None
    elif host == 'developer.huawei.com':
        if not path.lower().startswith('/consumer/cn/doc/'):
            return None
        path = path.removesuffix('.md')
    elif host == 'developers.google.com':
        if not path.startswith(('/android/', '/identity/', '/maps/documentation/', '/ml-kit/')):
            return None
    elif host == 'firebase.google.com':
        if not path.startswith('/docs/'):
            return None
    else:
        return None
    if path.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif', '.svg', '.zip', '.pdf',
                             '.xml', '.mp4', '.aep', '.psd', '.fig', '.mp3', '.woff', '.ttf')):
        return None
    params = dict(parse_qsl(parsed.query))
    if params.get('hl', 'en') not in ('en', 'en-US'):
        return None
    query = urlencode(sorted((k, v) for k, v in params.items() if k in VERSION_PARAMS or (path == '/news' and k == 'id')))
    path = quote(unquote(path), safe="/():@,$!+'=-._~")
    return urlunsplit(('https', host, path, query, ''))


def platform(url):
    host = urlsplit(url).hostname
    if host in ('developers.google.com', 'firebase.google.com') and re.search(r'/ios(?:-[^/]+)?(?:/|$)', urlsplit(url).path, re.I):
        return 'ios'
    return 'ios' if host == 'developer.apple.com' else 'harmonyos' if host == 'developer.huawei.com' else 'android'


def document_id(url):
    return hashlib.sha256(url.encode()).hexdigest()


def fetch_url(url):
    parsed = urlsplit(url)
    if parsed.hostname == 'developer.huawei.com' or (parsed.hostname == 'developer.apple.com' and parsed.path.startswith('/documentation/')):
        return urlunsplit(parsed._replace(path=parsed.path + '.md'))
    return url


def kind(url):
    path = urlsplit(url).path
    if '/reference' in path or '/harmonyos-references/' in path:
        return 'api'
    return 'guide'
