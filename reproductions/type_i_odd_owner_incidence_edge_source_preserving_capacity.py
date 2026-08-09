#!/usr/bin/env python3
"""Verify source-preserving normalization and rank capacity of odd-owner edges."""

from __future__ import annotations

import argparse
from math import gcd

from type_i_core_jacobi_punctured_kernel_primary_selector import factorint
from type_i_odd_owner_fiber_incidence_lattice_source_map import (
    affine_pair,
    full_affine_lift,
    owner_window,
)
from type_i_odd_owner_scale_dichotomy_small_cofactor_terminal import divisors


def euler_phi(value: int) -> int:
    result = value
    for prime, _ in factorint(value):
        result = result // prime * (prime - 1)
    return result


def endpoint_unit_group_lift_status(
    q: int, moduli: tuple[int, ...]
) -> dict[str, object]:
    orders = tuple(euler_phi(modulus) for modulus in moduli)
    if all(order % q for order in orders):
        return {
            "status": "DIRECT_ENDPOINT_UNIT_GROUP_LIFT_OBSTRUCTED",
            "q": q,
            "moduli": moduli,
            "orders": orders,
        }
    return {
        "status": "DIRECT_ENDPOINT_UNIT_GROUP_LIFT_NOT_OBSTRUCTED_BY_ORDER",
        "q": q,
        "moduli": moduli,
        "orders": orders,
    }


def inversion_edge_receipt(
    *,
    p: int,
    q: int,
    j: int,
    phases: tuple[int, int],
    affine: tuple[int, int],
    source_fractions: tuple[tuple[int, int], tuple[int, int]],
    record_ids: tuple[tuple[int, int], tuple[int, int]],
) -> dict[str, object]:
    """Rebuild a named inversion edge and its normalized source column."""
    (u, v), reciprocal = source_fractions
    assert gcd(u, v) == 1
    assert reciprocal == (v, u)
    sigma = u + v
    endpoints = (sigma, sigma + q**j)

    data = owner_window(p, q, j)
    rows = data["rows"]
    assert isinstance(rows, list)
    by_s = {int(row["s"]): row for row in rows}
    assert all(endpoint in by_s for endpoint in endpoints)

    phase_left, phase_right = phases
    a, c = affine
    left = by_s[endpoints[0]]
    right = by_s[endpoints[1]]
    digit_left = int(left["digit"])
    digit_right = int(right["digit"])
    assert phase_left != phase_right
    assert a % q
    assert digit_left == (a * phase_left + c) % q
    assert digit_right == (a * phase_right + c) % q

    phase_scalar = a * (phase_left - phase_right) % q
    theta = digit_left - digit_right
    theta %= q
    assert theta == phase_scalar and theta

    cofactor_delta = int(left["cofactor"]) - int(right["cofactor"])
    cofactor_theta = pow(4, -1, q) * cofactor_delta % q
    assert cofactor_theta == theta

    normalized_column = theta * pow(phase_scalar, -1, q) % q
    integer_normalized_column = (
        cofactor_delta * pow(4 * phase_scalar, -1, q)
    ) % q
    assert normalized_column == integer_normalized_column == 1

    signature = (
        j,
        record_ids,
        source_fractions,
        "inversion_sum_plus_qj",
        endpoints,
        phase_scalar,
        normalized_column,
    )
    return {
        "status": "QUALIFIED_INCIDENCE_EDGE",
        "p": p,
        "q": q,
        "j": j,
        "record_ids": record_ids,
        "source_fractions": source_fractions,
        "lift_rule": "inversion_sum_plus_qj",
        "source_relation_scope": "one_edge",
        "sigma": sigma,
        "endpoints": endpoints,
        "vertices": (
            (int(left["D"]), int(left["A"]), int(left["C"])),
            (int(right["D"]), int(right["A"]), int(right["C"])),
        ),
        "heights": (int(left["height"]), int(right["height"])),
        "cofactors": (int(left["cofactor"]), int(right["cofactor"])),
        "phases": phases,
        "affine": affine,
        "phase_scalar": phase_scalar,
        "theta": theta,
        "cofactor_delta_mod_q": cofactor_delta % q,
        "normalized_column": normalized_column,
        "signature": signature,
    }


def transverse_dispatch(
    *,
    incidence_rank: int,
    qualified_edges: list[dict[str, object]],
    independent_requests: int,
) -> dict[str, object]:
    if incidence_rank == 0:
        return {"status": "OWNER_WINDOW_RANK_DEFICIT", "rank": 0}
    assert incidence_rank == 1
    if not qualified_edges:
        return {
            "status": "INCIDENCE_EDGE_SOURCE_PROVENANCE_OBSTRUCTED",
            "rank": 1,
        }

    assert independent_requests >= 1
    assert all(edge["normalized_column"] == 1 for edge in qualified_edges)
    canonical = min(qualified_edges, key=lambda edge: repr(edge["signature"]))
    source_rank = 1
    if independent_requests > source_rank:
        return {
            "status": "OWNER_TRANSVERSE_SOURCE_RANK_DEFICIT",
            "requests": independent_requests,
            "rank": source_rank,
            "canonical_signature": canonical["signature"],
        }

    signatures = {canonical["signature"]}
    assert len(signatures) == 1
    return {
        "status": "TRANSVERSE_INCIDENCE_CANONICAL_RESOURCE_CERT",
        "resource_class": "additive_incidence_source",
        "token_flow": 1,
        "slot_flow": 1,
        "source_rank": source_rank,
        "fiber_uniform": True,
        "physical_owner_projection": "unproved",
        "canonical_signature": canonical["signature"],
    }


