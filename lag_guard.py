import csv
import sys


def minutes_to_catch_up(row):
    rate = max(float(row["ingest_rate_per_min"]), 1.0)
    return float(row["lag_messages"]) / rate


def lag_status(row):
    projected = minutes_to_catch_up(row)
    slo = float(row["slo_minutes"])
    if projected > slo * 1.5:
        return "page"
    if projected > slo:
        return "warn"
    return "ok"


def risky_groups(rows):
    return [
        {
            "consumer_group": row["consumer_group"],
            "topic": row["topic"],
            "status": lag_status(row),
            "catchup_minutes": round(minutes_to_catch_up(row), 2),
        }
        for row in rows
        if lag_status(row) != "ok"
    ]


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for item in risky_groups(csv.DictReader(handle)):
            print(f'{item["status"]}: {item["consumer_group"]} on {item["topic"]} needs {item["catchup_minutes"]}m')


if __name__ == "__main__":
    main(sys.argv[1])
