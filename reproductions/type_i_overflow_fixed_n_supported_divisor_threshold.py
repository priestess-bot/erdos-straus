#!/usr/bin/env python3
"""Verify focused support-preserving fixed-n fold threshold receipts.

The checks exercise the exact least-prime-factor selector and two known
rough-residual arithmetic controls. They are not a range scan or a proof of
reachability for the residual controls.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from itertools import product
from math import isqrt


@dataclass(frozen=True)
class Fixture:
    name: str
    prime: int
    carrier: int
    d: int
    denominator: int
    support: int
    expected_factor: int | None
    expected_target: tuple[int, int, int] | None
    expected_height_lower_bound: int | None
    expected_total_capacity: tuple[int, int] | None


@dataclass(frozen=True)
class SaturatedFixture:
    name: str
    prime: int
    support: int
    expected_class: str


FIXTURES = (
    Fixture(
        "least_prime_support_promotion",
        73,
        1332,
        1,
        73,
        6,
        2,
        (12, 38, 25),
        None,
        None,
    ),
    Fixture(
        "low_support_d_gt_one_forces_fold",
        73,
        82,
        2,
        9,
        1,
        2,
        (2, 9, 1),
        None,
        None,
    ),
    Fixture(
        "p73_h_rough_double_atlas_hole",
        73,
        2051,
        13,
        1461,
        293,
        None,
        None,
        357,
        (420, 55),
    ),
    Fixture(
        "p673_h_rough_double_atlas_hole",
        673,
        215923,
        647,
        830325,
        821,
        None,
        None,
        92601,
        (6838, 108),
    ),
)


SATURATED_FIXTURES = (
    SaturatedFixture("p73_saturated_rough_g", 73, 97, "G"),
    SaturatedFixture("p73_saturated_rough_f", 73, 56, "F"),
    SaturatedFixture("p97_saturated_rough_g", 97, 79, "G"),
    SaturatedFixture("p97_saturated_rough_f", 97, 70, "F"),
)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def smallest_prime_factor(value: int) -> int | None:
    if value < 2:
        return None
    if value % 2 == 0:
        return 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return divisor
    return value


def height_lower_bound(prime: int, support_window: int) -> int:
    j = min(support_window + 1, prime - 2)
    return j * (prime - 2) + 1 + j % 4


def inverse_mod(value: int, modulus: int) -> int:
    return pow(value, -1, modulus)


def prime_factorization(value: int) -> tuple[tuple[int, int], ...]:
    factors: list[tuple[int, int]] = []
    remaining = value
    if remaining % 2 == 0:
        exponent = 0
        while remaining % 2 == 0:
            remaining //= 2
            exponent += 1
        factors.append((2, exponent))
    divisor = 3
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            exponent = 0
            while remaining % divisor == 0:
                remaining //= divisor
                exponent += 1
            factors.append((divisor, exponent))
        divisor += 2
    if remaining > 1:
        factors.append((remaining, 1))
    return tuple(factors)


def target_class(
    modulus: int, factorization: tuple[tuple[int, int], ...]
) -> str:
    generated = {1}
    frontier = [1]
    while frontier:
        residue = frontier.pop()
        for prime, _ in factorization:
            successor = residue * prime % modulus
            if successor not in generated:
                generated.add(successor)
                frontier.append(successor)
    if modulus - 1 not in generated:
        return "G"
    for exponents in product(
        *(range(-exponent, exponent + 1) for _, exponent in factorization)
    ):
        residue = 1
        for (prime, _), exponent in zip(factorization, exponents):
            base = prime if exponent >= 0 else inverse_mod(prime, modulus)
            residue = residue * pow(base, abs(exponent), modulus) % modulus
        if residue == modulus - 1:
            return "hit"
    return "F"


def audit(fixture: Fixture) -> dict[str, int | str | None]:
    p = fixture.prime
    M = fixture.carrier
    d = fixture.d
    n = fixture.denominator
    A = fixture.support
    B = (p - 1) ** 2 // 4
    H = B // A
    b, remainder = divmod(M, A)
    if not (
        is_prime(p)
        and p % 24 == 1
        and remainder == 0
        and 1 <= d < p
        and 1 <= A <= B
        and p * n == 4 * M * d + 1
        and 4 * M - n > p
    ):
        raise AssertionError(f"{fixture.name}: source overflow contract changed")

    product = b * d
    factor = smallest_prime_factor(product)
    candidates = [
        t
        for t in range(2, H + 1)
        if product % t == 0
    ]
    if bool(candidates) != (factor is not None and factor <= H):
        raise AssertionError(f"{fixture.name}: threshold equivalence changed")

    if fixture.expected_factor is not None:
        if factor != fixture.expected_factor or candidates[0] != factor:
            raise AssertionError(f"{fixture.name}: canonical least-prime choice changed")
        L = A * factor
        quotient = M * d // L
        h, delta = divmod(quotient, p)
        n_target = n - 4 * L * h
        R_target = 4 * L - n_target
        K_target = L * (p - delta)
        if not (
            1 <= delta < p
            and n_target > 0
            and p * n_target == 4 * L * delta + 1
            and 0 < R_target < 4 * L
            and R_target % 4 == 3
            and 4 * K_target == p * R_target + 1
            and K_target % L == 0
            and B // L < B // A
        ):
            raise AssertionError(f"{fixture.name}: quotient-fold target changed")
        target = (L, delta, n_target)
        if target != fixture.expected_target:
            raise AssertionError(f"{fixture.name}: expected target changed")
        return {
            "name": fixture.name,
            "kind": "support_preserving_fold",
            "least_factor": factor,
            "target_denominator": n_target,
        }

    if candidates or factor is None or not (d > 1 and factor > H):
        raise AssertionError(f"{fixture.name}: rough residual gate changed")
    c = (p - 1) // 4
    if not (A > c and d >= H + 1 and M > B):
        raise AssertionError(f"{fixture.name}: high-support residual consequences changed")
    lower_bound = height_lower_bound(p, H)
    if n < lower_bound or lower_bound != fixture.expected_height_lower_bound:
        raise AssertionError(f"{fixture.name}: height lower bound changed")

    total_capacity = b * (p - d)
    canonical_capacity = inverse_mod(4 * A, p)
    if total_capacity % p != canonical_capacity:
        raise AssertionError(f"{fixture.name}: total-fold congruence changed")
    if (total_capacity, canonical_capacity) != fixture.expected_total_capacity:
        raise AssertionError(f"{fixture.name}: total-fold receipt changed")
    if total_capacity <= p:
        raise AssertionError(f"{fixture.name}: strict total-fold control changed")
    return {
        "name": fixture.name,
        "kind": "h_rough_residual",
        "least_factor": factor,
        "height_lower_bound": lower_bound,
        "total_capacity": total_capacity,
    }


def audit_saturated(fixture: SaturatedFixture) -> dict[str, int | str]:
    p = fixture.prime
    A = fixture.support
    B = (p - 1) ** 2 // 4
    H = B // A
    C = inverse_mod(4 * A, p)
    d = p - C
    n = (4 * A * d + 1) // p
    R = 4 * A - n
    K = A * C
    factorization = prime_factorization(K)
    actual_class = target_class(R, factorization)
    factor = smallest_prime_factor(d)
    if not (
        p * n == 4 * A * d + 1
        and R > p
        and K == A * (p - d)
        and K % A == 0
        and d > 1
        and factor is not None
        and factor > H
        and A * d > B
        and A * (H + 1) > B
        and actual_class == fixture.expected_class
    ):
        raise AssertionError(f"{fixture.name}: saturated rough boundary changed")
    return {
        "name": fixture.name,
        "kind": "saturated_rough_normal_form",
        "class": actual_class,
        "least_factor": factor,
        "carrier": A * d,
    }


def verify() -> None:
    receipts = [audit(fixture) for fixture in FIXTURES]
    saturated = [audit_saturated(fixture) for fixture in SATURATED_FIXTURES]
    fold_count = sum(receipt["kind"] == "support_preserving_fold" for receipt in receipts)
    rough_count = sum(receipt["kind"] == "h_rough_residual" for receipt in receipts)
    if (fold_count, rough_count) != (2, 2):
        raise AssertionError("fixture classification changed")
    if sorted(receipt["class"] for receipt in saturated) != ["F", "F", "G", "G"]:
        raise AssertionError("saturated typed boundary changed")
    print(
        "verified 2 least-prime support-preserving folds and "
        "2 H-rough residual receipts plus 4 saturated F/G boundaries"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused exact checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
