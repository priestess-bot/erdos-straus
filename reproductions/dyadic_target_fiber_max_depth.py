#!/usr/bin/env python3
"""Verify the maximum 2-adic target-fiber depth dichotomy."""

from __future__ import annotations

import argparse
from itertools import product
from typing import Sequence

Element = tuple[int, ...]
Exponent = tuple[int, ...]


def add(left: Element, right: Element, moduli: Sequence[int]) -> Element:
    return tuple((a + b) % modulus for a, b, modulus in zip(left, right, moduli))


def scale(value: Element, multiplier: int, moduli: Sequence[int]) -> Element:
    return tuple((multiplier * coordinate) % modulus for coordinate, modulus in zip(value, moduli))


def negate(value: Element, moduli: Sequence[int]) -> Element:
    return scale(value, -1, moduli)


def image(exponent: Exponent, generators: Sequence[Element], moduli: Sequence[int]) -> Element:
    result = tuple(0 for _ in moduli)
    for coefficient, generator in zip(exponent, generators):
        result = add(result, scale(generator, coefficient, moduli), moduli)
    return result


def box(bounds: Sequence[int]) -> tuple[Exponent, ...]:
    return tuple(product(*(range(-bound, bound + 1) for bound in bounds)))


def order(value: Element, moduli: Sequence[int]) -> int:
    identity = tuple(0 for _ in moduli)
    current = identity
    for exponent in range(1, 1 + 4 * max(moduli)):
        current = add(current, value, moduli)
        if current == identity:
            return exponent
    raise AssertionError("element order exceeds control bound")


def cyclic_depth(coordinate: int, modulus: int) -> int:
    """Return max d with coordinate in 2^d C_modulus, for nonzero coordinate."""
    coordinate %= modulus
    if coordinate == 0 or modulus & (modulus - 1):
        raise AssertionError("depth requires a nonzero residue modulo a power of two")
    depth = 0
    while coordinate % 2 == 0:
        coordinate //= 2
        depth += 1
    return depth


def profile(
    *,
    moduli: Sequence[int],
    kernel_modulus: int,
    generators: Sequence[Element],
    bounds: Sequence[int],
    target: Element,
) -> dict[str, object]:
    moduli = tuple(moduli)
    bounds = tuple(bounds)
    if kernel_modulus != moduli[-1] or kernel_modulus & (kernel_modulus - 1):
        raise AssertionError("the control kernel must be the final C_(2^a) coordinate")
    kernel_exponent = kernel_modulus.bit_length() - 1
    top_depth = kernel_exponent - 1
    if len(generators) != len(bounds) or len(target) != len(moduli):
        raise AssertionError("dimension mismatch")
    kernel_elements = tuple(
        tuple([0] * (len(moduli) - 1) + [coordinate])
        for coordinate in range(kernel_modulus)
    )
    identity = tuple(0 for _ in moduli)
    if order(target, moduli) != 2:
        raise AssertionError("target must be an involution")
    if target in kernel_elements:
        target_in_kernel = True
    else:
        target_in_kernel = False

    exponents = box(bounds)
    source_set = {image(exponent, generators, moduli) for exponent in exponents}
    if target in source_set:
        raise AssertionError("control must miss the exact target")
    target_coset = {
        add(target, kernel_element, moduli) for kernel_element in kernel_elements
    }
    if not source_set & target_coset:
        raise AssertionError("target coset must be hit")
    fiber_values = {
        (add(source, negate(target, moduli), moduli)[-1] % kernel_modulus)
        for source in source_set & target_coset
    }
    if 0 in fiber_values:
        raise AssertionError("exact target unexpectedly appeared in source set")
    depths = {value: cyclic_depth(value, kernel_modulus) for value in fiber_values}
    maximum_depth = max(depths.values())
    layer = 1 << (maximum_depth + 1)
    subgroup = {
        tuple([0] * (len(moduli) - 1) + [coordinate])
        for coordinate in range(0, kernel_modulus, layer)
    }
    if (source_set & {
        add(target, subgroup_element, moduli) for subgroup_element in subgroup
    }):
        raise AssertionError("maximum-depth subgroup intersects target fiber")

    quotient_fiber = {
        value % layer for value in fiber_values
    }
    top_digit = 1 << maximum_depth
    if top_digit not in quotient_fiber:
        raise AssertionError("maximum-depth fiber did not produce quotient top digit")
    quotient_strict = maximum_depth < top_depth

    fiber_exponents = tuple(
        exponent
        for exponent in exponents
        if image(exponent, generators, moduli) in target_coset
    )
    pairs: list[tuple[Exponent, Exponent]] = []
    fixed: list[Exponent] = []
    unseen = set(fiber_exponents)
    while unseen:
        left = min(unseen)
        right = tuple(-coordinate for coordinate in left)
        if right == left:
            fixed.append(left)
            unseen.remove(left)
            continue
        if right not in unseen:
            raise AssertionError("symmetric box did not give a complete antipodal fiber")
        pairs.append((left, right))
        unseen.remove(left)
        unseen.remove(right)

    pair_receipts: list[dict[str, object]] = []
    for left, right in pairs:
        source = image(left, generators, moduli)
        kernel_offset = add(source, negate(target, moduli), moduli)[-1] % kernel_modulus
        delta = tuple(2 * coordinate for coordinate in left)
        relation = image(delta, generators, moduli)
        expected_relation = tuple(
            [0] * (len(moduli) - 1) + [(2 * kernel_offset) % kernel_modulus]
        )
        if relation != expected_relation:
            raise AssertionError("antipodal relation did not map to twice the fiber offset")
        pair_depth = depths[kernel_offset]
        overflow = tuple(
            max(abs(coordinate) - bound, 0)
            for coordinate, bound in zip(delta, bounds)
        )
        short = not any(overflow)
        if pair_depth < top_depth and relation == identity:
            raise AssertionError("a non-top dyadic offset produced a zero relation")
        if pair_depth < top_depth:
            relation_depth = cyclic_depth(relation[-1], kernel_modulus)
            if relation_depth != pair_depth + 1:
                raise AssertionError("relation depth did not increase by one")
        pair_receipts.append(
            {
                "left": list(left),
                "right": list(right),
                "kernel_offset": kernel_offset,
                "offset_depth": pair_depth,
                "delta": list(delta),
                "relation": list(relation),
                "short_relation": short,
                "overflow": list(overflow),
                "relation_is_zero": relation == identity,
            }
        )

    if target_in_kernel and identity not in {
        image(exponent, generators, moduli)
        for exponent in fiber_exponents
        if exponent == tuple(0 for _ in bounds)
    }:
        raise AssertionError("target-in-kernel control lost its fixed exponent")
    if target_in_kernel and maximum_depth != top_depth:
        raise AssertionError("an involution inside cyclic K must expose the top digit")

    return {
        "kernel_modulus": kernel_modulus,
        "target_in_kernel": target_in_kernel,
        "fiber_values": sorted(fiber_values),
        "fiber_depths": {str(value): depth for value, depth in sorted(depths.items())},
        "maximum_depth": maximum_depth,
        "quotient_layer": layer,
        "quotient_subgroup": sorted(element[-1] for element in subgroup),
        "quotient_strict": quotient_strict,
        "quotient_fiber": sorted(quotient_fiber),
        "top_digit": top_digit,
        "fiber_exponent_count": len(fiber_exponents),
        "antipodal_pair_count": len(pairs),
        "fixed_exponents": [list(exponent) for exponent in fixed],
        "pairs": pair_receipts,
        "certificate_type": (
            "DYADIC_TARGET_FIBER_QUOTIENT_DESCENT"
            if quotient_strict
            else "TOP_DYADIC_TARGET_FIBER"
        ),
    }


