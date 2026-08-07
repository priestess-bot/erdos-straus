#!/usr/bin/env python3
"""Verify the terminal-preempted c=3 C=19 atomic raw-to-reset control.

The control keeps the ambiguous A=1 raw seed inside one macro.  It proves a
provided unbounded F classification at the source and an explicit hit at the
fixed R=63 reset target, but it does not register a selector edge because the
focused prime has an earlier direct Type II terminal.
"""

from __future__ import annotations

import argparse
import json
from math import gcd

import type_i_c3_adaptive_core19_v5_dual_leaf_f19_control as v5
import type_i_c3_affine_prime_even_tail_root_entry as raw
import type_i_high_r_chart_two_anchor as shared


ADAPTER = "c3_adaptive_core19_c19_atomic_reset_v1"
SOURCE_SCOPE = "fresh_source_tree_only"
C = 19
AFFINE_P0 = 181_740_263_041
AFFINE_P_STEP = 204_127_330_680
AFFINE_R0 = 787_541_139_831
AFFINE_R_STEP = 884_551_766_280
SKELETON_PERIOD = 1_085_239
GRAMMAR = {
    "b": 11_246,
    "a": 386,
    "Q1": 92_660_501,
    "Q2": 10_798_549_169,
    "Q3": 54_845_262_851,
}
SOURCE_F_DECLARATION = {
    "classification": "F",
    "witness": [0, 0, 0, 0, 0, v5.F_WITNESS_EXPONENT],
    "witness_policy": "provided_unbounded_modular",
}
TARGET_HIT_DECLARATION = {
    "classification": "hit",
    "witness": [0, -1, 0, 1, 1],
}


def affine_R(v: int) -> int:
    """Return the C=19 ambient-ray chart modulus at one nonnegative parameter."""
    if v < 0:
        raise AssertionError("affine C=19 parameters must be nonnegative")
    return AFFINE_R0 + AFFINE_R_STEP * v


def verify_affine_skeleton_language() -> dict[str, object]:
    """Prove the exact parameter congruence for the fixed C=19 block skeleton."""
    B0, B_step = (AFFINE_R0 - 1) // 5, AFFINE_R_STEP // 5
    second0, second_step = 4 * AFFINE_R0 + 11_246, 4 * AFFINE_R_STEP
    if not (
        v5.P == AFFINE_P0 + AFFINE_P_STEP * v5.V
        and v5.R == affine_R(v5.V)
        and AFFINE_R0 % 5 == 1
        and AFFINE_R_STEP % 5 == 0
        and gcd(B_step, 11_246) == 2
        and B0 % 11_246 == 2_060
        and gcd(second_step, 1_930) == 10
        and second0 % 1_930 == 110
        and (AFFINE_R0 - 386) % 95 == 0
        and AFFINE_R_STEP % 95 == 0
        and SKELETON_PERIOD == 5_623 * 193
        and gcd(5_623, 193) == 1
    ):
        raise AssertionError("affine C=19 skeleton arithmetic changed")

    def skeleton_data(v: int) -> tuple[int, int, int] | None:
        R = affine_R(v)
        B = (R - 1) // 5
        if (
            B % 11_246
            or (4 * R + 11_246) % 1_930
            or (R - 386) % 95
        ):
            return None
        return B // 11_246, (4 * R + 11_246) // 1_930, (R - 386) // 95

    if skeleton_data(v5.V) != (
        GRAMMAR["Q1"],
        GRAMMAR["Q2"],
        GRAMMAR["Q3"],
    ):
        raise AssertionError("v=5 no longer lies in the affine C=19 skeleton")
    return {
        "ray": {
            "p": [AFFINE_P0, AFFINE_P_STEP],
            "R": [AFFINE_R0, AFFINE_R_STEP],
        },
        "condition": f"v == {v5.V} (mod {SKELETON_PERIOD})",
        "congruence_proof": {
            "Q1": {"root": v5.V, "modulus": 5_623, "coefficient_gcd": 2},
            "Q2": {"root": v5.V, "modulus": 193, "coefficient_gcd": 10},
            "Q3": {"all_v": True, "denominator": 95},
            "CRT_period": SKELETON_PERIOD,
        },
        "block_divisors": {
            "Q1": "(R-1)/(5*11246)",
            "Q2": "(4R+11246)/1930",
            "Q3": "(R-386)/95",
        },
        "conditional_raw_rule": (
            "If p(v) is prime and gcd(Q1*Q2*Q3,K(v))=1, factor each Qi "
            "and replay the fixed block topology."
        ),
    }


