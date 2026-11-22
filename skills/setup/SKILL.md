---
name: setup
description: Create the person's private Sapiens OS workspace, a local folder they own, so notes, check-ins and reviews persist between sessions. Use only when the person asks to set up, install or save their Sapiens OS notes.
disable-model-invocation: true
compatibility: Designed for Claude Code. Needs Python 3 on the machine. Works offline and sends nothing anywhere.
license: MIT
---

# Setup: a private workspace you own

Read AGENTS.md first (`${CLAUDE_PLUGIN_ROOT}/AGENTS.md` in a plugin install, otherwise the repository root).

Why a separate folder: a plugin folder is replaced when the plugin updates, and the public repository must never hold personal notes. The workspace is a plain folder of Markdown files. The person can read, edit, move or delete it.

## Steps

1. **Ask where.** Suggest `~/sapiens-os-private`. Any location outside the plugin and outside this repository is fine.
2. **Dry run first.** Run `python3 "${CLAUDE_PLUGIN_ROOT}/tools/init_workspace.py" <folder> --dry-run` (from a repository clone: `python3 tools/init_workspace.py <folder> --dry-run`). Show the output and say what each file is for.
3. **Create it on a yes.** Run the same command without `--dry-run`. It never overwrites an existing file. Add `--git` only if the person wants a local git repository.
4. **Explain the three things that matter.**
   - To use it, open Claude Code in that folder. Its CLAUDE.md carries the standing rules.
   - If they ever push the folder to a remote, the remote must be private, and they should know what their notes contain first.
   - To remove everything: delete the folder, then uninstall the plugin. See [docs/LIFECYCLE.md](../../docs/LIFECYCLE.md).
5. **Do not fill anything in yet.** Offer `/sapiens-os:start` as the next step.

## Boundaries

- Do not create reminders or scheduled jobs here. Use [docs/RHYTHM.md](../../docs/RHYTHM.md) and ask separately.
- Do not copy anything from the person's other files or chat history into the workspace without asking and naming the source.
