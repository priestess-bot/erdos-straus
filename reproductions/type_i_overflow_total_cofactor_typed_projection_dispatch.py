#!/usr/bin/env python3
"""Verify typed total-cofactor projection dispatch and persistence controls."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import prod

from type_i_overflow_total_cofactor_canonical_projection_rank import (
    p1201_macro_provenance,
)


@dataclass(frozen=True)
class TypedFoldFixture:
    label: str
    p: int
    A: int
    M: int
    d: int
    n: int
    expected_types: tuple[str, str]


FIXTURES = (
    TypedFoldFixture("F_to_G", 73, 3, 45, 15, 37, ("F", "G")),
    TypedFoldFixture("G_to_F", 73, 22, 220, 18, 217, ("G", "F")),
    TypedFoldFixture("F_to_hit", 73, 5, 40, 26, 57, ("F", "hit")),
)


def factorint(value: int) -> tuple[tuple[int, int], ...]:
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


def subgroup(generators: tuple[int, ...], modulus: int) -> set[int]:
    values = {1 % modulus}
    frontier = [1 % modulus]
    steps = tuple(sorted(set(generators) | {pow(value, -1, modulus) for value in generators}))
    while frontier:
        value = frontier.pop()
        for step in steps:
            successor = value * step % modulus
            if successor not in values:
                values.add(successor)
                frontier.append(successor)
    return values


def typed_classification(R: int, K: int) -> tuple[str, tuple[int, ...] | None]:
    factors = factorint(K)
    primes = tuple(q for q, _ in factors)
    ranges = tuple(range(-nu, nu + 1) for _, nu in factors)
    target = R - 1
    hits: list[tuple[int, ...]] = []
    for vector in product(*ranges):
        residue = prod(
            pow(q, exponent, R)
            for q, exponent in zip(primes, vector, strict=True)
        ) % R
        if residue == target:
            hits.append(vector)
    if hits:
        return "hit", min(hits, key=lambda row: (sum(map(abs, row)), row))

    H = subgroup(tuple(q % R for q in primes), R)
    if target not in H:
        return "G", None

    # Exact L1 shells implement the stated (norm, vector) canonical order.
    # A shortest Cayley path is simple, so radius |H|-1 is sufficient.
    for radius in range(1, len(H)):
        shell_hits: list[tuple[int, ...]] = []
        for vector in product(range(-radius, radius + 1), repeat=len(primes)):
            if sum(map(abs, vector)) != radius:
                continue
            residue = prod(
                pow(q, exponent, R)
                for q, exponent in zip(primes, vector, strict=True)
            ) % R
            if residue == target:
                shell_hits.append(vector)
        if shell_hits:
            return "F", min(shell_hits)
    raise AssertionError("subgroup membership must yield an F witness")


def fold(fixture: TypedFoldFixture) -> dict[str, object]:
    p, A, M, d, n = fixture.p, fixture.A, fixture.M, fixture.d, fixture.n
    assert p * n == 4 * M * d + 1 and M % A == 0
    source_R = 4 * M - n
    source_K = M * (p - d)
    C_A = pow(4 * A, -1, p)
    target_R = (4 * A * C_A - 1) // p
    target_K = A * C_A
    h, delta = divmod((M // A) * d, p)
    target_n = n - 4 * A * h
    t = (source_K // A - C_A) // p
    assert delta == p - C_A and target_n == 4 * A - target_R
    assert p * target_R + 1 == 4 * target_K and p * target_n == 4 * A * delta + 1
    assert t > 0 and source_K - target_K == A * p * t

    source_type, source_witness = typed_classification(source_R, source_K)
    target_type, target_witness = typed_classification(target_R, target_K)
    assert (source_type, target_type) == fixture.expected_types
    return {
        "source": (source_R, source_K, A),
        "target": (target_R, target_K, A),
        "types": (source_type, target_type),
        "source_witness": source_witness,
        "target_witness": target_witness,
        "t": t,
    }


def legendre(value: int, odd_prime: int) -> int:
    residue = pow(value % odd_prime, (odd_prime - 1) // 2, odd_prime)
    return -1 if residue == odd_prime - 1 else residue


def verify_explicit_certificates(receipts: dict[str, dict[str, object]]) -> None:
    first = receipts["F_to_G"]
    assert first["target"] == (11, 201, 3)
    assert legendre(3, 11) == legendre(67, 11) == 1
    assert legendre(-1, 11) == -1

    second = receipts["G_to_F"]
    assert second["target"] == (47, 858, 22)
    for q, _ in factorint(12100):
        assert legendre(q, 3) * legendre(q, 13) == 1
    assert legendre(-1, 3) * legendre(-1, 13) == -1
    assert second["target_witness"] == (-2, 1, -1, 0)

    third = receipts["F_to_hit"]
    assert third["target"] == (3, 55, 5)
    assert third["target_witness"] == (-1, 0)
    assert Fraction(4, 73) == Fraction(1, 22) + Fraction(1, 110) + Fraction(1, 4015)

    # FIFO Cayley discovery returns a noncanonical equal-length witness here.
    assert typed_classification(383, 6990) == ("F", (-2, 0, 0, 3))


def verify_transient_boundary() -> None:
    states = p1201_macro_provenance()
    anchor = states["anchor"]
    transient = states["intermediate"]
    assert anchor == (1839, 552160, 986)
    assert transient == (2873071, 862639568, 986)
    p, A, _M, _d, _n = 1201, 986, 906134, 249, 751465
    C_A = pow(4 * A, -1, p)
    projected = ((4 * A * C_A - 1) // p, A * C_A, A)
    assert projected == anchor
    assert transient[1] // A == 874888 and projected[1] // A == 560


def verify() -> None:
    receipts = {fixture.label: fold(fixture) for fixture in FIXTURES}
    verify_explicit_certificates(receipts)
    verify_transient_boundary()
    print("verified typed total-cofactor projection dispatch")
    for label, receipt in receipts.items():
        print(label, receipt["source"], "->", receipt["target"], receipt["types"])
    print("p1201_transient_boundary", "projected target equals persistent parent")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
