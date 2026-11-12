# Kafka Consumer Lag Slo Guard architecture

SRE utility for AI/ML streaming platforms that flags Kafka consumer groups at risk of missing freshness SLOs.

```mermaid
flowchart LR
    A["Lag, ingest rate, and freshness limit"]
    B["Estimate lag divided by ingest rate"]
    C{"Estimate exceeds SLO?"}
    D["Warn or page at 1.5× threshold"]
    E["Omit OK group from output"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
