"""Download official URL catalogs independently of document-body acquisition."""

from concurrent.futures import ThreadPoolExecutor
import hashlib
import gzip
import json
from pathlib import Path
import time
import xml.etree.ElementTree as ET

import requests

from .store import now
from .http import request_proxies


HUAWEI_CATALOG = 'https://svc-drcn.developer.huawei.com/community/servlet/consumer/cn/documentPortal/getCatalogTree'


def archive_response(path, raw, metadata=None):
    """Keep catalog history before replacing the current discovery snapshot."""
    archive=path.parent/'history'/hashlib.sha256(raw).hexdigest()/(path.name+'.gz')
    archive.parent.mkdir(parents=True,exist_ok=True)
    if not archive.exists():
        archive.write_bytes(gzip.compress(raw,mtime=0))
    if metadata:
        record=archive.with_suffix('.meta.json')
        if not record.exists():
            record.write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n')
    return archive


def retrieve(url, path, payload=None, refresh=False):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    metadata_path=path.with_suffix(path.suffix+'.meta.json')
    if not refresh and path.exists() and metadata_path.exists():
        meta=json.loads(metadata_path.read_text())
        if hashlib.sha256(path.read_bytes()).hexdigest()==meta['sha256']:
            archive_response(path,path.read_bytes(),meta)
            return meta
    for attempt in range(3):
        try:
            kwargs={'json':payload} if payload is not None else {}
            response=requests.request('POST' if payload is not None else 'GET',url,timeout=(10,90),proxies=request_proxies(url),
                headers={'User-Agent':'FeatureTree-official-document-mirror/1.0',
                         'Origin':'https://developer.huawei.com','Referer':'https://developer.huawei.com/consumer/cn/doc/'},**kwargs)
            response.raise_for_status();raw=response.content
            if path.suffix=='.xml':
                ET.fromstring(raw)
            elif path.suffix=='.json':
                data=json.loads(raw)
                if payload is not None and data.get('code')!=0:
                    raise ValueError('Huawei catalog business response was unsuccessful')
            if path.exists():
                old_meta=json.loads(metadata_path.read_text()) if metadata_path.exists() else None
                archive_response(path,path.read_bytes(),old_meta)
            archive=archive_response(path,raw)
            meta={'url':url,'request_body':payload,'retrieved_at':now(),'sha256':hashlib.sha256(raw).hexdigest(),
                  'bytes':len(raw),'path':str(path),'archive_path':str(archive),'status':response.status_code}
            archive_response(path,raw,meta)
            path.write_bytes(raw)
            metadata_path.write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
            return meta
        except (requests.RequestException,ValueError,ET.ParseError) as error:
            if attempt==2:
                return {'url':url,'error':str(error),'checked_at':now()}
            time.sleep(2**attempt)


def sync_catalogs(root, refresh=False, progress=print):
    root=Path(root)/'catalogs'
    jobs=[('https://developer.android.com/sitemap.xml',root/'android/sitemap.xml',None),
          ('https://developer.apple.com/tutorials/data/documentation/technologies.json',root/'apple/technologies.json',None)]
    for family,filename in [('harmonyos-guides','harmonyos-guide-catalog.json'),
                            ('harmonyos-references','harmonyos-api-catalog.json')]:
        jobs.append((HUAWEI_CATALOG,root/'huawei'/filename,{'language':'cn','catalogName':family,'showHide':1}))
    results=[]
    for url,path,payload in jobs:
        result=retrieve(url,path,payload,refresh);results.append(result);progress(result)
    sitemap=root/'android/sitemap.xml'
    if sitemap.exists():
        ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls=[e.text for e in ET.parse(sitemap).findall('s:sitemap/s:loc',ns)]
        def download(url):
            result=retrieve(url,root/'android'/url.rsplit('/',1)[-1],refresh=refresh)
            progress(result);return result
        with ThreadPoolExecutor(max_workers=3) as pool:
            results.extend(pool.map(download,urls))
    report={'retrieved_at':now(),'sources':results,'errors':[r for r in results if 'error' in r]}
    (root/'manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    return report
