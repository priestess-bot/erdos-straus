#!/usr/bin/env python3
"""Verify the core Jacobi punctured-kernel primary selector."""

from __future__ import annotations

import argparse
import cmath
from collections import Counter
from fractions import Fraction
from itertools import product
from math import cos, gcd, isqrt, pi, prod


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


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


def jacobi(value: int, odd_modulus: int) -> int:
    assert odd_modulus > 0 and odd_modulus % 2 == 1
    assert gcd(value, odd_modulus) == 1
    value %= odd_modulus
    result = 1
    while value:
        while value % 2 == 0:
            value //= 2
            if odd_modulus % 8 in (3, 5):
                result = -result
        value, odd_modulus = odd_modulus, value
        if value % 4 == odd_modulus % 4 == 3:
            result = -result
        value %= odd_modulus
    assert odd_modulus == 1
    return result


def generated_subgroup(generators: tuple[int, ...], modulus: int) -> set[int]:
    subgroup = {1 % modulus}
    frontier = [1 % modulus]
    while frontier:
        value = frontier.pop()
        for generator in generators:
            successor = value * generator % modulus
            if successor not in subgroup:
                subgroup.add(successor)
                frontier.append(successor)
    return subgroup


def multiplicative_order(value: int, modulus: int) -> int:
    current = 1
    for exponent in range(1, modulus * modulus + 1):
        current = current * value % modulus
        if current == 1:
            return exponent
    raise AssertionError("order search did not terminate")


def vector_image(
    modulus: int,
    factors: tuple[tuple[int, int], ...],
    vector: tuple[int, ...],
) -> int:
    return prod(
        pow(prime, exponent, modulus)
        for (prime, _), exponent in zip(factors, vector, strict=True)
    ) % modulus


def rational_value(
    factors: tuple[tuple[int, int], ...], vector: tuple[int, ...]
) -> Fraction:
    value = Fraction(1)
    for (prime, _), exponent in zip(factors, vector, strict=True):
        if exponent >= 0:
            value *= prime**exponent
        else:
            value /= prime ** (-exponent)
    return value


