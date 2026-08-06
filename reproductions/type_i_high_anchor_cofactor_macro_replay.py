#!/usr/bin/env python3
"""Replay direct high-cofactor macros as parent -> H -> transient S -> T.

This is deliberately separate from the selector's legacy direct S-to-T
charged-parent registry.  It independently reconstructs the three-link macro
and checks E1--E5 with the Lambda_p rank on the persistent H-to-T macro edge.
"""

from __future__ import annotations

import argparse
import json
from math import gcd, lcm
from pathlib import Path
from typing import Callable

from short_certificate import type_i_normal_form_certificate, verify_certificate
import type_i_high_r_chart_two_anchor as shared
import type_i_high_r_chart_60913_h2_nonreturn as h2_g_fixture


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-high-anchor-cofactor-macro-replay-results.json"

FiberVerifier = Callable[[int, int, dict[str, object]], bool]
ParentVerifier = Callable[[dict[str, object], dict[str, object]], bool]

PARENT_IDENTITY_LIFT = {
    "source": "Sol(p)",
    "successor": "Sol(p)",
    "lift": "identity",
}
MACRO_IDENTITY_LIFT = {
    "source": "Sol(p)",
    "successor": "Sol(p)",
    "lift": "identity",
    "direction": "T_to_H",
}
MACRO_REPLAY_ADAPTER = "high_anchor_cofactor_macro_replay_v1"


def all_checks_pass(checks: object) -> bool:
    return isinstance(checks, dict) and all(bool(value) for value in checks.values())


def verifier_identity(verifier: Callable[..., object]) -> str:
    return f"{verifier.__module__}.{verifier.__qualname__}"


def typed_fiber_payload(fiber: dict[str, object]) -> dict[str, object]:
    """Translate a local F/G certificate into the state-contract representation."""
    classification = fiber.get("classification")
    signed_defect = fiber.get("signed_defect")
    if classification in {"F", "hit"}:
        witness = fiber.get("witness")
        if not isinstance(witness, list) or not isinstance(signed_defect, dict):
            raise AssertionError("F/hit fiber lacks its typed witness or defect")
        return {
            "classification": classification,
            "target_fiber": {"status": "nonempty", "witness": witness},
            "signed_defect": {"status": "defined", "data": signed_defect},
        }
    if classification == "G":
        separator = fiber.get("separator")
        if (
            not isinstance(separator, dict)
            or not isinstance(signed_defect, dict)
            or signed_defect.get("status") != "not_applicable"
        ):
            raise AssertionError("G fiber lacks its typed emptiness certificate")
        return {
            "classification": "G",
            "target_fiber": {
                "status": "empty",
                "emptiness_certificate": separator,
            },
            "signed_defect": signed_defect,
        }
    raise AssertionError("unsupported typed fiber classification")


def omega(value: int) -> int:
    if value <= 0:
        raise AssertionError("Omega requires a positive integer")
    return sum(exponent for _prime, exponent in shared.factorization(value))


def lambda_rank(prime: int, K: int, support: int) -> tuple[int, int]:
    if support <= 0 or K % support:
        raise AssertionError("Lambda_p requires a charged support dividing K")
    B_p = (prime - 1) ** 2 // 4
    return B_p // support, omega(K // support)


def lex_strictly_decreases(
    source: tuple[int, int], target: tuple[int, int]
) -> bool:
    return target[0] < source[0] or (
        target[0] == source[0] and target[1] < source[1]
    )


def expected_edge_id(receipt: dict[str, object]) -> str | None:
    source = receipt.get("source_state")
    successor = receipt.get("successor_state")
    if not isinstance(source, dict) or not isinstance(successor, dict):
        return None
    return "edge:" + shared.canonical_hash({"source": source, "successor": successor})


