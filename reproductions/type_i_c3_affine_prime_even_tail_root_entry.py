#!/usr/bin/env python3
"""Verify guarded c=3 affine-prime even-tail root-entry receipts.

This is a standalone, root-only E1--E3 verifier.  It accepts a conditional
two-intermediate target-source word and creates an A=1 overflow seed receipt.
It deliberately does not import the aggregate selector, register an edge, or
claim E4/E5.  A future dispatcher must run terminal-first before using any
such receipt and must preserve the raw-entry digest if it ever authorizes a
further raw action.
"""

from __future__ import annotations

import argparse
import json
from math import gcd

import type_i_high_r_chart_two_anchor as shared


ROOT_ENTRY_ADAPTER = "c3_affine_prime_even_tail_root_entry_v1"
NORMAL_FORM = "c3_even_tail_overflow_seed_v1"
SOURCE_TREE_SCOPE = "fresh_source_tree_only"
CERTIFICATE_TYPE = "c3_target_source_even_tail_root_entry_v1"


def ordered_raw_step(
    *,
    modulus: int,
    K: int,
    source: tuple[int, int, int],
    selected_coordinate_index: int,
    q: int,
    expected_destination: tuple[int, int, int],
    name: str,
) -> dict[str, object]:
    """Replay one raw step while retaining the selected side and shift."""
    if selected_coordinate_index not in (0, 1):
        raise AssertionError("selected coordinate index must be 0 or 1")
    left, right, m = source
    if min(left, right, m) <= 0 or left + right != modulus * m:
        raise AssertionError(f"{name}: source is not a positive formal node")
    if gcd(left, right) != 1:
        raise AssertionError(f"{name}: source is not primitive")
    selected, other = (left, right) if selected_coordinate_index == 0 else (right, left)
    if not shared.is_prime(q) or selected % q:
        raise AssertionError(f"{name}: selected coordinate lacks the declared prime")

    selected_height = shared.valuation(selected, q)
    K_height = shared.valuation(K, q)
    shift = (-m) % q
    unit_condition = gcd(q, modulus * m * other) == 1
    if not (
        selected_height > K_height
        and 1 <= shift < q
        and unit_condition
    ):
        raise AssertionError(f"{name}: raw capacity or unit condition failed")

    selected_after_division = selected // q
    other_after_shift = (other + modulus * shift) // q
    m_after_shift = (m + shift) // q
    common = gcd(selected_after_division, other_after_shift)
    if common <= 0 or m_after_shift % common:
        raise AssertionError(f"{name}: gcd reduction did not preserve the layer")
    destination = (
        selected_after_division // common,
        other_after_shift // common,
        m_after_shift // common,
    )
    if destination != expected_destination:
        raise AssertionError(f"{name}: ordered destination changed")
    if (
        min(destination) <= 0
        or gcd(destination[0], destination[1]) != 1
        or destination[0] + destination[1] != modulus * destination[2]
    ):
        raise AssertionError(f"{name}: destination is not a primitive formal node")
    if m == 1 and destination[2] != 1:
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
        "pre_gcd_destination": [
            selected_after_division,
            other_after_shift,
            m_after_shift,
        ],
        "gcd_reduction": common,
        "destination": list(destination),
        "edge_semantics": "raw_step_inside_root_receipt_only",
    }


def bounded_hit_fiber(
    *,
    R: int,
    K: int,
    witness: list[int],
) -> dict[str, object]:
    """Validate a supplied finite-box witness without enumerating the box."""
    factors = shared.factorization(K)
    if len(witness) != len(factors) or not all(isinstance(value, int) for value in witness):
        raise AssertionError("bounded hit witness has the wrong dimension")
    if any(abs(value) > budget for value, (_q, budget) in zip(witness, factors)):
        raise AssertionError("bounded hit witness lies outside the finite box")
    residue = 1
    for (q, _budget), exponent in zip(factors, witness):
        residue = residue * pow(q, exponent, R) % R
    if residue != R - 1:
        raise AssertionError("bounded hit witness does not reach -1")
    return {
        "classification": "hit",
        "support_factorization": [[q, budget] for q, budget in factors],
        "witness": list(witness),
        "witness_residue": residue,
        "finite_box_hit": True,
        "witness_policy": "provided_bounded_hit",
        "signed_defect": {
            "status": "defined",
            "reason": "bounded_hit_has_no_outside_box_defect",
        },
    }


