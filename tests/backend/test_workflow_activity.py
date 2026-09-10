"""Console projections include recovery activity without rewriting scheduler facts."""
from pathlib import Path
import tempfile
import unittest
from featuretree.core.io import write_json
from featuretree.reporting.workflow_activity import stage_activity, event_tail


class ActivityTests(unittest.TestCase):
    def test_recovery_process_overrides_stale_failed_display(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            task = {'id':'w--ft-ios', 'status':'failed','revision':0}
            parent = root/'attempts'/task['id']/'recovery-stage-0001'
            batch = parent/'batches/0001'
            write_json(parent/'batch-progress.json',{'status':'running','completed':1,'total':16})
            write_json(batch/'input.json',{'batch':{'index':1},'work':{'api_ids':['api_one'],'topic_ids':[]}})
            write_json(batch/'process.json',{'pid':123,'identity':'same'})
            (batch/'events.jsonl').write_text('{"type":"step_start","timestamp":123}\n')
            result = stage_activity(root,task,None,lambda pid:'same')
            self.assertEqual('running',result['status'])
            self.assertEqual('failed',result['scheduler_status'])
            self.assertTrue(result['live']['recovery'])
            self.assertEqual(['api_one'],result['live']['api_ids'])
            self.assertEqual('awaiting_inspection',stage_activity(root,task,None,lambda pid:None)['status'])

    def test_partial_event_and_tool_bodies_are_not_exposed(self):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'events.jsonl'
            path.write_text('{"type":"text","part":{"text":"private reasoning"}}\n{"type":"tool_use","part":{"tool":"source_catalog","state":{"status":"completed","output":"private source"}}}\n{"partial"')
            events=event_tail(path)
            self.assertEqual(1,len(events))
            self.assertNotIn('private',str(events))
