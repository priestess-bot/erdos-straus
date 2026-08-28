#!/usr/bin/env python3
"""Independent SP-05 replayer.

This file intentionally imports neither ``sp05_constructor`` nor
``sp05_contract``.  It reimplements primality, factorization, divisor traversal,
canonical encoding, complete terminal coverage, projection, V1 state checks,
owner recognition and T5 comparison.
"""
from __future__ import annotations

import copy
import hashlib
import json
from math import gcd, isqrt
from typing import Any, Mapping, Sequence

PINNED_HEAD_SHA = "7dff8a9e7338814e83ab839c33b8b58c28f4ea0d"
M23 = (3, 7, 11, 15, 19, 23)
SOURCE_SCHEDULE_ID = "q1_complete_terminal_m23_then_factor_pairs_v1"
TARGET_SCHEDULE_ID = "q1_phase_root_complete_terminal_then_anchor_v1"
COVERAGE_THEOREM_ID = "sp05_sorted_solution_factor_pair_bijection_v1"
SOURCE_OWNER = "type_ii_relation_g_endpoint"
TARGET_OWNER = "type_i_full_carrier_post_g"
EDGE_PRODUCER_ID = "q1_phase_root_complete_producer_v1"
EDGE_BRANCH_ID = "q1_g_complete_miss_phase_root_v1"

FACT_FIELDS = frozenset(
    {
        "major_phase", "type_i_protocol", "t5_eta_p", "pre_a", "absorb_m",
        "absorb_r_epsilon", "reset_carrier", "endpoint_fiber", "relation_q",
        "provenance_kind", "full_carrier_scope", "atomic_arm", "dispatch_status",
        "proper_root_k", "proper_root_height_class", "proper_root_height",
        "proper_root_r", "is_overflow", "support_A", "carrier_M", "overflow_d",
        "chart_R", "chart_K", "sink_scc_receipt", "same_chart_promotion_receipt",
    }
)
TOP_LEVEL_FIELDS = frozenset(
    {
        "schema_id", "schema_version", "state_id", "artifact_class", "consumer",
        "queue_gate", "producer_id", "branch_id", "parent_state_id", "root_context",
        "equation_rank", "mark", "terminal_first", "source_receipt", "facts",
    }
)


class ReplayError(ValueError):
    pass


def canonical_json(value: Any) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False
    )


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("ascii")).hexdigest()


def verify_seal(value: Mapping[str, Any]) -> None:
    if not isinstance(value, Mapping):
        raise ReplayError("artifact is not a mapping")
    claimed = value.get("digest")
    if not isinstance(claimed, str) or len(claimed) != 64:
        raise ReplayError("artifact digest is malformed")
    unsigned = dict(value)
    unsigned.pop("digest", None)
    if digest(unsigned) != claimed:
        raise ReplayError("artifact digest mismatch")


def build_state_id(raw: Mapping[str, Any]) -> str:
    payload = copy.deepcopy(dict(raw))
    payload.pop("state_id", None)
    return "state:" + digest(payload)


def exact_value_equal(value: Any, expected: Any) -> bool:
    """Compare decoded JSON values without accepting bool/float int aliases."""
    if type(expected) in {type(None), bool, int, str}:
        return type(value) is type(expected) and value == expected
    if isinstance(expected, Mapping):
        return (
            isinstance(value, Mapping)
            and set(value) == set(expected)
            and all(exact_value_equal(value[key], expected[key]) for key in expected)
        )
    if isinstance(expected, (list, tuple)):
        return (
            isinstance(value, (list, tuple))
            and len(value) == len(expected)
            and all(exact_value_equal(item, want) for item, want in zip(value, expected))
        )
    return type(value) is type(expected) and value == expected


