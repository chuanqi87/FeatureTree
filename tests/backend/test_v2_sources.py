from pathlib import Path
from contextlib import closing
import sqlite3
import tempfile
import unittest

from featuretree.core.io import IntegrityError
from featuretree.corpus.identity import declaration_id
from featuretree.corpus.sdk import extract_sdk
from featuretree.corpus.extractors import android, native, syntax
from featuretree.workflow.source_tool import query
from tests.fixtures.v2 import PROJECT, schemas
from tests.fixtures.v2_pipeline import source_fixture


class SourceIntegrityTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(); self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.store, self.snapshot, self.catalog = source_fixture(self.root, schemas())

    def test_deleted_index_row_does_not_reduce_authoritative_coverage_denominator(self):
        path = self.catalog._index(self.snapshot['id'])
        with closing(sqlite3.connect(path)) as db:
            db.execute("DELETE FROM records WHERE kind='declarations' AND platform='ios'")
            db.commit()
        ids = self.catalog.enumerate_ids(self.snapshot['id'], {})
        self.assertEqual(3, len(ids))
        from featuretree.workflow.tree_handlers import TreeHandlers
        packet = {'work': {'snapshot_id': self.snapshot['id'], 'api_ids': ids}}
        with self.assertRaises(ValueError): TreeHandlers(None, self.catalog).input_records(packet)

    def test_tampered_body_and_cross_platform_read_are_rejected(self):
        packet = {'source_access': {'snapshot_id': self.snapshot['id'], 'platform': 'android', 'api_ids': ['api_android'], 'topic_ids': []}}
        with self.assertRaises(ValueError): query(self.catalog, packet, {'operation': 'body', 'id': 'doc_ios'})
        with self.assertRaises(ValueError): query(self.catalog, packet, {'operation': 'apis', 'id': 'api_ios'})
        (self.root / 'docs-raw/official/android.md').write_text('changed')
        with self.assertRaises(IntegrityError): query(self.catalog, packet, {'operation': 'body', 'id': 'doc_android'})

    def test_missing_body_is_data_gap_and_invalid_filters_fail(self):
        document = self.catalog.get(self.snapshot['id'], 'documents', 'doc_android')
        document.update(body_path=None, body_sha256=None, status='unprocessed')
        snapshot = self.store.seal({'documents': [document]}, files=[])
        packet = {'source_access': {'snapshot_id': snapshot['id'], 'platform': 'android', 'api_ids': [], 'topic_ids': []}}
        self.assertEqual('needs_sources', query(self.catalog, packet, {'operation': 'body', 'id': 'doc_android'})['status'])
        with self.assertRaises(ValueError): self.catalog.enumerate_ids(snapshot['id'], {'unknown': []})

    def test_api_identity_preserves_overloads_languages_and_literal_whitespace(self):
        identity = lambda language, signature: declaration_id('ios', 'Apple SDK', language, 'Module.Type.call', signature)
        self.assertNotEqual(identity('swift', '(label: "a b")'), identity('swift', '(label: "a  b")'))
        self.assertNotEqual(identity('swift', '(x: Int)'), identity('swift', '(x: String)'))
        self.assertNotEqual(identity('swift', '()'), identity('objc', '()'))

    def test_bounded_body_search_returns_verifiable_offsets(self):
        result = self.catalog.find_body(self.snapshot['id'], 'doc_android', 'official')
        text = (self.root / 'docs-raw/official/android.md').read_text()
        for window in result['windows']:
            self.assertEqual(window['text'], text[window['offset']:window['offset'] + len(window['text'])])


class SdkExtractionTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(); self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)

    def test_android_overloads_removed_and_inheritance_are_retained(self):
        path = self.root / 'api-versions.xml'
        path.write_text('<api><class name="android/example/Child" since="1"><extends name="android/example/Parent"/><method name="run(I)V"/><method name="run(Ljava/lang/String;)V"/><field name="OLD" removed="3"/></class></api>')
        rows, errors = android.extract(path, {})
        self.assertFalse(errors); self.assertEqual(4, len(rows))
        self.assertEqual('nonpublic', rows[-1]['visibility'])
        self.assertEqual(['android/example/Parent'], rows[1]['availability']['inherited_types'])

    def test_native_public_property_and_parse_failure(self):
        path = self.root / 'api.h'; path.write_text('struct Item { int value; }; int read_item(struct Item *item);')
        rows, errors = native.extract(path, {'sdk_root': self.root, 'module': 'Example', 'language': 'c'})
        self.assertFalse(errors); self.assertIn('Example.Item.value', {row['qualified_name'] for row in rows})
        path.write_text('#include "missing_required_header.h"\nint still_visible(void);')
        rows, errors = native.extract(path, {'sdk_root': self.root, 'module': 'Example', 'language': 'c'})
        self.assertTrue(errors); self.assertTrue(all(row['visibility'] != 'public' for row in rows))

    def test_clang_flag_enum_attributes_are_not_mistaken_for_declarations(self):
        path = self.root / 'flags.h'
        path.write_text('enum __attribute__((flag_enum)) Flags { One = 1, Two = 2 };')
        rows, errors = native.extract(path, {'sdk_root': self.root, 'module': 'Example', 'language': 'c'})
        self.assertFalse(errors)
        self.assertIn('Example.Flags', {row['qualified_name'] for row in rows})

    def test_arkts_system_api_inherited_and_literal_signature_retained(self):
        path = self.root / 'api.d.ts'; path.write_text('/** @systemapi */\nexport interface Secret { run(): void; }\nexport interface Public { readonly value: "a  b"; }')
        rows, errors = syntax.arkts(path, {'project_root': PROJECT, 'module': 'Example'})
        self.assertFalse(errors)
        secret = next(row for row in rows if row['qualified_name'].endswith('Secret.run'))
        self.assertEqual('nonpublic', secret['visibility'])
        self.assertIn('"a  b"', next(row for row in rows if row['qualified_name'].endswith('Public.value'))['signature'])

    def test_swift_public_private_and_inherited_availability(self):
        path = self.root / 'Example.swiftinterface'
        path.write_text('@available(iOS 18.0, *)\npublic struct Item { public var value: Int; private func hidden() {} }\npublic func call(_ value: Int) {}\npublic func call(_ value: String) {}')
        rows, errors = syntax.swift(path, {'project_root': PROJECT, 'module': 'Example'})
        self.assertFalse(errors)
        self.assertEqual(2, len([row for row in rows if row['qualified_name'] == 'Example.call']))
        hidden = next(row for row in rows if row['qualified_name'] == 'Example.Item.hidden')
        self.assertEqual('nonpublic', hidden['visibility'])
        value = next(row for row in rows if row['qualified_name'] == 'Example.Item.value')
        self.assertEqual('public', value['visibility']); self.assertIn('@available(iOS 18.0, *)', value['availability']['available'])

    def test_sdk_source_bytes_are_retained_and_failures_not_hidden(self):
        from featuretree.corpus.snapshots import SnapshotStore
        path = self.root / 'broken.xml'; path.write_text('<api><class')
        store = SnapshotStore(self.root / 'data/sources', schemas())
        result = extract_sdk(self.root, {'adapter': 'android-xml', 'sdk_root': str(self.root), 'patterns': ['*.xml'],
            'platform': 'android', 'distribution': 'Android SDK', 'language': 'java', 'module': 'android', 'sdk_version': 'test'}, store)
        self.assertEqual('failed', result['files'][0]['status'])
        self.assertTrue(result['gaps'])
        retained = list((self.root / 'data/imports/sdk').glob('*/broken.xml'))
        self.assertEqual(path.read_bytes(), retained[0].read_bytes())
        retained[0].write_text('changed retained input')
        with self.assertRaises(ValueError): store.verify(result['id'])

class ObservationImportTests(unittest.TestCase):
    def test_device_material_is_retained_and_tampering_is_rejected(self):
        from featuretree.workflow.observations import ObservationService
        from featuretree.knowledge.observations import validate_observation
        from tests.fixtures.v2 import stores
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); artifacts, _ = stores(root)
            path = root / 'device.log'; path.write_text('Synthetic test material; not a real device observation')
            request = {'claim_id': 'claim_test', 'claim_hash': 'a'*64, 'baseline_ref': 'b'*64,
                'platform': 'android', 'actor': 'fixture-human', 'executed_at': '2026-09-10T00:00:00Z',
                'environment': {'device': 'synthetic fixture', 'system_build': 'fixture', 'app_build': 'fixture'},
                'test_case': {'goal': 'Fixture validation', 'steps': ['Read fixture'], 'conditions': ['Test only'], 'expected_result': 'Fixture retained'},
                'observed_result': 'Fixture retained', 'material_paths': [str(path)]}
            receipt = ObservationService(artifacts, schemas()).import_record(request)
            observation = artifacts.get(receipt['observation_ref'])
            path.write_text('Original may change; retained material must not')
            validate_observation(observation, artifacts)
            observation['materials'][0]['sha256'] = 'f'*64
            with self.assertRaises(ValueError): validate_observation(observation, artifacts)
