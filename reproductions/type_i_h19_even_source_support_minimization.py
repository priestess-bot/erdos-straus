#!/usr/bin/env python3
"""Minimize Type I even-bridge support on the 1B H19 source-free residuals."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
H19 = ROOT / "reproductions" / "type-ii-source-free-transition-h19-1b-results.json"
SUPPORT_MIN = ROOT / "reproductions" / "type_i_tail_reverse_even_source_support_minimization.py"
DEFAULT_GAP_CAP = 215
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-h19-even-source-support-min-1b-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


support_min = load_module("h19_even_source_support_min", SUPPORT_MIN)


def run_audit(h19: dict[str, object], gap_cap: int = DEFAULT_GAP_CAP) -> dict[str, object]:
    """Exhaustively minimize bridge support for every stored H19 residual."""
    if gap_cap < 3 or gap_cap % 4 != 3:
        raise ValueError("gap_cap must be at least 3 and congruent to 3 modulo 4")
    records: list[dict[str, object]] = []
    misses: list[int] = []
    forms = 0
    lifts = 0
    for profile in h19["profiles"]:
        prime = int(profile["prime"])
        witness, local_forms, local_lifts = support_min.least_support_edge(prime, gap_cap)
        forms += local_forms
        lifts += local_lifts
        if witness is None:
            misses.append(prime)
        else:
            records.append({"prime": prime, "selected_edge": witness})
    support_histogram = Counter(
        str(record["selected_edge"]["E_prime_support_count"]) for record in records
    )
    exponent_histogram = Counter(
        str(record["selected_edge"]["E_exponent_count"]) for record in records
    )
    return {
        "arithmetic": (
            "for every stored 1B H19 source-free residual, enumerate every Type I normal form "
            "and strict maximum-tail reverse lift through gap_cap; retain even-source lifts and "
            "minimize the bridge factor E by (prime support, exponent count, value, B, gap, source)"
        ),
        "scope_note": (
            "An exhaustive finite complexity profile of the target-side even-source selector on "
            "the independent H19 source-free residual subset. It does not prove a global support bound."
        ),
        "prime_limit": h19["prime_limit"],
        "h19_source_free_count": len(h19["profiles"]),
        "gap_cap": gap_cap,
        "captured_count": len(records),
        "misses": misses,
        "normal_forms_exhaustively_checked": forms,
        "strict_reverse_lifts_exhaustively_checked": lifts,
        "least_E_support_histogram": dict(
            sorted(support_histogram.items(), key=lambda item: int(item[0]))
        ),
        "least_E_exponent_histogram": dict(
            sorted(exponent_histogram.items(), key=lambda item: int(item[0]))
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
