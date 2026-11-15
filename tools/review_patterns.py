#!/usr/bin/env python3
"""Offline discussion cues from explicitly provided, private self-reports.

No background monitoring, notifications, diagnosis, or clinical thresholds.
Usage: python3 tools/review_patterns.py examples/sample-check-ins.json
"""

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

DOMAINS = (
    "Sleep", "Nutrition", "Movement", "Stress", "Social connection",
    "Light/dark rhythms", "Agency", "Meaning", "Rest", "Curiosity",
)
STATUSES = {"supportive", "mixed", "difficult", "unknown"}


def read_private_input(path):
    if path.stat().st_size > 1_000_000:
        raise ValueError("Input exceeds 1 MB; provide a smaller private review file")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Input must be an object")
    if data.get("schema") != "sapiens-os-check-ins-v1":
        raise ValueError("Unsupported schema")
    watch = data.get("watch_domains", [])
    if not isinstance(watch, list) or any(not isinstance(d, str) or d not in DOMAINS for d in watch):
        raise ValueError("watch_domains must contain valid domain names")
    check_ins = data.get("check_ins", [])
    if not isinstance(check_ins, list) or len(check_ins) > 1000:
        raise ValueError("check_ins must be a list of at most 1000 entries")
    result = []
    for row in check_ins:
        if not isinstance(row, dict) or not isinstance(row.get("domains"), dict):
            raise ValueError("Each check-in needs a domains object")
        if not isinstance(row.get("date"), str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", row["date"]):
            raise ValueError("Use a valid YYYY-MM-DD date")
        try:
            date = dt.date.fromisoformat(row["date"])
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError("Use a valid YYYY-MM-DD date") from exc
        if any(k not in DOMAINS or not isinstance(v, str) or v not in STATUSES
               for k, v in row["domains"].items()):
            raise ValueError("Use only supported domain labels and statuses")
        result.append((date, row["domains"]))
    return sorted(result, key=lambda r: r[0]), list(dict.fromkeys(watch))


def review(rows, watch):
    cues = []
    for domain in watch:
        observed = [(date, states[domain]) for date, states in rows
                    if domain in states and states[domain] != "unknown"]
        if len(observed) < 2:
            continue
        (before, first), (recent, second) = observed[-2:]
        if first == second == "difficult" and 0 < (recent - before).days <= 42:
            cues.append({
                "domain": domain,
                "observation": "Two supplied check-ins described this area as difficult",
                "dates": [before.isoformat(), recent.isoformat()],
                "question": "Does this still fit, what changed, and would support or a reduction in demands help?",
                "limits": "Self-report discussion cue only; not a diagnosis, risk score, or safety alert",
            })
    return {
        "schema": "sapiens-os-review-v1",
        "source": "explicitly supplied self-report file",
        "latest_check_in": rows[-1][0].isoformat() if rows else None,
        "check_ins_supplied": len(rows),
        "watch_domains": watch,
        "cues": cues,
        "note": "Missing and unselected areas were not assessed. Ask the person for context; urgent disclosed concerns follow the safety guide immediately.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="Private JSON file or fictional sample")
    args = parser.parse_args()
    try:
        result = review(*read_private_input(args.file))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
    print()


if __name__ == "__main__":
    main()
