---
name: return
description: Welcome someone back to Sapiens OS after a gap of weeks or months, with no guilt and no catch-up. Offers to resume, shrink, change or close what they had. Use only when the person asks, or says they have been away.
disable-model-invocation: true
compatibility: Designed for Claude Code. Other agents that read Agent Skills can use it by reading AGENTS.md at the repository root.
license: MIT
---

# Return after a gap

Read AGENTS.md first (`${CLAUDE_PLUGIN_ROOT}/AGENTS.md` in a plugin install, otherwise the repository root). A lapse is information about fit, not a verdict on the person. Do not list what was missed, do not compare against streaks, and do not ask them to explain the gap.

## Steps

1. **One welcoming line.** Say it is fine that time passed and that they set the pace.
2. **Look quietly.** Read `profile.md` and `experiments.md` if they exist and note their dates. If nothing exists, say so and offer `/sapiens-os:start`.
3. **Offer four doors, not a plan.** Pick up where it was, shrink it to the smallest version, change it, or close it. Ask which fits today. Closing is a good answer.
4. **Ask what changed in life.** Work, health, caring duties, money, mood, season. Ask once, accept any answer, and do not interpret it.
5. **If the gap was long (about three months or more),** offer a light refresh of only the profile items that may be stale, such as constraints, supports and the chosen mode. Do not restart the full onboarding unless they ask.
6. **If they want to leave,** follow the pause, disable and removal path in AGENTS.md and [docs/LIFECYCLE.md](../../docs/LIFECYCLE.md) without asking them to reconsider.
7. **Offer to save** the outcome as a short dated note, and write it only on a yes.

Any new, persistent, worsening or severe concern goes to [docs/SAFETY.md](../../docs/SAFETY.md) first.
