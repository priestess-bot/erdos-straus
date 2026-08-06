#!/usr/bin/env python3
"""Verify a root-only c=3 factor-block even-tail receipt.

This is the composite-label counterpart of the prime-label root receipt.  It
replays every prime factor in alpha, beta, and gamma as an individual raw step,
then creates only an E1--E3 analysis receipt.  It never registers a selector
edge, runs a coverage scan, or treats a reverse p-parent as a root.
"""

from __future__ import annotations

import argparse
import json
from math import gcd

import type_i_c3_affine_prime_even_tail_root_entry as prime_entry
import type_i_high_r_chart_two_anchor as shared


ROOT_ENTRY_ADAPTER = "c3_factor_block_even_tail_root_entry_v1"
NORMAL_FORM = "c3_factor_block_even_tail_overflow_seed_v1"
SOURCE_TREE_SCOPE = "fresh_source_tree_only"
CERTIFICATE_TYPE = "c3_factor_block_target_source_even_tail_root_entry_v1"


def prime_word(value: int) -> list[int]:
    """Expand a positive integer into its sorted prime-factor word."""
    word: list[int] = []
    for prime, exponent in shared.factorization(value):
        word.extend([prime] * exponent)
    return word


def replay_block(
    *,
    modulus: int,
    K: int,
    source: tuple[int, int, int],
    selected_coordinate_index: int,
    word: list[int],
    endpoint: tuple[int, int, int],
    name: str,
) -> tuple[tuple[int, int, int], list[dict[str, object]]]:
    """Replay one ordered m=1 factor block without treating it as a macro edge."""
    current = source
    side = selected_coordinate_index
    rows: list[dict[str, object]] = []
    for index, prime in enumerate(word):
        left, right, m = current
        selected = left if side == 0 else right
        if m != 1 or selected % prime:
            raise AssertionError(f"{name}: factor word no longer divides selected coordinate")
        selected_after = selected // prime
        # A raw step writes the divided, selected coordinate first regardless
        # of which side of the ordered source carried it.
        expected = (selected_after, modulus - selected_after, 1)
        row = prime_entry.ordered_raw_step(
            modulus=modulus,
            K=K,
            source=current,
            selected_coordinate_index=side,
            q=prime,
            expected_destination=expected,
            name=f"{name}_{index}_{prime}",
        )
        if row["gcd_reduction"] != 1:
            raise AssertionError(f"{name}: factor block unexpectedly reduced a gcd")
        current = expected
        # ordered_raw_step emits the divided coordinate first, so subsequent
        # factors in this block always continue on the left.
        side = 0
        rows.append(row)
    if current != endpoint:
        raise AssertionError(f"{name}: factor word ended at the wrong node")
    return current, rows


