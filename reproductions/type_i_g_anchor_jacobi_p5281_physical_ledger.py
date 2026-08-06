#!/usr/bin/env python3
"""Verify a finite physical G-anchor ledger at p=5281.

The ledger is complete only for the declared Jacobi-odd divisor menu and for
actual m=1 raw factor steps whose endpoints both remain in that menu.  It is
not an F/q-primary affine table, a carry-lift certificate, or a selector edge.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd, isqrt


PRIME = 5_281


def factorization(value: int) -> dict[int, int]:
    """Return the prime factorization of one positive integer."""
    if value <= 0:
        raise AssertionError("factorization requires a positive integer")
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def is_prime(value: int) -> bool:
    """Return whether one fixed positive integer is prime."""
    return value > 1 and factorization(value) == {value: 1}


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


def valuation(value: int, prime: int) -> int:
    """Return the prime-adic valuation of a positive integer."""
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def jacobi_symbol(value: int, modulus: int) -> int:
    """Return the Jacobi symbol for an odd positive modulus."""
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
        if value % 4 == 3 and modulus % 4 == 3:
            result = -result
        value %= modulus
    return result if modulus == 1 else 0


def prime_word(value: int) -> list[int]:
    """Return one deterministic prime-factor word."""
    return [
        prime
        for prime, exponent in factorization(value).items()
        for _ in range(exponent)
    ]


def raw_step(
    *,
    modulus: int,
    K: int,
    source: tuple[int, int, int],
    selected_coordinate_index: int,
    q: int,
    expected_destination: tuple[int, int, int],
    name: str,
) -> dict[str, object]:
    """Replay one actual raw step with capacity, unit, and gcd checks."""
    if selected_coordinate_index not in (0, 1):
        raise AssertionError("selected coordinate index must be 0 or 1")
    left, right, layer = source
    if min(left, right, layer) <= 0 or left + right != modulus * layer:
        raise AssertionError(f"{name}: source is not a positive formal node")
    if gcd(left, right) != 1:
        raise AssertionError(f"{name}: source is not primitive")
    selected, other = (left, right) if selected_coordinate_index == 0 else (right, left)
    if not is_prime(q) or selected % q:
        raise AssertionError(f"{name}: selected coordinate lacks the declared prime")

    selected_height = valuation(selected, q)
    K_height = valuation(K, q)
    shift = (-layer) % q
    unit_condition = gcd(q, modulus * layer * other) == 1
    if not (
        selected_height > K_height
        and 1 <= shift < q
        and unit_condition
    ):
        raise AssertionError(f"{name}: raw capacity or unit condition failed")

    selected_after = selected // q
    other_after = (other + modulus * shift) // q
    layer_after = (layer + shift) // q
    common = gcd(selected_after, other_after)
    if common <= 0 or layer_after % common:
        raise AssertionError(f"{name}: gcd reduction did not preserve the layer")
    destination = (
        selected_after // common,
        other_after // common,
        layer_after // common,
    )
    if destination != expected_destination:
        raise AssertionError(f"{name}: raw destination changed")
    if (
        min(destination) <= 0
        or gcd(destination[0], destination[1]) != 1
        or destination[0] + destination[1] != modulus * destination[2]
    ):
        raise AssertionError(f"{name}: destination is not a primitive formal node")
    if layer == 1 and destination[2] != 1:
        raise AssertionError(f"{name}: an m=1 step changed the layer")
    return {
        "name": name,
        "source": list(source),
        "selected_coordinate_index": selected_coordinate_index,
        "selected_coordinate": selected,
        "other_coordinate": other,
        "q": q,
        "shift": shift,
        "selected_q_height": selected_height,
        "K_q_height": K_height,
        "strict_capacity": selected_height > K_height,
        "unit_condition": unit_condition,
        "pre_gcd_destination": [selected_after, other_after, layer_after],
        "gcd_reduction": common,
        "destination": list(destination),
    }


def ledger_parameters() -> dict[str, int]:
    """Return and verify the fixed G-anchor chart parameters."""
    prime = PRIME
    R = prime - 2
    K = (prime - 1) ** 2 // 4
    Q = (prime - 3) // 2
    if not (
        is_prime(prime)
        and prime % 24 == 1
        and 4 * K == prime * R + 1
        and R == 2 * Q + 1
        and factorization(Q) == {7: 1, 13: 1, 29: 1}
        and factorization(K) == {2: 8, 3: 2, 5: 2, 11: 2}
        and gcd(Q, K) == 1
    ):
        raise AssertionError("p=5281 G-anchor parameters changed")
    return {"p": prime, "R": R, "K": K, "Q": Q}


def row_from_delta(*, delta: int, parameters: dict[str, int]) -> dict[str, int]:
    """Project one Jacobi-odd endpoint to its marked physical determinant row."""
    prime = parameters["p"]
    R = parameters["R"]
    K = parameters["K"]
    Q = parameters["Q"]
    if Q % delta or jacobi_symbol(delta, R) != -1:
        raise AssertionError("delta is outside the declared Jacobi-odd source menu")
    x = 2 * Q // delta
    y = R - x
    C = gcd(y, K)
    M = K // C
    t = y // C
    d = prime - C
    n = 4 * M - R
    if not (
        x > 0
        and x % 2 == 0
        and y > 0
        and y % 2 == 1
        and gcd(x, y) == 1
        and C * M == K
        and C * t == y
        and gcd(t, M) == 1
        and 0 < d < prime
        and n > 0
        and 4 * M > R
        and prime * n == 4 * M * d + 1
        and M * pow(t, -1, R) % R == K * delta % R
    ):
        raise AssertionError(f"delta={delta}: marked determinant row changed")
    return {
        "delta": delta,
        "x_even": x,
        "y_odd": y,
        "C": C,
        "M": M,
        "t": t,
        "d": d,
        "n": n,
    }


def root_and_menu_paths(
    *, parameters: dict[str, int], menu: tuple[int, ...]
) -> dict[str, object]:
    """Verify the universal root and one actual raw path to every menu row."""
    prime = parameters["p"]
    R = parameters["R"]
    K = parameters["K"]
    Q = parameters["Q"]
    root_source = (prime, R * (prime - 1) - prime, prime - 1)
    root_step = raw_step(
        modulus=R,
        K=K,
        source=root_source,
        selected_coordinate_index=0,
        q=prime,
        expected_destination=(1, R - 1, 1),
        name="universal_p_edge",
    )
    if root_step["gcd_reduction"] != 1:
        raise AssertionError("universal p edge unexpectedly reduced a gcd")

    anchor = (2 * Q, R - 2 * Q, 1)
    if anchor != (R - 1, 1, 1):
        raise AssertionError("G-anchor orientation changed")
    paths: dict[str, list[dict[str, object]]] = {}
    for delta in menu:
        current_delta = 1
        current = anchor
        steps: list[dict[str, object]] = []
        for q in prime_word(delta):
            next_delta = current_delta * q
            expected = (2 * Q // next_delta, R - 2 * Q // next_delta, 1)
            step = raw_step(
                modulus=R,
                K=K,
                source=current,
                selected_coordinate_index=0,
                q=q,
                expected_destination=expected,
                name=f"anchor_to_{delta}_via_{next_delta}",
            )
            if step["gcd_reduction"] != 1:
                raise AssertionError("Jacobi-odd menu path unexpectedly reduced a gcd")
            steps.append(step)
            current_delta = next_delta
            current = expected
        if current_delta != delta:
            raise AssertionError("canonical Jacobi-odd factor path ended at the wrong label")
        paths[str(delta)] = steps
    return {
        "root_source": list(root_source),
        "root_step": root_step,
        "anchor_orientation": {
            "from": [1, R - 1, 1],
            "to": list(anchor),
            "semantics": "coordinate_swap_not_a_raw_transition",
        },
        "canonical_paths": paths,
    }


def inter_menu_raw_edges(
    *, parameters: dict[str, int], menu: tuple[int, ...]
) -> list[dict[str, object]]:
    """Enumerate every declared actual raw factor edge whose endpoints stay in the menu."""
    R = parameters["R"]
    K = parameters["K"]
    Q = parameters["Q"]
    menu_set = set(menu)
    edges: list[dict[str, object]] = []
    for source_delta in menu:
        for q in factorization(Q):
            target_delta = source_delta * q
            if Q % target_delta or target_delta not in menu_set:
                continue
            source = (2 * Q // source_delta, R - 2 * Q // source_delta, 1)
            target = (2 * Q // target_delta, R - 2 * Q // target_delta, 1)
            step = raw_step(
                modulus=R,
                K=K,
                source=source,
                selected_coordinate_index=0,
                q=q,
                expected_destination=target,
                name=f"delta_{source_delta}_to_{target_delta}_via_{q}",
            )
            if step["gcd_reduction"] != 1:
                raise AssertionError("inter-menu raw step unexpectedly reduced a gcd")
            edges.append(
                {
                    "raw_from_delta": source_delta,
                    "q": q,
                    "raw_to_delta": target_delta,
                    "reverse_peeling_from_delta": target_delta,
                    "reverse_peeling_to_delta": source_delta,
                    "raw_step": step,
                }
            )
    expected = [(7, 13, 91), (7, 29, 203), (91, 29, 2639), (203, 13, 2639)]
    actual = [
        (int(edge["raw_from_delta"]), int(edge["q"]), int(edge["raw_to_delta"]))
        for edge in edges
    ]
    if actual != expected:
        raise AssertionError(f"inter-menu raw edge set changed: {actual}")
    return edges


def verified_menu_exit_edges(*, parameters: dict[str, int]) -> list[dict[str, object]]:
    """Replay enough legal menu exits to prove the full raw graph is larger."""
    R = parameters["R"]
    K = parameters["K"]
    declarations = [
        ((754, 4525, 1), 1, 181, (25, 5254, 1)),
        ((58, 5221, 1), 1, 23, (227, 5052, 1)),
        ((58, 5221, 1), 1, 227, (23, 5256, 1)),
        ((26, 5253, 1), 1, 17, (309, 4970, 1)),
        ((26, 5253, 1), 1, 103, (51, 5228, 1)),
        ((2, 5277, 1), 1, 1759, (3, 5276, 1)),
    ]
    exits: list[dict[str, object]] = []
    for index, (source, side, q, destination) in enumerate(declarations):
        step = raw_step(
            modulus=R,
            K=K,
            source=source,
            selected_coordinate_index=side,
            q=q,
            expected_destination=destination,
            name=f"verified_menu_exit_{index}",
        )
        if step["gcd_reduction"] != 1:
            raise AssertionError("fixed menu exit unexpectedly reduced a gcd")
        exits.append(step)
    return exits


def terminal_first_leaf(*, prime: int) -> dict[str, int]:
    """Verify the gap-seven Type II terminal which preempts this control."""
    x = (prime + 7) // 4
    if 4 * x != prime + 7 or (prime - 3) // 2 % 7:
        raise AssertionError("gap-seven terminal precondition changed")
    y = prime * (x + 1) // 7
    z = prime * x * (x + 1) // 7
    if Fraction(4, prime) != Fraction(1, x) + Fraction(1, y) + Fraction(1, z):
        raise AssertionError("gap-seven terminal identity changed")
    return {"x": x, "y": y, "z": z}


def build_result() -> dict[str, object]:
    """Build the narrowly scoped, fully replayed physical row ledger."""
    parameters = ledger_parameters()
    R = parameters["R"]
    Q = parameters["Q"]
    menu = tuple(delta for delta in divisors(Q) if jacobi_symbol(delta, R) == -1)
    if menu != (7, 91, 203, 2639):
        raise AssertionError("p=5281 Jacobi-odd menu changed")
    rows = [row_from_delta(delta=delta, parameters=parameters) for delta in menu]
    expected_rows = {
        7: {"M": 278_784, "C": 25, "t": 181, "d": 5_256, "n": 1_109_857},
        91: {"M": 6_969_600, "C": 1, "t": 5_221, "d": 5_280, "n": 27_873_121},
        203: {"M": 2_323_200, "C": 3, "t": 1_751, "d": 5_278, "n": 9_287_521},
        2639: {"M": 2_323_200, "C": 3, "t": 1_759, "d": 5_278, "n": 9_287_521},
    }
    for row in rows:
        expected = expected_rows[int(row["delta"])]
        if any(row[key] != value for key, value in expected.items()):
            raise AssertionError(f"physical row changed for delta={row['delta']}")

    root_paths = root_and_menu_paths(parameters=parameters, menu=menu)
    edges = inter_menu_raw_edges(parameters=parameters, menu=menu)
    exits = verified_menu_exit_edges(parameters=parameters)
    row_by_delta = {int(row["delta"]): row for row in rows}
    first_collision = row_by_delta[203]
    second_collision = row_by_delta[2639]
    unmarked_keys = ("M", "C", "d", "n")
    if (
        tuple(first_collision[key] for key in unmarked_keys)
        != tuple(second_collision[key] for key in unmarked_keys)
        or first_collision["t"] == second_collision["t"]
    ):
        raise AssertionError("p=5281 tail-label collision changed")
    if not all(
        bool(edge["raw_step"]["strict_capacity"])
        and bool(edge["raw_step"]["unit_condition"])
        for edge in edges
    ):
        raise AssertionError("inter-menu raw edge lost capacity or unit status")

    terminal = terminal_first_leaf(prime=parameters["p"])
    return {
        "schema_version": 1,
        "certificate_type": "g_anchor_jacobi_odd_physical_row_ledger_v1",
        "scope": (
            "Exact p=5281 ledger for the finite Jacobi-odd divisor menu and the "
            "actual m=1 raw factor edges with both endpoints in that menu. It is "
            "not complete for the full raw graph, and is not an F/q-primary affine "
            "source table, carry-lift, or selector edge."
        ),
        "parameters": parameters,
        "source_menu": {
            "definition": "{delta | delta divides Q and Jacobi_R(delta) = -1}",
            "deltas": list(menu),
            "source_complete": True,
            "completeness_scope": "the declared finite Jacobi-odd divisor menu only",
            "root_and_paths": root_paths,
        },
        "physical_rows": rows,
        "physical_transition_relation": {
            "raw_orientation": "e -> q*e",
            "reverse_peeling_orientation": "q*e -> e",
            "edges": edges,
            "physical_transition_complete": True,
            "completeness_scope": (
                "all divisor-factor m=1 raw edges with both endpoints in the declared "
                "Jacobi-odd menu only"
            ),
            "full_raw_transition_complete": False,
            "verified_exit_edges": exits,
        },
        "tail_label_necessity": {
            "unmarked_fields": list(unmarked_keys),
            "collision_deltas": [203, 2639],
            "shared_unmarked_row": {
                key: first_collision[key] for key in unmarked_keys
            },
            "distinct_tails": [first_collision["t"], second_collision["t"]],
            "conclusion": (
                "The exact tail t is required to identify a marked physical row and "
                "its reverse-peeling successor; M/C data alone cannot do so."
            ),
        },
        "aal_gate_status": {
            "source_complete": True,
            "physical_transition_complete": True,
            "F_q_primary_anchor": "not_available_in_this_G_Jacobi_C2_control",
            "row_to_anchor_map": "not_available",
            "common_affine_chart": "not_available",
            "physical_label_interval": "not_available",
            "physical_label_multiplicity": "not_available",
            "physical_carry_status": "not_evaluated_for_a_cofactor_lift",
            "status": "ANCHORED_PHASE_MAP_UNCLOSED",
        },
        "terminal_first": {
            "status": "terminal_leaf",
            "certificate_type": "gap_seven_type_ii",
            "denominators": terminal,
            "preempts_recursive_use": True,
        },
        "selector_status": "analysis_evidence",
        "recursive_edge_eligible": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    build_result()
    if args.verify:
        print("verified p=5281 Jacobi-odd physical row ledger")


if __name__ == "__main__":
    main()
