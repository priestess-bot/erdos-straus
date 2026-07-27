#!/usr/bin/env python3
"""Find alternative ordinary Type II tail descents for collision-label misses."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = (
    ROOT / "reproductions" / "type-ii-collision-label-tail-deflation-h19-1b-results.json"
)
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-ii-collision-alternative-tail-descent-h19-1b-results.json"
)


def factorization_record(value: int) -> list[dict[str, int]]:
    return [
        {"prime": int(prime), "exponent": int(exponent)}
        for prime, exponent in sorted(sympy.factorint(value).items())
    ]


def type_ii_certificate(prime: int, gap: int) -> dict[str, int] | None:
    """Find one exact Type II certificate at a prescribed gap."""
    if gap < 3 or gap % 4 != 3:
        return None
    numerator = prime + gap
    if numerator % 4:
        return None
    x = numerator // 4
    target = (-x) % gap
    for candidate in sympy.divisors(x * x):
        if candidate % gap != target:
            continue
        divisor = min(int(candidate), x * x // int(candidate))
        y_numerator = prime * (x + divisor)
        z_numerator = prime * (x + x * x // divisor)
        if y_numerator % gap or z_numerator % gap:
            continue
        y, z = y_numerator // gap, z_numerator // gap
        if y % prime or z % prime:
            continue
        if Fraction(4, prime) != sum((Fraction(1, value) for value in (x, y, z)), Fraction()):
            raise AssertionError("candidate Type II certificate did not verify")
        return {"x": x, "divisor": divisor, "y": y, "z": z}
    return None


def first_alternative_tail_descent(prime: int) -> tuple[dict[str, object] | None, int]:
    """Exhaust every p-1 indexed tail gap and return the least successful one."""
    candidate_gaps = [
        int(divisor) - 1
        for divisor in sympy.divisors(prime - 1)
        if divisor >= 4 and divisor % 4 == 0
    ]
    for gap in sorted(candidate_gaps):
        certificate = type_ii_certificate(prime, gap)
        if certificate is None:
            continue
        source_denominator = (prime + gap) // (gap + 1)
        if (gap + 1) * source_denominator != prime + gap:
            raise AssertionError("p-1 indexed source is not integral")
        source_solution = (
            certificate["x"],
            certificate["y"] // prime,
            certificate["z"] // prime,
        )
        if not 2 <= source_denominator < prime:
            raise AssertionError("tail descent did not strictly decrease")
        if Fraction(4, source_denominator) != sum(
            (Fraction(1, value) for value in source_solution), Fraction()
        ):
            raise AssertionError("tail descent source solution did not verify")
        return (
            {
                "gap": gap,
                "gap_plus_one": gap + 1,
                "certificate": certificate,
                "source_denominator": source_denominator,
                "source_solution": list(source_solution),
            },
            len(candidate_gaps),
        )
    return None, len(candidate_gaps)


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Replace each fixed-certificate miss by an exhaustive p-1 tail scan."""
    records: list[dict[str, object]] = []
    for prime in payload["marked_tail_descent_misses"]:
        prime = int(prime)
        witness, candidate_gap_count = first_alternative_tail_descent(prime)
        records.append(
            {
                "prime": prime,
                "p_minus_one_factorization": factorization_record(prime - 1),
                "candidate_gap_count": candidate_gap_count,
                "alternative_tail_witness": witness,
            }
        )
    hits = [record for record in records if record["alternative_tail_witness"] is not None]
    return {
        "arithmetic": (
            "complete p-1 divisor enumeration for all 4-divisible gaps, exact "
            "factorization of every resulting x, complete Type II square-divisor "
            "checks, and exact strict source reconstruction"
        ),
        "scope_note": (
            "A complete ordinary two-tail-deflation scan on the supplied finite "
            "states. A miss does not exclude scaled, Type I, or external-source descents."
        ),
        "input_artifact": "type-ii-collision-label-tail-deflation-h19-1b-results.json",
        "prime_limit": payload["prime_limit"],
        "fixed_certificate_miss_count": len(records),
        "alternative_tail_descent_count": len(hits),
        "alternative_tail_descent_misses": [
            record["prime"] for record in records if record["alternative_tail_witness"] is None
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