def derive_cofactor(
    *, prime: int, support: int, bundle: dict[str, object]
) -> dict[str, int]:
    rechart = bundle.get("rechart")
    if not isinstance(rechart, dict):
        raise AssertionError("bundle is missing its overflow rechart")
    M = int(rechart["M"])
    R_M = int(rechart["R"])
    K_M = int(rechart["K"])
    C = int(rechart["C"])
    d = int(rechart["d"])
    n = int(rechart["n"])
    k, r = divmod(M, prime)
    if r == 0:
        raise AssertionError("direct cofactor macro has zero residue")
    s_numerator = 4 * r * d + 1
    if s_numerator % prime:
        raise AssertionError("cofactor s is not integral")
    s = s_numerator // prime
    R_T = 4 * r - s
    K_T = r * C
    g = gcd(support, C)
    a = support // g
    A_T = lcm(support, C)
    if r % a:
        raise AssertionError("cofactor support gate failed")
    C_T = r // a
    d_T = prime - C_T
    n_T = 4 * A_T - R_T
    return {
        "M": M,
        "R_M": R_M,
        "K_M": K_M,
        "C": C,
        "d": d,
        "n": n,
        "k": k,
        "r": r,
        "s": s,
        "R_T": R_T,
        "K_T": K_T,
        "g": g,
        "a": a,
        "A_T": A_T,
        "C_T": C_T,
        "d_T": d_T,
        "n_T": n_T,
    }


