#!/usr/bin/env python3
"""Verify the relative typed total-cofactor adapter for persistent overflow.

The adapter deliberately consumes, rather than manufactures, a registered
persistent source and a terminal-first miss.  Given those upstream facts, it
recomputes both charts, the complete hit/F/G payload, the identity lift, and
the Type-I CHARGED local-drop ticket.  A target-derived raw parent or an
unregistered transient is rejected before it can be treated as an E1 source.

This is a contract verifier, not a global T6 selector.  Its finite group
operations terminate for every supplied chart, but it does not assert that
every actual reachable state has a registered determinant receipt.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import product
from math import gcd, lcm, prod
from typing import Any

import sympy
from sympy import Matrix, Rational
from sympy.matrices.normalforms import hermite_normal_form
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp


ADAPTER_VERSION = "total_cofactor_typed_projection_v1"
STATE_NORMAL_FORM = "type_i_total_cofactor_charged_v1"


def canonical_digest(value: object) -> str:
    """Return a stable digest for a JSON-compatible proof payload."""
    data = json.dumps(
        value, ensure_ascii=True, sort_keys=True, separators=(",", ":")
    ).encode("ascii")
    return hashlib.sha256(data).hexdigest()


def factorization(value: int) -> tuple[tuple[int, int], ...]:
    """Factor one positive integer and verify its ordered prime-power record."""
    if value < 1:
        raise ValueError("factorization requires a positive integer")
    factors = tuple(
        sorted((int(prime), int(exponent)) for prime, exponent in sympy.factorint(value).items())
    )
    if (
        prod(prime**exponent for prime, exponent in factors) != value
        or any(not sympy.isprime(prime) or exponent < 1 for prime, exponent in factors)
    ):
        raise AssertionError("factorization did not reconstruct into prime powers")
    return factors


def factor_payload(factors: tuple[tuple[int, int], ...]) -> list[list[int]]:
    return [[prime, exponent] for prime, exponent in factors]


def residue(
    factors: tuple[tuple[int, int], ...], vector: tuple[int, ...], modulus: int
) -> int:
    """Evaluate the signed support monomial modulo a coprime chart modulus."""
    if len(factors) != len(vector):
        raise ValueError("factor and exponent-vector lengths differ")
    value = 1
    for (prime, _bound), exponent in zip(factors, vector, strict=True):
        if gcd(prime, modulus) != 1:
            raise AssertionError("K support is not a unit modulo the chart modulus")
        value = value * pow(prime, exponent, modulus) % modulus
    return value


def bounded_hits(
    factors: tuple[tuple[int, int], ...], modulus: int
) -> tuple[tuple[int, ...], ...]:
    """Enumerate the finite centered box in the contract's canonical order."""
    ranges = tuple(range(-bound, bound + 1) for _prime, bound in factors)
    hits = [
        vector
        for vector in product(*ranges)
        if residue(factors, vector, modulus) == modulus - 1
    ]
    return tuple(sorted(hits, key=lambda row: (sum(map(abs, row)), row)))


def component_lattice_hnf(
    generator_logs: list[list[int]], component_orders: list[int]
) -> Matrix:
    """Return the HNF basis for the support subgroup plus component periods."""
    dimension = len(component_orders)
    if not dimension or any(len(row) != dimension for row in generator_logs):
        raise AssertionError("invalid finite-unit coordinate system")
    columns = [*generator_logs]
    columns.extend(
        [
            [component_orders[row] if row == column else 0 for row in range(dimension)]
            for column in range(dimension)
        ]
    )
    lattice = Matrix(
        dimension,
        len(columns),
        lambda row, column: columns[column][row],
    )
    hnf = hermite_normal_form(lattice)
    if hnf.shape != (dimension, dimension) or hnf.det() == 0:
        raise AssertionError("support lattice did not have a full-rank HNF")
    return hnf