def materialize_typed_fiber(
    *,
    R: int,
    K: int,
    declaration: dict[str, object],
) -> dict[str, object]:
    """Construct and revalidate one explicit F, hit, or Legendre-G receipt."""
    classification = declaration.get("classification")
    if classification == "F":
        witness = declaration.get("witness")
        if not isinstance(witness, list) or not all(isinstance(value, int) for value in witness):
            raise AssertionError("F declaration requires an integer witness")
        fiber = shared.residue_witness(R, shared.factorization(K), tuple(witness))
    elif classification == "hit":
        witness = declaration.get("witness")
        if not isinstance(witness, list):
            raise AssertionError("hit declaration requires a witness")
        fiber = bounded_hit_fiber(R=R, K=K, witness=witness)
    elif classification == "G":
        conductor = declaration.get("conductor")
        if not isinstance(conductor, int):
            raise AssertionError("G declaration requires a Legendre conductor")
        fiber = shared.legendre_g_fiber(R, K, conductor)
    else:
        raise AssertionError("root entry requires a declared F, hit, or Legendre-G fiber")

    if classification in {"F", "G"} and not shared.fiber_certificate_is_valid(R, K, fiber):
        raise AssertionError("typed fiber certificate did not replay")
    return fiber


def typed_fiber_payload(fiber: dict[str, object]) -> dict[str, object]:
    """Render the classification in the state-contract-facing form."""
    classification = fiber.get("classification")
    if classification in {"F", "hit"}:
        witness = fiber.get("witness")
        signed_defect = fiber.get("signed_defect")
        if not isinstance(witness, list) or not isinstance(signed_defect, dict):
            raise AssertionError("nonempty fiber has no witness or defect payload")
        return {
            "classification": classification,
            "target_fiber": {"status": "nonempty", "witness": witness},
            "signed_defect": {"status": "defined", "data": signed_defect},
        }
    if classification == "G":
        separator = fiber.get("separator")
        signed_defect = fiber.get("signed_defect")
        if not isinstance(separator, dict) or not isinstance(signed_defect, dict):
            raise AssertionError("G fiber has no separating character")
        return {
            "classification": "G",
            "target_fiber": {
                "status": "empty",
                "emptiness_certificate": separator,
            },
            "signed_defect": signed_defect,
        }
    raise AssertionError("unsupported typed fiber classification")


