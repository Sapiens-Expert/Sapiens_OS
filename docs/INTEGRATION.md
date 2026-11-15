# Opt-in personal AI integration

Sapiens OS can be used as a scoped, removable layer in a person's AI project. The default remains **on-demand**. A person can opt into contextual suggestions or an explicitly scheduled review, and can pause, disable or remove the layer under [LIFECYCLE.md](LIFECYCLE.md). A repository checkout alone does not monitor a person, receive wearable data, schedule jobs, or send notifications.

## The useful result of onboarding

The output is a person-approved **baseline and action brief**, not merely ten answers:

1. A ten-domain picture with each area labeled `supportive`, `mixed`, `difficult` or `unknown`, the person's own words, and any focus areas **chosen by them**. The [dashboard](../dashboard/index.html) displays this as a qualitative map. Statuses are reflections, not clinical grades or a composite score.
2. A short account of strengths, the person's chosen priority, constraints that affect several domains, alternative explanations and missing information. Ask which change would matter in daily life. Do not automatically rank a domain by its color or claim the lowest tile needs fixing.
3. One feasible, reversible experiment or a decision to seek human support, with a cue, stop condition and review date. The person may choose no action. The quarterly review revisits all ten domains; a shorter weekly check-in is optional.
4. If requested, an opt-in dashboard and one to three personal signals, with source, units, coverage and context. Device data never fills an unanswered domain or determines clinical safety.

The immediate value is orientation: the person sees what is supportive, what is uncertain, what feels difficult, and which constraint they want to address. They can correct the map before it is saved.

## Integration boundary

| Component | Input and permission | Output | Removal |
| --- | --- | --- | --- |
| AI project instructions | Person enables scoped `AGENTS.md` | On-demand or contextual conversation under chosen mode | Remove instruction reference and project copy |
| Private operating note | User-approved onboarding summary only | Current baseline, priorities, exclusions, language and rhythms | Delete note and retrieval copy |
| Optional local dashboard | User-approved private JSON / CSV | Ten-domain map and descriptive trends | Close tab; delete exported private files |
| Optional pattern review | Explicitly supplied dated check-ins, selected domains and consent | Evidence-linked *question to discuss*, never diagnosis | Stop task and delete private inputs/results |
| Optional scheduler/connector | Separate opt-in for exact source, scope, cadence and channel | Invokes a review while authorized; shows last run | Cancel job, revoke token, delete cache and event |

Do not move health records into a public repository, generic global memory, public logs or analytics. A personal installation should keep an [inventory](../templates/INSTALLATION-RECORD.md) of instructions, data, jobs and outputs. Each input should have provenance, timestamp, retention choice and user correction path. Connectors require least-privilege consent, secure credentials, scoped deletion and an explicit “last checked” state. Refer to [CONNECTORS.md](CONNECTORS.md) for future vendor sync; the starter supports manual files only.

## Noticing a pattern

1. The person chooses which signals matter and how often to review. If no permission for scheduled review exists, the AI waits until they ask. If a scheduler is available, confirm exact cadence, timezone, notification surface, quiet hours, data sources and how to stop it; verify the job was created. An AI without that integration must not claim it will notice things in the background.
2. At each authorized review, read only the approved recent period. Check dates, data coverage, source changes, travel/illness/workload/cycle context if volunteered, and changes in routine. Compare to the person's own approved baseline. Missing data is **unknown**, not reassuring or alarming.
3. Distinguish **observation** (“two dated check-ins describe difficult rest and reduced functioning”) from **hypothesis** (“the current workload may be contributing”) and **action** (“would you like to look at demands and support?”). Ask whether the interpretation fits; offer a reversible step. Do not infer a diagnosis, assign a risk score or treat a sensor deviation as proof of harm.
4. Report the exact observations, alternatives, confidence/uncertainty and last review date. The person decides what is important. Use [SAFETY.md](SAFETY.md) for disclosed urgent concerns without waiting for repeated check-ins. Do not promise emergency detection or response.
5. Keep a user-editable review log. If the person declines a cue, pauses the framework, or changes their baseline, update the private note with consent and stop unused jobs. Review whether nudges themselves create burden.

The included [local review script](../tools/review_patterns.py) is a small, offline reference for *explicitly provided* check-ins. It does not monitor files or send messages. The [fictional example](../examples/sample-check-ins.json) lets installers test a discussion cue before considering any personal data. Its output is educational and requires the person's interpretation.

## Required acceptance checks for an integration

- Onboarding yields a reviewable ten-domain map and a person-chosen focus; skipped areas remain `unknown`.
- The AI can say what was observed, when, from which source, and what it cannot conclude. It does not fire an alert from missing data.
- Only authorized sources and surfaces are used; a scheduled job is observable and stoppable; no duplicate reminders appear.
- A user correction changes future interpretation; a change in rhythms prompts review of the baseline, not a rigid population target.
- “Pause,” “disable” and “remove” stop framework use and jobs and produce the truthful removal receipt described in [LIFECYCLE.md](LIFECYCLE.md).
