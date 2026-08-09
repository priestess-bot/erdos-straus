#!/usr/bin/env python3
"""Exact non-cyclic finite-abelian quotient Fourier control.

The group-ring payload is integral for every finite abelian quotient.  The
focused verifier evaluates the C2 x C4 control in Gaussian integers, so the
canonical deficit character and all Parseval checks avoid floating point.
"""

from __future__ import annotations

import argparse
from collections import Counter
from math import gcd, lcm
from typing import Iterable, Mapping, Sequence

Element = tuple[int, ...]
Gaussian = tuple[int, int]


def _check_moduli(moduli: Sequence[int]) -> tuple[int, ...]:
    normalized = tuple(int(modulus) for modulus in moduli)
    if not normalized or any(modulus < 2 for modulus in normalized):
        raise AssertionError("invariant factors must be at least 2")
    return normalized


def elements(moduli: Sequence[int]) -> tuple[Element, ...]:
    moduli = _check_moduli(moduli)
    result: list[Element] = [()]
    for modulus in moduli:
        result = [prefix + (coordinate,) for prefix in result for coordinate in range(modulus)]
    return tuple(result)


def add(left: Element, right: Element, moduli: Sequence[int]) -> Element:
    return tuple((a + b) % modulus for a, b, modulus in zip(left, right, moduli))


def negate(value: Element, moduli: Sequence[int]) -> Element:
    return tuple((-coordinate) % modulus for coordinate, modulus in zip(value, moduli))


def subtract(left: Element, right: Element, moduli: Sequence[int]) -> Element:
    return add(left, negate(right, moduli), moduli)


def _zero(moduli: Sequence[int]) -> Element:
    return tuple(0 for _ in moduli)


def product_blocks(
    moduli: Sequence[int], blocks: Iterable[Iterable[Element]]
) -> dict[Element, int]:
    moduli = _check_moduli(moduli)
    counts: Counter[Element] = Counter({_zero(moduli): 1})
    universe = set(elements(moduli))
    for block in blocks:
        values = tuple(block)
        if not values or any(value not in universe for value in values):
            raise AssertionError("each block must be a nonempty subset of the quotient")
        next_counts: Counter[Element] = Counter()
        for left, left_count in counts.items():
            for right in values:
                next_counts[add(left, right, moduli)] += left_count
        counts = next_counts
    return {value: counts.get(value, 0) for value in universe}


def autocorrelation(
    counts: Mapping[Element, int], moduli: Sequence[int]
) -> dict[Element, int]:
    moduli = _check_moduli(moduli)
    universe = elements(moduli)
    return {
        shift: sum(
            counts.get(value, 0)
            * counts.get(subtract(value, shift, moduli), 0)
            for value in universe
        )
        for shift in universe
    }


