"""Evidence integrity, parser boundaries and retrieval behavior of the source corpus."""

import gzip
import hashlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from featuretree.corpus.catalogs import archive_response
from featuretree.corpus.extract import Content, markdown_links, parse
from featuretree.corpus.import_cache import import_response
from featuretree.corpus.search import locate, search
from featuretree.corpus.store import Corpus
from featuretree.corpus.urls import canonical, fetch_url




class OfficialURLTests(unittest.TestCase):
    def test_tracking_removed_but_version_retained(self):
        url='https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/example?ha_source=x&topicVersion=6.0#section'
        self.assertEqual(canonical(url),'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/example?topicVersion=6.0')
        self.assertEqual(fetch_url(canonical(url)),'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/example.md?topicVersion=6.0')

    def test_disallowed_hosts_local_files_and_locales(self):
        for url in ('file:///etc/passwd','https://developer.apple.com.attacker.test/documentation/foo',
                    'https://developer.apple.com:8443/documentation/foo',
                    'https://developer.android.com/reference/android/app/Activity?hl=fr'):
            self.assertIsNone(canonical(url))
        self.assertIsNone(canonical('https://media:201787890276720037'))
        self.assertIsNone(canonical('https://developer.android.com/googlecac5c7e67791100b'))
        self.assertIsNone(canonical('https://developer.android.com/design/example.aep'))
        for root in ('health-and-fitness','privacy-and-security','developer-verification'):
            url='https://developer.android.com/'+root+'/guides'
            self.assertEqual(canonical(url),url)

    def test_apple_methods_with_balanced_parentheses(self):
        text='See [scan](/documentation/CoreBluetooth/CBCentralManager/scanForPeripherals(withServices:options:)).'
        self.assertEqual(markdown_links(text,'https://developer.apple.com/documentation/corebluetooth'),
            ['https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/scanforperipherals(withservices:options:)'])


