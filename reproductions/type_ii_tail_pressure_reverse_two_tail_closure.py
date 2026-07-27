#!/usr/bin/env python3
"""Close the 500M shifted-external pressure set by short reverse two-tail edges.

Each pressure point is scanned through short Bradford gaps in deterministic
order.  Every Type I normal form is tested with the complete divisor reverse
search from ``boundary_gap_27_reverse_two_tail_bridge.py``.  A record is a
verified strict source/target edge, but target-side selection is deliberately
not presented as an inductive source-side rule.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXTERNAL_BOUNDARY = ROOT / "reproductions" / "type-ii-tail-deflation-external-boundary-500m-results.json"
LANDSCAPE = ROOT / "reproductions" / "boundary_gap_certificate_landscape.py"
REVERSE_BRIDGE = ROOT / "reproductions" / "boundary_gap_27_reverse_two_tail_bridge.py"
DEFAULT_GAP_CAP = 1_003
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-tail-pressure-reverse-two-tail-500m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


landscape = load_module("tail_pressure_reverse_landscape", LANDSCAPE)
bridge = load_module("tail_pressure_reverse_bridge", REVERSE_BRIDGE)


def first_reverse_edge(prime: int, gap_cap: int) -> tuple[dict[str, object] | None, int, int]:
    """Return the first short-gap Type I reverse edge and checked certificate counts."""
    type_i_checked = 0
    type_ii_checked = 0
    for gap in range(3, gap_cap + 1, 4):
        gap_entry = landscape.gap_landscape(prime, gap)
        type_ii_checked += len(gap_entry["type_ii_divisors"])
        for entry in gap_entry["type_i"]:
            type_i_checked += 1
            A, B, C = entry["normal_form"]
            certificate = bridge.short_certificate.type_i_normal_form_certificate(
                prime, gap, A, B
            )
            if certificate is None:
                raise AssertionError("stored Type I normal form did not rebuild")
            target = (certificate.x, certificate.y, certificate.z)
            factorization = bridge.type_i_target_factorizations(prime, gap, A, B, C)
            for position, (target_term, target_factors) in enumerate(zip(target, factorization)):
                if position == 2:
                    eligible_count, lifts = bridge.type_i_normal_reverse_two_tail_lifts(
                        prime, gap, A, B, C
                    )
                else:
                    eligible_count, lifts = bridge.reverse_two_tail_lifts_by_divisors(
                        prime, target_term, target_factors
                    )
                if not lifts:
                    continue
                lift = lifts[0]
                source = (
                    lift["source_term"],
                    *(term for index, term in enumerate(target) if index != position),
                )
                if Fraction(4, lift["source_denominator"]) != sum(
                    (Fraction(1, term) for term in source), Fraction()
                ):
                    raise AssertionError("reverse source identity did not verify")
                if Fraction(4, prime) != sum(
                    (Fraction(1, term) for term in target), Fraction()
                ):
                    raise AssertionError("reverse target identity did not verify")
                return (
                    {
                        "gap": gap,
                        "divisor": entry["divisor"],
                        "normal_form": [A, B, C],
                        "target_solution": list(target),
                        "replaced_target_position": position,
                        "target_term": target_term,
                        "target_term_factorization": {
                            str(q): exponent for q, exponent in target_factors.items()
                        },
                        "eligible_bridge_divisor_count": eligible_count,
                        "reverse_two_tail_lift": lift,
                        "source_solution": list(source),
                    },
                    type_i_checked,
                    type_ii_checked,
                )
    return None, type_i_checked, type_ii_checked


def primes_from_payload(payload: dict[str, object], miss_field: str) -> list[int]:
    """Read either integer misses or full miss records from a stored audit."""
    if miss_field not in payload:
        raise ValueError(f"input payload has no {miss_field!r} field")
    values = payload[miss_field]
    if not isinstance(values, list):
        raise ValueError("miss field must be a list")
    primes = [int(value["prime"]) if isinstance(value, dict) else int(value) for value in values]
    if not primes:
        raise ValueError("input payload has no misses")
    return primes


def run_audit(
    payload: dict[str, object], gap_cap: int = DEFAULT_GAP_CAP, miss_field: str = "shared_external_misses"
) -> dict[str, object]:
    if gap_cap < 3 or gap_cap % 4 != 3:
        raise ValueError("gap_cap must be at least 3 and congruent to 3 modulo 4")
    primes = primes_from_payload(payload, miss_field)
    records: list[dict[str, object]] = []
    misses: list[int] = []
    total_type_i_checked = 0
    total_type_ii_checked = 0
    for prime in primes:
        edge, type_i_checked, type_ii_checked = first_reverse_edge(prime, gap_cap)
        total_type_i_checked += type_i_checked
        total_type_ii_checked += type_ii_checked
        if edge is None:
            misses.append(prime)
            continue
        records.append({"prime": prime, **edge})
    source_denominators = [
        int(record["reverse_two_tail_lift"]["source_denominator"])
        for record in records
    ]
    return {
        "arithmetic": (
            "for each stored input miss, factor x=(p+m)/4 "
            "by trial division for every m=3 (mod 4) through gap_cap; enumerate "
            "every Type I/II divisor certificate; for each Type I target term, "
            "enumerate every D|4*p^2*t^2 and verify the first strict reverse "
            "source and target identities with Fraction"
        ),
        "scope_note": (
            "A target-side finite closure of the stated pressure set. It proves "
            "each recorded strict edge, but its target-first selection is not a "
            "source-side inductive selector for arbitrary core primes."
        ),
        "input_prime_limit": payload["prime_limit"],
        "pressure_point_count": len(primes),
        "gap_cap": gap_cap,
        "captured_count": len(records),
        "misses": misses,
        "total_type_i_certificates_checked_until_first_edge_or_cap": total_type_i_checked,
        "total_type_ii_certificates_checked_until_first_edge_or_cap": total_type_ii_checked,
        "maximum_selected_gap": max((int(record["gap"]) for record in records), default=None),
        "even_source_count": sum(source % 2 == 0 for source in source_denominators),
        "odd_source_count": sum(source % 2 == 1 for source in source_denominators),
        "minimum_descent_slack": min(
            (int(record["prime"]) - int(record["reverse_two_tail_lift"]["source_denominator"]) for record in records),
            default=None,
        ),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=EXTERNAL_BOUNDARY)
    parser.add_argument("--gap-cap", type=int, default=DEFAULT_GAP_CAP)
    parser.add_argument("--miss-field", default="shared_external_misses")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload, args.gap_cap, args.miss_field)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
