#!/usr/bin/env python3
"""Reproduce the p=60913 h=2 high-R non-return r-chart.

The first high anchor and the high overflow are G states.  Their separators
are exact CRT parity characters written through verified primitive-root
discrete-log coordinates.  The r-chart target is an F state with a canonical
signed exponent witness.  This keeps the example independent of the central
selector while closing every local source, support, and fiber check.
"""

from __future__ import annotations

import argparse
import json
from math import gcd, lcm, prod
from pathlib import Path

from short_certificate import type_i_normal_form_certificate, verify_certificate
import type_i_high_r_chart_two_anchor as shared


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-high-r-chart-60913-h2-nonreturn-results.json"


ANCHOR_COMPONENTS = [
    {
        "modulus": 11,
        "primitive_root": 2,
        "factor_logs": [[29, 7], [643, 4], [59011, 7]],
        "minus_one_log": 5,
    },
    {
        "modulus": 6569,
        "primitive_root": 3,
        "factor_logs": [[29, 1737], [643, 4000], [59011, 3015]],
        "minus_one_log": 3284,
    },
]

SOURCE_COMPONENTS = [
    {
        "modulus": 37,
        "primitive_root": 2,
        "factor_logs": [[2, 1], [3, 26], [29, 21], [643, 33], [12043, 17]],
        "minus_one_log": 18,
    },
    {
        "modulus": 677,
        "primitive_root": 2,
        "factor_logs": [[2, 1], [3, 479], [29, 229], [643, 350], [12043, 585]],
        "minus_one_log": 338,
    },
    {
        "modulus": 197599,
        "primitive_root": 3,
        "factor_logs": [
            [2, 166274],
            [3, 1],
            [29, 123248],
            [643, 71787],
            [12043, 99096],
        ],
        "minus_one_log": 98799,
    },
]