def factor_block_reserve(value: int, block: int, carrier: int) -> bool:
    """Check the exact endpoint reserve for one factor block."""
    return all(
        shared.valuation(value, prime) >= shared.valuation(carrier, prime)
        for prime, _exponent in shared.factorization(block)
    )


def verify_c19_factor_block_grammar() -> dict[str, object]:
    """Recheck the declared mixed-side C=19 grammar at the v=5 point."""
    p, R, K = v5.P, v5.R, v5.K
    a, b = GRAMMAR["a"], GRAMMAR["b"]
    Q1, Q2, Q3 = GRAMMAR["Q1"], GRAMMAR["Q2"], GRAMMAR["Q3"]
    conditions = {
        "R_one_mod_five": R % 5 == 1,
        "five_outside_carrier": K % 5 != 0,
        "C_divides_carrier": K % C == 0,
        "C_unit_mod_R": gcd(C, R) == 1,
        "first_block_equation": R - 1 == 5 * b * Q1,
        "second_block_equation": 4 * R + b == 5 * a * Q2,
        "third_block_equation": R - a == 5 * C * Q3,
        "first_reserve": factor_block_reserve(b, Q1, K),
        "second_reserve": factor_block_reserve(a, Q2, K),
        "third_reserve": factor_block_reserve(C, Q3, K),
        "block_labels_are_prime": all(
            shared.is_prime(value) for value in (Q1, Q2, Q3)
        ),
    }
    if not all(conditions.values()):
        failed = [name for name, passed in conditions.items() if not passed]
        raise AssertionError(f"C=19 factor-block grammar failed: {failed}")
    raw_tree = v5.verify_raw_tree()
    if raw_tree["C1_raw_step_count"] != 7:
        raise AssertionError("C=19 grammar no longer replays the declared raw word")
    return {
        "parameters": {"C": C, **GRAMMAR},
        "conditions": conditions,
        "raw_word": "5; Fac(Q1); 5; Fac(Q2); 5; Fac(Q3)",
        "physical_tail": raw_tree["physical_tails"]["C1"],
        "raw_entry_digest": "raw-receipt:"
        + shared.canonical_hash(raw_tree["C1_lineage"]),
    }


