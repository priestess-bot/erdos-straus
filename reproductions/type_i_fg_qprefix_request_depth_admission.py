#!/usr/bin/env python3
"""Focused checks for F/G q-prefix request-depth admission."""

from __future__ import annotations

import argparse
import json
from itertools import product
from math import gcd, isqrt


def is_prime(value: int) -> bool:
    return value > 1 and all(value % divisor for divisor in range(2, isqrt(value) + 1))


def valuation(value: int, prime: int) -> int:
    if value == 0:
        raise AssertionError("valuation control requires a nonzero integer")
    value = abs(value)
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def jacobi_symbol(value: int, modulus: int) -> int:
    if modulus <= 0 or modulus % 2 == 0:
        raise AssertionError("Jacobi modulus must be positive and odd")
    value %= modulus
    result = 1
    while value:
        while value % 2 == 0:
            value //= 2
            if modulus % 8 in (3, 5):
                result = -result
        value, modulus = modulus, value
        if value % 4 == modulus % 4 == 3:
            result = -result
        value %= modulus
    return result if modulus == 1 else 0


def divisors(value: int) -> tuple[int, ...]:
    low: list[int] = []
    high: list[int] = []
    for divisor in range(1, isqrt(value) + 1):
        if value % divisor:
            continue
        low.append(divisor)
        if divisor * divisor != value:
            high.append(value // divisor)
    return tuple(low + list(reversed(high)))


def dot(left: tuple[int, ...], right: tuple[int, ...], q: int) -> int:
    return sum(a * b for a, b in zip(left, right)) % q


def role_span(
    basis: tuple[tuple[int, ...], ...], q: int
) -> tuple[tuple[int, ...], ...]:
    dimension = len(basis[0])
    vectors = {
        tuple(
            sum(coefficient * basis[row][column] for row, coefficient in enumerate(coefficients))
            % q
            for column in range(dimension)
        )
        for coefficients in product(range(q), repeat=len(basis))
    }
    return tuple(sorted(vectors))


def evaluation_image(
    role_basis: tuple[tuple[int, ...], ...],
    edges: tuple[tuple[int, ...], ...],
    q: int,
) -> tuple[tuple[int, ...], ...]:
    return tuple(
        sorted(
            {
                tuple(dot(role, edge, q) for edge in edges)
                for role in role_span(role_basis, q)
            }
        )
    )


def verify_single_f_request_and_depth() -> dict[str, object]:
    # Actual p=73 F-state: U(27)=<2> has order 18 and K=17*29.
    f_prime, modulus, q = 73, 27, 3
    assert is_prime(f_prime) and f_prime % 24 == 1
    K = (f_prime * modulus + 1) // 4
    assert K == 493 == 17 * 29
    assert pow(2, 15, modulus) == 17
    assert pow(2, 1, modulus) == 29 % modulus
    target_log = 9
    assert pow(2, target_log, modulus) == modulus - 1

    exponent_box = tuple(product(range(-1, 2), repeat=2))
    source_logs = {
        (15 * left + right) % 18 for left, right in exponent_box
    }
    source_support = {pow(2, source_log, modulus) for source_log in source_logs}
    assert source_logs == {0, 1, 2, 3, 4, 14, 15, 16, 17}
    assert source_support == {1, 2, 4, 7, 8, 14, 16, 17, 22}
    assert target_log not in source_logs

    # Repository CRT coordinates use u -> 2u mod 9.  This differs from the
    # zeta_9 exponent coordinate by the common unit 2.
    target_q_phase = 2 * target_log % 9
    edge_evaluation = 2 * (0 - 1) % q
    assert target_q_phase == 0
    assert edge_evaluation == 1

    sorted_logs = tuple(sorted(source_logs))
    unordered_pairs = tuple(
        (left, right)
        for index, left in enumerate(sorted_logs)
        for right in sorted_logs[index + 1 :]
    )
    nonzero_pair_edges = sum(
        2 * (right - left) % q != 0 for left, right in unordered_pairs
    )
    assert len(unordered_pairs) == 36
    assert nonzero_pair_edges == 27

    request_ids = ("F-p73-R27-q3-role",)
    source_menu = ((1, 0), (2, 1), (3, 2))
    assert all(
        2 * (destination - source) % q == edge_evaluation
        for source, destination in source_menu
    )
    assert len(request_ids) == 1
    assert len(source_menu) == 3

    # A separate arithmetic carrier control: it is not a realization of p=73 above.
    p, layer, depth = 557_281, 1, 2
    assert is_prime(p) and p % 24 == 1
    target_owner = 182
    deep_source, shallow_source = 19_838, 138_866
    heights = (
        valuation(p + 4 * target_owner, q),
        valuation(p + 4 * deep_source, q),
        valuation(p + 4 * shallow_source, q),
    )
    assert heights == (4, 3, 1)
    difference = shallow_source - deep_source
    assert valuation(difference, q) == layer
    assert difference // q**layer % q == edge_evaluation
    assert target_owner % q ** (layer + depth) == (
        -p * pow(4, -1, q ** (layer + depth))
    ) % q ** (layer + depth)

    cyclotomic_prime = 13
    prefix = tuple(q**exponent for exponent in range(depth + 1))
    quotient_image = {
        pow(value, (cyclotomic_prime - 1) // q, cyclotomic_prime)
        for value in prefix
    }
    assert prefix == (1, 3, 9)
    assert quotient_image == {1, 3, 9}

    return {
        "actual_f_control": {
            "p": f_prime,
            "R": modulus,
            "K": K,
            "source_logs": sorted_logs,
            "source_support": tuple(sorted(source_support)),
            "target_log": target_log,
            "target_q_phase": target_q_phase,
            "q_primary_coordinate": "REPOSITORY_CRT_UNIT_2_NORMALIZATION",
            "source_edge_evaluation": edge_evaluation,
            "sample_actual_source_edges": source_menu,
            "nonzero_unordered_pair_edges": nonzero_pair_edges,
            "request_count": len(request_ids),
            "menu_columns": len(source_menu),
            "singleton_request_role_rank": 1,
            "global_role_rank_not_asserted": True,
        },
        "arithmetic_depth_control": {
            "p": p,
            "q": q,
            "layer": layer,
            "depth": depth,
            "q_heights": heights,
            "prefix": prefix,
            "request_count": 1,
            "q_prefix_lineages": 1,
            "singleton_request_role_rank": 1,
            "global_role_rank_not_asserted": True,
            "typed_realization": "conditional",
            "same_fiber_as_actual_f_control": False,
        },
    }


def verify_joint_role_gate() -> dict[str, object]:
    q = 3

    positive_basis = ((1, 1),)
    positive_edges = ((1, 0), (0, 1))
    positive_target = (1, 1)
    positive_image = evaluation_image(positive_basis, positive_edges, q)
    assert positive_image == ((0, 0), (1, 1), (2, 2))
    assert positive_target in positive_image
    positive_request_roles = ((1, 1), (1, 1))
    assert len(set(positive_request_roles)) == 1

    negative_basis = ((1,),)
    negative_edges = ((1,), (1,))
    negative_target = (1, 2)
    negative_image = evaluation_image(negative_basis, negative_edges, q)
    assert negative_image == ((0, 0), (1, 1), (2, 2))
    assert negative_target not in negative_image
    assert all(
        any(dot(role, edge, q) == desired for role in role_span(negative_basis, q))
        for edge, desired in zip(negative_edges, negative_target)
    )

    annihilator_witness = (1, 2)
    combined_edge = tuple(
        sum(
            annihilator_witness[index] * negative_edges[index][coordinate]
            for index in range(2)
        )
        % q
        for coordinate in range(1)
    )
    target_pairing = dot(annihilator_witness, negative_target, q)
    assert combined_edge == (0,)
    assert target_pairing != 0

    independent_request_roles = ((1, 0), (0, 1))
    line_mismatch_edges = ((1, 0), (0, 1))
    large_role_image = evaluation_image(
        independent_request_roles, line_mismatch_edges, q
    )
    assert (1, 1) in large_role_image
    assert all(
        tuple(unit * value % q for value in independent_request_roles[0])
        != independent_request_roles[1]
        for unit in range(1, q)
    )

    mapped_difference = 5 * q**4
    scalar_units = (1, 2)
    scalar_heights = tuple(
        valuation(unit * mapped_difference, q) for unit in scalar_units
    )
    assert scalar_heights == (4, 4)
    assert scalar_heights != (4, 5)

    return {
        "positive": {
            "distinct_request_ids": 2,
            "request_subsystem_role_rank": 1,
            "desired_vector": positive_target,
            "joint_role_admitted": True,
            "common_role_line_cert": True,
        },
        "strict_counterexample": {
            "individual_edges_admitted": True,
            "joint_role_admitted": False,
            "annihilator_relation": annihilator_witness,
            "annihilator_target_pairing": target_pairing,
            "branch": "FG_STAIRCASE_JOINT_ROLE_OBSTRUCTED",
        },
        "role_line_mismatch": {
            "joint_image_test_in_large_role_space": True,
            "original_request_role_rank": 2,
            "common_role_line_cert": False,
            "branch": "FG_STAIRCASE_ROLE_LINE_MISMATCH",
        },
        "scalar_copy_no_go": {
            "q_unit_scalars": scalar_units,
            "q_heights": scalar_heights,
            "branch": "FG_STAIRCASE_FILTERED_STAR_OBSTRUCTED",
        },
    }


def verify_target_odd_affine_boundary() -> dict[str, object]:
    p, q, exponent = 73, 3, 2
    target_log = 9
    gamma = 2 * target_log % q**exponent
    owner_center = (-p * pow(4, -1, q**exponent)) % q**exponent
    assert gamma == 0
    assert owner_center == 2
    assert gamma != owner_center
    return {
        "p": p,
        "q": q,
        "exponent": exponent,
        "target_phase": gamma,
        "owner_center": owner_center,
        "branch": "TARGET_ODD_QPREFIX_DIRECT_OWNER_CONFLICT",
        "required_repair": "NONZERO_AFFINE_OFFSET_OR_OTHER_SOURCE_RELATION",
    }


def verify_g_jacobi_zero_capacity() -> dict[str, object]:
    p = 5_281
    R = p - 2
    K = (p - 1) ** 2 // 4
    Q = (p - 3) // 2
    assert (R, K, Q) == (5_279, 6_969_600, 2_639)
    assert is_prime(p) and is_prime(R) and p % 24 == 1
    assert jacobi_symbol(K, R) == 1

    negative_menu = tuple(
        delta for delta in divisors(Q) if jacobi_symbol(delta, R) == -1
    )
    assert negative_menu == (7, 91, 203, 2_639)

    theta: dict[int, int] = {}
    for delta in negative_menu:
        x = 2 * Q // delta
        y = R - x
        C = gcd(y, K)
        M = K // C
        tail = y // C
        assert gcd(tail, R) == 1
        theta_delta = M * pow(tail, -1, R) % R
        assert theta_delta == K * delta % R
        assert jacobi_symbol(theta_delta, R) == -1
        theta[delta] = theta_delta
    assert theta == {7: 3_961, 91: 3_982, 203: 4_010, 2_639: 4_619}

    pair_evaluations: list[int] = []
    for left in negative_menu:
        for right in negative_menu:
            ratio = theta[left] * pow(theta[right], -1, R) % R
            pair_evaluations.append(jacobi_symbol(ratio, R))
    assert set(pair_evaluations) == {1}

    raw_edges = ((7, 13, 91), (7, 29, 203), (91, 29, 2_639), (203, 13, 2_639))
    for source, label, destination in raw_edges:
        assert source * label == destination
        assert source in negative_menu and destination in negative_menu
        assert jacobi_symbol(label, R) == 1
        ratio = theta[destination] * pow(theta[source], -1, R) % R
        assert ratio == label % R
        assert jacobi_symbol(ratio, R) == 1

    q = 3
    required_nonzero_values = q - 1
    actual_nonzero_values = sum(value == -1 for value in pair_evaluations)
    assert len(raw_edges) >= required_nonzero_values
    assert actual_nonzero_values == 0

    # Scope guards: the anchor and alternative odd roles are outside this zero claim.
    theta_anchor = K % R
    assert jacobi_symbol(theta_anchor, R) == 1
    anchor_to_negative = theta[7] * pow(theta_anchor, -1, R) % R
    assert anchor_to_negative == 7
    assert jacobi_symbol(anchor_to_negative, R) == -1
    assert pow(13, (R - 1) // 7, R) != 1

    return {
        "p": p,
        "R": R,
        "K": K,
        "Q": Q,
        "negative_menu": negative_menu,
        "theta": theta,
        "menu_internal_raw_edges": len(raw_edges),
        "naive_q3_edge_threshold": required_nonzero_values,
        "negative_endpoint_internal_jacobi_evaluation_rank": 0,
        "canonical_role_order": 2,
        "odd_primary_components": (),
        "canonical_jacobi_role_supplied_odd_q_request_count": 0,
        "branch": "G_JACOBI_NEGATIVE_ENDPOINT_MENU_ODD_QPREFIX_INGRESS_ZERO",
        "scope": "declared_negative_coset_and_internal_divisor_factor_edges",
        "anchor_inclusive_c2_rank_is_nonzero": True,
        "alternative_odd_role_exists": True,
    }


def verify() -> None:
    receipt = {
        "status": "PASS",
        "single_f_request_and_depth": verify_single_f_request_and_depth(),
        "joint_role_gate": verify_joint_role_gate(),
        "target_odd_affine_boundary": verify_target_odd_affine_boundary(),
        "g_jacobi_zero_capacity": verify_g_jacobi_zero_capacity(),
    }
    print(json.dumps(receipt, ensure_ascii=True, sort_keys=True))


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
