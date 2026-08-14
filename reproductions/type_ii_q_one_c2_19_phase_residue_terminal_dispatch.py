#!/usr/bin/env python3
"""Verify the finite q=1 C=2 19-phase affine terminal dispatch.

This enumerates only the exact 119 residue quotient and the 151 factor
triples forced by a fixed Type II raw ray.  It does not scan primes or
Egyptian-fraction solutions over an interval.
"""

from __future__ import annotations

import argparse
from collections import defaultdict

from short_certificate import (
    type_i_normal_form_certificate,
    type_ii_normal_form_certificate,
    type_ii_raw_ray_certificate,
    verify_certificate,
)


STEP = 912 * 119
MODULUS = 2_261
H_VALUES = (3, 7, 19, 51, 119, 323, 399, 6_783)
EXTRA_TYPE_II = {
    47: (1, 10, 3),
    48: (2, 5, 3),
    55: (3, 10, 1),
    61: (5, 6, 1),
    64: (6, 5, 1),
    71: (2, 3, 5),
    76: (10, 3, 1),
    82: (1, 3, 10),
    106: (1, 5, 6),
    110: (3, 5, 2),
    113: (5, 3, 2),
    118: (1, 6, 5),
}
EXTRA_TYPE_I = {
    33: (1, 17, 7),
    50: (1, 34, 7),
    89: (1, 17, 3),
}
AFFINE_TYPE_II = {
    # Fixed (A,B), with C affine in p=912u+769+STEP*t.
    13: (23, 6, 17, 31, 266),
    20: (31, 14, 17, 20, 114),
}
RESIDUAL = {
    1,
    5,
    6,
    8,
    15,
    19,
    22,
    26,
    27,
    34,
    36,
    40,
    41,
    43,
    54,
    57,
    62,
    68,
    69,
    75,
    78,
    83,
    85,
    90,
    92,
    96,
    99,
    103,
    104,
    111,
    117,
}


def divisors(value: int) -> tuple[int, ...]:
    result: list[int] = []
    candidate = 1
    while candidate * candidate <= value:
        if value % candidate == 0:
            result.append(candidate)
            other = value // candidate
            if other != candidate:
                result.append(other)
        candidate += 1
    return tuple(sorted(result))


def factor_triples(product: int) -> tuple[tuple[int, int, int], ...]:
    rows: list[tuple[int, int, int]] = []
    for a in divisors(product):
        for c in divisors(product // a):
            rows.append((a, c, product // (a * c)))
    return tuple(rows)


def prime_residue(u: int) -> int:
    return 912 * u + 769


def valid_residues() -> set[int]:
    return {
        u
        for u in range(119)
        if prime_residue(u) % 7 != 0 and prime_residue(u) % 17 != 0
    }


def type_ii_fixed_ray_coverage(valid: set[int]) -> dict[int, set[tuple[int, int, int, int]]]:
    candidate_h = tuple(h for h in divisors(STEP) if h % 4 == 3)
    if candidate_h != H_VALUES:
        raise AssertionError("the forced fixed-Type-II defining factors changed")

    coverage: dict[int, set[tuple[int, int, int, int]]] = defaultdict(set)
    triple_count = 0
    for h in candidate_h:
        triples = factor_triples((h + 1) // 4)
        triple_count += len(triples)
        for a, c, k in triples:
            if 4 * a * c * k - 1 != h:
                raise AssertionError("a Type II factor triple did not reconstruct h")
            for u in valid:
                base = prime_residue(u)
                if (k * base + a) % h:
                    continue
                for prime in (base, base + STEP):
                    certificate = type_ii_raw_ray_certificate(prime, a, c, k)
                    if certificate is None or not verify_certificate(certificate):
                        raise AssertionError("an affine Type II raw ray lost its terminal certificate")
                coverage[u].add((h, a, c, k))

    if triple_count != 151:
        raise AssertionError("the finite Type II factor-triple quotient changed")
    return coverage


def verify_type_i_extensions() -> None:
    for u, (a, b, gap) in EXTRA_TYPE_I.items():
        base = prime_residue(u)
        for prime in (base, base + STEP):
            certificate = type_i_normal_form_certificate(prime, gap, a, b)
            if certificate is None or not verify_certificate(certificate):
                raise AssertionError("an affine Type I normal form lost its terminal certificate")


def verify_affine_type_ii_extensions() -> None:
    for u, (gap, a, b, c_base, c_step) in AFFINE_TYPE_II.items():
        base = prime_residue(u)
        for parameter, prime in enumerate((base, base + STEP)):
            certificate = type_ii_normal_form_certificate(prime, gap, a, b)
            if certificate is None or not verify_certificate(certificate):
                raise AssertionError("an affine Type II normal form lost its terminal certificate")
            if (prime + gap) // (4 * a * b) != c_base + c_step * parameter:
                raise AssertionError("the affine Type II C coordinate changed")


def verify() -> None:
    valid = valid_residues()
    expected_u7 = {u for u in valid if u % 7 in {0, 2, 3}}
    expected_type_ii = expected_u7 | set(EXTRA_TYPE_II)
    coverage = type_ii_fixed_ray_coverage(valid)

    expected_h7 = {
        0: (7, 1, 2, 1),
        2: (7, 1, 1, 2),
        3: (7, 2, 1, 1),
    }
    for u in expected_u7:
        if expected_h7[u % 7] not in coverage[u]:
            raise AssertionError("a listed h=7 terminal template is missing")
    for u, (a, c, k) in EXTRA_TYPE_II.items():
        if (119, a, c, k) not in coverage[u]:
            raise AssertionError("a listed h=119 terminal template is missing")

    if not (
        len(valid) == 96
        and set(coverage) == expected_type_ii
        and len(expected_u7) == 48
        and len(EXTRA_TYPE_II) == 12
        and len(expected_type_ii) == 60
    ):
        raise AssertionError("the exact fixed-Type-II residue coverage changed")

    verify_type_i_extensions()
    verify_affine_type_ii_extensions()
    terminal = expected_type_ii | set(EXTRA_TYPE_I) | set(AFFINE_TYPE_II)
    if not (
        len(terminal) == 65
        and valid - terminal == RESIDUAL
        and len(RESIDUAL) == 31
        and not (set(EXTRA_TYPE_I) & expected_type_ii)
        and not (set(AFFINE_TYPE_II) & (expected_type_ii | set(EXTRA_TYPE_I)))
    ):
        raise AssertionError("the affine terminal dispatch partition changed")

    descending = 0
    for u in RESIDUAL:
        selector = (-1536 * pow(prime_residue(u), -1, MODULUS)) % MODULUS
        if selector <= 1547:
            descending += 1
    if descending != 20 or len(RESIDUAL) - descending != 11:
        raise AssertionError("the residual third-anchor capacity split changed")

    print(
        "verified q=1 C=2 affine terminal dispatch: "
        "62 Type II + 3 Type I terminal classes; 31 residual classes"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the finite affine receipt")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
