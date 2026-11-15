# Skills and verification

## What this repository demonstrates

A Kafka freshness review CLI and a replay mode for time-ordered snapshots. Replay subtracts ingest rate from consumer throughput and marks an existing backlog stalled when net drain is zero or negative. Otherwise it compares the estimated catch-up time to the SLO.

## Reproduce the result

The basic sample emits warnings for two groups. Replay adds measured drain rate and decision evidence for each snapshot. Reproduce the primary fixture with `python3 lag_guard.py sample_lag.csv`.

Run `make verify` locally. Ruff and Bandit medium/high checks passed for the checked Python code.

## Scope

The basic CLI uses ingest rate as a proxy. Use replay with measured throughput for recovery estimates. Both modes work on local exports and send no pages.

Use the replay path when measured consumer throughput is available. Backlog cannot shrink while consumer throughput is at or below ingest.

[lag_guard.py](../lag_guard.py) · [examples/Demo 1.stdout.txt](../examples/Demo%201.stdout.txt) · [Architecture](../docs/ARCHITECTURE.md) · [Case study](../docs/CASE_STUDY.md) · [Runbook](../docs/RUNBOOK.md) · [CI template](../docs/github-actions/ci.yml)
