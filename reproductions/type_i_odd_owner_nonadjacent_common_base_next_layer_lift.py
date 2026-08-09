#!/usr/bin/env python3
"""Verify nonadjacent common-base arithmetic and next-q-layer gates."""

from __future__ import annotations

import argparse
from math import gcd

from type_i_core_jacobi_punctured_kernel_primary_selector import factorint
from type_i_odd_owner_scale_dichotomy_small_cofactor_terminal import divisors


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def euler_phi(value: int) -> int:
    result = value
    for prime, _ in factorint(value):
        result = result // prime * (prime - 1)
    return result


def multiplicative_order(value: int, modulus: int) -> int:
    assert gcd(value, modulus) == 1
    group_order = euler_phi(modulus)
    order = group_order
    for prime, _ in factorint(group_order):
        while order % prime == 0 and pow(value, order // prime, modulus) == 1:
            order //= prime
    assert pow(value, order, modulus) == 1
    return order


def canonical_target(x: int) -> tuple[int, int, int]:
    a = 1
    d_star = 1
    for prime, exponent in factorint(x):
        a *= prime ** (exponent // 2)
        d_star *= prime ** ((exponent + 1) // 2)
    c = d_star // a
    assert x == a * d_star
    assert all(exponent == 1 for _, exponent in factorint(c))
    return d_star, a, c


def target_menu(p: int, q: int, j: int, d0: int) -> tuple[int, ...]:
    power = q**j
    beta = (-p * pow(4, -1, power)) % power
    by_x = tuple(
        x
        for x in divisors(d0 * d0)
        if 4 * x < p and x % power == beta
    )
    by_parameters = []
    for d_star in divisors(d0):
        for a in divisors(d_star):
            c = d_star // a
            if any(exponent > 1 for _, exponent in factorint(c)):
                continue
            x = a * d_star
            if 4 * x < p and x % power == beta:
                by_parameters.append(x)
                assert canonical_target(x) == (d_star, a, c)
    assert by_x == tuple(sorted(by_parameters))
    return by_x


def edge_target_receipt(
    *, p: int, q: int, j: int, endpoints: tuple[int, int], d0: int, x: int
) -> dict[str, object]:
    power = q**j
    beta = (-p * pow(4, -1, power)) % power
    left, right = endpoints
    assert 0 < 4 * left < p and 0 < 4 * right < p
    assert left < right
    assert left % power == right % power == beta
    indices = ((left - beta) // power, (right - beta) // power)
    delta = indices[1] - indices[0]
    assert delta % q
    endpoint_gcd = gcd(left, right)
    assert endpoint_gcd == gcd(left, delta)
    assert endpoint_gcd % d0 == 0 and delta % d0 == 0 and d0 % q

    menu = target_menu(p, q, j, d0)
    assert x in menu
    d_star, a, c = canonical_target(x)
    assert d0 % d_star == 0
    modulus = 4 * d_star

    cofactors = tuple((p + 4 * endpoint) // power for endpoint in endpoints)
    target_cofactor = (p + 4 * x) // power
    assert cofactors[1] - cofactors[0] == 4 * delta
    assert all(gcd(cofactor, modulus) == 1 for cofactor in cofactors)
    cofactor_residues = tuple(cofactor % modulus for cofactor in cofactors)
    assert cofactor_residues[0] == cofactor_residues[1]
    assert target_cofactor % modulus == cofactor_residues[0]

    endpoint_heights = tuple(valuation(p + 4 * endpoint, q) for endpoint in endpoints)
    target_height = valuation(p + 4 * x, q)
    deep = tuple(height >= j + 1 for height in endpoint_heights)
    assert sum(deep) <= 1
    physical_order = multiplicative_order(q, modulus)
    ambient_q_torsion = euler_phi(modulus) % q == 0

    if sum(deep) == 0:
        status = "EDGE_NEXT_LAYER_SOURCE_CLASS_UNSEPARATED"
    elif target_height < j + 1:
        status = "EDGE_NEXT_LAYER_TARGET_QJ1_CRT_OBSTRUCTED"
    elif physical_order % q:
        status = "TARGET_PHYSICAL_Q_DIRECTION_PRIMARY_RANK_ZERO"
    else:
        status = "ARITHMETIC_NEXT_LAYER_LIFT_READY"

    return {
        "status": status,
        "p": p,
        "q": q,
        "j": j,
        "beta": beta,
        "endpoints": endpoints,
        "indices": indices,
        "delta": delta,
        "endpoint_gcd": endpoint_gcd,
        "common_source_base": d0,
        "target_menu": menu,
        "target": (d_star, a, c, x),
        "cofactors": cofactors,
        "target_cofactor": target_cofactor,
        "cofactor_residues": cofactor_residues,
        "endpoint_heights": endpoint_heights,
        "target_height": target_height,
        "physical_q_order": physical_order,
        "ambient_q_torsion": ambient_q_torsion,
        "arithmetic_next_layer_ready": sum(deep) == 1 and target_height >= j + 1,
        "freely_selectable_q_primary_role": physical_order % q == 0,
        "strict_parameter_drop": d_star < d0,
        "physical_source_class_e1": "requires_provenance_and_unclaimed_occurrences",
        "recursive_edge_eligible": False,
    }


def assert_canonical_source_rows(d0: int, source_as: tuple[int, int]) -> None:
    for a in source_as:
        assert d0 % a == 0
        assert all(exponent == 1 for _, exponent in factorint(d0 // a))


def assign_physical_occurrences(
    ledger: dict[tuple[str, int, int, int], str],
    *,
    edge_id: str,
    source_state_id: str,
    target_state_id: str,
    deep_endpoint: int,
    target: int,
    q: int,
    layer: int,
) -> str:
    keys = (
        (source_state_id, deep_endpoint, q, layer),
        (target_state_id, target, q, layer),
    )
    assignment_id = repr((edge_id, keys))
    owners = tuple(ledger.get(key) for key in keys)
    if all(owner == assignment_id for owner in owners):
        return "PHYSICAL_Q_LAYER_ASSIGNMENT_REPLAYED_NO_NEW_CHARGE"
    if any(owner is not None for owner in owners):
        return "PHYSICAL_Q_LAYER_ASSIGNMENT_CAPACITY_OBSTRUCTED"
    for key in keys:
        ledger[key] = assignment_id
    return "PHYSICAL_Q_LAYER_ASSIGNMENT_RECORDED"


def verify_universal_templates() -> tuple[dict[str, object], ...]:
    fixtures = (
        # p mod 9 = 7: x=14 and the A=2 row share the second 3-layer.
        (2689, (140, 350), 70, (2, 5), 14),
        # p mod 9 = 4: x=98 and the A=5 row share the second 3-layer.
        (1489, (140, 350), 70, (2, 5), 98),
        # p mod 9 = 1: use the D0=130 template and x=65.
        (2953, (260, 650), 130, (2, 5), 65),
    )
    receipts = []
    for p, endpoints, d0, source_as, x in fixtures:
        assert p % 24 == 1
        assert_canonical_source_rows(d0, source_as)
        assert endpoints == tuple(d0 * a for a in source_as)
        receipt = edge_target_receipt(
            p=p, q=3, j=1, endpoints=endpoints, d0=d0, x=x
        )
        assert receipt["status"] == "ARITHMETIC_NEXT_LAYER_LIFT_READY"
        assert receipt["strict_parameter_drop"] is True
        assert receipt["recursive_edge_eligible"] is False
        receipts.append(receipt)
    return tuple(receipts)


def verify() -> None:
    templates = verify_universal_templates()
    assert tuple(receipt["p"] % 9 for receipt in templates) == (7, 4, 1)
    assert tuple(receipt["target"] for receipt in templates) == (
        (14, 1, 14, 14),
        (14, 7, 2, 98),
        (65, 1, 65, 65),
    )
    assert tuple(receipt["physical_q_order"] for receipt in templates) == (6, 6, 12)

    positive = edge_target_receipt(
        p=2113, q=3, j=1, endpoints=(140, 350), d0=70, x=14
    )
    assert positive["status"] == "ARITHMETIC_NEXT_LAYER_LIFT_READY"
    assert positive["endpoint_heights"] == (5, 1)
    assert positive["target_height"] == 2
    assert positive["cofactor_residues"] == (51, 51)
    assert positive["target_cofactor"] % 56 == 51
    assert factorint(2113 + 4) == ((29, 1), (73, 1))
    assert not any(h > 1 and h % 56 == 55 for h in divisors(2113 + 56))

    missing_target_layer = edge_target_receipt(
        p=1489, q=3, j=1, endpoints=(140, 350), d0=70, x=14
    )
    assert missing_target_layer["status"] == "EDGE_NEXT_LAYER_TARGET_QJ1_CRT_OBSTRUCTED"
    assert missing_target_layer["endpoint_heights"] == (1, 3)
    assert missing_target_layer["target_height"] == 1
    assert missing_target_layer["physical_q_order"] == 6

    ambient_only = edge_target_receipt(
        p=2113, q=3, j=1, endpoints=(122, 488), d0=122, x=122
    )
    assert ambient_only["status"] == "TARGET_PHYSICAL_Q_DIRECTION_PRIMARY_RANK_ZERO"
    assert ambient_only["endpoint_heights"] == (2, 1)
    assert ambient_only["target_height"] == 2
    assert ambient_only["ambient_q_torsion"] is True
    assert ambient_only["physical_q_order"] == 10
    assert ambient_only["cofactor_residues"] == (379, 379)

    # Direct C3 quotient is stronger than a general q-primary character lift.
    assert multiplicative_order(3, 584) == 12
    assert pow(67, 3, 584) == 3

    occurrence_ledger: dict[tuple[str, int, int, int], str] = {}
    assignment = dict(
        source_state_id="source-state",
        target_state_id="target-state",
        deep_endpoint=140,
        target=14,
        q=3,
        layer=2,
    )
    assert assign_physical_occurrences(
        occurrence_ledger, edge_id="qualified-edge-1", **assignment
    ) == "PHYSICAL_Q_LAYER_ASSIGNMENT_RECORDED"
    assert assign_physical_occurrences(
        occurrence_ledger, edge_id="qualified-edge-1", **assignment
    ) == "PHYSICAL_Q_LAYER_ASSIGNMENT_REPLAYED_NO_NEW_CHARGE"
    assert assign_physical_occurrences(
        occurrence_ledger, edge_id="qualified-edge-2", **assignment
    ) == "PHYSICAL_Q_LAYER_ASSIGNMENT_CAPACITY_OBSTRUCTED"
    assert assign_physical_occurrences(
        occurrence_ledger,
        edge_id="qualified-edge-1",
        **(assignment | {"target_state_id": "other-target-state", "target": 98}),
    ) == "PHYSICAL_Q_LAYER_ASSIGNMENT_CAPACITY_OBSTRUCTED"

    print("verified nonadjacent common-base arithmetic and next-layer gates")
    print("universal_templates", tuple((r["p"], r["target"][3]) for r in templates))
    print("p2113_arithmetic_ready", positive["status"], "order=6", "residue=51")
    print("p1489_target_layer", missing_target_layer["status"])
    print("p2113_ambient_only", ambient_only["status"], "order=10")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
