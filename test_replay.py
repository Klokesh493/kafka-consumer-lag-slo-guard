import json
import subprocess
import sys
import unittest

from replay import review


class ReplayTest(unittest.TestCase):
    def test_replay_captures_stall_breach_and_recovery(self):
        raw = subprocess.check_output(
            [sys.executable, "replay.py", "examples/replay.csv"], text=True
        )
        result = json.loads(raw)
        self.assertEqual([row["decision"] for row in result], ["stalled", "page", "ok"])
        self.assertEqual([row["catchup_minutes"] for row in result], [None, 20, 5])

    def test_empty_backlog_is_healthy_without_traffic(self):
        row = dict(minute="0", consumer_group="g", topic="t", lag_messages="0",
                   ingest_rate_per_min="0", consume_rate_per_min="0", slo_minutes="10")
        self.assertEqual(review(row)["decision"], "ok")
        with self.assertRaises(ValueError):
            review(dict(row, consume_rate_per_min="nan"))
