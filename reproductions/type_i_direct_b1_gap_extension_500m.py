#!/usr/bin/env python3
"""Extend the direct B=1 even-source audit on the stored 500M tail profile.

The direct target audit closes the profile through m<=215 using B in {1,2,8}.
This script first recomputes its B=1 stage, then exhaustively scans the four
remaining targets for their first B=1 normal form with a strict even source
through the stated larger gap bound.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TAIL = ROOT / "reproductions" / "type-i-tail-reverse-even-source-support-min-500m-results.json"
DIRECT = ROOT / "reproductions" / "type_i_direct_small_b_even_source_audit.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-direct-b1-gap-extension-500m-results.json"
DIRECT_GAP_CAP = 215
GAP_CAP = 999


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


direct = load_module("direct_b1_extension_direct", DIRECT)


def first_b_one_even_source(prime: int, gap_cap: int = GAP_CAP) -> dict[str, object] | None:
    """Return the first B=1 normal reverse edge with an exact strict even source."""
    for gap in range(3, gap_cap + 1, 4):
        for entry in direct.support_min.landscape.gap_landscape(prime, gap)["type_i"]:
            A, B, C = (int(value) for value in entry["normal_form"])
            if B != 1:
                continue
            _, lifts = direct.support_min.bridge.type_i_normal_reverse_two_tail_lifts(
                prime, gap, A, B, C
            )
            for lift in lifts:
                source = int(lift["source_denominator"])
                if source % 2:
                    continue
                return {
                    "gap": gap,
                    "normal_form": [A, B, C],
                    "source_denominator": source,
                    "source_term": int(lift["source_term"]),
                    "bridge_factor": int(lift["bridge_divisor"]) // (prime * prime),
                }
    return None


def run_audit(tail: dict[str, object], gap_cap: int = GAP_CAP) -> dict[str, object]:
    """Close the stored tail profile using B=1 alone through ``gap_cap``."""
    if gap_cap < DIRECT_GAP_CAP or gap_cap % 4 != 3:
        raise ValueError("gap_cap must be at least 215 and congruent to 3 modulo 4")
    primes = [int(record["prime"]) for record in tail["records"]]
    if len(primes) != 1717:
        raise AssertionError("input does not match the stored 500M bridge profile")

    direct_stage = direct.staged_audit(primes, [1], "tail-500M-direct-B1")
    if direct_stage["maximum_selected_gap"] != DIRECT_GAP_CAP:
        raise AssertionError("the direct B=1 cutoff changed")
    residuals = [int(prime) for prime in direct_stage["misses"]]
    extensions = []
    for prime in residuals:
        witness = first_b_one_even_source(prime, gap_cap)
        if witness is None:
            raise AssertionError(f"B=1 extension missed {prime}")
        if int(witness["gap"]) <= DIRECT_GAP_CAP:
            raise AssertionError("residual had an earlier direct B=1 edge")
        extensions.append({"prime": prime, "witness": witness})

    return {
        "arithmetic": (
            "recompute the complete direct target B=1 maximum-tail even-source stage through m<=215; "
            "for precisely its residual targets, enumerate every Type I normal form with B=1 through "
            "m<=999 and every maximum-tail reverse lift, retaining exact strict even sources"
        ),
        "scope_note": (
            "This is a complete finite audit of the stored 1,717-target 500M tail profile. "
            "It supplies neither a uniform gap bound nor a global selector for arbitrary core primes."
        ),
        "input_count": len(primes),
        "direct_gap_cap": DIRECT_GAP_CAP,
        "gap_cap": gap_cap,
        "direct_b_one_count": direct_stage["captured_count"],
        "extended_b_one_count": len(extensions),
        "residuals": residuals,
        "extensions": extensions,
        "misses": [],
        "maximum_selected_gap": max(
            [int(record["witness"]["gap"]) for record in extensions]
            + [int(direct_stage["maximum_selected_gap"])]
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tail", type=Path, default=TAIL)
    parser.add_argument("--gap-cap", type=int, default=GAP_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(json.loads(args.tail.read_text(encoding="utf-8")), args.gap_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
