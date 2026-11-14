# Data sources and future synchronization

Device data is personal, not a public dataset. What may be publicly available is documentation or a user-authorized export/API. The owner decides whether to connect a source at all. Start with a file export and keep the dashboard offline.

| Source | Current starter route | Ongoing sync route (not implemented) | Caveat |
| --- | --- | --- | --- |
| Self-report | Ten-domain profile and optional notes in the dashboard | User-owned private file or local app | Subjective data often explains context that sensors cannot see. |
| Apple Health | iPhone Health → Export All Health Data → extracted XML → selected type through `tools/convert_health.py` | A separate, consented native app with HealthKit permissions | Export can contain many sensitive records and overlapping device sources. Choose one source; avoid interpreting a selected metric alone. |
| Oura | Oura on the Web Trends → Download Data CSV → select a date and numeric column in the dashboard | A separate registered API V2 app with OAuth scopes and secure token storage | Membership and API access conditions vary. No tokens should be placed in this repository or dashboard. |
| Other wearable | User-exported CSV → explicit date/value/unit/source mapping | Provider-specific adapter with scope-limited authorization | Check data definition, units, device version, timezone and duplicate records. |

## Normalized adapter contract

An adapter produces `date,metric,value,unit,source,context_phase`. It must report its source version, timezone/date interpretation, sampling period, aggregation method, missingness, unit conversion, duplicate policy and errors. Never silently blend distinct sources or claim a device score is comparable across vendors. Keep raw exports separate and private; transformed rows are a convenience view, not a substitute for original records.

For a real sync service, specify consent per source and data type, least-privilege access, encryption, credential rotation, a deletion/export path, offline behavior, retries with backoff, idempotent upserts, and a user-visible “last synced” state. Obtain a separate security/privacy and clinical-scope review before deploying it. A scheduled import can use a private user-owned folder and an OS task, but avoid unattended parsing of untrusted files and do not call it continuous monitoring.

Cycle-related context is optional; only a person can decide whether to record it. Never infer menstrual phase, ovulation, sex, gender or fertility from temperature, HRV or dates in this starter. A user may be pregnant, postpartum, perimenopausal, on hormonal treatment, not cycling, or unwilling to disclose. A sensor change remains an observation that can have many explanations.
