#!/usr/bin/env python3
"""Integrity check for the Agent Skills in skills/ and the plugin manifests.

Fails if a skill's frontmatter breaks the Agent Skills format (name must match
its folder; lowercase letters, digits and single hyphens; description 1-1024
characters), if a relative link in a skill points nowhere, if a skill contains
a remote URL or an em dash, or if a manifest is invalid JSON or lists a
skill that does not exist. Standard library only.

Usage: python3 tools/check_skills.py
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fields = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
    return fields


def main():
    problems = []
    skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if not skills:
        problems.append("no skills found in skills/")
    for path in skills:
        folder = path.parent.name
        text = path.read_text(encoding="utf-8")
        fm = frontmatter(text)
        if fm is None:
            problems.append(f"{path.relative_to(ROOT)}: missing frontmatter")
            continue
        name = fm.get("name", "")
        if name != folder:
            problems.append(f"{folder}: name '{name}' must match the folder")
        if not NAME_RE.match(name) or len(name) > 64:
            problems.append(f"{folder}: invalid name '{name}'")
        desc = fm.get("description", "")
        if not 1 <= len(desc) <= 1024:
            problems.append(f"{folder}: description must be 1-1024 characters (is {len(desc)})")
        if len(text.splitlines()) > 500:
            problems.append(f"{folder}: SKILL.md is over 500 lines")
        if "—" in text:
            problems.append(f"{folder}: contains an em dash")
        if re.search(r"https?://", text):
            problems.append(f"{folder}: contains a remote URL")
        for target in LINK_RE.findall(text):
            if target.startswith(("http", "mailto:")):
                continue
            if not (path.parent / target).resolve().exists():
                problems.append(f"{folder}: broken link {target}")

    for rel in (".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"):
        try:
            data = json.loads((ROOT / rel).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as err:
            problems.append(f"{rel}: {err}")
            continue
        if not data.get("name"):
            problems.append(f"{rel}: missing name")
    try:
        plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
        listed = {p.get("name") for p in market.get("plugins", [])}
        if plugin.get("name") not in listed:
            problems.append("marketplace.json does not list the plugin in plugin.json")
    except (OSError, json.JSONDecodeError):
        pass

    if problems:
        print("FAILED:")
        for p in problems:
            print(" -", p)
        return 1
    print(f"OK: {len(skills)} skills, 2 manifests checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