def sign_intervals(exponent: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    return tuple(range(exponent + 1)), tuple(range(-exponent, 0))


def analyze_core(prime: int, modulus: int, K: int) -> dict[str, object]:
    assert is_prime(prime) and prime % 24 == 1
    assert 4 * K == prime * modulus + 1 and modulus % 4 == 3
    factors = factorint(K)
    generators = tuple(q % modulus for q, _ in factors)
    H = generated_subgroup(generators, modulus)
    assert modulus - 1 in H and jacobi(modulus - 1, modulus) == -1
    L = {value for value in H if jacobi(value, modulus) == 1}
    assert len(H) == 2 * len(L)
    d = len(L)
    active = {
        index for index, (q, _) in enumerate(factors) if jacobi(q, modulus) == -1
    }
    assert active

    boxes: list[dict[str, object]] = []
    target_hits: list[tuple[int, ...]] = []
    collisions: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
    negative_records: list[tuple[tuple[int, ...], int, int]] = []
    multiplicities: Counter[int] = Counter()

    for signs in product((0, 1), repeat=len(factors)):
        intervals = tuple(
            sign_intervals(nu)[sign]
            for sign, (_, nu) in zip(signs, factors, strict=True)
        )
        images: dict[int, tuple[int, ...]] = {}
        character_sum = 0
        filtered = 0
        size = 0
        for vector in product(*intervals):
            size += 1
            image = vector_image(modulus, factors, vector)
            character = jacobi(image, modulus)
            character_sum += character
            if image in images:
                collisions.append((images[image], vector))
            else:
                images[image] = vector
            if image == modulus - 1:
                target_hits.append(vector)
            if character == -1:
                filtered += 1
                normalized = (-image) % modulus
                assert normalized in L
                negative_records.append((vector, image, normalized))
                multiplicities[normalized] += 1
        special = character_sum > 0
        boxes.append(
            {
                "signs": signs,
                "size": size,
                "D": character_sum,
                "filtered": filtered,
                "special": special,
            }
        )

    C = len(negative_records)
    V = prod(2 * nu + 1 for _, nu in factors)
    A0 = prod(
        2 * factors[index][1] + 1
        for index in range(len(factors))
        if index not in active
    )
    assert C == (V - A0) // 2 and C % 2 == 0
    assert multiplicities[1] == len(target_hits)
    for value, count in multiplicities.items():
        assert count == multiplicities[pow(value, -1, modulus)]

    theta_ordered = sum(min(int(box["size"]), d) for box in boxes)
    theta_punctured = sum(min(int(box["size"]), d - 1) for box in boxes)
    large_boxes = {index for index, box in enumerate(boxes) if box["size"] >= d}
    special_boxes = {index for index, box in enumerate(boxes) if box["special"]}
    hybrid = theta_ordered - len(large_boxes | special_boxes)
    parity_hybrid = 2 * (hybrid // 2)

    if not target_hits and not collisions:
        assert all(box["filtered"] <= min(box["size"], d - 1) for box in boxes)
        assert C <= theta_punctured <= (d - 1) * 2 ** len(factors)
        assert C <= parity_hybrid
        assert all(box["size"] - box["D"] <= len(H) - 2 for box in boxes)

    return {
        "factors": factors,
        "H": H,
        "L": L,
        "d": d,
        "C": C,
        "V": V,
        "A0": A0,
        "boxes": boxes,
        "target_hits": target_hits,
        "collisions": collisions,
        "negative_records": negative_records,
        "multiplicities": multiplicities,
        "theta_punctured": theta_punctured,
        "hybrid": hybrid,
        "parity_hybrid": parity_hybrid,
    }


def oriented_relation_terminal(
    prime: int,
    modulus: int,
    K: int,
    factors: tuple[tuple[int, int], ...],
    pair: tuple[tuple[int, ...], tuple[int, ...]],
) -> tuple[int, int]:
    relation = tuple(left - right for left, right in zip(*pair, strict=True))
    if rational_value(factors, relation) > 1:
        relation = tuple(-entry for entry in relation)
    U = prod(
        q ** (nu + exponent)
        for (q, nu), exponent in zip(factors, relation, strict=True)
    )
    assert 0 < U < K and U % modulus == K % modulus
    E = 4 * U
    n = (4 * K - E) // modulus
    assert E % modulus == 1 and n % 4 == 0 and 0 < n < prime
    return E, n


def exact_target_divisor(
    modulus: int,
    K: int,
    factors: tuple[tuple[int, int], ...],
    vector: tuple[int, ...],
) -> int:
    if rational_value(factors, vector) > 1:
        vector = tuple(-entry for entry in vector)
    value = Fraction(K) * rational_value(factors, vector)
    assert value.denominator == 1
    divisor = value.numerator
    assert 0 < divisor < K and K * K % divisor == 0
    assert divisor % modulus == (-K) % modulus
    return divisor


def verify_p97_fourier(data: dict[str, object]) -> None:
    modulus = 67
    L = data["L"]
    assert isinstance(L, set) and len(L) == 33
    coordinates = {pow(4, exponent, modulus): exponent for exponent in range(33)}
    assert set(coordinates) == L
    multiplicities = data["multiplicities"]
    assert isinstance(multiplicities, Counter)
    coordinate_multiset = sorted(
        coordinates[value]
        for value, count in multiplicities.items()
        for _ in range(count)
    )
    assert coordinate_multiset == [6, 7, 8, 9, 11, 22, 24, 25, 26, 27]

    root = cmath.exp(2j * pi / 11)
    mhat = sum(root ** (coordinate % 11) for coordinate in coordinate_multiset)
    closed_form = 1 - 2 * cos(2 * pi / 11)
    assert abs(mhat.imag) < 1e-12 and abs(mhat.real - closed_form) < 1e-12
    assert mhat.real < -data["C"] / (data["d"] - 1)

    factors = data["factors"]
    assert isinstance(factors, tuple)
    all_vectors = product(*(range(-nu, nu + 1) for _, nu in factors))
    F_psi = 0j
    F_chi_psi = 0j
    for vector in all_vectors:
        image = vector_image(modulus, factors, vector)
        normalized = image if jacobi(image, modulus) == 1 else (-image) % modulus
        eta = root ** (coordinates[normalized] % 11)
        F_psi += eta
        F_chi_psi += jacobi(image, modulus) * eta
    assert abs((F_psi - F_chi_psi) / 2 - mhat) < 1e-11

    local_coordinates = [coordinate // 3 for coordinate in coordinate_multiset if coordinate % 3 == 0]
    assert sorted(local_coordinates) == [2, 3, 8, 9]
    local_coefficient = sum(root ** (2 * coordinate) for coordinate in local_coordinates)
    assert abs(local_coefficient.imag) < 1e-12
    assert local_coefficient.real <= -len(local_coordinates) / 10
    assert {coordinate % 11 for coordinate in local_coordinates} != {0}


def verify_p73_dyadic_boundary(data: dict[str, object]) -> None:
    factors = data["factors"]
    assert factors == ((2, 1), (5, 2), (23, 1))
    record = next(
        row for row in data["negative_records"] if row[0] == (0, 1, -1)
    )
    vector, _, normalized = record
    assert normalized == 8 and multiplicative_order(normalized, 63) == 2
    relation = tuple(2 * entry for entry in vector)
    assert relation == (0, 2, -2)
    assert vector_image(63, factors, relation) == 1
    assert rational_value(factors, relation) == Fraction(25, 529) < 1

    overflow: dict[int, int] = {}
    for (q, nu), exponent in zip(factors, relation, strict=True):
        if q == 2:
            excess = max(-nu - 1 - exponent, exponent - nu, 0)
        else:
            excess = max(abs(exponent) - nu, 0)
        if excess:
            overflow[q] = excess
    assert overflow == {23: 1}


def verify_composite_primary_boundary() -> None:
    multiplicities: Counter[int] = Counter()
    for first, second in product(range(-1, 2), repeat=2):
        if (first + second) % 2:
            multiplicities[(2 * first + 3 * second) % 6] += 1
    assert multiplicities == Counter({3: 2, 2: 1, 4: 1})

    coefficients: list[int] = []
    negative_orders: set[int] = set()
    for frequency in range(1, 6):
        root = cmath.exp(2j * pi * frequency / 6)
        value = sum(count * root**phase for phase, count in multiplicities.items())
        assert abs(value.imag) < 1e-12
        rounded = round(value.real)
        assert abs(value.real - rounded) < 1e-12
        coefficients.append(rounded)
        if rounded < 0:
            negative_orders.add(6 // gcd(frequency, 6))
    assert coefficients == [-3, 1, 0, 1, -3]
    assert negative_orders == {6}

    # Equality in C = M(d-2) does not force every nontrivial coefficient negative.
    threshold = [0, 1, 0, 1]
    assert sum(threshold) == 1 * (4 - 2)
    threshold_coefficients: list[int] = []
    for frequency in range(1, 4):
        root = cmath.exp(2j * pi * frequency / 4)
        value = sum(count * root**phase for phase, count in enumerate(threshold))
        assert abs(value.imag) < 1e-12
        threshold_coefficients.append(round(value.real))
    assert threshold_coefficients == [0, -2, 0]


def verify() -> None:
    p97 = analyze_core(97, 67, 1625)
    assert p97["C"] == 10 and p97["theta_punctured"] == 21
    assert p97["hybrid"] == p97["parity_hybrid"] == 20
    assert not p97["target_hits"] and not p97["collisions"]
    verify_p97_fourier(p97)

    p73 = analyze_core(73, 63, 1150)
    assert p73["C"] == 18 and p73["theta_punctured"] == 45
    assert p73["hybrid"] == 41 and p73["parity_hybrid"] == 40
    assert not p73["target_hits"] and not p73["collisions"]
    verify_p73_dyadic_boundary(p73)

    p433 = analyze_core(433, 15, 1624)
    assert p433["C"] == 28 and p433["theta_punctured"] == 24
    assert len(p433["target_hits"]) == 6 and len(p433["collisions"]) == 12
    target = (0, 0, -1)
    assert target in p433["target_hits"]
    assert exact_target_divisor(15, 1624, p433["factors"], target) == 56
    pair = ((0, 0, 1), (1, 1, 0))
    assert pair in p433["collisions"]
    assert oriented_relation_terminal(433, 15, 1624, p433["factors"], pair) == (
        3136,
        224,
    )

    verify_composite_primary_boundary()
    print("verified core Jacobi punctured-kernel primary selector")
    print("p97", "global_order_11_fourier", "local_order_11_source_rank")
    print("p73_R63", "pure_2_primary", "scaled_relation_overflow={23:1}")
    print("p433", "punctured_threshold", "type_I=56", "even_predecessor=(3136,224)")
    print("C6xC2", "negative_orders={6}", "q_primary_sign_inheritance=false")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