def verify_high_anchor_cofactor_macro(
    *,
    prime: int,
    parent_receipt: dict[str, object],
    anchor_state: dict[str, object],
    anchor_fiber: dict[str, object],
    bundle_receipt: dict[str, object],
    source_fiber: dict[str, object],
    target_fiber: dict[str, object],
    verify_parent: ParentVerifier,
    verify_fiber: FiberVerifier,
) -> dict[str, object]:
    """Reconstruct a macro certificate without relying on an S-to-T registry."""
    parent_source = parent_receipt.get("source_state")
    parent_successor = parent_receipt.get("successor_state")
    parent_fiber = parent_receipt.get("fiber_certificate")
    parent_marked_solution_set = parent_receipt.get("marked_solution_set")
    if not all(
        isinstance(value, dict)
        for value in (
            parent_source,
            parent_successor,
            parent_fiber,
            parent_marked_solution_set,
        )
    ):
        raise AssertionError("parent receipt shape changed")
    if parent_successor != anchor_state:
        raise AssertionError("charged parent must end at H, not at transient S")

    R = int(anchor_state["R"])
    K = int(anchor_state["K"])
    support = int(anchor_state["absorbed_support"])
    scope = anchor_state.get("source_tree_scope")
    if not isinstance(scope, str):
        raise AssertionError("macro anchor lacks a source-tree scope")

    expected_bundle = shared.high_R_path_anchored_bundle(
        prime=prime,
        R=R,
        support=support,
    )
    if bundle_receipt != expected_bundle:
        raise AssertionError("high-R bundle did not replay from the exact anchor")
    cofactor = derive_cofactor(
        prime=prime,
        support=support,
        bundle=bundle_receipt,
    )
    R_M = cofactor["R_M"]
    K_M = cofactor["K_M"]
    R_T = cofactor["R_T"]
    K_T = cofactor["K_T"]
    A_T = cofactor["A_T"]
    intermediate_state = shared.make_state(
        prime=prime,
        R=R_M,
        K=K_M,
        support=support,
        state_class="overflow",
        fiber_class=str(source_fiber.get("classification")),
        source_tree_scope=scope,
    )
    target_state = shared.make_state(
        prime=prime,
        R=R_T,
        K=K_T,
        support=A_T,
        state_class="overflow",
        fiber_class=str(target_fiber.get("classification")),
        source_tree_scope=scope,
    )

    parent_status = bool(
        parent_receipt.get("edge_id") == expected_edge_id(parent_receipt)
        and parent_receipt.get("selector_status") == "verified_edge"
        and parent_receipt.get("recursive_edge_eligible") is True
        and isinstance(parent_receipt.get("normal_form_replay_adapter"), str)
        and parent_receipt.get("e1_e5")
        == {f"E{index}": True for index in range(1, 6)}
        and parent_marked_solution_set == PARENT_IDENTITY_LIFT
        and all_checks_pass(parent_receipt.get("checks"))
        and shared.state_id_is_valid(parent_source)
        and shared.state_id_is_valid(anchor_state)
        and parent_receipt.get("fiber_certificate") == anchor_fiber
        and verify_parent(parent_receipt, anchor_state)
    )
    anchor_normal_form = bool(
        anchor_state.get("equation_target") == [4, prime]
        and anchor_state.get("state_class") == "overflow"
        and anchor_state.get("fiber_class") == anchor_fiber.get("classification")
        and support > 0
        and K % support == 0
        and prime < R < 4 * support
        and R % 4 == 3
        and R % prime != 0
        and prime * R + 1 == 4 * K
        and shared.canonical_chart(prime, support) == (R, K)
    )
    bundle_source = bundle_receipt.get("source")
    bundle_rechart = bundle_receipt.get("rechart")
    bundle_conditions = bundle_receipt.get("conditions")
    bundle_normal_form = bool(
        isinstance(bundle_source, dict)
        and isinstance(bundle_rechart, dict)
        and bundle_receipt.get("adapter") == "high_R_path_anchored_bundle_v1"
        and bundle_receipt.get("R_domain") == "high_R"
        and int(bundle_source.get("R", 0)) == R
        and int(bundle_source.get("K", 0)) == K
        and all_checks_pass(bundle_conditions)
        and int(bundle_rechart.get("M", 0)) == cofactor["M"]
        and int(bundle_rechart.get("R", 0)) == R_M
        and int(bundle_rechart.get("K", 0)) == K_M
        and bundle_rechart.get("result_class") == "overflow"
        and support and cofactor["M"] % support == 0
        and shared.canonical_chart(prime, cofactor["M"]) == (R_M, K_M)
        and K_M == cofactor["M"] * cofactor["C"]
        and prime * cofactor["n"] == 4 * cofactor["M"] * cofactor["d"] + 1
        and R_M == 4 * cofactor["M"] - cofactor["n"]
        and R_M > prime
    )
    cofactor_normal_form = bool(
        0 < cofactor["r"] < prime
        and prime * cofactor["s"] == 4 * cofactor["r"] * cofactor["d"] + 1
        and prime * R_T + 1 == 4 * K_T
        and K_T == cofactor["r"] * cofactor["C"]
        and cofactor["a"] > 0
        and cofactor["r"] % cofactor["a"] == 0
        and A_T == lcm(support, cofactor["C"])
        and K_T % A_T == 0
        and R_T > prime
        and shared.canonical_chart(prime, A_T) == (R_T, K_T)
        and cofactor["C_T"] > 0
        and cofactor["d_T"] > 0
        and cofactor["n_T"] > 0
        and K_T == A_T * cofactor["C_T"]
        and prime * cofactor["n_T"] == 4 * A_T * cofactor["d_T"] + 1
        and R_T == 4 * A_T - cofactor["n_T"]
    )
    link_checks = {
        "parent_successor_is_anchor": parent_successor == anchor_state,
        "bundle_source_is_anchor": isinstance(bundle_source, dict)
        and int(bundle_source.get("R", 0)) == R
        and int(bundle_source.get("K", 0)) == K,
        "bundle_output_is_intermediate": intermediate_state.get("R") == R_M
        and intermediate_state.get("K") == K_M
        and int(intermediate_state["absorbed_support"]) == support,
        "cofactor_source_is_intermediate": shared.state_id_is_valid(intermediate_state)
        and intermediate_state.get("source_tree_scope") == scope,
        "cofactor_target_is_target": shared.state_id_is_valid(target_state)
        and target_state.get("source_tree_scope") == scope,
        "scope_propagated": parent_source.get("source_tree_scope")
        == anchor_state.get("source_tree_scope")
        == intermediate_state.get("source_tree_scope")
        == target_state.get("source_tree_scope"),
    }
    anchor_typed_fiber = typed_fiber_payload(anchor_fiber)
    intermediate_typed_fiber = typed_fiber_payload(source_fiber)
    target_typed_fiber = typed_fiber_payload(target_fiber)
    typed_fibers = bool(
        anchor_state.get("fiber_class") == anchor_fiber.get("classification")
        and intermediate_state.get("fiber_class") == source_fiber.get("classification")
        and target_state.get("fiber_class") == target_fiber.get("classification")
        and verify_fiber(R, K, anchor_fiber)
        and verify_fiber(R_M, K_M, source_fiber)
        and verify_fiber(R_T, K_T, target_fiber)
    )
    identity_lift = bool(
        typed_fibers
        and parent_marked_solution_set == PARENT_IDENTITY_LIFT
        and MACRO_IDENTITY_LIFT
        == {
            "source": "Sol(p)",
            "successor": "Sol(p)",
            "lift": "identity",
            "direction": "T_to_H",
        }
        and anchor_state.get("equation_target") == [4, prime]
        and intermediate_state.get("equation_target") == [4, prime]
        and target_state.get("equation_target") == [4, prime]
    )
    phase_numerator = K_T - K
    phase_denominator = prime * support
    phase_integral = phase_denominator > 0 and phase_numerator % phase_denominator == 0
    h = phase_numerator // phase_denominator if phase_integral else None
    lambda_source = lambda_rank(prime, K, support)
    lambda_target = lambda_rank(prime, K_T, A_T)
    phase_checks = {
        "h_integral": phase_integral,
        "h_in_three_phase_window": h in {0, 1, 2},
        "chart_difference": h is not None and R_T == R + 4 * support * h,
        "not_full_state_stutter": (R, K, support) != (R_T, K_T, A_T),
    }
    verifier_contract = {
        "macro_replay_adapter": MACRO_REPLAY_ADAPTER,
        "parent_replay_adapter": parent_receipt[
            "normal_form_replay_adapter"
        ],
        "parent_verifier": verifier_identity(verify_parent),
        "fiber_verifier": verifier_identity(verify_fiber),
        "bundle_adapter": bundle_receipt["adapter"],
        "cofactor_derivation": "derive_cofactor_v1",
    }
    macro_payload = {
        "parent_receipt_digest": shared.canonical_hash(parent_receipt),
        "parent_edge_id": parent_receipt["edge_id"],
        "verifier_contract": verifier_contract,
        "anchor_state": anchor_state,
        "bundle_receipt": bundle_receipt,
        "intermediate_state": intermediate_state,
        "cofactor": cofactor,
        "target_state": target_state,
        "source_tree_scope": scope,
        "typed_fibers": {
            "anchor": anchor_typed_fiber,
            "intermediate": intermediate_typed_fiber,
            "target": target_typed_fiber,
        },
        "marked_solution_lift": MACRO_IDENTITY_LIFT,
    }
    e1_e5 = {
        "E1": parent_status and anchor_normal_form and bundle_normal_form,
        "E2": cofactor_normal_form,
        "E3": all_checks_pass(link_checks),
        "E4": identity_lift,
        "E5": bool(
            all_checks_pass(phase_checks)
            and lex_strictly_decreases(lambda_source, lambda_target)
        ),
    }
    if e1_e5 != {f"E{index}": True for index in range(1, 6)}:
        raise AssertionError(f"high-anchor cofactor macro failed: {e1_e5}")
    return {
        "certificate_type": MACRO_REPLAY_ADAPTER,
        "certificate_status": "verified_macro_replay",
        "selector_status": "analysis_evidence",
        "recursive_edge_eligible": False,
        "proof_boundary": (
            "This standalone verifier closes a concrete macro E1--E5 receipt. "
            "It does not register the macro in the global selector or override "
            "terminal-first dispatch."
        ),
        "macro_edge_id": "macro:" + shared.canonical_hash(macro_payload),
        "parent_edge_id": parent_receipt["edge_id"],
        "parent_receipt_digest": shared.canonical_hash(parent_receipt),
        "verifier_contract": verifier_contract,
        "anchor_state": anchor_state,
        "intermediate_state": intermediate_state,
        "target_state": target_state,
        "bundle_digest": shared.canonical_hash(bundle_receipt),
        "cofactor": cofactor,
        "links": link_checks,
        "typed_fibers": {
            "anchor": anchor_typed_fiber,
            "intermediate": intermediate_typed_fiber,
            "target": target_typed_fiber,
            "marked_solution_lift": MACRO_IDENTITY_LIFT,
        },
        "phase": {"h": h, **phase_checks},
        "lambda_p": {
            "source": list(lambda_source),
            "target": list(lambda_target),
            "strict_lexicographic_decrease": lex_strictly_decreases(
                lambda_source, lambda_target
            ),
        },
        "e1_e5": e1_e5,
    }


