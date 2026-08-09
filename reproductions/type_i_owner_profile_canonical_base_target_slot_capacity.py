#!/usr/bin/env python3
"""Focused checks for canonical-base/profile/target slot admission."""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import product
from math import gcd


def factorization(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    prime = 2
    while prime * prime <= value:
        while value % prime == 0:
            factors[prime] = factors.get(prime, 0) + 1
            value //= prime
        prime += 1
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def divisors(value: int) -> tuple[int, ...]:
    result = [1]
    for prime, exponent in factorization(value).items():
        result = [
            old * prime**power
            for old in result
            for power in range(exponent + 1)
        ]
    return tuple(sorted(result))


def radical(value: int) -> int:
    result = 1
    for prime in factorization(value):
        result *= prime
    return result


def canonical_vertex(value: int) -> tuple[int, int, int]:
    """Return the unique (D, A, C) with value=A*D=A^2*C."""
    d_value = 1
    a_value = 1
    for prime, exponent in factorization(value).items():
        d_value *= prime ** ((exponent + 1) // 2)
        a_value *= prime ** (exponent // 2)
    c_value = d_value // a_value
    assert value == d_value * a_value
    assert all(exponent == 1 for exponent in factorization(c_value).values())
    return d_value, a_value, c_value


def owner_prefix(p: int, modulus: int) -> int:
    value = (-p * pow(4, -1, modulus)) % modulus
    assert 0 < value < modulus
    return value


def owner_parameters(p: int, q: int, layer: int) -> tuple[int, int, int]:
    modulus = q**layer
    prefix = owner_prefix(p, modulus)
    bound = (p - 1) // 4
    maximum_index = (bound - prefix) // modulus
    return prefix, bound, maximum_index


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def euler_phi(value: int) -> int:
    result = value
    for prime in factorization(value):
        result = result // prime * (prime - 1)
    return result


def multiplicative_order(value: int, modulus: int) -> int:
    assert gcd(value, modulus) == 1
    order = euler_phi(modulus)
    for prime in factorization(order):
        while order % prime == 0 and pow(value, order // prime, modulus) == 1:
            order //= prime
    assert pow(value, order, modulus) == 1
    return order


def canonical_slots(
    p: int, q: int, layer: int, d_value: int
) -> tuple[tuple[int, int, int, int, int], ...]:
    """Return sorted (index, source, A, c, phase) fixed-D slots."""
    modulus = q**layer
    prefix, bound, _ = owner_parameters(p, q, layer)
    slots = []
    for c_value in divisors(radical(d_value)):
        source = d_value * d_value // c_value
        if source > bound or (source - prefix) % modulus:
            continue
        index = (source - prefix) // modulus
        a_value = d_value // c_value
        assert source == d_value * a_value
        assert d_value % a_value == 0
        assert radical(c_value) == c_value
        assert canonical_vertex(source) == (d_value, a_value, c_value)
        slots.append((index, source, a_value, c_value, index % q))
    return tuple(sorted(slots))


def rank_one_profiles(
    p: int,
    q: int,
    layer: int,
    separation: int,
    role_value: int,
) -> tuple[tuple[tuple[int, int], int, int], ...]:
    """Directly enumerate the two-point owner box for Y=role+qZ."""
    _, _, maximum_index = owner_parameters(p, q, layer)
    profiles = []
    for left, right in product(range(maximum_index + 1), repeat=2):
        difference = right - left
        if difference % separation:
            continue
        normalized_dual = difference // separation
        if normalized_dual % q != role_value % q:
            continue
        profiles.append(((left, right), normalized_dual, left))
    return tuple(profiles)


def common_canonical_profiles(
    p: int,
    q: int,
    layer: int,
    profiles: tuple[tuple[tuple[int, int], int, int], ...],
) -> tuple[tuple[int, tuple[int, int], tuple[int, int]], ...]:
    modulus = q**layer
    prefix = owner_prefix(p, modulus)
    result = []
    for indices, _, _ in profiles:
        labels = tuple(prefix + modulus * index for index in indices)
        bases = tuple(canonical_vertex(label)[0] for label in labels)
        if bases[0] == bases[1]:
            result.append((bases[0], indices, labels))
    return tuple(result)


def transverse_capacity(phase_counts: tuple[int, ...]) -> int:
    total = sum(phase_counts)
    return min(total // 2, total - max(phase_counts, default=0))


def eligible_deep_targets(
    p: int, q: int, layer: int, d_value: int
) -> tuple[tuple[int, int, int], ...]:
    deeper_modulus = q ** (layer + 1)
    deeper_prefix = owner_prefix(p, deeper_modulus)
    bound = (p - 1) // 4
    result = []
    for target in divisors(d_value * d_value):
        if target > bound or target % deeper_modulus != deeper_prefix:
            continue
        target_base = canonical_vertex(target)[0]
        if gcd(q, target_base) != 1:
            continue
        order = multiplicative_order(q, 4 * target_base)
        if order % q == 0:
            result.append((target, target_base, order))
    return tuple(result)


def verify_inverse_dictionary() -> dict[str, object]:
    checked = 0
    for d_value in range(1, 81):
        expected = {
            d_value * d_value // c_value
            for c_value in divisors(radical(d_value))
        }
        actual = set()
        for source in expected:
            source_base, a_value, c_value = canonical_vertex(source)
            assert source_base == d_value
            assert source == d_value * a_value
            assert d_value % a_value == 0
            assert c_value == d_value // a_value
            actual.add(source)
            checked += 1
        assert actual == expected
    return {"fixed_bases": 80, "canonical_rows_checked": checked}


def verify_gcd_false_positive_profile() -> dict[str, object]:
    p, q, layer = 97, 3, 1
    profiles = rank_one_profiles(p, q, layer, separation=4, role_value=1)
    assert tuple(indices for indices, _, _ in profiles) == (
        (0, 4),
        (1, 5),
        (2, 6),
        (3, 7),
    )
    assert common_canonical_profiles(p, q, layer, profiles) == ()

    prefix = owner_prefix(p, q**layer)
    labels = tuple(prefix + q**layer * index for index in (2, 6))
    bases = tuple(canonical_vertex(label)[0] for label in labels)
    assert labels == (8, 20)
    assert gcd(*labels) == gcd(labels[0], 6 - 2) == 4
    assert bases == (4, 10)
    assert (20 // 4) == 5 and 4 % 5
    return {
        "profiles": len(profiles),
        "common_canonical_profiles": 0,
        "gcd_false_positive": (labels, 4, bases),
    }


def verify_joint_profile_target() -> dict[str, object]:
    p, q, layer = 2113, 3, 1
    profiles = rank_one_profiles(p, q, layer, separation=70, role_value=1)
    assert len(profiles) == 142
    common = common_canonical_profiles(p, q, layer, profiles)
    assert common == (
        (35, (11, 81), (35, 245)),
        (70, (46, 116), (140, 350)),
    )

    target = 14
    target_base = canonical_vertex(target)[0]
    admitted = tuple(item for item in common if item[0] % target_base == 0)
    assert target_base == 14
    assert admitted == ((70, (46, 116), (140, 350)),)
    assert valuation(p + 4 * target, q) == 2
    assert multiplicative_order(q, 4 * target_base) == 6

    blocked_target = 65
    blocked_base = canonical_vertex(blocked_target)[0]
    assert blocked_base == 65
    prefix, bound, _ = owner_parameters(p, q, layer)
    assert blocked_target <= bound
    assert blocked_target % (q**layer) == prefix
    assert not tuple(item for item in common if item[0] % blocked_base == 0)
    return {
        "range_profiles": len(profiles),
        "common_bases": tuple(item[0] for item in common),
        "target_14_joint_witness": admitted[0],
        "target_65_joint_witnesses": 0,
    }


def verify_phase_and_target_capacity() -> dict[str, object]:
    p, q, layer, d_value = 2113, 3, 1, 70
    prefix = owner_prefix(p, q**layer)
    deeper_prefix = owner_prefix(p, q ** (layer + 1))
    delta = (deeper_prefix - prefix) // (q**layer)
    assert (prefix, deeper_prefix, delta) == (2, 5, 1)

    slots = canonical_slots(p, q, layer, d_value)
    assert slots == (
        (46, 140, 2, 35, 1),
        (116, 350, 5, 14, 2),
    )
    phase_counter = Counter(slot[4] for slot in slots)
    phase_counts = tuple(phase_counter[phase] for phase in range(q))
    assert phase_counts == (0, 1, 1)
    assert transverse_capacity(phase_counts) == 1
    deep = phase_counts[delta]
    shallow = len(slots) - deep
    assert (deep, shallow, min(deep, shallow)) == (1, 1, 1)

    targets = eligible_deep_targets(p, q, layer, d_value)
    assert targets == ((14, 14, 6), (140, 70, 12))
    candidate_triples = deep * shallow * len(targets)
    arithmetic_capacity = min(deep, shallow, len(targets))
    assert (candidate_triples, arithmetic_capacity) == (2, 1)
    return {
        "slots": slots,
        "phase_counts": phase_counts,
        "transverse_capacity": 1,
        "exclusive_capacity": 1,
        "eligible_deep_targets": targets,
        "candidate_triples": candidate_triples,
        "arithmetic_capacity": arithmetic_capacity,
    }


def verify() -> None:
    inverse = verify_inverse_dictionary()
    false_positive = verify_gcd_false_positive_profile()
    joint = verify_joint_profile_target()
    capacity = verify_phase_and_target_capacity()
    print("verified: canonical fixed-base inverse dictionary", inverse)
    print("verified: gcd-base profile false positive", false_positive)
    print("verified: joint profile/common-base/target admission", joint)
    print("verified: phase and deep-target slot capacity", capacity)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