def solve_upper_hnf_membership(hnf: Matrix, target: list[int]) -> tuple[bool, list[int] | None]:
    """Solve H*x=target over integers for the canonical upper HNF basis."""
    dimension = len(target)
    if hnf.shape != (dimension, dimension):
        raise AssertionError("HNF dimension mismatch")
    if any(int(hnf[row, column]) for row in range(dimension) for column in range(row)):
        raise AssertionError("expected an upper triangular HNF")
    coordinates = [0] * dimension
    for row in range(dimension - 1, -1, -1):
        diagonal = int(hnf[row, row])
        if diagonal <= 0:
            raise AssertionError("HNF has a nonpositive diagonal")
        numerator = target[row] - sum(
            int(hnf[row, column]) * coordinates[column]
            for column in range(row + 1, dimension)
        )
        if numerator % diagonal:
            return False, None
        coordinates[row] = numerator // diagonal
    return True, coordinates


def unit_group_certificate(
    factors: tuple[tuple[int, int], ...], modulus: int
) -> dict[str, Any]:
    """Coordinate U(modulus) and decide whether the K support reaches -1."""
    modulus_factors = factorization(modulus)
    component_moduli = [prime**exponent for prime, exponent in modulus_factors]
    component_orders = [int(sympy.totient(value)) for value in component_moduli]
    primitive_roots = [int(sympy.primitive_root(value)) for value in component_moduli]
    if any(root <= 0 for root in primitive_roots):
        raise AssertionError("odd prime-power unit component lacks a primitive root")
    target = [order // 2 for order in component_orders]
    if any(
        pow(root, target_log, local_modulus) != local_modulus - 1
        for root, target_log, local_modulus in zip(
            primitive_roots, target, component_moduli, strict=True
        )
    ):
        raise AssertionError("minus-one coordinate did not replay")

    generator_primes = [prime for prime, _exponent in factors]
    logs: list[list[int]] = []
    for prime in generator_primes:
        if gcd(prime, modulus) != 1:
            raise AssertionError("K support must be a unit modulo R")
        row = [
            int(sympy.discrete_log(local_modulus, prime % local_modulus, root))
            for local_modulus, root in zip(component_moduli, primitive_roots, strict=True)
        ]
        if any(
            pow(root, logarithm, local_modulus) != prime % local_modulus
            for root, logarithm, local_modulus in zip(
                primitive_roots, row, component_moduli, strict=True
            )
        ):
            raise AssertionError("discrete logarithm failed to replay a support prime")
        logs.append(row)

    hnf = component_lattice_hnf(logs, component_orders)
    in_subgroup, coordinates = solve_upper_hnf_membership(hnf, target)
    return {
        "component_orders": component_orders,
        "component_moduli": component_moduli,
        "primitive_roots": primitive_roots,
        "generator_primes": generator_primes,
        "generator_log_vectors": logs,
        "target_log_vector_for_minus_one": target,
        "support_lattice_hnf": [
            [int(hnf[row, column]) for column in range(hnf.cols)]
            for row in range(hnf.rows)
        ],
        "target_in_generated_subgroup": in_subgroup,
        "target_lattice_coordinates": coordinates,
    }


def fraction_payload(value: Rational) -> list[int]:
    value = Rational(value)
    return [int(value.p), int(value.q)]


def canonical_g_separator(certificate: dict[str, Any]) -> dict[str, Any]:
    """Build a deterministic exact quotient character from the HNF dual basis."""
    if bool(certificate["target_in_generated_subgroup"]):
        raise ValueError("an F/hit chart has no G separator")
    orders = [int(value) for value in certificate["component_orders"]]
    logs = [[int(value) for value in row] for row in certificate["generator_log_vectors"]]
    target = [int(value) for value in certificate["target_log_vector_for_minus_one"]]
    hnf = Matrix(certificate["support_lattice_hnf"])
    dimension = len(orders)
    if hnf.shape != (dimension, dimension):
        raise AssertionError("separator HNF dimension mismatch")
    inverse = hnf.inv()
    candidates: list[tuple[tuple[Any, ...], tuple[Rational, ...], Rational]] = []
    for row in range(dimension):
        phase_vector = tuple(Rational(inverse[row, column]) for column in range(dimension))
        target_phase = sum(
            (phase_vector[column] * target[column] for column in range(dimension)),
            Rational(0),
        )
        if target_phase.q == 1:
            continue
        if any((orders[column] * phase_vector[column]).q != 1 for column in range(dimension)):
            raise AssertionError("HNF-dual row is not a unit-group character")
        if any(
            sum(
                (phase_vector[column] * generator[column] for column in range(dimension)),
                Rational(0),
            ).q
            != 1
            for generator in logs
        ):
            raise AssertionError("HNF-dual row is not trivial on K support")
        order = lcm(*(int(value.q) for value in phase_vector))
        key = (
            order,
            sum(value % 1 != 0 for value in phase_vector),
            tuple((int(value.p), int(value.q)) for value in phase_vector),
            row,
        )
        candidates.append((key, phase_vector, target_phase))
    if not candidates:
        raise AssertionError("G nonmembership had no separating HNF-dual character")
    _key, phase_vector, target_phase = min(candidates, key=lambda item: item[0])
    target_mod_one = target_phase - sympy.floor(target_phase)
    return {
        "kind": "canonical_hnf_dual_separator_v1",
        "component_orders": orders,
        "phase_vector": [fraction_payload(value) for value in phase_vector],
        "character_order": lcm(*(int(value.q) for value in phase_vector)),
        "generator_phases_integral": True,
        "target_phase": fraction_payload(target_phase),
        "target_phase_mod_one": fraction_payload(target_mod_one),
        "target_separated": True,
    }


def canonical_f_witness(
    certificate: dict[str, Any], factor_count: int
) -> tuple[int, ...]:
    """Recover a deterministic unbounded support vector for an F chart."""
    if not bool(certificate["target_in_generated_subgroup"]):
        raise ValueError("a G chart has no F witness")
    orders = [int(value) for value in certificate["component_orders"]]
    logs = Matrix(certificate["generator_log_vectors"]).T
    target = Matrix([int(value) for value in certificate["target_log_vector_for_minus_one"]])
    diagonal = sympy.diag(*orders)
    congruence_matrix = logs.row_join(-diagonal)
    domain_matrix = DomainMatrix.from_Matrix(
        congruence_matrix, fmt="dense"
    ).convert_to(sympy.ZZ)
    smith_domain, left_domain, right_domain = smith_normal_decomp(domain_matrix)
    smith = smith_domain.to_Matrix()
    left = left_domain.to_Matrix()
    right = right_domain.to_Matrix()
    if left * congruence_matrix * right != smith:
        raise AssertionError("Smith relation reconstruction failed")
    transformed_target = left * target
    coordinates = sympy.zeros(right.cols, 1)
    for row in range(len(orders)):
        diagonal_entry = int(smith[row, row])
        if diagonal_entry == 0 or int(transformed_target[row]) % diagonal_entry:
            raise AssertionError("subgroup membership and Smith preimage disagree")
        coordinates[row] = int(transformed_target[row]) // diagonal_entry
    preimage = right * coordinates
    witness = tuple(int(preimage[index]) for index in range(factor_count))
    for row, order in enumerate(orders):
        value = sum(int(logs[row, column]) * witness[column] for column in range(factor_count))
        if (value - int(target[row])) % order:
            raise AssertionError("Smith F witness did not reconstruct -1")
    return witness


def signed_defect(
    factors: tuple[tuple[int, int], ...], vector: tuple[int, ...]
) -> dict[str, Any]:
    """Record the contract's globally oriented defect relative to the centered box."""
    if len(factors) != len(vector):
        raise ValueError("factor and vector lengths differ")
    minus_exponents = tuple(
        max(-exponent - bound, 0)
        for (_prime, bound), exponent in zip(factors, vector, strict=True)
    )
    plus_exponents = tuple(
        max(exponent - bound, 0)
        for (_prime, bound), exponent in zip(factors, vector, strict=True)
    )

    def payload(exponents: tuple[int, ...]) -> dict[str, Any]:
        terms = [
            [prime, exponent]
            for (prime, _bound), exponent in zip(factors, exponents, strict=True)
            if exponent
        ]
        return {
            "factorization": terms,
            "value": prod(prime**exponent for prime, exponent in terms),
        }

    return {
        "status": "defined",
        "orientation": "canonical_smith_or_centered_vector",
        "D_minus": payload(minus_exponents),
        "D_plus": payload(plus_exponents),
    }


def centered_hit_terminal(
    p: int, R: int, K: int, factors: tuple[tuple[int, int], ...], vector: tuple[int, ...]
) -> dict[str, Any]:
    """Turn one bounded hit into the exact Type-I terminal from the centered-pair card."""
    positive = prod(
        prime ** max(exponent, 0)
        for (prime, _bound), exponent in zip(factors, vector, strict=True)
    )
    negative = prod(
        prime ** max(-exponent, 0)
        for (prime, _bound), exponent in zip(factors, vector, strict=True)
    )
    if not (
        gcd(positive, negative) == 1
        and K % (positive * negative) == 0
        and (positive + negative) % R == 0
    ):
        raise AssertionError("bounded vector did not give a centered terminal pair")
    a, b = sorted((positive, negative))
    mu = (a + b) // R
    c = K // (a * b)
    denominators = (mu * a * c, mu * b * c, p * a * b * c)
    if not (
        mu > 0
        and all(denominator > 0 for denominator in denominators)
        and Fraction(4, p)
        == sum((Fraction(1, denominator) for denominator in denominators), Fraction())
    ):
        raise AssertionError("centered hit did not serialize a Type-I terminal")
    return {
        "kind": "type_i_centered_pair_terminal",
        "centered_pair": [a, b],
        "mu": mu,
        "c": c,
        "egyptian_denominators": list(denominators),
    }


def classify_chart(p: int, R: int, K: int) -> dict[str, Any]:
    """Return the contract-complete hit/F/G payload for one linear Type-I chart."""
    factors = factorization(K)
    hits = bounded_hits(factors, R)
    if hits:
        witness = hits[0]
        return {
            "classification": "hit",
            "factorization": factor_payload(factors),
            "target_fiber": {"status": "nonempty", "witness": list(witness)},
            "signed_defect": signed_defect(factors, witness),
            "certificate_context": {
                "kind": "centered_box_hit",
                "terminal": centered_hit_terminal(p, R, K, factors, witness),
            },
        }

    certificate = unit_group_certificate(factors, R)
    if not bool(certificate["target_in_generated_subgroup"]):
        separator = canonical_g_separator(certificate)
        return {
            "classification": "G",
            "factorization": factor_payload(factors),
            "target_fiber": {
                "status": "empty",
                "emptiness_certificate": separator,
            },
            "signed_defect": {
                "status": "not_applicable",
                "reason": "G_empty_target_fiber",
            },
            "certificate_context": {"kind": "finite_abelian_separator", "data": certificate},
        }

    witness = canonical_f_witness(certificate, len(factors))
    if residue(factors, witness, R) != R - 1:
        raise AssertionError("F witness did not represent the target phase")
    return {
        "classification": "F",
        "factorization": factor_payload(factors),
        "target_fiber": {"status": "nonempty", "witness": list(witness)},
        "signed_defect": signed_defect(factors, witness),
        "certificate_context": {"kind": "smith_relation_witness", "data": certificate},
    }


def build_state(p: int, R: int, A: int, source_tree_scope: str) -> dict[str, Any]:
    """Rebuild every canonical field of one Type-I CHARGED state."""
    if not (p % 24 == 1 and sympy.isprime(p)):
        raise ValueError("a total-cofactor state requires a core prime")
    if R < 3 or R % 4 != 3:
        raise ValueError("linear Type-I chart requires R >= 3 and R == 3 mod 4")
    if not source_tree_scope:
        raise ValueError("source_tree_scope must be nonempty")
    numerator = p * R + 1
    if numerator % 4:
        raise AssertionError("linear chart does not produce integral K")
    K = numerator // 4
    if A <= 0 or K % A:
        raise ValueError("charged support must be a positive divisor of K")
    if R == p:
        raise AssertionError("R == p is incompatible with the required mod-4 classes")
    typed = classify_chart(p, R, K)
    B_p = (p - 1) ** 2 // 4
    core: dict[str, Any] = {
        "adapter_version": ADAPTER_VERSION,
        "equation_target": [4, p],
        "root_prime": p,
        "induction_rank": p,
        "modulus_context": {"R": R, "congruence": "R_eq_3_mod_4"},
        "K_context": {"K": K, "factorization": typed["factorization"]},
        "absorbed_support": A,
        "source_tree_scope": source_tree_scope,
        "state_class": "marked_absorb" if R < p else "overflow",
        "marked_solution_set": "Sol(p)",
        "phase": "TYPEI",
        "protocol": "CHARGED",
        "normal_form": STATE_NORMAL_FORM,
        "typed_classification": typed["classification"],
        "target_fiber": typed["target_fiber"],
        "signed_defect": typed["signed_defect"],
        "certificate_context": typed["certificate_context"],
        "potential_record": {
            "t5_local_rank": [B_p // A, K // A, 0, 0],
            "ticket_family": "LOCAL_DROP",
        },
    }
    return {"state_id": f"state:{canonical_digest(core)}", **core}


def verify_state(state: dict[str, Any]) -> dict[str, Any]:
    """Reject stale typed fields by rebuilding the complete canonical state."""
    rebuilt = build_state(
        int(state["root_prime"]),
        int(state["modulus_context"]["R"]),
        int(state["absorbed_support"]),
        str(state["source_tree_scope"]),
    )
    if state != rebuilt:
        raise ValueError("state content address or typed fields do not replay")
    return rebuilt


def registration(
    state: dict[str, Any], *, parent_receipt_digest: str, terminal_first_digest: str, terminal_first_miss: bool, persistent_queue: bool
) -> dict[str, Any]:
    """Build the upstream E1 precondition consumed by the relative adapter."""
    return {
        "registration_version": ADAPTER_VERSION,
        "source_state_id": state["state_id"],
        "parent_receipt_digest": parent_receipt_digest,
        "terminal_first_digest": terminal_first_digest,
        "terminal_first_miss": terminal_first_miss,
        "persistent_queue": persistent_queue,
    }


def verify_registration(state: dict[str, Any], record: dict[str, Any]) -> None:
    """Require a real upstream registration instead of target-derived provenance."""
    if record.get("registration_version") != ADAPTER_VERSION:
        raise ValueError("registration version mismatch")
    if record.get("source_state_id") != state.get("state_id"):
        raise ValueError("registration does not bind this source state")
    if not record.get("persistent_queue"):
        raise ValueError("transient determinant receipt is not a persistent source")
    if not record.get("parent_receipt_digest"):
        raise ValueError("persistent source lacks a parent receipt digest")
    if not record.get("terminal_first_digest") or not record.get("terminal_first_miss"):
        raise ValueError("terminal-first miss is not registered")


def total_cofactor_target(p: int, A: int) -> tuple[int, int, int, int]:
    """Return (R_A, K_A, d_A, n_A) for the canonical total-cofactor projection."""
    C_A = pow(4 * A, -1, p)
    K_A = A * C_A
    numerator = 4 * K_A - 1
    if numerator % p:
        raise AssertionError("canonical target R is not integral")
    R_A = numerator // p
    d_A = p - C_A
    n_A = 4 * A - R_A
    if not (
        1 <= C_A < p
        and 1 <= d_A < p
        and n_A > 0
        and p * R_A + 1 == 4 * K_A
        and p * n_A == 4 * A * d_A + 1
    ):
        raise AssertionError("canonical total-cofactor target changed")
    return R_A, K_A, d_A, n_A


def verify_transition(
    source: dict[str, Any], record: dict[str, Any], *, M: int, d: int, n: int
) -> dict[str, Any]:
    """Verify the relative E1--E5 total-cofactor dispatch for one source receipt."""
    verify_registration(source, record)
    source = verify_state(source)
    if source["typed_classification"] == "hit":
        raise ValueError("a source centered hit must terminal before cofactor folding")
    p = int(source["root_prime"])
    R = int(source["modulus_context"]["R"])
    K = int(source["K_context"]["K"])
    A = int(source["absorbed_support"])
    if not (
        M > 0
        and 1 <= d < p
        and n > 0
        and M % A == 0
        and p * n == 4 * M * d + 1
        and R == 4 * M - n
        and K == M * (p - d)
    ):
        raise ValueError("determinant receipt does not bind the persistent source chart")
    target_R, target_K, target_d, target_n = total_cofactor_target(p, A)
    target = build_state(p, target_R, A, str(source["source_tree_scope"]))
    source_capacity = K // A
    target_capacity = target_K // A
    quotient, remainder = divmod(source_capacity - target_capacity, p)
    if remainder or quotient < 0:
        raise AssertionError("total-cofactor capacity congruence changed")
    if target["typed_classification"] == "hit":
        return {
            "kind": "terminal_leaf",
            "terminal": target["certificate_context"]["terminal"],
            "source_state_id": source["state_id"],
            "target_state_id": target["state_id"],
            "E1": "registered_persistent_source_and_terminal_first_miss",
            "E2": "canonical_total_cofactor_chart",
            "E3": "source_and_target_retyped_independently",
            "E4": "root_terminal_not_a_recursive_lift",
        }
    if quotient == 0:
        raise ValueError("canonical total-cofactor projection is a nondecreasing stutter")
    source_rank = tuple(int(value) for value in source["potential_record"]["t5_local_rank"])
    target_rank = tuple(int(value) for value in target["potential_record"]["t5_local_rank"])
    if not (
        source_rank[0] == target_rank[0]
        and source_rank[1] > target_rank[1]
        and source_rank[2:] == target_rank[2:]
    ):
        raise AssertionError("T5 CHARGED local rank did not strictly decrease")
    edge_core = {
        "adapter_version": ADAPTER_VERSION,
        "source_state_id": source["state_id"],
        "target_state_id": target["state_id"],
        "determinant": {"M": M, "d": d, "n": n},
        "canonical_target": {
            "R": target_R,
            "K": target_K,
            "d": target_d,
            "n": target_n,
        },
        "source_scope": source["source_tree_scope"],
        "target_scope": target["source_tree_scope"],
        "t5_ticket": "LOCAL_DROP",
        "source_rank": list(source_rank),
        "target_rank": list(target_rank),
        "capacity_quotient_t": quotient,
    }
    return {
        "kind": "relative_verified_edge",
        "edge_id": f"edge:{canonical_digest(edge_core)}",
        "edge": edge_core,
        "source": source,
        "target": target,
        "E1": "registered_persistent_source_and_terminal_first_miss",
        "E2": "canonical_total_cofactor_chart",
        "E3": "content_addressed_independent_retyping",
        "E4": "identity_on_Sol(p)",
        "E5": "TYPEI_CHARGED_LOCAL_DROP",
    }


def fixture_source(A: int, M: int, d: int, n: int, scope: str = "charged_history_only") -> dict[str, Any]:
    """Construct a typed source only for fixed contract controls, not reachability claims."""
    p = 73
    R = 4 * M - n
    state = build_state(p, R, A, scope)
    if int(state["K_context"]["K"]) != M * (p - d):
        raise AssertionError("fixed determinant fixture did not build its source state")
    return state


def verify() -> None:
    """Replay positive and negative contract controls without asserting reachability."""
    f_to_g = fixture_source(3, 45, 15, 37)
    record = registration(
        f_to_g,
        parent_receipt_digest="contract-fixture-parent",
        terminal_first_digest="contract-fixture-miss",
        terminal_first_miss=True,
        persistent_queue=True,
    )
    edge = verify_transition(f_to_g, record, M=45, d=15, n=37)
    if not (
        edge["kind"] == "relative_verified_edge"
        and edge["source"]["typed_classification"] == "F"
        and edge["target"]["typed_classification"] == "G"
        and edge["source"]["source_tree_scope"] == edge["target"]["source_tree_scope"]
        and edge["E5"] == "TYPEI_CHARGED_LOCAL_DROP"
    ):
        raise AssertionError("F-to-G relative adapter control changed")

    g_to_f = fixture_source(22, 220, 18, 217)
    g_record = registration(
        g_to_f,
        parent_receipt_digest="contract-fixture-parent",
        terminal_first_digest="contract-fixture-miss",
        terminal_first_miss=True,
        persistent_queue=True,
    )
    g_edge = verify_transition(g_to_f, g_record, M=220, d=18, n=217)
    if not (
        g_edge["kind"] == "relative_verified_edge"
        and g_edge["source"]["typed_classification"] == "G"
        and g_edge["target"]["typed_classification"] == "F"
    ):
        raise AssertionError("G-to-F relative adapter control changed")

    f_to_hit = fixture_source(5, 40, 26, 57)
    hit_record = registration(
        f_to_hit,
        parent_receipt_digest="contract-fixture-parent",
        terminal_first_digest="contract-fixture-miss",
        terminal_first_miss=True,
        persistent_queue=True,
    )
    terminal = verify_transition(f_to_hit, hit_record, M=40, d=26, n=57)
    if not (
        terminal["kind"] == "terminal_leaf"
        and terminal["terminal"]["egyptian_denominators"] == [22, 110, 4015]
    ):
        raise AssertionError("F-to-hit terminal control changed")

    canonical = build_state(73, 11, 3, "charged_history_only")
    stutter_record = registration(
        canonical,
        parent_receipt_digest="contract-fixture-parent",
        terminal_first_digest="contract-fixture-miss",
        terminal_first_miss=True,
        persistent_queue=True,
    )
    try:
        verify_transition(canonical, stutter_record, M=3, d=6, n=1)
    except ValueError as error:
        if "nondecreasing stutter" not in str(error):
            raise
    else:
        raise AssertionError("canonical stutter was admitted")

    transient_record = dict(record)
    transient_record["persistent_queue"] = False
    try:
        verify_transition(f_to_g, transient_record, M=45, d=15, n=37)
    except ValueError as error:
        if "transient" not in str(error):
            raise
    else:
        raise AssertionError("transient determinant receipt was admitted")

    missing_priority = dict(record)
    missing_priority["terminal_first_miss"] = False
    try:
        verify_transition(f_to_g, missing_priority, M=45, d=15, n=37)
    except ValueError as error:
        if "terminal-first" not in str(error):
            raise
    else:
        raise AssertionError("missing terminal-first miss was admitted")

    print("verified relative total-cofactor typed adapter")
    print("F_to_G", edge["edge"]["source_rank"], "->", edge["edge"]["target_rank"])
    print("G_to_F", g_edge["edge"]["source_rank"], "->", g_edge["edge"]["target_rank"])
    print("F_to_hit", terminal["terminal"]["egyptian_denominators"])
    print("contract-only controls; no actual reachability or T6 totality claim")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused contract controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