def verify_c3_affine_prime_even_tail_root_entry_v1(
    *,
    h: int,
    a: int,
    b: int,
    fiber_declaration: dict[str, object],
) -> dict[str, object]:
    """Build a conditional c=3 raw-to-overflow root-entry receipt.

    The caller can choose only the arithmetic source-word parameters and an
    independently checkable typed fiber certificate.  Scope, origin, normal
    form, and recursive status are fixed here so this function cannot be used
    as a charged-history adapter or as a recursive transition constructor.
    """
    if h < 3 or a <= 0 or b <= 0:
        raise AssertionError("c=3 parameters must be positive with h >= 3")

    p = 24 * h + 1
    R = 104 * h - 9
    M = 26 * h + 1
    x = p - 3
    K = M * x
    if (R - 1) % b or (R - b) % a or (R - a) % 8:
        raise AssertionError("two-intermediate divisibilities failed")
    alpha = (R - 1) // b
    beta = (R - b) // a
    gamma = (R - a) // 8

    arithmetic_checks = {
        "core_prime": shared.is_prime(p),
        "core_residue": p % 24 == 1,
        "c3_branch": h % 3 != 2,
        "thirteen_capacity_branch": h % 13 != 12,
        "a_b_coprime": gcd(a, b) == 1,
        "a_mod_eight": a % 8 == 7,
        "alpha_prime": shared.is_prime(alpha),
        "beta_prime": shared.is_prime(beta),
        "gamma_prime": shared.is_prime(gamma),
        "R_equals_four_M_minus_thirteen": R == 4 * M - 13,
        "pR_plus_one_equals_four_K": p * R + 1 == 4 * K,
        "canonical_chart": shared.canonical_chart(p, M) == (R, K),
        "high_R": R > p and R % 4 == 3,
        "x_equals_p_minus_three": x == p - 3,
        "C_equals_gcd_x_K": gcd(x, K) == x,
        "carrier_recovers_M": K // x == M,
        "overflow_inequality": 4 * M > R,
        "d_equals_three": p - x == 3,
        "n_equals_thirteen": 4 * M - R == 13,
        "d_dual_determinant": p * 13 == 4 * M * 3 + 1,
    }
    if not all(arithmetic_checks.values()):
        failed = [name for name, passed in arithmetic_checks.items() if not passed]
        raise AssertionError(f"c=3 root-entry arithmetic failed: {failed}")

    # These bounds are a convenient sufficient route to the three variable
    # label capacities, but the root receipt checks those capacities directly
    # on each raw step below.  Keeping this diagnostic separate avoids
    # silently treating a raw-valid control as an instance of a stronger
    # printed sufficient-bound statement.
    sufficient_bound_diagnostics = {
        "alpha_gt_fourteen": alpha > 14,
        "beta_gt_max_b_plus_thirteen_3b_plus_one": beta > max(b + 13, 3 * b + 1),
        "gamma_gt_max_a_plus_thirteen_3a_plus_one": gamma > max(a + 13, 3 * a + 1),
    }
    sufficient_bound_diagnostics["all"] = all(sufficient_bound_diagnostics.values())

    universal_source = shared.high_R_universal_source(p, R)
    source = (p, R * (p - 1) - p, p - 1)
    if universal_source.get("source") != list(source) or universal_source.get("K") != K:
        raise AssertionError("shared high-R universal source no longer matches this chart")
    canonical_anchor = (1, R - 1, 1)
    anchor = (R - 1, 1, 1)
    steps = [
        ordered_raw_step(
            modulus=R,
            K=K,
            source=source,
            selected_coordinate_index=0,
            q=p,
            expected_destination=canonical_anchor,
            name="universal_p_edge",
        ),
        ordered_raw_step(
            modulus=R,
            K=K,
            source=anchor,
            selected_coordinate_index=0,
            q=alpha,
            expected_destination=(b, R - b, 1),
            name="anchor_to_b",
        ),
        ordered_raw_step(
            modulus=R,
            K=K,
            source=(b, R - b, 1),
            selected_coordinate_index=1,
            q=beta,
            expected_destination=(a, R - a, 1),
            name="b_to_a",
        ),
        ordered_raw_step(
            modulus=R,
            K=K,
            source=(a, R - a, 1),
            selected_coordinate_index=1,
            q=2,
            expected_destination=(4 * gamma, R - 4 * gamma, 1),
            name="a_to_4gamma",
        ),
        ordered_raw_step(
            modulus=R,
            K=K,
            source=(4 * gamma, R - 4 * gamma, 1),
            selected_coordinate_index=0,
            q=gamma,
            expected_destination=(4, R - 4, 1),
            name="4gamma_to_4",
        ),
        ordered_raw_step(
            modulus=R,
            K=K,
            source=(4, R - 4, 1),
            selected_coordinate_index=1,
            q=13,
            expected_destination=(R - 4 * x, 4 * x, 1),
            name="4_to_t4",
        ),
        ordered_raw_step(
            modulus=R,
            K=K,
            source=(R - 4 * x, 4 * x, 1),
            selected_coordinate_index=1,
            q=2,
            expected_destination=(2 * x, R - 2 * x, 1),
            name="t4_to_t2",
        ),
        ordered_raw_step(
            modulus=R,
            K=K,
            source=(2 * x, R - 2 * x, 1),
            selected_coordinate_index=0,
            q=2,
            expected_destination=(x, R - x, 1),
            name="t2_to_t1",
        ),
    ]
    if any(step["gcd_reduction"] != 1 for step in steps):
        raise AssertionError("the c=3 template unexpectedly required gcd reduction")

    P = 2 * alpha * beta * gamma
    W = 13 * P
    full_phase = 4 * W
    phase_checks = {
        "P_times_four_is_minus_one": 4 * P % R == R - 1,
        "W_is_minus_M": W % R == (-M) % R,
        "full_word_is_minus_thirteen": full_phase % R == (-13) % R,
    }
    if not all(phase_checks.values()):
        raise AssertionError("c=3 endpoint phase gate failed")
    even_tail = [
        {
            "t": 4,
            "node": [R - 4 * x, 4 * x, 1],
            "even_coordinate_index": 1,
            "phase": W % R,
            "expected_phase": (-M) % R,
        },
        {
            "t": 2,
            "node": [2 * x, R - 2 * x, 1],
            "even_coordinate_index": 0,
            "phase": (2 * W) % R,
            "expected_phase": (-2 * M) % R,
        },
        {
            "t": 1,
            "node": [x, R - x, 1],
            "even_coordinate_index": 0,
            "phase": full_phase % R,
            "expected_phase": (-13) % R,
        },
    ]
    if any(row["phase"] != row["expected_phase"] for row in even_tail):
        raise AssertionError("even-tail phase transcript changed")

    fiber = materialize_typed_fiber(R=R, K=K, declaration=fiber_declaration)
    typed_fiber = typed_fiber_payload(fiber)
    state = shared.make_state(
        prime=p,
        R=R,
        K=K,
        support=1,
        state_class="overflow",
        fiber_class=str(fiber["classification"]),
        source_tree_scope=SOURCE_TREE_SCOPE,
    )
    if not shared.state_id_is_valid(state):
        raise AssertionError("selector-compatible seed state hash failed")

    raw_transcript = {
        "source": list(source),
        "canonical_anchor_after_p": list(canonical_anchor),
        "anchor_orientation": {
            "from": list(canonical_anchor),
            "to": list(anchor),
            "semantics": "coordinate_swap_not_a_raw_transition",
        },
        "steps": steps,
        "labels_after_anchor": [alpha, beta, 2, gamma, 13, 2, 2],
        "phases": {
            "P_to_N_R_4": P % R,
            "W_to_exact_t4": W % R,
            "full_word_to_seed": full_phase % R,
        },
        "even_tail": even_tail,
    }
    raw_entry_digest = "raw-receipt:" + shared.canonical_hash(raw_transcript)
    typed_fiber_digest = "fiber:" + shared.canonical_hash(fiber)
    entry_core = {
        "adapter": ROOT_ENTRY_ADAPTER,
        "certificate_type": CERTIFICATE_TYPE,
        "source_tree_scope": SOURCE_TREE_SCOPE,
        "state_origin": ROOT_ENTRY_ADAPTER,
        "normal_form": NORMAL_FORM,
        "marked_solution_set": "Sol(p)",
        "potential_record": "not_a_transition",
        "seed_state_id": state["state_id"],
        "raw_entry_digest": raw_entry_digest,
        "typed_fiber_digest": typed_fiber_digest,
    }
    entry_id = "root-entry:" + shared.canonical_hash(entry_core)
    local_e1_e3 = {
        "E1": bool(
            universal_source.get("raw_p_edge", {}).get("destination") == list(canonical_anchor)
            and all(step["strict_capacity"] and step["unit_condition"] for step in steps)
            and steps[-1]["destination"] == [x, R - x, 1]
        ),
        "E2": bool(
            arithmetic_checks["canonical_chart"]
            and arithmetic_checks["pR_plus_one_equals_four_K"]
            and arithmetic_checks["C_equals_gcd_x_K"]
            and arithmetic_checks["d_dual_determinant"]
        ),
        "E3": bool(
            shared.state_id_is_valid(state)
            and typed_fiber["classification"] == state["fiber_class"]
            and all(row["phase"] == row["expected_phase"] for row in even_tail)
            and raw_entry_digest.startswith("raw-receipt:")
        ),
    }
    if not all(local_e1_e3.values()):
        raise AssertionError("root-entry E1--E3 receipt did not close")

    return {
        "entry_id": entry_id,
        "entry_core": entry_core,
        "parameters": {
            "h": h,
            "a": a,
            "b": b,
            "p": p,
            "R": R,
            "M": M,
            "x": x,
            "K": K,
            "alpha": alpha,
            "beta": beta,
            "gamma": gamma,
        },
        "arithmetic_checks": arithmetic_checks,
        "sufficient_bound_diagnostics": sufficient_bound_diagnostics,
        "raw_transcript": raw_transcript,
        "seed": {
            "C": x,
            "M": M,
            "t": 1,
            "d": 3,
            "n": 13,
            "state": state,
            "typed_fiber": typed_fiber,
            "fiber_certificate": fiber,
        },
        "local_e1_e3": local_e1_e3,
        "admission": {
            "selector_status": "analysis_evidence",
            "recursive_edge_eligible": False,
            "root_only": True,
            "top_level_only": True,
            "source_tree_scope": SOURCE_TREE_SCOPE,
            "state_origin": ROOT_ENTRY_ADAPTER,
            "normal_form": NORMAL_FORM,
            "potential_record": "not_a_transition",
            "E4": "not_attempted",
            "E5": "not_attempted",
            "terminal_first": "required_before_any_selector_integration",
            "outgoing_raw_policy": (
                "forbidden_by_this_receipt; a future action must bind the raw-entry digest, "
                "tail orientation, and phase into its own state contract"
            ),
            "formal_p_parent_policy": (
                "a locally manufactured q=p predecessor is not a root declaration and "
                "cannot satisfy this adapter's target-source provenance requirement"
            ),
        },
    }


