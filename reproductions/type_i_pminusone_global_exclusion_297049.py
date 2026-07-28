#!/usr/bin/env python3
"""Exclude every normal-form maximum-tail p-1 Type I bridge at p=297049.

The p-1 bridge criterion forces ``R=4*r-1`` with ``r | ((p-1)/4)^2``.
For every one of those 27 states, this audit enumerates both all ordered
factorizations ``B*C*H=K`` and all normalized square divisors ``d | K^2``.
It also recomputes the ordinary Type II p-1 tail and the known shifted B=1
terminal bridge.  This is a complete single-prime audit in that architecture,
not a universal selector theorem.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict
from fractions import Fraction
import json
import math
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from reproductions import short_certificate  # noqa: E402


PRIME = 297_049
SHIFT = 25
SHIFT_R = 19
SHIFT_C = 71
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-I-pminusone-global-exclusion-297049.json"
)


def exact_factorization(value: int) -> list[tuple[int, int]]:
    """Factor ``value`` and verify the returned prime-power product exactly."""
    if value < 1:
        raise ValueError("factorization requires a positive integer")
    factors = sorted(
        (int(prime), int(exponent))
        for prime, exponent in sympy.factorint(value).items()
    )
    if math.prod(prime**exponent for prime, exponent in factors) != value or any(
        not sympy.isprime(prime) for prime, _ in factors
    ):
        raise AssertionError("factorization did not reconstruct into primes")
    return factors


def divisors_from_factorization(
    factors: list[tuple[int, int]], exponent_multiplier: int = 1
) -> list[int]:
    """Return sorted divisors after multiplying every prime exponent."""
    if exponent_multiplier < 1:
        raise ValueError("exponent multiplier must be positive")
    divisors = [1]
    for prime, exponent in factors:
        divisors = [
            divisor * prime**power
            for divisor in divisors
            for power in range(exponent_multiplier * exponent + 1)
        ]
    return sorted(divisors)


def ordered_factor_triples(
    factors: list[tuple[int, int]],
) -> list[tuple[int, int, int]]:
    """Return every ordered positive triple ``(B,C,H)`` with product ``K``."""
    triples = [(1, 1, 1)]
    for prime, exponent in factors:
        triples = [
            (
                B * prime**b_exponent,
                C * prime**c_exponent,
                H * prime ** (exponent - b_exponent - c_exponent),
            )
            for B, C, H in triples
            for b_exponent in range(exponent + 1)
            for c_exponent in range(exponent - b_exponent + 1)
        ]
    return triples


def exact_fraction_identity(numerator: int, denominators: list[int]) -> bool:
    """Check a three-term unit-fraction identity exactly."""
    return Fraction(4, numerator) == sum(
        (Fraction(1, denominator) for denominator in denominators), Fraction()
    )


def build_natural_witness(
    prime: int,
    t: int,
    r: int,
    R: int,
    K: int,
    matched_divisor: int,
) -> dict[str, object]:
    """Normalize a square-divisor hit and orient it to a natural Type I gap."""
    common = math.gcd(matched_divisor, K)
    initial_B = matched_divisor // common
    if common * common % matched_divisor:
        raise AssertionError("square divisor did not normalize to integral C")
    C = common * common // matched_divisor
    initial_H = K // common
    if (
        initial_B * C * initial_H != K
        or initial_B * initial_B * C != matched_divisor
        or math.gcd(initial_B, initial_H) != 1
    ):
        raise AssertionError("square-divisor normalization failed")
    if initial_B == initial_H:
        raise AssertionError("target residue unexpectedly allowed B=H")

    orientation_swapped = initial_H < initial_B
    B, H = (initial_H, initial_B) if orientation_swapped else (initial_B, initial_H)
    oriented_divisor = B * B * C
    if (H + B) % R:
        raise AssertionError("target congruence did not recover integral A")
    A = (H + B) // R
    gap, gap_remainder = divmod(4 * oriented_divisor + 1, R)
    if gap_remainder:
        raise AssertionError("oriented divisor did not recover integral gap")

    certificate = short_certificate.type_i_normal_form_certificate(prime, gap, A, B)
    if certificate is None:
        raise AssertionError("oriented hit did not recover a Type I certificate")
    E = R + 1
    source = prime - 1
    source_term, source_remainder = divmod(source * K, E)
    target_solution = [A * B * C, A * C * H, prime * K]
    source_solution = [source_term, *target_solution[:2]]
    natural_gap = 3 <= gap <= prime - 2 and gap % 4 == 3
    conditions = {
        "forced_state_reconstructs": (
            R == 4 * r - 1 and 4 * K == prime * R + 1 and (t * t) % r == 0
        ),
        "matched_square_divisor_divides_K_squared": (K * K) % matched_divisor == 0,
        "matched_target_residue": matched_divisor % R == (-r) % R,
        "matched_gap_is_integral": (4 * matched_divisor + 1) % R == 0,
        "oriented_square_divisor_divides_K_squared": (K * K) % oriented_divisor == 0,
        "orientation_preserves_target_residue": oriented_divisor % R == (-r) % R,
        "B_C_H_reconstruct_K": B * C * H == K,
        "B_H_are_coprime": math.gcd(B, H) == 1,
        "H_is_greater_than_B": H > B,
        "A_is_integral": A * R == H + B,
        "A_B_are_coprime": math.gcd(A, B) == 1,
        "normal_form_reconstructs_prime": 4 * A * B * C - gap == prime,
        "gap_is_natural": natural_gap,
        "certificate_matches_normal_form": (
            certificate.x == target_solution[0]
            and certificate.y == target_solution[1]
            and certificate.z == target_solution[2]
        ),
        "source_square_compatible": (source * source // math.gcd(E, 4)) % E == 0,
        "E_divides_4K_squared": (4 * K * K) % E == 0,
        "source_term_is_integral": source_remainder == 0,
        "target_solution_is_ordered": (
            target_solution[0] < target_solution[1] < target_solution[2]
        ),
        "target_fraction_identity": exact_fraction_identity(prime, target_solution),
        "source_fraction_identity": exact_fraction_identity(source, source_solution),
    }
    if not all(conditions.values()):
        failed = [name for name, passed in conditions.items() if not passed]
        raise AssertionError(f"natural p-1 witness failed: {failed}")
    return {
        "r": r,
        "R": R,
        "K": K,
        "E": E,
        "source_denominator": source,
        "matched_square_divisor": matched_divisor,
        "normalized_before_orientation": [initial_B, C, initial_H],
        "orientation_swapped": orientation_swapped,
        "oriented_square_divisor": oriented_divisor,
        "normal_form": [A, B, C],
        "H": H,
        "gap": gap,
        "natural_gap": natural_gap,
        "target_certificate": asdict(certificate),
        "source_term": source_term,
        "target_solution": target_solution,
        "source_solution": source_solution,
        "conditions": conditions,
    }


def audit_pminusone_state(prime: int, t: int, r: int) -> dict[str, object]:
    """Exhaust all normal-form factor states for one forced p-1 scale ``r``."""
    R = 4 * r - 1
    K = prime * r - t
    if 4 * K != prime * R + 1:
        raise AssertionError("forced p-1 state did not reconstruct 4K=pR+1")

    factors = exact_factorization(K)
    triples = ordered_factor_triples(factors)
    square_divisors = divisors_from_factorization(factors, 2)
    target_residue = (-r) % R

    ordered_reachable: set[int] = set()
    ordered_residue_hits = 0
    ordered_hit_divisors: set[int] = set()
    ordered_witnesses: dict[int, dict[str, object]] = {}
    for B, C, H in triples:
        if B * C * H != K:
            raise AssertionError("ordered factor triple did not reconstruct K")
        divisor = B * B * C
        residue = divisor % R
        ordered_reachable.add(residue)
        if residue != target_residue:
            continue
        ordered_residue_hits += 1
        witness = build_natural_witness(prime, t, r, R, K, divisor)
        ordered_hit_divisors.add(divisor)
        if divisor in ordered_witnesses and ordered_witnesses[divisor] != witness:
            raise AssertionError("ordered hits disagreed after normalization")
        ordered_witnesses[divisor] = witness

    normalized_reachable: set[int] = set()
    normalized_residue_hits = 0
    natural_witnesses: list[dict[str, object]] = []
    normalized_hit_divisors: set[int] = set()
    for divisor in square_divisors:
        common = math.gcd(divisor, K)
        B = divisor // common
        if common * common % divisor:
            raise AssertionError("square divisor did not normalize to integral C")
        C = common * common // divisor
        H = K // common
        if B * C * H != K or B * B * C != divisor or math.gcd(B, H) != 1:
            raise AssertionError("normalized square divisor did not reconstruct")
        residue = divisor % R
        normalized_reachable.add(residue)
        if residue != target_residue:
            continue
        normalized_residue_hits += 1
        witness = build_natural_witness(prime, t, r, R, K, divisor)
        normalized_hit_divisors.add(divisor)
        natural_witnesses.append(witness)
        if ordered_witnesses.get(divisor) != witness:
            raise AssertionError("ordered and normalized hit witnesses disagree")

    if normalized_reachable != ordered_reachable:
        raise AssertionError("the two exhaustive enumerations disagree on residues")
    if normalized_hit_divisors != ordered_hit_divisors:
        raise AssertionError("the two exhaustive enumerations disagree on hits")
    return {
        "r": r,
        "R": R,
        "K": K,
        "K_factorization": [
            {"prime": factor, "exponent": exponent} for factor, exponent in factors
        ],
        "normalized_square_divisor_candidate_count": len(square_divisors),
        "ordered_BCH_candidate_count": len(triples),
        "reachable_residue_count": len(ordered_reachable),
        "target_residue": target_residue,
        "target_residue_reachable": target_residue in ordered_reachable,
        "ordered_residue_hit_count": ordered_residue_hits,
        "normalized_residue_hit_count": normalized_residue_hits,
        "valid_normal_form_hit_count": len(natural_witnesses),
        "orientation_swapped_count": sum(
            bool(witness["orientation_swapped"]) for witness in natural_witnesses
        ),
        "natural_gap_verified_count": sum(
            bool(witness["natural_gap"]) for witness in natural_witnesses
        ),
        "natural_witnesses": natural_witnesses,
    }


def ordinary_type_ii_tail_audit(prime: int) -> dict[str, object]:
    """Recompute the complete ordinary Type II p-1 double-tail selector."""
    factors = exact_factorization(prime - 1)
    eligible_gaps = [
        divisor - 1
        for divisor in divisors_from_factorization(factors)
        if divisor % 4 == 0
    ]
    spf = short_certificate.smallest_prime_factors(prime + 1)
    witnesses = short_certificate.type_ii_tail_deflation_scan(prime, spf)
    return {
        "eligible_gap_count": len(eligible_gaps),
        "eligible_gaps": eligible_gaps,
        "witness_count": len(witnesses),
        "witnesses": [asdict(witness) for witness in witnesses],
    }


def shifted_b1_terminal_audit(prime: int) -> dict[str, object]:
    """Rebuild the exact p-25, B=1 Type I terminal bridge."""
    source = prime - SHIFT
    R = SHIFT_R
    E = SHIFT * R + 1
    K, remainder = divmod(prime * R + 1, 4)
    if remainder:
        raise AssertionError("shifted state has nonintegral K")
    B = 1
    C = SHIFT_C
    H, remainder = divmod(K, B * C)
    if remainder or (H + B) % R or (4 * B * B * C + 1) % R:
        raise AssertionError("shifted B=1 state did not realize a normal form")
    A = (H + B) // R
    gap = (4 * B * B * C + 1) // R
    certificate = short_certificate.type_i_normal_form_certificate(prime, gap, A, B)
    if certificate is None:
        raise AssertionError("shifted B=1 target certificate did not reconstruct")
    source_term, remainder = divmod(source * K, E)
    if remainder:
        raise AssertionError("shifted bridge has nonintegral source term")

    target_solution = [certificate.x, certificate.y, certificate.z]
    source_solution = [source_term, certificate.x, certificate.y]
    conditions = {
        "source_is_strict_even": 2 <= source < prime and source % 2 == 0,
        "source_square_compatible": (source * source // math.gcd(E, 4)) % E == 0,
        "E_divides_4K_squared": (4 * K * K) % E == 0,
        "E_is_one_mod_R": E % R == 1,
        "E_is_even": E % 2 == 0,
        "terminal_size_bound": E <= 4 * K - 2 * R,
        "target_identity": Fraction(4, prime)
        == sum(
            (Fraction(1, denominator) for denominator in target_solution),
            Fraction(),
        ),
        "source_identity": Fraction(4, source)
        == sum(
            (Fraction(1, denominator) for denominator in source_solution),
            Fraction(),
        ),
    }
    if not all(conditions.values()):
        raise AssertionError("shifted B=1 bridge failed an exact condition")
    if (
        certificate.x != A * B * C
        or certificate.y != A * C * H
        or certificate.z != prime * K
        or 4 * A * B * C - gap != prime
    ):
        raise AssertionError("shifted target normal form did not reconstruct")
    return {
        "shift": SHIFT,
        "source_denominator": source,
        "R": R,
        "E": E,
        "K": K,
        "normal_form": [A, B, C],
        "H": H,
        "gap": gap,
        "source_term": source_term,
        "target_certificate": asdict(certificate),
        "target_solution": target_solution,
        "source_solution": source_solution,
        "conditions": conditions,
    }


def orientation_swap_positive_control() -> dict[str, object]:
    """Exercise the natural-gap orientation on a known reversed hit at p=73."""
    prime = 73
    t = (prime - 1) // 4
    r = 1
    R = 4 * r - 1
    K = prime * r - t
    witness = build_natural_witness(prime, t, r, R, K, 275)
    expected = {
        "normalized_before_orientation": [5, 11, 1],
        "orientation_swapped": True,
        "oriented_square_divisor": 11,
        "normal_form": [2, 1, 11],
        "H": 5,
        "gap": 15,
        "natural_gap": True,
        "target_solution": [22, 110, 4_015],
        "source_solution": [990, 22, 110],
    }
    if any(witness[key] != value for key, value in expected.items()):
        raise AssertionError("p=73 orientation-swap positive control changed")
    return witness


def run_audit() -> dict[str, object]:
    """Run the single-prime exclusion and its exact regression controls."""
    prime = PRIME
    if not sympy.isprime(prime) or prime % 24 != 1:
        raise AssertionError("the target is not a core prime")
    t = (prime - 1) // 4
    t_factors = exact_factorization(t)
    r_values = divisors_from_factorization(t_factors, 2)
    states = [audit_pminusone_state(prime, t, r) for r in r_values]
    totals = {
        "forced_r_state_count": len(states),
        "normalized_square_divisor_candidate_count": sum(
            int(state["normalized_square_divisor_candidate_count"]) for state in states
        ),
        "ordered_BCH_candidate_count": sum(
            int(state["ordered_BCH_candidate_count"]) for state in states
        ),
        "reachable_residue_count_sum": sum(
            int(state["reachable_residue_count"]) for state in states
        ),
        "ordered_residue_hit_count": sum(
            int(state["ordered_residue_hit_count"]) for state in states
        ),
        "normalized_residue_hit_count": sum(
            int(state["normalized_residue_hit_count"]) for state in states
        ),
        "valid_normal_form_hit_count": sum(
            int(state["valid_normal_form_hit_count"]) for state in states
        ),
        "orientation_swapped_count": sum(
            int(state["orientation_swapped_count"]) for state in states
        ),
        "natural_gap_verified_count": sum(
            int(state["natural_gap_verified_count"]) for state in states
        ),
    }
    expected = {
        "forced_r_state_count": 27,
        "normalized_square_divisor_candidate_count": 37_557,
        "ordered_BCH_candidate_count": 61_851,
        "reachable_residue_count_sum": 34_222,
        "ordered_residue_hit_count": 0,
        "normalized_residue_hit_count": 0,
        "valid_normal_form_hit_count": 0,
        "orientation_swapped_count": 0,
        "natural_gap_verified_count": 0,
    }
    if totals != expected:
        raise AssertionError("global p-1 exclusion totals changed")

    ordinary_tail = ordinary_type_ii_tail_audit(prime)
    if ordinary_tail["witness_count"] != 0:
        raise AssertionError("target unexpectedly has an ordinary Type II tail")
    shifted_bridge = shifted_b1_terminal_audit(prime)
    orientation_control = orientation_swap_positive_control()
    return {
        "arithmetic": (
            "for p=297049 set t=(p-1)/4; exhaust all r|t^2 forced by the "
            "p-1 bridge criterion, then for K=pr-t enumerate every ordered "
            "B*C*H=K state and cross-check every normalized d|K^2 state; "
            "normalize and orient every hit before checking its natural gap, "
            "coprimality, prime reconstruction, and exact target/source "
            "identities; also recompute the ordinary Type II p-1 tail and "
            "replay the p-25 B=1 bridge"
        ),
        "scope_note": (
            "Global means all Type I normal forms and all B for the repository's "
            "maximum-tail p-1 terminal bridge at this one prime. It does not "
            "exclude other Type I transformations or other Type II coordinates, "
            "and it is not a universal selector theorem. Calling this the first "
            "mixed-architecture forced shift additionally relies on the stored "
            "complete prefix audit, not on this single-prime enumeration alone."
        ),
        "prime": prime,
        "prime_is_core": True,
        "t": t,
        "t_factorization": [
            {"prime": factor, "exponent": exponent} for factor, exponent in t_factors
        ],
        "candidate_totals": totals,
        "p_minus_one_states": states,
        "ordinary_type_ii_p_minus_one_tail": ordinary_tail,
        "shifted_B_eq_1_terminal_bridge": shifted_bridge,
        "orientation_swap_positive_control_p73": orientation_control,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    summary = {
        key: value for key, value in result.items() if key != "p_minus_one_states"
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
