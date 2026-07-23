#!/usr/bin/env python3
"""Create missing Markdown paper cards from the reviewed seed manifest."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SEED = ROOT / "data" / "paper-seed.yaml"
DESTINATION = ROOT / "papers"


def render(entry: dict) -> str:
    body_fields = {
        "summary": entry.pop("summary"),
        "contributions": entry.pop("contributions"),
        "limits": entry.pop("limits"),
        "evidence": entry.pop("evidence"),
    }
    frontmatter = yaml.safe_dump(
        entry,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
        width=1000,
    ).strip()
    contributions = "\n".join(f"- {item}" for item in body_fields["contributions"])
    evidence = "\n".join(f"- {item}" for item in body_fields["evidence"])
    return f"""---
{frontmatter}
---

# {entry['title']}

## 定位

{body_fields['summary']}

## 主要贡献

{contributions}

## 证据与核查

{evidence}

## 局限与后续

{body_fields['limits']}
"""


def main() -> int:
    payload = yaml.safe_load(SEED.read_text(encoding="utf-8"))
    entries = payload.get("papers", [])
    DESTINATION.mkdir(parents=True, exist_ok=True)
    created = 0
    skipped = 0
    for raw in entries:
        entry = dict(raw)
        key = entry["citation_key"]
        path = DESTINATION / f"{key}.md"
        if path.exists():
            skipped += 1
            continue
        path.write_text(render(entry), encoding="utf-8")
        created += 1
    print(f"created={created} skipped={skipped} manifest={len(entries)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
