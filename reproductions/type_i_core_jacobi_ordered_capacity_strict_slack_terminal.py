#!/usr/bin/env python3
"""Verify the core Jacobi ordered-capacity strict slack theorem."""

from __future__ import annotations

import argparse
from itertools import product
from math import gcd, isqrt, prod


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


def jacobi(a: int, odd_modulus: int) -> int:
    assert odd_modulus > 0 and odd_modulus % 2 == 1 and gcd(a, odd_modulus) == 1
    a %= odd_modulus
    result = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if odd_modulus % 8 in (3, 5):
                result = -result
        a, odd_modulus = odd_modulus, a
        if a % 4 == odd_modulus % 4 == 3:
            result = -result
        a %= odd_modulus
    assert odd_modulus == 1
    return result


def generated_subgroup(generators: tuple[int, ...], modulus: int) -> set[int]:
    subgroup = {1 % modulus}
    frontier = [1 % modulus]
    steps = tuple(sorted(set(generators) | {pow(g, -1, modulus) for g in generators}))
    while frontier:
        value = frontier.pop()
        for step in steps:
            successor = value * step % modulus
            if successor not in subgroup:
                subgroup.add(successor)
                frontier.append(successor)
    return subgroup


def sign_intervals(exponent: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    return tuple(range(exponent + 1)), tuple(range(-exponent, 0))


def analyze_core(prime: int, modulus: int, K: int) -> dict[str, object]:
    assert is_prime(prime) and prime % 24 == 1
    assert 4 * K == prime * modulus + 1 and modulus % 4 == 3
    factors = factorint(K)
    assert prod(q**nu for q, nu in factors) == K
    generators = tuple(q % modulus for q, _ in factors)
    H = generated_subgroup(generators, modulus)
    target = modulus - 1
    assert target in H and jacobi(target, modulus) == -1
    active = tuple(index for index, (q, _) in enumerate(factors) if jacobi(q, modulus) == -1)
    assert active
    assert sum(factors[index][1] for index in active) % 2 == 0
    d = len(H) // 2
    assert len(H) == 2 * d

    boxes: list[dict[str, object]] = []
    collision: tuple[tuple[int, ...], tuple[int, ...]] | None = None
    for signs in product((0, 1), repeat=len(factors)):
        intervals = tuple(sign_intervals(nu)[sign] for sign, (_, nu) in zip(signs, factors, strict=True))
        vectors = tuple(product(*intervals))
        images: dict[int, tuple[int, ...]] = {}
        character_sum = 0
        filtered = 0
        for vector in vectors:
            image = prod(pow(q, exponent, modulus) for (q, _), exponent in zip(factors, vector, strict=True)) % modulus
            character = jacobi(image, modulus)
            character_sum += character
            filtered += character == -1
            if image in images and collision is None:
                collision = (images[image], vector)
            images.setdefault(image, vector)

        special = all(
            signs[index] == (0 if factors[index][1] % 2 == 0 else 1)
            for index in active
        )
        b = len(vectors)
        theta = min(b, d)
        assert filtered == (b - character_sum) // 2
        assert (character_sum > 0) == special
        if b <= len(H) and len(images) == b:
            assert filtered <= theta - int(special)
        boxes.append(
            {
                "signs": signs,
                "size": b,
                "filtered": filtered,
                "character_sum": character_sum,
                "theta": theta,
                "injective": len(images) == b,
                "special": special,
            }
        )

    C = sum(int(box["filtered"]) for box in boxes)
    theta_ordered = sum(int(box["theta"]) for box in boxes)
    special_count = sum(bool(box["special"]) for box in boxes)
    expected_special = 2 ** (len(factors) - len(active))
    V = prod(2 * nu + 1 for _, nu in factors)
    A0 = prod(2 * factors[index][1] + 1 for index in range(len(factors)) if index not in active)
    assert special_count == expected_special
    assert C == (V - A0) // 2

    no_collision = collision is None
    if no_collision:
        assert C <= theta_ordered - expected_special
        assert C <= d * 2 ** len(factors) - 1
        assert V <= 2 ** len(factors) * len(H)

    return {
        "factors": factors,
        "H_order": len(H),
        "active": active,
        "boxes": boxes,
        "C": C,
        "theta_ordered": theta_ordered,
        "strong_capacity": d * 2 ** len(factors),
        "special_count": special_count,
        "collision": collision,
    }


def collision_terminal(
    prime: int,
    modulus: int,
    K: int,
    factors: tuple[tuple[int, int], ...],
    collision: tuple[tuple[int, ...], tuple[int, ...]],
) -> tuple[int, int]:
    left, right = collision
    relation = tuple(a - b for a, b in zip(left, right, strict=True))
    numerator = prod(q**max(exponent, 0) for (q, _), exponent in zip(factors, relation, strict=True))
    denominator = prod(q**max(-exponent, 0) for (q, _), exponent in zip(factors, relation, strict=True))
    if numerator > denominator:
        relation = tuple(-exponent for exponent in relation)
    U = prod(q ** (nu + exponent) for (q, nu), exponent in zip(factors, relation, strict=True))
    assert 0 < U < K and U % modulus == K % modulus
    E = 4 * U
    n = (4 * K - E) // modulus
    assert E % modulus == 1 and 0 < n < prime and n % 4 == 0
    return E, n


def verify_balanced_fixed_layer_boundary() -> None:
    # Additive H=C6, J={0,1}, chi(x)=(-1)^x, y=3.
    J = (0, 1)
    images_by_box: list[list[int]] = []
    C = 0
    theta = 0
    for first, second in product((0, 1), repeat=2):
        interval_1 = sign_intervals(1)[first]
        interval_2 = sign_intervals(1)[second]
        images = [(z1 + 2 * z2) % 6 for z1, z2 in product(interval_1, interval_2)]
        assert len(images) == len(set(images))
        images_by_box.append(images)
        for image in images:
            C += sum((j + image - 3) % 2 == 0 for j in J)
        theta += len(images)
    assert [len(images) for images in images_by_box] == [4, 2, 2, 1]
    assert C == theta == 9


def verify() -> None:
    nonuniform = analyze_core(97, 67, 1625)
    assert nonuniform["active"] == (0, 1)
    assert [(box["size"], box["filtered"]) for box in nonuniform["boxes"]] == [
        (8, 4),
        (4, 2),
        (6, 3),
        (3, 1),
    ]
    assert nonuniform["C"] == 10
    assert nonuniform["theta_ordered"] == 21
    assert nonuniform["strong_capacity"] == 132
    assert nonuniform["collision"] is None

    squareful_modulus = analyze_core(73, 27, 493)
    assert squareful_modulus["H_order"] == 18
    assert squareful_modulus["C"] == 4
    assert squareful_modulus["theta_ordered"] == 9
    assert squareful_modulus["collision"] is None

    positive = analyze_core(433, 15, 1624)
    assert positive["collision"] is not None
    terminal = collision_terminal(
        433,
        15,
        1624,
        positive["factors"],
        positive["collision"],
    )
    verify_balanced_fixed_layer_boundary()

    print("verified core Jacobi ordered-capacity strict slack")
    print("p97", "C=10", "Theta=21", "strong_capacity=132")
    print("p73_R27", "C=4", "Theta=9", "squareful_modulus")
    print("p433_collision_terminal", terminal)
    print("balanced_fixed_layer_boundary", "C=Theta=9", "no_same_sign_collision")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
