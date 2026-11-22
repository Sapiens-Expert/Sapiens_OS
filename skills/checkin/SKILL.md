---
name: checkin
description: A short, optional Sapiens OS check-in (about five minutes): how the week went, how the current experiment is going, one next step or no change. Use only when the person asks for a check-in.
disable-model-invocation: true
compatibility: Designed for Claude Code. Other agents that read Agent Skills can use it by reading AGENTS.md at the repository root.
license: MIT
---

# Check-in

Read AGENTS.md first (`${CLAUDE_PLUGIN_ROOT}/AGENTS.md` in a plugin install, otherwise the repository root). The method follows [templates/WEEKLY-CHECK-IN.md](../../templates/WEEKLY-CHECK-IN.md).

You have no memory of the person except what is in files they gave you. Say which files you read and their dates. A missing entry is unknown, never a failure.

## Steps

1. **Read, if they exist:** `profile.md`, `experiments.md`, the latest note in `check-ins/`, and the newest `exports/brief-*.md` (a summary the person downloaded from the local dashboard). Tell the person what you found and what you did not.
2. **Ask three things, each skippable.** How did the week go, in your words? If there is an experiment: did the cue happen, did you do it, adapt it, skip it or have no chance, and did it help, cost energy or add pressure? Anything new, persistent, worsening or severe?
3. **Care threshold.** If something needs it, follow [docs/SAFETY.md](../../docs/SAFETY.md) before anything else.
4. **Reflect, then ask.** Name what you heard and ask whether the reading fits before offering any interpretation. Cite dates. Never score the person or predict anything.
5. **One decision.** Keep, adapt, pause or stop the experiment, or no change. Offer one feasible next step, a stop condition and a review date.
6. **Offer to save.** Show a short dated note for `check-ins/YYYY-MM-DD.md` and write it only on a yes.

If the person is returning after a gap, use `/sapiens-os:return` instead.
