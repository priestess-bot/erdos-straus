#!/usr/bin/env python3
"""Bound one-new-prime Type II exponents on the H19-k23 global tail menu."""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
import math
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
DEFAULT_PROFILE_INPUT = ROOT / "reproductions" / "h19-k23-global-one-prime-power-descent-profile-2097152.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-global-one-prime-power-exponent-compression-2097152.json"
GLOBAL_CLOSURE = ROOT / "reproductions" / "h19_k23_full_global_tail_closure.py"
NORMAL_FORM = ROOT / "reproductions" / "type_ii_square_root_completion_family.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


global_closure = load_module("h19_k23_exponent_compression_global", GLOBAL_CLOSURE)
normal_form = load_module("h19_k23_exponent_compression_normal_form", NORMAL_FORM)


def carmichael(value: int) -> int:
    """Return lambda(value), including the harmless convention lambda(1)=1."""
    if value < 1:
        raise ValueError("Carmichael input must be positive")
    return (
        1
        if value == 1
        else int(sympy.functions.combinatorial.numbers.reduced_totient(value))
    )


def compressed_exponent(exponent: int, order: int) -> int:
    """Return the least positive exponent congruent to exponent modulo order."""
    if exponent < 1 or order < 1:
        raise ValueError("exponent and order must be positive")
    return (exponent - 1) % order + 1


def run_audit(profile_payload: dict[str, object]) -> dict[str, object]:
    """Compress every stored one-prime-power witness and tabulate menu bounds."""
    _, bases = global_closure.global_tail_bases()
    all_gaps = sorted(bases)
    bound_rows = [
        {"tail_gap": gap, "carmichael_bound": carmichael(gap)}
        for gap in all_gaps
    ]
    compression_histogram: Counter[str] = Counter()
    used_gap_bounds = []
    for row in profile_payload["records"]:
        prime = int(row["prime"])
        gap = int(row["tail_gap"])
        divisor = int(row["divisor"])
        new_prime = int(row["new_prime"])
        exponent = int(row["new_prime_exponent"])
        if math.gcd(new_prime, gap) != 1:
            raise AssertionError("a Type II divisor prime is not a unit modulo its gap")
        order = int(sympy.n_order(new_prime, gap))
        reduced_exponent = compressed_exponent(exponent, order)
        if reduced_exponent > carmichael(gap):
            raise AssertionError("multiplicative-order compression exceeded lambda(m)")
        reduced_divisor = divisor // new_prime ** (exponent - reduced_exponent)
        tail_parameter = (prime - 1) // (gap + 1)
        normal_form.two_tail_witness(
            (gap + 1) // 4, reduced_divisor, tail_parameter
        )
        compression_histogram[f"{exponent}->{reduced_exponent}"] += 1
        used_gap_bounds.append(carmichael(gap))
    if len(used_gap_bounds) != int(profile_payload["final_one_support_count"]):
        raise AssertionError("not every one-prime-power record was compressed")
    return {
        "arithmetic": (
            "for every Type II divisor d=b*ell^e, gcd(x,m)=1 forces ell to be a "
            "unit modulo m. Reducing e to its least positive congruence class modulo "
            "ord_m(ell) preserves d modulo m while decreasing it, so it remains a "
            "valid divisor and strict ordinary two-tail descent"
        ),
        "scope_note": (
            "A proof-level exponent compression for one-prime-power certificates on "
            "the fixed global tail menu. It does not force a suitable adaptive prime."
        ),
        "global_tail_count": len(all_gaps),
        "global_max_carmichael_bound": max(row["carmichael_bound"] for row in bound_rows),
        "global_max_carmichael_bound_gap": max(
            bound_rows, key=lambda row: row["carmichael_bound"]
        )["tail_gap"],
        "used_profile_count": len(used_gap_bounds),
        "used_tail_max_carmichael_bound": max(used_gap_bounds),
        "used_tail_max_carmichael_bound_gap": max(
            int(row["tail_gap"])
            for row in profile_payload["records"]
            if carmichael(int(row["tail_gap"])) == max(used_gap_bounds)
        ),
        "selected_exponent_compression_histogram": dict(
            sorted(compression_histogram.items())
        ),
        "tail_bounds": bound_rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile-input", type=Path, default=DEFAULT_PROFILE_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    profile_payload = json.loads(args.profile_input.read_text(encoding="utf-8"))
    result = run_audit(profile_payload)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
