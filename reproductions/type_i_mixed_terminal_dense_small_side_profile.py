#!/usr/bin/env python3
"""Audit small-side Type I terminal bridges on the dense 500M--600M interval.

The dense mixed-terminal audit stores the first even Type I reverse lift for
each ordinary Type II tail miss.  This script first verifies those witnesses.
When a stored witness is a large-side divisor ratio E/(2K)=a/b with a>b, it
exhausts the same Type I normal-form box and releases the point only through a
replacement small-side bridge a<b.  Small-side bridges have source n in the
upper half of the target interval, so this is a deliberately stronger finite
audit than the underlying mixed-terminal closure.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-mixed-terminal-dense-500m-600m-results.json"
ALTERNATIVE = ROOT / "reproductions" / "type_i_tail_reverse_even_source_small_side_alternative_profile.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-mixed-terminal-dense-small-side-profile-500m-600m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


alternative = load_module("dense_small_side_alternative", ALTERNATIVE)


def verified_selected_bridge(record: dict[str, object]) -> dict[str, object]:
    """Rebuild one stored terminal bridge and classify its reduced pair."""
    prime = int(record["prime"])
    witness = record["type_i_even_witness"]
    if not isinstance(witness, dict):
        raise AssertionError("stored witness must be an object")
    gap = int(witness["gap"])
    A, B, C = (int(value) for value in witness["normal_form"])
    R = (4 * B * B * C + 1) // gap
    H = A * R - B
    K = B * C * H
    L = 2 * K
    lift = witness["reverse_two_tail_lift"]
    if not isinstance(lift, dict):
        raise AssertionError("stored reverse lift must be an object")
    bridge_divisor = int(lift["bridge_divisor"])
    if bridge_divisor % (prime * prime):
        raise AssertionError("stored bridge divisor did not yield an integral E")
    E = bridge_divisor // (prime * prime)
    source = int(lift["source_denominator"])
    divisor_gcd = math.gcd(E, L)
    a, b = E // divisor_gcd, L // divisor_gcd

    if gap * R != 4 * B * B * C + 1 or 4 * K != prime * R + 1:
        raise AssertionError("stored Type I normal form did not reconstruct")
    if (
        math.gcd(a, b) != 1
        or L % a
        or L % b
        or (a - 2 * b) % R
        or E != L * a // b
        or E % 2
        or E > 2 * L - 2 * R
        or source % 2
    ):
        raise AssertionError("stored bridge failed exact terminal conditions")
    target_solution = tuple(int(value) for value in witness["target_solution"])
    source_solution = tuple(int(value) for value in witness["source_solution"])
    if Fraction(4, prime) != sum((Fraction(1, value) for value in target_solution), Fraction()):
        raise AssertionError("stored target identity failed")
    if Fraction(4, source) != sum((Fraction(1, value) for value in source_solution), Fraction()):
        raise AssertionError("stored source identity failed")
    if a == b:
        raise AssertionError("a Type I normal bridge cannot have a=b")
    upper_half = 2 * source >= prime + 1
    if upper_half != (a < b):
        raise AssertionError("small-side and upper-half source conditions disagreed")
    return {
        "gap": gap,
        "normal_form": [A, B, C],
        "R": R,
        "K": K,
        "E": E,
        "a": a,
        "b": b,
        "source_denominator": source,
        "upper_half_source": upper_half,
    }


def run_profile(dense_audit: dict[str, object]) -> dict[str, object]:
    """Classify stored bridges and exhaust replacements for its large-side records."""
    gap_cap = int(dense_audit["type_i_gap_cap"])
    selected_small = 0
    selected_large = 0
    alternative_forms = 0
    alternative_lifts = 0
    alternative_records: list[dict[str, object]] = []
    misses: list[int] = []

    records = dense_audit["type_i_even_terminal_bridge_records"]
    if not isinstance(records, list):
        raise AssertionError("dense audit records must be a list")
    for record in records:
        if not isinstance(record, dict):
            raise AssertionError("dense audit entry must be an object")
        prime = int(record["prime"])
        selected = verified_selected_bridge(record)
        if bool(selected["upper_half_source"]):
            selected_small += 1
            continue
        selected_large += 1
        replacement, forms, lifts = alternative.least_small_side_edge(prime, gap_cap)
        alternative_forms += forms
        alternative_lifts += lifts
        if replacement is None:
            misses.append(prime)
            continue
        replacement_source = int(replacement["source_denominator"])
        if 2 * replacement_source < prime + 1:
            raise AssertionError("replacement small-side bridge was not upper-half")
        alternative_records.append(
            {
                "prime": prime,
                "selected_large_side": selected,
                "alternative_small_side": replacement,
            }
        )

    bridge_count = int(dense_audit["type_i_even_terminal_bridge_count"])
    if selected_small + selected_large != bridge_count:
        raise AssertionError("stored bridge classifications did not partition the dense audit")
    if selected_small + len(alternative_records) + len(misses) != bridge_count:
        raise AssertionError("replacement search did not partition the dense audit")
    return {
        "arithmetic": (
            "reconstruct every stored Type I terminal bridge exactly; reduce E/(2K)=a/b; and for "
            "each selected large-side a>b bridge exhaust all Type I normal forms and strict even-source "
            "reverse lifts through the dense audit's gap cap, retaining a<b replacements"
        ),
        "scope_note": (
            "A finite strengthening of the 500M--600M dense mixed-terminal audit. A small-side bridge "
            "is equivalent here to an even source in the upper half of the target range. The result "
            "does not establish a uniform normal-form bound or the global mixed selector."
        ),
        "input_artifact": INPUT.name,
        "prime_interval": dense_audit["prime_interval"],
        "gap_cap": gap_cap,
        "type_i_terminal_bridge_count": bridge_count,
        "selected_small_side_count": selected_small,
        "selected_large_side_count": selected_large,
        "alternative_small_side_captured_count": len(alternative_records),
        "small_side_misses": misses,
        "combined_small_side_closure_count": selected_small + len(alternative_records),
        "alternative_normal_forms_exhaustively_checked": alternative_forms,
        "alternative_strict_reverse_lifts_exhaustively_checked": alternative_lifts,
        "alternative_records": alternative_records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_profile(json.loads(args.input.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "alternative_records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
