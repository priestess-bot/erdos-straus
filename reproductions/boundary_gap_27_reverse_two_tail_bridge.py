#!/usr/bin/env python3
"""Audit complete two-tail-preserving reverse lifts at the 500M boundary point.

For a target term t, put R=4t-p and D=4pt-nR.  Every reverse lift has
``D | 4*p^2*t^2``.  This turns the otherwise p-sized scan over source
denominators into an exact finite divisor scan after the target term is
factored.
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
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
LANDSCAPE = ROOT / "reproductions" / "boundary_gap_certificate_landscape.py"
DEFAULT_PRIME = 477_015_289
DEFAULT_GAP = 27
DEFAULT_OUTPUT = ROOT / "reproductions" / "boundary-gap-27-reverse-two-tail-477015289-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_module(
    "boundary_gap_27_reverse_short_certificate", SHORT_CERTIFICATE
)
landscape = load_module("boundary_gap_27_reverse_landscape", LANDSCAPE)


def merge_factorizations(*factorizations: dict[int, int]) -> dict[int, int]:
    result: dict[int, int] = {}
    for factorization in factorizations:
        for prime, exponent in factorization.items():
            result[prime] = result.get(prime, 0) + exponent
    return dict(sorted(result.items()))


def factor_product(*values: int) -> dict[int, int]:
    if any(value <= 0 for value in values):
        raise ValueError("factorized values must be positive")
    return merge_factorizations(
        *(landscape.factor_by_trial_division(value) for value in values)
    )


def multiply_factorization(factors: dict[int, int]) -> int:
    return math.prod(prime**exponent for prime, exponent in factors.items())


def divisors_from_factorization(factors: dict[int, int]) -> list[int]:
    divisors = [1]
    for prime, exponent in factors.items():
        divisors = [
            base * prime**power
            for base in divisors
            for power in range(exponent + 1)
        ]
    return divisors


def reverse_two_tail_lifts_by_divisors(
    prime: int, target_term: int, target_factors: dict[int, int] | None = None
) -> tuple[int, list[dict[str, int]]]:
    """Return every strict reverse lift by exhaustively scanning its D divisors.

    A lift has ``4/n = 1/a + (4/p - 1/t)``.  With ``R=4t-p`` and
    ``D=4pt-nR``, it is equivalent to a positive divisor D of ``4p^2t^2``
    satisfying the displayed reconstruction tests below.  The returned count
    is the number of such divisors reaching a valid source denominator before
    the final source-term integrality filter.
    """
    if prime < 2 or target_term < 1:
        raise ValueError("prime and target_term must be positive")
    R = 4 * target_term - prime
    if R <= 0:
        return 0, []
    if target_factors is None:
        target_factors = landscape.factor_by_trial_division(target_term)
    if multiply_factorization(target_factors) != target_term:
        raise ValueError("target factorization does not reconstruct target_term")
    constant_factors = merge_factorizations(
        {2: 2},
        {prime_factor: 2 * exponent for prime_factor, exponent in landscape.factor_by_trial_division(prime).items()},
        {prime_factor: 2 * exponent for prime_factor, exponent in target_factors.items()},
    )
    eligible_count = 0
    lifts: list[dict[str, int]] = []
    for D in divisors_from_factorization(constant_factors):
        if D >= 4 * prime * target_term:
            continue
        numerator_n = 4 * prime * target_term - D
        if numerator_n % R:
            continue
        source_denominator = numerator_n // R
        if not 2 <= source_denominator < prime:
            continue
        eligible_count += 1
        numerator_a = source_denominator * prime * target_term
        if numerator_a % D:
            continue
        source_term = numerator_a // D
        if (
            Fraction(4, source_denominator)
            != Fraction(1, source_term)
            + Fraction(4, prime)
            - Fraction(1, target_term)
        ):
            raise AssertionError("reverse divisor lift identity did not verify")
        lifts.append(
            {
                "source_denominator": source_denominator,
                "source_term": source_term,
                "bridge_divisor": D,
            }
        )
    return eligible_count, sorted(lifts, key=lambda item: (item["source_denominator"], item["source_term"]))


def type_i_target_factorizations(prime: int, gap: int, A: int, B: int, C: int) -> list[dict[int, int]]:
    """Factor the three Type I target terms from their normal-form factors."""
    R = (4 * B * B * C + 1) // gap
    if gap * R != 4 * B * B * C + 1:
        raise AssertionError("normal form does not have an integral quotient")
    x_factors = factor_product(A, B, C)
    y_factors = factor_product(A, C, A * R - B)
    z_factors = factor_product(prime, B, C, A * R - B)
    return [x_factors, y_factors, z_factors]


def type_i_normal_reverse_two_tail_lifts(
    prime: int, gap: int, A: int, B: int, C: int
) -> tuple[int, list[dict[str, int]]]:
    """Reverse every maximum-tail lift from one Type I normal form.

    Put ``R=(4*B^2*C+1)/gap``, ``H=A*R-B``, and ``K=B*C*H``.  The
    target is ``(A*B*C, A*C*H, p*K)``, while its first two terms sum to
    ``R/K`` and ``4*K=p*R+1``.  A source retaining them has
    ``4/n=1/a+R/K``.  If ``E=4*K-n*R``, then necessarily ``E|4*K^2``;
    conversely the reconstruction checks below are sufficient.  This is the
    maximum-coordinate specialization of the generic D-divisor reverse scan
    with ``D=p^2*E``.
    """
    R = (4 * B * B * C + 1) // gap
    if gap * R != 4 * B * B * C + 1:
        raise ValueError("normal-form quotient is not integral")
    H = A * R - B
    K = B * C * H
    if H <= 0 or 4 * K != prime * R + 1:
        raise ValueError("normal form does not reconstruct its p-tail")
    target = (A * B * C, A * C * H, prime * K)
    if Fraction(4, prime) != sum((Fraction(1, term) for term in target), Fraction()):
        raise AssertionError("normal-form target identity did not verify")
    K_factors = factor_product(B, C, H)
    constant_factors = merge_factorizations(
        {2: 2}, {q: 2 * exponent for q, exponent in K_factors.items()}
    )
    eligible_count = 0
    lifts: list[dict[str, int]] = []
    for E in divisors_from_factorization(constant_factors):
        if E >= 4 * K:
            continue
        numerator_n = 4 * K - E
        if numerator_n % R:
            continue
        source_denominator = numerator_n // R
        if not 2 <= source_denominator < prime:
            continue
        eligible_count += 1
        numerator_a = source_denominator * K
        if numerator_a % E:
            continue
        source_term = numerator_a // E
        source = (source_term, target[0], target[1])
        if Fraction(4, source_denominator) != sum(
            (Fraction(1, term) for term in source), Fraction()
        ):
            raise AssertionError("normal-form reverse source identity did not verify")
        lifts.append(
            {
                "source_denominator": source_denominator,
                "source_term": source_term,
                "bridge_divisor": prime * prime * E,
            }
        )
    return eligible_count, sorted(lifts, key=lambda item: (item["source_denominator"], item["source_term"]))


def run_audit(prime: int = DEFAULT_PRIME, gap: int = DEFAULT_GAP) -> dict[str, object]:
    gap_entry = landscape.gap_landscape(prime, gap)
    records: list[dict[str, object]] = []
    total_lifts = 0
    for entry in gap_entry["type_i"]:
        A, B, C = entry["normal_form"]
        certificate = short_certificate.type_i_normal_form_certificate(prime, gap, A, B)
        if certificate is None:
            raise AssertionError("stored normal form did not rebuild")
        target = (certificate.x, certificate.y, certificate.z)
        term_factors = type_i_target_factorizations(prime, gap, A, B, C)
        if [multiply_factorization(factors) for factors in term_factors] != list(target):
            raise AssertionError("normal-form term factorization did not reconstruct")
        term_records: list[dict[str, object]] = []
        for position, (target_term, factors) in enumerate(zip(target, term_factors)):
            if position == 2:
                eligible_count, lifts = type_i_normal_reverse_two_tail_lifts(
                    prime, gap, A, B, C
                )
            else:
                eligible_count, lifts = reverse_two_tail_lifts_by_divisors(
                    prime, target_term, factors
                )
            for lift in lifts:
                source = (
                    lift["source_term"],
                    *(term for index, term in enumerate(target) if index != position),
                )
                if Fraction(4, lift["source_denominator"]) != sum(
                    (Fraction(1, term) for term in source), Fraction()
                ):
                    raise AssertionError("source triple did not verify")
            total_lifts += len(lifts)
            term_records.append(
                {
                    "replaced_target_position": position,
                    "target_term": target_term,
                    "target_term_factorization": {str(q): exponent for q, exponent in factors.items()},
                    "eligible_bridge_divisor_count": eligible_count,
                    "reverse_two_tail_lifts": lifts,
                }
            )
        records.append(
            {
                "divisor": entry["divisor"],
                "normal_form": [A, B, C],
                "target_solution": list(target),
                "reverse_two_tail_by_replaced_target_term": term_records,
            }
        )
    return {
        "arithmetic": (
            "for each gap-27 Type I normal form, factor its three target terms "
            "from the normal-form products; enumerate every D|4*p^2*t^2; "
            "reconstruct n=(4pt-D)/(4t-p) and a=npt/D; verify each source and target identity exactly"
        ),
        "scope_note": (
            "This exhausts only one-coordinate reverse lifts preserving the other "
            "two terms of the three gap-27 Type I target triples. It does not "
            "exclude other gaps, Type II triples, or lifts changing more coordinates."
        ),
        "prime": prime,
        "gap": gap,
        "type_i_certificate_count": len(records),
        "total_reverse_two_tail_lift_count": total_lifts,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prime", type=int, default=DEFAULT_PRIME)
    parser.add_argument("--gap", type=int, default=DEFAULT_GAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.prime, args.gap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
