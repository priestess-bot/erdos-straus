#!/usr/bin/env python3
"""Verify a scale-15 mixed-factor transition in a post-affine H19 residual.

The v=17 k=23 residual contains the prime

    p=69,252,070,248,001 = P*44+C.

Every permitted scale k<15 has no mixed-factor witness g|k*n_k with
g<=n_k and g=-1 mod (4k-1).  At the next permitted scale k=15,
g=353 gives an exact strict external-source lift.  The complete
factorizations below make this a finite, dependency-free transition witness.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "mixed-factor-h19-scale-transition-witness.json"

P = 1_552_726_375_200
C = 932_109_739_201
PARAMETER = 44
PRIME = P * PARAMETER + C
BASE = (PRIME - 1) // 4

# Complete factorizations of M_k=k*n_k=((4k-1)*p+1)/4.
FACTORIZATIONS = {
    1: ((13, 1), (7_177, 1), (8_761, 1), (63_541, 1)),
    2: ((2, 1), (11, 1), (5_508_687_406_091, 1)),
    3: ((3, 1), (63_481_064_394_001, 1)),
    4: ((2, 2), (64_923_815_857_501, 1)),
    5: ((5, 1), (7, 1), (9_398_495_247_943, 1)),
    6: ((2, 1), (3, 1), (197, 1), (929, 1), (362_633_077, 1)),
    8: ((2, 3), (43, 1), (757, 1), (2_061_010_201, 1)),
    9: ((3, 2), (67_328_401_630_001, 1)),
    10: ((2, 1), (5, 1), (67_520_768_491_801, 1)),
    12: ((2, 2), (3, 1), (7, 1), (37, 1), (261_812_041_639, 1)),
    15: ((3, 1), (5, 1), (353, 1), (461, 1), (418_463_797, 1)),
}


def is_prime(value: int) -> bool:
    """Deterministic Miller--Rabin for the range used in this witness."""
    if value < 2:
        return False
    for prime in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if value == prime:
            return True
        if value % prime == 0:
            return False
    exponent = value - 1
    power = 0
    while exponent % 2 == 0:
        exponent //= 2
        power += 1
    # Valid for every integer below 3.4e14, in fact far beyond this range.
    for base in (2, 3, 5, 7, 11, 13, 17):
        residue = pow(base, exponent, value)
        if residue in (1, value - 1):
            continue
        for _ in range(power - 1):
            residue = residue * residue % value
            if residue == value - 1:
                break
        else:
            return False
    return True


def divisors(factorization: tuple[tuple[int, int], ...]) -> tuple[int, ...]:
    return tuple(
        sorted(
            value
            for powers in product(
                *(range(exponent + 1) for _, exponent in factorization)
            )
            for value in [
                math.prod(
                    prime**power
                    for (prime, _), power in zip(factorization, powers)
                )
            ]
        )
    )


def source_denominator(scale: int) -> int:
    q = 4 * scale - 1
    numerator = q * PRIME + 1
    if numerator % (4 * scale):
        raise AssertionError("scale does not divide (p-1)/4")
    return numerator // (4 * scale)


def mixed_hits(scale: int) -> list[int]:
    q = 4 * scale - 1
    source = source_denominator(scale)
    product_value = scale * source
    factorization = FACTORIZATIONS[scale]
    if product_value != math.prod(
        prime**exponent for prime, exponent in factorization
    ):
        raise AssertionError("stored factorization has wrong product")
    if not all(is_prime(prime) for prime, _ in factorization):
        raise AssertionError("stored factorization has a composite factor")
    return [
        factor
        for factor in divisors(factorization)
        if factor <= source and factor % q == q - 1
    ]


def verify_scale_15_witness() -> dict[str, int]:
    scale = 15
    q = 4 * scale - 1
    source = source_denominator(scale)
    factor = 353
    if factor not in mixed_hits(scale):
        raise AssertionError("expected scale-15 mixed factor is absent")
    first_tail = scale * (source + factor) // q
    second_tail = source * first_tail // factor
    if Fraction(4, source) != (
        Fraction(1, scale * source)
        + Fraction(1, first_tail)
        + Fraction(1, second_tail)
    ):
        raise AssertionError("source identity failed")
    if Fraction(4, PRIME) != (
        Fraction(1, scale * source * PRIME)
        + Fraction(1, first_tail)
        + Fraction(1, second_tail)
    ):
        raise AssertionError("strict lift identity failed")
    return {
        "k": scale,
        "q": q,
        "source_denominator": source,
        "mixed_factor": factor,
        "first_tail": first_tail,
        "second_tail": second_tail,
    }


def run_audit() -> dict[str, object]:
    if not is_prime(PRIME):
        raise AssertionError("designated residual value must be prime")
    if PRIME % 24 != 1 or BASE != 17_313_017_562_000:
        raise AssertionError("unexpected residual prime")
    permitted_smaller = tuple(
        scale for scale in FACTORIZATIONS if scale < 15 and BASE % scale == 0
    )
    if permitted_smaller != (1, 2, 3, 4, 5, 6, 8, 9, 10, 12):
        raise AssertionError("incomplete smaller-scale list")
    smaller_rows = [
        {"k": scale, "mixed_factor_hits": mixed_hits(scale)}
        for scale in permitted_smaller
    ]
    if any(row["mixed_factor_hits"] for row in smaller_rows):
        raise AssertionError("a smaller permitted scale unexpectedly succeeds")
    witness = verify_scale_15_witness()
    return {
        "arithmetic": (
            "deterministic primality checks, complete factorizations of every "
            "k*n_k through the first successful scale, divisor enumeration, "
            "and exact Fraction verification of the strict lift"
        ),
        "scope_note": (
            "One exact residual-prime transition witness. It shows a bounded "
            "small-scale failure can recover at a larger adaptive scale; it is "
            "not a uniform scale-selection theorem."
        ),
        "residual_state": {
            "v_mod_29": 17,
            "parameter": PARAMETER,
            "prime": PRIME,
            "base": BASE,
        },
        "smaller_permitted_scales": smaller_rows,
        "first_success": witness,
    }


def main() -> int:
    payload = run_audit()
    RESULTS.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
