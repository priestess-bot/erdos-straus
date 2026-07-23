#!/usr/bin/env python3
"""Create missing claim and concept cards from the reviewed knowledge seed."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SEED = ROOT / "data" / "knowledge-seed.yaml"


def render_claim(entry: dict) -> str:
    analysis = entry.pop("analysis")
    caveats = entry.pop("caveats")
    evidence = entry.pop("evidence")
    frontmatter = yaml.safe_dump(entry, allow_unicode=True, sort_keys=False, width=1000).strip()
    evidence_text = "\n".join(f"- {item}" for item in evidence)
    return f"""---
{frontmatter}
---

# {entry['title']}

## 结论

{entry['statement']}

## 推理与来源

{analysis}

{evidence_text}

## 边界

{caveats}
"""


def render_concept(entry: dict) -> str:
    explanation = entry.pop("explanation")
    pitfalls = entry.pop("pitfalls")
    frontmatter = yaml.safe_dump(entry, allow_unicode=True, sort_keys=False, width=1000).strip()
    pitfalls_text = "\n".join(f"- {item}" for item in pitfalls)
    return f"""---
{frontmatter}
---

# {entry['title']}

{entry['summary']}

## 数学说明

{explanation}

## 常见误读

{pitfalls_text}
"""


def main() -> int:
    payload = yaml.safe_load(SEED.read_text(encoding="utf-8"))
    created = skipped = 0
    for kind, plural, renderer in (
        ("claim", "claims", render_claim),
        ("concept", "concepts", render_concept),
    ):
        destination = ROOT / plural
        destination.mkdir(parents=True, exist_ok=True)
        for raw in payload.get(plural, []):
            entry = dict(raw)
            key = entry[f"{kind}_id"]
            path = destination / f"{key}.md"
            if path.exists():
                skipped += 1
                continue
            path.write_text(renderer(entry), encoding="utf-8")
            created += 1
    print(f"created={created} skipped={skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
