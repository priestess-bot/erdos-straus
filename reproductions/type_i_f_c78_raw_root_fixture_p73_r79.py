#!/usr/bin/env python3
"""Verify the minimal p=73, R=79 F/C78 raw-root control fixture.

This is a terminal-preempted local control.  It certifies a finite F box,
an exact C78 fixed-layer Fourier profile, one actual universal raw p-edge,
and an already available Type II leaf.  It deliberately does not construct a
row-to-anchor map, a common affine law, a carry/E2 contract, a solution lift,
or a recursive selector edge.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import product
from math import gcd, isqrt


P = 73
R = 79
K = 1_442
SUPPORT = (2, 7, 103)
TARGET = R - 1
CYCLIC_GENERATOR = 3


def is_prime(value: int) -> bool:
    """Return whether one small positive integer is prime."""
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def factorization(value: int) -> dict[int, int]:
    """Factor a positive control integer by trial division."""
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[value] = 1
    return factors


def valuation(value: int, prime: int) -> int:
    """Return v_prime(value) for a positive control integer."""
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def euler_phi(value: int) -> int:
    """Compute Euler's phi function from the exact factorization."""
    result = value
    for prime in factorization(value):
        result = result // prime * (prime - 1)
    return result


def generated_subgroup(generators: set[int], modulus: int) -> set[int]:
    """Build a finite multiplicative subgroup without using a log oracle."""
    subgroup = {1}
    generators = {value % modulus for value in generators}
    if any(gcd(value, modulus) != 1 for value in generators):
        raise AssertionError("nonunit generator in the F fixture")
    changed = True
    while changed:
        changed = False
        expanded = {
            left * right % modulus
            for left in subgroup
            for right in subgroup | generators
        }
        if not expanded <= subgroup:
            subgroup |= expanded
            changed = True
    return subgroup


def cyclic_log_table(generator: int, modulus: int) -> dict[int, int]:
    """Return the exact coordinate table after proving generator order R-1."""
    table: dict[int, int] = {}
    value = 1
    for exponent in range(modulus - 1):
        if value in table:
            raise AssertionError("claimed C78 generator repeated too early")
        table[value] = exponent
        value = value * generator % modulus
    if value != 1 or len(table) != modulus - 1:
        raise AssertionError("claimed C78 generator did not have full order")
    return table


def residue(exponents: tuple[int, int, int]) -> int:
    """Evaluate a signed support exponent vector modulo R."""
    value = 1
    for prime, exponent in zip(SUPPORT, exponents, strict=True):
        if exponent >= 0:
            value = value * pow(prime, exponent, R) % R
        else:
            value = value * pow(pow(prime, -1, R), -exponent, R) % R
    return value


def fixed_layer() -> set[int]:
    """Return the centered 2,7 layer used before the residual 103 block."""
    return {
        pow(2, left, R) * pow(7, right, R) % R
        for left, right in product(range(-1, 2), repeat=2)
    }


def verify_minimality() -> dict[str, object]:
    """Verify the two elementary lower bounds behind the word 'minimal'."""
    lower_core_primes = [
        value for value in range(2, P) if value % 24 == 1 and is_prime(value)
    ]
    if lower_core_primes:
        raise AssertionError("p=73 was not the first core prime")
    if not (is_prime(P) and P % 24 == 1 and P < R and R % 4 == 3):
        raise AssertionError("fixture left the stated core/high-R domain")
    if euler_phi(R) != 78:
        raise AssertionError("R=79 lost its C78 unit group")

    # A quotient isomorphic to C78 has at least 78 elements.  For 1 < r < 79,
    # phi(r) <= r-1 < 78, so no smaller R can meet the C78 requirement.
    if not all(euler_phi(value) < 78 for value in range(2, R)):
        raise AssertionError("the elementary C78 lower bound changed")
    return {
        "scope": "p == 1 mod 24, p < R, R == 3 mod 4, stabilizer quotient C78",
        "smallest_core_prime": P,
        "smallest_possible_modulus_for_C78": R,
    }


