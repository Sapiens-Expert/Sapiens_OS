---
name: review
description: Quarterly Sapiens OS review across all ten domains, ending with an honest question, is this still worth keeping and in what form. Use only when the person asks for a review or says it is time for one.
disable-model-invocation: true
compatibility: Designed for Claude Code. Other agents that read Agent Skills can use it by reading AGENTS.md at the repository root.
license: MIT
---

# Quarterly review

Read AGENTS.md first (`${CLAUDE_PLUGIN_ROOT}/AGENTS.md` in a plugin install, otherwise the repository root). Follow [templates/QUARTERLY-REVIEW.md](../../templates/QUARTERLY-REVIEW.md) for the questions and the ten-domain table. This skill adds the order and the closing question.

## Steps

1. **Gather.** Read `profile.md`, `experiments.md`, recent `check-ins/` notes, the last file in `reviews/` and any `exports/brief-*.md`. Say what exists and what does not. If there is no earlier record, reconstruct a baseline with the person instead of pretending to remember.
2. **Context first.** Ask what changed in goals, work, caring duties, money, access needs, support and treatment. Ask which past experiments helped, did nothing or cost too much.
3. **All ten domains, one at a time,** even if unchanged. Use the person's own words. `better`, `about the same`, `worse` or `unknown` only if they choose it. These are reflections, not scores.
4. **Synthesis with consent.** Offer a hypothesis about the main limiting constraint and at least one alternative. Check [docs/SAFETY.md](../../docs/SAFETY.md). Agree on one or two changes, a stop condition and a date.
5. **The honest question.** "Is this still worth keeping, and in what form?" Offer: keep as is, shrink to on-demand only, pause, or remove. Ask what was useful and what was not, and treat the answer as feedback that stays in their workspace unless they decide otherwise.
6. **Show the full draft,** ask what to correct, delete or keep, and write `reviews/YYYY-MM-DD.md` only on a yes. Remind them to set their own reminder for the next one; see [docs/RHYTHM.md](../../docs/RHYTHM.md).

A choice to pause or remove ends the review. Follow the exit path in AGENTS.md.
