# Sapiens OS for Humans

**Framework creator and developer: Vladislav (Vlad) Andreev.** © 2026 Vladislav Andreev. Original code and documentation: [MIT License](LICENSE). [Brand and rights details](RIGHTS.md).

A portable, human-owned set of instructions for working with an AI assistant to notice patterns in well-being and make sustainable choices. This repository presents the ten-domain Sapiens OS framework developed by Vladislav (Vlad) Andreev. This is an educational decision aid, not a medical device, diagnosis, treatment, or emergency service. There is no evidence that these ten domains, this particular scoring approach, or an AI chat can reliably predict burnout or disease.

Generated dashboards, reports and other branded materials follow the [brand and visual production standard](docs/BRANDING.md), with the approved O!Sapiens wordmark and the visible name **Sapiens OS** for this framework.

## Start in 10 minutes

1. Create your own **private** working copy or project. The MIT-licensed code and documentation can be used without asking for individual permission; see [RIGHTS.md](RIGHTS.md) for the separate brand-asset boundary. Keep this public template free of your health data. Do not submit completed forms in issues or pull requests.
2. Give your AI assistant [AGENTS.md](AGENTS.md) as its standing instruction, then ask: “Start the Sapiens OS onboarding interview in `templates/ONBOARDING.md`. Ask one section at a time. Let me skip any question.” If your AI cannot retain files, paste AGENTS.md and the form at the start of each session.
3. Save your answers outside this template in your own private notes. You can use the blank form, or keep only a concise summary. Review what the AI retained and correct it. Do not upload records, tests, diagnoses, or third-party information unless you understand the service's data controls.
4. Set your own calendar reminder for a quarterly review. At that time give the AI your latest private summary and [templates/QUARTERLY-REVIEW.md](templates/QUARTERLY-REVIEW.md). An AI chat alone cannot guarantee a scheduled check-in or alert; use a real reminder or automation you control.
5. Between reviews, use [templates/WEEKLY-CHECK-IN.md](templates/WEEKLY-CHECK-IN.md) when useful. You can stop, delete your notes, or change the system at any time.

**Quick-start prompt:** “Read AGENTS.md and the onboarding template. First ask which language(s) I prefer for conversation, summaries and any reports or reminders. Ask permission for each sensitive topic, cover all ten domains without assuming answers, and finish with my reviewable baseline, the single most useful next experiment, and a date for follow-up. Tell me which information you stored.”

## Ten domains

| Foundations | Regulation and context | Coherence |
| --- | --- | --- |
| Sleep; nutrition; movement | Stress; social connection; light/dark rhythms; agency | Meaning; rest; curiosity |

The domains are a teaching structure, not ten equally validated biomarkers or a required sequence. Start with the person's own priorities and the main constraint; do not optimize all domains at once. `docs/FRAMEWORK.md` explains the questions and boundaries.

## How the loop works

Onboard across all ten domains → agree on a private baseline and what matters → optional brief check-ins → notice changes and ask clarifying questions → propose one feasible adjustment or recommend qualified care when appropriate → quarterly full review. The human decides what to share, try, retain, and stop. The AI must not claim passive monitoring, automatic detection, or emergency response unless those capabilities have actually been configured and tested.

After onboarding, the AI offers an optional [local dashboard](dashboard/README.md) with a ten-domain reflection and imported weekly or monthly data. [Data-source setup](docs/CONNECTORS.md) explains Apple Health, Oura, generic CSV and what a future consented sync would require. It runs without an account or network connection, and makes no clinical prediction. For coaching and behavior-change practice, see [docs/COACHING.md](docs/COACHING.md).

The dashboard now shows a **qualitative ten-domain map** and lets the person choose areas to explore. The [integration guide](docs/INTEGRATION.md) describes the reviewable baseline and action brief after onboarding and how an opt-in AI integration can notice dated, person-selected patterns. Try its [fictional check-ins](examples/sample-check-ins.json) with the [offline review script](tools/review_patterns.py). Nothing in this repository runs in the background or sends an alert on installation.

To try a small routine, use the [habit guide](docs/HABITS.md), [private experiment template](templates/HABIT-EXPERIMENT.md), and optional [local habit tracker](habits/index.html). The tracker supports dated reflections and an opt-in calendar event download. It does not send notifications itself or monitor behavior in the background.

For integration into your own AI environment, follow the [installation and removal guide](docs/LIFECYCLE.md). It explains how to adapt to the person's changing rhythms and keep the framework in a removable project boundary. Use is **on-demand by default**; contextual suggestions require an opt-in. A private [installation record](templates/INSTALLATION-RECORD.md) tracks where instructions, generated files, reminders and connected data live. The person can [ask their AI to pause, disable or remove the framework](templates/REMOVE-FRAMEWORK.md); the AI must verify what it can remove and identify what remains in other services or backups.

The [language guide](docs/LANGUAGE.md) makes the person's chosen language govern AI interactions and generated materials. The included HTML dashboard and habit tracker currently have English interface text; localize a copy before deploying them in another language.

See [docs/SAFETY.md](docs/SAFETY.md) for escalation, [docs/EVIDENCE.md](docs/EVIDENCE.md) for the scientific basis and limits, and [docs/IMPLEMENTATION.md](docs/IMPLEMENTATION.md) for platform setup and privacy.

## Operator pack and science library

For people who run things (a business, a team, a household, their own work), the optional [operator pack](operator/README.md) adds a daily start and close, a monthly capacity review, an annual review and a decision record, on a rhythm the person controls. It draws on a [behavioral science library](docs/science/README.md): short method modules for decisions, motivation, attention, recovery and environment, each with an evidence tag, its limits and a "when not to use" note, plus a [register of popular claims that do not hold up](docs/science/weak-evidence-register.md). Sources are listed in [references.json](references.json); `python3 tools/check_references.py` verifies them.

## Authorship and rights

Sapiens OS was developed by **Vladislav (Vlad) Andreev**. Original code, templates and documentation are [MIT-licensed](LICENSE): use, adapt and share them, including commercially, while retaining the copyright and license notice. No individual written consent is needed for that licensed use. The O!Sapiens logo files under `assets/brand/` are excluded from MIT and may be used to identify this original project in its unmodified demonstration pages; see [RIGHTS.md](RIGHTS.md). Private health data is never part of the open-source grant. Contributors must have the rights to license their additions under MIT.