def character_order(index: Element, moduli: Sequence[int]) -> int:
    order = 1
    for coordinate, modulus in zip(index, moduli):
        order = lcm(order, modulus // gcd(modulus, coordinate))
    return order


def gaussian_add(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def gaussian_scale(value: Gaussian, scalar: int) -> Gaussian:
    return scalar * value[0], scalar * value[1]


def gaussian_mul(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] * right[0] - left[1] * right[1], left[0] * right[1] + left[1] * right[0]


def gaussian_conjugate(value: Gaussian) -> Gaussian:
    return value[0], -value[1]


def gaussian_norm(value: Gaussian) -> int:
    return value[0] * value[0] + value[1] * value[1]


def root_of_unity(exponent: int, modulus: int) -> Gaussian:
    """Return exp(2*pi*i*exponent/modulus) for modulus 2 or 4."""
    if modulus == 2:
        return (-1, 0) if exponent % 2 else (1, 0)
    if modulus == 4:
        return ((1, 0), (0, 1), (-1, 0), (0, -1))[exponent % 4]
    raise AssertionError("focused exact backend supports only factors 2 and 4")


def character_value(index: Element, value: Element, moduli: Sequence[int]) -> Gaussian:
    phase: Gaussian = (1, 0)
    for k, x, modulus in zip(index, value, moduli):
        phase = gaussian_mul(phase, root_of_unity(k * x, modulus))
    return phase


def fourier_value(
    counts: Mapping[Element, int], index: Element, moduli: Sequence[int]
) -> Gaussian:
    value: Gaussian = (0, 0)
    for point, multiplicity in counts.items():
        value = gaussian_add(
            value,
            gaussian_scale(character_value(index, point, moduli), multiplicity),
        )
    return value


def energy_from_group_ring(
    correlation: Mapping[Element, int], index: Element, moduli: Sequence[int]
) -> Gaussian:
    value: Gaussian = (0, 0)
    for shift, coefficient in correlation.items():
        value = gaussian_add(
            value,
            gaussian_scale(character_value(index, shift, moduli), coefficient),
        )
    return value


def noncyclic_fourier_profile(
    *,
    moduli: Sequence[int],
    counts: Mapping[Element, int],
    target: Element,
) -> dict[str, object]:
    """Build a canonical exact profile for the C2 x C4 control backend.

    The theorem behind this payload is valid for every finite abelian quotient;
    the focused backend uses Gaussian integers because all invariant factors in
    the control divide four.
    """
    moduli = _check_moduli(moduli)
    if any(modulus not in (2, 4) for modulus in moduli):
        raise AssertionError("focused verifier requires invariant factors 2 or 4")
    universe = elements(moduli)
    target = tuple(target)
    if target not in universe or set(counts) != set(universe):
        raise AssertionError("counts and target must cover the quotient")
    if any(multiplicity < 0 for multiplicity in counts.values()):
        raise AssertionError("representation counts must be nonnegative")

    correlation = autocorrelation(counts, moduli)
    total = sum(counts.values())
    sum_squares = sum(value * value for value in counts.values())
    group_order = len(universe)
    target_count = counts[target]
    if total <= 0:
        raise AssertionError("the Fourier deficit lemma needs a nonempty source box")
    if target_count == 0 and group_order <= 1:
        raise AssertionError("a nonempty singleton quotient cannot miss its target")

    characters = [value for value in universe if value != _zero(moduli)]
    samples: dict[Element, dict[str, int]] = {}
    for index in characters:
        coefficient = fourier_value(counts, index, moduli)
        ring_energy = energy_from_group_ring(correlation, index, moduli)
        if ring_energy != (gaussian_norm(coefficient), 0):
            raise AssertionError("group-ring energy does not equal Fourier norm")
        twisted = gaussian_mul(
            gaussian_conjugate(character_value(index, target, moduli)), coefficient
        )
        samples[index] = {
            "character_order": character_order(index, moduli),
            "fourier_real": coefficient[0],
            "fourier_imag": coefficient[1],
            "energy": gaussian_norm(coefficient),
            "twisted_real": twisted[0],
            "deficit": -twisted[0],
        }

    nontrivial_energy = group_order * sum_squares - total * total
    if sum(sample["energy"] for sample in samples.values()) != nontrivial_energy:
        raise AssertionError("nontrivial Parseval energy mismatch")
    deficit_sum = sum(sample["twisted_real"] for sample in samples.values())
    expected_deficit_sum = group_order * target_count - total
    if deficit_sum != expected_deficit_sum:
        raise AssertionError("target Fourier deficit identity mismatch")

    certificate = None
    if target_count == 0:
        certificate_index = min(
            characters,
            key=lambda index: (
                -samples[index]["deficit"],
                samples[index]["character_order"],
                index,
            ),
        )
        certificate = {
            "kind": "NONCYCLIC_FOURIER_DEFICIT",
            "character_index": list(certificate_index),
            "character_order": samples[certificate_index]["character_order"],
            "deficit": samples[certificate_index]["deficit"],
            "threshold_numerator": total,
            "threshold_denominator": group_order - 1,
        }
        if certificate["deficit"] * (group_order - 1) < total:
            raise AssertionError("canonical deficit misses the universal threshold")

    return {
        "moduli": list(moduli),
        "group_order": group_order,
        "target": list(target),
        "target_count": target_count,
        "total": total,
        "sum_squares": sum_squares,
        "nontrivial_parseval_energy": nontrivial_energy,
        "correlation": {"/".join(map(str, key)): value for key, value in correlation.items()},
        "certificate": certificate,
    }


def verify() -> None:
    moduli = (2, 4)
    zero = (0, 0)
    blocks = (
        ((0, 0), (1, 0)),
        ((0, 0), (0, 1), (0, 3)),
    )
    counts = product_blocks(moduli, blocks)
    profile = noncyclic_fourier_profile(
        moduli=moduli,
        counts=counts,
        target=(1, 2),
    )
    assert profile["group_order"] == 8
    assert profile["total"] == 6
    assert profile["target_count"] == 0
    assert profile["nontrivial_parseval_energy"] == 12
    certificate = profile["certificate"]
    assert certificate is not None
    assert certificate["character_index"] == [0, 2]
    assert certificate["character_order"] == 2
    assert certificate["deficit"] == 2
    assert certificate["threshold_numerator"] == 6
    assert certificate["threshold_denominator"] == 7
    print("verified non-cyclic quotient Fourier certificate")
    print(
        {
            "quotient": "C2xC4",
            "target": "(1,2)",
            "certificate": "NONCYCLIC_FOURIER_DEFICIT",
            "character": "(0,2)",
            "deficit": 2,
            "parseval_nontrivial_energy": 12,
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
