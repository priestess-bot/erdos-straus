#!/usr/bin/env python3
"""Verify the bounded p=7129 F c=3 triple-tail certificate.

The certificate keeps four logically separate facts exact: a suffix-local
centered-layer positive control, the fixed-layer membership obstruction on
the declared source-root p-edge, two older narrow raw-to-affine obstructions,
and a direct Type II terminal identity.  It does not prove a selector edge,
carry/E2 lift, E4/E5, a stabilizer-quotient theorem, or global nonexistence.
"""

from __future__ import annotations

import argparse
import json
from itertools import product
from math import gcd


P = 7129
R = 30879
M = 7723
C = 7126
K = 55034098
Q_PRIMARY_LAYERS = (3, 23)
SUPPORT = (2, 7, 509, 7723)
COMPONENT_DATA = ((9, 2, 6), (47, 5, 46), (73, 5, 72))


def factorization(value: int) -> list[tuple[int, int]]:
    """Return the factorization of a positive integer by trial division."""
    if value <= 0:
        raise AssertionError("factorization requires a positive integer")
    factors: list[tuple[int, int]] = []
    divisor = 2
    while divisor * divisor <= value:
        exponent = 0
        while value % divisor == 0:
            value //= divisor
            exponent += 1
        if exponent:
            factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors.append((value, 1))
    return factors


def is_prime(value: int) -> bool:
    """Use the exact local factorization rather than a range scan."""
    return value > 1 and factorization(value) == [(value, 1)]


