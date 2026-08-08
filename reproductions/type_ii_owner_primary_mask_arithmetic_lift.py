#!/usr/bin/env python3
"""Verify owner primary-mask arithmetic lifting and obstruction branches."""

from __future__ import annotations

import argparse
from math import gcd, isqrt

from type_ii_owner_kernel_primary_digit_certificate import owner_primary_dispatch


def divisors(value: int) -> tuple[int, ...]:
    """Return positive divisors in increasing order."""
    lower: list[int] = []
    upper: list[int] = []
    for divisor in range(1, isqrt(value) + 1):
        if value % divisor:
            continue
        lower.append(divisor)
        if divisor * divisor != value:
            upper.append(value // divisor)
    return tuple(lower + list(reversed(upper)))


def squarefree(value: int) -> bool:
    """Check that no prime square divides a positive integer."""
    divisor = 2
    remaining = value
    while divisor * divisor <= remaining:
        if remaining % (divisor * divisor) == 0:
            return False
        divisor = 3 if divisor == 2 else divisor + 2
    return True


def admissible_pairs(prime: int, layer: int) -> tuple[tuple[int, int], ...]:
    """Enumerate the finite Type II parameter menu below one original layer."""
    pairs: list[tuple[int, int]] = []
    for lower_layer in divisors(layer):
        for parameter in divisors(lower_layer):
            if not squarefree(lower_layer // parameter):
                continue
            if 4 * parameter * lower_layer >= prime:
                continue
            pairs.append((lower_layer, parameter))
    return tuple(pairs)


def owner_mask_lift(
    prime: int,
    layer: int,
    records: tuple[tuple[int, int], ...],
    *,
    group_map: bool = True,
) -> dict[str, object]:
    """Return the first arithmetic branch for one selected owner mask."""
    factors = [factor for _, factor in records]
    for source_parameter, factor in records:
        if factor <= 1 or gcd(factor, 4 * layer) != 1:
            return {"status": "OWNER_MASK_FIBER_REALIZATION_OBSTRUCTED"}
        if (prime + 4 * layer * source_parameter) % factor:
            return {"status": "OWNER_MASK_FIBER_REALIZATION_OBSTRUCTED"}
    for left, (_, first) in enumerate(records):
        for _, (_, second) in enumerate(records[left + 1 :], start=left + 1):
            if gcd(first, second) != 1:
                return {"status": "OWNER_MASK_SHARED_Q_COLLISION"}

    if not group_map:
        return {"status": "OWNER_MASK_GROUP_MAP_OBSTRUCTED"}

    product = 1
    for factor in factors:
        product *= factor

    same_modulus_seen = False
    for lower_layer, parameter in admissible_pairs(prime, layer):
        x = parameter * lower_layer
        if any(x % factor != (layer * source_parameter) % factor for source_parameter, factor in records):
            continue
        if product % (4 * lower_layer) == 4 * lower_layer - 1:
            K = (product + 1) // (4 * lower_layer)
            numerator = K * prime + parameter
            if numerator % product:
                raise AssertionError("normal form lost integrality")
            B = numerator // product
            if B <= parameter:
                raise AssertionError("normal form lost B>A")
            return {
                "status": "OWNER_MASK_TYPE_II_SHORT_CERTIFICATE",
                "D_prime": lower_layer,
                "A": parameter,
                "C": lower_layer // parameter,
                "K": K,
                "B": B,
                "factor": product,
            }
        if lower_layer < layer:
            return {
                "status": "OWNER_MASK_STRICT_SOURCE_SWITCH_RELAY",
                "D_prime": lower_layer,
                "A": parameter,
                "factor": product,
            }
        same_modulus_seen = True

    if same_modulus_seen:
        return {"status": "OWNER_MASK_SAME_MODULUS_RELAY_UNCLOSED"}
    return {
        "status": "OWNER_MASK_ADMISSIBLE_FIBER_EMPTY",
        "factor": product,
    }


def run_verification() -> dict[str, object]:
    # Compose the previous primary mask with the actual q=7 source factor.
    primary = owner_primary_dispatch(
        [1],
        1,
        2,
        1,
        slots=("q7-slot",),
        budgets={"q7-slot": 1},
    )
    assert primary["status"] == "OWNER_PRIMARY_TYPE_II_SHORT_CERTIFICATE"
    single = owner_mask_lift(5_113, 6, ((6, 7),))
    assert single["status"] == "OWNER_MASK_TYPE_II_SHORT_CERTIFICATE"
    assert single["K"] == 2
    assert single["B"] == 1_461
    assert single["C"] == 1

    # Two distinct source labels still lift through one common D'=1 fiber.
    double = owner_mask_lift(5_113, 6, ((3, 17), (6, 7)))
    assert double["status"] == "OWNER_MASK_TYPE_II_SHORT_CERTIFICATE"
    assert double["factor"] == 119
    assert double["K"] == 30
    assert double["B"] == 1_289

    # The p=97 pooled pseudo-hit has h=143 but no admissible x=A*D' <= D^2.
    empty = owner_mask_lift(97, 6, ((1, 11), (3, 13)))
    assert empty["status"] == "OWNER_MASK_ADMISSIBLE_FIBER_EMPTY"
    assert empty["factor"] == 143

    # A target map with the wrong invariant factors fails before arithmetic charging.
    group_obstructed = owner_mask_lift(
        5_113,
        6,
        ((6, 7),),
        group_map=False,
    )
    assert group_obstructed["status"] == "OWNER_MASK_GROUP_MAP_OBSTRUCTED"

    return {
        "primary_mask": primary,
        "single": single,
        "double": double,
        "empty": empty,
        "group_obstructed": group_obstructed,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    result = run_verification()
    print("verified owner primary-mask arithmetic lift")
    for key in ("single", "double", "empty", "group_obstructed"):
        print(key, result[key]["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
