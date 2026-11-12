# Kafka Consumer Lag Slo Guard walkthrough

## Business problem

SRE utility for AI/ML streaming platforms that flags Kafka consumer groups at risk of missing freshness SLOs.

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
