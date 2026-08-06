#!/usr/bin/env python3
"""Verify the p=1201 two-anchor high-carrier r-chart construction."""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import product
from math import gcd, lcm
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-high-r-chart-two-anchor-results.json"


def factorization(value: int) -> list[tuple[int, int]]:
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
    factors = factorization(value)
    return factors == [(value, 1)]


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def canonical_chart(prime: int, support: int) -> tuple[int, int]:
    modulus = 4 * support
    R = (-pow(prime, -1, modulus)) % modulus
    K = (prime * R + 1) // 4
    if not (1 <= R < modulus and K % support == 0):
        raise AssertionError("canonical chart normalization failed")
    return R, K


def canonical_hash(payload: object) -> str:
    return hashlib.sha256(
        json.dumps(
            payload,
            ensure_ascii=True,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("ascii")
    ).hexdigest()


def make_state(
    *,
    prime: int,
    R: int,
    K: int,
    support: int,
    state_class: str,
    fiber_class: str,
    source_tree_scope: str,
) -> dict[str, object]:
    state = {
        "equation_target": [4, prime],
        "R": R,
        "K": K,
        "absorbed_support": support,
        "state_class": state_class,
        "fiber_class": fiber_class,
        "source_tree_scope": source_tree_scope,
    }
    state["state_id"] = "state:" + canonical_hash(state)
    return state


def state_id_is_valid(state: dict[str, object]) -> bool:
    descriptor = {key: value for key, value in state.items() if key != "state_id"}
    return state.get("state_id") == "state:" + canonical_hash(descriptor)


def complete_excess_bundle(value: int, K: int) -> tuple[int, int]:
    Q = 1
    for prime, exponent in factorization(value):
        if exponent > valuation(K, prime):
            Q *= prime**exponent
    if value % Q:
        raise AssertionError("complete bundle did not divide anchor side")
    return Q, value // Q


def high_R_universal_source(prime: int, R: int) -> dict[str, object]:
    K = (prime * R + 1) // 4
    U = prime
    V = R * (prime - 1) - prime
    m = prime - 1
    destination = (U // prime, (V + R) // prime, (m + 1) // prime)
    if not (
        is_prime(prime)
        and prime % 24 == 1
        and R >= 3
        and R % 4 == 3
        and R % prime != 0
        and U + V == R * m
        and gcd(U, V) == 1
        and K % prime != 0
        and valuation(U, prime) > valuation(K, prime)
        and destination == (1, R - 1, 1)
    ):
        raise AssertionError("high-R universal source lemma failed")
    return {
        "R": R,
        "K": K,
        "source": [U, V, m],
        "raw_p_edge": {
            "q": prime,
            "shift": 1,
            "gcd_reduction": 1,
            "destination": list(destination),
        },
    }


def high_R_path_anchored_bundle(
    *,
    prime: int,
    R: int,
    support: int,
) -> dict[str, object]:
    """Verify a high-R raw-source and complete-excess path receipt.

    This adapter replaces the old consequence Q<p with the exact condition
    that p does not divide Q. It proves source/path provenance only; charged
    support still needs a parent ledger.
    """
    source = high_R_universal_source(prime, R)
    K = int(source["K"])
    Q, beta = complete_excess_bundle(R - 1, K)
    M = lcm(support, Q)
    if gcd(prime, 4 * M) != 1:
        raise AssertionError("high-R bundle did not produce a coprime rechart carrier")
    R_M, K_M = canonical_chart(prime, M)
    C = K_M // M
    d = prime - C
    n = 4 * M - R_M
    result_class = "marked_absorb" if R_M < prime else "overflow"
    conditions = {
        "support_divides_parent_K": support > 0 and K % support == 0,
        "complete_excess_nontrivial": Q > 1,
        "anchor_factorization": R - 1 == Q * beta,
        "beta_divides_parent_K": K % beta == 0,
        "bundle_coprime_to_beta": gcd(Q, beta) == 1,
        "bundle_not_dividing_parent_K": K % Q != 0,
        "bundle_below_anchor": Q < R,
        "p_coprime_to_bundle": Q % prime != 0,
        "source_coprime_condition": R % prime != 0,
        "lcm_contains_support": M % support == 0,
        "lcm_contains_bundle": M % Q == 0,
        "strict_support_growth": M // support >= 2,
        "new_carrier_not_in_parent_K": K % M != 0,
        "canonical_chart_changed": R_M != R,
        "canonical_chart_not_equal_p": R_M != prime,
        "canonical_R_mod_4": R_M % 4 == 3,
    }
    if not all(conditions.values()):
        raise AssertionError("high-R path-anchored bundle contract failed")
    rechart: dict[str, object] = {
        "M": M,
        "R": R_M,
        "K": K_M,
        "C": C,
        "result_class": result_class,
    }
    if result_class == "overflow":
        if not (
            C > 0
            and d > 0
            and n > 0
            and prime * n == 4 * M * d + 1
            and R_M == 4 * M - n
        ):
            raise AssertionError("high-R bundle overflow determinant failed")
        rechart.update({"d": d, "n": n})
    else:
        if not (3 <= R_M <= prime - 2 and K_M % M == 0):
            raise AssertionError("high-R bundle marked rechart failed")
    return {
        "adapter": "high_R_path_anchored_bundle_v1",
        "R_domain": "high_R" if R > prime else "core_R",
        "source": source,
        "anchor_node": [1, R - 1, 1],
        "complete_excess_bundle": {"Q": Q, "beta": beta},
        "conditions": conditions,
        "rechart": rechart,
    }


def residue_product(
    modulus: int,
    factors: list[tuple[int, int]],
    vector: tuple[int, ...],
) -> int:
    value = 1
    for (prime, _), exponent in zip(factors, vector):
        value = value * pow(prime, exponent, modulus) % modulus
    return value


def canonical_residue_witness(
    modulus: int,
    factors: list[tuple[int, int]],
    target: int,
    upper_l1: int,
) -> tuple[int, ...]:
    """Find the minimum-L1, then lexicographically first, unrestricted witness."""
    if upper_l1 < 0 or any(gcd(prime, modulus) != 1 for prime, _ in factors):
        raise AssertionError("canonical witness input is not a unit problem")
    split = max(1, len(factors) // 2)
    left_factors = factors[:split]
    right_factors = factors[split:]
    exponent_range = range(-upper_l1, upper_l1 + 1)
    right_best: dict[int, tuple[int, tuple[int, ...]]] = {}
    for right_vector in product(exponent_range, repeat=len(right_factors)):
        right_cost = sum(abs(value) for value in right_vector)
        if right_cost > upper_l1:
            continue
        residue = residue_product(modulus, right_factors, right_vector)
        candidate = (right_cost, right_vector)
        if residue not in right_best or candidate < right_best[residue]:
            right_best[residue] = candidate
    best: tuple[int, tuple[int, ...]] | None = None
    for left_vector in product(exponent_range, repeat=len(left_factors)):
        left_cost = sum(abs(value) for value in left_vector)
        if left_cost > upper_l1:
            continue
        left_residue = residue_product(modulus, left_factors, left_vector)
        needed = target * pow(left_residue, -1, modulus) % modulus
        right = right_best.get(needed)
        if right is None:
            continue
        candidate = (left_cost + right[0], left_vector + right[1])
        if best is None or candidate < best:
            best = candidate
    if best is None:
        raise AssertionError("declared witness bound did not reach the target")
    return best[1]


def signed_defect(
    factors: list[tuple[int, int]],
    witness: tuple[int, ...],
) -> dict[str, object]:
    minus = [max(-value - budget, 0) for value, (_prime, budget) in zip(witness, factors)]
    plus = [max(value - budget, 0) for value, (_prime, budget) in zip(witness, factors)]

    def render(exponents: list[int]) -> dict[str, object]:
        value = 1
        rendered: list[list[int]] = []
        for (prime, _budget), exponent in zip(factors, exponents):
            value *= prime**exponent
            if exponent:
                rendered.append([prime, exponent])
        return {"factorization": rendered, "value": value}

    return {
        "orientation": "canonical_minimum_l1_then_lexicographic",
        "D_minus": render(minus),
        "D_plus": render(plus),
    }


def residue_witness(
    modulus: int,
    factors: list[tuple[int, int]],
    witness: tuple[int, ...],
) -> dict[str, object]:
    if len(factors) != len(witness):
        raise AssertionError("witness dimension mismatch")
    value = residue_product(modulus, factors, witness)
    box_hit = False
    ranges = [range(-exponent, exponent + 1) for _, exponent in factors]
    for vector in product(*ranges):
        candidate = residue_product(modulus, factors, vector)
        if candidate == (-1) % modulus:
            box_hit = True
            break
    if value != (-1) % modulus or box_hit:
        raise AssertionError("F witness or finite box classification failed")
    canonical_witness = canonical_residue_witness(
        modulus,
        factors,
        (-1) % modulus,
        sum(abs(value) for value in witness),
    )
    if canonical_witness != witness:
        raise AssertionError("F witness was not canonical")
    return {
        "factors": [[prime, exponent] for prime, exponent in factors],
        "witness": list(witness),
        "witness_residue": value,
        "witness_l1": sum(abs(value) for value in witness),
        "witness_policy": "minimum_l1_then_lexicographic",
        "finite_box_hit": box_hit,
        "classification": "F",
        "signed_defect": signed_defect(factors, witness),
    }


def legendre_symbol(value: int, modulus: int) -> int:
    """Return the quadratic character modulo an odd prime."""
    if modulus <= 2 or not is_prime(modulus) or value % modulus == 0:
        raise AssertionError("Legendre character requires a nonzero unit modulo a prime")
    residue = pow(value % modulus, (modulus - 1) // 2, modulus)
    if residue == 1:
        return 1
    if residue == modulus - 1:
        return -1
    raise AssertionError("Euler criterion returned a non-quadratic residue")


def legendre_g_fiber(R: int, K: int, conductor: int) -> dict[str, object]:
    """Build a G certificate from a quadratic quotient of the chart modulus."""
    factors = factorization(K)
    support_values = {
        str(prime): legendre_symbol(prime, conductor)
        for prime, _exponent in factors
    }
    conditions = {
        "conductor_divides_modulus": R % conductor == 0,
        "support_is_character_trivial": all(value == 1 for value in support_values.values()),
        "minus_one_is_character_nontrivial": legendre_symbol(-1, conductor) == -1,
    }
    if not all(conditions.values()):
        raise AssertionError("Legendre data did not certify a G fiber")
    return {
        "classification": "G",
        "support_factorization": [[prime, exponent] for prime, exponent in factors],
        "target_in_generated_subgroup": False,
        "separator": {
            "kind": "Legendre",
            "modulus": conductor,
            "support_values": support_values,
            "minus_one": legendre_symbol(-1, conductor),
        },
        "signed_defect": {"status": "not_applicable", "reason": "G_support_separator"},
        "conditions": conditions,
    }


def fiber_certificate_is_valid(
    R: int,
    K: int,
    fiber: dict[str, object],
) -> bool:
    """Recheck an F or Legendre-G certificate against its chart."""
    classification = fiber.get("classification")
    if classification == "F":
        witness = fiber.get("witness")
        if not isinstance(witness, list) or not all(isinstance(value, int) for value in witness):
            return False
        try:
            return residue_witness(R, factorization(K), tuple(witness)) == fiber
        except AssertionError:
            return False
    if classification == "G":
        separator = fiber.get("separator")
        if not isinstance(separator, dict) or separator.get("kind") != "Legendre":
            return False
        conductor = separator.get("modulus")
        if not isinstance(conductor, int):
            return False
        try:
            return legendre_g_fiber(R, K, conductor) == fiber
        except AssertionError:
            return False
    return False


def same_chart_fiber_identity_lift(
    R: int,
    K: int,
    fiber: dict[str, object],
) -> bool:
    """A fixed chart preserves a rechecked F/G certificate under identity lift."""
    return fiber_certificate_is_valid(R, K, fiber)


def same_chart_parent_replay(
    *,
    prime: int,
    B_p: int,
    root_bundle: dict[str, object],
    fiber: dict[str, object],
) -> dict[str, object]:
    """Serialize the concrete 1-to-M same-chart parent used by the high-R path."""
    rechart = root_bundle.get("rechart")
    conditions = root_bundle.get("conditions")
    if not isinstance(rechart, dict) or not isinstance(conditions, dict):
        raise AssertionError("root bundle receipt shape changed")
    M = int(rechart["M"])
    R = int(rechart["R"])
    K = int(rechart["K"])
    C = int(rechart["C"])
    d = int(rechart["d"])
    n = int(rechart["n"])
    scope = "fresh_source_tree_only"
    fiber_class = str(fiber.get("classification", ""))
    source_state = make_state(
        prime=prime,
        R=R,
        K=K,
        support=1,
        state_class="overflow",
        fiber_class=fiber_class,
        source_tree_scope=scope,
    )
    successor_state = make_state(
        prime=prime,
        R=R,
        K=K,
        support=M,
        state_class="overflow",
        fiber_class=fiber_class,
        source_tree_scope=scope,
    )
    source_potential = B_p
    successor_potential = B_p // M
    root_entry_valid = bool(
        root_bundle.get("R_domain") == "core_R"
        and all(bool(value) for value in conditions.values())
        and int(root_bundle["source"]["R"]) < prime
        and M >= 2
        and M <= B_p
        and R > prime
        and K == M * C
        and prime * n == 4 * M * d + 1
    )
    checks = {
        "root_entry": root_entry_valid,
        "source_state": state_id_is_valid(source_state)
        and source_state["absorbed_support"] == 1
        and K % int(source_state["absorbed_support"]) == 0,
        "same_chart_successor": state_id_is_valid(successor_state)
        and successor_state["R"] == source_state["R"]
        and successor_state["K"] == source_state["K"]
        and successor_state["absorbed_support"] == M
        and K % M == 0,
        "identity_lift": same_chart_fiber_identity_lift(R, K, fiber),
        "strict_support_potential": successor_potential < source_potential,
        "scope_propagated": source_state["source_tree_scope"]
        == successor_state["source_tree_scope"]
        == scope,
    }
    if not all(checks.values()):
        raise AssertionError("same-chart parent replay failed")
    receipt = {
        "certificate_type": "overflow_same_chart_support_promotion",
        "normal_form_replay_adapter": "high_r_same_chart_parent_replay_v1",
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
        "potential": {"source": source_potential, "successor": successor_potential},
    }
    receipt["edge_id"] = "edge:" + canonical_hash(
        {"source": source_state, "successor": successor_state}
    )
    return receipt


def verify_charged_parent_replay(
    parent: dict[str, object],
    anchor_state: dict[str, object],
) -> bool:
    source = parent.get("source_state")
    successor = parent.get("successor_state")
    checks = parent.get("checks")
    fiber = parent.get("fiber_certificate")
    marked_solution_set = parent.get("marked_solution_set")
    if not (
        isinstance(source, dict)
        and isinstance(successor, dict)
        and isinstance(checks, dict)
        and isinstance(fiber, dict)
        and isinstance(marked_solution_set, dict)
    ):
        return False
    equation_target = source.get("equation_target")
    expected_edge_id = "edge:" + canonical_hash({"source": source, "successor": successor})
    return bool(
        parent.get("certificate_type") == "overflow_same_chart_support_promotion"
        and parent.get("normal_form_replay_adapter") == "high_r_same_chart_parent_replay_v1"
        and parent.get("edge_id") == expected_edge_id
        and parent.get("selector_status") == "verified_edge"
        and parent.get("recursive_edge_eligible") is True
        and parent.get("e1_e5") == {f"E{index}": True for index in range(1, 6)}
        and all(bool(value) for value in checks.values())
        and state_id_is_valid(source)
        and state_id_is_valid(successor)
        and same_chart_fiber_identity_lift(int(source["R"]), int(source["K"]), fiber)
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


def verify_cofactor_r_chart_normal_form(
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
    support_quotient = support // gcd(support, C)
    target_C = r // support_quotient
    target_d = prime - target_C
    target_n = 4 * cofactor_support - R_r
    source_ok = bool(
        state_id_is_valid(source_state)
        and source_state.get("equation_target") == [4, prime]
        and source_state.get("R") == R_M
        and source_state.get("K") == K_M
        and source_state.get("absorbed_support") == support
        and source_state.get("state_class") == "overflow"
        and source_state.get("fiber_class") == source_fiber.get("classification")
        and fiber_certificate_is_valid(R_M, K_M, source_fiber)
        and R_M > prime
        and M % support == 0
        and canonical_chart(prime, M) == (R_M, K_M)
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
        state_id_is_valid(successor_state)
        and successor_state.get("equation_target") == [4, prime]
        and successor_state.get("R") == R_r
        and successor_state.get("K") == K_r
        and successor_state.get("absorbed_support") == cofactor_support
        and successor_state.get("state_class") == "overflow"
        and successor_state.get("fiber_class") == successor_fiber.get("classification")
        and fiber_certificate_is_valid(R_r, K_r, successor_fiber)
        and R_r > prime
        and canonical_chart(prime, cofactor_support) == (R_r, K_r)
        and target_C > 0
        and target_d > 0
        and target_n > 0
        and K_r == cofactor_support * target_C
        and prime * target_n == 4 * cofactor_support * target_d + 1
        and R_r == 4 * cofactor_support - target_n
    )
    scope_ok = source_state.get("source_tree_scope") == successor_state.get(
        "source_tree_scope"
    ) == "fresh_source_tree_only"
    checks = {
        "source_state": source_ok,
        "construction": construction_ok,
        "successor_state": successor_ok,
        "source_tree_scope": scope_ok,
        "parent_ledger": charged_parent_replayed,
    }
    checks["passed"] = all(checks.values())
    return checks


def same_anchor_bundle_reuse_exhaustion(
    *,
    prime: int,
    anchor_R: int,
    anchor_K: int,
    support: int,
    Q: int,
    first_rechart: dict[str, object],
    successor_support: int,
) -> dict[str, object]:
    """Prove that a same-anchor cofactor return cannot pay a second support rise.

    If the first cofactor target returns to the fixed high anchor, its support
    is lcm(A, C). Reusing the same complete-excess bundle gives
    lcm(lcm(A, C), Q) = lcm(M, C), so it divides the already constructed
    K_M = M*C. The canonical overflow chart is therefore unchanged and its
    new cofactor divides the charged support.
    """
    M = int(first_rechart["M"])
    R_M = int(first_rechart["R"])
    K_M = int(first_rechart["K"])
    C = int(first_rechart["C"])
    d = int(first_rechart["d"])
    expected_support = lcm(support, C)
    first_conditions = {
        "anchor_support_divides_K": support > 0 and anchor_K % support == 0,
        "first_carrier_is_bundle_lcm": M == lcm(support, Q),
        "first_canonical_overflow": canonical_chart(prime, M) == (R_M, K_M)
        and K_M == M * C
        and R_M > prime
        and prime * (4 * M - R_M) == 4 * M * d + 1,
        "first_cofactor_support": successor_support == expected_support,
        "first_target_returns_anchor": canonical_chart(
            prime, successor_support
        )
        == (anchor_R, anchor_K),
    }
    if not all(first_conditions.values()):
        raise AssertionError("same-anchor reuse input contract failed")
    M_next = lcm(successor_support, Q)
    expected_M_next = lcm(M, C)
    R_next, K_next = canonical_chart(prime, M_next)
    C_next = K_next // M_next
    d_next = prime - C_next
    n_next = 4 * M_next - R_next
    k_next, r_next = divmod(M_next, prime)
    s_numerator = 4 * r_next * d_next + 1
    if s_numerator % prime:
        raise AssertionError("reuse r-chart s was not integral")
    s_next = s_numerator // prime
    R_r_next = 4 * r_next - s_next
    K_r_next = r_next * C_next
    g_next = gcd(successor_support, C_next)
    a_next = successor_support // g_next
    cofactor_support_next = lcm(successor_support, C_next)
    reuse_conditions = {
        "second_carrier_lcm_identity": M_next == expected_M_next,
        "second_carrier_divides_first_K": K_M % M_next == 0,
        "canonical_chart_is_fixed": (R_next, K_next) == (R_M, K_M),
        "cofactor_is_gcd": C_next == gcd(M, C),
        "second_cofactor_is_already_absorbed": successor_support % C_next == 0,
        "second_cofactor_support_is_fixed": cofactor_support_next
        == successor_support,
        "overflow_determinant": d_next > 0
        and n_next > 0
        and prime * n_next == 4 * M_next * d_next + 1,
        "formal_r_chart": r_next > 0
        and canonical_chart(prime, r_next) == (R_r_next, K_r_next),
    }
    if not all(reuse_conditions.values()):
        raise AssertionError("same-anchor reuse exhaustion theorem failed")
    support_gate = r_next % a_next == 0
    return {
        "lemma": "same_anchor_complete_excess_one_shot_exhaustion_v1",
        "first_conditions": first_conditions,
        "reuse_conditions": reuse_conditions,
        "first": {
            "A": support,
            "Q": Q,
            "M": M,
            "R_M": R_M,
            "K_M": K_M,
            "C": C,
            "A_next": successor_support,
        },
        "second": {
            "M": M_next,
            "R_M": R_next,
            "K_M": K_next,
            "C": C_next,
            "d": d_next,
            "n": n_next,
            "k": k_next,
            "r": r_next,
            "s": s_next,
            "R_r": R_r_next,
            "K_r": K_r_next,
            "gcd_A_C": g_next,
            "A_over_gcd": a_next,
            "A_C": cofactor_support_next,
            "support_gate": support_gate,
            "formal_target_support_wall": {
                "K_r_below_current_support": K_r_next < successor_support,
                "all_legal_supports_below_current_if_true": K_r_next
                < successor_support,
            },
        },
        "conclusion": {
            "strict_support_growth": cofactor_support_next > successor_support,
            "same_anchor_reuse_exhausted": True,
            "reason": (
                "the second cofactor divides the already charged support, so a "
                "same-bundle cofactor reuse cannot pay a second strict support step"
            ),
        },
    }


def type_i_terminal_from_formal_chart(
    *,
    prime: int,
    formal_R: int,
    formal_K: int,
    gap: int,
    a: int,
    b: int,
    box_vector: tuple[int, ...],
) -> dict[str, object]:
    """Recover and verify a direct Type I terminal from a formal low-chart hit."""
    x_numerator = prime + gap
    if (
        prime % 4 != 1
        or gap % 4 != 3
        or not 3 <= gap <= prime - 2
        or x_numerator % 4
        or gcd(a, b) != 1
    ):
        raise AssertionError("Type I terminal input is invalid")
    x = x_numerator // 4
    if x % (a * b):
        raise AssertionError("Type I normal form did not divide x")
    c = x // (a * b)
    h_numerator = b * prime + a
    if h_numerator % gap:
        raise AssertionError("Type I normal form gap condition failed")
    h = h_numerator // gap
    K = b * c * h
    target_divisor = b * b * c
    y = a * c * h
    z = prime * K
    factors = factorization(formal_K)
    if len(factors) != len(box_vector):
        raise AssertionError("formal chart box witness dimension changed")
    box_residue = residue_product(formal_R, factors, box_vector)
    conditions = {
        "formal_chart": prime * formal_R + 1 == 4 * formal_K,
        "normal_form": prime == 4 * a * b * c - gap
        and gap * formal_R == 4 * b * b * c + 1
        and K == formal_K,
        "box_hit": all(
            -exponent <= value <= exponent
            for value, (_factor, exponent) in zip(box_vector, factors)
        )
        and box_residue == (-1) % formal_R,
        "target_divisor": x * x % target_divisor == 0
        and target_divisor % formal_R == (-pow(4, -1, formal_R)) % formal_R,
        "unit_fraction_identity": 4 * x * y * z
        == prime * (y * z + x * z + x * y),
    }
    if not all(conditions.values()):
        raise AssertionError("formal low-chart Type I terminal failed")
    return {
        "certificate_type": "type_i_normal_form_terminal",
        "selector_status": "terminal_leaf",
        "recursive_edge_eligible": False,
        "formal_chart": {"R": formal_R, "K": formal_K},
        "formal_box_hit": {
            "factors": [[factor, exponent] for factor, exponent in factors],
            "vector": list(box_vector),
            "residue": box_residue,
            "target_divisor": target_divisor,
        },
        "normal_form": {"gap": gap, "A": a, "B": b, "C": c, "H": h, "K": K},
        "denominators": {"x": x, "y": y, "z": z},
        "conditions": conditions,
    }


def build_result() -> dict[str, object]:
    prime = 1201
    B_p = (prime - 1) ** 2 // 4
    R_0 = 987
    K_0 = (prime * R_0 + 1) // 4
    if not (
        is_prime(prime)
        and prime % 24 == 1
        and 3 <= R_0 <= prime - 2
        and K_0 == 296_347
        and is_prime(K_0)
    ):
        raise AssertionError("core state changed")
    root_bundle = high_R_path_anchored_bundle(
        prime=prime,
        R=R_0,
        support=1,
    )
    root_rechart = root_bundle["rechart"]
    M_0 = int(root_rechart["M"])
    R_1 = int(root_rechart["R"])
    K_1 = int(root_rechart["K"])
    Q_0 = int(root_bundle["complete_excess_bundle"]["Q"])
    beta_0 = int(root_bundle["complete_excess_bundle"]["beta"])
    if not (
        (Q_0, beta_0, M_0, R_1, K_1) == (986, 1, 986, 1839, 552_160)
        and root_rechart["result_class"] == "overflow"
        and R_1 > prime
        and K_1 % M_0 == 0
        and M_0 <= B_p
    ):
        raise AssertionError("first anchor overflow changed")
    anchor_fiber = residue_witness(
        R_1,
        factorization(K_1),
        (0, 0, -2, 2, -3),
    )
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
        raise AssertionError("same-chart charged parent did not replay")
    charged_support = M_0
    if not (
        high_anchor_state["R"] == R_1
        and high_anchor_state["K"] == K_1
        and high_anchor_state["absorbed_support"] == charged_support
        and high_anchor_state["source_tree_scope"] == "fresh_source_tree_only"
    ):
        raise AssertionError("charged high-R anchor state changed")
    high_bundle = high_R_path_anchored_bundle(
        prime=prime,
        R=R_1,
        support=charged_support,
    )
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
        (Q_1, beta_1) == (919, 2)
        and (M, R_M, K_M, C, d, n, k, r)
        == (906_134, 2_873_071, 862_639_568, 952, 249, 751_465, 754, 580)
        and M > B_p
        and prime * n == 4 * M * d + 1
    ):
        raise AssertionError("second anchor overflow changed")
    g = gcd(charged_support, C)
    a = charged_support // g
    A_C = lcm(charged_support, C)
    s_numerator = 4 * r * d + 1
    if s_numerator % prime:
        raise AssertionError("r-chart s was not integral")
    s = s_numerator // prime
    R_r = 4 * r - s
    K_r = r * C
    C_target = r // a
    d_target = prime - C_target
    n_target = 4 * A_C - R_r
    if not (
        (g, a, A_C, s, R_r, K_r, C_target, d_target, n_target)
        == (34, 29, 27_608, 481, 1839, 552_160, 20, 1181, 108_593)
        and r % a == 0
        and canonical_chart(prime, A_C) == (R_r, K_r)
        and K_r == A_C * C_target
        and prime * n_target == 4 * A_C * d_target + 1
    ):
        raise AssertionError("cofactor r-chart normal form changed")
    source_fiber = residue_witness(
        R_M,
        factorization(K_M),
        (-2, 1, 19, 1, -13),
    )
    target_fiber = anchor_fiber
    if (R_r, K_r) != (R_1, K_1):
        raise AssertionError("r-chart target did not return to the high anchor chart")
    source_state = make_state(
        prime=prime,
        R=R_M,
        K=K_M,
        support=charged_support,
        state_class="overflow",
        fiber_class=str(source_fiber["classification"]),
        source_tree_scope="fresh_source_tree_only",
    )
    successor_state = make_state(
        prime=prime,
        R=R_r,
        K=K_r,
        support=A_C,
        state_class="overflow",
        fiber_class=str(target_fiber["classification"]),
        source_tree_scope="fresh_source_tree_only",
    )
    cofactor_normal_form = verify_cofactor_r_chart_normal_form(
        prime=prime,
        support=charged_support,
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
        charged_parent_replayed=verify_charged_parent_replay(
            parent_replay, high_anchor_state
        ),
    )
    reuse_exhaustion = same_anchor_bundle_reuse_exhaustion(
        prime=prime,
        anchor_R=R_1,
        anchor_K=K_1,
        support=charged_support,
        Q=Q_1,
        first_rechart=high_rechart,
        successor_support=A_C,
    )
    reuse_second = reuse_exhaustion["second"]
    reuse_conclusion = reuse_exhaustion["conclusion"]
    if not isinstance(reuse_second, dict) or not isinstance(reuse_conclusion, dict):
        raise AssertionError("same-anchor reuse receipt shape changed")
    if not (
        (
            reuse_second["M"],
            reuse_second["R_M"],
            reuse_second["K_M"],
            reuse_second["C"],
            reuse_second["d"],
            reuse_second["n"],
            reuse_second["k"],
            reuse_second["r"],
            reuse_second["s"],
            reuse_second["R_r"],
            reuse_second["K_r"],
            reuse_second["gcd_A_C"],
            reuse_second["A_over_gcd"],
            reuse_second["A_C"],
        )
        == (
            25_371_752,
            2_873_071,
            862_639_568,
            34,
            1_167,
            98_613_937,
            21_125,
            627,
            2_437,
            71,
            21_318,
            34,
            812,
            27_608,
        )
        and reuse_second["support_gate"] is False
        and reuse_second["formal_target_support_wall"]
        == {
            "K_r_below_current_support": True,
            "all_legal_supports_below_current_if_true": True,
        }
        and reuse_conclusion["strict_support_growth"] is False
    ):
        raise AssertionError("same-anchor reuse exhaustion data changed")
    formal_terminal = type_i_terminal_from_formal_chart(
        prime=prime,
        formal_R=int(reuse_second["R_r"]),
        formal_K=int(reuse_second["K_r"]),
        gap=1_043,
        a=1,
        b=33,
        box_vector=(-1, 1, 1, 0, -1),
    )
    if formal_terminal["denominators"] != {
        "x": 561,
        "y": 646,
        "z": 25_602_918,
    }:
        raise AssertionError("formal low-chart Type I terminal changed")
    source_potential = B_p // charged_support
    target_potential = B_p // A_C
    if not (
        source_potential == 365
        and target_potential == 13
        and target_potential < source_potential
        and cofactor_normal_form["passed"]
    ):
        raise AssertionError("local support potential changed")
    local_e1_e5 = {
        "E1": bool(
            all(bool(value) for value in root_bundle["conditions"].values())
            and verify_charged_parent_replay(parent_replay, high_anchor_state)
            and all(bool(value) for value in high_bundle["conditions"].values())
        ),
        "E2": bool(
            cofactor_normal_form["construction"]
            and canonical_chart(prime, A_C) == (R_r, K_r)
        ),
        "E3": cofactor_normal_form["passed"],
        "E4": bool(
            source_fiber["classification"] == "F"
            and target_fiber["classification"] == "F"
            and source_fiber.get("signed_defect")
            and target_fiber.get("signed_defect")
        ),
        "E5": target_potential < source_potential,
    }
    if local_e1_e5 != {f"E{index}": True for index in range(1, 6)}:
        raise AssertionError("two-anchor local E1-E5 contract failed")
    e1_e5 = dict(local_e1_e5)
    e1_e5["E5"] = False
    p_plus_four_factors = factorization(prime + 4)
    direct_gap_candidates = [
        factor for factor, _exponent in p_plus_four_factors if factor % 4 == 3
    ]
    if direct_gap_candidates:
        raise AssertionError("p=1201 p+4 terminal diagnostic changed")
    return {
        "schema_version": 1,
        "certificate_type": "type_i_two_anchor_high_r_chart_v1",
        "selector_status": "candidate_transition",
        "recursive_edge_eligible": False,
        "proof_boundary": (
            "the dedicated high-R adapter proves the local source/path and parent replay; "
            "same-anchor bundle reuse is exhausted after one strict support step, and "
            "the p=1201 formal low chart supplies a direct Type I terminal; a global "
            "non-resetting phase rank is still absent for the general branch"
        ),
        "e1_e5": e1_e5,
        "local_e1_e5": local_e1_e5,
        "missing_conditions": ["global_nonresetting_phase_rank"],
        "prime": prime,
        "B_p": B_p,
        "core_anchor": root_bundle,
        "first_overflow": {
            "M": M_0,
            "R": R_1,
            "K": K_1,
            "C": root_rechart["C"],
            "d": root_rechart["d"],
            "n": root_rechart["n"],
            "fiber": anchor_fiber,
        },
        "same_chart_parent_replay": parent_replay,
        "high_R_anchor": high_bundle,
        "source_overflow": {
            "A": charged_support,
            "M": M,
            "R": R_M,
            "K": K_M,
            "C": C,
            "d": d,
            "n": n,
            "k": k,
            "r": r,
            "fiber": source_fiber,
            "state": source_state,
        },
        "r_chart_target": {
            "A": A_C,
            "R": R_r,
            "K": K_r,
            "C": C_target,
            "d": d_target,
            "n": n_target,
            "fiber": target_fiber,
            "state": successor_state,
        },
        "cofactor_normal_form": cofactor_normal_form,
        "same_anchor_bundle_reuse_exhaustion": reuse_exhaustion,
        "local_potential": {"source": source_potential, "target": target_potential},
        "terminal_first_diagnostic": {
            "p_plus_four_factorization": [
                [factor, exponent] for factor, exponent in p_plus_four_factors
            ],
            "p_plus_four_direct_gap_candidates": direct_gap_candidates,
            "formal_low_chart_type_i_terminal": formal_terminal,
            "preempts_high_r_candidate_for_p1201": True,
            "does_not_rule_out_other_certificates": True,
        },
        "terminal_first_status": "terminal_leaf",
        "integration_status": "dedicated_reproducer_only",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified p=1201 two-anchor high r-chart")
        return
    args.output.write_text(json.dumps(result, ensure_ascii=True, indent=2) + "\n")
    print(args.output)


if __name__ == "__main__":
    main()