def primitive_root_is_valid(modulus: int, root: int) -> bool:
    """Use the prime-factor order test, avoiding a hidden discrete-log oracle."""
    if not shared.is_prime(modulus) or not 1 <= root < modulus:
        return False
    order = modulus - 1
    return pow(root, order, modulus) == 1 and all(
        pow(root, order // prime, modulus) != 1
        for prime, _exponent in shared.factorization(order)
    )


def crt_discrete_log_parity_g_fiber(
    R: int,
    K: int,
    components: list[dict[str, object]],
) -> dict[str, object]:
    """Certify G by a parity character across prime CRT components.

    For a component q with primitive root g, write log_g(u) in Z/(q-1).
    The sum of these logs modulo 2 is a well-defined character precisely
    because every q-1 is even.  The supplied records verify that it is zero
    on every prime factor of K and one on -1.
    """
    factors = shared.factorization(K)
    bases = [prime for prime, _exponent in factors]
    canonical_components: list[dict[str, object]] = []
    logs_by_base = {base: [] for base in bases}
    target_logs: list[int] = []
    component_conditions: list[bool] = []

    for component in sorted(components, key=lambda item: int(item["modulus"])):
        modulus = int(component["modulus"])
        root = int(component["primitive_root"])
        raw_logs = component["factor_logs"]
        if not isinstance(raw_logs, list):
            raise AssertionError("CRT parity component factor logs changed")
        factor_logs = [[int(base), int(value)] for base, value in raw_logs]
        log_map = {base: value for base, value in factor_logs}
        order = modulus - 1
        minus_one_log = int(component["minus_one_log"])
        component_ok = bool(
            len(log_map) == len(factor_logs)
            and sorted(log_map) == bases
            and primitive_root_is_valid(modulus, root)
            and 0 <= minus_one_log < order
            and pow(root, minus_one_log, modulus) == (-1) % modulus
            and all(
                0 <= log_map[base] < order
                and pow(root, log_map[base], modulus) == base % modulus
                for base in bases
            )
        )
        component_conditions.append(component_ok)
        if not component_ok:
            raise AssertionError("CRT parity component did not verify")
        for base in bases:
            logs_by_base[base].append(log_map[base])
        target_logs.append(minus_one_log)
        canonical_components.append(
            {
                "modulus": modulus,
                "primitive_root": root,
                "factor_logs": [[base, log_map[base]] for base in bases],
                "minus_one_log": minus_one_log,
            }
        )

    moduli = [int(component["modulus"]) for component in canonical_components]
    support_parity = {str(base): sum(values) % 2 for base, values in logs_by_base.items()}
    minus_one_parity = sum(target_logs) % 2
    conditions = {
        "prime_crt_factorization": (
            prod(moduli) == R
            and shared.factorization(R) == [(modulus, 1) for modulus in moduli]
        ),
        "pairwise_coprime_components": all(
            gcd(left, right) == 1
            for index, left in enumerate(moduli)
            for right in moduli[index + 1 :]
        ),
        "primitive_roots_and_logs": all(component_conditions),
        "support_character_trivial": all(value == 0 for value in support_parity.values()),
        "minus_one_character_nontrivial": minus_one_parity == 1,
    }
    if not all(conditions.values()):
        raise AssertionError("CRT parity data did not certify a G fiber")
    return {
        "classification": "G",
        "support_factorization": [[prime, exponent] for prime, exponent in factors],
        "target_in_generated_subgroup": False,
        "separator": {
            "kind": "crt_discrete_log_parity",
            "components": canonical_components,
            "support_parity": support_parity,
            "minus_one_parity": minus_one_parity,
        },
        "signed_defect": {
            "status": "not_applicable",
            "reason": "CRT_discrete_log_parity_separator",
        },
        "conditions": conditions,
    }


def fiber_certificate_is_valid(R: int, K: int, fiber: dict[str, object]) -> bool:
    if fiber.get("classification") == "F":
        return shared.fiber_certificate_is_valid(R, K, fiber)
    separator = fiber.get("separator")
    if not isinstance(separator, dict) or separator.get("kind") != "crt_discrete_log_parity":
        return False
    components = separator.get("components")
    if not isinstance(components, list):
        return False
    try:
        return crt_discrete_log_parity_g_fiber(R, K, components) == fiber
    except (AssertionError, KeyError, TypeError, ValueError):
        return False


def same_chart_parent_replay(
    *,
    prime: int,
    B_p: int,
    root_bundle: dict[str, object],
    fiber: dict[str, object],
) -> dict[str, object]:
    """Replay the root support promotion with the CRT-G E4 verifier."""
    rechart = root_bundle["rechart"]
    conditions = root_bundle["conditions"]
    if not isinstance(rechart, dict) or not isinstance(conditions, dict):
        raise AssertionError("root receipt shape changed")
    M = int(rechart["M"])
    R = int(rechart["R"])
    K = int(rechart["K"])
    C = int(rechart["C"])
    d = int(rechart["d"])
    n = int(rechart["n"])
    scope = "fresh_source_tree_only"
    fiber_class = str(fiber["classification"])
    source_state = shared.make_state(
        prime=prime,
        R=R,
        K=K,
        support=1,
        state_class="overflow",
        fiber_class=fiber_class,
        source_tree_scope=scope,
    )
    successor_state = shared.make_state(
        prime=prime,
        R=R,
        K=K,
        support=M,
        state_class="overflow",
        fiber_class=fiber_class,
        source_tree_scope=scope,
    )
    checks = {
        "root_entry": bool(
            root_bundle["R_domain"] == "core_R"
            and all(bool(value) for value in conditions.values())
            and int(root_bundle["source"]["R"]) < prime
            and 2 <= M <= B_p
            and R > prime
            and K == M * C
            and prime * n == 4 * M * d + 1
        ),
        "source_state": shared.state_id_is_valid(source_state) and K % 1 == 0,
        "same_chart_successor": bool(
            shared.state_id_is_valid(successor_state)
            and successor_state["R"] == source_state["R"]
            and successor_state["K"] == source_state["K"]
            and K % M == 0
        ),
        "identity_lift": fiber_certificate_is_valid(R, K, fiber),
        "strict_support_potential": B_p // M < B_p,
        "scope_propagated": source_state["source_tree_scope"]
        == successor_state["source_tree_scope"]
        == scope,
    }
    if not all(checks.values()):
        raise AssertionError("CRT-G same-chart parent replay failed")
    receipt = {
        "certificate_type": "overflow_same_chart_support_promotion",
        "normal_form_replay_adapter": "high_r_same_chart_parent_replay_crt_parity_v1",
        "selector_status": "verified_edge",
        "recursive_edge_eligible": True,
        "source_state": source_state,
        "successor_state": successor_state,
        "source_provenance": {
            "state_origin": "universal_raw_default_entry_v1",
            "source_tree_scope": scope,
            "root_bundle_adapter": root_bundle["adapter"],
            "root_anchor": root_bundle["anchor_node"],
        },
        "marked_solution_set": {"source": "Sol(p)", "successor": "Sol(p)", "lift": "identity"},
        "fiber_certificate": fiber,
        "e1_e5": {f"E{index}": True for index in range(1, 6)},
        "checks": checks,
    }
    receipt["edge_id"] = "edge:" + shared.canonical_hash(
        {"source": source_state, "successor": successor_state}
    )
    return receipt


def verify_charged_parent_replay(parent: dict[str, object], anchor_state: dict[str, object]) -> bool:
    source = parent.get("source_state")
    successor = parent.get("successor_state")
    checks = parent.get("checks")
    fiber = parent.get("fiber_certificate")
    marked_solution_set = parent.get("marked_solution_set")
    if not all(
        isinstance(value, dict)
        for value in (source, successor, checks, fiber, marked_solution_set)
    ):
        return False
    equation_target = source.get("equation_target")
    expected_edge_id = "edge:" + shared.canonical_hash({"source": source, "successor": successor})
    return bool(
        parent.get("certificate_type") == "overflow_same_chart_support_promotion"
        and parent.get("normal_form_replay_adapter")
        == "high_r_same_chart_parent_replay_crt_parity_v1"
        and parent.get("edge_id") == expected_edge_id
        and parent.get("selector_status") == "verified_edge"
        and parent.get("recursive_edge_eligible") is True
        and parent.get("e1_e5") == {f"E{index}": True for index in range(1, 6)}
        and all(bool(value) for value in checks.values())
        and shared.state_id_is_valid(source)
        and shared.state_id_is_valid(successor)
        and fiber_certificate_is_valid(int(source["R"]), int(source["K"]), fiber)
        and source.get("fiber_class") == fiber.get("classification")
        and successor.get("fiber_class") == fiber.get("classification")
        and isinstance(equation_target, list)
        and len(equation_target) == 2
        and equation_target[0] == 4
        and isinstance(equation_target[1], int)
        and equation_target[1] > 1
        and successor.get("equation_target") == equation_target
        and marked_solution_set
        == {"source": "Sol(p)", "successor": "Sol(p)", "lift": "identity"}
        and successor == anchor_state
        and source.get("R") == successor.get("R")
        and source.get("K") == successor.get("K")
        and int(source.get("absorbed_support", 0)) < int(successor.get("absorbed_support", 0))
        and source.get("source_tree_scope") == successor.get("source_tree_scope")
    )


def verify_cofactor_normal_form(
    *,
    prime: int,
    support: int,
    M: int,
    R_M: int,
    K_M: int,
    C: int,
    d: int,
    n: int,
    r: int,
    s: int,
    R_r: int,
    K_r: int,
    cofactor_support: int,
    source_state: dict[str, object],
    successor_state: dict[str, object],
    source_fiber: dict[str, object],
    successor_fiber: dict[str, object],
    charged_parent_replayed: bool,
) -> dict[str, bool]:
    """The r-chart normal form with the local CRT-G/F fiber verifier."""
    support_quotient = support // gcd(support, C)
    target_C = r // support_quotient
    target_d = prime - target_C
    target_n = 4 * cofactor_support - R_r
    source_ok = bool(
        shared.state_id_is_valid(source_state)
        and source_state.get("equation_target") == [4, prime]
        and source_state.get("R") == R_M
        and source_state.get("K") == K_M
        and source_state.get("absorbed_support") == support
        and source_state.get("state_class") == "overflow"
        and source_state.get("fiber_class") == source_fiber.get("classification")
        and fiber_certificate_is_valid(R_M, K_M, source_fiber)
        and R_M > prime
        and M % support == 0
        and shared.canonical_chart(prime, M) == (R_M, K_M)
        and K_M == M * C
        and C == prime - d
        and prime * n == 4 * M * d + 1
        and R_M == 4 * M - n
    )
    construction_ok = bool(
        r > 0
        and prime * s == 4 * r * d + 1
        and prime * R_r + 1 == 4 * K_r
        and K_r == r * C
        and support_quotient > 0
        and r % support_quotient == 0
        and cofactor_support == lcm(support, C)
        and K_r % cofactor_support == 0
    )
    successor_ok = bool(
        shared.state_id_is_valid(successor_state)
        and successor_state.get("equation_target") == [4, prime]
        and successor_state.get("R") == R_r
        and successor_state.get("K") == K_r
        and successor_state.get("absorbed_support") == cofactor_support
        and successor_state.get("state_class") == "overflow"
        and successor_state.get("fiber_class") == successor_fiber.get("classification")
        and fiber_certificate_is_valid(R_r, K_r, successor_fiber)
        and R_r > prime
        and shared.canonical_chart(prime, cofactor_support) == (R_r, K_r)
        and target_C > 0
        and target_d > 0
        and target_n > 0
        and K_r == cofactor_support * target_C
        and prime * target_n == 4 * cofactor_support * target_d + 1
        and R_r == 4 * cofactor_support - target_n
    )
    checks = {
        "source_state": source_ok,
        "construction": construction_ok,
        "successor_state": successor_ok,
        "source_tree_scope": source_state.get("source_tree_scope")
        == successor_state.get("source_tree_scope")
        == "fresh_source_tree_only",
        "parent_ledger": charged_parent_replayed,
    }
    checks["passed"] = all(checks.values())
    return checks


def direct_type_i_terminal(prime: int) -> dict[str, object]:
    certificate = type_i_normal_form_certificate(prime, 7, 1, 1)
    if certificate is None or not verify_certificate(certificate):
        raise AssertionError("p=60913 gap-seven Type I terminal failed")
    c = 15_230
    h = 8_702
    checks = {
        "normal_form": prime == 4 * c - 7,
        "gap_condition": (prime + 1) % 7 == 0,
        "denominator_parameters": (
            certificate.x == c
            and certificate.y == c * h
            and certificate.z == prime * c * h
        ),
        "unit_fraction_identity": 4 * certificate.x * certificate.y * certificate.z
        == prime * (certificate.y * certificate.z + certificate.x * certificate.z + certificate.x * certificate.y),
    }
    if not all(checks.values()):
        raise AssertionError("p=60913 direct Type I terminal arithmetic changed")
    return {
        "certificate_type": "type_i_normal_form_terminal",
        "selector_status": "terminal_leaf",
        "recursive_edge_eligible": False,
        "normal_form": {"gap": 7, "A": 1, "B": 1, "C": c, "H": h},
        "denominators": {"x": certificate.x, "y": certificate.y, "z": certificate.z},
        "checks": checks,
    }


def build_result() -> dict[str, object]:
    prime = 60_913
    B_p = (prime - 1) ** 2 // 4
    R_0 = 37_295
    K_0 = (prime * R_0 + 1) // 4
    if not (
        shared.is_prime(prime)
        and prime % 24 == 1
        and 3 <= R_0 <= prime - 2
        and R_0 % 4 == 3
        and K_0 == 567_937_584
        and shared.factorization(R_0 - 1) == [(2, 1), (29, 1), (643, 1)]
    ):
        raise AssertionError("p=60913 fresh core root changed")

    root_bundle = shared.high_R_path_anchored_bundle(prime=prime, R=R_0, support=1)
    root_rechart = root_bundle["rechart"]
    Q_0 = int(root_bundle["complete_excess_bundle"]["Q"])
    beta_0 = int(root_bundle["complete_excess_bundle"]["beta"])
    A = int(root_rechart["M"])
    R_1 = int(root_rechart["R"])
    K_1 = int(root_rechart["K"])
    if not (
        (Q_0, beta_0, A, R_1, K_1) == (18_647, 2, 18_647, 72_259, 1_100_378_117)
        and root_rechart["result_class"] == "overflow"
        and A <= B_p
        and K_1 == A * 59_011
    ):
        raise AssertionError("p=60913 first high anchor changed")

    anchor_fiber = crt_discrete_log_parity_g_fiber(R_1, K_1, ANCHOR_COMPONENTS)
    parent_replay = same_chart_parent_replay(
        prime=prime,
        B_p=B_p,
        root_bundle=root_bundle,
        fiber=anchor_fiber,
    )
    high_anchor_state = parent_replay["successor_state"]
    if not isinstance(high_anchor_state, dict) or not verify_charged_parent_replay(
        parent_replay, high_anchor_state
    ):
        raise AssertionError("p=60913 CRT-G charged parent did not replay")

    high_bundle = shared.high_R_path_anchored_bundle(prime=prime, R=R_1, support=A)
    high_rechart = high_bundle["rechart"]
    Q_1 = int(high_bundle["complete_excess_bundle"]["Q"])
    beta_1 = int(high_bundle["complete_excess_bundle"]["beta"])
    M = int(high_rechart["M"])
    R_M = int(high_rechart["R"])
    K_M = int(high_rechart["K"])
    C = int(high_rechart["C"])
    d = int(high_rechart["d"])
    n = int(high_rechart["n"])
    k, r = divmod(M, prime)
    if not (
        (Q_1, beta_1) == (72_258, 1)
        and (M, R_M, K_M, C, d, n, k, r)
        == (1_347_394_926, 4_949_657_351, 75_374_619_555_366, 55_941, 4_972, 439_922_353, 22_119, 60_279)
        and M > B_p
        and prime * n == 4 * M * d + 1
    ):
        raise AssertionError("p=60913 high-R overflow changed")

    g = gcd(A, C)
    a = A // g
    A_C = lcm(A, C)
    s_numerator = 4 * r * d + 1
    if s_numerator % prime:
        raise AssertionError("p=60913 cofactor s is not integral")
    s = s_numerator // prime
    R_r = 4 * r - s
    K_r = r * C
    target_C = r // a
    target_d = prime - target_C
    target_n = 4 * A_C - R_r
    phase_numerator = K_r - K_1
    if phase_numerator % (prime * A):
        raise AssertionError("p=60913 phase h is not integral")
    h = phase_numerator // (prime * A)
    cofactor_checks = {
        "h_two": h == 2 and R_r == R_1 + 8 * A,
        "strict_nonreturn": R_r > R_1 > prime,
        "cofactor_gate": r % a == 0,
        "strict_support_growth": A < A_C <= B_p,
        "target_canonical_chart": shared.canonical_chart(prime, A_C) == (R_r, K_r),
        "target_overflow_normal_form": (
            target_C > 0
            and target_d > 0
            and target_n > 0
            and K_r == A_C * target_C
            and prime * target_n == 4 * A_C * target_d + 1
        ),
    }
    if not (
        (g, a, A_C, s, R_r, K_r, target_C, target_d, target_n, h)
        == (18_647, 1, 55_941, 19_681, 221_435, 3_372_067_539, 60_279, 634, 2_329, 2)
        and all(cofactor_checks.values())
    ):
        raise AssertionError("p=60913 h=2 cofactor r-chart changed")

    source_fiber = crt_discrete_log_parity_g_fiber(R_M, K_M, SOURCE_COMPONENTS)
    target_fiber = shared.residue_witness(
        R_r,
        shared.factorization(K_r),
        (-5, -2, 5, 0, -5),
    )
    if target_fiber["witness_l1"] != 17:
        raise AssertionError("p=60913 target F witness changed")

    scope = "fresh_source_tree_only"
    source_state = shared.make_state(
        prime=prime,
        R=R_M,
        K=K_M,
        support=A,
        state_class="overflow",
        fiber_class=str(source_fiber["classification"]),
        source_tree_scope=scope,
    )
    successor_state = shared.make_state(
        prime=prime,
        R=R_r,
        K=K_r,
        support=A_C,
        state_class="overflow",
        fiber_class=str(target_fiber["classification"]),
        source_tree_scope=scope,
    )
    cofactor_normal_form = verify_cofactor_normal_form(
        prime=prime,
        support=A,
        M=M,
        R_M=R_M,
        K_M=K_M,
        C=C,
        d=d,
        n=n,
        r=r,
        s=s,
        R_r=R_r,
        K_r=K_r,
        cofactor_support=A_C,
        source_state=source_state,
        successor_state=successor_state,
        source_fiber=source_fiber,
        successor_fiber=target_fiber,
        charged_parent_replayed=verify_charged_parent_replay(parent_replay, high_anchor_state),
    )
    if not cofactor_normal_form["passed"]:
        raise AssertionError("p=60913 cofactor normal-form replay failed")

    source_potential = B_p // A
    target_potential = B_p // A_C
    terminal = direct_type_i_terminal(prime)
    p_plus_four_factors = shared.factorization(prime + 4)
    p_plus_four_q3 = [factor for factor, _exponent in p_plus_four_factors if factor % 4 == 3]
    if p_plus_four_q3:
        raise AssertionError("p=60913 p+4 Type II quick filter changed")
    local_e1_e5 = {
        "E1": bool(
            all(bool(value) for value in root_bundle["conditions"].values())
            and verify_charged_parent_replay(parent_replay, high_anchor_state)
            and all(bool(value) for value in high_bundle["conditions"].values())
        ),
        "E2": bool(cofactor_normal_form["construction"] and cofactor_checks["h_two"]),
        "E3": cofactor_normal_form["passed"],
        "E4": bool(
            anchor_fiber["classification"] == "G"
            and source_fiber["classification"] == "G"
            and target_fiber["classification"] == "F"
            and fiber_certificate_is_valid(R_1, K_1, anchor_fiber)
            and fiber_certificate_is_valid(R_M, K_M, source_fiber)
            and fiber_certificate_is_valid(R_r, K_r, target_fiber)
        ),
        "E5": target_potential < source_potential,
    }
    if local_e1_e5 != {f"E{index}": True for index in range(1, 6)}:
        raise AssertionError("p=60913 local E1-E5 contract failed")

    return {
        "schema_version": 1,
        "certificate_type": "type_i_high_r_h2_nonreturn_g_g_f_v1",
        "selector_status": "candidate_transition",
        "recursive_edge_eligible": False,
        "proof_boundary": (
            "this dedicated receipt verifies a fresh root, a CRT-G charged parent, "
            "a G-to-F h=2 cofactor transition, and a strict local support potential. "
            "It is not a global recursive edge because a non-resetting cross-anchor "
            "phase rank is still unproved; terminal-first independently closes p=60913."
        ),
        "prime": prime,
        "B_p": B_p,
        "bounded_search_provenance": {
            "range": "p <= 100000, p == 1 (mod 24)",
            "purpose": "construction discovery only, not a coverage statement",
            "arithmetic_h_two_rows_before_fresh_root_filter": 13,
            "fresh_root_rows_after_exact_complete_excess_replay": 2,
            "h_two_predicates": [
                "p/4 < A <= (3p-9)/8",
                "fresh core complete-excess root",
                "charged same-chart parent",
                "high complete-excess overflow",
                "cofactor gate and A < lcm(A,C) <= B_p",
            ],
        },
        "core_anchor": {"R": R_0, "K": K_0},
        "first_high_anchor": {
            "Q": Q_0,
            "beta": beta_0,
            "R": R_1,
            "K": K_1,
            "fiber": anchor_fiber,
            "same_chart_parent_replay": parent_replay,
        },
        "high_overflow": {
            "Q": Q_1,
            "beta": beta_1,
            "M": M,
            "R": R_M,
            "K": K_M,
            "C": C,
            "d": d,
            "n": n,
            "carrier_outside_support_potential_domain": M > B_p,
            "fiber": source_fiber,
            "state": source_state,
        },
        "h_two_target": {
            "k": k,
            "r": r,
            "s": s,
            "R": R_r,
            "K": K_r,
            "gcd_A_C": g,
            "A_over_gcd": a,
            "A_C": A_C,
            "C": target_C,
            "d": target_d,
            "n": target_n,
            "h": h,
            "checks": cofactor_checks,
            "fiber": target_fiber,
            "state": successor_state,
        },
        "cofactor_normal_form": cofactor_normal_form,
        "local_potential": {"source": source_potential, "target": target_potential},
        "candidate_e1_e5": local_e1_e5,
        "terminal_first": {
            "p_plus_four_factorization": [[factor, exponent] for factor, exponent in p_plus_four_factors],
            "p_plus_four_has_3mod4_factor": bool(p_plus_four_q3),
            "direct_type_i_gap_seven": terminal,
            "status": "terminal_leaf",
        },
        "integration_status": "dedicated_reproducer_only",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified p=60913 h=2 G-G-F high-R non-return r-chart")
        return
    args.output.write_text(json.dumps(result, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