class ExtractionTests(unittest.TestCase):
    def test_html_navigation_removed_and_table_code_retained(self):
        raw=b'''<html><nav>UNRELATED NAVIGATION</nav><h1>Scan devices</h1>
        <div class="devsite-article-body"><h2 id="permission">Permissions</h2>
        <p>Requires Bluetooth permission and the applicable platform version.</p>
        <pre>startScan(filters, callback)</pre><table><tr><th>API</th><th>Since</th></tr>
        <tr><td>scan</td><td>21</td></tr></table><a href="/reference/android/bluetooth/le/ScanFilter">Filter</a></div></html>'''
        doc=parse(raw,'https://developer.android.com/develop/bluetooth','text/html')
        self.assertNotIn('UNRELATED',doc.body)
        self.assertIn('startScan(filters, callback)',doc.body)
        self.assertIn('| API | Since |',doc.body)
        self.assertIn('permission',doc.metadata['anchors'])
        self.assertEqual(doc.quality,'ready')

    def test_shell_cannot_be_evidence(self):
        for raw,ctype in [(b'<html><h1>Sign in</h1></html>','text/html'),
                          (b'<html>JavaScript application shell</html>','text/markdown'),
                          (b'# Page Not Found','text/markdown')]:
            with self.assertRaises(ValueError):
                parse(raw,'https://developer.apple.com/documentation/foo',ctype)

    def test_apple_availability_is_preserved_without_asserting_ios(self):
        raw=b'<!-- {"availability":["macOS: 15.0 -"],"documentType":"symbol"} -->\n# Feature\n\n'+b'Document content. '*20
        doc=parse(raw,'https://developer.apple.com/documentation/foo','text/markdown')
        self.assertEqual(doc.metadata['availability'],['macOS: 15.0 -'])

    def test_thin_pages_remain_distinguishable(self):
        doc=parse('# 目录\n\n[链接](next)'.encode(),'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/test','text/markdown')
        self.assertEqual(doc.quality,'thin')

    def test_plain_text_diagnostics_preserved_but_empty_response_rejected(self):
        url='https://developer.android.com/topic/performance/memory/guide/meminfo_sample.txt'
        raw=b'   PID    Native heap\n  1234   8192 KiB\n'
        doc=parse(raw,url,'text/plain')
        self.assertIn(raw.decode().strip(),doc.body)
        self.assertEqual(doc.metadata['source_format'],'plain-text')
        with self.assertRaises(ValueError):
            parse(b'',url,None)

    def test_docc_directory_retains_references(self):
        data={'metadata':{'title':'Technologies'},'sections':[{'kind':'technologies','groups':[
            {'name':'Frameworks','technologies':[{'destination':{'type':'reference','identifier':'doc://ble'}}]}]}],
            'references':{'doc://ble':{'type':'topic','title':'Core Bluetooth','url':'/documentation/corebluetooth'}}}
        doc=parse(json.dumps(data).encode(),'https://developer.apple.com/documentation/technologies','application/json')
        self.assertIn('Core Bluetooth',doc.body)
        self.assertIn('/documentation/corebluetooth',doc.body)
        self.assertEqual(doc.metadata['unhandled_render_types'],[])

    def test_legacy_api_diff_navigation_is_not_a_body_claim(self):
        raw=b'<html><head><title>API 35 to 36</title><meta name="generator" content="JDiff v1.1.0"></head><frameset><frame src="/sdk/api_diff/36/changes/changes-summary"></frameset></html>'
        doc=parse(raw,'https://developer.android.com/sdk/api_diff/36/changes','text/html')
        self.assertEqual(doc.quality,'thin')
        self.assertIn('https://developer.android.com/sdk/api_diff/36/changes/changes-summary',doc.links)
        raw=b'<html><head><title>Math</title><meta name="generator" content="JDiff v1.1.0"></head><body><h2>Added Methods</h2><table><tr><td>ceilDiv</td><td>Since 35</td></tr></table></body></html>'
        doc=parse(raw,'https://developer.android.com/sdk/api_diff/35/changes/java.lang.Math','text/html')
        self.assertIn('ceilDiv',doc.body)
        self.assertIn('Since 35',doc.body)

    def test_docc_fallback_preserves_parameter_and_code_context(self):
        data={'metadata':{'title':'scan','platforms':[{'name':'iOS','introducedAt':'5.0'}]},
              'primaryContentSections':[{'kind':'parameters','parameters':[{'name':'filters','content':[
                  {'type':'paragraph','inlineContent':[{'type':'text','text':'Select advertised services.'}]}]}]},
                  {'kind':'content','content':[{'type':'codeListing','syntax':'swift','code':['manager.scan()']}]}]}
        doc=parse(json.dumps(data).encode(),'https://developer.apple.com/documentation/corebluetooth/scan','application/json')
        self.assertIn('filters',doc.body)
        self.assertIn('Select advertised services.',doc.body)
        self.assertIn('manager.scan()',doc.body)
        self.assertEqual(doc.metadata['availability'][0]['name'],'iOS')


