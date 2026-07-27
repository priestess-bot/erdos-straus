#!/usr/bin/env python3
"""Measure the fixed n=p-m Type I even-bridge branch on 500M tail misses."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TAIL = ROOT / "reproductions" / "type-ii-tail-deflation-500m-full-results.json"
LANDSCAPE = ROOT / "reproductions" / "boundary_gap_certificate_landscape.py"
DEFAULT_GAP_CAP = 215
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-normal-gap-source-even-bridge-500m-results.json"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


landscape = load_module("normal_gap_source_landscape", LANDSCAPE)
bridge = load_module(
    "normal_gap_source_bridge",
    ROOT / "reproductions" / "type_i_normal_gap_source_even_bridge.py",
)


def first_gap_source_witness(prime: int, gap_cap: int) -> tuple[dict[str, object] | None, int]:
    """Exhaust every stated normal form and retain the first n=p-m hit."""
    witness: dict[str, object] | None = None
    forms = 0
    for gap in range(3, gap_cap + 1, 4):
        for entry in landscape.gap_landscape(prime, gap)["type_i"]:
            A, B, C = (int(value) for value in entry["normal_form"])
            forms += 1
            candidate = bridge.gap_source_even_bridge(prime, gap, A, B, C)
            if candidate is not None and witness is None:
                witness = {
                    "gap": gap,
                    "normal_form": [A, B, C],
                    **candidate,
                }
    return witness, forms


def run_audit(tail: dict[str, object], gap_cap: int = DEFAULT_GAP_CAP) -> dict[str, object]:
    """Run the complete capped audit on the supplied ordinary-tail miss list."""
    if gap_cap < 3 or gap_cap % 4 != 3:
        raise ValueError("gap_cap must be at least 3 and congruent to 3 modulo 4")
    records: list[dict[str, object]] = []
    misses: list[int] = []
    forms = 0
    for entry in tail["misses"]:
        prime = int(entry["prime"])
        witness, local_forms = first_gap_source_witness(prime, gap_cap)
        forms += local_forms
        if witness is None:
            misses.append(prime)
        else:
            records.append({"prime": prime, "witness": witness})
    gap_histogram: dict[str, int] = {}
    for record in records:
        gap = str(record["witness"]["gap"])
        gap_histogram[gap] = gap_histogram.get(gap, 0) + 1
    return {
        "arithmetic": (
            "for every stored ordinary Type II p-1-tail miss, enumerate every Type I "
            "normal form through gap_cap, apply the exact n=p-m gap-source square "
            "criterion, and verify the source and target unit-fraction identities"
        ),
        "scope_note": (
            "A complete finite audit of the fixed source-distance n=p-m subbranch. "
            "Its misses may still have another source distance, another Type I bridge, "
            "or a Type II terminal certificate."
        ),
        "input_tail_audit": TAIL.name,
        "prime_limit": tail["prime_limit"],
        "ordinary_tail_miss_count": len(tail["misses"]),
        "gap_cap": gap_cap,
        "gap_source_captured_count": len(records),
        "gap_source_misses": misses,
        "normal_forms_exhaustively_checked": forms,
        "maximum_selected_gap": max(
            (int(record["witness"]["gap"]) for record in records), default=None
        ),
        "first_gap_source_gap_histogram": dict(
            sorted(gap_histogram.items(), key=lambda item: int(item[0]))
        ),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tail", type=Path, default=TAIL)
    parser.add_argument("--gap-cap", type=int, default=DEFAULT_GAP_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.tail.read_text(encoding="utf-8")), args.gap_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
