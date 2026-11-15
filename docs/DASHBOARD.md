# Personal dashboard: setup after onboarding

After the ten-domain interview, the AI **offers**, rather than assumes, a dashboard. Ask which questions it should answer, what metrics are worth the effort, whether cycle context is relevant, and where data may live. The person may choose a paper log or no dashboard. The dashboard is a reflection aid, not a validated warning system or medical device.

Apply the [brand and visual production standard](BRANDING.md) to the original dashboard and any human-readable report generated from it. Use the approved O!Sapiens mark with the Sapiens OS title for this original project; modified or separately branded distributions replace the logo under [RIGHTS.md](../RIGHTS.md). Preserve accessible text labels, source provenance and personal privacy.

## Minimum useful view

- Show all ten domains, with the person's own baseline and one-sentence observation or `unknown`; do not fill missing areas from a wearable.
- Show a qualitative ten-domain visual map with explicit text status and a person-selected focus. Unknown is visibly unknown. Let the person correct the map and choose the question they want to explore; no composite score or automated ranking of difficult domains.
- Show one to three personally relevant signals with clear units, source, date coverage and weekly/monthly summaries. Start with subjective functioning and demands/recovery where relevant, then add device data only if it helps.
- Display changes against the **person's own** prior data and context. Show gaps and changed devices, travel, illness, medication, shift work or other confounders. Never infer safety from an empty tile.
- Let the person set optional review prompts (for example, repeated self-reported difficulty or a sustained change they want to discuss). Prompts are invitations to review, not clinical thresholds or predictions. The starter offers an optional user-set range cue after two sufficiently observed weekly or monthly periods; it does not run while the page is closed. Urgent disclosed concerns always follow [SAFETY.md](SAFETY.md).
- Give an accessible table and plain-language summary; color is supplemental. Allow deleting imports and turning off cycle context or reminders.

## Data path

`User-approved interview summary → private profile → optional self-report / exported device file → local normalized rows → dashboard → person reviews interpretation → chosen action or referral.`

After onboarding, ask the AI to generate a private JSON file using `examples/sample-profile.json` as the schema: all ten exact domain names, each with `status` (`unknown`, `supportive`, `mixed`, `difficult`), a short user-approved `note`, and optional boolean `focus` chosen by the person, plus an optional overall `note`. The person reviews the file before importing it. No diagnoses or detailed records are necessary. The dashboard can load this JSON to prefill the ten-domain view and focus map. See [INTEGRATION.md](INTEGRATION.md) for the action brief and opt-in review path.

The included [dashboard](../dashboard/index.html) runs locally in a modern browser without a server, account, network dependency or persistent storage. It accepts the example normalized CSV and a single-metric CSV with chosen date/value columns. It keeps data in the current tab's memory; closing or refreshing clears it. The [converter](../tools/convert_health.py) can turn selected Apple Health XML records into normalized CSV. Oura Trends CSV can be mapped through the dashboard if it has a date and numeric metric column. Vendor exports change; inspect column names and units. No automatic account sync is implemented; see [CONNECTORS.md](CONNECTORS.md) for an adapter and consent design. For ongoing sync, an independent application would need the vendor's current OAuth/consent flow, secure token storage, duplicate handling, deletion, and threat review.

## Portable CSV contract

UTF-8 with header `date,metric,value,unit,source,context_phase`. Date is `YYYY-MM-DD`; numeric `value` uses a dot decimal; `metric` is a stable machine name; `unit` must be explicit; `source` names the device or self-report. `context_phase` is optional user-entered context (e.g. menstrual, follicular, luteal, unknown), **not** inferred ovulation. Do not mix different units or devices into one trend without conversion and a visible provenance note. For daily duplicate records, retain the original export separately and choose a clear aggregation policy; the starter dashboard displays the last valid value per date/metric/unit/source.

## Physiological diversity

Do not choose targets or alert thresholds solely from sex assigned at birth, gender, age, body size or population averages. Ask about relevant life stage and physiology only with consent: menstruation, pregnancy/postpartum, perimenopause/menopause, hormonal contraception or therapy, disability, chronic illness, training, shift work, medications, etc. Users may skip all. A cycle field is opt-in and private. Compare similar self-labeled phases only when enough personal observations exist; never presume a cycle, predict fertility, or explain symptoms away as hormonal. Wearable resting heart rate, HRV and temperature may vary across cycles and with many other factors; a notable or persistent concern should be assessed clinically, not dismissed by a dashboard.

## Accessibility and cognitive load

Use plain language, keyboard-operable controls, explicit labels, visible focus, table-based data, sufficient contrast and no color-only meaning. Provide a short default view with optional detail, no mandatory daily logging, no penalties for missing data, and a pause/exit path. Test with assistive technology and real users; this starter has not been audited for WCAG conformance.