def verify_c3_factor_block_even_tail_root_entry_v1(
    *,
    h: int,
    a: int,
    b: int,
    fiber_declaration: dict[str, object],
) -> dict[str, object]:
    """Build a conditional factor-block c=3 root receipt from raw integers."""
    if h < 3 or a <= 0 or b <= 0:
        raise AssertionError("c=3 factor-block parameters must be positive with h >= 3")

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
    if min(alpha, beta, gamma) <= 0:
        raise AssertionError("factor-block labels must be positive")

    arithmetic_checks = {
        "core_prime": shared.is_prime(p),
        "core_residue": p % 24 == 1,
        "c3_branch": h % 3 != 2,
        "thirteen_capacity_branch": h % 13 != 12,
        "a_b_coprime": gcd(a, b) == 1,
        "a_mod_eight": a % 8 == 7,
        "R_equals_four_M_minus_thirteen": R == 4 * M - 13,
        "pR_plus_one_equals_four_K": p * R + 1 == 4 * K,
        "canonical_chart": shared.canonical_chart(p, M) == (R, K),
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
        raise AssertionError(f"c=3 factor-block arithmetic failed: {failed}")

    words = {
        "alpha": prime_word(alpha),
        "beta": prime_word(beta),
        "gamma": prime_word(gamma),
    }
    source = (p, R * (p - 1) - p, p - 1)
    universal_source = shared.high_R_universal_source(p, R)
    if universal_source.get("source") != list(source) or universal_source.get("K") != K:
        raise AssertionError("shared high-R universal source no longer matches this chart")

    canonical_anchor = (1, R - 1, 1)
    anchor = (R - 1, 1, 1)
    source_step = prime_entry.ordered_raw_step(
        modulus=R,
        K=K,
        source=source,
        selected_coordinate_index=0,
        q=p,
        expected_destination=canonical_anchor,
        name="universal_p_edge",
    )
    _, alpha_rows = replay_block(
        modulus=R,
        K=K,
        source=anchor,
        selected_coordinate_index=0,
        word=words["alpha"],
        endpoint=(b, R - b, 1),
        name="alpha_block",
    )
    _, beta_rows = replay_block(
        modulus=R,
        K=K,
        source=(b, R - b, 1),
        selected_coordinate_index=1,
        word=words["beta"],
        endpoint=(a, R - a, 1),
        name="beta_block",
    )
    entry_gamma = prime_entry.ordered_raw_step(
        modulus=R,
        K=K,
        source=(a, R - a, 1),
        selected_coordinate_index=1,
        q=2,
        expected_destination=(4 * gamma, R - 4 * gamma, 1),
        name="enter_gamma_block",
    )
    _, gamma_rows = replay_block(
        modulus=R,
        K=K,
        source=(4 * gamma, R - 4 * gamma, 1),
        selected_coordinate_index=0,
        word=words["gamma"],
        endpoint=(4, R - 4, 1),
        name="gamma_block",
    )
    tail_13 = prime_entry.ordered_raw_step(
        modulus=R,
        K=K,
        source=(4, R - 4, 1),
        selected_coordinate_index=1,
        q=13,
        expected_destination=(R - 4 * x, 4 * x, 1),
        name="tail_13",
    )
    tail_2a = prime_entry.ordered_raw_step(
        modulus=R,
        K=K,
        source=(R - 4 * x, 4 * x, 1),
        selected_coordinate_index=1,
        q=2,
        expected_destination=(2 * x, R - 2 * x, 1),
        name="tail_2a",
    )
    tail_2b = prime_entry.ordered_raw_step(
        modulus=R,
        K=K,
        source=(2 * x, R - 2 * x, 1),
        selected_coordinate_index=0,
        q=2,
        expected_destination=(x, R - x, 1),
        name="tail_2b",
    )
    all_rows = [source_step, *alpha_rows, *beta_rows, entry_gamma, *gamma_rows, tail_13, tail_2a, tail_2b]
    if any(not row["strict_capacity"] or not row["unit_condition"] for row in all_rows):
        raise AssertionError("factor-block raw capacity or unit condition failed")

    P = 2 * alpha * beta * gamma
    W = 13 * P
    phase_checks = {
        "P_times_four_is_minus_one": 4 * P % R == R - 1,
        "W_is_minus_M": W % R == (-M) % R,
        "full_word_is_minus_thirteen": 4 * W % R == R - 13,
    }
    if not all(phase_checks.values()):
        raise AssertionError("factor-block endpoint phase gate failed")

    even_tail = [
        {"t": 4, "node": [R - 4 * x, 4 * x, 1], "phase": W % R, "expected_phase": (-M) % R},
        {"t": 2, "node": [2 * x, R - 2 * x, 1], "phase": (2 * W) % R, "expected_phase": (-2 * M) % R},
        {"t": 1, "node": [x, R - x, 1], "phase": (4 * W) % R, "expected_phase": (-13) % R},
    ]
    if any(row["phase"] != row["expected_phase"] for row in even_tail):
        raise AssertionError("factor-block even-tail phase transcript changed")

    fiber = prime_entry.materialize_typed_fiber(R=R, K=K, declaration=fiber_declaration)
    typed_fiber = prime_entry.typed_fiber_payload(fiber)
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
        raise AssertionError("factor-block seed state hash failed")

    raw_transcript = {
        "source": list(source),
        "canonical_anchor_after_p": list(canonical_anchor),
        "anchor_orientation": {
            "from": list(canonical_anchor),
            "to": list(anchor),
            "semantics": "coordinate_swap_not_a_raw_transition",
        },
        "factor_words": words,
        "steps": all_rows,
        "phases": {
            "P_to_N_R_4": P % R,
            "W_to_exact_t4": W % R,
            "full_word_to_seed": 4 * W % R,
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
            and all(row["strict_capacity"] and row["unit_condition"] for row in all_rows)
            and tail_2b["destination"] == [x, R - x, 1]
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
        raise AssertionError("factor-block root-entry E1--E3 receipt did not close")

    return {
        "entry_id": entry_id,
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
        "factor_words": words,
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
            "outgoing_raw_policy": "forbidden_by_this_receipt",
            "formal_p_parent_policy": "formal_p_parent_only_is_not_a_root_declaration",
        },
    }


CONTROL = {
    "name": "c3_h297_composite_beta_gamma_control",
    "h": 297,
    "a": 7,
    "b": 2,
    "fiber": {"classification": "F", "witness": [-2, 0, -5, 8]},
    "expected": {
        "p": 7129,
        "alpha": 15439,
        "beta": 4411,
        "gamma": 3859,
        "factor_words": {"alpha": [15439], "beta": [11, 401], "gamma": [17, 227]},
    },
}


def build_result() -> dict[str, object]:
    """Replay one non-prime-label control, without a range search."""
    entry = verify_c3_factor_block_even_tail_root_entry_v1(
        h=int(CONTROL["h"]),
        a=int(CONTROL["a"]),
        b=int(CONTROL["b"]),
        fiber_declaration=dict(CONTROL["fiber"]),
    )
    expected = CONTROL["expected"]
    parameters = entry["parameters"]
    if not isinstance(parameters, dict):
        raise AssertionError("factor-block parameter payload changed")
    for key in ("p", "alpha", "beta", "gamma"):
        if parameters.get(key) != expected[key]:
            raise AssertionError(f"factor-block control changed: {key}")
    if entry["factor_words"] != expected["factor_words"]:
        raise AssertionError("factor-block prime word changed")
    if entry["local_e1_e3"] != {"E1": True, "E2": True, "E3": True}:
        raise AssertionError("factor-block E1--E3 control changed")
    return {
        "certificate_type": CERTIFICATE_TYPE,
        "scope": (
            "One composite-label root-only control. The receipt is analysis evidence, "
            "not a selector edge, E4/E5 proof, or terminal coverage claim."
        ),
        "control": {"name": CONTROL["name"], "entry": entry},
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified c=3 factor-block root-entry control: h=297")
        return
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
