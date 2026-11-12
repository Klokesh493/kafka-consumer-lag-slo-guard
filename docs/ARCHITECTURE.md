# Kafka Consumer Lag Slo Guard architecture

SRE utility for AI/ML streaming platforms that flags Kafka consumer groups at risk of missing freshness SLOs.

```mermaid
flowchart LR
    N0["sample_lag.csv"]
    N1["lag_guard.py"]
    N2["minutes to catch up / lag status / risky groups"]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
