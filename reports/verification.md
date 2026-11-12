# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 lag_guard.py sample_lag.csv
warn: feature-risk-prod on features.risk needs 15.0m
warn: fraud-signals-prod on events.fraud needs 30.0m
python3 replay.py examples/replay.csv
[
  {
    "minute": 0,
    "consumer_group": "ranking",
    "topic": "features",
    "net_drain_per_min": 0.0,
    "catchup_minutes": null,
    "decision": "stalled"
  },
  {
    "minute": 5,
    "consumer_group": "ranking",
    "topic": "features",
    "net_drain_per_min": 600.0,
    "catchup_minutes": 20.0,
    "decision": "page"
  },
  {
    "minute": 10,
    "consumer_group": "ranking",
    "topic": "features",
    "net_drain_per_min": 600.0,
    "catchup_minutes": 5.0,
    "decision": "ok"
  }
]
test_pages_when_catchup_exceeds_slo_by_half (test_lag_guard.LagGuardTest) ... ok
test_returns_only_non_ok_groups (test_lag_guard.LagGuardTest) ... ok
test_empty_backlog_is_healthy_without_traffic (test_replay.ReplayTest) ... ok
test_replay_captures_stall_breach_and_recovery (test_replay.ReplayTest) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.026s

OK
````