class CorpusTests(unittest.TestCase):
    def setUp(self):
        self.temp=TemporaryDirectory();self.corpus=Corpus(self.temp.name)

    def tearDown(self):
        self.corpus.close();self.temp.cleanup()

    def save(self,url,title,body):
        self.corpus.add(url)
        self.corpus.save(self.corpus.get(url),body.encode(),Content(title,body),fetch_url(url))
        self.corpus.db.commit()
        return self.corpus.get(url)

    def test_original_and_normalized_snapshot_integrity(self):
        url='https://developer.android.com/develop/bluetooth'
        old=self.save(url,'Bluetooth','# Bluetooth\nOld official behavior.')
        new=self.save(url,'Bluetooth','# Bluetooth\nUpdated official behavior.')
        self.assertNotEqual(old['raw_path'],new['raw_path'])
        raw=gzip.decompress((self.corpus.root/old['raw_path']).read_bytes())
        self.assertEqual(hashlib.sha256(raw).hexdigest(),old['raw_sha256'])
        self.assertIn('Old official',self.corpus.body(old))
        (self.corpus.root/new['body_path']).write_text('tampered')
        with self.assertRaisesRegex(ValueError,'hash mismatch'):
            self.corpus.body(new)

    def test_refresh_does_not_duplicate_search_results(self):
        url='https://developer.apple.com/documentation/corebluetooth'
        for i in range(2):
            self.save(url,'Bluetooth',f'# Bluetooth\nScanning peripherals revision {i}.')
        self.assertEqual(len(search(self.corpus,'Bluetooth','ios')),1)

    def test_captured_sources_remain_readable_when_discovery_rules_change(self):
        url='https://developer.android.com/develop/bluetooth'
        self.save(url,'Bluetooth','# Bluetooth\nOfficial source snapshot.')
        with patch('featuretree.corpus.store.canonical',return_value=None):
            row=self.corpus.get(url)
            self.assertIn('Official source snapshot',self.corpus.body(row))

    def test_failed_refresh_preserves_previous_readable_snapshot(self):
        url='https://developer.apple.com/documentation/corebluetooth'
        row=self.save(url,'Bluetooth','# Bluetooth\nExisting official response.')
        self.corpus.fail(row,'503 on refresh',503)
        updated=self.corpus.get(url)
        self.assertEqual(updated['status'],'ready')
        self.assertEqual(updated['raw_sha256'],row['raw_sha256'])
        self.assertIn('Existing official',self.corpus.body(updated))

    def test_cache_hash_mismatch_rejected(self):
        p=Path(self.temp.name)/'source.md';p.write_text('# Fake\nMade up content')
        result=import_response(self.corpus,'https://developer.apple.com/documentation/foo',p,'0'*64,
                               '2026-09-01T00:00:00Z','text/markdown')
        self.assertEqual(result,'hash_mismatch')
        self.assertIsNone(self.corpus.get('https://developer.apple.com/documentation/foo'))

    def test_search_platform_filter_and_chinese(self):
        self.save('https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ble','蓝牙扫描','# 蓝牙扫描\n蓝牙扫描需要运行时权限。')
        self.save('https://developer.apple.com/documentation/corebluetooth','Bluetooth','# Bluetooth\nScan devices.')
        results=search(self.corpus,'蓝牙扫描','harmonyos')
        self.assertEqual(len(results),1)
        self.assertEqual(results[0]['platform'],'harmonyos')
        self.assertFalse(results[0]['metadata']['version_verified'])
        self.assertEqual(search(self.corpus,'nonexistentsymbol','android'),[])



    def test_catalog_history_retains_original_response(self):
        path=Path(self.temp.name)/'catalog.json'
        old=archive_response(path,b'{"old":1}',{'retrieved_at':'2026-09-01'})
        new=archive_response(path,b'{"new":1}')
        self.assertNotEqual(old,new)
        self.assertEqual(gzip.decompress(old.read_bytes()),b'{"old":1}')
        self.assertEqual(json.loads(old.with_suffix('.meta.json').read_text())['retrieved_at'],'2026-09-01')


    def test_queue_interleaves_platforms_and_respects_priority(self):
        for url in ['https://developer.apple.com/documentation/a','https://developer.apple.com/documentation/b',
                    'https://developer.android.com/develop/test']:
            self.corpus.add(url,priority=20)
        self.corpus.add('https://developer.android.com/reference/test',priority=65)
        queue=self.corpus.pending(['android','ios'],2,max_priority=40)
        self.assertEqual([r['platform'] for r in queue],['android','ios'])

    def test_catalog_search_finds_uncached_api_without_claiming_body_exists(self):
        self.corpus.add('https://developer.android.com/reference/android/bluetooth/le/ScanFilter')
        rows=locate(self.corpus,'ScanFilter','android')
        self.assertEqual(len(rows),1)
        self.assertEqual(rows[0]['status'],'pending')
        self.assertEqual(search(self.corpus,'ScanFilter','android'),[])


if __name__=='__main__':
    unittest.main()
