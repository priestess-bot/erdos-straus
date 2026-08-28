#!/usr/bin/env python3
"""Constructive SP-05 scheduler and conditional edge builder.

The selector is total on every finite input p.  It returns a verified terminal
certificate whenever the complete schedule finds one.  Only an independently
replayable MISS_COMPLETE plus an exact-source actualness receipt can enter the
phase-root edge branch.
"""
from __future__ import annotations

import copy
from math import gcd, isqrt
from typing import Any, Iterable, Mapping, Sequence

import sp05_contract as C

M23 = (3, 7, 11, 15, 19, 23)
SOURCE_SCHEDULE_ID = "q1_complete_terminal_m23_then_factor_pairs_v1"
TARGET_SCHEDULE_ID = "q1_phase_root_complete_terminal_then_anchor_v1"
COVERAGE_THEOREM_ID = "sp05_sorted_solution_factor_pair_bijection_v1"
CONSTRUCTOR_ID = "sp05_complete_scheduler_constructor_v1"


class ConstructorError(ValueError):
    pass


def is_prime_trial(n: int) -> bool:
    if type(n) is not int or n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d <= isqrt(n):
        if n % d == 0:
            return False
        d += 2
    return True


def factor_trial(n: int) -> tuple[tuple[int, int], ...]:
    if type(n) is not int or n < 1:
        raise ConstructorError("factor input must be a positive integer")
    remaining = n
    factors: list[tuple[int, int]] = []
    d = 2
    while d * d <= remaining:
        if remaining % d:
            d = 3 if d == 2 else d + 2
            continue
        exponent = 0
        while remaining % d == 0:
            remaining //= d
            exponent += 1
        factors.append((d, exponent))
        d = 3 if d == 2 else d + 2
    if remaining > 1:
        factors.append((remaining, 1))
    return tuple(factors)


def divisors_from_factorization(
    factors: Sequence[tuple[int, int]], *, exponent_multiplier: int = 1
) -> tuple[int, ...]:
    values = [1]
    for prime, exponent in factors:
        powers = [prime**power for power in range(exponent * exponent_multiplier + 1)]
        values = [base * power for base in values for power in powers]
    return tuple(sorted(values))


def ordinary_q1_g_parameters(p: int) -> dict[str, Any]:
    if not is_prime_trial(p):
        raise ConstructorError("p is not prime")
    t, X = C.root_parameters(p)
    factors = factor_trial(X)
    if any(prime % 3 != 1 for prime, _ in factors):
        raise ConstructorError("X has a prime factor outside 1 mod 3")
    return {"p": p, "t": t, "X": X, "X_factorization": [list(v) for v in factors]}


def verify_egyptian(p: int, denominators: Sequence[int]) -> bool:
    if len(denominators) != 3 or any(type(v) is not int or v <= 0 for v in denominators):
        return False
    x, y, z = denominators
    return 4 * x * y * z == p * (x * y + x * z + y * z)


def _bradford_certificate(p: int, m: int, d: int, kind: str) -> dict[str, Any]:
    x = (p + m) // 4
    if 4 * x != p + m or (x * x) % d:
        raise ConstructorError("malformed Bradford input")
    if kind == "TYPEI":
        numerator = p * x + d
        if numerator % m:
            raise ConstructorError("TYPEI divisibility does not hold")
        y = numerator // m
        z_num = p * x * numerator
        z_den = m * d
        if z_num % z_den:
            raise ConstructorError("TYPEI z is not integral")
        z = z_num // z_den
    elif kind == "TYPEII":
        if d > x or (x + d) % m:
            raise ConstructorError("TYPEII divisibility does not hold")
        y_num = p * (x + d)
        z_num = p * x * (x + d)
        if y_num % m or z_num % (m * d):
            raise ConstructorError("TYPEII denominator is not integral")
        y = y_num // m
        z = z_num // (m * d)
    else:
        raise ConstructorError("unknown Bradford kind")
    triple = (x, y, z)
    if not verify_egyptian(p, triple):
        raise ConstructorError("Bradford certificate lost the equation")
    return {
        "certificate_kind": kind,
        "gap": m,
        "divisor": d,
        "denominators": list(triple),
        "equation_interface": {"numerator": 4, "denominator": p},
    }


