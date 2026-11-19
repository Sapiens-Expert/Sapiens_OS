#!/usr/bin/env python3
"""Integrity check for the behavioral science library.

Fails if a reference id used in docs/science/*.md is missing from references.json,
if a reference is never used, if a module lacks an evidence tag or a
"When not to use" section, or if a reference entry misses a required field.

Usage: python3 tools/check_references.py
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = ("id", "authors", "year", "venue", "title", "design", "url")
ID_RE = re.compile(r"\bR(\d{2})\b")


def main():
    problems = []
    data = json.loads((ROOT / "references.json").read_text(encoding="utf-8"))
    refs = data.get("references", [])
    ids = set()
    for entry in refs:
        for key in REQUIRED:
            if not entry.get(key):
                problems.append(f"reference {entry.get('id', '?')} missing field: {key}")
        if entry.get("id") in ids:
            problems.append(f"duplicate reference id: {entry.get('id')}")
        ids.add(entry.get("id"))

    used = set()
    modules = sorted((ROOT / "docs" / "science").glob("*.md"))
    for path in modules:
        text = path.read_text(encoding="utf-8")
        found = {f"R{m}" for m in ID_RE.findall(text)}
        used |= found
        for ref in sorted(found - ids):
            problems.append(f"{path.name}: cites {ref}, not in references.json")
        if path.name != "README.md":
            if "Evidence tag" not in text:
                problems.append(f"{path.name}: no 'Evidence tag'")
            if "When not to use" not in text:
                problems.append(f"{path.name}: no 'When not to use' section")
            if "—" in text:
                problems.append(f"{path.name}: contains an em dash")
    for ref in sorted(ids - used):
        problems.append(f"{ref} is in references.json but never cited")

    if problems:
        print("FAIL")
        for p in problems:
            print(" -", p)
        return 1
    print(f"OK: {len(refs)} references, {len(modules)} files checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
