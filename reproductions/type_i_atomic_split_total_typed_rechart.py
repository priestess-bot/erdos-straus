#!/usr/bin/env python3
"""Verify total typed rechart controls for a strict atomic split.

The script keeps the expensive-looking constructions finite and explicit.  It
does not search prime ranges, enumerate Egyptian-fraction certificates beyond
the one fixed priority control, or claim a persistent H4 edge from a local
atomic arithmetic fixture.
"""

from __future__ import annotations

import argparse
from itertools import product
from math import gcd, prod

import type_i_atomic_split_s_zero_endpoint_boundary as atomic


ATOMIC_TARGET_FACTORS = (
    (2, 2),
    (3, 3),
    (5, 1),
    (7, 2),
    (11, 1),
    (13, 1),
    (37, 1),
    (67, 1),
    (152_381, 1),
)


def factorint(value: int) -> tuple[tuple[int, int], ...]:
    """Factor a small fixed control integer by exact trial division."""
    factors: list[tuple[int, int]] = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor:
            divisor = 3 if divisor == 2 else divisor + 2
            continue
        exponent = 0
        while value % divisor == 0:
            value //= divisor
            exponent += 1
        factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors.append((value, 1))
    return tuple(factors)


def divisor_list(value: int) -> tuple[int, ...]:
    """List all divisors of a small exact control value."""
    values = [1]
    for prime, exponent in factorint(value):
        values = [
            item * prime_power
            for item in values
            for prime_power in (prime**power for power in range(exponent + 1))
        ]
    return tuple(sorted(values))


def direct_type_i_ii_screen(prime: int) -> tuple[str, int, int] | None:
    """Return the canonical finite Bradford Type I/II divisor receipt, if any."""
    candidates: list[tuple[int, int, int, str]] = []
    for gap in range(3, prime - 1, 4):
        x = (prime + gap) // 4
        for divisor in divisor_list(x * x):
            if (prime * x + divisor) % gap == 0:
                candidates.append((gap, 0, divisor, "I"))
            if divisor <= x and (x + divisor) % gap == 0:
                candidates.append((gap, 1, divisor, "II"))
    if not candidates:
        return None
    gap, _, divisor, kind = min(candidates)
    return kind, gap, divisor


def direct_certificate_denominators(
    prime: int, kind: str, gap: int, divisor: int
) -> tuple[int, int, int]:
    """Materialize a screened Bradford Type I/II unit-fraction receipt."""
    x = (prime + gap) // 4
    if kind == "I":
        if (prime * x + divisor) % gap:
            raise AssertionError("unscreened Type I divisor")
        y = (prime * x + divisor) // gap
        if prime * x * y % divisor:
            raise AssertionError("Type I final denominator is not integral")
        z = prime * x * y // divisor
    elif kind == "II":
        if divisor > x or (x + divisor) % gap:
            raise AssertionError("unscreened Type II divisor")
        y = prime * (x + divisor) // gap
        if x * y % divisor:
            raise AssertionError("Type II final denominator is not integral")
        z = x * y // divisor
    else:
        raise ValueError("unknown direct certificate kind")
    if not (
        4 * x == prime + gap
        and divisor > 0
        and x * x % divisor == 0
        and x > 0
        and y > 0
        and z > 0
        and 4 * x * y * z == prime * (x * y + x * z + y * z)
    ):
        raise AssertionError("direct certificate did not reconstruct")
    return x, y, z


def residue(
    factors: tuple[tuple[int, int], ...], vector: tuple[int, ...], modulus: int
) -> int:
    """Evaluate the signed support product modulo a coprime chart modulus."""
    if len(factors) != len(vector):
        raise ValueError("factor/vector lengths differ")
    value = 1
    for (prime, _), exponent in zip(factors, vector, strict=True):
        value = value * pow(prime, exponent, modulus) % modulus
    return value


def bounded_hits(
    factors: tuple[tuple[int, int], ...], modulus: int
) -> tuple[tuple[int, ...], ...]:
    """Enumerate the finite centered box only; this is the hit test."""
    ranges = tuple(range(-exponent, exponent + 1) for _, exponent in factors)
    hits = [
        vector
        for vector in product(*ranges)
        if residue(factors, vector, modulus) == modulus - 1
    ]
    return tuple(sorted(hits, key=lambda row: (sum(map(abs, row)), row)))


