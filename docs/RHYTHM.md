# A rhythm that is real

Sapiens OS framework developed by **Vladislav (Vlad) Andreev**. © 2026 Vladislav Andreev. MIT-licensed original code and text; brand assets excepted.

A chat or a repository cannot remind you, check on you or send an alert. Anything that feels like a rhythm has to be set up by you, in a tool you control, and that tool then prompts you to open a session. None of the options below runs an AI by itself, and none is required. The default is no reminder at all.

## What is worth a rhythm

Keep it to what you could run for six months. More is not better.

| What | How often | Where it comes from |
| --- | --- | --- |
| A short check-in (`/sapiens-os:checkin`) | Weekly, optional | [WEEKLY-CHECK-IN.md](../templates/WEEKLY-CHECK-IN.md) |
| A review (`/sapiens-os:review`) | About every three months | [QUARTERLY-REVIEW.md](../templates/QUARTERLY-REVIEW.md) |
| The current experiment's review date | Once, two weeks or less out | the date you agreed in `experiments.md` |

## Options you can set up

1. **A calendar event you create.** Name it neutrally (for example "Check-in, if I want one"), set the repeat yourself, and confirm the notification fires once. The [habit tracker](../habits/README.md) can download an `.ics` file with a neutral title for this. A calendar may handle repeating and floating times differently, and a new download does not cancel an earlier import.
2. **Your phone's reminder app.** The same idea, with no file to import.
3. **A review date inside `experiments.md`.** The AI can ask about it when you open a session. It cannot start the session itself.

## If your AI agent offers scheduled runs

Treat each scheduled run as its own consent, and check three things before you give it anything private:

- **What it can reach.** A scheduled run in someone else's cloud typically cannot see files on your machine, and a local one sees whatever the folder holds. Confirm which before you use it with your workspace.
- **What it will do on its own.** A scheduled run that writes to files or sends messages needs a clear, separate yes. A run that only prepares a draft for you to read is much safer.
- **How to stop it.** Know where to cancel it before you start it. Removal is described in [LIFECYCLE.md](LIFECYCLE.md).

An unread reminder is not a lapse and does not need an apology. When you are ready to return, use `/sapiens-os:return`.