def primes_up_to(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return [i for i, flag in enumerate(sieve) if flag]


def factor_by_sieve(n: int) -> tuple[tuple[int, int], ...]:
    if type(n) is not int or n < 1:
        raise ReplayError("factor input must be positive")
    remaining = n
    factors: list[tuple[int, int]] = []
    for p in primes_up_to(isqrt(n)):
        if p * p > remaining:
            break
        if remaining % p:
            continue
        exponent = 0
        while remaining % p == 0:
            remaining //= p
            exponent += 1
        factors.append((p, exponent))
    if remaining > 1:
        factors.append((remaining, 1))
    return tuple(factors)


def is_prime_exact(n: int) -> bool:
    """Use the independent complete factorization path for every finite input."""
    return type(n) is int and n >= 2 and factor_by_sieve(n) == ((n, 1),)


def iterative_divisors(
    factors: Sequence[tuple[int, int]], exponent_multiplier: int
) -> tuple[int, ...]:
    values = {1}
    for prime, exponent in reversed(tuple(factors)):
        expanded: set[int] = set()
        power = 1
        for _ in range(exponent * exponent_multiplier + 1):
            for value in values:
                expanded.add(value * power)
            power *= prime
        values = expanded
    return tuple(sorted(values))


def square_divisors_by_complement(x: int) -> tuple[int, ...]:
    n = x * x
    values: list[int] = []
    for d in range(1, x + 1):
        if n % d == 0:
            values.append(d)
            q = n // d
            if q != d:
                values.append(q)
    return tuple(sorted(values))


def ordinary_parameters(p: int) -> dict[str, Any]:
    if not is_prime_exact(p):
        raise ReplayError("p is not prime")
    if p < 25 or (p - 1) % 24:
        raise ReplayError("p is not 24t+1")
    t = (p - 1) // 24
    X = 6 * t + 1
    factors = factor_by_sieve(X)
    if any(prime % 3 != 1 for prime, _ in factors):
        raise ReplayError("X is not G")
    return {"p": p, "t": t, "X": X, "X_factorization": [list(v) for v in factors]}


def egyptian(p: int, triple: Sequence[int]) -> bool:
    if len(triple) != 3 or any(type(v) is not int or v <= 0 for v in triple):
        return False
    x, y, z = triple
    return 4 * x * y * z == p * (x * y + x * z + y * z)


def bradford_certificate(p: int, m: int, d: int, kind: str) -> dict[str, Any]:
    x = (p + m) // 4
    if kind == "TYPEI":
        y = (p * x + d) // m
        z = p * x * (p * x + d) // (m * d)
    elif kind == "TYPEII":
        y = p * (x + d) // m
        z = p * x * (x + d) // (m * d)
    else:
        raise ReplayError("unknown Bradford kind")
    triple = (x, y, z)
    if not egyptian(p, triple):
        raise ReplayError("Bradford certificate invalid")
    return {
        "certificate_kind": kind,
        "gap": m,
        "divisor": d,
        "denominators": list(triple),
        "equation_interface": {"numerator": 4, "denominator": p},
    }


def replay_prefix(p: int) -> dict[str, Any]:
    checks = 0
    divisor_positions = 0
    for gap_index, m in enumerate(M23):
        x = (p + m) // 4
        if 4 * x != p + m:
            raise ReplayError("nonintegral M23 x")
        for divisor_index, d in enumerate(square_divisors_by_complement(x)):
            divisor_positions += 1
            checks += 1
            if (p * x + d) % m == 0:
                return {
                    "outcome": "HIT", "stage": "M23_PREFIX",
                    "gap_index": gap_index, "divisor_index": divisor_index,
                    "kind_index": 0, "checks_before_hit": checks - 1,
                    "divisor_positions_seen": divisor_positions,
                    "certificate": bradford_certificate(p, m, d, "TYPEI"),
                }
            checks += 1
            if d <= x and (x + d) % m == 0:
                return {
                    "outcome": "HIT", "stage": "M23_PREFIX",
                    "gap_index": gap_index, "divisor_index": divisor_index,
                    "kind_index": 1, "checks_before_hit": checks - 1,
                    "divisor_positions_seen": divisor_positions,
                    "certificate": bradford_certificate(p, m, d, "TYPEII"),
                }
    return {
        "outcome": "MISS_REGISTERED_PRIORITY_COMPLETE", "stage": "M23_PREFIX",
        "ordered_gaps": list(M23), "checks": checks,
        "divisor_positions": divisor_positions, "global_exhaustion": False,
    }


def replay_global(p: int) -> dict[str, Any]:
    x_min = p // 4 + 1
    x_max = (3 * p) // 4
    factor_pairs_checked = 0
    x_positions = 0
    for x_index, x in enumerate(range(x_min, x_max + 1)):
        x_positions += 1
        num = 4 * x - p
        den = p * x
        g = gcd(num, den)
        a = num // g
        b = den // g
        factors = factor_by_sieve(b)
        for d in iterative_divisors(factors, 2):
            if d > b:
                break
            e = b * b // d
            if d > e or d * e != b * b:
                continue
            if (b + d) % a or (b + e) % a:
                continue
            y = (b + d) // a
            z = (b + e) // a
            factor_pairs_checked += 1
            if not (x <= y <= z):
                continue
            triple = (x, y, z)
            if not egyptian(p, triple):
                raise ReplayError("factor-pair identity invalid")
            return {
                "outcome": "HIT", "stage": "GLOBAL_FACTOR_PAIR",
                "x_index": x_index, "x_bounds": [x_min, x_max],
                "x_positions_seen": x_positions,
                "factor_pairs_checked": factor_pairs_checked,
                "certificate": {
                    "certificate_kind": "GLOBAL_FACTOR_PAIR", "x": x,
                    "reduced_residual": {"a": a, "b": b},
                    "factor_pair": [d, e], "denominators": list(triple),
                    "equation_interface": {"numerator": 4, "denominator": p},
                },
            }
    return {
        "outcome": "MISS_COMPLETE", "stage": "GLOBAL_FACTOR_PAIR",
        "x_bounds": [x_min, x_max], "x_positions": x_positions,
        "factor_pairs_checked": factor_pairs_checked,
        "coverage_identity": "(a*y-b)*(a*z-b)=b^2",
        "global_exhaustion": True,
    }


def expected_source_decision(source_state: Mapping[str, Any]) -> dict[str, Any]:
    p = source_state["root_context"]
    ordinary = ordinary_parameters(p)
    prefix = replay_prefix(p)
    if prefix["outcome"] == "HIT":
        global_result = None
        outcome = "HIT"
        certificate = prefix["certificate"]
    else:
        global_result = replay_global(p)
        outcome = global_result["outcome"]
        certificate = global_result.get("certificate")
    source_digest = digest(source_state)
    unsigned = {
        "receipt_type": "SP05CompleteTerminalDecisionV1", "schema_version": 1,
        "head_sha": PINNED_HEAD_SHA, "schedule_id": SOURCE_SCHEDULE_ID,
        "schedule_semantics": "M23_PREFIX_THEN_GLOBAL_SORTED_FACTOR_PAIR_EXHAUSTION",
        "subject_kind": "SOURCE_STATE", "subject_id": source_state["state_id"],
        "subject_digest": source_digest, "source_state_id": source_state["state_id"],
        "source_state_digest": source_digest, "projection_id": None,
        "projection_digest": None, "p": p, "ordinary_q1_g": ordinary,
        "prefix_result": prefix, "global_result": global_result,
        "anchor_result": None, "outcome": outcome, "certificate": certificate,
        "coverage_theorem_id": COVERAGE_THEOREM_ID,
        "constructor_id": "sp05_complete_scheduler_constructor_v1",
    }
    unsigned["digest"] = digest(unsigned)
    return unsigned


def projection_for(p: int) -> dict[str, Any]:
    params = ordinary_parameters(p)
    t, X = params["t"], params["X"]
    R = 16 * t + 3
    K = X * (16 * t + 1)
    if 4 * K != p * R + 1:
        raise ReplayError("projection equation failed")
    facts = target_facts(p)
    base = {
        "artifact_type": "CanonicalPhaseRootProjectionV2", "schema_version": 1,
        "transition_kind": "Q1_G_FULL_CARRIER_PHASE_ROOT", "root_context": p,
        "equation_rank": p, "t": t, "x": X, "mark_kind": "ROOT_SOL",
        "facts": facts,
        "tie_break_rule_id": "q1_phase_root_closed_form_no_caller_tie_break_v1",
    }
    projection_id = "phase-root-projection:" + digest(base)
    return {
        "artifact_type": "CanonicalPhaseRootProjectionV2", "schema_version": 1,
        "projection_id": projection_id, "root_context": p, "equation_rank": p,
        "t": t, "x": X, "R": R, "K": K, "mark_kind": "ROOT_SOL",
        "facts": facts,
        "tie_break_rule_id": "q1_phase_root_closed_form_no_caller_tie_break_v1",
    }


def source_facts() -> dict[str, Any]:
    return {
        "major_phase": "TYPEII_G_HANDOFF", "type_i_protocol": None,
        "t5_eta_p": 0, "pre_a": None, "absorb_m": None,
        "absorb_r_epsilon": 0, "reset_carrier": None, "endpoint_fiber": "G",
        "relation_q": 1, "provenance_kind": "ORDINARY_ENDPOINT",
        "full_carrier_scope": False, "atomic_arm": "NONE", "dispatch_status": "NONE",
        "proper_root_k": None, "proper_root_height_class": "NONE",
        "proper_root_height": None, "proper_root_r": None, "is_overflow": False,
        "support_A": None, "carrier_M": None, "overflow_d": None,
        "chart_R": None, "chart_K": None, "sink_scc_receipt": False,
        "same_chart_promotion_receipt": False,
    }


def target_facts(p: int) -> dict[str, Any]:
    t = (p - 1) // 24
    X = 6 * t + 1
    return {
        "major_phase": "TYPEI", "type_i_protocol": "CHARGED", "t5_eta_p": 0,
        "pre_a": None, "absorb_m": None, "absorb_r_epsilon": 0,
        "reset_carrier": None, "endpoint_fiber": "NONE", "relation_q": None,
        "provenance_kind": "FULL_CARRIER_POST_G", "full_carrier_scope": True,
        "atomic_arm": "NONE", "dispatch_status": "NONE", "proper_root_k": None,
        "proper_root_height_class": "NONE", "proper_root_height": None,
        "proper_root_r": None, "is_overflow": False, "support_A": 1,
        "carrier_M": None, "overflow_d": None, "chart_R": 16 * t + 3,
        "chart_K": X * (16 * t + 1), "sink_scc_receipt": False,
        "same_chart_promotion_receipt": False,
    }


def expected_target_decision(
    source_state: Mapping[str, Any], projection: Mapping[str, Any]
) -> dict[str, Any]:
    p = source_state["root_context"]
    prefix = replay_prefix(p)
    global_result = None
    if prefix["outcome"] == "HIT":
        anchor_result = {"outcome": "NOT_REACHED", "reason": "p-only prefix HIT preempted target continuation"}
        certificate = prefix["certificate"]
        outcome, hit_family = "HIT", "P_ONLY_COMPLETE_SCHEDULE"
    else:
        global_result = replay_global(p)
        if global_result["outcome"] == "HIT":
            anchor_result = {"outcome": "NOT_REACHED", "reason": "p-only complete HIT preempted target continuation"}
            certificate = global_result["certificate"]
            outcome, hit_family = "HIT", "P_ONLY_COMPLETE_SCHEDULE"
        else:
            anchor = projection["R"] - 1
            common_gcd = gcd(anchor, projection["K"])
            if projection["K"] % anchor == 0:
                triple = [projection["K"] // anchor, projection["K"], p * projection["K"]]
                anchor_result = {
                    "outcome": "HIT", "gcd": common_gcd, "anchor": anchor,
                    "certificate": {
                        "certificate_kind": "PHASE_ROOT_ANCHOR_SINK",
                        "denominators": triple,
                        "equation_interface": {"numerator": 4, "denominator": p},
                    },
                }
                certificate = anchor_result["certificate"]
                outcome, hit_family = "HIT", "PHASE_ROOT_ANCHOR_SINK"
            else:
                anchor_result = {
                    "outcome": "MISS", "gcd": common_gcd, "anchor": anchor,
                    "reason": "R-1 does not divide K",
                }
                certificate = None
                outcome, hit_family = "MISS_COMPLETE", None
    projection_digest = digest(projection)
    source_digest = digest(source_state)
    unsigned = {
        "receipt_type": "SP05CompleteTerminalDecisionV1", "schema_version": 1,
        "head_sha": PINNED_HEAD_SHA, "schedule_id": TARGET_SCHEDULE_ID,
        "schedule_semantics": "INDEPENDENT_P_ONLY_COMPLETE_REPLAY_THEN_PHASE_ROOT_ANCHOR",
        "subject_kind": "TARGET_PROJECTION", "subject_id": projection["projection_id"],
        "subject_digest": projection_digest, "source_state_id": source_state["state_id"],
        "source_state_digest": source_digest, "projection_id": projection["projection_id"],
        "projection_digest": projection_digest, "p": p,
        "ordinary_q1_g": ordinary_parameters(p), "prefix_result": prefix,
        "global_result": global_result, "anchor_result": anchor_result,
        "outcome": outcome, "hit_family": hit_family, "certificate": certificate,
        "coverage_theorem_id": COVERAGE_THEOREM_ID,
        "constructor_id": "sp05_complete_scheduler_constructor_v1",
    }
    unsigned["digest"] = digest(unsigned)
    return unsigned


def validate_source_state(raw: Mapping[str, Any]) -> None:
    if not isinstance(raw, Mapping) or set(raw) != TOP_LEVEL_FIELDS:
        raise ReplayError("source is not an exact V1 state")
    if (
        raw.get("schema_id") != "persistent_selector_state_v1"
        or type(raw.get("schema_version")) is not int
        or raw.get("schema_version") != 1
    ):
        raise ReplayError("source schema mismatch")
    if raw.get("queue_gate") != "ROOT_INITIALIZER_OUTPUT" or raw.get("parent_state_id") is not None:
        raise ReplayError("source is not an initializer output")
    if raw.get("state_id") != build_state_id(raw):
        raise ReplayError("source state ID mismatch")
    if not exact_value_equal(raw.get("facts"), source_facts()):
        raise ReplayError("source facts mismatch")
    if raw["facts"].get("relation_q") != 1:
        raise ReplayError("source q occurrence is not 1")
    for receipt in (raw["mark"], raw["terminal_first"], raw["source_receipt"]):
        verify_seal(receipt)


def validate_projection(p: int, projection: Mapping[str, Any]) -> None:
    expected = projection_for(p)
    if not exact_value_equal(projection, expected):
        raise ReplayError("projection is not the unique frozen projection")
    R, K = projection["R"], projection["K"]
    if 4 * K != p * R + 1:
        raise ReplayError("projection equation failed")
    if gcd(R - 1, K) != 1:
        raise ReplayError("canonical anchor gcd is not 1")


def validate_target_state(
    source: Mapping[str, Any], target: Mapping[str, Any]
) -> tuple[str, str]:
    validate_source_state(source)
    if not isinstance(target, Mapping) or set(target) != TOP_LEVEL_FIELDS:
        raise ReplayError("target is not an exact V1 state")
    p = source["root_context"]
    if (
        target.get("schema_id") != "persistent_selector_state_v1"
        or type(target.get("schema_version")) is not int
        or target.get("schema_version") != 1
    ):
        raise ReplayError("target schema mismatch")
    if target.get("queue_gate") != "ADMITTED_SUCCESSOR":
        raise ReplayError("target queue gate mismatch")
    if target.get("producer_id") != EDGE_PRODUCER_ID or target.get("branch_id") != EDGE_BRANCH_ID:
        raise ReplayError("target producer/branch mismatch")
    if target.get("parent_state_id") != source["state_id"]:
        raise ReplayError("source swap detected")
    if (
        type(target.get("root_context")) is not int
        or type(target.get("equation_rank")) is not int
        or target.get("root_context") != p
        or target.get("equation_rank") != p
    ):
        raise ReplayError("target equation interface mismatch")
    if target.get("state_id") != build_state_id(target):
        raise ReplayError("target state ID mismatch")
    if not exact_value_equal(target.get("facts"), target_facts(p)):
        raise ReplayError("target canonical facts mismatch")
    for receipt in (target["mark"], target["terminal_first"], target["source_receipt"]):
        verify_seal(receipt)
    receipt = target["source_receipt"]
    if receipt.get("parent_state_id") != source["state_id"]:
        raise ReplayError("target receipt source swap detected")
    if receipt.get("T5_ticket") != "PHASE_DROP":
        raise ReplayError("target lacks PHASE_DROP")
    if not all(receipt.get(k) is True for k in ("E1", "E2", "E3", "E4", "E5")):
        raise ReplayError("legacy target E1--E5 claims absent")
    owner = TARGET_OWNER
    owner_payload = {
        "contract_id": "t6_persistent_selector_state_v1", "schema_version": 1,
        "state_id": target["state_id"], "facts_digest": digest(target["facts"]),
        "owner": owner, "matched_families": [owner], "precedence_index": 14,
    }
    return owner, "owner:" + digest(owner_payload)


def validate_t5(p: int, source_coordinates: Sequence[int], target_coordinates: Sequence[int]) -> None:
    t = (p - 1) // 24
    X = 6 * t + 1
    K = X * (16 * t + 1)
    expected_source = (p, 3, 0, 0, 0, 0, 0)
    expected_target = (p, 2, 4, (p - 1) ** 2 // 4, K, 0, 0)
    if tuple(source_coordinates) != expected_source:
        raise ReplayError("source T5 vector drift")
    if tuple(target_coordinates) != expected_target:
        raise ReplayError("target T5 vector drift")
    if not expected_target < expected_source or expected_target[1] >= expected_source[1]:
        raise ReplayError("PHASE_DROP failed")


def replay_source_decision(
    source_state: Mapping[str, Any], decision: Mapping[str, Any]
) -> dict[str, Any]:
    validate_source_state(source_state)
    verify_seal(decision)
    expected = expected_source_decision(source_state)
    if not exact_value_equal(decision, expected):
        raise ReplayError("source complete-terminal decision does not replay")
    return {"accepted": True, "outcome": decision["outcome"], "digest": decision["digest"]}


def replay_target_decision(
    source_state: Mapping[str, Any], projection: Mapping[str, Any], decision: Mapping[str, Any]
) -> dict[str, Any]:
    validate_source_state(source_state)
    validate_projection(source_state["root_context"], projection)
    verify_seal(decision)
    expected = expected_target_decision(source_state, projection)
    if not exact_value_equal(decision, expected):
        raise ReplayError("target complete-terminal decision does not replay")
    return {"accepted": True, "outcome": decision["outcome"], "digest": decision["digest"]}


def replay_actualness(source: Mapping[str, Any], actualness: Mapping[str, Any]) -> None:
    verify_seal(actualness)
    if actualness.get("authority_class") != "EXACT_HEAD_V5_V6_ACTUAL_SOURCE":
        raise ReplayError("actual source authority absent")
    if actualness.get("head_sha") != PINNED_HEAD_SHA:
        raise ReplayError("actualness HEAD mismatch")
    if actualness.get("source_state_id") != source["state_id"]:
        raise ReplayError("actualness source ID mismatch")
    if actualness.get("source_state_digest") != digest(source):
        raise ReplayError("actualness source digest mismatch")
    if actualness.get("occurrence_path") != ["facts", "relation_q"]:
        raise ReplayError("q-path swap")
    if actualness.get("occurrence_value") != 1 or source["facts"]["relation_q"] != 1:
        raise ReplayError("q occurrence value mismatch")
    for name in ("v5_admission_receipt_digest", "v6_rebind_receipt_digest"):
        value = actualness.get(name)
        if not (
            isinstance(value, str)
            and len(value) == 64
            and all(ch in "0123456789abcdef" for ch in value)
            and set(value) != {"0"}
        ):
            raise ReplayError(f"{name} malformed")
    raise ReplayError(
        "NO_EXTERNAL_ACTUALNESS_AUTHORITY: independent package has no exact-HEAD trust resolver"
    )


def replay_structured_bundle(
    source: Mapping[str, Any], target: Mapping[str, Any], projection: Mapping[str, Any],
    source_decision: Mapping[str, Any], target_decision: Mapping[str, Any],
    actualness: Mapping[str, Any], bundle: Mapping[str, Any]
) -> dict[str, Any]:
    validate_source_state(source)
    replay_actualness(source, actualness)
    replay_source_decision(source, source_decision)
    replay_target_decision(source, projection, target_decision)
    if source_decision["outcome"] != "MISS_COMPLETE" or target_decision["outcome"] != "MISS_COMPLETE":
        raise ReplayError("edge was attempted without two complete MISS decisions")
    owner, owner_digest = validate_target_state(source, target)
    validate_projection(source["root_context"], projection)
    verify_seal(bundle)
    if bundle.get("source_state_id") != source["state_id"] or bundle.get("target_state_id") != target["state_id"]:
        raise ReplayError("bundle source/target binding mismatch")
    if bundle.get("source_terminal_decision_digest") != source_decision["digest"]:
        raise ReplayError("bundle source terminal swap")
    if bundle.get("target_terminal_decision_digest") != target_decision["digest"]:
        raise ReplayError("bundle target terminal swap")
    for name in ("E1", "E2", "E3", "E4", "E5", "reentry_registration", "reentry_receipt"):
        verify_seal(bundle[name])
    e1 = bundle["E1"]
    if e1.get("source_state_id") != source["state_id"] or e1.get("occurrence_path") != ["facts", "relation_q"]:
        raise ReplayError("E1 source/q-path mismatch")
    if e1.get("source_terminal_result") != "MISS_COMPLETE":
        raise ReplayError("E1 does not bind MISS_COMPLETE")
    e2 = bundle["E2"]
    if e2.get("canonical_target_payload") != projection:
        raise ReplayError("E2 projection/tie-break swap")
    e3 = bundle["E3"]
    if e3.get("target_state_id") != target["state_id"] or e3.get("owner") != owner:
        raise ReplayError("E3 target owner mismatch")
    if e3.get("owner_digest") != owner_digest:
        raise ReplayError("E3 owner digest mismatch")
    e4 = bundle["E4"]
    if e4.get("source_equation_interface") != e4.get("target_equation_interface"):
        raise ReplayError("E4 interfaces differ")
    if e4.get("lift_map_id") != "identity_on_positive_integer_triples_v1":
        raise ReplayError("E4 lift is not identity")
    e5 = bundle["E5"]
    if e5.get("ticket_type") != "PHASE_DROP":
        raise ReplayError("E5 ticket swap")
    validate_t5(source["root_context"], e5["source_coordinates"], e5["target_coordinates"])
    registration = bundle["reentry_registration"]
    if registration.get("source_owners") != [TARGET_OWNER] or registration.get("consumer") != "t6_selector":
        raise ReplayError("re-entry route mismatch")
    if registration.get("creates_self_edge") is not False:
        raise ReplayError("re-entry creates a forbidden self-edge")
    receipt = bundle["reentry_receipt"]
    if receipt.get("target_state_id") != target["state_id"] or receipt.get("outcome") != "PHASE_BODY_ENTERED":
        raise ReplayError("re-entry receipt mismatch")
    return {
        "accepted": True, "source_state_id": source["state_id"],
        "target_state_id": target["state_id"], "owner": owner,
        "ticket": "PHASE_DROP", "reentry": "PHASE_BODY_ENTERED",
    }