def type_i_terminal(prime: int, gap: int, a: int, b: int) -> dict[str, object]:
    certificate = type_i_normal_form_certificate(prime, gap, a, b)
    if certificate is None or not verify_certificate(certificate):
        raise AssertionError("expected Type I terminal changed")
    return {
        "certificate_type": "type_i_normal_form_terminal",
        "selector_status": "terminal_leaf",
        "gap": gap,
        "parameters": {"A": a, "B": b},
        "denominators": {"x": certificate.x, "y": certificate.y, "z": certificate.z},
    }


def p1201_fixture() -> dict[str, object]:
    prime = 1_201
    B_p = (prime - 1) ** 2 // 4
    root_bundle = shared.high_R_path_anchored_bundle(prime=prime, R=987, support=1)
    root_rechart = root_bundle["rechart"]
    if not isinstance(root_rechart, dict):
        raise AssertionError("p=1201 root bundle shape changed")
    A = int(root_rechart["M"])
    R = int(root_rechart["R"])
    K = int(root_rechart["K"])
    if (A, R, K) != (986, 1_839, 552_160):
        raise AssertionError("p=1201 high anchor changed")
    anchor_fiber = shared.residue_witness(
        R, shared.factorization(K), (0, 0, -2, 2, -3)
    )
    parent = shared.same_chart_parent_replay(
        prime=prime, B_p=B_p, root_bundle=root_bundle, fiber=anchor_fiber
    )
    anchor_state = parent["successor_state"]
    if not isinstance(anchor_state, dict):
        raise AssertionError("p=1201 parent successor shape changed")
    bundle = shared.high_R_path_anchored_bundle(prime=prime, R=R, support=A)
    cofactor = derive_cofactor(prime=prime, support=A, bundle=bundle)
    if (
        cofactor["M"],
        cofactor["R_M"],
        cofactor["K_M"],
        cofactor["R_T"],
        cofactor["K_T"],
        cofactor["A_T"],
    ) != (906_134, 2_873_071, 862_639_568, 1_839, 552_160, 27_608):
        raise AssertionError("p=1201 macro arithmetic changed")
    source_fiber = shared.residue_witness(
        cofactor["R_M"],
        shared.factorization(cofactor["K_M"]),
        (-2, 1, 19, 1, -13),
    )
    target_fiber = shared.residue_witness(
        cofactor["R_T"],
        shared.factorization(cofactor["K_T"]),
        (0, 0, -2, 2, -3),
    )
    macro = verify_high_anchor_cofactor_macro(
        prime=prime,
        parent_receipt=parent,
        anchor_state=anchor_state,
        anchor_fiber=anchor_fiber,
        bundle_receipt=bundle,
        source_fiber=source_fiber,
        target_fiber=target_fiber,
        verify_parent=shared.verify_charged_parent_replay,
        verify_fiber=shared.fiber_certificate_is_valid,
    )
    return {
        "prime": prime,
        "fixture": "p1201_h0_F_F_F",
        "macro": macro,
        "terminal_first": type_i_terminal(prime, 1_043, 1, 33),
        "terminal_note": "same-bundle exhaustion reaches the formal low-chart Type I leaf",
    }


