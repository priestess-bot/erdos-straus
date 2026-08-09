#!/usr/bin/env python3
"""Verify the adjacent odd-owner fixed-base terminal/obstruction trichotomy."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd

from type_i_core_jacobi_punctured_kernel_primary_selector import factorint
from type_i_odd_owner_fiber_incidence_lattice_source_map import owner_window
from type_i_odd_owner_incidence_edge_source_preserving_capacity import (
    inversion_edge_receipt,
)
from type_i_odd_owner_scale_dichotomy_small_cofactor_terminal import divisors


def euler_phi(value: int) -> int:
    result = value
    for prime, _ in factorint(value):
        result = result // prime * (prime - 1)
    return result


def adjacent_fixed_base_arithmetic(
    *, p: int, q: int, j: int, left_index: int = 0
) -> dict[str, object]:
    """Compute the unique common-base arithmetic menu for adjacent owners."""
    data = owner_window(p, q, j)
    rows = data["rows"]
    assert isinstance(rows, list)
    assert 0 <= left_index < len(rows) - 1

    left = rows[left_index]
    right = rows[left_index + 1]
    power = q**j
    endpoints = (int(left["s"]), int(right["s"]))
    assert endpoints[1] - endpoints[0] == power
    assert endpoints[0] % q
    assert gcd(*endpoints) == gcd(endpoints[0], power) == 1
    assert all((p + 4 * endpoint) % power == 0 for endpoint in endpoints)

    common_source_bases = tuple(divisors(gcd(*endpoints)))
    assert common_source_bases == (1,)
    only_target = (1, 1, 1)  # (D_star, A, x=A*D_star)
    beta = int(data["beta"])
    source_crt_pass = all((only_target[2] - endpoint) % power == 0 for endpoint in endpoints)
    assert source_crt_pass == (beta == 1) == ((p + 4) % power == 0)

    common = {
        "p": p,
        "q": q,
        "j": j,
        "power": power,
        "beta": beta,
        "endpoints": endpoints,
        "endpoint_gcd": gcd(*endpoints),
        "common_source_bases": common_source_bases,
        "only_target": only_target,
    }
    if not source_crt_pass:
        return {
            **common,
            "status": "ADJACENT_EDGE_FIXED_BASE_QJ_SOURCE_CRT_OBSTRUCTED",
            "required_residue": beta,
            "target_residue": 1,
            "failed_gate": "E2_SOURCE_CRT",
        }

    target_modulus = 4
    target_group_order = euler_phi(target_modulus)
    assert target_group_order == 2 and target_group_order % q
    return {
        **common,
        "status": "ADJACENT_EDGE_FIXED_BASE_QJ_PHYSICAL_OCCURRENCE",
        "physical_occurrence": (q, j, power, p + 4),
        "e2_source_crt": "pass",
        "e3_range": "pass",
        "target_unit_group_order": target_group_order,
        "target_q_primary_rank": 0,
        "e1_factor_toggle": "unproved_external_integer_contract_required",
        "physical_source_class_token": "not_constructed",
    }


def attach_qualified_edge(
    arithmetic: dict[str, object], edge: dict[str, object] | None
) -> dict[str, object]:
    """Attach additive rank only after validating a complete prior edge receipt."""
    if edge is None:
        return {**arithmetic, "qualified_edge": "not_asserted_arithmetic_control"}
    assert edge["status"] == "QUALIFIED_INCIDENCE_EDGE"
    assert (edge["p"], edge["q"], edge["j"]) == (
        arithmetic["p"],
        arithmetic["q"],
        arithmetic["j"],
    )
    assert edge["endpoints"] == arithmetic["endpoints"]
    assert edge["normalized_column"] == 1
    attached = {
        **arithmetic,
        "qualified_edge": "verified_complete_receipt",
        "edge_signature": edge["signature"],
        "additive_source_rank": 1,
    }
    if arithmetic["status"] == "ADJACENT_EDGE_FIXED_BASE_QJ_PHYSICAL_OCCURRENCE":
        attached["direct_source_rank_lift"] = "DIRECT_TARGET_U4_Q_PRIMARY_LIFT_OBSTRUCTED"
    return attached


def d1_raw_certificate(p: int, h: int) -> dict[str, object]:
    assert h > 1 and (p + 4) % h == 0 and h % 4 == 3
    k = (h + 1) // 4
    numerator = k * p + 1
    assert numerator % h == 0
    b = numerator // h
    assert b > 1 and (b + 1) % k == 0
    denominators = (b, p * k, p * b * k)
    assert sum((Fraction(1, value) for value in denominators), Fraction()) == Fraction(4, p)
    return {
        "status": "D1_TYPE_II_RAW_SHORT_CERTIFICATE",
        "h": h,
        "A": 1,
        "C": 1,
        "K": k,
        "B": b,
        "m": (b + 1) // k,
        "x": b,
        "d": 1,
        "denominators": denominators,
    }


def d1_menu_dispatch(p: int) -> dict[str, object]:
    menu = tuple(h for h in divisors(p + 4) if h > 1 and h % 4 == 3)
    prime_factors = tuple(prime for prime, _ in factorint(p + 4))
    assert bool(menu) == any(prime % 4 == 3 for prime in prime_factors)
    if menu:
        return {
            "status": "D1_RAW_MENU_HIT",
            "menu": menu,
            "prime_factors": prime_factors,
            "selected": d1_raw_certificate(p, min(menu)),
        }
    assert all(prime % 4 == 1 for prime in prime_factors)
    return {
        "status": "D1_SINGLE_FACTOR_RAW_MENU_EMPTY",
        "menu": (),
        "prime_factors": prime_factors,
        "strict_d0_divisor_descent": False,
    }


def full_dispatch(
    *,
    p: int,
    q: int,
    j: int,
    left_index: int = 0,
    edge_receipt: dict[str, object] | None = None,
) -> dict[str, object]:
    menu = d1_menu_dispatch(p)
    if menu["status"] == "D1_RAW_MENU_HIT":
        return {
            "status": "D1_TYPE_II_TERMINAL",
            "terminal_first": True,
            "d1_menu": menu,
        }
    arithmetic = attach_qualified_edge(
        adjacent_fixed_base_arithmetic(p=p, q=q, j=j, left_index=left_index),
        edge_receipt,
    )
    if arithmetic["status"] == "ADJACENT_EDGE_FIXED_BASE_QJ_SOURCE_CRT_OBSTRUCTED":
        return {**arithmetic, "d1_menu": menu}
    return {
        **arithmetic,
        "status": "D1_QJ_OCCURRENCE_NO_D1_SINGLE_FACTOR_RAW_OR_DIRECT_U4_Q_LIFT",
        "d1_menu": menu,
    }


def verify() -> None:
    p73_arithmetic = adjacent_fixed_base_arithmetic(p=73, q=11, j=1)
    assert p73_arithmetic["beta"] == 1
    assert p73_arithmetic["endpoints"] == (1, 12)
    assert p73_arithmetic["physical_occurrence"] == (11, 1, 11, 77)
    assert "additive_source_rank" not in p73_arithmetic
    p73 = full_dispatch(p=73, q=11, j=1)
    assert p73["status"] == "D1_TYPE_II_TERMINAL"
    assert p73["terminal_first"] is True
    q11_terminal = d1_raw_certificate(73, 11)
    assert q11_terminal["K"] == 3 and q11_terminal["B"] == 20
    assert q11_terminal["denominators"] == (20, 219, 4380)

    p1033 = full_dispatch(p=1033, q=17, j=1)
    assert p1033["status"] == "D1_QJ_OCCURRENCE_NO_D1_SINGLE_FACTOR_RAW_OR_DIRECT_U4_Q_LIFT"
    assert p1033["beta"] == 1 and p1033["endpoints"] == (1, 18)
    assert p1033["physical_occurrence"] == (17, 1, 17, 1037)
    assert p1033["physical_source_class_token"] == "not_constructed"
    assert p1033["target_q_primary_rank"] == 0
    assert p1033["qualified_edge"] == "not_asserted_arithmetic_control"
    assert "additive_source_rank" not in p1033
    assert p1033["d1_menu"] == {
        "status": "D1_SINGLE_FACTOR_RAW_MENU_EMPTY",
        "menu": (),
        "prime_factors": (17, 61),
        "strict_d0_divisor_descent": False,
    }
    other_raw_denominators = (
        1 * 94 * 3,
        1033 * 1 * 3 * 1,
        1033 * 94 * 3 * 1,
    )
    assert 4 * 1 * 3 * 1 - 1 == 11
    assert (1 * 1033 + 1) // 11 == 94
    assert sum(
        (Fraction(1, value) for value in other_raw_denominators), Fraction()
    ) == Fraction(4, 1033)

    p241_arithmetic = adjacent_fixed_base_arithmetic(p=241, q=5, j=2)
    assert 245 % 5 == 0 and 245 % 25 != 0
    assert p241_arithmetic["beta"] == 21
    assert p241_arithmetic["endpoints"] == (21, 46)
    assert p241_arithmetic["status"] == "ADJACENT_EDGE_FIXED_BASE_QJ_SOURCE_CRT_OBSTRUCTED"
    p241 = full_dispatch(p=241, q=5, j=2)
    assert p241["status"] == "D1_TYPE_II_TERMINAL"
    assert p241["d1_menu"]["selected"]["h"] == 7

    p97_edge = inversion_edge_receipt(
        p=97,
        q=11,
        j=1,
        phases=(2, 9),
        affine=(8, 6),
        source_fractions=((5, 1), (1, 5)),
        record_ids=((1, 0), (-1, 0)),
    )
    p97 = full_dispatch(
        p=97,
        q=11,
        j=1,
        edge_receipt=p97_edge,
    )
    assert p97["status"] == "ADJACENT_EDGE_FIXED_BASE_QJ_SOURCE_CRT_OBSTRUCTED"
    assert p97["qualified_edge"] == "verified_complete_receipt"
    assert p97["additive_source_rank"] == 1
    assert p97["edge_signature"] == p97_edge["signature"]
    assert (p97["required_residue"], p97["target_residue"]) == (6, 1)
    assert p97["d1_menu"]["status"] == "D1_SINGLE_FACTOR_RAW_MENU_EMPTY"

    print("verified adjacent odd-owner fixed-base terminal/obstruction trichotomy")
    print("p73_q11", p73["status"], q11_terminal["denominators"])
    print("p1033_q17", p1033["status"], "target_q_rank=0")
    print("p241_q5_j2", p241["status"], "selected_h=7")
    print("p97_q11", p97["status"], "required_residue=6", "target_residue=1")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
