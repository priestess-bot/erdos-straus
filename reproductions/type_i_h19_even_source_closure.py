#!/usr/bin/env python3
"""Audit the 1B H19 source-free residuals with the Type I even-source selector."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
H19 = ROOT / "reproductions" / "type-ii-source-free-transition-h19-1b-results.json"
EVEN_SELECTOR = ROOT / "reproductions" / "type_i_tail_reverse_even_source_closure.py"
DEFAULT_GAP_CAP = 215
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-h19-even-source-closure-1b-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


even_selector = load_module("h19_even_source_selector", EVEN_SELECTOR)


def run_audit(h19: dict[str, object], gap_cap: int = DEFAULT_GAP_CAP) -> dict[str, object]:
    if gap_cap < 3 or gap_cap % 4 != 3:
        raise ValueError("gap_cap must be at least 3 and congruent to 3 modulo 4")
    primes = [int(profile["prime"]) for profile in h19["profiles"]]
    records: list[dict[str, object]] = []
    misses: list[int] = []
    forms = 0
    lifts = 0
    for prime in primes:
        witness, local_forms, local_lifts = even_selector.first_even_source_edge(prime, gap_cap)
        forms += local_forms
        lifts += local_lifts
        if witness is None:
            misses.append(prime)
        else:
            records.append({"prime": prime, **witness})
    gap_histogram: dict[str, int] = {}
    for record in records:
        gap = str(record["gap"])
        gap_histogram[gap] = gap_histogram.get(gap, 0) + 1
    return {
        "arithmetic": (
            "for every stored 1B H19 source-free residual, enumerate Type I normal certificates "
            "with m=3 (mod 4) through gap_cap and all strict maximum-tail reverse lifts; select "
            "the first even source and verify source and target identities exactly"
        ),
        "scope_note": (
            "A finite audit on the H19 source-free residual subset, independent of the 500M "
            "ordinary-tail input. It is not a closure for every core prime through 1B."
        ),
        "prime_limit": h19["prime_limit"],
        "h19_source_free_count": len(primes),
        "gap_cap": gap_cap,
        "even_source_captured_count": len(records),
        "even_source_misses": misses,
        "normal_forms_checked_until_first_even_source_or_exhaustion": forms,
        "strict_reverse_lifts_checked_until_first_even_source_or_exhaustion": lifts,
        "maximum_selected_gap": max((int(record["gap"]) for record in records), default=None),
        "first_even_source_gap_histogram": dict(
            sorted(gap_histogram.items(), key=lambda item: int(item[0]))
        ),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--h19", type=Path, default=H19)
    parser.add_argument("--gap-cap", type=int, default=DEFAULT_GAP_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.h19.read_text(encoding="utf-8")), args.gap_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