CONTROL_DECLARATIONS = [
    {
        "name": "c3_h3_original_two_intermediate_control",
        "h": 3,
        "a": 7,
        "b": 2,
        "fiber": {"classification": "F", "witness": [-2, 1, 0, 2]},
        "expected": {"p": 73, "alpha": 151, "beta": 43, "gamma": 37},
        "expected_sufficient_bounds": True,
    },
    {
        "name": "c3_h43_mod6_one_control",
        "h": 43,
        "a": 7,
        "b": 46,
        "fiber": {"classification": "F", "witness": [0, -1, 1, 12, 0]},
        "expected": {"p": 1033, "alpha": 97, "beta": 631, "gamma": 557},
        "expected_sufficient_bounds": True,
    },
    {
        "name": "c3_h138_mod6_zero_control",
        "h": 138,
        "a": 79,
        "b": 202,
        "fiber": {"classification": "F", "witness": [0, -3, 0, -2, 0]},
        "expected": {"p": 3313, "alpha": 71, "beta": 179, "gamma": 1783},
        "expected_sufficient_bounds": False,
    },
    {
        "name": "c3_h1114_mod6_four_control",
        "h": 1114,
        "a": 15,
        "b": 2,
        "fiber": {"classification": "F", "witness": [-2, 2, -4, 3, 9]},
        "expected": {"p": 26737, "alpha": 57923, "beta": 7723, "gamma": 14479},
        "expected_sufficient_bounds": True,
    },
]


