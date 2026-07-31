#!/usr/bin/env python3
"""Verify complement-flip segment normal forms for two universal cycles."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-universal-cycle-flip-segment-results.json"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def support(value: int) -> set[int]:
    return {int(prime) for prime in sympy.factorint(value)}


def signed_cube(modulus: int, primes: list[int]) -> set[int]:
    residues = {1}
    for prime in primes:
        inverse = pow(prime, -1, modulus)
        residues |= {
            residue * multiplier % modulus
            for residue in tuple(residues)
            for multiplier in (prime, inverse)
        }
    return residues


def analyze_cycle(
    modulus: int,
    cycle: list[int],
    selected: list[int],
    labels: list[int],
) -> dict[str, object]:
    if not (len(cycle) == len(selected) == len(labels)):
        raise AssertionError("cycle data lengths disagreed")
    signs: list[int] = []
    for index, (node, coordinate, prime) in enumerate(
        zip(cycle, selected, labels)
    ):
        if node != min(coordinate, modulus - coordinate):
            raise AssertionError("selected coordinate was not in its node")
        if coordinate % (prime * prime):
            raise AssertionError("universal edge lacked q^2 divisibility")
        reduced = coordinate // prime
        next_selected = selected[(index + 1) % len(selected)]
        if next_selected == reduced:
            signs.append(1)
        elif next_selected == modulus - reduced:
            signs.append(-1)
        else:
            raise AssertionError("selected coordinates did not compose")

    flips = [index for index, sign in enumerate(signs) if sign == -1]
    if not flips or len(flips) % 2:
        raise AssertionError("complement-flip parity failed")
    if math.prod(labels) % modulus != 1 or math.prod(signs) != 1:
        raise AssertionError("strengthened cycle product law failed")

    start = (flips[-1] + 1) % len(cycle)
    order = [(start + offset) % len(cycle) for offset in range(len(cycle))]
    rotated_selected = [selected[index] for index in order]
    rotated_labels = [labels[index] for index in order]
    rotated_signs = [signs[index] for index in order]

    segments: list[dict[str, int | list[int]]] = []
    segment_start = 0
    product = 1
    segment_labels: list[int] = []
    for index, (prime, sign) in enumerate(zip(rotated_labels, rotated_signs)):
        product *= prime
        segment_labels.append(prime)
        if sign != -1:
            continue
        first = rotated_selected[segment_start]
        next_first = rotated_selected[(index + 1) % len(cycle)]
        quotient = modulus - next_first
        if first != product * quotient:
            raise AssertionError("flip segment identity failed")
        if math.prod(support(product)) and quotient % math.prod(support(product)):
            raise AssertionError("segment radical did not divide its final quotient")
        segments.append(
            {
                "start": first,
                "next_start": next_first,
                "labels": segment_labels,
                "product": product,
                "final_quotient": quotient,
            }
        )
        segment_start = index + 1
        product = 1
        segment_labels = []
    if product != 1 or segment_labels or len(segments) != len(flips):
        raise AssertionError("segment decomposition did not close")

    two_flip: dict[str, int] | None = None
    if len(segments) == 2:
        first, second = segments
        q_product = int(first["product"])
        t_product = int(second["product"])
        a_value = int(first["start"])
        b_value = int(second["start"])
        if (q_product * t_product - 1) % modulus:
            raise AssertionError("two-flip product did not define h")
        h_value = (q_product * t_product - 1) // modulus
        if h_value <= 0 or math.gcd(q_product, t_product) != 1:
            raise AssertionError("two-flip coprimality failed")
        expected = {
            "A": q_product * (t_product - 1) // h_value,
            "R_minus_A": (q_product - 1) // h_value,
            "B": t_product * (q_product - 1) // h_value,
            "R_minus_B": (t_product - 1) // h_value,
        }
        actual = {
            "A": a_value,
            "R_minus_A": modulus - a_value,
            "B": b_value,
            "R_minus_B": modulus - b_value,
        }
        if expected != actual:
            raise AssertionError("two-flip closed form failed")
        if (
            (t_product - 1) // h_value % math.prod(support(q_product))
            or (q_product - 1) // h_value % math.prod(support(t_product))
        ):
            raise AssertionError("two-flip cross divisibility failed")
        two_flip = {
            "Q": q_product,
            "T": t_product,
            "h": h_value,
            **actual,
        }

    return {
        "R": modulus,
        "cycle": cycle,
        "cycle_pairs": [[node, modulus - node] for node in cycle],
        "selected_coordinates": selected,
        "edge_labels": labels,
        "orientation_signs": signs,
        "flip_count": len(flips),
        "edge_product_mod_R": math.prod(labels) % modulus,
        "segments": segments,
        "two_flip_normal_form": two_flip,
    }


def selected_support_boundary() -> dict[str, object]:
    modulus = 55
    selected = [49, 48, 24, 12]
    cycle = [6, 7, 24, 12]
    selected_primes = sorted(set().union(*(support(value) for value in selected)))
    full_primes = sorted(
        set().union(
            *(
                support(node) | support(modulus - node)
                for node in cycle
            )
        )
    )
    if selected_primes != [2, 3, 7] or full_primes != [2, 3, 7, 31, 43]:
        raise AssertionError("the selected/full support boundary changed")
    selected_residues = signed_cube(modulus, selected_primes)
    selected_radical = math.prod(selected_primes)
    targets = {
        "minus_one": modulus - 1,
        "minus_four_radical": (-4 * selected_radical) % modulus,
        "minus_inverse_four_radical": (
            -pow(4 * selected_radical, -1, modulus)
        )
        % modulus,
    }
    if any(target in selected_residues for target in targets.values()):
        raise AssertionError("selected support unexpectedly hit a multiplier target")
    if len(selected_residues) != 24:
        raise AssertionError("the selected signed-cube size changed")
    numerator = 3
    denominator = 7 * 31
    if numerator * pow(denominator, -1, modulus) % modulus != modulus - 1:
        raise AssertionError("the full-support direct witness failed")
    if not (support(numerator) | support(denominator)) <= set(full_primes):
        raise AssertionError("the full-support witness left the cycle support")
    return {
        "R": modulus,
        "selected_support": selected_primes,
        "selected_signed_cube_size": len(selected_residues),
        "selected_support_targets": targets,
        "selected_support_hits_any_target": False,
        "full_support": full_primes,
        "full_support_direct_witness": {
            "numerator": numerator,
            "denominator": denominator,
        },
    }


def run() -> dict[str, object]:
    cycle_55 = analyze_cycle(
        55,
        [6, 7, 24, 12],
        [49, 48, 24, 12],
        [7, 2, 2, 2],
    )
    cycle_30031 = analyze_cycle(
        30_031,
        [31, 6_000, 1_200, 240, 961],
        [30_000, 6_000, 1_200, 29_791, 961],
        [5, 5, 5, 31, 31],
    )
    return {
        "arithmetic": (
            "Verify even positive complement-flip parity, the exact segment "
            "identity and radical divisibility, the two-flip closed form, and "
            "the necessity of using unselected complementary coordinates."
        ),
        "cycle_55": cycle_55,
        "cycle_30031": cycle_30031,
        "selected_support_boundary": selected_support_boundary(),
        "script_sha256": sha256(Path(__file__)),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run()
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "R55": result["cycle_55"]["two_flip_normal_form"],
                "R30031": result["cycle_30031"]["two_flip_normal_form"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
