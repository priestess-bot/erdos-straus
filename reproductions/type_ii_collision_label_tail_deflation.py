#!/usr/bin/env python3
"""Test marked Type II tail deflation on H19 collision-labelled witnesses."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = (
    ROOT / "reproductions" / "type-ii-minimal-collision-support-h19-1b-results.json"
)
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-ii-collision-label-tail-deflation-h19-1b-results.json"
)


def factorization_record(value: int) -> list[dict[str, int]]:
    return [
        {"prime": int(prime), "exponent": int(exponent)}
        for prime, exponent in sorted(sympy.factorint(value).items())
    ]


def verify_type_ii_certificate(prime: int, gap: int, divisor: int) -> tuple[int, int, int]:
    """Recover and exactly verify the stored Type II certificate."""
    numerator = prime + gap
    if numerator % 4:
        raise AssertionError("Type II gap does not give an integral first denominator")
    x = numerator // 4
    if divisor <= 0 or x * x % divisor:
        raise AssertionError("stored Type II divisor does not divide x squared")
    y_numerator = prime * (x + divisor)
    z_numerator = prime * (x + x * x // divisor)
    if y_numerator % gap or z_numerator % gap:
        raise AssertionError("stored Type II divisor does not reconstruct integral tails")
    y, z = y_numerator // gap, z_numerator // gap
    if y % prime or z % prime:
        raise AssertionError("stored certificate is not Type II")
    if Fraction(4, prime) != sum((Fraction(1, value) for value in (x, y, z)), Fraction()):
        raise AssertionError("stored Type II certificate failed exact reconstruction")
    return x, y, z


def marked_tail_witness(prime: int, gap: int, divisor: int) -> dict[str, object] | None:
    """Return the least scaled-first strict lift at this fixed certificate gap."""
    x, y, z = verify_type_ii_certificate(prime, gap, divisor)
    shifted_value = prime + gap
    candidates = [
        int(candidate)
        for candidate in sympy.divisors(shifted_value)
        if candidate > 1 and (candidate - 1) % gap == 0
    ]
    if not candidates:
        return None
    shared_divisor = min(candidates)
    first_scale = (shared_divisor - 1) // gap
    source_denominator = first_scale * shifted_value // shared_divisor
    if not 2 <= source_denominator < prime:
        raise AssertionError("marked source is not a strict smaller instance")
    source_solution = (first_scale * x, y // prime, z // prime)
    if Fraction(4, source_denominator) != sum(
        (Fraction(1, value) for value in source_solution), Fraction()
    ):
        raise AssertionError("marked source solution did not verify")
    return {
        "shared_divisor": shared_divisor,
        "shared_divisor_factorization": factorization_record(shared_divisor),
        "first_scale": first_scale,
        "source_denominator": source_denominator,
        "source_solution": list(source_solution),
        "eligible_shared_divisor_count": len(candidates),
    }


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Test every positive-collision minimum witness at its selected gap."""
    records: list[dict[str, object]] = []
    for profile in payload["profiles"]:
        multiplicity = int(profile["minimum_collision_multiplicity"])
        if multiplicity == 0:
            continue
        witness = profile["selected_witness"]
        prime = int(profile["prime"])
        gap = int(witness["gap"])
        divisor = int(witness["divisor"])
        strict_lift = marked_tail_witness(prime, gap, divisor)
        records.append(
            {
                "prime": prime,
                "collision_multiplicity": multiplicity,
                "shift": int(profile["first_minimum_collision_shift"]),
                "gap": gap,
                "certificate_factor": int(witness["h"]),
                "gap_plus_one_remainder": (prime - 1) % (gap + 1),
                "marked_tail_witness": strict_lift,
            }
        )
    hits = [record for record in records if record["marked_tail_witness"] is not None]
    return {
        "arithmetic": (
            "complete exact factorization of p+m, all divisors D>1 with "
            "D=1 mod m, stored Type II certificate reconstruction, and exact "
            "scaled-first source verification"
        ),
        "scope_note": (
            "A fixed-certificate finite audit. A miss only rules out marked "
            "tail deflation at that selected collision-labelled certificate, "
            "not other certificates or descents."
        ),
        "input_artifact": "type-ii-minimal-collision-support-h19-1b-results.json",
        "prime_limit": payload["prime_limit"],
        "collision_labelled_state_count": len(records),
        "marked_tail_descent_count": len(hits),
        "marked_tail_descent_misses": [
            record["prime"] for record in records if record["marked_tail_witness"] is None
        ],
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
