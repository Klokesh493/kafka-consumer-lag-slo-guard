"""Review successive Kafka lag snapshots with measured consumer throughput."""
import argparse
import csv
import json
import math


def review(row):
    backlog, ingest, consume, slo = (
        float(row[key]) for key in (
            "lag_messages", "ingest_rate_per_min", "consume_rate_per_min", "slo_minutes"
        )
    )
    if not all(math.isfinite(value) and value >= 0 for value in (backlog, ingest, consume, slo)) or slo == 0:
        raise ValueError("lag and rates must be finite and nonnegative, and SLO must be positive")
    net_rate = consume - ingest
    minutes = 0 if backlog == 0 else backlog / net_rate if net_rate > 0 else None
    if minutes is None:
        decision = "stalled"
    elif minutes > slo * 1.5:
        decision = "page"
    elif minutes > slo:
        decision = "warn"
    else:
        decision = "ok"
    return {
        "minute": int(row["minute"]),
        "consumer_group": row["consumer_group"],
        "topic": row["topic"],
        "net_drain_per_min": net_rate,
        "catchup_minutes": round(minutes, 2) if minutes is not None else None,
        "decision": decision,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot_csv")
    args = parser.parse_args()
    try:
        with open(args.snapshot_csv, newline="", encoding="utf-8") as stream:
            results = sorted(
                (review(row) for row in csv.DictReader(stream, strict=True)),
                key=lambda row: (row["minute"], row["consumer_group"], row["topic"]),
            )
        print(json.dumps(results, indent=2, allow_nan=False))
    except (OSError, ValueError, TypeError, KeyError, csv.Error) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
