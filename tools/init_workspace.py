#!/usr/bin/env python3
"""Create a private Sapiens OS workspace: a plain local folder of Markdown files.

Works offline, uses only the standard library, and sends nothing anywhere.
It never overwrites an existing file, and refuses to create the workspace
inside the framework folder (public repository or plugin install), because
personal notes must not live where they can be published or replaced by an update.

Usage:
    python3 tools/init_workspace.py [FOLDER] [--dry-run] [--git]

FOLDER defaults to ~/sapiens-os-private.
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "templates" / "workspace"
FILES = ("CLAUDE.md", "profile.md", "experiments.md")
DIRS = ("check-ins", "reviews", "exports")
PURPOSE = {
    "CLAUDE.md": "standing rules the AI reads when you open this folder",
    "profile.md": "your reviewable operating note, starts blank",
    "experiments.md": "small experiments with review dates and stop conditions",
    "check-ins": "dated check-in notes, only if you want them saved",
    "reviews": "quarterly reviews",
    "exports": "files you download from the local dashboard",
}


def inside(child: Path, parent: Path) -> bool:
    try:
        child.relative_to(parent)
        return True
    except ValueError:
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("folder", nargs="?", default="~/sapiens-os-private")
    parser.add_argument("--dry-run", action="store_true", help="show what would be created and change nothing")
    parser.add_argument("--git", action="store_true", help="also run git init (local only, no remote)")
    args = parser.parse_args()

    target = Path(args.folder).expanduser().resolve()
    if inside(target, ROOT) or inside(ROOT, target):
        print(f"Refusing: {target} overlaps the framework folder {ROOT}.", file=sys.stderr)
        print("Choose a folder outside it, for example ~/sapiens-os-private.", file=sys.stderr)
        return 2
    missing = [f for f in FILES if not (TEMPLATES / f).is_file()]
    if missing:
        print(f"Missing template files in {TEMPLATES}: {', '.join(missing)}", file=sys.stderr)
        return 1

    plan = []
    for name in FILES:
        plan.append(("file", name, (target / name).exists()))
    for name in DIRS:
        plan.append(("dir", name, (target / name).exists()))

    verb = "Would create" if args.dry_run else "Creating"
    print(f"{verb} a private workspace at {target}")
    for kind, name, exists in plan:
        status = "keep (already there)" if exists else "create"
        print(f"  {status:22} {name}{'/' if kind == 'dir' else ''}: {PURPOSE[name]}")

    if args.dry_run:
        print("Dry run only. Nothing was written.")
        return 0

    target.mkdir(parents=True, exist_ok=True)
    for kind, name, exists in plan:
        if exists:
            continue
        if kind == "file":
            shutil.copyfile(TEMPLATES / name, target / name)
        else:
            (target / name).mkdir()
            (target / name / ".gitkeep").touch()

    if args.git and not (target / ".git").exists():
        if shutil.which("git"):
            subprocess.run(["git", "init", "-q", str(target)], check=False)
            print("Ran git init (local only). Add a remote only if it is private.")
        else:
            print("git was not found, so no repository was created.")

    print()
    print("Done. To use it, open your AI assistant in that folder and start with /sapiens-os:start.")
    print("If you ever push this folder to a remote, make the remote private first.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