def verify_f_c78_profile() -> dict[str, object]:
    """Check the F miss, trivial stabilizer, target-odd Fourier data, and C3 map."""
    if 4 * K != P * R + 1 or factorization(K) != {2: 1, 7: 1, 103: 1}:
        raise AssertionError("fixture determinant or support changed")

    units = set(range(1, R))
    subgroup = generated_subgroup(set(SUPPORT), R)
    if subgroup != units:
        raise AssertionError("support no longer generates the whole unit group")
    logs = cyclic_log_table(CYCLIC_GENERATOR, R)
    support_coordinates = [logs[prime % R] for prime in SUPPORT]
    if support_coordinates != [4, 53, 13] or logs[TARGET] != 39:
        raise AssertionError("C78 support or target coordinates changed")

    J = fixed_layer()
    if len(J) != 9 or J != {1, 2, 7, 14, 17, 34, 40, 43, 68}:
        raise AssertionError("fixed J layer changed")
    stabilizer = {
        value
        for value in subgroup
        if {value * member % R for member in J} == J
    }
    if stabilizer != {1}:
        raise AssertionError("J retained a nontrivial stabilizer")

    box = list(product(range(-1, 2), repeat=3))
    target_vectors = [vector for vector in box if residue(vector) == TARGET]
    if target_vectors:
        raise AssertionError("the finite F box unexpectedly reached -1")

    # This is the repository's usual minimum-L1, then lexicographic policy.
    short_ball = [
        vector
        for vector in product(range(-3, 4), repeat=3)
        if sum(abs(entry) for entry in vector) <= 3 and residue(vector) == TARGET
    ]
    canonical_witness = min(short_ball, key=lambda vector: (sum(map(abs, vector)), vector))
    if canonical_witness != (0, 0, -3):
        raise AssertionError("canonical unrestricted F witness changed")
    if any(sum(abs(entry) for entry in vector) < 3 for vector in short_ball):
        raise AssertionError("a shorter unrestricted target witness appeared")

    coefficient_vector = [0] * 78
    for vector in box:
        coordinate = logs[residue(vector)]
        expected_coordinate = sum(
            exponent * coordinate
            for exponent, coordinate in zip(vector, support_coordinates, strict=True)
        ) % 78
        if coordinate != expected_coordinate:
            raise AssertionError("signed support coordinate did not agree with its residue")
        coefficient_vector[coordinate] += 1
    if (
        sum(coefficient_vector) != 27
        or coefficient_vector[39] != 0
        or any(count not in (0, 1) for count in coefficient_vector)
    ):
        raise AssertionError("C78 coefficient vector changed")

    autocorrelation = [
        sum(
            coefficient_vector[position]
            * coefficient_vector[(position - shift) % 78]
            for position in range(78)
        )
        for shift in range(78)
    ]
    if autocorrelation[0] != 27 or autocorrelation[39] != 0:
        raise AssertionError("target-involution autocorrelation changed")
    target_odd_energy = 78 * (autocorrelation[0] - autocorrelation[39]) // 2
    if target_odd_energy != 1_053:
        raise AssertionError("target-odd C78 energy changed")

    # chi_1(3)=zeta_78 is target-odd because chi_1(-1)=zeta_78^39=-1.
    # Its product coefficient is D_1(zeta^4) D_1(zeta^53) D_1(zeta^13).
    # For a root of unity w, D_1(w)=w^-1+1+w vanishes exactly at order 3.
    chi_one_factor_orders = [78 // gcd(78, coordinate) for coordinate in support_coordinates]
    if chi_one_factor_orders != [39, 78, 6] or 3 in chi_one_factor_orders:
        raise AssertionError("chi_1 nonvanishing factor test changed")
    if 39 % 2 != 1:
        raise AssertionError("chi_1 ceased to be target-odd")

    # For chi_1 of order 78, project a coordinate a to its 3-primary phase by
    # (78 / 3) * a modulo 3.  The involutive target collapses to zero, while
    # the residual 103 coordinate remains 2 mod 3.
    target_coordinate = logs[TARGET]
    residual_coordinate = logs[103 % R]
    target_primary = (78 // 3 * target_coordinate) % 3
    residual_primary = (78 // 3 * residual_coordinate) % 3
    if (target_coordinate, residual_coordinate) != (39, 13):
        raise AssertionError("target or residual cyclic coordinate changed")
    if (target_primary, residual_primary) != (0, 2):
        raise AssertionError("C3 target/residual phase coordinates changed")

    return {
        "state_class": "F",
        "support": list(SUPPORT),
        "finite_box": "[-1,1]^3",
        "finite_box_target_count": len(target_vectors),
        "canonical_unrestricted_witness": list(canonical_witness),
        "canonical_witness_policy": "minimum_l1_then_lexicographic",
        "H_order": len(subgroup),
        "cyclic_generator": CYCLIC_GENERATOR,
        "support_coordinates": support_coordinates,
        "target_coordinate": target_coordinate,
        "J": sorted(J),
        "J_stabilizer": sorted(stabilizer),
        "stabilizer_quotient": "C78",
        "residual_prime": 103,
        "residual_coordinate": residual_coordinate,
        "target_odd_chi_1": {
            "character_order": 78,
            "nonzero": True,
            "dirichlet_factor_orders": chi_one_factor_orders,
        },
        "target_odd_energy": target_odd_energy,
        "autocorrelation": {"C_identity": autocorrelation[0], "C_target": autocorrelation[39]},
        "three_primary_phase_coordinates": {
            "target_mod_3": target_primary,
            "residual_103_mod_3": residual_primary,
        },
    }


def verify_universal_raw_source() -> dict[str, object]:
    """Replay the actual p-labelled universal source edge in this same chart."""
    source = (P, R * (P - 1) - P, P - 1)
    if source != (73, 5_615, 72):
        raise AssertionError("universal raw source changed")
    selected, other, layer = source
    if selected + other != R * layer or gcd(selected, other) != 1:
        raise AssertionError("universal source is not a primitive raw node")
    if valuation(selected, P) <= valuation(K, P):
        raise AssertionError("p did not exceed the K capacity at the source")
    if gcd(P, R * layer * other) != 1:
        raise AssertionError("p-labelled raw source unit condition failed")

    shift = (-layer) % P
    if shift != 1:
        raise AssertionError("universal p-edge shift changed")
    pre_reduction = (selected // P, (other + R * shift) // P, (layer + shift) // P)
    if P * pre_reduction[1] != other + R * shift or P * pre_reduction[2] != layer + shift:
        raise AssertionError("universal p-edge division failed")
    common = gcd(pre_reduction[0], pre_reduction[1])
    if pre_reduction[2] % common:
        raise AssertionError("raw p-edge gcd reduction did not divide the layer")
    destination = tuple(value // common for value in pre_reduction)
    if common != 1 or destination != (1, 78, 1):
        raise AssertionError("universal raw p-edge destination changed")

    source_phase = (-pow(source[0], -1, R)) % R
    destination_phase = (-pow(destination[0], -1, R)) % R
    if (source_phase, destination_phase) != (66, 78):
        raise AssertionError("normalized lineage phases changed")
    if destination_phase * pow(source_phase, -1, R) % R != P:
        raise AssertionError("raw p-edge lost its normalized phase ratio")

    # With the fixed J used by this F/C78 fixture, an assignment
    # Phi = theta * j^-1 along this one edge would force j_source in P * J.
    # The empty intersection rules out that canonical assignment for every
    # fixed theta; it does not rule out another fixed layer or chart.
    J = fixed_layer()
    scaled_layer = {P * member % R for member in J}
    if J & scaled_layer:
        raise AssertionError("the fixed-layer raw-to-anchor obstruction disappeared")
    return {
        "source": list(source),
        "q": P,
        "shift": shift,
        "gcd_reduction": common,
        "destination": list(destination),
        "actual_raw_edge": True,
        "normalized_lineage_phases": {
            "source": source_phase,
            "destination": destination_phase,
            "ratio": P,
        },
        "fixed_layer_anchor_assignment": {
            "J_intersect_qJ": sorted(J & scaled_layer),
            "status": "OBSTRUCTED_FOR_THIS_FIXED_J",
        },
    }


def verify_terminal_type_ii_leaf() -> dict[str, object]:
    """Check the preempting p=73 Type II unit-fraction identity exactly."""
    A, B, C, kappa = 2, 5, 2, 1
    gap = (A + B) // kappa
    denominator_product = A * B * C
    denominators = [
        denominator_product,
        P * A * C * kappa,
        P * B * C * kappa,
    ]
    divisor = A * A * C
    if (
        gap != 7
        or P != 4 * A * B * C - gap
        or denominators != [20, 292, 730]
        or divisor != 8
        or denominator_product * denominator_product % divisor
        or divisor > denominator_product
        or (denominator_product + divisor) % gap
    ):
        raise AssertionError("p=73 Type II normal form changed")
    if sum((Fraction(1, denominator) for denominator in denominators), Fraction()) != Fraction(4, P):
        raise AssertionError("p=73 Type II leaf no longer proves the unit-fraction identity")
    return {
        "type": "II",
        "normal_form": {"A": A, "B": B, "C": C, "kappa": kappa, "gap": gap},
        "denominators": denominators,
        "terminal_preempted": True,
    }


def build_receipt() -> dict[str, object]:
    """Build the entire local control receipt without creating a selector edge."""
    return {
        "certificate_type": "F_C78_raw_root_terminal_preempted_fixture_v1",
        "scope": (
            "One minimal F/C78 control with an actual universal raw source edge and "
            "an already-terminal Type II leaf; it is not a recursive edge or a descent."
        ),
        "minimality": verify_minimality(),
        "f_c78_profile": verify_f_c78_profile(),
        "raw_source": verify_universal_raw_source(),
        "terminal_leaf": verify_terminal_type_ii_leaf(),
        "selector_dispatch": "direct_Type_II_terminal",
        "unclosed_interfaces": [
            "row_to_anchor_map",
            "common_affine_law",
            "carry_contract",
            "E2",
            "solution_lift",
        ],
        "recursive_edge_eligible": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    build_receipt()
    if args.verify:
        print("verified p=73 R=79 F/C78 terminal-preempted raw-root fixture")


if __name__ == "__main__":
    main()
