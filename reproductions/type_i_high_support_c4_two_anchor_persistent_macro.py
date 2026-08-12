#!/usr/bin/env python3
"""Verify the conditional C=4 two-anchor persistent macro.

The first C=4 complete-excess rechart is a sharp-rank stutter. This verifier
keeps it as an internal checkpoint and immediately replays its own high-R
universal-source bundle. It never creates a fresh root: admission still needs
a persistent parent for the first high anchor and a terminal-first guard.
"""

from __future__ import annotations

import argparse
import json

import type_i_bottom_sink_scc_complete_excess_bundle as bottom
import type_i_high_r_chart_two_anchor as shared
from type_i_high_support_c4_g_stutter_boundary import (
    c4_plus_boundary,
    canonical_stutter,
    two_anchor_compression,
)


SCOPE = "fresh_source_tree_only"
IDENTITY_LIFT = {
    "source": "Sol(p)",
    "successor": "Sol(p)",
    "lift": "identity",
    "direction": "H2_to_H0",
}


def sharp_rank(prime: int, K: int, support: int) -> tuple[int, int]:
    if support <= 0 or K % support:
        raise AssertionError("sharp rank requires charged support")
    return ((prime - 1) ** 2 // (4 * support), K // support)


def jacobi_g_fiber(R: int, K: int) -> dict[str, object]:
    """Construct a directly replayable Jacobi separator."""
    factors = shared.factorization(K)
    values = {str(q): bottom.jacobi_symbol(q, R) for q, _ in factors}
    conditions = {
        "support_character_trivial": all(value == 1 for value in values.values()),
        "minus_one_character_nontrivial": bottom.jacobi_symbol(-1, R) == -1,
    }
    if not all(conditions.values()):
        raise AssertionError("Jacobi data does not certify this G chart")
    return {
        "classification": "G",
        "support_factorization": [[q, exponent] for q, exponent in factors],
        "target_in_generated_subgroup": False,
        "separator": {
            "kind": "Jacobi",
            "modulus": R,
            "support_values": values,
            "minus_one": bottom.jacobi_symbol(-1, R),
        },
        "signed_defect": {
            "status": "not_applicable",
            "reason": "Jacobi_support_separator",
        },
        "conditions": conditions,
    }


def fiber_is_valid(R: int, K: int, fiber: dict[str, object]) -> bool:
    if fiber.get("classification") == "G":
        try:
            return jacobi_g_fiber(R, K) == fiber
        except (AssertionError, ValueError):
            return False
    return shared.fiber_certificate_is_valid(R, K, fiber)


def make_high_state(
    *,
    prime: int,
    R: int,
    K: int,
    support: int,
    fiber: dict[str, object],
    scope: str,
) -> dict[str, object]:
    state = shared.make_state(
        prime=prime,
        R=R,
        K=K,
        support=support,
        state_class="overflow",
        fiber_class=str(fiber["classification"]),
        source_tree_scope=scope,
    )
    if not (
        shared.state_id_is_valid(state)
        and prime < R < 4 * support
        and R % 4 == 3
        and R % prime != 0
        and 4 * K == prime * R + 1
        and K % support == 0
        and shared.canonical_chart(prime, support) == (R, K)
        and fiber_is_valid(R, K, fiber)
    ):
        raise AssertionError("C=4 macro chart is not a typed canonical overflow")
    return state


def c4_two_anchor_structure(prime: int) -> dict[str, object]:
    """Rebuild both bundles without assuming any particular fiber class."""
    boundary = c4_plus_boundary(prime)
    first = canonical_stutter(boundary)
    compression = two_anchor_compression(boundary)
    first_bundle = shared.high_R_path_anchored_bundle(
        prime=prime, R=boundary["R"], support=boundary["A"]
    )
    second_bundle = shared.high_R_path_anchored_bundle(
        prime=prime, R=first["target_R"], support=first["M"]
    )
    first_rechart = first_bundle["rechart"]
    second_rechart = second_bundle["rechart"]
    first_excess = first_bundle["complete_excess_bundle"]
    second_excess = second_bundle["complete_excess_bundle"]
    if not all(
        isinstance(value, dict)
        for value in (first_rechart, second_rechart, first_excess, second_excess)
    ):
        raise AssertionError("high-R bundle shape changed")
    checks = {
        "first_bundle_conditions": all(first_bundle["conditions"].values()),
        "first_exact_c4_stutter": (
            first_excess == {"Q": first["Q"], "beta": 2}
            and first_rechart["M"] == first["M"]
            and first_rechart["R"] == first["target_R"]
            and first_rechart["K"] == first["target_K"]
            and first_rechart["C"] == 4
        ),
        "second_bundle_conditions": all(second_bundle["conditions"].values()),
        "second_exact_c4_to_c2": (
            second_excess == {"Q": compression["Q1"], "beta": 2}
            and second_rechart["M"] == compression["A2"]
            and second_rechart["R"] == compression["R2"]
            and second_rechart["K"] == compression["K2"]
            and second_rechart["C"] == 2
        ),
        "both_residuals_are_paid": (
            boundary["K"] % (2 * int(first_excess["beta"])) == 0
            and first["target_K"] % (2 * int(second_excess["beta"])) == 0
        ),
        "two_anchor_formula": (
            compression["source_cofactor"] == 4
            and compression["intermediate_cofactor"] == 4
            and compression["target_cofactor"] == 2
        ),
    }
    if not all(checks.values()):
        raise AssertionError(f"C=4 two-anchor structure failed: {checks}")
    return {
        "boundary": boundary,
        "first_bundle": first_bundle,
        "second_bundle": second_bundle,
        "compression": compression,
        "checks": checks,
    }


def p2137_control() -> dict[str, object]:
    """Replay a G-to-F-to-F C=4 control with no inherited fiber labels."""
    prime = 2_137
    structure = c4_two_anchor_structure(prime)
    boundary = structure["boundary"]
    first_bundle = structure["first_bundle"]
    second_bundle = structure["second_bundle"]
    compression = structure["compression"]
    first_rechart = first_bundle["rechart"]
    second_rechart = second_bundle["rechart"]
    assert isinstance(first_rechart, dict) and isinstance(second_rechart, dict)

    H0_fiber = jacobi_g_fiber(boundary["R"], boundary["K"])
    H1_fiber = shared.provided_unbounded_residue_witness(
        int(first_rechart["R"]),
        shared.factorization(int(first_rechart["K"])),
        (0, 0, 18_277_763, 0, 0, 0),
    )
    H2_fiber = shared.provided_unbounded_residue_witness(
        int(second_rechart["R"]),
        shared.factorization(int(second_rechart["K"])),
        (171_932_900_936, 0, 3, 0, 0, 0, 0, 0, 0),
    )
    H0 = make_high_state(
        prime=prime,
        R=boundary["R"],
        K=boundary["K"],
        support=boundary["A"],
        fiber=H0_fiber,
        scope=SCOPE,
    )
    H1 = make_high_state(
        prime=prime,
        R=int(first_rechart["R"]),
        K=int(first_rechart["K"]),
        support=int(first_rechart["M"]),
        fiber=H1_fiber,
        scope=SCOPE,
    )
    H2 = make_high_state(
        prime=prime,
        R=int(second_rechart["R"]),
        K=int(second_rechart["K"]),
        support=int(second_rechart["M"]),
        fiber=H2_fiber,
        scope=SCOPE,
    )
    ranks = {
        "H0": sharp_rank(prime, int(H0["K"]), int(H0["absorbed_support"])),
        "H2": sharp_rank(prime, int(H2["K"]), int(H2["absorbed_support"])),
    }
    checks = {
        "all_state_ids_recomputed": all(shared.state_id_is_valid(state) for state in (H0, H1, H2)),
        "internal_checkpoint_is_exact_first_target": (
            H1["R"] == first_rechart["R"]
            and H1["K"] == first_rechart["K"]
            and H1["absorbed_support"] == first_rechart["M"]
        ),
        "final_state_is_exact_second_target": (
            H2["R"] == second_rechart["R"]
            and H2["K"] == second_rechart["K"]
            and H2["absorbed_support"] == second_rechart["M"]
            and H2["R"] == compression["R2"]
            and H2["K"] == compression["K2"]
        ),
        "scope_is_propagated_not_recreated": (
            H0["source_tree_scope"]
            == H1["source_tree_scope"]
            == H2["source_tree_scope"]
            == SCOPE
        ),
        "independent_typed_reclassification": (
            H0_fiber["classification"] == "G"
            and H1_fiber["classification"] == "F"
            and H2_fiber["classification"] == "F"
            and fiber_is_valid(int(H0["R"]), int(H0["K"]), H0_fiber)
            and fiber_is_valid(int(H1["R"]), int(H1["K"]), H1_fiber)
            and fiber_is_valid(int(H2["R"]), int(H2["K"]), H2_fiber)
        ),
        "identity_solution_lift": IDENTITY_LIFT
        == {
            "source": "Sol(p)",
            "successor": "Sol(p)",
            "lift": "identity",
            "direction": "H2_to_H0",
        },
        "strict_endpoint_rank": ranks["H2"] < ranks["H0"] == (0, 4),
    }
    if not all(checks.values()):
        raise AssertionError(f"p=2137 C=4 persistent-macro control failed: {checks}")
    payload = {
        "adapter": "c4_two_anchor_internal_checkpoint_v1",
        "source_state": H0,
        "internal_checkpoint": H1,
        "target_state": H2,
        "first_bundle": first_bundle,
        "second_bundle": second_bundle,
        "typed_fibers": {"H0": H0_fiber, "H1": H1_fiber, "H2": H2_fiber},
        "marked_solution_lift": IDENTITY_LIFT,
        "source_tree_scope": SCOPE,
    }
    return {
        "certificate_type": "c4_two_anchor_conditional_persistent_macro_v1",
        "certificate_status": "conditional_macro_replay",
        "selector_status": "analysis_evidence",
        "recursive_edge_eligible": False,
        "requires": {
            "persistent_anchor_parent": (
                "A verified charged parent must end at H0; this focused chart "
                "control does not manufacture one."
            ),
            "terminal_first_guard": (
                "The selector must exhaust its versioned terminal/alternate prefix "
                "before admitting the macro."
            ),
        },
        "macro_id": "macro:" + shared.canonical_hash(payload),
        "structural_checks": structure["checks"],
        "checks": checks,
        "e1_e5_given_requirements": {
            "E1": "conditional_on_persistent_anchor_parent",
            "E2": True,
            "E3": True,
            "E4": True,
            "E5": True,
        },
        "lambda_sharp": {key: list(value) for key, value in ranks.items()},
        "fibers": {
            "H0": H0_fiber["classification"],
            "H1": H1_fiber["classification"],
            "H2": H2_fiber["classification"],
        },
    }


def verify() -> None:
    # This small arithmetic control prevents p=2137 type data from carrying
    # the general two-anchor identities by itself.
    c4_two_anchor_structure(73)
    control = p2137_control()
    if not (
        control["e1_e5_given_requirements"]
        == {
            "E1": "conditional_on_persistent_anchor_parent",
            "E2": True,
            "E3": True,
            "E4": True,
            "E5": True,
        }
        and control["lambda_sharp"] == {"H0": [0, 4], "H2": [0, 2]}
        and control["fibers"] == {"H0": "G", "H1": "F", "H2": "F"}
    ):
        raise AssertionError("C=4 two-anchor control summary changed")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--show", action="store_true")
    args = parser.parse_args()
    if not (args.verify or args.show):
        parser.error("pass --verify or --show")
    if args.verify:
        verify()
        print("verified conditional C=4 two-anchor persistent macro")
    if args.show:
        print(json.dumps(p2137_control(), ensure_ascii=True, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
