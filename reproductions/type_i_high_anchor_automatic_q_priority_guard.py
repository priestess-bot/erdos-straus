#!/usr/bin/env python3
"""Verify the gap-3/gap-7 priority guard on automatic-q source controls.

The controls are genuine beta_0=2 fresh-root high anchors with charged
same-chart parents and a second full-excess automatic C=2A cofactor gate.
They are deliberately terminal-preempted: this fixture proves that a
gap-7-only prefix is too weak, not that either macro is recursive.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict
import json
from math import gcd, lcm
from pathlib import Path

from short_certificate import certificate_at_gap, smallest_prime_factors, verify_certificate
import type_i_high_r_chart_two_anchor as shared


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-high-anchor-automatic-q-priority-guard-results.json"

FULL_PREFIX = (
    {"id": "direct_bradford_gap_3", "version": "short_certificate/v1", "gap": 3},
    {"id": "direct_bradford_gap_7", "version": "short_certificate/v1", "gap": 7},
)
GAP_SEVEN_ONLY_PREFIX = (FULL_PREFIX[1],)

CONTROLS = (
    {
        "label": "p34897_q2_gap3_preempted",
        "p": 34_897,
        "A": 13_635,
        "q": 2,
        "R": 39_827,
        "K": 347_460_705,
        "parent_fiber": "F",
        "parent_witness": (-3, -1, 4, -1, 4),
        "expected_terminal": {"type": "I", "gap": 3, "divisor": 5},
        "expected_gap_seven_only": None,
    },
    {
        "label": "p68713_q2_gap3_preempted",
        "p": 68_713,
        "A": 31_143,
        "q": 2,
        "R": 103_067,
        "K": 1_770_510_693,
        "parent_fiber": "G",
        "expected_terminal": {"type": "I", "gap": 3, "divisor": 41},
        "expected_gap_seven_only": {"type": "I", "gap": 7, "divisor": 5},
    },
)


def transient_descriptor(
    *, prime: int, R: int, K: int, support: int, scope: str
) -> dict[str, object]:
    """Serialize a bundle output before any fiber classification is needed."""
    descriptor = {
        "equation_target": [4, prime],
        "R": R,
        "K": K,
        "absorbed_support": support,
        "lifecycle": "transient_bundle_output",
        "source_tree_scope": scope,
    }
    return {"state_id": "state:" + shared.canonical_hash(descriptor), **descriptor}


def priority_guard(
    *, prime: int, state_id: str, prefix: tuple[dict[str, object], ...]
) -> dict[str, object]:
    """Run one versioned direct-terminal prefix for a concrete state input."""
    if not state_id.startswith("state:"):
        raise AssertionError("priority guard requires a content-addressed state")
    if not prefix:
        raise AssertionError("priority guard prefix must be nonempty")
    spf = smallest_prime_factors((prime + max(int(item["gap"]) for item in prefix)) // 4 + 1)
    steps: list[dict[str, object]] = []
    for item in prefix:
        gap = int(item["gap"])
        certificate = certificate_at_gap(prime, gap, spf)
        step: dict[str, object] = {
            "id": str(item["id"]),
            "version": str(item["version"]),
            "gap": gap,
        }
        if certificate is None:
            step["result"] = "no_output"
            steps.append(step)
            continue
        if not verify_certificate(certificate):
            raise AssertionError("priority guard reconstructed an invalid terminal")
        step["result"] = "terminal_leaf"
        step["certificate"] = asdict(certificate)
        steps.append(step)
        return {
            "state_id": state_id,
            "priority_prefix": list(prefix),
            "priority_prefix_digest": shared.canonical_hash(prefix),
            "steps": steps,
            "selected_output": step,
        }
    return {
        "state_id": state_id,
        "priority_prefix": list(prefix),
        "priority_prefix_digest": shared.canonical_hash(prefix),
        "steps": steps,
        "selected_output": None,
    }


def parent_fiber(control: dict[str, object], R: int, K: int) -> dict[str, object]:
    kind = str(control["parent_fiber"])
    if kind == "F":
        witness = tuple(int(value) for value in control["parent_witness"])
        return shared.provided_unbounded_residue_witness(
            R, shared.factorization(K), witness
        )
    if kind == "G":
        return shared.legendre_g_fiber(R, K, R)
    raise AssertionError("unknown parent fiber kind")


def cofactor_profile(
    *, prime: int, support: int, bundle: dict[str, object]
) -> dict[str, int]:
    rechart = bundle.get("rechart")
    if not isinstance(rechart, dict):
        raise AssertionError("automatic-q bundle is missing its overflow rechart")
    M = int(rechart["M"])
    C = int(rechart["C"])
    d = int(rechart["d"])
    k, r = divmod(M, prime)
    if r == 0 or (4 * r * d + 1) % prime:
        raise AssertionError("automatic-q cofactor residue failed")
    s = (4 * r * d + 1) // prime
    R_T = 4 * r - s
    K_T = r * C
    target_support = lcm(support, C)
    quotient = support // gcd(support, C)
    if r % quotient:
        raise AssertionError("automatic-q cofactor gate failed")
    target_C = r // quotient
    target_d = prime - target_C
    target_n = 4 * target_support - R_T
    if not (
        R_T > prime
        and shared.canonical_chart(prime, target_support) == (R_T, K_T)
        and K_T == target_support * target_C
        and target_C > 0
        and target_d > 0
        and target_n > 0
        and prime * target_n == 4 * target_support * target_d + 1
    ):
        raise AssertionError("automatic-q cofactor target normal form failed")
    return {
        "M": M,
        "C": C,
        "d": d,
        "k": k,
        "r": r,
        "s": s,
        "R_T": R_T,
        "K_T": K_T,
        "target_support": target_support,
        "target_C": target_C,
        "target_d": target_d,
        "target_n": target_n,
    }


def replay_control(control: dict[str, object]) -> dict[str, object]:
    prime = int(control["p"])
    A = int(control["A"])
    q = int(control["q"])
    expected_R = int(control["R"])
    expected_K = int(control["K"])
    R0 = 2 * A + 1
    B_p = (prime - 1) ** 2 // 4

    root_bundle = shared.high_R_path_anchored_bundle(
        prime=prime, R=R0, support=1
    )
    root_rechart = root_bundle["rechart"]
    if not isinstance(root_rechart, dict):
        raise AssertionError("root bundle shape changed")
    R = int(root_rechart["R"])
    K = int(root_rechart["K"])
    Q0 = int(root_bundle["complete_excess_bundle"]["Q"])
    beta0 = int(root_bundle["complete_excess_bundle"]["beta"])
    if not (
        prime % 24 == 1
        and A % 4 == 3
        and R0 < prime
        and (Q0, beta0, R, K) == (A, 2, expected_R, expected_K)
        and root_rechart.get("result_class") == "overflow"
    ):
        raise AssertionError("beta_0=2 root receipt changed")

    fiber = parent_fiber(control, R, K)
    parent = shared.same_chart_parent_replay(
        prime=prime,
        B_p=B_p,
        root_bundle=root_bundle,
        fiber=fiber,
    )
    anchor_state = parent.get("successor_state")
    if not isinstance(anchor_state, dict) or not shared.verify_charged_parent_replay(
        parent, anchor_state
    ):
        raise AssertionError("charged same-chart parent did not replay")

    high_bundle = shared.high_R_path_anchored_bundle(
        prime=prime, R=R, support=A
    )
    high_rechart = high_bundle["rechart"]
    if not isinstance(high_rechart, dict):
        raise AssertionError("high bundle shape changed")
    Q1 = int(high_bundle["complete_excess_bundle"]["Q"])
    beta1 = int(high_bundle["complete_excess_bundle"]["beta"])
    cofactor = cofactor_profile(prime=prime, support=A, bundle=high_bundle)
    M = cofactor["M"]
    C = cofactor["C"]
    B = K // A
    phase_numerator = q * cofactor["r"] - B
    if not (
        K % A == 0
        and Q1 == R - 1
        and beta1 == 1
        and M == A * (R - 1)
        and q * A < prime
        and C == q * A
        and (4 * q * A * A * (R - 1)) % prime == 1
        and phase_numerator % prime == 0
        and phase_numerator // prime == q - 1
    ):
        raise AssertionError("automatic-q high source conditions changed")

    scope = str(anchor_state["source_tree_scope"])
    transient = transient_descriptor(
        prime=prime,
        R=int(high_rechart["R"]),
        K=int(high_rechart["K"]),
        support=A,
        scope=scope,
    )
    weak_anchor = priority_guard(
        prime=prime,
        state_id=str(anchor_state["state_id"]),
        prefix=GAP_SEVEN_ONLY_PREFIX,
    )
    weak_transient = priority_guard(
        prime=prime,
        state_id=str(transient["state_id"]),
        prefix=GAP_SEVEN_ONLY_PREFIX,
    )
    full_anchor = priority_guard(
        prime=prime,
        state_id=str(anchor_state["state_id"]),
        prefix=FULL_PREFIX,
    )
    full_transient = priority_guard(
        prime=prime,
        state_id=str(transient["state_id"]),
        prefix=FULL_PREFIX,
    )
    expected_terminal = control["expected_terminal"]
    for receipt in (full_anchor, full_transient):
        selected = receipt["selected_output"]
        if not isinstance(selected, dict) or selected.get("result") != "terminal_leaf":
            raise AssertionError("complete direct prefix failed to preempt the macro")
        certificate = selected.get("certificate")
        if not isinstance(certificate, dict) or not (
            certificate["certificate_type"] == expected_terminal["type"]
            and certificate["gap"] == expected_terminal["gap"]
            and certificate["divisor"] == expected_terminal["divisor"]
        ):
            raise AssertionError("priority prefix terminal changed")
    expected_gap_seven_only = control["expected_gap_seven_only"]
    for receipt in (weak_anchor, weak_transient):
        selected = receipt["selected_output"]
        if expected_gap_seven_only is None:
            if selected is not None:
                raise AssertionError("gap-seven-only guard unexpectedly preempted the gap-3 control")
            continue
        if not isinstance(selected, dict) or selected.get("result") != "terminal_leaf":
            raise AssertionError("gap-seven-only order control lost its terminal")
        certificate = selected.get("certificate")
        if not isinstance(certificate, dict) or not (
            certificate["certificate_type"] == expected_gap_seven_only["type"]
            and certificate["gap"] == expected_gap_seven_only["gap"]
            and certificate["divisor"] == expected_gap_seven_only["divisor"]
        ):
            raise AssertionError("gap-seven-only terminal changed")

    return {
        "label": str(control["label"]),
        "prime": prime,
        "root": {"R0": R0, "Q0": Q0, "beta0": beta0},
        "high_anchor": {
            "R": R,
            "K": K,
            "A": A,
            "B": B,
            "fiber_class": fiber["classification"],
            "parent_edge_id": parent["edge_id"],
            "parent_checks": parent["checks"],
        },
        "automatic_q": {
            "q": q,
            "Q1": Q1,
            "beta1": beta1,
            **cofactor,
            "phase_h": phase_numerator // prime,
        },
        "priority_guard": {
            "weak_gap_seven_only": {
                "anchor": weak_anchor,
                "transient": weak_transient,
            },
            "full_gap_three_then_seven": {
                "anchor": full_anchor,
                "transient": full_transient,
            },
        },
        "selector_status": "terminal_leaf",
        "recursive_edge_eligible": False,
    }


def build_result() -> dict[str, object]:
    controls = [replay_control(control) for control in CONTROLS]
    if any(item["selector_status"] != "terminal_leaf" for item in controls):
        raise AssertionError("priority controls lost their terminal status")
    return {
        "schema_version": 1,
        "certificate_type": "automatic_q_high_anchor_gap3_gap7_priority_boundary_v1",
        "scope": (
            "Two actual fresh-root automatic-q high sources. The result proves only that "
            "a gap-seven-only terminal prefix is incomplete at p=34897, while p=68713 "
            "checks the ordering when both gaps have terminals. The ordered gap-three/gap-seven "
            "prefix preempts both the persistent anchor and its transient bundle output. "
            "No macro edge is registered."
        ),
        "priority_prefix": list(FULL_PREFIX),
        "priority_prefix_digest": shared.canonical_hash(FULL_PREFIX),
        "controls": controls,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified automatic-q gap-3/gap-7 priority boundary: p=34897, p=68713")
        return
    args.output.write_text(json.dumps(result, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