def verify() -> None:
    common = {
        "moduli": (2, 8),
        "kernel_modulus": 8,
        "target": (1, 0),
    }
    strict = profile(
        generators=((1, 2),),
        bounds=(1,),
        **common,
    )
    assert strict["fiber_values"] == [2, 6]
    assert strict["maximum_depth"] == 1
    assert strict["quotient_layer"] == 4
    assert strict["quotient_strict"] is True
    assert strict["quotient_fiber"] == [2]
    assert strict["certificate_type"] == "DYADIC_TARGET_FIBER_QUOTIENT_DESCENT"
    assert strict["pairs"][0]["short_relation"] is False
    assert strict["pairs"][0]["relation"] == [0, 4]

    short = profile(
        generators=((1, 2),),
        bounds=(2,),
        **common,
    )
    assert short["quotient_strict"] is True
    assert short["pairs"][0]["short_relation"] is True
    assert short["pairs"][0]["relation"] == [0, 4]

    top = profile(
        generators=((1, 4),),
        bounds=(1,),
        **common,
    )
    assert top["fiber_values"] == [4]
    assert top["maximum_depth"] == 2
    assert top["quotient_layer"] == 8
    assert top["quotient_strict"] is False
    assert top["certificate_type"] == "TOP_DYADIC_TARGET_FIBER"
    assert top["pairs"][0]["relation_is_zero"] is True

    in_kernel = profile(
        moduli=(8,),
        kernel_modulus=8,
        generators=((1,),),
        bounds=(1,),
        target=(4,),
    )
    assert in_kernel["target_in_kernel"] is True
    assert in_kernel["maximum_depth"] == 2
    assert in_kernel["fixed_exponents"] == [[0]]
    assert in_kernel["certificate_type"] == "TOP_DYADIC_TARGET_FIBER"

    print("verified maximum-depth dyadic target-fiber dichotomy")
    print(
        {
            "strict_quotient": "C8_to_C4",
            "short_relation": "2z_maps_to_C2_subgroup",
            "top_terminal": "order_two_offset",
            "in_kernel_fixed_point": "z=0_is_allowed_only_in_top_case",
        }
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
