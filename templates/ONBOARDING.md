# Private onboarding interview

AI: ask conversationally in small batches. Say that every question is optional. Do not put completed answers in this public repository.

Begin by asking which language(s) the person wants for the interview, summaries, dashboard/reports and reminders, using [LANGUAGE.md](../docs/LANGUAGE.md). Follow their answer throughout the interview; do not assume that English documentation implies an English conversation. They can switch languages at any time.

## Consent and context

1. What would you like this system to help you notice or change? What should it never optimize at your expense?
2. What does a good week feel like for you? What are your priorities, responsibilities, constraints, access needs, and financial/work pressures?
3. Do you want a brief or detailed interview? What information may be remembered, where, for how long, and who can see it? Are there topics or data sources to exclude? Do you want a calendar reminder you set yourself?
4. Is there current professional care, a plan for symptoms, or an urgent concern you want to disclose? You may leave this blank; the AI does not need diagnoses or records.

5. Where will these instructions live in your AI environment? Do you want **on-demand** use only, or may the AI occasionally offer the framework in relevant conversations (**contextual**)? You can pause, disable or request removal at any time. What topics, times, devices, people, or connected services are out of scope?
6. What does a typical day and week look like for you, and how does it change across seasons, work schedules, travel, caregiving or other rhythms? Which observations feel stable, which are uncertain, and when should we check again? No answer should become a permanent assumption.

## Ten domains (ask each, and allow `skip`)

For **each** domain, ask: “How has this been for you over the last few weeks? What works, what is difficult, what changed, how does it affect daily life, and what would you like to be different?” Then use one or two prompts below only if helpful.

1. **Sleep:** time available, regularity, refreshment, daytime sleepiness, obstacles.
2. **Nutrition:** reliable food access, variety, regular meals, restrictions by choice or necessity, difficulties.
3. **Movement:** daily movement, strength/activity you enjoy, limitations or symptoms, recovery.
4. **Stress:** demands, perceived load, coping, work context, what is within your control.
5. **Social connection:** supportive people, belonging, boundaries, loneliness if relevant.
6. **Light/dark:** outdoor time and daylight, evening environment, shift work/travel.
7. **Agency:** choices, workload control, ability to change conditions or seek help.
8. **Meaning:** values, roles, purpose, conflicts or uncertainty.
9. **Rest:** breaks, unscheduled time, leisure, recovery and actual reduction in demands.
10. **Curiosity:** play, learning, exploration, room for novelty without pressure.

## Operating context (optional)

Only if the person wants the [operator pack](../operator/README.md): ask the operating-context questions listed there (what they run or look after, decisions only they can make, where attention fragments, what cannot change now, what they would stop, what enough looks like). Mark skipped items `unknown` and keep answers in the private note.

## Close and confirm

Ask: “What is the one constraint that affects several areas? Which small change is worth trying? What could make it harmful or impractical? When shall we review it?” Summarize all ten with `unknown` where skipped. Include strengths, contextual barriers, no more than two user-chosen experiments, review date, and circumstances that warrant professional help. Ask the person to correct and approve the summary before saving. Then offer a choice: no dashboard, simple paper/notes view, or the private local dashboard described in `docs/DASHBOARD.md`. Ask what one to three signals they actually want to see, whether device exports or cycle context are relevant, and what data can be retained. If chosen, offer a reviewable JSON profile in the structure of `examples/sample-profile.json`, with only consented summaries; guide them through `dashboard/README.md` and check that all ten domains show an honest baseline or `unknown`.

Show a short, editable personal operating note: selected mode, language preferences by output, priorities, lived rhythms and cue windows, domain observations, unknowns, exclusions, data source permissions, reminder limits, and the AI surfaces where the note may be used. Obtain approval before saving and create/update the private [installation record](INSTALLATION-RECORD.md) with *locations*, not sensitive answers. Explain the pause/disable/removal choices in [LIFECYCLE.md](../docs/LIFECYCLE.md).