def type_ii_terminal_menu(p: int, row: dict[str, int]) -> tuple[int, ...]:
    modulus = 4 * int(row["D"])
    return tuple(
        h for h in divisors(p + 4 * int(row["s"])) if h % modulus == modulus - 1
    )


def verify() -> None:
    p97_q11 = owner_window(97, 11, 1)
    rows_11 = p97_q11["rows"]
    assert isinstance(rows_11, list)
    assert [row["s"] for row in rows_11] == [6, 17]
    assert affine_pair(2, 9, 0, 1, 11) == (8, 6)

    edge = inversion_edge_receipt(
        p=97,
        q=11,
        j=1,
        phases=(2, 9),
        affine=(8, 6),
        source_fractions=((5, 1), (1, 5)),
        record_ids=((1, 0), (-1, 0)),
    )
    assert edge["sigma"] == 6
    assert edge["endpoints"] == (6, 17)
    assert edge["vertices"] == ((6, 1, 6), (17, 1, 17))
    assert edge["heights"] == (2, 1)
    assert edge["cofactors"] == (11, 15)
    assert edge["phase_scalar"] == edge["theta"] == 10
    assert edge["cofactor_delta_mod_q"] == 7
    assert edge["normalized_column"] == 1

    one_request = transverse_dispatch(
        incidence_rank=int(p97_q11["rank"]),
        qualified_edges=[edge],
        independent_requests=1,
    )
    assert one_request == {
        "status": "TRANSVERSE_INCIDENCE_CANONICAL_RESOURCE_CERT",
        "resource_class": "additive_incidence_source",
        "token_flow": 1,
        "slot_flow": 1,
        "source_rank": 1,
        "fiber_uniform": True,
        "physical_owner_projection": "unproved",
        "canonical_signature": edge["signature"],
    }

    two_requests = transverse_dispatch(
        incidence_rank=int(p97_q11["rank"]),
        qualified_edges=[edge],
        independent_requests=2,
    )
    assert two_requests["status"] == "OWNER_TRANSVERSE_SOURCE_RANK_DEFICIT"
    assert (two_requests["requests"], two_requests["rank"]) == (2, 1)

    by_s_11 = {int(row["s"]): row for row in rows_11}
    assert type_ii_terminal_menu(97, by_s_11[6]) == ()
    assert type_ii_terminal_menu(97, by_s_11[17]) == ()
    endpoint_no_go = endpoint_unit_group_lift_status(11, (24, 68, 408))
    assert endpoint_no_go == {
        "status": "DIRECT_ENDPOINT_UNIT_GROUP_LIFT_OBSTRUCTED",
        "q": 11,
        "moduli": (24, 68, 408),
        "orders": (8, 32, 128),
    }

    p97_q3 = owner_window(97, 3, 1)
    assert p97_q3["full_digit_coverage"]
    assert full_affine_lift([0, 1, 2], p97_q3, 1, 0) == {
        0: 2,
        1: 5,
        2: 8,
    }
    phase_only = transverse_dispatch(
        incidence_rank=int(p97_q3["rank"]),
        qualified_edges=[],
        independent_requests=1,
    )
    assert phase_only == {
        "status": "INCIDENCE_EDGE_SOURCE_PROVENANCE_OBSTRUCTED",
        "rank": 1,
    }

    p73_q17 = owner_window(73, 17, 1)
    rank_zero = transverse_dispatch(
        incidence_rank=int(p73_q17["rank"]),
        qualified_edges=[],
        independent_requests=1,
    )
    assert rank_zero == {"status": "OWNER_WINDOW_RANK_DEFICIT", "rank": 0}

    print("verified odd-owner incidence-edge source-preserving capacity")
    print(
        "p97_q11",
        "edge=(6,17)",
        "normalized_column=1",
        "one_request=incidence_flow_rado_pass",
        "physical_owner_projection=unproved_external_contract_required",
    )
    print(
        "p97_q11_endpoint_groups",
        "orders=(8,32,128)",
        "direct_unit_group_11_lift=obstructed",
    )
    print("p97_q11_overload", "requests=2", "source_rank=1", "strict_deficit")
    print("p97_q3", "full_phase_lift", "source_provenance=obstructed")
    print("p73_q17", "singleton_owner", "transverse_rank=0")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
