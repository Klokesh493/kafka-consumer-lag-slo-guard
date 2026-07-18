import unittest

from lag_guard import lag_status, risky_groups


class LagGuardTest(unittest.TestCase):
    def test_pages_when_catchup_exceeds_slo_by_half(self):
        row = {"lag_messages": "12000", "ingest_rate_per_min": "800", "slo_minutes": "8"}
        self.assertEqual(lag_status(row), "page")

    def test_returns_only_non_ok_groups(self):
        rows = [
            {"consumer_group": "a", "topic": "x", "lag_messages": "100", "ingest_rate_per_min": "100", "slo_minutes": "5"},
            {"consumer_group": "b", "topic": "y", "lag_messages": "1000", "ingest_rate_per_min": "100", "slo_minutes": "5"},
        ]
        self.assertEqual([item["consumer_group"] for item in risky_groups(rows)], ["b"])


if __name__ == "__main__":
    unittest.main()