def p60913_fixture() -> dict[str, object]:
    prime = 60_913
    B_p = (prime - 1) ** 2 // 4
    root_bundle = shared.high_R_path_anchored_bundle(prime=prime, R=37_295, support=1)
    root_rechart = root_bundle["rechart"]
    if not isinstance(root_rechart, dict):
        raise AssertionError("p=60913 root bundle shape changed")
    A = int(root_rechart["M"])
    R = int(root_rechart["R"])
    K = int(root_rechart["K"])
    if (A, R, K) != (18_647, 72_259, 1_100_378_117):
        raise AssertionError("p=60913 high anchor changed")
    anchor_fiber = h2_g_fixture.crt_discrete_log_parity_g_fiber(
        R, K, h2_g_fixture.ANCHOR_COMPONENTS
    )
    parent = h2_g_fixture.same_chart_parent_replay(
        prime=prime, B_p=B_p, root_bundle=root_bundle, fiber=anchor_fiber
    )
    anchor_state = parent["successor_state"]
    if not isinstance(anchor_state, dict):
        raise AssertionError("p=60913 parent successor shape changed")
    bundle = shared.high_R_path_anchored_bundle(prime=prime, R=R, support=A)
    cofactor = derive_cofactor(prime=prime, support=A, bundle=bundle)
    if (
        cofactor["M"],
        cofactor["R_M"],
        cofactor["K_M"],
        cofactor["R_T"],
        cofactor["K_T"],
        cofactor["A_T"],
        cofactor["s"],
    ) != (
        1_347_394_926,
        4_949_657_351,
        75_374_619_555_366,
        221_435,
        3_372_067_539,
        55_941,
        19_681,
    ):
        raise AssertionError("p=60913 macro arithmetic changed")
    source_fiber = h2_g_fixture.crt_discrete_log_parity_g_fiber(
        cofactor["R_M"], cofactor["K_M"], h2_g_fixture.SOURCE_COMPONENTS
    )
    target_fiber = shared.residue_witness(
        cofactor["R_T"],
        shared.factorization(cofactor["K_T"]),
        (-5, -2, 5, 0, -5),
    )
    macro = verify_high_anchor_cofactor_macro(
        prime=prime,
        parent_receipt=parent,
        anchor_state=anchor_state,
        anchor_fiber=anchor_fiber,
        bundle_receipt=bundle,
        source_fiber=source_fiber,
        target_fiber=target_fiber,
        verify_parent=h2_g_fixture.verify_charged_parent_replay,
        verify_fiber=h2_g_fixture.fiber_certificate_is_valid,
    )
    return {
        "prime": prime,
        "fixture": "p60913_h2_G_G_F",
        "macro": macro,
        "terminal_first": type_i_terminal(prime, 7, 1, 1),
        "terminal_note": "gap-7 direct Type I terminal preempts recursive enqueueing",
    }


def build_result() -> dict[str, object]:
    fixtures = [p1201_fixture(), p60913_fixture()]
    for fixture in fixtures:
        macro = fixture["macro"]
        terminal = fixture["terminal_first"]
        if not isinstance(macro, dict) or not isinstance(terminal, dict):
            raise AssertionError("macro fixture shape changed")
        if macro.get("e1_e5") != {f"E{index}": True for index in range(1, 6)}:
            raise AssertionError("macro fixture did not close E1--E5")
        if terminal.get("selector_status") != "terminal_leaf":
            raise AssertionError("terminal-first fixture changed")
    return {
        "schema_version": 1,
        "certificate_type": "high_anchor_cofactor_macro_replay_suite_v1",
        "scope": (
            "Independent macro replay only: parent -> H, deterministic bundle H -> S, "
            "and cofactor S -> T.  The global selector remains unchanged."
        ),
        "fixtures": fixtures,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified high-anchor cofactor macro suite: p=1201, p=60913")
        return
    args.output.write_text(json.dumps(result, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
