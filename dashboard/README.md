# Local dashboard starter

The original starter uses the approved O!Sapiens master-brand wordmark, the Sapiens OS framework name and visual tokens documented in [BRANDING.md](../docs/BRANDING.md). The logo is excluded from MIT; replace it with your own artwork or text in a separately branded distribution. Retain the MIT copyright notice in copies or substantial portions. Do not include the logo in the private session JSON export.

Open `index.html` in a modern browser, from inside the repository so that `../assets/theme.css` and the logo load. Import fictional `../examples/sample-profile.json` to try the onboarding handoff, then `../examples/sample-data.csv` for trends; clear the tab afterward. Files are parsed in the current tab; the page contains no remote scripts or analytics and does not save data across refreshes. A browser extension, sync feature or computer backup may still access local files, so keep your own device secure.

The fictional `../examples/sample-fitness.csv` shows training-log trends (a lift's load and a self-rated energy score per session, no body weight) for the [fitness path](../docs/paths/FITNESS.md).

Use a normalized CSV (`date,metric,value,unit,source,context_phase`) or map one numeric column in a generic/Oura Trends CSV. Select the date, value, metric label, unit and source. The import preview is not uploaded. A person may set an optional personal range for a two-period review cue; it never runs in the background. Weekly and monthly trends show averages of available days, count and missing days within the selected date span; do not treat these as clinical norms. A free-text note can be kept only during the session. There is no automated alert, OAuth sync, cycle phase inference or medical interpretation.

The onboarding JSON now displays a ten-domain qualitative map. Each domain can include an optional `focus: true` chosen by the person; the page lets them edit statuses, notes and focus. The map is an accessible set of labeled tiles with a short summary, not a clinical score or automatic priority ranking. Use the person's own explanation and [INTEGRATION.md](../docs/INTEGRATION.md) for a short action brief after onboarding.

For Apple Health, export all data on the iPhone, extract `export.xml` locally, then run `python3 tools/convert_health.py apple /path/to/export.xml output.csv --type HKQuantityTypeIdentifierStepCount`. The converter supports selected quantity types only; consult `--help`. Treat both the original and converted file as sensitive. Never commit them.

## Look and feel

The page is one HTML file plus a shared local stylesheet, [`../assets/theme.css`](../assets/theme.css), also used by the [routine experiment](../habits/index.html). It has a branded header, a section navigation bar, summary tiles, a ten-tile domain map, and a small line chart of weekly or monthly averages with the accessible table kept beside it. Hollow dots mark periods with too few observed days, and an optional shaded band shows the person's own range. Light and dark follow the system setting, and the layout works at phone width and in print.

Why plain HTML and CSS: component registries such as 21st.dev publish React and Tailwind components that need a build step and packages. This starter keeps to a file you can open offline, with no remote code, fonts or analytics, because that is the privacy promise above. A fork that accepts a build step can port the tokens in `assets/theme.css` into its own design system. The stylesheet uses the five brand colors; the neutrals and dark-mode values are derived from them and documented in [BRANDING.md](../docs/BRANDING.md).

## Brief for your AI

`Download a brief for my AI` saves `brief-YYYY-MM-DD.md`, a short summary built in your browser (map, note, recent weekly averages, no raw rows). It sends nothing anywhere. See [DASHBOARD.md](../docs/DASHBOARD.md).
