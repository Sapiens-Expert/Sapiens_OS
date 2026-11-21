# Evidence map and limits

Reviewed 2026-11-14. These links support selected public-health context; they do **not** validate Sapiens OS as a clinical instrument, the ten-domain taxonomy, the quarterly cadence, or AI prediction of burnout or disease. Recheck current local guidance before consequential advice.

| Area | Grounding and limit |
| --- | --- |
| Sleep | [CDC adult sleep guidance](https://www.cdc.gov/sleep/about/) discusses duration, quality, and clinician review for sleep problems. Population guidance is not an individual diagnosis. |
| Movement | [WHO physical activity guideline](https://www.who.int/publications/i/item/9789240015128/) supports regular activity with adaptation for health and capacity. A personal plan may need qualified input. |
| Nutrition | [WHO healthy diet fact sheet](https://www.who.int/news-room/fact-sheets/detail/healthy-diet) supports dietary variety and adequacy. This repository does not prescribe diets or supplements. |
| Work stress | [WHO mental health at work guideline](https://www.who.int/publications/i/item/9789240053052) includes organizational interventions. [WHO ICD-11 burnout clarification](https://www.who.int/standards/classifications/frequently-asked-questions/burn-out-an-occupational-phenomenon) defines burnout as occupational, not a medical condition. Self-report patterns do not establish it. |
| Connection | [WHO Commission on Social Connection](https://www.who.int/publications/i/item/978240112360) describes health relevance of isolation and loneliness. The experience and desired amount of connection vary. |
| Safety | [NIMH warning signs](https://www.nimh.nih.gov/health/publications/warning-signs-of-suicide) illustrate why acute safety concerns require prompt human help. Use local emergency services for immediate danger. |
| Light/dark, agency, meaning, rest, curiosity | Useful inquiry areas in this teaching framework. This repository makes no claim that each is an independently validated score or that modifying any one will prevent illness. Evidence for specific interventions must be checked separately. |

The framework's practical hypothesis is that asking across interconnected domains and revisiting changes can improve a person's reflection and choices. It remains untested here. A future validation study would need defined populations, outcomes, false-positive and false-negative analysis, harms, privacy review, and comparison to usual support before any predictive claims.

## Behavior-change practices and limitations

- [Implementation intentions, Gollwitzer & Sheeran (2006)](https://cancercontrol.cancer.gov/brp/research/constructs/implementation-intentions) synthesize evidence for specific cue-linked plans. Effects vary by behavior and context; do not use a universal effect size as an individual promise.
- [Self-monitoring of sedentary behavior, systematic review (2019)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6693254/) found short-term benefits in included trials but noted heterogeneity and uncertainty about sustained effects. Tracking should be optional and judged for burden.
- [Motivational interviewing components for physical activity, systematic review (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11234249/) found low to very low certainty for several effects, no clear isolated effect versus similarly intensive comparators, and waning evidence over time. The AI uses collaborative language without claiming MI proficiency.

### Habit and reminder design

- [COM-B behavior change wheel, Michie et al. (2011)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3096582/) provides a way to inspect capability, opportunity and motivation before choosing an intervention. It does not imply all barriers can be fixed with individual effort.
- [Implementation intentions meta-analysis, Gollwitzer & Sheeran (2006)](https://www.decisionskills.com/uploads/5/1/6/0/5160560/2006_gollwitzersheeran_implementation_intentions.pdf) supports if–then planning for goal attainment in studied settings; a cue-linked plan is an option, not a guaranteed result.
- [Lally et al. (2010)](https://onlinelibrary.wiley.com/doi/10.1002/ejsp.674) followed real-world behavior repetition and automaticity and found wide variation. A single “21-day” or “66-day” prescription is not justified for an individual.
- [Randomized walking context study (2024)](https://pubmed.ncbi.nlm.nih.gov/39225981/) found consistent context improved habit automaticity in its sample, but the expected walking-maintenance advantage was not observed.
- [HabitWalk micro-randomized trial (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11635918/) included 24 participants; findings about prompts plus commitment are tentative and do not establish a universal reminder schedule. The reminder schedule in this repository is user-chosen, not clinically optimized.
- [Behavior change technique taxonomy, Michie et al. (2013)](https://pubmed.ncbi.nlm.nih.gov/23512568/) supplies consistent terms such as self-monitoring, action planning, and prompts/cues; it catalogs techniques rather than proving every technique works for every person.

## Behavioral science library

The decision, motivation, attention, recovery and environment methods used by the optional operator pack are documented in [docs/science](science/README.md), each with an evidence tag and cited sources in [references.json](../references.json). Several popular claims are recorded as contested in the [weak-evidence register](science/weak-evidence-register.md). These sources do not validate Sapiens OS as a whole.

## Fitness and body composition

The optional [fitness path](paths/FITNESS.md) uses [its own evidence module](science/fitness-and-body-composition.md), with each claim tagged and sourced in [references.json](../references.json). The module records what trials found about muscle gain, fat loss and regain, and flags the evidence linking tracking with eating-disorder symptoms. It does not validate Sapiens OS.

## Wearables, cycles and access

- [Apple Health export instructions](https://support.apple.com/en-gb/guide/iphone/iph5ede58c3d/ios) describe export in XML format. An XML export is a user-controlled snapshot, not live sync.
- [Oura export instructions](https://support.ouraring.com/hc/articles/360025441594-Export-Share-Your-Oura-Data) describe CSV Trends and personal-data export. [Oura API V2](https://cloud.ouraring.com/v2/docs) requires a registered app and OAuth; personal access tokens were deprecated in 2025. This project implements file import only.
- [Wearable menstrual-cycle study (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11416332/) and a [larger observational study (2026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13482339/) describe within-person variation in some wearable signals. Study populations and device measures do not define a person's clinical normal. Cycle phase should be optional and user-labeled, not inferred from a biomarker.
- [W3C WCAG 2.2](https://www.w3.org/TR/wcag/) informs the dashboard's labels, keyboard use, text alternatives and cognitive accessibility. This implementation is a starter and has not been independently audited for conformance.