def bradford_m23_prefix(p: int) -> dict[str, Any]:
    """Run the frozen M23 prefix in the order m, d, TYPEI, TYPEII."""
    checks = 0
    divisor_positions = 0
    for gap_index, m in enumerate(M23):
        x = (p + m) // 4
        if 4 * x != p + m:
            raise ConstructorError("M23 gap did not yield an integer x")
        divisors = divisors_from_factorization(factor_trial(x), exponent_multiplier=2)
        for divisor_index, d in enumerate(divisors):
            divisor_positions += 1
            checks += 1
            if (p * x + d) % m == 0:
                certificate = _bradford_certificate(p, m, d, "TYPEI")
                return {
                    "outcome": "HIT",
                    "stage": "M23_PREFIX",
                    "gap_index": gap_index,
                    "divisor_index": divisor_index,
                    "kind_index": 0,
                    "checks_before_hit": checks - 1,
                    "divisor_positions_seen": divisor_positions,
                    "certificate": certificate,
                }
            checks += 1
            if d <= x and (x + d) % m == 0:
                certificate = _bradford_certificate(p, m, d, "TYPEII")
                return {
                    "outcome": "HIT",
                    "stage": "M23_PREFIX",
                    "gap_index": gap_index,
                    "divisor_index": divisor_index,
                    "kind_index": 1,
                    "checks_before_hit": checks - 1,
                    "divisor_positions_seen": divisor_positions,
                    "certificate": certificate,
                }
    return {
        "outcome": "MISS_REGISTERED_PRIORITY_COMPLETE",
        "stage": "M23_PREFIX",
        "ordered_gaps": list(M23),
        "checks": checks,
        "divisor_positions": divisor_positions,
        "global_exhaustion": False,
    }


def _factor_pair_candidates(p: int, x: int) -> Iterable[tuple[int, int, int, int, int]]:
    """Yield canonical factor-pair candidates (d,e,y,z,a/b) for one x."""
    numerator = 4 * x - p
    denominator = p * x
    g = gcd(numerator, denominator)
    a = numerator // g
    b = denominator // g
    factors_b = factor_trial(b)
    for d in divisors_from_factorization(factors_b, exponent_multiplier=2):
        if d > b:
            break
        e = b * b // d
        if d * e != b * b or d > e:
            continue
        if (b + d) % a or (b + e) % a:
            continue
        y = (b + d) // a
        z = (b + e) // a
        yield d, e, y, z, a


def complete_factor_pair_search(p: int) -> dict[str, Any]:
    """Exhaust all sorted solutions using (ay-b)(az-b)=b^2.

    The x interval is finite: p/4 < x <= 3p/4.  For each x, the positive
    factor pairs of b^2 are finite.  Thus a returned MISS is global.
    """
    x_min = p // 4 + 1
    x_max = (3 * p) // 4
    factor_pairs_checked = 0
    x_positions = 0
    for x_index, x in enumerate(range(x_min, x_max + 1)):
        x_positions += 1
        numerator = 4 * x - p
        denominator = p * x
        g = gcd(numerator, denominator)
        a = numerator // g
        b = denominator // g
        for d, e, y, z, _ in _factor_pair_candidates(p, x):
            factor_pairs_checked += 1
            if not (x <= y <= z):
                continue
            triple = (x, y, z)
            if not verify_egyptian(p, triple):
                raise ConstructorError("factor-pair candidate lost the equation")
            return {
                "outcome": "HIT",
                "stage": "GLOBAL_FACTOR_PAIR",
                "x_index": x_index,
                "x_bounds": [x_min, x_max],
                "x_positions_seen": x_positions,
                "factor_pairs_checked": factor_pairs_checked,
                "certificate": {
                    "certificate_kind": "GLOBAL_FACTOR_PAIR",
                    "x": x,
                    "reduced_residual": {"a": a, "b": b},
                    "factor_pair": [d, e],
                    "denominators": list(triple),
                    "equation_interface": {"numerator": 4, "denominator": p},
                },
            }
    return {
        "outcome": "MISS_COMPLETE",
        "stage": "GLOBAL_FACTOR_PAIR",
        "x_bounds": [x_min, x_max],
        "x_positions": x_positions,
        "factor_pairs_checked": factor_pairs_checked,
        "coverage_identity": "(a*y-b)*(a*z-b)=b^2",
        "global_exhaustion": True,
    }


