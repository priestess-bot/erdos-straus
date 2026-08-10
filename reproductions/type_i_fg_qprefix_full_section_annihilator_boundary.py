#!/usr/bin/env python3
"""Focused verifier for the full q-prefix divisor-kernel section boundary."""

from __future__ import annotations

import argparse
from math import gcd


def divisors(n: int) -> list[int]:
    out = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
        d += 1
    return sorted(out)


def is_squarefree(n: int) -> bool:
    prime = 2
    while prime * prime <= n:
        if n % (prime * prime) == 0:
            return False
        if n % prime == 0:
            n //= prime
        prime += 1
    return True


def multiplicative_order(a: int, modulus: int) -> int:
    value = 1
    for exponent in range(1, 10_000):
        value = value * a % modulus
        if value == 1:
            return exponent
    raise AssertionError("order bound exceeded")


def generated_subgroup(generators: tuple[int, ...], modulus: int) -> set[int]:
    subgroup = {1}
    frontier = [1]
    while frontier:
        value = frontier.pop()
        for generator in generators:
            candidate = value * generator % modulus
            if candidate not in subgroup:
                subgroup.add(candidate)
                frontier.append(candidate)
    return subgroup


def chi_minus_eight(unit: int) -> int:
    residue = unit % 8
    assert residue in (1, 3, 5, 7)
    return 1 if residue in (1, 3) else -1


def verify() -> None:
    p = 557_281
    d_star = 182
    modulus = 4 * d_star
    target = modulus - 1
    numerator = p + 4 * d_star

    assert modulus == 728
    assert numerator == 558_009 == 3**4 * 83**2

    units = {u for u in range(modulus) if gcd(u, modulus) == 1}
    kernel = {u for u in units if pow(u % 13, 4, 13) == 1}
    assert len(units) == 288
    assert len(kernel) == 96

    prefix = {1, 3, 9}
    full_fiber = {
        pow(3, exponent_three, modulus) * pow(83, exponent_83, modulus) % modulus
        for exponent_three in range(5)
        for exponent_83 in range(3)
    }
    assert len(full_fiber) == 15

    def section(source: set[int]) -> set[int]:
        return {target * value % modulus for value in source if value in kernel}

    prefix_kernel = prefix & kernel
    full_kernel = full_fiber & kernel
    prefix_section = section(prefix)
    full_section = section(full_fiber)

    assert prefix_kernel == {1}
    assert prefix_section == {727}
    assert full_kernel == {1, 27, 57, 83, 337, 363}
    assert full_section == {365, 391, 645, 671, 701, 727}
    assert min(full_kernel - prefix) == 27
    assert len(prefix_section) * (len(kernel) - len(prefix_section)) == 95
    assert len(full_section) * (len(kernel) - len(full_section)) == 540

    # The same prefix datum admits two incompatible ambient set completions.
    assert prefix & kernel == {1}
    assert (prefix | {27}) & kernel == {1, 27}

    kernel_divisor_group = generated_subgroup((27, 83), modulus)
    assert kernel_divisor_group == {1, 27, 57, 83, 281, 307, 337, 363}
    assert multiplicative_order(27, modulus) == 2
    assert multiplicative_order(83, modulus) == 4
    assert target not in kernel_divisor_group

    assert all(chi_minus_eight(value) == 1 for value in full_fiber)
    assert chi_minus_eight(target) == -1
    assert sum(chi_minus_eight(value) for value in full_section) == -6

    candidate_products = set()
    for d_prime in divisors(d_star):
        if d_prime >= d_star:
            continue
        for a in divisors(d_prime):
            if not is_squarefree(d_prime // a):
                continue
            product = a * d_prime
            if 4 * product < p:
                candidate_products.add(product)

    expected_products = {
        1,
        2,
        4,
        7,
        13,
        14,
        26,
        28,
        49,
        52,
        91,
        98,
        169,
        196,
        338,
        637,
        676,
        1183,
        8281,
    }
    assert candidate_products == expected_products
    assert d_star % 83 == 16
    assert all(product % 83 != 16 for product in candidate_products)

    print("PASS: FULL_QPREFIX_DIVISOR_KERNEL_SECTION_BOUNDARY")
    print(f"unit_group={len(units)} kernel={len(kernel)}")
    print(f"prefix_section={sorted(prefix_section)} energy=95")
    print(f"full_section={sorted(full_section)} energy=540")
    print(f"kernel_divisor_group={sorted(kernel_divisor_group)}")
    print("same_fiber_factor_character=CHI_MINUS_8 coefficient=-6")
    print("h83_low_modulus_source_crt_candidates=19 hits=0")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
