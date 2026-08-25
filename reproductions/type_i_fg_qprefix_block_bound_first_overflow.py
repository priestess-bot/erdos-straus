#!/usr/bin/env python3
"""Verify actual-F q-prefix block binding and the first-overflow gap map."""

from __future__ import annotations

import argparse
import cmath
import math
from fractions import Fraction
from itertools import product


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


def valuation(value: int, prime: int) -> int:
    value = abs(value)
    if value == 0:
        raise ValueError("valuation(0) is not used by this verifier")
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def canonical_vertex(value: int) -> tuple[int, int, int]:
    """Return the unique (D, A, C) with value=A*D=A^2*C."""
    d_value = 1
    a_value = 1
    for prime, exponent in factorization(value).items():
        d_value *= prime ** ((exponent + 1) // 2)
        a_value *= prime ** (exponent // 2)
    c_value = d_value // a_value
    assert value == d_value * a_value
    return d_value, a_value, c_value


def euler_phi(value: int) -> int:
    result = value
    for prime in factorization(value):
        result = result // prime * (prime - 1)
    return result


def multiplicative_order(value: int, modulus: int) -> int:
    assert math.gcd(value, modulus) == 1
    order = euler_phi(modulus)
    for prime in factorization(order):
        while order % prime == 0 and pow(value, order // prime, modulus) == 1:
            order //= prime
    assert pow(value, order, modulus) == 1
    return order


def cyclic_logs(generator: int, order: int, modulus: int) -> dict[int, int]:
    logs: dict[int, int] = {}
    value = 1
    for exponent in range(order):
        assert value not in logs
        logs[value] = exponent
        value = value * generator % modulus
    assert value == 1 and len(logs) == order
    return logs


def mod_power(base: int, exponent: int, modulus: int) -> int:
    if exponent < 0:
        return pow(pow(base, -1, modulus), -exponent, modulus)
    return pow(base, exponent, modulus)


def first_overflow_gap(p: int, modulus: int) -> tuple[int, int, int]:
    """Return (m, y, n) from m=3 mod 4 and m=-2p mod modulus."""
    assert modulus % 2 == 1 and math.gcd(p, modulus) == 1
    candidates = tuple(
        value
        for value in range(1, 4 * modulus)
        if value % 4 == 3 and (value + 2 * p) % modulus == 0
    )
    assert len(candidates) == 1
    gap = candidates[0]
    label = (p + gap) // 4
    quotient = (2 * p + gap) // modulus
    assert 4 * label == p + gap
    assert (p + 4 * label) % modulus == 0
    assert p < 4 * label < p + 4 * modulus
    assert quotient % 2 == 1
    assert math.gcd(label, modulus) == 1
    return gap, label, quotient


def gap_menu(p: int, gap: int) -> tuple[tuple[str, int], ...]:
    """Return all Bradford I/II divisor witnesses at one gap."""
    assert gap % 4 == 3 and 3 <= gap <= p - 2
    first = (p + gap) // 4
    result: list[tuple[str, int]] = []
    for divisor in divisors(first * first):
        if (p * first + divisor) % gap == 0:
            result.append(("I", divisor))
        if divisor <= first and (first + divisor) % gap == 0:
            result.append(("II", divisor))
    return tuple(result)


def replacement_lift_numerator(p: int, n: int, coordinate: int) -> int:
    """Numerator for a lift that preserves the other two denominators."""
    assert 2 <= n < p and 4 * coordinate > n
    return n * p - 4 * (p - n) * coordinate


def replacement_lift_positivity_bound(p: int, n: int) -> tuple[int, int]:
    """Return the least source coordinate and the maximal lift numerator."""
    least_coordinate = n // 4 + 1
    bound = replacement_lift_numerator(p, n, least_coordinate)
    if n % 4 == 1:
        assert bound == n * n + 3 * n - 3 * p
    elif n % 4 == 3:
        assert bound == n * n + n - p
    return least_coordinate, bound


def verify_actual_f_request() -> dict[str, object]:
    p, modulus = 557_281, 199
    group_order = modulus - 1
    generator = 3
    k_value = (p * modulus + 1) // 4
    expected_factors = {2: 1, 5: 1, 11: 3, 2_083: 1}
    assert factorization(p) == {p: 1}
    assert factorization(modulus) == {modulus: 1}
    assert p % 24 == 1
    assert 4 * k_value == p * modulus + 1
    assert factorization(k_value) == expected_factors

    # The three maximal-prime-divisor order checks prove ord_199(3)=198.
    assert (
        pow(generator, 99, modulus),
        pow(generator, 66, modulus),
        pow(generator, 18, modulus),
    ) == (198, 106, 125)
    logs = cyclic_logs(generator, group_order, modulus)
    primes = tuple(expected_factors)
    budgets = tuple(expected_factors[prime] for prime in primes)
    prime_logs = tuple(logs[prime % modulus] for prime in primes)
    assert primes == (2, 5, 11, 2_083)
    assert budgets == (1, 1, 3, 1)
    assert prime_logs == (106, 138, 189, 165)
    assert math.gcd(group_order, *prime_logs) == 1

    points = tuple(product(*(range(-budget, budget + 1) for budget in budgets)))
    support_logs = tuple(
        sum(log_value * exponent for log_value, exponent in zip(prime_logs, point))
        % group_order
        for point in points
    )
    target_log = group_order // 2
    assert len(points) == 189
    assert len(set(support_logs)) == 129
    identity_count = support_logs.count(0)
    assert identity_count == 3
    assert target_log == 99 and target_log not in support_logs

    # Exact congruence proof of target absence. Modulo 9 first forces a=0,
    # then d=-b; division by 9 leaves 21c-3b=11 (mod 22), impossible mod 3.
    possible = []
    for a, b, c, d in points:
        if (106 * a + 138 * b + 189 * c + 165 * d - 99) % 198 == 0:
            possible.append((a, b, c, d))
        if (106 * a + 138 * b + 189 * c + 165 * d - 99) % 9 == 0:
            assert a == 0 and d == -b
            assert (21 * c - 3 * b - 11) % 22 != 0
    assert possible == []

    # The state-local selector digest explicitly names this target-odd role.
    # Integer angle bounds below certify the four Dirichlet-factor signs;
    # floating evaluation is only a focused numerical cross-check.
    character_index = 43
    assert character_index % 2 == 1
    assert character_index * target_log % group_order == target_log
    residues = tuple(
        ((character_index * value + group_order // 2) % group_order)
        - group_order // 2
        for value in prime_logs
    )
    assert residues == (4, -6, 9, -33)
    assert all(0 < 6 * abs(residue) < group_order for residue in residues[:2])
    assert 0 < 14 * residues[2] < group_order
    assert 6 * abs(residues[3]) == group_order
    factors = tuple(
        sum(
            cmath.exp(2j * math.pi * residue * exponent / group_order)
            for exponent in range(-budget, budget + 1)
        ).real
        for residue, budget in zip(residues, budgets)
    )
    assert all(value > 0 for value in factors)
    score = math.prod(factors)
    assert score > 104
    assert score > identity_count
    assert score > len(points) / (group_order - 1)

    q_primary_index = character_index * (group_order // 9) % group_order
    assert q_primary_index == 154
    assert group_order // math.gcd(group_order, q_primary_index) == 9
    zeta9_exponents = tuple(7 * (value % 9) % 9 for value in prime_logs)
    assert zeta9_exponents == (4, 3, 0, 3)
    assert zeta9_exponents[0] % 3 == 1

    return {
        "p": p,
        "R": modulus,
        "K": k_value,
        "box_points": len(points),
        "distinct_support": len(set(support_logs)),
        "identity_count": identity_count,
        "fourier_selector_digest": "EXPLICIT_TARGET_ODD_INDEX_43",
        "selected_character": character_index,
        "q3_primary_index": q_primary_index,
        "factor_2_edge_full_phase": zeta9_exponents[0],
        "factor_2_edge_elementary_phase": zeta9_exponents[0] % 3,
        "request_count": 1,
    }


def verify_candidate_fiber_block_bound() -> dict[str, object]:
    p, q, base_layer, depth = 557_281, 3, 1, 2
    target, deep, shallow = 182, 19_838, 138_866
    target_base, target_a, target_c = canonical_vertex(target)
    deep_base, deep_a, deep_c = canonical_vertex(deep)
    shallow_base, shallow_a, shallow_c = canonical_vertex(shallow)
    assert (target_base, target_a, target_c) == (182, 1, 182)
    assert (deep_base, deep_a, deep_c) == (19_838, 1, 19_838)
    assert (shallow_base, shallow_a, shallow_c) == (19_838, 7, 2_834)
    assert target_base * 109 == deep_base == shallow_base
    assert target_base % target_a == 0
    assert deep_base % deep_a == shallow_base % shallow_a == 0
    assert all(
        all(exponent == 1 for exponent in factorization(value).values())
        for value in (target_c, deep_c, shallow_c)
    )
    assert 4 * max(target, deep, shallow) < p

    target_height = valuation(p + 4 * target, q)
    deep_height = valuation(p + 4 * deep, q)
    shallow_height = valuation(p + 4 * shallow, q)
    assert (target_height, deep_height, shallow_height) == (4, 3, 1)
    assert valuation(deep - target, q) == base_layer + depth
    assert valuation(shallow - deep, q) == base_layer
    assert (shallow - deep) // q**base_layer % q == 1

    # The actual F edge is 0 -> e_2. Its full order-9 phase is 4 and its
    # elementary phase is 1. This affine source-line map realizes both.
    source_difference = shallow - deep
    def affine(point):
        return deep + source_difference * point[0]
    zero = (0, 0, 0, 0)
    factor_2_edge = (1, 0, 0, 0)
    assert affine(zero) == deep and affine(factor_2_edge) == shallow
    assert math.gcd(*factor_2_edge) == 1

    beta = (-p * pow(4, -1, q**base_layer)) % q**base_layer
    tail_modulus = q**depth
    def tail(value):
        return (value - beta) // q ** base_layer % tail_modulus
    assert beta == 2
    assert (tail(target), tail(deep), tail(shallow)) == (6, 6, 1)
    assert (tail(shallow) - tail(deep)) % tail_modulus == 4
    assert (tail(target) - 0) % tail_modulus == 6

    target_modulus = 4 * target_base
    target_numerator = p + 4 * target
    block = tuple(q**power for power in range(depth + 1))
    assert target_modulus == 728
    assert factorization(target_numerator) == {3: 4, 83: 2}
    assert all(target_numerator % value == 0 for value in block)
    assert multiplicative_order(q, target_modulus) == 6

    def eta(value):
        return pow(value % 13, 4, 13)
    assert tuple(eta(value) for value in block) == (1, 3, 9)
    assert set(eta(value) for value in block) == {1, 3, 9}
    assert eta(-1) == 1

    source_keys = tuple(("S", deep, q, base_layer + level) for level in range(1, depth + 1))
    target_keys = tuple(("T", target, q, base_layer + level) for level in range(1, depth + 1))
    assert len(set(source_keys + target_keys)) == 4
    assert len(block) == q

    # This is the strict gate-order counterexample: the typed, individually
    # bound block exists, but no divisor of the complete target numerator is
    # the target residue. Terminal FIBER_REALIZED is therefore false.
    target_divisors = divisors(target_numerator)
    terminal_products = tuple(
        value for value in target_divisors if value % target_modulus == target_modulus - 1
    )
    assert terminal_products == ()
    assert all(value % target_modulus != target_modulus - 1 for value in block)

    units = tuple(
        value for value in range(1, target_modulus) if math.gcd(value, target_modulus) == 1
    )
    kernel = {value for value in units if eta(value) == 1}
    section = {
        value
        for value in kernel
        if ((-1) * value) % target_modulus in {entry % target_modulus for entry in block}
    }
    assert len(kernel) == 96
    assert section == {target_modulus - 1}
    assert len(section) * (len(kernel) - len(section)) == 95

    return {
        "target": target,
        "source_rows": (deep, shallow),
        "heights": (target_height, deep_height, shallow_height),
        "tail_coordinates_mod_9": (tail(target), tail(deep), tail(shallow)),
        "candidate_block": block,
        "eta_image": tuple(eta(value) for value in block),
        "candidate_fiber_qblock_bound": True,
        "typed_full_c3_prefix": True,
        "terminal_fiber_realized": False,
        "kernel_section": tuple(sorted(section)),
        "kernel_fourier_energy": 95,
    }


def verify_p73_strict_no_go() -> dict[str, object]:
    p, q, depth = 73, 3, 2
    assert factorization(p) == {p: 1}
    bound = (p - 1) // 4
    # Repository CRT normalization on the reverse (0,1)->(0,0) edge.
    z0, z1 = (0, 1), (0, 0)
    delta = tuple(right - left for left, right in zip(z0, z1))
    role_value = 2 * (15 * delta[0] + delta[1]) % q
    def affine(point):
        return 5 - 3 * point[1]
    assert delta == (0, -1) and role_value == 1
    assert affine(z0) == 2 and affine(z1) == 5
    assert (affine(z1) - affine(z0)) // q == role_value
    assert (
        valuation(p + 4 * 2, q),
        valuation(p + 4 * 2, q),
        valuation(p + 4 * 5, q),
    ) == (4, 4, 1)

    candidates = []
    for layer in range(1, 5):
        power = q**layer
        for target in range(1, bound + 1):
            if valuation(p + 4 * target, q) < layer + depth:
                continue
            for deep in range(1, bound + 1):
                if valuation(p + 4 * deep, q) < layer + depth:
                    continue
                for shallow in range(1, bound + 1):
                    if valuation(p + 4 * shallow, q) != layer:
                        continue
                    difference = shallow - deep
                    if difference % power == 0 and difference // power % q == role_value:
                        candidates.append((layer, target, deep, shallow))
    assert candidates == [(1, 2, 2, 5), (1, 2, 2, 14), (2, 2, 2, 11)]
    base_profiles = tuple(
        (item, canonical_vertex(item[2])[0], canonical_vertex(item[3])[0])
        for item in candidates
    )
    assert base_profiles == (
        ((1, 2, 2, 5), 2, 5),
        ((1, 2, 2, 14), 2, 14),
        ((2, 2, 2, 11), 2, 11),
    )
    assert all(left != right for _, left, right in base_profiles)

    maximum_fixed_base_slots = {}
    for layer in (1, 2):
        groups: dict[int, list[int]] = {}
        for label in range(1, bound + 1):
            if (p + 4 * label) % q**layer:
                continue
            groups.setdefault(canonical_vertex(label)[0], []).append(label)
        maximum_fixed_base_slots[layer] = max(map(len, groups.values()))
    assert maximum_fixed_base_slots == {1: 1, 2: 1}

    target_base = canonical_vertex(2)[0]
    assert target_base == 2
    assert multiplicative_order(q, 4 * target_base) == 2
    assert {pow(q, exponent, 8) for exponent in range(5)} == {1, 3}

    return {
        "p": p,
        "actual_edge_role": role_value,
        "depth_2_candidates": tuple(candidates),
        "maximum_fixed_base_slots": maximum_fixed_base_slots,
        "common_canonical_profile_count": 0,
        "target_q_direction_order": 2,
        "status": (
            "CANONICAL_COMMON_SOURCE_BASE_PROFILE_EMPTY",
            "TARGET_PHYSICAL_Q_DIRECTION_PRIMARY_RANK_ZERO",
        ),
    }


def verify_first_overflow_dispatch() -> dict[str, object]:
    modulus = 27
    negative = first_overflow_gap(73, modulus)
    assert negative == (43, 29, 7)
    assert gap_menu(73, 43) == ()
    least_coordinate, positivity_bound = replacement_lift_positivity_bound(73, 7)
    assert (least_coordinate, positivity_bound) == (2, -17)
    assert Fraction(4, 7) == Fraction(1, 2) + Fraction(1, 28) + Fraction(1, 28)
    assert all(
        replacement_lift_numerator(73, 7, coordinate) < 0
        for coordinate in (2, 28, 28)
    )

    positive = first_overflow_gap(557_281, modulus)
    assert positive == (79, 139_340, 41_283)
    menu = gap_menu(557_281, 79)
    assert ("II", 16) in menu
    gap, first, _ = positive
    divisor = 16
    second = 557_281 * (first + divisor) // gap
    third = 557_281 * (first + first * first // divisor) // gap
    assert (second, third) == (983_043_684, 8_561_081_683_035)
    assert Fraction(4, 557_281) == (
        Fraction(1, first) + Fraction(1, second) + Fraction(1, third)
    )

    return {
        "p73": {
            "gap_label_quotient": negative,
            "gap_menu": "empty",
            "two_denominator_preserving_replacement_bound": positivity_bound,
            "status": "FIRST_OVERFLOW_SHORT_GAP_MENU_EMPTY",
        },
        "p557281": {
            "gap_label_quotient": positive,
            "type_ii_divisor": divisor,
            "solution": (first, second, third),
            "status": "FIRST_OVERFLOW_TYPE_II_TERMINAL",
        },
    }


def verify() -> None:
    actual_f = verify_actual_f_request()
    block_bound = verify_candidate_fiber_block_bound()
    p73_no_go = verify_p73_strict_no_go()
    overflow = verify_first_overflow_dispatch()
    print("verified actual-F q-prefix block binding and first-overflow gap map")
    print(
        {
            "actual_f": actual_f,
            "block_bound": block_bound,
            "p73_no_go": p73_no_go,
            "first_overflow": overflow,
        }
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
