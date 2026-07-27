#!/usr/bin/env python3
"""Join H19 strict descents with pure Type II fallback certificates."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROFILE = ROOT / "reproductions" / "type-ii-minimal-collision-support-h19-300m-results.json"
DEFAULT_DESCENT = ROOT / "reproductions" / "type-ii-h19-targeted-quadratic-descent-300m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-hybrid-short-or-descent-300m-results.json"


def verify_descent(prime: int, witness: dict[str, object]) -> None:
    source = int(witness["source_denominator"])
    source_solution = tuple(int(value) for value in witness["source_solution"])
    target_solution = tuple(int(value) for value in witness["target_solution"])
    if not 2 <= source < prime:
        raise AssertionError("descent source is not strictly smaller")
    if Fraction(4, source) != sum((Fraction(1, value) for value in source_solution), Fraction()):
        raise AssertionError("source solution does not verify")
    if Fraction(4, prime) != sum((Fraction(1, value) for value in target_solution), Fraction()):
        raise AssertionError("target lift does not verify")


def verify_pure_type_ii(prime: int, profile: dict[str, object]) -> None:
    witness = profile["selected_witness"]
    if witness["collision_multiplicity"] or witness["old_private_multiplicity"]:
        raise AssertionError("fallback is not source-free and pure-new")
    if witness["new_multiplicity"] != 1:
        raise AssertionError("fallback does not have one new factor")
    h = int(witness["h"])
    a = int(witness["a"])
    c = int(witness["c"])
    k = int(witness["k"])
    if h != 4 * a * c * k - 1 or (prime + 4 * a * a * c) % h:
        raise AssertionError("fallback does not meet the canonical Type II factor condition")


def run_audit(profile_payload: dict[str, object], descent_payload: dict[str, object]) -> dict[str, object]:
    """Verify that every stored H19 residual has a descent or pure Type II exit."""
    profiles = {int(row["prime"]): row for row in profile_payload["profiles"]}
    descents = {int(row["prime"]): row for row in descent_payload["records"]}
    if not set(profiles) <= set(descents):
        raise AssertionError("new-factor profile contains a non-H19 residual")
    fallback_records: list[dict[str, object]] = []
    descent_count = 0
    for prime, descent_record in sorted(descents.items()):
        descent = descent_record["quadratic_factor_external_source_descent"]
        if descent is not None:
            verify_descent(prime, descent)
            descent_count += 1
            continue
        profile = profiles.get(prime)
        if profile is None:
            raise AssertionError("a descent miss has no source-free new-factor profile")
        verify_pure_type_ii(prime, profile)
        fallback_records.append(
            {
                "prime": prime,
                "shift": profile["first_minimum_collision_shift"],
                "selected_witness": profile["selected_witness"],
            }
        )
    return {
        "arithmetic": (
            "exact rational verification of every strict lift and exact "
            "canonical Type II divisibility verification for every fallback"
        ),
        "scope_note": (
            "A finite H19 hybrid closure over the supplied profile. It does "
            "not establish a universal H19, descent, or shift bound."
        ),
        "prime_limit": profile_payload["prime_limit"],
        "base_shift_bound": profile_payload["base_shift_bound"],
        "h19_residual_count": len(descents),
        "quadratic_descent_count": descent_count,
        "pure_type_ii_fallback_count": len(fallback_records),
        "unclosed_primes": [],
        "fallback_records": fallback_records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--descent", type=Path, default=DEFAULT_DESCENT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    profile_payload = json.loads(args.profile.read_text(encoding="utf-8"))
    descent_payload = json.loads(args.descent.read_text(encoding="utf-8"))
    result = run_audit(profile_payload, descent_payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