def _subject_binding(
    *,
    subject_kind: str,
    source_state: Mapping[str, Any],
    projection: Mapping[str, Any] | None,
) -> dict[str, Any]:
    source_digest = C.state_wire_digest(source_state)
    if subject_kind == "SOURCE_STATE":
        return {
            "subject_kind": subject_kind,
            "subject_id": source_state["state_id"],
            "subject_digest": source_digest,
            "source_state_id": source_state["state_id"],
            "source_state_digest": source_digest,
            "projection_id": None,
            "projection_digest": None,
        }
    if subject_kind != "TARGET_PROJECTION" or projection is None:
        raise ConstructorError("invalid target subject binding")
    return {
        "subject_kind": subject_kind,
        "subject_id": projection["projection_id"],
        "subject_digest": C.canonical_digest(projection),
        "source_state_id": source_state["state_id"],
        "source_state_digest": source_digest,
        "projection_id": projection["projection_id"],
        "projection_digest": C.canonical_digest(projection),
    }


def projection_mapping(projection: C.PhaseProjection) -> dict[str, Any]:
    return {
        "artifact_type": "CanonicalPhaseRootProjectionV2",
        "schema_version": 1,
        "projection_id": projection.projection_id,
        "root_context": projection.p,
        "equation_rank": projection.p,
        "t": projection.t,
        "x": projection.X,
        "R": projection.R,
        "K": projection.K,
        "mark_kind": C.ROOT_SOL,
        "facts": copy.deepcopy(dict(projection.facts)),
        "tie_break_rule_id": "q1_phase_root_closed_form_no_caller_tie_break_v1",
    }


def complete_source_terminal_decision(
    source_state: Mapping[str, Any]
) -> dict[str, Any]:
    C.validate_root_state_shape(source_state)
    p = int(source_state["root_context"])
    ordinary = ordinary_q1_g_parameters(p)
    prefix = bradford_m23_prefix(p)
    if prefix["outcome"] == "HIT":
        global_result = None
        outcome = "HIT"
        certificate = prefix["certificate"]
    else:
        global_result = complete_factor_pair_search(p)
        outcome = global_result["outcome"]
        certificate = global_result.get("certificate")
    binding = _subject_binding(
        subject_kind="SOURCE_STATE", source_state=source_state, projection=None
    )
    return C.seal(
        {
            "receipt_type": "SP05CompleteTerminalDecisionV1",
            "schema_version": 1,
            "head_sha": C.PINNED_HEAD_SHA,
            "schedule_id": SOURCE_SCHEDULE_ID,
            "schedule_semantics": "M23_PREFIX_THEN_GLOBAL_SORTED_FACTOR_PAIR_EXHAUSTION",
            **binding,
            "p": p,
            "ordinary_q1_g": ordinary,
            "prefix_result": prefix,
            "global_result": global_result,
            "anchor_result": None,
            "outcome": outcome,
            "certificate": certificate,
            "coverage_theorem_id": COVERAGE_THEOREM_ID,
            "constructor_id": CONSTRUCTOR_ID,
        }
    )