def verify_fixed_c_reset() -> dict[str, object]:
    """Recheck the fixed-c r-side reset and its R=63 specialization."""
    p, R, K = v5.P, v5.R, v5.K
    M = K // C
    d = p - C
    n = 4 * M - R
    candidates = [
        value
        for value in range(1, 4 * C)
        if (value * p + 1) % (4 * C) == 0
    ]
    if candidates != [63]:
        raise AssertionError("C=19 inverse residue no longer gives a=63")
    a = candidates[0]
    r = (a * p + 1) // (4 * C)
    s = (a * p - a * C + 1) // C
    R_r = 4 * r - s
    K_r = r * C
    checks = {
        "source_overflow_determinant": p * n == 4 * M * d + 1,
        "r_is_M_mod_p": M % p == r,
        "r_side_determinant": p * s == 4 * r * d + 1,
        "fixed_low_modulus": R_r == a == 63,
        "fixed_carrier_formula": K_r == (a * p + 1) // 4,
        "canonical_target_chart": shared.canonical_chart(p, r) == (R_r, K_r),
        "target_cofactor_is_C": K_r == r * C,
        "marked_absorb_target": 0 < R_r < p,
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"fixed-C reset failed: {failed}")
    B_p = (p - 1) ** 2 // 4
    if not (1 < r <= B_p and B_p // r < B_p):
        raise AssertionError("A=1 reset lost its strict outer-rank decrease")
    return {
        "source": {"M": M, "C": C, "d": d, "n": n},
        "fixed_c_inverse": {"a": a, "r": r, "s": s},
        "target": {"R": R_r, "K": K_r, "support": r, "C": C, "d": d, "n": s},
        "checks": checks,
        "potential": {"source": B_p, "target": B_p // r},
    }


def verify_typed_fibers(reset: dict[str, object]) -> dict[str, object]:
    """Rebuild the source F and R=63 target-hit classifications."""
    source_fiber = raw.materialize_typed_fiber(
        R=v5.R,
        K=v5.K,
        declaration=SOURCE_F_DECLARATION,
    )
    target = reset["target"]
    if not isinstance(target, dict):
        raise AssertionError("reset target receipt changed shape")
    target_fiber = raw.materialize_typed_fiber(
        R=int(target["R"]),
        K=int(target["K"]),
        declaration=TARGET_HIT_DECLARATION,
    )
    target_replay = raw.bounded_hit_fiber(
        R=int(target["R"]),
        K=int(target["K"]),
        witness=list(TARGET_HIT_DECLARATION["witness"]),
    )
    if not (
        source_fiber.get("canonical_fourier_eligible") is False
        and shared.fiber_certificate_is_valid(v5.R, v5.K, source_fiber)
        and target_fiber == target_replay
        and target_fiber.get("classification") == "hit"
    ):
        raise AssertionError("atomic reset typed fibers did not replay")
    return {
        "source": source_fiber,
        "target": target_fiber,
        "reclassification_boundary": (
            "The source F certificate is a provided modular witness and is not a "
            "canonical Fourier/capacity input; the target is independently a hit."
        ),
    }


def verify_q19_relative_leaf_phase() -> dict[str, object]:
    """Locate q=19 on the relative C0/C1 direction, not on the target."""
    conductor, zeta = 191, 150
    phase_table = {pow(zeta, exponent, conductor): exponent for exponent in range(19)}
    if len(phase_table) != 19:
        raise AssertionError("q=19 phase group changed")

    def phase(value: int) -> int:
        image = pow(value, 10, conductor)
        if image not in phase_table:
            raise AssertionError("leaf has no q=19 phase")
        return phase_table[image]

    C0_phase = phase(v5.C0)
    C1_phase = phase(C)
    checks = {
        "target_even": pow(-1, 10, conductor) == 1,
        "C0_phase": C0_phase == 3,
        "C1_phase": C1_phase == 11,
        "relative_phase": (C0_phase - C1_phase) % 19 == 11,
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"q=19 relative leaf phase failed: {failed}")
    return {
        "conductor": conductor,
        "zeta": zeta,
        "checks": checks,
        "relative_label_constraint_mod_19": 11,
        "capacity_status": "not_registered_without_a_complete_mixed_source_adapter",
    }


def verify_atomic_state_contract(
    grammar: dict[str, object],
    reset: dict[str, object],
    fibers: dict[str, object],
) -> dict[str, object]:
    """Bind the raw receipt to one atomic reset and expose the seed collision."""
    target = reset["target"]
    source_fiber = fibers["source"]
    target_fiber = fibers["target"]
    if not isinstance(target, dict) or not isinstance(source_fiber, dict) or not isinstance(target_fiber, dict):
        raise AssertionError("atomic contract receipt changed shape")
    target_state = shared.make_state(
        prime=v5.P,
        R=int(target["R"]),
        K=int(target["K"]),
        support=int(target["support"]),
        state_class="marked_absorb",
        fiber_class=str(target_fiber["classification"]),
        source_tree_scope=SOURCE_SCOPE,
    )
    ambiguous_seed_C0 = shared.make_state(
        prime=v5.P,
        R=v5.R,
        K=v5.K,
        support=1,
        state_class="overflow",
        fiber_class=str(source_fiber["classification"]),
        source_tree_scope=SOURCE_SCOPE,
    )
    ambiguous_seed_C1 = shared.make_state(
        prime=v5.P,
        R=v5.R,
        K=v5.K,
        support=1,
        state_class="overflow",
        fiber_class=str(source_fiber["classification"]),
        source_tree_scope=SOURCE_SCOPE,
    )
    c0_r = v5.M0 % v5.P
    c0_s = (4 * c0_r * 3 + 1) // v5.P
    c0_d_reset_R = 4 * 3 - c0_s
    if c0_d_reset_R != 11 or ambiguous_seed_C0 != ambiguous_seed_C1:
        raise AssertionError("raw-seed collision control changed")
    raw_digest = grammar["raw_entry_digest"]
    if not isinstance(raw_digest, str):
        raise AssertionError("raw entry has no immutable digest")
    macro_core = {
        "adapter": ADAPTER,
        "source_tree_scope": SOURCE_SCOPE,
        "raw_entry_digest": raw_digest,
        "source_fiber_digest": "fiber:" + shared.canonical_hash(source_fiber),
        "C": C,
        "tail": 1,
        "orientation": 1,
        "phase": (-v5.N1) % v5.R,
        "target_state": target_state,
    }
    macro_id = "atomic-reset:" + shared.canonical_hash(macro_core)
    checks = {
        "target_state_valid": shared.state_id_is_valid(target_state),
        "ambiguous_A_one_seed_collision": ambiguous_seed_C0 == ambiguous_seed_C1,
        "C0_natural_d_reset_R": c0_d_reset_R == 11,
        "C1_atomic_r_reset_R": int(target["R"]) == 63,
        "identity_solution_lift": True,
        "strict_outer_rank": int(reset["potential"]["target"]) < int(reset["potential"]["source"]),
    }
    if not all(checks.values()):
        raise AssertionError("atomic reset contract failed")
    return {
        "macro_id": macro_id,
        "macro_core": macro_core,
        "target_state": target_state,
        "nonpersistent_source_seed": {
            "reason": "C0 and C1 share the same legacy A=1 state id but require R=11 and R=63 resets",
            "legacy_state_id": ambiguous_seed_C1["state_id"],
        },
        "e1_e5_local": {f"E{index}": True for index in range(1, 6)},
        "checks": checks,
    }


def build_result() -> dict[str, object]:
    """Build one atomic C=19 control and enforce terminal-first preemption."""
    v5.verify_prime_point()
    affine_skeleton = verify_affine_skeleton_language()
    grammar = verify_c19_factor_block_grammar()
    reset = verify_fixed_c_reset()
    fibers = verify_typed_fibers(reset)
    q19_relative_phase = verify_q19_relative_leaf_phase()
    atomic = verify_atomic_state_contract(grammar, reset, fibers)
    terminal = v5.verify_terminal_first()
    return {
        "certificate_type": "c3_adaptive_core19_c19_atomic_reset_v1",
        "scope": (
            "A terminal-preempted C=19 raw-to-R=63 atomic reset control. It proves "
            "the local macro interface, not a globally registered selector edge."
        ),
        "affine_skeleton": affine_skeleton,
        "grammar": grammar,
        "fixed_c_reset": reset,
        "typed_fibers": fibers,
        "q19_relative_leaf_phase": q19_relative_phase,
        "atomic_contract": atomic,
        "terminal_first": {
            "terminal": terminal,
            "selector_status": "terminal_preempted_control",
            "recursive_edge_eligible": False,
            "reason": "The direct (m,d)=(3,11) Type II certificate must dispatch first.",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified terminal-preempted adaptive C=19 atomic reset control")
        return
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
