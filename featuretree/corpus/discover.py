"""Discover document URLs from saved official catalog responses and prior evidence."""

import json
from pathlib import Path
import xml.etree.ElementTree as ET

from featuretree.corpus.urls import canonical


def walk(nodes):
    for node in nodes:
        yield node
        yield from walk(node.get('children', []))


def seed_android(corpus, directory):
    accepted = excluded = 0
    for path in sorted(Path(directory).glob('sitemap_*xml')):
        for _, elem in ET.iterparse(path, events=('end',)):
            if elem.tag.endswith('}url'):
                location = elem.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
                if location is not None and location.text:
                    url = canonical(location.text)
                    if url:
                        priority = 90 if '/sdk/api_diff/' in url else 65 if '/reference/' in url else 20
                        corpus.add(url, priority=priority, source=str(path)); accepted += 1
                    else:
                        excluded += 1
                elem.clear()
    corpus.db.commit()
    return {'accepted_entries':accepted,'excluded_entries':excluded}


def seed_huawei(corpus, directory):
    for family, filename in [('harmonyos-guides','harmonyos-guide-catalog.json'),
                             ('harmonyos-references','harmonyos-api-catalog.json')]:
        path = Path(directory)/filename
        data = json.loads(path.read_text())
        if data.get('code') != 0:
            raise ValueError(f'Catalog was not successful: {path}')
        for node in walk(data['value']['catalogTreeList']):
            slug = node.get('relateDocument')
            if slug:
                url = slug if slug.startswith('https://') else f'https://developer.huawei.com/consumer/cn/doc/{family}/{slug}'
                corpus.add(url,node.get('nodeName',''),20 if 'guides' in family else 30,source=str(path))
    corpus.db.commit()


def seed_apple(corpus, path):
    data = json.loads(Path(path).read_text())
    for reference in data.get('references',{}).values():
        if reference.get('type') == 'topic' and reference.get('url'):
            corpus.add(reference['url'] if reference['url'].startswith('https://') else
                       'https://developer.apple.com'+reference['url'],reference.get('title',''),20,source=str(path))
    corpus.add('https://developer.apple.com/documentation/technologies',priority=5)
    corpus.add('https://developer.apple.com/documentation/technologyoverviews',priority=5)
    corpus.db.commit()


def seed_previous(corpus, previous_root):
    previous_root = Path(previous_root)
    for name in ('android','apple','harmonyos'):
        taxonomy = previous_root/f'ontology/official/{name}.json'
        if taxonomy.exists():
            for node in walk(json.loads(taxonomy.read_text())['roots']):
                url = node.get('url')
                if url:
                    corpus.add(url,node.get('name',''),25,source=str(taxonomy))
        profiles = previous_root/f'ontology/official/evidence/{name}.jsonl'
        if profiles.exists():
            with profiles.open() as stream:
                for line in stream:
                    row = json.loads(line)
                    for guide in row.get('evidence',{}).get('guide_documents',[]):
                        corpus.add(guide['source_url'],guide.get('title',''),15,source=str(profiles))
    corpus.db.commit()


def seed_features(corpus, repo):
    for f in repo.features().values():
        for bindings in f.get('bindings',{}).values():
            for binding in bindings:
                if binding.get('url'):
                    corpus.add(binding['url'],priority=0,source=f['id'])
    knowledge,_ = repo.knowledge()
    for doc in knowledge.values():
        for evidence in doc.get('evidence',[]):
            corpus.add(evidence.get('url',''),priority=0,source=doc['feature_id'])
    corpus.db.commit()
