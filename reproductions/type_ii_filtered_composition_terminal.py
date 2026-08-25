#!/usr/bin/env python3
"""Verify a filtered composition-series Type II terminal certificate."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import product
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-ii-filtered-composition-terminal-results.json"
)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor = 3 if divisor == 2 else divisor + 2
    return True


def add(left: tuple[int, ...], right: tuple[int, ...], moduli: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((x + y) % modulus for x, y, modulus in zip(left, right, moduli))


def is_subgroup(
    subset: set[tuple[int, ...]], moduli: tuple[int, ...]
) -> bool:
    zero = tuple(0 for _ in moduli)
    return (
        zero in subset
        and all(
            add(left, right, moduli) in subset
            for left in subset
            for right in subset
        )
    )


def product_set(
    vectors: list[tuple[int, ...]], moduli: tuple[int, ...]
) -> set[tuple[int, ...]]:
    reached = {tuple(0 for _ in moduli)}
    for vector in vectors:
        reached |= {add(value, vector, moduli) for value in tuple(reached)}
    return reached


def stabilizer(
    subset: set[tuple[int, ...]],
    group: set[tuple[int, ...]],
    moduli: tuple[int, ...],
) -> set[tuple[int, ...]]:
    return {
        shift
        for shift in group
        if {add(value, shift, moduli) for value in subset} == subset
    }


def is_squarefree(value: int) -> bool:
    divisor = 2
    while divisor * divisor <= value:
        if value % (divisor * divisor) == 0:
            return False
        divisor = 3 if divisor == 2 else divisor + 2
    return True


def unit_group_example() -> dict[str, object]:
    prime = 3313
    original_D = 12
    A = 1
    D_star = 3
    modulus = 4 * D_star
    N = prime + 4 * A * D_star
    C = D_star // A
    base_factor = 1
    moduli = (2, 2)
    H_0 = {(0, 0)}
    H_1 = {(0, 0), (1, 0)}
    H_2 = set(product(range(2), repeat=2))
    chain = [H_0, H_1, H_2]
    slots = [
        {
            "label": "source-q-5",
            "factor": 5,
            "vector": (1, 0),
            "layer": 1,
            "source_a": 4,
            "same_fiber": "A=1,D*=3",
            "independent": True,
        },
        {
            "label": "source-q-7",
            "factor": 7,
            "vector": (0, 1),
            "layer": 2,
            "source_a": 2,
            "same_fiber": "A=1,D*=3",
            "independent": True,
        },
    ]
    residue = {
        (0, 0): 1,
        (1, 0): 5,
        (0, 1): 7,
        (1, 1): 11,
    }
    if not (
        is_prime(prime)
        and prime % 24 == 1
        and A > 0
        and A <= D_star
        and D_star % A == 0
        and is_squarefree(D_star // A)
        and 4 * A * D_star < prime
        and N == 3325
        and N % base_factor == 0
        and gcd(base_factor, modulus) == 1
        and all(is_subgroup(layer, moduli) for layer in chain)
        and all(chain[index - 1] < chain[index] for index in range(1, len(chain)))
    ):
        raise AssertionError("filtered composition example setup failed")
    for index in range(1, len(chain)):
        quotient_order = len(chain[index]) // len(chain[index - 1])
        if not is_prime(quotient_order):
            raise AssertionError("composition quotient was not prime")
    factors = [int(slot["factor"]) for slot in slots]
    ledger_products: list[int] = []
    for selection in product((0, 1), repeat=len(factors)):
        ledger_product = base_factor
        for include, factor in zip(selection, factors):
            if include:
                ledger_product *= factor
        ledger_products.append(ledger_product)
    if not (
        all(N % factor == 0 and gcd(factor, modulus) == 1 for factor in factors)
        and all(N % ledger_product == 0 for ledger_product in ledger_products)
        and all(
            (prime + 4 * original_D * int(slot["source_a"])) % int(slot["factor"]) == 0
            and (A * D_star - original_D * int(slot["source_a"])) % int(slot["factor"]) == 0
            for slot in slots
        )
        and all(gcd(left, right) == 1 for index, left in enumerate(factors) for right in factors[index + 1 :])
        and all(bool(slot["independent"]) for slot in slots)
        and len({str(slot["same_fiber"]) for slot in slots}) == 1
    ):
        raise AssertionError("physical same-fiber source-slot contract failed")
    for slot in slots:
        layer = int(slot["layer"])
        vector = tuple(slot["vector"])
        if vector not in chain[layer] or vector in chain[layer - 1]:
            raise AssertionError("slot did not survive in its claimed composition quotient")
    filtered_capacity = [
        {
            "layer": index,
            "quotient_order": len(chain[index]) // len(chain[index - 1]),
            "available_slots": sum(int(slot["layer"]) == index for slot in slots),
        }
        for index in range(1, len(chain))
    ]
    if not all(
        int(item["available_slots"]) >= int(item["quotient_order"]) - 1
        for item in filtered_capacity
    ):
        raise AssertionError("filtered composition capacity threshold failed")
    for left in H_2:
        for right in H_2:
            if residue[add(left, right, moduli)] != (
                residue[left] * residue[right] % modulus
            ):
                raise AssertionError("coordinate map was not a unit-group homomorphism")
    reached = product_set([tuple(slot["vector"]) for slot in slots], moduli)
    if reached != H_2:
        raise AssertionError("composition-layer slots did not cover the full group")
    final_stabilizer = stabilizer(reached, H_2, moduli)
    if final_stabilizer != H_2:
        raise AssertionError("full covered product set was not stabilizer saturated")
    target = (1, 1)
    selected_factors = factors
    h = base_factor
    for factor in selected_factors:
        h *= factor
    if not (
        target in reached
        and residue[target] == (-1) % modulus
        and h % modulus == (-1) % modulus
        and N % h == 0
        and all(factor % modulus != (-1) % modulus for factor in (5, 7, 19))
    ):
        raise AssertionError("covered target did not yield a physical divisor")
    K = (h + 1) // modulus
    B_numerator = K * prime + A
    if B_numerator % h:
        raise AssertionError("Type II ray quotient was not integral")
    B = B_numerator // h
    x = A * B * C
    d = A * A * C
    m_numerator = A + B
    if m_numerator % K:
        raise AssertionError("Type II gap was not integral")
    m = m_numerator // K
    y_numerator = prime * (x + d)
    z_numerator = prime * x * (x + d)
    if y_numerator % m or z_numerator % (m * d):
        raise AssertionError("Type II denominators were not integral")
    y = y_numerator // m
    z = z_numerator // (m * d)
    solution = [x, y, z]
    if not (
        h == 4 * A * C * K - 1
        and B >= A
        and d <= x
        and x * x % d == 0
        and (x + d) % m == 0
        and prime == 4 * x - m
        and sum((Fraction(1, value) for value in solution), Fraction()) == Fraction(4, prime)
    ):
        raise AssertionError("Type II certificate verification failed")
    one_slot_reached = product_set([(1, 0)], moduli)
    if target in one_slot_reached:
        raise AssertionError("threshold sharpness fixture changed")
    return {
        "prime": prime,
        "fiber": {
            "original_D": original_D,
            "A": A,
            "D_star": D_star,
            "C": C,
            "modulus": modulus,
            "N": N,
            "base_factor": base_factor,
            "same_fiber_id": slots[0]["same_fiber"],
            "N_factorization": [5, 5, 7, 19],
        },
        "composition_series": [
            {"index": index, "order": len(layer), "elements": [list(value) for value in sorted(layer)]}
            for index, layer in enumerate(chain)
        ],
        "physical_source_slots": slots,
        "filtered_capacity": filtered_capacity,
        "unit_group_coordinate_map": {
            ",".join(map(str, key)): value for key, value in sorted(residue.items())
        },
        "target": {
            "coordinate": list(target),
            "residue": residue[target],
            "selected_factors": selected_factors,
            "h": h,
        },
        "coverage": {
            "reached_coordinates": [list(value) for value in sorted(reached)],
            "full_group_covered": reached == H_2,
            "one_slot_target_missing": target not in one_slot_reached,
            "ledger_products": ledger_products,
            "final_stabilizer_coordinates": [
                list(value) for value in sorted(final_stabilizer)
            ],
            "final_stabilizer_saturated": final_stabilizer == H_2,
        },
        "type_ii_certificate": {
            "raw_parameters": {"A": A, "B": B, "C": C, "K": K},
            "normal_form": {"A": 1, "B": B, "C": C, "K": K},
            "gap": m,
            "x": x,
            "d": d,
            "denominators": solution,
        },
    }


def build_result() -> dict[str, object]:
    example = unit_group_example()
    return {
        "schema_version": 1,
        "certificate_type": "type_ii_filtered_composition_terminal_v1",
        "selector_status": "terminal_leaf",
        "recursive_edge_eligible": False,
        "theorem_scope": (
            "conditional on same-fiber independently selectable physical source slots "
            "and a final stabilizer-saturated quotient lift"
        ),
        "example": example,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified filtered composition Type II terminal")
        return
    args.output.write_text(json.dumps(result, ensure_ascii=True, indent=2) + "\n")
    print(args.output)


if __name__ == "__main__":
    main()
