# Kafka Consumer Lag Slo Guard architecture

SRE utility for AI/ML streaming platforms that flags Kafka consumer groups at risk of missing freshness SLOs.

```mermaid
flowchart LR
    Legacy["Legacy lag export"] --> CLI["Original CLI estimate"]
    Snapshots["Snapshots with ingest and consume rates"] --> Net["Calculate net drain rate"]
    Net --> Stall{"Backlog with no positive net drain?"}
    Stall -->|Yes| Blocked["Stalled"]
    Stall -->|No| ETA["Estimate minutes to clear backlog"]
    ETA --> SLO["Compare with freshness SLO"]
    SLO --> Status["OK, warn, or page"]
    Blocked --> Report["Time-ordered JSON evidence"]
    Status --> Report
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
