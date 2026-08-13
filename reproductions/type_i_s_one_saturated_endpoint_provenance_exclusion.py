#!/usr/bin/env python3
"""Verify the p=73 saturated s=1 endpoint provenance exclusion.

This focused verifier reconstructs one finite reverse raw closure and the
complete first-step menus of two named sources.  It performs no prime-range,
denominator, selector-history, or historical-result scan.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd, isqrt


P = 73
R = 16_463_572_454_087
K = 300_460_197_287_088
ENDPOINT = 451_141_437_368

EXPECTED_LAYERS = (
    (451_141_437_368,),
    (
        2_255_707_186_840,
        2_478_187_895_679,
        3_157_990_061_576,
        3_380_470_770_415,
        5_864_838_685_784,
        6_087_319_394_623,
        7_669_404_435_256,
    ),
    (
        673_622_146_207,
        4_072_632_975_692,
        5_185_036_519_887,
        7_434_563_687_037,
    ),
    (
        970_263_091_326,
        3_368_110_731_035,
        4_715_355_023_449,
        5_011_995_968_568,
        7_706_484_553_396,
    ),
    (
        1_427_584_548_383,
        3_850_152_266_849,
        4_851_315_456_630,
        6_791_841_639_282,
    ),
    (6_470_480_615_406, 7_137_922_741_915),
)

EXPECTED_EDGES = {
    (2_255_707_186_840, 5, 451_141_437_368),
    (2_478_187_895_679, 31, 451_141_437_368),
    (3_157_990_061_576, 7, 451_141_437_368),
    (3_380_470_770_415, 29, 451_141_437_368),
    (5_864_838_685_784, 13, 451_141_437_368),
    (6_087_319_394_623, 23, 451_141_437_368),
    (7_669_404_435_256, 17, 451_141_437_368),
    (673_622_146_207, 7, 2_255_707_186_840),
    (5_185_036_519_887, 5, 2_255_707_186_840),
    (4_072_632_975_692, 5, 2_478_187_895_679),
    (7_434_563_687_037, 3, 2_478_187_895_679),
    (673_622_146_207, 5, 3_157_990_061_576),
    (970_263_091_326, 23, 673_622_146_207),
    (3_368_110_731_035, 5, 673_622_146_207),
    (4_715_355_023_449, 7, 673_622_146_207),
    (5_011_995_968_568, 17, 673_622_146_207),
    (7_706_484_553_396, 13, 673_622_146_207),
    (3_850_152_266_849, 13, 970_263_091_326),
    (4_851_315_456_630, 5, 970_263_091_326),
    (6_791_841_639_282, 7, 970_263_091_326),
    (1_427_584_548_383, 3, 5_011_995_968_568),
    (6_470_480_615_406, 7, 1_427_584_548_383),
    (7_137_922_741_915, 5, 1_427_584_548_383),
}


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        exponent += 1
        value //= prime
    return exponent


def verified_factorization(value: int, factors: dict[int, int]) -> dict[int, int]:
    product = 1
    for prime, exponent in factors.items():
        if not is_prime(prime) or exponent <= 0:
            raise AssertionError("invalid claimed prime factorization")
        product *= prime**exponent
    if product != value:
        raise AssertionError("claimed factorization is incomplete")
    return factors


def primes_up_to(limit: int) -> list[int]:
    return [candidate for candidate in range(2, limit + 1) if is_prime(candidate)]


def bottom_predecessors(target: int) -> list[tuple[int, int]]:
    """Return all (source, q) labeled m=1 predecessors of N_target."""
    if not (1 <= target and 2 * target < R and gcd(target, R) == 1):
        raise AssertionError("target is not a canonical primitive bottom node")
    predecessors: list[tuple[int, int]] = []
    for prime in primes_up_to((R - 1) // target):
        if R % prime and valuation(target, prime) >= valuation(K, prime):
            source = min(prime * target, R - prime * target)
            predecessors.append((source, prime))
    return predecessors


def verify_bottom_edge(source: int, prime: int, target: int) -> None:
    selected = prime * target
    other = R - selected
    if not (
        selected > 0
        and other > 0
        and source == min(selected, other)
        and gcd(selected, other) == 1
        and valuation(selected, prime) > valuation(K, prime)
    ):
        raise AssertionError("reverse predecessor failed its source gates")
    shift = prime - 1
    output = (selected // prime, (other + R * shift) // prime)
    if min(output) != target or sum(output) != R or gcd(*output) != 1:
        raise AssertionError("reverse predecessor did not replay to its target")


def verify_reverse_closure() -> set[int]:
    seen = {ENDPOINT}
    frontier = {ENDPOINT}
    layers: list[tuple[int, ...]] = [(ENDPOINT,)]
    edges: set[tuple[int, int, int]] = set()

    while frontier:
        new: set[int] = set()
        for target in frontier:
            for source, prime in bottom_predecessors(target):
                verify_bottom_edge(source, prime, target)
                edges.add((source, prime, target))
                if source not in seen:
                    new.add(source)
        if not new:
            break
        seen.update(new)
        layers.append(tuple(sorted(new)))
        frontier = new

    if tuple(layers) != EXPECTED_LAYERS:
        raise AssertionError("reverse-reach layers changed")
    if edges != EXPECTED_EDGES or len(seen) != 23 or len(edges) != 23:
        raise AssertionError("reverse-reach graph changed")
    if any(source not in seen for target in seen for source, _ in bottom_predecessors(target)):
        raise AssertionError("reverse-reach set is not predecessor closed")
    return seen


def raw_successor(U: int, V: int, m: int, prime: int) -> tuple[int, int]:
    if (U % prime == 0) == (V % prime == 0):
        raise AssertionError("raw label does not select exactly one coordinate")
    selected, other = (U, V) if U % prime == 0 else (V, U)
    if valuation(selected, prime) <= valuation(K, prime):
        raise AssertionError("raw label is not over capacity")
    shift = (-m) % prime
    if not 1 <= shift < prime:
        raise AssertionError("raw shift left its canonical range")
    selected //= prime
    other = (other + R * shift) // prime
    new_m = (m + shift) // prime
    reduction = gcd(selected, other)
    if new_m % reduction:
        raise AssertionError("gcd reduction does not divide the new layer")
    selected //= reduction
    other //= reduction
    new_m //= reduction
    if selected + other != R * new_m or gcd(selected, other) != 1:
        raise AssertionError("raw successor is not primitive")
    return min(selected, other), new_m


def source_excess_labels(
    U: int,
    V: int,
    m: int,
    U_factors: dict[int, int],
    V_factors: dict[int, int],
    K_factors: dict[int, int],
) -> set[int]:
    verified_factorization(U, U_factors)
    verified_factorization(V, V_factors)
    if U + V != R * m or gcd(U, V) != 1:
        raise AssertionError("named source is not primitive")
    factors = dict(U_factors)
    for prime, exponent in V_factors.items():
        factors[prime] = factors.get(prime, 0) + exponent
    return {
        prime
        for prime, exponent in factors.items()
        if exponent > K_factors.get(prime, 0)
    }


def verify_named_source_exclusion(reverse_closure: set[int]) -> None:
    K_factors = verified_factorization(
        K, {2: 4, 3: 2, 37: 1, 1_801: 1, 31_311_871: 1}
    )

    universal = (P, R * (P - 1) - P, P - 1)
    universal_labels = source_excess_labels(
        *universal,
        {P: 1},
        {521: 1, 2_275_196_193_271: 1},
        K_factors,
    )
    universal_successors = {
        prime: raw_successor(*universal, prime) for prime in universal_labels
    }
    if universal_successors != {
        73: (1, 1),
        521: (2_275_196_193_271, 1),
        2_275_196_193_271: (521, 1),
    }:
        raise AssertionError("universal p-source first-step menu changed")

    if not (
        (R * K * (R - 1)) % 2 == 0
        and (R * K * (R - 1)) % 3 == 0
        and (R * K * (R - 1)) % 5 != 0
    ):
        raise AssertionError("least-coprime source prime is no longer 5")
    q_star = (5, R * 4 - 5, 4)
    q_star_labels = source_excess_labels(
        *q_star,
        {5: 1},
        {3: 2, 7: 1, 5_641: 1, 5_717: 1, 32_413: 1},
        K_factors,
    )
    q_star_successors = {
        prime: raw_successor(*q_star, prime) for prime in q_star_labels
    }
    if q_star_successors != {
        5: (1, 1),
        7: (7_055_816_766_038, 1),
        5_641: (11_674_222_623, 1),
        5_717: (11_519_029_179, 1),
        32_413: (2_031_724_611, 1),
    }:
        raise AssertionError("q-star source first-step menu changed")

    first_bottom_nodes = {
        node
        for node, layer in (
            list(universal_successors.values()) + list(q_star_successors.values())
        )
        if layer == 1
    }
    if first_bottom_nodes & reverse_closure:
        raise AssertionError("a named source acquired a path to the saturated endpoint")


def complete_excess(value: int, capacity: int) -> tuple[int, int]:
    common = gcd(value, capacity)
    exposed = value // common
    block = gcd(value, pow(exposed, value.bit_length(), value))
    return block, value // block


def verify_static_receipt_and_terminal() -> None:
    r0 = 21_164_451
    h = ENDPOINT
    g = (P + 1) // 2
    b = 2 * P * r0 - 1
    n = (P + 1) * b - 1
    support = g * (P * P * r0 - g)
    residual = (P - 1) * n - 1
    capacity = support * (P - 1)
    block = 5_337_477_005_573
    beta = 3
    t = 1_001_590_731
    z = residual - h

    if not (
        (support, residual, capacity) == (4_173_058_295_654, R, K)
        and h < R // 2
        and gcd(h, z) == 1
        and z == block * beta
        and complete_excess(z, capacity) == (block, beta)
        and gcd(support, block) == 1
        and capacity % (h * beta) == 0
        and block == 1 + P * (1 + P * t)
    ):
        raise AssertionError("static saturated endpoint receipt changed")

    relay = (block - 1) // P
    checkpoint_b = block * b - relay
    checkpoint_multiplier = (P - 1) * checkpoint_b - 1
    quotient = (checkpoint_multiplier - 1) // P
    final_b = checkpoint_b * checkpoint_multiplier - quotient
    final_multiplier = (P - 1) * final_b - 1
    final_n = (P + 1) * final_b - 1
    final_support = (P * final_n - 1) // 4
    final_capacity = final_support * (P - 1)
    final_residual = (P - 1) * final_n - 1

    if not (
        checkpoint_b == 16_492_856_494_608_573_742_821
        and checkpoint_multiplier == 1_187_485_667_611_817_309_483_111
        and valuation(checkpoint_multiplier - 1, P) == 1
        and ((checkpoint_multiplier - 1) // P) % P == P - 1
        and final_b
        == 19_585_030_705_326_159_181_134_936_369_307_691_371_618_510_061
        and valuation(final_multiplier, P) == 1
        and gcd(final_residual - (P + 1), final_capacity) == P * P + P + 1
        and Fraction(4, P)
        == Fraction(1, 20) + Fraction(1, 219) + Fraction(1, 4_380)
    ):
        raise AssertionError("s=1 return or terminal-first receipt changed")


def verify() -> None:
    reverse_closure = verify_reverse_closure()
    verify_named_source_exclusion(reverse_closure)
    verify_static_receipt_and_terminal()
    print(
        "verified the 23-node/23-edge reverse closure, both named-source "
        "exclusions, the saturated s=1 return, and the p=73 Type II intercept"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
