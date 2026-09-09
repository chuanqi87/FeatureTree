"""Bounded concurrent downloads with redirects checked and host-wide throttling."""

from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
import fcntl
import threading
import time
from urllib.parse import urlsplit

import requests
from lxml import etree

from featuretree.corpus.extract import parse
from featuretree.corpus.http import request_proxies
from featuretree.corpus.urls import canonical, fetch_url, platform


def link_priority(url, source_platform):
    if '/sdk/api_diff/' in url:
        return 90
    if source_platform == 'ios':
        parts = urlsplit(url).path.strip('/').split('/')
        return 40 if len(parts) == 2 or (len(parts) == 3 and '-' in parts[-1]) else 65
    return 70 if '/reference/' in url else 40


class Fetcher:
    def __init__(self, interval=0.2):
        self.local = threading.local()
        self.lock = threading.Lock()
        self.next_request = {}
        self.interval = interval

    def throttle(self, host):
        with self.lock:
            start = max(time.monotonic(),self.next_request.get(host,0))
            self.next_request[host] = start+self.interval
        time.sleep(max(0,start-time.monotonic()))

    def fetch(self, row):
        if not hasattr(self.local,'session'):
            self.local.session = requests.Session()
            self.local.session.headers['User-Agent'] = 'FeatureTree-official-document-mirror/1.0'
        url = fetch_url(row['url'])
        tried_json = False
        try:
            for _ in range(5):
                self.throttle(urlsplit(url).hostname)
                response = self.local.session.get(url,timeout=(10,35),allow_redirects=False,proxies=request_proxies(url))
                if response.is_redirect:
                    from urllib.parse import urljoin
                    next_url = urljoin(url,response.headers['Location'])
                    target = canonical(next_url)
                    if not target or platform(target)!=row['platform']:
                        raise ValueError('Redirect outside approved official documentation')
                    url = next_url
                    continue
                if response.status_code == 429:
                    retry = response.headers.get('Retry-After','60')
                    seconds = max(30,float(retry)) if retry.isdigit() else 60
                    with self.lock:
                        host = urlsplit(url).hostname
                        self.next_request[host] = max(self.next_request.get(host,0),time.monotonic()+seconds)
                if response.status_code==404 and urlsplit(row['url']).hostname=='developer.apple.com' and not tried_json:
                    url='https://developer.apple.com/tutorials/data'+urlsplit(row['url']).path+'.json'
                    tried_json=True
                    continue
                response.raise_for_status()
                raw = response.content
                content = parse(raw,row['url'],response.headers.get('Content-Type',''))
                return {'raw':raw,'content':content,'fetch_url':url}
            raise ValueError('Too many redirects')
        except (requests.RequestException,ValueError,UnicodeError,etree.LxmlError) as error:
            status = error.response.status_code if isinstance(error,requests.HTTPError) and error.response is not None else None
            return {'error':str(error),'http_status':status}


def crawl(corpus, platforms, workers=6, limit=0, max_priority=100, retry=False,
          follow_links=True, progress=print):
    lock_path = corpus.root/'download.lock'
    with lock_path.open('w') as process_lock:
        fcntl.flock(process_lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        return _crawl(corpus,platforms,workers,limit,max_priority,retry,follow_links,progress)


def _crawl(corpus, platforms, workers, limit, max_priority, retry, follow_links, progress):
    fetcher = Fetcher()
    completed = 0
    last_report = time.monotonic()
    while not limit or completed < limit:
        rows = corpus.pending(platforms,min(1000,limit-completed) if limit else 1000,max_priority,retry)
        if not rows:
            break
        iterator = iter(rows)
        with ThreadPoolExecutor(max_workers=workers) as pool:
            active = {}
            for row in iterator:
                active[pool.submit(fetcher.fetch,row)] = row
                if len(active)>=workers*2:
                    break
            while active:
                done,_ = wait(active,timeout=2,return_when=FIRST_COMPLETED)
                for future in done:
                    row = active.pop(future)
                    result = future.result()
                    if 'error' in result:
                        corpus.fail(row,result['error'],result['http_status'])
                    else:
                        corpus.save(row,**result)
                        if follow_links:
                            for link in result['content'].links:
                                # API members remain part of discovery; priority permits staged downloads.
                                corpus.add(link,priority=link_priority(link,row['platform']),
                                           depth=row['depth']+1,source=row['url'])
                    completed += 1
                    next_row = next(iterator,None)
                    if next_row:
                        active[pool.submit(fetcher.fetch,next_row)] = next_row
                if completed%25==0 or time.monotonic()-last_report>10:
                    corpus.db.commit()
                    progress({'completed_this_run':completed,'stats':corpus.stats()})
                    last_report = time.monotonic()
        corpus.db.commit()
    return {'completed_this_run':completed,'stats':corpus.stats()}