def subgroup(generators: tuple[int, ...], modulus: int) -> set[int]:
    """Build a finite generated subgroup for the small F/G controls."""
    if any(gcd(value, modulus) != 1 for value in generators):
        raise AssertionError("support is not a unit modulo the chart modulus")
    steps = tuple(
        sorted(
            set(generators)
            | {pow(value, -1, modulus) for value in generators}
        )
    )
    values = {1}
    frontier = [1]
    while frontier:
        value = frontier.pop()
        for step in steps:
            successor = value * step % modulus
            if successor not in values:
                values.add(successor)
                frontier.append(successor)
    return values


def small_chart_classification(
    modulus: int, support: int
) -> tuple[str, tuple[int, ...] | None]:
    """Return a canonical hit/F/G label on a small complete chart control."""
    factors = factorint(support)
    hits = bounded_hits(factors, modulus)
    if hits:
        return "hit", hits[0]
    generators = tuple(prime % modulus for prime, _ in factors)
    generated = subgroup(generators, modulus)
    if modulus - 1 not in generated:
        return "G", None
    for radius in range(1, len(generated)):
        shell = [
            vector
            for vector in product(range(-radius, radius + 1), repeat=len(factors))
            if sum(map(abs, vector)) == radius
            and residue(factors, vector, modulus) == modulus - 1
        ]
        if shell:
            return "F", min(shell)
    raise AssertionError("subgroup membership did not yield an F witness")


def legendre(value: int, odd_prime: int) -> int:
    """Return the quadratic character modulo a fixed odd prime."""
    result = pow(value % odd_prime, (odd_prime - 1) // 2, odd_prime)
    if result == 1:
        return 1
    if result == odd_prime - 1:
        return -1
    raise AssertionError("Legendre input is not a unit")


def signed_defect(
    factors: tuple[tuple[int, int], ...], vector: tuple[int, ...]
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Recompute the globally directed D-minus/D-plus pair from the contract."""
    negative = tuple(
        max(-exponent - bound, 0)
        for (_, bound), exponent in zip(factors, vector, strict=True)
    )
    positive = tuple(
        max(exponent - bound, 0)
        for (_, bound), exponent in zip(factors, vector, strict=True)
    )
    return negative, positive


def verify_total_typed_trichotomy() -> None:
    """Replay canonical hit/F/G outcomes and an explicit G separator."""
    assert small_chart_classification(3, 55) == ("hit", (-1, 0))
    assert small_chart_classification(383, 6_990) == ("F", (-2, 0, 0, 3))
    assert small_chart_classification(11, 201) == ("G", None)

    # The Legendre character is a compact separating-character control for G.
    assert factorint(201) == ((3, 1), (67, 1))
    assert legendre(3, 11) == legendre(67, 11) == 1
    assert legendre(-1, 11) == -1

    # The source-independent finite screen preempts this p=73 arithmetic fixture.
    assert direct_type_i_ii_screen(73) == ("I", 7, 10)
    assert direct_certificate_denominators(73, "I", 7, 10) == (20, 210, 30_660)
    assert direct_certificate_denominators(73, "II", 7, 1) == (20, 219, 4_380)


def verify_strict_atomic_target() -> None:
    """Reclassify one strict atomic target without treating it as persistent."""
    source = atomic.chart(73, 1)
    x, y = atomic.peeled_pair(source, anchor=1)
    split = atomic.split_data(source, x, y)
    target_support = int(split["target_support"])
    target_capacity = int(split["target_capacity"])
    target_residual = int(split["target_residual"])
    factors = ATOMIC_TARGET_FACTORS
    witness = (111_621_836, 4_010_792_179_018, 3, 0, 0, 0, 0, 0, 0)
    defects = signed_defect(factors, witness)

    if not (
        factorint(152_381) == ((152_381, 1),)
        and target_support == 21_333_318_666_660
        and target_capacity == 1_429_332_350_666_220
        and target_residual == 78_319_580_858_423
        and prod(prime**exponent for prime, exponent in factors) == target_capacity
        and 73 * target_residual + 1 == 4 * target_capacity
        and gcd(target_capacity, target_residual) == 1
        and not bounded_hits(factors, target_residual)
        and residue(factors, witness, target_residual) == target_residual - 1
        and defects
        == ((0, 0, 0, 0, 0, 0, 0, 0, 0), (111_621_834, 4_010_792_179_015, 2, 0, 0, 0, 0, 0, 0))
    ):
        raise AssertionError("strict atomic target F reclassification changed")


def verify() -> None:
    verify_total_typed_trichotomy()
    verify_strict_atomic_target()
    print(
        "verified total Type I chart hit/F/G controls, a G separator, "
        "the finite direct-priority screen, and a strict atomic F target"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused exact controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
