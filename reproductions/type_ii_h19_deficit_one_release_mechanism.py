#!/usr/bin/env python3
"""Test whether later-r releases restore the same exhausted prime in deficit-one states."""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-h19-deficit-one-saturated-prime-profile-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-deficit-one-release-mechanism-1b-results.json"


def saturated_primes(m1: int, r: int) -> list[tuple[int, int]]:
    """Return every q^nu whose exhausted extra q reaches -1 modulo r."""
    primes = []
    for q, exponent in sorted((int(q), int(e)) for q, e in sympy.factorint(m1).items()):
        q_power = q**exponent
        if any((q * q_power * int(b)) % r == r - 1 for b in sympy.divisors(m1 // q_power)):
            primes.append((q, exponent))
    if not primes:
        raise AssertionError("deficit-one state lacks every saturated-prime witness")
    return primes


def fixed_prime_lift_predictions(prime: int, r0: int, r1: int, m0: int, q: int, exponent: int) -> tuple[bool, bool]:
    """Predict persistence and exponent gain of q under r1=r0+8*j exactly."""
    if q % 2 == 0 or m0 % q**exponent != 0 or m0 % q ** (exponent + 1) == 0:
        raise ValueError("q^exponent must be the exact odd q-part of m0")
    if (r1 - r0) % 8:
        raise ValueError("both compatible r values must have the same class modulo eight")
    j = (r1 - r0) // 8
    persists = j % q == 0
    if not persists:
        return False, False
    t = j // q
    gains = (m0 // q + 2 * prime * t) % q**exponent == 0
    return True, gains


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Classify whether each later release preserves an initial saturated prime."""
    records = []
    for row in payload["records"]:
        later_r = row["later_zero_overflow_release_r"]
        if later_r is None:
            continue
        prime, r0, r1 = int(row["prime"]), int(row["r"]), int(later_r)
        m0, m1 = (r0 * prime + 1) // 4, (r1 * prime + 1) // 4
        later_factors = {int(q): int(e) for q, e in sympy.factorint(m1).items()}
        candidates = saturated_primes(m0, r0)
        candidate_rows = [
            {
                "prime": q,
                "initial_exponent": exponent,
                "later_exponent": later_factors.get(q, 0),
            }
            for q, exponent in candidates
        ]
        for candidate in candidate_rows:
            q, exponent = int(candidate["prime"]), int(candidate["initial_exponent"])
            persists, gains = fixed_prime_lift_predictions(prime, r0, r1, m0, q, exponent)
            if persists != (int(candidate["later_exponent"]) > 0):
                raise AssertionError("fixed-prime persistence congruence failed")
            if gains != (int(candidate["later_exponent"]) > exponent):
                raise AssertionError("fixed-prime exponent-gain congruence failed")
        if any(record["later_exponent"] > record["initial_exponent"] for record in candidate_rows):
            kind = "same_prime_exponent_gain"
        elif any(record["later_exponent"] > 0 for record in candidate_rows):
            kind = "same_prime_persists_without_gain"
        else:
            kind = "all_saturated_primes_absent"
        records.append(
            {
                "prime": prime,
                "first_r": r0,
                "release_r": r1,
                "mechanism_kind": kind,
                "initial_saturated_primes": candidate_rows,
            }
        )
    histogram = Counter(record["mechanism_kind"] for record in records)
    return {
        "arithmetic": (
            "exact factorization of initial and release M=(r*p+1)/4 values, with every "
            "deficit-one saturated-prime witness q^nu*b tested against the release support"
        ),
        "scope_note": (
            "A finite mechanism classification for stored delta-one later-r releases. "
            "It does not prove how a later-r release is selected generally."
        ),
        "prime_limit": payload["prime_limit"],
        "delta_one_later_release_count": len(records),
        "release_mechanism_histogram": dict(sorted(histogram.items())),
        "all_fixed_prime_lift_congruences_verified": True,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.input.read_text(encoding="utf-8")))
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