def valuation(value: int, prime: int) -> int:
    """Return v_prime(value) for a positive input."""
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def multiplicative_order(unit: int, modulus: int, group_order: int) -> int:
    """Compute an order from a supplied verified multiple of it."""
    if gcd(unit, modulus) != 1 or pow(unit, group_order, modulus) != 1:
        raise AssertionError("input is not a unit with the declared group order")
    order = group_order
    for prime, _ in factorization(group_order):
        while order % prime == 0 and pow(unit, order // prime, modulus) == 1:
            order //= prime
    return order


def cyclic_log_table(generator: int, modulus: int, order: int) -> dict[int, int]:
    """Build a small exact log table for one certified cyclic component."""
    if gcd(generator, modulus) != 1:
        raise AssertionError("cyclic generator must be a unit")
    table: dict[int, int] = {}
    value = 1
    for exponent in range(order):
        if value in table:
            raise AssertionError("generator repeated before its declared order")
        table[value] = exponent
        value = value * generator % modulus
    if value != 1 or len(table) != order:
        raise AssertionError("declared component generator has the wrong order")
    return table


def residue_product(factors: tuple[int, ...], exponents: tuple[int, ...]) -> int:
    """Evaluate one signed support word in U(R)."""
    residue = 1
    for factor, exponent in zip(factors, exponents):
        residue = residue * pow(factor, exponent, R) % R
    return residue


def crt_residue(residues: tuple[int, int, int]) -> int:
    """Return the unique residue modulo R with the specified CRT components."""
    moduli = (9, 47, 73)
    value = 0
    for residue, modulus in zip(residues, moduli):
        complement = R // modulus
        value += residue * complement * pow(complement, -1, modulus)
    return value % R


def component_log_tables() -> dict[int, dict[int, int]]:
    """Return certified CRT log tables for the three cyclic unit components."""
    return {
        modulus: cyclic_log_table(generator, modulus, order)
        for modulus, generator, order in COMPONENT_DATA
    }


def crt_log_coordinate(
    residue: int, logs: dict[int, dict[int, int]]
) -> tuple[int, int, int]:
    """Write a unit in the fixed C6 x C46 x C72 CRT coordinate system."""
    if gcd(residue, R) != 1:
        raise AssertionError("CRT coordinate requested for a nonunit")
    return tuple(logs[modulus][residue % modulus] for modulus, _, _ in COMPONENT_DATA)


def full_centered_layer() -> dict[int, tuple[int, int, int, int]]:
    """Construct the exact 3^4 fixed centered layer with inverse exponent data."""
    layer: dict[int, tuple[int, int, int, int]] = {}
    for exponents in product(range(-1, 2), repeat=len(SUPPORT)):
        residue = residue_product(SUPPORT, exponents)
        if residue in layer:
            raise AssertionError("the declared full centered layer has a collision")
        layer[residue] = exponents
    if len(layer) != 81 or 1 not in layer:
        raise AssertionError("the full centered layer changed")
    return layer


def raw_step(
    *,
    source: tuple[int, int, int],
    selected_coordinate_index: int,
    q: int,
    expected_destination: tuple[int, int, int],
) -> dict[str, int | bool | list[int]]:
    """Replay one ordered m=1 raw step from its integer definition."""
    if selected_coordinate_index not in (0, 1) or not is_prime(q):
        raise AssertionError("raw step input is malformed")
    left, right, layer = source
    if min(left, right, layer) <= 0 or left + right != R * layer:
        raise AssertionError("source is not a positive R-node")
    if gcd(left, right) != 1:
        raise AssertionError("source is not primitive")
    selected, other = (left, right) if selected_coordinate_index == 0 else (right, left)
    if selected % q:
        raise AssertionError("declared raw factor does not divide the selected coordinate")
    shift = (-layer) % q
    selected_height = valuation(selected, q)
    carrier_height = valuation(K, q)
    unit_condition = gcd(q, R * layer * other) == 1
    if not (
        selected_height > carrier_height
        and 1 <= shift < q
        and unit_condition
    ):
        raise AssertionError("strict capacity or unit condition failed")
    pre_gcd_destination = (
        selected // q,
        (other + R * shift) // q,
        (layer + shift) // q,
    )
    common = gcd(pre_gcd_destination[0], pre_gcd_destination[1])
    if common <= 0 or pre_gcd_destination[2] % common:
        raise AssertionError("gcd reduction does not preserve the layer")
    destination = tuple(value // common for value in pre_gcd_destination)
    if destination != expected_destination:
        raise AssertionError("raw destination changed")
    if (
        min(destination) <= 0
        or gcd(destination[0], destination[1]) != 1
        or destination[0] + destination[1] != R * destination[2]
    ):
        raise AssertionError("destination is not a primitive R-node")
    return {
        "source": list(source),
        "selected_coordinate_index": selected_coordinate_index,
        "selected_coordinate": selected,
        "q": q,
        "shift": shift,
        "selected_q_height": selected_height,
        "K_q_height": carrier_height,
        "strict_capacity": True,
        "unit_condition": True,
        "pre_gcd_destination": list(pre_gcd_destination),
        "gcd_reduction": common,
        "destination": list(destination),
    }


def verify_arithmetic_and_rows() -> dict[str, object]:
    """Check the c=3 determinant and all three exact-tail physical rows."""
    if not (
        is_prime(P)
        and P % 24 == 1
        and R == 4 * M - 13
        and P * R + 1 == 4 * K
        and K == M * C
        and factorization(K) == [(2, 1), (7, 1), (509, 1), (7723, 1)]
    ):
        raise AssertionError("p=7129 c=3 chart arithmetic changed")
    d = P - C
    n = 4 * M - R
    if (d, n) != (3, 13) or P * n != 4 * M * d + 1:
        raise AssertionError("c=3 determinant changed")

    rows: dict[str, dict[str, int]] = {}
    for tail in (4, 2, 1):
        selected = tail * C
        if gcd(selected, K) != C or K // C != M:
            raise AssertionError("exact tail no longer decodes to the physical row")
        rows[str(tail)] = {"C": C, "M": M, "t": tail, "d": d, "n": n}

    t4_node = (R - 4 * C, 4 * C, 1)
    t2_node = (2 * C, R - 2 * C, 1)
    t1_node = (C, R - C, 1)
    if t4_node != (2375, 28504, 1) or t2_node != (14252, 16627, 1) or t1_node != (7126, 23753, 1):
        raise AssertionError("p=7129 tail nodes changed")
    first = raw_step(
        source=t4_node,
        selected_coordinate_index=1,
        q=2,
        expected_destination=t2_node,
    )
    second = raw_step(
        source=t2_node,
        selected_coordinate_index=0,
        q=2,
        expected_destination=t1_node,
    )
    if [first["gcd_reduction"], second["gcd_reduction"]] != [1, 1]:
        raise AssertionError("tail chain unexpectedly needs gcd reduction")
    return {
        "parameters": {"p": P, "R": R, "K": K, "M": M, "C": C, "d": d, "n": n},
        "physical_rows": rows,
        "raw_tail": {"t4_to_t2": first, "t2_to_t1": second},
    }


def verify_f_fiber() -> dict[str, object]:
    """Check the supplied F witness and only its 3^4 finite central box."""
    if any(gcd(factor, R) != 1 for factor in SUPPORT):
        raise AssertionError("F support contains a nonunit")
    witness = (-2, 0, -5, 8)
    witness_residue = residue_product(SUPPORT, witness)
    if witness_residue != R - 1:
        raise AssertionError("declared F witness does not reach the target involution")
    finite_box_hit = any(
        residue_product(SUPPORT, exponents) == R - 1
        for exponents in product(range(-1, 2), repeat=len(SUPPORT))
    )
    if finite_box_hit:
        raise AssertionError("the finite F box unexpectedly reaches the target involution")
    return {
        "classification": "F",
        "support_factorization": [[factor, 1] for factor in SUPPORT],
        "finite_box": "[-1,1]^4",
        "finite_box_hit": False,
        "witness": list(witness),
        "witness_residue": witness_residue,
    }


def verify_group_and_primary_layers() -> dict[str, object]:
    """Certify U(R), then exhibit q=3 and q=23 characters nontrivial on 2."""
    if factorization(R) != [(3, 2), (47, 1), (73, 1)]:
        raise AssertionError("R factorization changed")
    logs = component_log_tables()
    unit_group_order = 6 * 46 * 72
    if unit_group_order != 19872 or factorization(unit_group_order) != [(2, 5), (3, 3), (23, 1)]:
        raise AssertionError("unit group order changed")

    eta_3_of_2 = logs[9][2 % 9] % 3
    eta_23_of_2 = logs[47][2 % 47] % 23
    if (eta_3_of_2, eta_23_of_2) != (1, 18):
        raise AssertionError("declared q-primary characters changed on raw factor 2")

    # Each word isolates one CRT cyclic generator.  Hence the actual F support
    # contains all three direct factors, rather than merely projecting onto each.
    isolation_words = {
        "C6_generator": ((1, 10, 10, 2), (2, 1, 1), 17156),
        "C46_generator": ((9, 0, 3, 12), (1, 5, 1), 28252),
        "C72_generator": ((6, 3, 0, 10), (1, 1, 5), 26650),
    }
    support_generators: dict[str, dict[str, object]] = {}
    for name, (word, components, expected_residue) in isolation_words.items():
        residue = residue_product(SUPPORT, word)
        if residue != expected_residue or residue != crt_residue(components):
            raise AssertionError("F support no longer generates the declared CRT factor")
        support_generators[name] = {
            "support_word": list(word),
            "CRT_components": list(components),
            "residue": residue,
        }
    return {
        "R_factorization": [[3, 2], [47, 1], [73, 1]],
        "unit_group": "C6 x C46 x C72",
        "unit_group_order": unit_group_order,
        "support_group": "<2,7,509,7723> = U(R)",
        "support_generator_words": support_generators,
        "component_generators": {
            "mod_9": {"generator": 2, "order": 6},
            "mod_47": {"generator": 5, "order": 46},
            "mod_73": {"generator": 5, "order": 72},
        },
        "q_primary_characters": {
            "3": {
                "component": "C6 -> C3",
                "character_order": 3,
                "eta_of_2": eta_3_of_2,
                "nontrivial_on_2": True,
            },
            "23": {
                "component": "C46 -> C23",
                "character_order": 23,
                "eta_of_2": eta_23_of_2,
                "nontrivial_on_2": True,
            },
        },
    }


def verify_centered_suffix_positive_control() -> dict[str, object]:
    """Verify the full-layer, suffix-local q-affine positive control only."""
    layer = full_centered_layer()
    layer_elements = set(layer)

    # Since 1 belongs to J, a setwise stabilizer element must itself lie in J.
    # Thus a finite check over J is an exact check of Stab_H(J).
    stabilizer = sorted(
        candidate
        for candidate in layer_elements
        if {candidate * element % R for element in layer_elements} == layer_elements
    )
    if stabilizer != [1]:
        raise AssertionError("the full centered layer stabilizer changed")

    theta = R - 1
    if multiplicative_order(theta, R, 19872) != 2:
        raise AssertionError("theta=-1 no longer has order 2")

    label_specs = {
        4: (4 * C, (0, 0, 0, -1)),
        2: (2 * C, (-1, 0, 0, -1)),
        1: (C, (1, 1, 1, 0)),
    }
    labels: dict[int, int] = {}
    phases: dict[int, int] = {}
    for tail, (label, expected_exponents) in label_specs.items():
        if layer.get(label) != expected_exponents:
            raise AssertionError("tail label is not in the declared centered layer")
        phase = (-pow(tail * C, -1, R)) % R
        if theta * pow(label, -1, R) % R != phase:
            raise AssertionError("tail phase does not have the centered-layer form")
        labels[tail] = label
        phases[tail] = phase
    if labels != {4: 28504, 2: 14252, 1: 7126}:
        raise AssertionError("centered tail labels changed")
    if phases != {4: 23156, 2: 15433, 1: 30866}:
        raise AssertionError("centered tail phases changed")
    if (
        labels[4] * pow(labels[2], -1, R) % R != 2
        or labels[2] * pow(labels[1], -1, R) % R != 2
    ):
        raise AssertionError("raw factor-2 tail transport changed in label form")

    logs = component_log_tables()
    character_components = {3: 9, 23: 47}
    expected_gamma = {3: {4: 0, 2: 1, 1: 2}, 23: {4: 21, 2: 16, 1: 11}}
    q_affine: dict[str, dict[str, object]] = {}
    for q, modulus in character_components.items():
        eta_of_2 = logs[modulus][2 % modulus] % q
        gamma = {
            tail: (-logs[modulus][label % modulus]) % q
            for tail, label in labels.items()
        }
        increments = {
            "4_to_2": (gamma[2] - gamma[4]) % q,
            "2_to_1": (gamma[1] - gamma[2]) % q,
        }
        if gamma != expected_gamma[q] or set(increments.values()) != {eta_of_2}:
            raise AssertionError("suffix-local q-affine phase data changed")
        q_affine[str(q)] = {
            "eta_of_2": eta_of_2,
            "gamma_by_tail": {str(tail): gamma[tail] for tail in (4, 2, 1)},
            "raw_2_edge_increments": increments,
        }

    return {
        "fixed_layer": "J_full = {2^a 7^b 509^c 7723^d : a,b,c,d in [-1,1]}",
        "cardinality": len(layer),
        "stabilizer": stabilizer,
        "quotient": "H / Stab_H(J_full) = H",
        "image_phi": "H = U(R), certified by the exact support isolation words",
        "theta": theta,
        "theta_order": 2,
        "theta_q_coprime_for": list(Q_PRIMARY_LAYERS),
        "labels": {
            str(tail): {
                "value": labels[tail],
                "support_exponents": list(label_specs[tail][1]),
                "phase": phases[tail],
            }
            for tail in (4, 2, 1)
        },
        "q_affine_suffix_data": q_affine,
        "scope": {
            "kind": "SUFFIX_LOCAL_POSITIVE_CONTROL",
            "integer_labels": "NOT_CONSTRUCTED",
            "carry_or_E2": "NOT_CONSTRUCTED",
            "E4_E5": "NOT_CONSTRUCTED",
            "source_root_policy": "NOT_PREDECLARED_FOR_THIS_SUFFIX_CONTROL",
        },
    }


def verify_declared_source_root_p_edge_no_go() -> dict[str, object]:
    """Block the declared source-root p-edge for the standard full centered J."""
    source = (P, R * (P - 1) - P, P - 1)
    first_edge = raw_step(
        source=source,
        selected_coordinate_index=0,
        q=P,
        expected_destination=(1, R - 1, 1),
    )
    if first_edge["gcd_reduction"] != 1:
        raise AssertionError("declared source-root p-edge changed")

    layer_elements = set(full_centered_layer())
    p_translate = {P * element % R for element in layer_elements}
    if layer_elements & p_translate:
        raise AssertionError("J_full unexpectedly admits the declared p-edge")

    logs = component_log_tables()
    support_coordinates = tuple(
        crt_log_coordinate(factor, logs) for factor in SUPPORT
    )
    p_coordinate = crt_log_coordinate(P, logs)
    expected_support_coordinates = (
        (1, 18, 8),
        (4, 32, 33),
        (5, 31, 44),
        (0, 21, 43),
    )
    if support_coordinates != expected_support_coordinates or p_coordinate != (0, 44, 38):
        raise AssertionError("CRT difference certificate changed")

    component_orders = (6, 46, 72)

    def difference_coordinate(exponents: tuple[int, int, int, int]) -> tuple[int, int, int]:
        return tuple(
            sum(
                exponents[index] * support_coordinates[index][component]
                for index in range(len(SUPPORT))
            )
            % component_orders[component]
            for component in range(3)
        )

    first_two_survivors = [
        exponents
        for exponents in product(range(-2, 3), repeat=len(SUPPORT))
        if difference_coordinate(exponents)[:2] == p_coordinate[:2]
    ]
    expected_survivors = [(-2, 0, -2, -2), (1, 1, -1, -1)]
    if first_two_survivors != expected_survivors:
        raise AssertionError("first-two-coordinate p-edge certificate changed")
    survivor_third_coordinates = [
        difference_coordinate(exponents)[2] for exponents in first_two_survivors
    ]
    if survivor_third_coordinates != [26, 26] or p_coordinate[2] != 38:
        raise AssertionError("third-coordinate p-edge obstruction changed")
    if any(
        difference_coordinate(exponents) == p_coordinate
        for exponents in product(range(-2, 3), repeat=len(SUPPORT))
    ):
        raise AssertionError("a centered-layer exponent difference reaches p")

    return {
        "declared_source_root": list(source),
        "first_raw_edge": first_edge,
        "fixed_layer_membership": "J_full intersection p*J_full is empty",
        "direct_finite_intersection_check": True,
        "CRT_difference_certificate": {
            "support_coordinates_C6_C46_C72": [list(value) for value in support_coordinates],
            "p_coordinate_C6_C46_C72": list(p_coordinate),
            "box_difference_range": "[-2,2]^4",
            "first_two_coordinate_survivors": [list(value) for value in first_two_survivors],
            "their_C72_coordinates": survivor_third_coordinates,
            "required_C72_coordinate": p_coordinate[2],
        },
        "forced_relation_if_one_theta_covers_edge": "j_source = p * j_destination",
        "status": "OBSTRUCTED_AT_P_EDGE_J_FULL_MEMBERSHIP",
        "scope": (
            "This applies to the declared source-root p-edge and the standard full "
            "centered layer J_full. It does not rule out another source word, root "
            "policy, or fixed layer."
        ),
    }


def verify_direct_type_ii_terminal() -> dict[str, object]:
    """Verify the direct Type II identity that terminates p=7129 first."""
    a, c, k = 1, 1, 2
    h = 4 * a * c * k - 1
    b = 2037
    m = (a + b) // k
    x = a * b * c
    d = a * a * c
    denominators = (x, 2 * P, 2 * P * x)
    if (
        h != 7
        or 2 * P + 1 != h * b
        or m != 1019
        or m % 4 != 3
        or (x + d) % m != 0
        or denominators != (2037, 14258, 29043546)
    ):
        raise AssertionError("direct Type II parameterization changed")
    product_of_denominators = denominators[0] * denominators[1] * denominators[2]
    if 4 * product_of_denominators != P * sum(
        product_of_denominators // denominator for denominator in denominators
    ):
        raise AssertionError("direct Type II identity failed")
    return {
        "type": "Type_II",
        "parameters": {"A": a, "C": c, "k": k, "h": h, "B": b, "m": m, "x": x, "d": d},
        "identity": "4/7129 = 1/2037 + 1/14258 + 1/29043546",
        "denominators": list(denominators),
        "terminal_status": "DIRECT_TYPE_II_TERMINAL_VERIFIED",
        "selector_status": "terminal_preempted",
    }


def verify_local_carry_core() -> dict[str, object]:
    """Record the local carry-core fact without promoting it to an E2 lift."""
    residue = M % P
    carry_core = gcd(M, C * residue)
    if residue != 594 or carry_core != 1:
        raise AssertionError("local p=7129 carry core changed")
    return {
        "row_representative": {"C": C, "M": M, "d": 3, "n": 13, "M_mod_p": residue},
        "tail_occurrences": [4, 2, 1],
        "carry_core": carry_core,
        "persistent_ledger_status": "ONLY_A_EQUALS_1_WITHIN_THIS_TRANSCRIPT",
        "physical_row_occurrence_policy": "ONE_PHYSICAL_ROW_THREE_MARKED_OCCURRENCES",
        "scope": "No carry/E2 lift or selector edge is claimed from this local fact.",
    }


def verify_natural_phase_and_affine_obstructions() -> dict[str, object]:
    """Establish only the natural-anchor and identity-map no-go statements."""
    unit_group_order = 19872
    phases = {tail: (-13 * pow(tail, -1, R)) % R for tail in (4, 2, 1)}
    expected_phases = {4: 23156, 2: 15433, 1: 30866}
    if phases != expected_phases:
        raise AssertionError("natural raw phase values changed")
    if phases[4] != (-M) % R or phases[2] != (-2 * M) % R or phases[1] != (-13) % R:
        raise AssertionError("natural raw phase lost its determinant normalization")
    if 2 * phases[4] % R != phases[2] or 2 * phases[2] % R != phases[1]:
        raise AssertionError("raw factor-2 phase transport changed")
    orders = {tail: multiplicative_order(phase, R, unit_group_order) for tail, phase in phases.items()}
    expected_orders = {4: 1656, 2: 552, 1: 1656}
    if orders != expected_orders:
        raise AssertionError("natural raw phase orders changed")
    if any(order % q for order in orders.values() for q in Q_PRIMARY_LAYERS):
        raise AssertionError("a natural phase unexpectedly became a q-coprime anchor")

    # In the unquotiented H=U(R), P=1 model, j_nu=s_nu=nu gives
    # gamma_1=0 and gamma_4=2 gamma_2 by multiplicativity.
    # A common affine law would force c=1, u*gamma_2=1, then 4=3 mod q.
    identity_affine_failures: dict[str, dict[str, int | str]] = {}
    for q in Q_PRIMARY_LAYERS:
        lhs = 4 % q
        rhs = (1 + 2 * (2 - 1)) % q
        if lhs == rhs:
            raise AssertionError("identity tail affine obstruction disappeared")
        identity_affine_failures[str(q)] = {
            "forced_c": 1 % q,
            "forced_u_gamma_2": 1 % q,
            "nu4_lhs": lhs,
            "nu4_rhs_from_affine_law": rhs,
            "status": "4_not_equal_3_mod_q",
        }
    return {
        "natural_raw_phase": {
            str(tail): {"value": phases[tail], "order": orders[tail]}
            for tail in (4, 2, 1)
        },
        "natural_anchor_status": {
            str(q): "OBSTRUCTED_ORDER_DIVISIBLE_BY_Q" for q in Q_PRIMARY_LAYERS
        },
        "scope": {
            "ambient_support_group": "H = U(R)",
            "stabilizer": "P = 1",
            "quotient_models": "NOT_ADDRESSED",
            "anchor_membership": "NOT_CHECKED",
        },
        "identity_abstract_label_ansatz": {
            "j_nu": "nu",
            "s_nu": "nu",
            "q_affine_failures": identity_affine_failures,
        },
        "alternative_anchor_or_map": "NOT_RULED_OUT",
    }


def build_result() -> dict[str, object]:
    """Build the bounded p=7129 certificate without a range search."""
    return {
        "certificate_type": "f_c3_triple_tail_raw_affine_obstruction_p7129_v2",
        "scope": (
            "One F c=3 physical control. Its full centered layer gives a suffix-local "
            "positive q-affine control, while the declared source-root p-edge fails "
            "that layer's membership gate. A direct Type II identity preempts any "
            "recursive selector action. The older natural-phase and identity-label "
            "obstructions remain limited to H=U(R), P=1; this is not an E2/E4/E5, "
            "stabilizer-quotient, or global nonexistence result."
        ),
        "physical_control": verify_arithmetic_and_rows(),
        "F_fiber": verify_f_fiber(),
        "unit_group_and_primary_layers": verify_group_and_primary_layers(),
        "centered_suffix_positive_control": verify_centered_suffix_positive_control(),
        "declared_source_root_p_edge_no_go": verify_declared_source_root_p_edge_no_go(),
        "obstructions": verify_natural_phase_and_affine_obstructions(),
        "direct_type_ii_terminal": verify_direct_type_ii_terminal(),
        "local_carry_core": verify_local_carry_core(),
        "admission": {
            "selector_status": "terminal_preempted",
            "recursive_edge_eligible": False,
            "terminal_first_status": "DIRECT_TYPE_II_TERMINAL_VERIFIED",
            "source_rooted_fixed_layer_status": "OBSTRUCTED_AT_P_EDGE_J_FULL_MEMBERSHIP",
            "suffix_only_fixed_layer_status": "POSITIVE_Q_AFFINE_CONTROL",
            "suffix_row_to_anchor_assignment": "VERIFIED_FOR_T4_T2_T1_ONLY",
            "full_source_rooted_row_to_anchor_assignment": (
                "OBSTRUCTED_AT_P_EDGE_J_FULL_MEMBERSHIP"
            ),
            "cross_chart_map": "not_ruled_out",
            "E4": "not_attempted",
            "E5": "not_attempted",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified p=7129 F c=3 triple-tail fixed-layer and terminal certificate")
        return
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
