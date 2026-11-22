---
name: start
description: Two-minute first session with Sapiens OS. Asks one question about what the person would like to feel different, then offers one small experiment with a review date. Use only when the person asks to start Sapiens OS or try it.
disable-model-invocation: true
compatibility: Designed for Claude Code. Other agents that read Agent Skills can use it by reading AGENTS.md at the repository root.
license: MIT
---

# Start: a first win in two minutes

Read AGENTS.md first (`${CLAUDE_PLUGIN_ROOT}/AGENTS.md` in a plugin install, otherwise the repository root). Its rules govern this skill. This is education and coaching, not medical advice.

Never write or change a file without showing the exact text and getting a yes. A skipped question is fine. The person can stop at any point.

## Steps

1. **Frame it in two sentences.** You will ask one question, offer one small experiment and a date to look at it again. Nothing runs in the background, and they can say stop at any time.
2. **Language.** Ask which language they want for this conversation and for anything you write down. Follow [docs/LANGUAGE.md](../../docs/LANGUAGE.md).
3. **The one question.** "What is one thing in your daily life you would like to feel different in the next month? Or say 'nothing yet, just explore'." Do not offer a list of domains.
4. **Check before you go on.**
   - New, severe, persistent or worsening symptoms, or any risk of harm: stop here and follow [docs/SAFETY.md](../../docs/SAFETY.md).
   - A goal about fat loss, muscle or body size: run the starting-point check in [docs/paths/FITNESS.md](../../docs/paths/FITNESS.md) first. If any row there applies, a professional comes before any plan.
5. **One clarifying question.** "What most often gets in the way?" Treat a structural limit (shift work, caring duties, money, access) as a fact, not a motivation problem.
6. **Offer one experiment.** Use [templates/HABIT-EXPERIMENT.md](../../templates/HABIT-EXPERIMENT.md) as the shape: a cue, a small version, a bad-day version, a stop condition and a review date within two weeks. Choose with the person. Offer at most one method from the [science library](../../docs/science/README.md), and only if its "open it when" line fits. Say its evidence tag in plain words.
7. **Offer to save it.** If a private workspace exists (a folder whose CLAUDE.md says Sapiens OS workspace), show the draft entry for `experiments.md` and write it only on a yes. If none exists, offer `/sapiens-os:setup`, and until then keep nothing.
8. **Close with choices, not a push.** Offer any of: the full ten-domain onboarding in [templates/ONBOARDING.md](../../templates/ONBOARDING.md) (about 30 minutes, one section at a time, skippable), a real reminder using [docs/RHYTHM.md](../../docs/RHYTHM.md), or stop here.

## Output

Keep it short: what you heard, the one experiment, who decides, the review date, and whether any professional input is indicated.
