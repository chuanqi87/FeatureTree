"""Command-line interface for the official document corpus."""

import argparse
import json
from pathlib import Path

from featuretree.core.paths import CONTEXTS_DIR, REPORTS_DIR
from featuretree.core.storage import ROOT, Repository
from featuretree.corpus.store import Corpus


def emit(value):
    print(json.dumps(value,ensure_ascii=False),flush=True)


def parser():
    result = argparse.ArgumentParser(description='Download and search official source evidence without generating claims.')
    result.add_argument('--corpus',type=Path,default=ROOT/'docs-raw/official')
    commands = result.add_subparsers(dest='command',required=True)
    catalogs = commands.add_parser('catalogs')
    catalogs.add_argument('--refresh',action='store_true')
    seed = commands.add_parser('seed')
    seed.add_argument('--previous',type=Path)
    cache = commands.add_parser('import-cache')
    cache.add_argument('--previous',type=Path,required=True)
    crawl = commands.add_parser('crawl')
    crawl.add_argument('--platform',action='append',choices=['android','ios','harmonyos'])
    crawl.add_argument('--workers',type=int,default=6)
    crawl.add_argument('--limit',type=int,default=0)
    crawl.add_argument('--max-priority',type=int,default=100)
    crawl.add_argument('--retry',action='store_true')
    crawl.add_argument('--no-follow',action='store_true')
    commands.add_parser('status')
    audit=commands.add_parser('audit')
    audit.add_argument('--verify-files',action='store_true')
    audit.add_argument('--output',type=Path,default=ROOT/REPORTS_DIR/'official-documents')
    search = commands.add_parser('search')
    search.add_argument('query')
    search.add_argument('--platform',choices=['android','ios','harmonyos'],required=True)
    search.add_argument('--limit',type=int,default=8)
    locate = commands.add_parser('locate')
    locate.add_argument('query')
    locate.add_argument('--platform',choices=['android','ios','harmonyos'],required=True)
    locate.add_argument('--limit',type=int,default=12)
    fetch = commands.add_parser('fetch')
    fetch.add_argument('url')
    fetch.add_argument('--refresh',action='store_true')
    read = commands.add_parser('read')
    read.add_argument('url')
    read.add_argument('--start-line',type=int,default=1)
    read.add_argument('--lines',type=int,default=100)
    context = commands.add_parser('context')
    context.add_argument('feature_id',nargs='?')
    context.add_argument('--all',action='store_true')
    context.add_argument('--output',type=Path,default=ROOT/CONTEXTS_DIR)
    context.add_argument('--limit',type=int,default=6)
    return result


def run(args, corpus):
    if args.command=='catalogs':
        from featuretree.corpus.catalogs import sync_catalogs
        report=sync_catalogs(corpus.root,args.refresh,emit)
        emit({'catalog_sources':len(report['sources']),'errors':report['errors']})
        if report['errors']:
            raise SystemExit(2)
    elif args.command=='seed':
        from featuretree.corpus.discover import seed_android, seed_apple, seed_features, seed_huawei, seed_previous
        probes = ROOT/'docs-raw/source-probes/2026-09-05'
        emit({'android':seed_android(corpus,corpus.root/'catalogs/android')})
        huawei=corpus.root/'catalogs/huawei'
        apple=corpus.root/'catalogs/apple/technologies.json'
        seed_huawei(corpus,huawei if huawei.exists() else probes)
        seed_apple(corpus,apple if apple.exists() else probes/'apple-technologies.json')
        if args.previous:
            seed_previous(corpus,args.previous)
        seed_features(corpus,Repository())
        emit(corpus.stats())
    elif args.command=='import-cache':
        from featuretree.corpus.import_cache import import_previous, import_probes
        emit({'probes':import_probes(corpus,ROOT)})
        emit({'previous':import_previous(corpus,args.previous,emit)})
    elif args.command=='crawl':
        from featuretree.corpus.download import crawl
        if not 1<=args.workers<=16 or args.limit<0:
            raise ValueError('workers must be 1..16 and limit must be nonnegative')
        emit(crawl(corpus,args.platform or ['android','ios','harmonyos'],args.workers,args.limit,
                   args.max_priority,args.retry,not args.no_follow,emit))
    elif args.command=='status':
        emit(corpus.stats())
    elif args.command=='audit':
        from featuretree.corpus.audit import audit
        report=audit(corpus,args.output,args.verify_files)
        emit(report)
        if report['integrity_errors']:
            raise SystemExit(2)
    elif args.command=='search':
        from featuretree.corpus.search import search
        emit(search(corpus,args.query,args.platform,args.limit))
    elif args.command=='locate':
        from featuretree.corpus.search import locate
        emit(locate(corpus,args.query,args.platform,args.limit))
    elif args.command=='fetch':
        from featuretree.corpus.download import Fetcher
        if not corpus.add(args.url,priority=0,source='explicit fetch'):
            raise ValueError('URL is outside the official document allowlist')
        row = corpus.get(args.url)
        if row['status'] not in ('ready','thin') or args.refresh:
            result = Fetcher().fetch(row)
            if 'error' in result:
                corpus.fail(row,result['error'],result['http_status']);corpus.db.commit()
                raise ValueError(result['error'])
            corpus.save(row,**result);corpus.db.commit()
        emit(corpus.get(args.url))
    elif args.command=='read':
        row = corpus.get(args.url)
        if not row or row['status'] not in ('ready','thin','partial'):
            raise ValueError('No readable local document; use fetch with the official URL')
        if args.start_line<1 or args.lines<1:
            raise ValueError('Line bounds must be positive')
        lines=corpus.body(row).splitlines();start=args.start_line-1
        emit({'source':row,'total_lines':len(lines),'lines':[
            {'line':i+1,'text':lines[i]} for i in range(start,min(len(lines),start+args.lines))]})
    elif args.command=='context':
        from featuretree.corpus.context import build_contexts
        if bool(args.feature_id) == args.all:
            raise ValueError('Specify exactly one of feature_id or --all')
        emit(build_contexts(corpus,Repository(),args.output,None if args.all else [args.feature_id],args.limit))


def main(argv=None):
    args=parser().parse_args(argv)
    corpus=Corpus(args.corpus)
    try:
        run(args,corpus)
    finally:
        corpus.close()
