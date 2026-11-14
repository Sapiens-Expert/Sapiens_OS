# Implement in your own AI environment

## Minimal setup

Place `AGENTS.md` in the tool's persistent project instructions if supported. Put the templates and docs in the same project or make them available on demand. Ask the AI to read the relevant file at the start of each review. Test it with fictional data before sharing real health information. Verify it can enumerate ten domains, honor a skip, preserve `unknown`, distinguish observation from inference, and respond to an urgent example without waiting for a scheduled review.

## Dashboard choice

After the initial ten-domain interview, offer the person `docs/DASHBOARD.md`. Ask whether a dashboard helps, which one to three signals matter, and whether a paper/notes version is preferable. The included `dashboard/index.html` works as an offline starter with manual reflections and CSV import. It does not sync devices or send alerts in the background. Verify data provenance and missingness before discussing trends.

## Data ownership

The public source repository is a blank template. Keep completed profiles and check-ins outside it, in a private location you choose. Consider whether your AI vendor stores conversations, trains on them, exposes them to collaborators, or supports deletion and export. Choose minimum necessary details, redact third-party information, and avoid storing medical documents by default. If you create a private fork, check its visibility and access before saving any records; a fork or its history may later become public.

A suggested private note: date, owner-defined goal, domain observations, context, uncertainty, user-approved experiment, stop condition, next review, and source of each observation. The owner may edit or erase it. Do not silently use wearable, calendar, email, or other connected data.

## Reminders and integrations

The AI may suggest a quarterly date, but only create a real reminder when the user authorizes it and a scheduling integration exists. State the exact schedule, timezone, notification channel, and whether it was successfully created. Without such integration, give the user a calendar entry to set manually. No repository file creates autonomous alerts; any continuous signal system would need separately designed consent, security, validation, and clinical safety review.

For a routine the person chooses, follow [HABITS.md](HABITS.md). The [local tracker](../habits/index.html) keeps entries in the current tab unless the person exports a JSON copy; it can produce an optional repeating calendar `.ics` event. The calendar application, not the HTML page, decides whether to import it and notify. The person must verify the event, timezone, notification setting, privacy and end date in that calendar, and delete it there to stop reminders. Keep this separate from health alerts or clinical triage.

## Adaptation

Translate wording and examples for age, culture, disability, shift work, chronic illness, household and income constraints. Preserve optionality, all ten inquiry areas, evidence boundaries, and urgent escalation. The system should fit a person's life rather than demand that they fit a universal ideal.
