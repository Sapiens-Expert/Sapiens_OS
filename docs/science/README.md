# Behavioral science library

Sapiens OS framework developed by **Vladislav (Vlad) Andreev**. © 2026 Vladislav Andreev. MIT-licensed original code and text; brand assets excepted.

A set of short method modules the AI can open when a person's situation calls for one. Each module says what the method is, how strong the evidence is, what it does *not* show, how to use it with consent, and when to leave it alone. This is an educational aid, not a medical or clinical protocol, and none of it validates Sapiens OS itself (see [EVIDENCE.md](../EVIDENCE.md)).

## How to read the evidence tags

| Tag | Meaning here |
| --- | --- |
| **Established** | Consistent findings across several meta-analyses or a large body of field and lab work. Effects are still averages, not promises for one person. |
| **Promising** | Small to moderate average effects in meta-analyses, usually with heterogeneity, publication-bias warnings or short follow-up. Worth a time-boxed trial. |
| **Thin** | A few small studies, mostly correlational work, or a practice that is popular but with little direct testing. Use as an experiment, never as a claim. |
| **Contested** | Credible researchers disagree, or large replications and bias-corrected analyses shrink the effect toward zero. See the [register](weak-evidence-register.md). |

A tag describes what a source actually tested. It is a judgment made on the date in [references.json](../../references.json) and should be rechecked before consequential advice.

## Modules

| Module | Open it when the person is... |
| --- | --- |
| [Decisions and forecasting](decisions.md) | facing a consequential choice, a plan with a deadline, or repeated underestimates of time and effort |
| [Motivation and goals](motivation-and-goals.md) | setting a goal, stuck between wanting and doing, or recovering from a lapse |
| [Attention and load](attention-and-load.md) | fragmented by switching, interruptions or too many open commitments |
| [Energy and recovery](energy-and-recovery.md) | depleted, unable to switch off, or shaping their work and sleep timing |
| [Environment and commitment](environment-and-commitment.md) | relying on willpower where friction, cues or a commitment would do the job |
| [Weak-evidence register](weak-evidence-register.md) | quoting a popular claim, or asked "is it true that..." |

## Rules for every module

1. Offer one method at a time, and say its tag in plain words. Ask before applying it.
2. Never present an average effect as a prediction for this person.
3. A method is an experiment with a review date and a stop condition, in line with [HABITS.md](../HABITS.md).
4. A structural constraint (workload, money, caregiving, safety) is not a method problem. Say so.
5. Anything resembling a clinical symptom goes to [SAFETY.md](../SAFETY.md), not to a method.

## Source integrity

Every numbered reference in these pages (for example `R05`) has an entry in [references.json](../../references.json) with its title, authors, year, venue and the date its abstract was read. Run `python3 tools/check_references.py` before merging a change: it fails on a missing or unused reference, a missing evidence tag, or a module without a "When not to use" section. A claim without a source is cut, not hedged.

Not yet reviewed, so deliberately absent: heart-rate-variability or "readiness" scores, step-count targets, chronotype questionnaires, time-restricted eating, cold exposure, and any supplement. Add them only with sources opened and tagged.
