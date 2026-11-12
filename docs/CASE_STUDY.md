# Kafka Consumer Lag Slo Guard walkthrough

## Business problem

A consumer group can process messages without shrinking its backlog. Responders need to distinguish stalled recovery from a backlog that will clear within the freshness target.

## Reproduce the workflow

Run `python3 lag_guard.py sample_lag.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
warn: feature-risk-prod on features.risk needs 15.0m
warn: fraud-signals-prod on events.fraud needs 30.0m
```

The sample supplies these fields. `consumer_group`, `topic`, `lag_messages`, `ingest_rate_per_min`, `slo_minutes`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.

## Incident replay

A freshness alert is harder to interpret when a backlog stays flat. The
consumer may be processing messages at the same rate producers create
them, so it can serve traffic while making no progress toward recovery.

Run `python3 replay.py examples/replay.csv`. The first snapshot reports
`stalled` because consume and ingest rates are both 800 messages/minute.
At minute five the consumer drains 600 messages/minute net, but a backlog of
12,000 still projects 20 minutes to recover against a 10-minute SLO.
At minute ten the projection drops to five minutes and the result is `ok`.

The estimates assume constant rates within each snapshot. The replay reads
synthetic CSV and sends no pages. The original CLI continues to accept the
older CSV format, which has no measured consumer throughput.