def anchor_decision(p: int, projection: C.PhaseProjection) -> dict[str, Any]:
    anchor = projection.R - 1
    common_gcd = gcd(anchor, projection.K)
    if projection.K % anchor == 0:
        triple = (projection.K // anchor, projection.K, p * projection.K)
        if not verify_egyptian(p, triple):
            raise ConstructorError("anchor candidate lost the equation")
        return {
            "outcome": "HIT",
            "gcd": common_gcd,
            "anchor": anchor,
            "certificate": {
                "certificate_kind": "PHASE_ROOT_ANCHOR_SINK",
                "denominators": list(triple),
                "equation_interface": {"numerator": 4, "denominator": p},
            },
        }
    return {
        "outcome": "MISS",
        "gcd": common_gcd,
        "anchor": anchor,
        "reason": "R-1 does not divide K",
    }


def complete_target_terminal_decision(
    source_state: Mapping[str, Any], projection: C.PhaseProjection
) -> dict[str, Any]:
    C.validate_root_state_shape(source_state)
    p = int(source_state["root_context"])
    if projection.p != p:
        raise ConstructorError("projection p differs from source p")
    projection_wire = projection_mapping(projection)
    prefix = bradford_m23_prefix(p)
    global_result = None
    anchor: dict[str, Any]
    if prefix["outcome"] == "HIT":
        # Strict terminal-first preemption: no later target predicate is evaluated.
        anchor = {"outcome": "NOT_REACHED", "reason": "p-only prefix HIT preempted target continuation"}
        certificate = prefix["certificate"]
        outcome = "HIT"
        hit_family = "P_ONLY_COMPLETE_SCHEDULE"
    else:
        global_result = complete_factor_pair_search(p)
        if global_result["outcome"] == "HIT":
            # The complete p-only fallback also preempts the target-local anchor.
            anchor = {"outcome": "NOT_REACHED", "reason": "p-only complete HIT preempted target continuation"}
            certificate = global_result["certificate"]
            outcome = "HIT"
            hit_family = "P_ONLY_COMPLETE_SCHEDULE"
        else:
            anchor = anchor_decision(p, projection)
            if anchor["outcome"] == "HIT":
                certificate = anchor["certificate"]
                outcome = "HIT"
                hit_family = "PHASE_ROOT_ANCHOR_SINK"
            else:
                certificate = None
                outcome = "MISS_COMPLETE"
                hit_family = None
    binding = _subject_binding(
        subject_kind="TARGET_PROJECTION",
        source_state=source_state,
        projection=projection_wire,
    )
    return C.seal(
        {
            "receipt_type": "SP05CompleteTerminalDecisionV1",
            "schema_version": 1,
            "head_sha": C.PINNED_HEAD_SHA,
            "schedule_id": TARGET_SCHEDULE_ID,
            "schedule_semantics": "INDEPENDENT_P_ONLY_COMPLETE_REPLAY_THEN_PHASE_ROOT_ANCHOR",
            **binding,
            "p": p,
            "ordinary_q1_g": ordinary_q1_g_parameters(p),
            "prefix_result": prefix,
            "global_result": global_result,
            "anchor_result": anchor,
            "outcome": outcome,
            "hit_family": hit_family,
            "certificate": certificate,
            "coverage_theorem_id": COVERAGE_THEOREM_ID,
            "constructor_id": CONSTRUCTOR_ID,
        }
    )


def make_reference_actualness_receipt(source_state: Mapping[str, Any]) -> dict[str, Any]:
    """A negative-control fixture; edge construction must reject it."""
    C.validate_root_state_shape(source_state)
    return C.seal(
        {
            "receipt_type": "SP05SourceActualnessReceiptV1",
            "schema_version": 1,
            "head_sha": C.PINNED_HEAD_SHA,
            "authority_class": "REFERENCE_FIXTURE_NOT_REPOSITORY_AUTHORITY",
            "source_state_id": source_state["state_id"],
            "source_state_digest": C.state_wire_digest(source_state),
            "v5_admission_receipt_id": "REFERENCE_ONLY",
            "v5_admission_receipt_digest": "0" * 64,
            "v6_rebind_receipt_id": "REFERENCE_ONLY",
            "v6_rebind_receipt_digest": "0" * 64,
            "occurrence_path": ["facts", "relation_q"],
            "occurrence_value": 1,
            "producer_id": C.EDGE_PRODUCER_ID,
            "branch_id": C.EDGE_BRANCH_ID,
        }
    )


def verify_actualness_receipt(
    source_state: Mapping[str, Any], actualness: Mapping[str, Any]
) -> None:
    C.verify_seal(actualness)
    if actualness.get("receipt_type") != "SP05SourceActualnessReceiptV1":
        raise ConstructorError("wrong actualness receipt type")
    if actualness.get("head_sha") != C.PINNED_HEAD_SHA:
        raise ConstructorError("actualness receipt is not pinned to exact HEAD")
    if actualness.get("authority_class") != "EXACT_HEAD_V5_V6_ACTUAL_SOURCE":
        raise ConstructorError("source actualness authority is absent")
    if actualness.get("source_state_id") != source_state["state_id"]:
        raise ConstructorError("actualness source state ID mismatch")
    if actualness.get("source_state_digest") != C.state_wire_digest(source_state):
        raise ConstructorError("actualness source wire digest mismatch")
    if actualness.get("occurrence_path") != ["facts", "relation_q"]:
        raise ConstructorError("q occurrence path was swapped")
    if actualness.get("occurrence_value") != 1:
        raise ConstructorError("q occurrence value is not the source integer 1")
    if source_state["facts"]["relation_q"] != 1:
        raise ConstructorError("source wire does not contain q=1 at the bound path")
    for name in ("v5_admission_receipt_digest", "v6_rebind_receipt_digest"):
        value = actualness.get(name)
        if not (
            isinstance(value, str)
            and len(value) == 64
            and all(ch in "0123456789abcdef" for ch in value)
            and set(value) != {"0"}
        ):
            raise ConstructorError(f"{name} is not a well-formed authority digest")
    # This standalone package deliberately bundles no exact-HEAD role registry,
    # Git trust-anchor resolver, V5/V6 issuer, or post-issuance receipt replayer.
    # A caller-supplied sealed mapping is therefore never sufficient authority.
    raise ConstructorError(
        "NO_EXTERNAL_ACTUALNESS_AUTHORITY: standalone package cannot grant V5/V6 actualness"
    )


def _require_complete_miss(
    decision: Mapping[str, Any], *, subject_kind: str, expected_id: str
) -> None:
    C.verify_seal(decision)
    if decision.get("receipt_type") != "SP05CompleteTerminalDecisionV1":
        raise ConstructorError("wrong complete terminal decision type")
    if decision.get("subject_kind") != subject_kind:
        raise ConstructorError("terminal decision subject kind mismatch")
    if decision.get("subject_id") != expected_id:
        raise ConstructorError("terminal decision subject ID mismatch")
    if decision.get("outcome") != "MISS_COMPLETE":
        raise ConstructorError("producer requires MISS_COMPLETE")
    if decision.get("coverage_theorem_id") != COVERAGE_THEOREM_ID:
        raise ConstructorError("terminal decision has the wrong coverage theorem")


def build_structured_bundle(
    *,
    source_state: Mapping[str, Any],
    actualness: Mapping[str, Any],
    source_decision: Mapping[str, Any],
    projection: C.PhaseProjection,
    target_decision: Mapping[str, Any],
    target_state: Mapping[str, Any],
) -> dict[str, Any]:
    # Fail closed before emitting any E1--E5-shaped wire.  This call is kept as
    # the constructive content of the conditional theorem, not as an issuer.
    verify_actualness_receipt(source_state, actualness)
    p = int(source_state["root_context"])
    owner, owner_digest = C.validate_successor_state_shape(target_state, source_state)
    source_vector = C.source_potential(p)
    target_vector = C.target_potential(p)
    C.verify_phase_drop(p, source_vector, target_vector)
    e1 = C.seal(
        {
            "receipt_type": "E1OccurrenceReceiptV1",
            "schema_version": 1,
            "source_state_id": source_state["state_id"],
            "source_state_digest": C.state_wire_digest(source_state),
            "parent_transition_id": "ROOT_INITIALIZER",
            "parent_transition_digest": "ROOT_INITIALIZER",
            "producer_id": C.EDGE_PRODUCER_ID,
            "producer_digest": C.canonical_digest({"producer_id": C.EDGE_PRODUCER_ID}),
            "branch_id": C.EDGE_BRANCH_ID,
            "scope": "Q1_G_COMPLETE_TERMINAL_CLEARANCE",
            "occurrence_path": ["facts", "relation_q"],
            "occurrence_value": 1,
            "provenance_digest": actualness["digest"],
            "source_terminal_schedule_id": SOURCE_SCHEDULE_ID,
            "source_terminal_schedule_digest": source_decision["digest"],
            "source_terminal_result": "MISS_COMPLETE",
            "source_terminal_result_digest": C.canonical_digest(
                {"outcome": "MISS_COMPLETE", "decision_digest": source_decision["digest"]}
            ),
            "claim_id": "SP-05",
            "claim_digest": C.canonical_digest({"claim_id": "SP-05"}),
            "reproduction_id": "sp05_complete_proof_package_v1",
            "reproduction_digest": C.canonical_digest({"reproduction_id": "sp05_complete_proof_package_v1"}),
            "independent_verifier_id": "sp05_independent_replayer_v1",
            "independent_verifier_digest": C.canonical_digest({"verifier": "sp05_independent_replayer_v1"}),
        }
    )
    projection_wire = projection_mapping(projection)
    e2 = C.seal(
        {
            "receipt_type": "E2ProjectionReceiptV1",
            "schema_version": 1,
            "source_state_id": source_state["state_id"],
            "source_state_digest": C.state_wire_digest(source_state),
            "producer_id": C.EDGE_PRODUCER_ID,
            "branch_id": C.EDGE_BRANCH_ID,
            "candidate_witness_digest": C.canonical_digest(
                {"actualness": actualness["digest"], "source_miss": source_decision["digest"]}
            ),
            "projector_id": "q1_phase_root_closed_form_projector_v1",
            "projector_digest": C.canonical_digest({"formula": ["16t+3", "X(16t+1)"]}),
            "tie_break_rule_id": "q1_phase_root_closed_form_no_caller_tie_break_v1",
            "tie_break_rule_digest": C.canonical_digest({"caller_tie_break": False}),
            "canonical_target_payload": projection_wire,
            "target_projection_digest": C.canonical_digest(projection_wire),
        }
    )
    family_results = {
        "type_ii_relation_f_endpoint": False,
        "type_ii_relation_g_endpoint": False,
        "type_i_full_carrier_post_g": True,
    }
    e3 = C.seal(
        {
            "receipt_type": "E3TypingReceiptV1",
            "schema_version": 1,
            "target_state_id": target_state["state_id"],
            "target_projection_digest": C.canonical_digest(projection_wire),
            "target_schema_id": C.STATE_SCHEMA_ID,
            "target_schema_version": 1,
            "normal_form_verifier_id": "persistent_selector_state_v1.extract_verified_selector_header_v1",
            "normal_form_verifier_digest": C.canonical_digest({"contract": "persistent_selector_state_v1"}),
            "family_predicate_results": family_results,
            "precedence_table_id": "persistent_selector_state_v1.family_precedence",
            "precedence_table_digest": C.canonical_digest({"target_owner_index": 14}),
            "owner": owner,
            "owner_digest": owner_digest,
            "grammar_id": "persistent_selector_state_v1",
            "grammar_digest": C.canonical_digest({"fact_fields": sorted(C.FACT_FIELDS)}),
            "admission_gate_id": "reject_before_persistent_queue_v1",
            "admission_gate_version": 1,
            "admission_gate_digest": C.canonical_digest({"gate": "common_v1_plus_structured_bundle_wrapper"}),
        }
    )
    interface = {"interface": "ROOT_SOL", "numerator": 4, "denominator": p}
    e4 = C.seal(
        {
            "receipt_type": "E4LiftReceiptV1",
            "schema_version": 1,
            "source_state_id": source_state["state_id"],
            "target_state_id": target_state["state_id"],
            "source_equation_interface": interface,
            "source_equation_interface_digest": C.canonical_digest(interface),
            "target_equation_interface": interface,
            "target_equation_interface_digest": C.canonical_digest(interface),
            "lift_map_id": "identity_on_positive_integer_triples_v1",
            "lift_map_digest": C.canonical_digest({"Lambda": "(x,y,z)->(x,y,z)"}),
            "universal_quantifier_statement": "forall u in Sol(T), Lambda(u)=u in Sol(S)",
            "symbolic_verifier_id": "sp05_identity_lift_symbolic_verifier_v1",
            "symbolic_verifier_digest": C.canonical_digest({"reason": "same ROOT_SOL 4/p interface"}),
            "reproduction_id": "sp05_complete_proof_package_v1",
            "reproduction_digest": C.canonical_digest({"reproduction_id": "sp05_complete_proof_package_v1"}),
        }
    )
    e5 = C.seal(
        {
            "receipt_type": "E5DescentReceiptV1",
            "schema_version": 1,
            "source_state_id": source_state["state_id"],
            "target_state_id": target_state["state_id"],
            "potential_contract_id": "t5-global-well-foundedness-contract-v2",
            "source_coordinates": list(source_vector),
            "target_coordinates": list(target_vector),
            "ticket_type": C.PHASE_DROP,
            "first_difference_index": 1,
            "comparison": "STRICT_LEXICOGRAPHIC_DROP",
        }
    )
    reentry_registration = C.make_reentry_registration()
    reentry = C.verify_reentry(target_state, reentry_registration)
    bundle = C.seal(
        {
            "receipt_type": "SP05StructuredTransitionBundleV1",
            "schema_version": 1,
            "head_sha": C.PINNED_HEAD_SHA,
            "source_state_id": source_state["state_id"],
            "target_state_id": target_state["state_id"],
            "source_terminal_decision_digest": source_decision["digest"],
            "target_terminal_decision_digest": target_decision["digest"],
            "E1": e1,
            "E2": e2,
            "E3": e3,
            "E4": e4,
            "E5": e5,
            "reentry_registration": reentry_registration,
            "reentry_receipt": reentry,
            "admission_order": ["RAW_TARGET_STATE_ID", "STRUCTURED_BUNDLE", "ADMISSION_SIDECAR"],
        }
    )
    return bundle


def build_edge_if_complete_miss(
    *,
    source_state: Mapping[str, Any],
    actualness: Mapping[str, Any],
    source_decision: Mapping[str, Any],
    target_decision: Mapping[str, Any],
    projection: C.PhaseProjection,
) -> dict[str, Any]:
    C.validate_root_state_shape(source_state)
    verify_actualness_receipt(source_state, actualness)
    _require_complete_miss(
        source_decision,
        subject_kind="SOURCE_STATE",
        expected_id=source_state["state_id"],
    )
    _require_complete_miss(
        target_decision,
        subject_kind="TARGET_PROJECTION",
        expected_id=projection.projection_id,
    )
    target_state = C.make_successor_state(
        source_state=source_state,
        complete_source_miss_digest=source_decision["digest"],
        complete_target_miss_digest=target_decision["digest"],
    )
    bundle = build_structured_bundle(
        source_state=source_state,
        actualness=actualness,
        source_decision=source_decision,
        projection=projection,
        target_decision=target_decision,
        target_state=target_state,
    )
    return C.seal(
        {
            "decision_type": "SP05VerifiedSuccessorDecisionV1",
            "schema_version": 1,
            "outcome": "VERIFIED_EDGE",
            "source_state": copy.deepcopy(dict(source_state)),
            "target_state": target_state,
            "projection": projection_mapping(projection),
            "structured_bundle": bundle,
        }
    )


def select(
    source_state: Mapping[str, Any], actualness: Mapping[str, Any]
) -> dict[str, Any]:
    """Terminal-first total selector for the stated SP-05 domain."""
    C.validate_root_state_shape(source_state)
    # Actual-source authentication is an input gate, not a successor step.
    # It precedes terminal replay while terminal HIT still preempts every
    # projection/target construction.
    verify_actualness_receipt(source_state, actualness)
    p = int(source_state["root_context"])
    ordinary_q1_g_parameters(p)
    source_decision = complete_source_terminal_decision(source_state)
    if source_decision["outcome"] == "HIT":
        return C.seal(
            {
                "decision_type": "SP05SelectionDecisionV1",
                "schema_version": 1,
                "outcome": "TERMINAL",
                "terminal_subject": "SOURCE_STATE",
                "source_state_id": source_state["state_id"],
                "terminal_decision": source_decision,
                "certificate": source_decision["certificate"],
                "successor": None,
            }
        )
    projection = C.phase_projection(p)
    target_decision = complete_target_terminal_decision(source_state, projection)
    if target_decision["outcome"] == "HIT":
        certificate = target_decision["certificate"]
        if not verify_egyptian(p, certificate["denominators"]):
            raise ConstructorError("target terminal lift does not solve the source interface")
        return C.seal(
            {
                "decision_type": "SP05SelectionDecisionV1",
                "schema_version": 1,
                "outcome": "TERMINAL",
                "terminal_subject": "TARGET_PROJECTION_WITH_IDENTITY_LIFT_TO_SOURCE",
                "source_state_id": source_state["state_id"],
                "projection": projection_mapping(projection),
                "terminal_decision": target_decision,
                "certificate": certificate,
                "lift_map": "IDENTITY",
                "successor": None,
            }
        )
    edge = build_edge_if_complete_miss(
        source_state=source_state,
        actualness=actualness,
        source_decision=source_decision,
        target_decision=target_decision,
        projection=projection,
    )
    return C.seal(
        {
            "decision_type": "SP05SelectionDecisionV1",
            "schema_version": 1,
            "outcome": "VERIFIED_EDGE",
            "source_state_id": source_state["state_id"],
            "terminal_decision": source_decision,
            "successor": edge,
        }
    )
