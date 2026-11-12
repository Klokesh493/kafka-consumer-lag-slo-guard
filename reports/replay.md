# Replay evidence

Captured stdout is compared with a checked-in baseline.

## Demo 1

Result: **PASS**

````text
warn: feature-risk-prod on features.risk needs 15.0m
warn: fraud-signals-prod on events.fraud needs 30.0m
````

## Demo 2

Result: **PASS**

````text
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
````
