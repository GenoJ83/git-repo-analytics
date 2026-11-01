# Architecture

```mermaid
flowchart LR
    GitLog[git log] --> StreamParser[Log Parser]
    StreamParser --> Engine[Churn & Velocity Engine]
    Engine --> Stats[Author & Churn Stats]
    Stats --> UI[Terminal / SVG / JSON]
```