def build_result() -> dict[str, object]:
    """Replay the four fixed controls covering all allowed c=3 h mod 6 classes."""
    controls: list[dict[str, object]] = []
    for declaration in CONTROL_DECLARATIONS:
        entry = verify_c3_affine_prime_even_tail_root_entry_v1(
            h=int(declaration["h"]),
            a=int(declaration["a"]),
            b=int(declaration["b"]),
            fiber_declaration=dict(declaration["fiber"]),
        )
        parameters = entry["parameters"]
        if not isinstance(parameters, dict):
            raise AssertionError("root-entry parameter payload changed")
        expected = declaration["expected"]
        if not isinstance(expected, dict) or any(parameters.get(key) != value for key, value in expected.items()):
            raise AssertionError(f"{declaration['name']}: fixed arithmetic control changed")
        if entry["sufficient_bound_diagnostics"].get("all") != declaration["expected_sufficient_bounds"]:
            raise AssertionError(f"{declaration['name']}: sufficient-bound diagnostic changed")
        if entry["local_e1_e3"] != {"E1": True, "E2": True, "E3": True}:
            raise AssertionError(f"{declaration['name']}: E1--E3 control changed")
        admission = entry["admission"]
        if not isinstance(admission, dict) or admission.get("recursive_edge_eligible") is not False:
            raise AssertionError(f"{declaration['name']}: root receipt became a recursive edge")
        controls.append({"name": declaration["name"], "entry": entry})

    residues = sorted(entry["entry"]["parameters"]["h"] % 6 for entry in controls)
    if residues != [0, 1, 3, 4]:
        raise AssertionError("fixed controls no longer cover the four c=3 residue classes")
    return {
        "schema_version": 1,
        "certificate_type": CERTIFICATE_TYPE,
        "scope": (
            "Four fixed conditional target-source controls only. This verifier creates a "
            "fresh A=1 root receipt, not a selector edge, recursive action, or E4/E5 proof. "
            "The h=138 control is direct raw evidence, not an instance of the stronger "
            "beta sufficient bound printed in the two-intermediate template."
        ),
        "root_policy": {
            "allowed_origin": ROOT_ENTRY_ADAPTER,
            "allowed_scope": SOURCE_TREE_SCOPE,
            "disallowed": ["charged_history_only", "recursive_edge", "formal_p_parent_only"],
        },
        "controls": controls,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified c=3 even-tail root-entry controls: h=3,43,138,1114")
        return
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
