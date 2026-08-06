#!/usr/bin/env python3
"""Map non-monotone same-chart support resets before the high-R cofactor gate.

This is deliberately narrower than a selector search.  It reads the frozen
verified-parent high anchors, and only enumerates divisors

    L | K,  A < L <= B_p,  A does not divide L.

For a high canonical anchor H=(p,R,K;A), every such L is again the same
canonical chart because R<4A<4L and L|K.  The strict subset Pi_p(L)<Pi_p(A)
is the only subset that has an available outer-rank payment for discarding the
old charged-support chain.  We then replay the deterministic high-R bundle
and its exact cofactor gate.  Neither an arithmetic hit nor a paid reset is
registered as a selector edge: the parent/reset E1--E4 contract is emitted as
an explicit missing requirement.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import gcd, lcm
from pathlib import Path

import type_i_high_r_chart_two_anchor as shared


ROOT = Path(__file__).resolve().parents[1]
ATLAS_INPUT = ROOT / "reproductions" / "type-i-high-anchor-parent-atlas-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-high-anchor-nonmonotone-reset-gate-results.json"
NONSELFLOOP_CONTROL = {
    "p": 1201,
    "R": 1839,
    "K": 552_160,
    "source_support": 560,
    "reset_support": 986,
}


def canonical_hash(payload: object) -> str:
    return hashlib.sha256(
        json.dumps(payload, ensure_ascii=True, sort_keys=True, separators=(",", ":")).encode("ascii")
    ).hexdigest()


def divisors(value: int) -> list[int]:
    if value <= 0:
        raise AssertionError("divisors require a positive integer")
    result = [1]
    for prime, exponent in shared.factorization(value):
        result = [candidate * prime**power for candidate in result for power in range(exponent + 1)]
    return sorted(result)


def pi_p(prime: int, support: int) -> int:
    return ((prime - 1) ** 2 // 4) // support


def omega(value: int) -> int:
    return sum(exponent for _prime, exponent in shared.factorization(value))


def frozen_anchors() -> list[dict[str, int]]:
    payload = json.loads(ATLAS_INPUT.read_text(encoding="utf-8"))
    grouped: set[tuple[int, int, int, int]] = set()
    for row in payload["rows"]:
        if row.get("high_anchor_candidate") is not True:
            continue
        anchor = row["anchor"]
        grouped.add(tuple(int(anchor[key]) for key in ("p", "R", "K", "absorbed_support")))
    return [
        {"p": prime, "R": R, "K": K, "A": A}
        for prime, R, K, A in sorted(grouped)
    ]


def reset_lattice(prime: int, R: int, K: int, A: int) -> list[int]:
    """The exact finite non-divisibility same-chart reset domain."""
    B_prime = (prime - 1) ** 2 // 4
    if not (
        shared.is_prime(prime)
        and prime % 24 == 1
        and A > 0
        and K % A == 0
        and shared.canonical_chart(prime, A) == (R, K)
        and prime < R < 4 * A
        and K // A < prime
    ):
        raise AssertionError("input is not a bounded high canonical anchor")
    # The high-anchor atlas is broader than the outer Pi_p domain.  In the
    # latter's complement, A<L<=B_p is simply empty rather than ill-formed.
    if A > B_prime:
        return []
    result = [L for L in divisors(K) if A < L <= B_prime and L % A != 0]
    for L in result:
        # This is the reason the reset still has the *same* chart.
        if shared.canonical_chart(prime, L) != (R, K):
            raise AssertionError("same-chart reset lattice changed")
        if not (K % L == 0 and 0 < K // L < prime and R < 4 * L):
            raise AssertionError("reset re-factorization left the overflow chart domain")
    return result


def cofactor_attempt(prime: int, R: int, K: int, L: int) -> dict[str, object]:
    """Replay one high-R bundle and record only its arithmetic gate outcome."""
    bundle = shared.high_R_path_anchored_bundle(prime=prime, R=R, support=L)
    rechart = bundle["rechart"]
    if not isinstance(rechart, dict) or rechart.get("result_class") != "overflow":
        raise AssertionError("frozen high anchor no longer has an overflow high-R bundle")
    M, C, d, n = (int(rechart[key]) for key in ("M", "C", "d", "n"))
    R_M, K_M = (int(rechart[key]) for key in ("R", "K"))
    _k, r = divmod(M, prime)
    numerator = 4 * r * d + 1
    if numerator % prime:
        raise AssertionError("cofactor s integrality changed")
    s = numerator // prime
    R_T, K_T = 4 * r - s, r * C
    g = gcd(L, C)
    quotient = L // g
    c = C // g
    target_support = lcm(L, C)
    gate = r % quotient == 0
    checks = {
        "intermediate_chart": shared.canonical_chart(prime, M) == (R_M, K_M),
        "intermediate_determinant": prime * n == 4 * M * d + 1,
        "cofactor_identity": prime * s == 4 * r * d + 1,
        "target_chart_equation": prime * R_T + 1 == 4 * K_T,
        "support_gate": gate,
        "target_support_divides_K": gate and K_T % target_support == 0,
        "canonical_target": gate and shared.canonical_chart(prime, target_support) == (R_T, K_T),
    }
    if not all(checks[key] for key in ("intermediate_chart", "intermediate_determinant", "cofactor_identity", "target_chart_equation")):
        raise AssertionError("cofactor arithmetic identity changed")
    if gate and not all(checks.values()):
        raise AssertionError("passing cofactor gate no longer has a canonical target")
    exact_reset_self_loop = gate and (R_T, K_T, target_support) == (R, K, L)
    h_numerator = K_T - K
    h_denominator = prime * L
    h = h_numerator // h_denominator if h_numerator % h_denominator == 0 else None
    phase_factorization: dict[str, object] | None = None
    if gate:
        if h is None:
            raise AssertionError("passing gate no longer has an integral same-chart phase")
        u = r // quotient
        B = K // L
        phase_factorization = {
            "gcd_L_C": g,
            "a_L_over_gcd": quotient,
            "c_C_over_gcd": c,
            "u_r_over_a": u,
            "B_K_over_L": B,
            "target_support_equals_Lc": target_support == L * c,
            "target_K_equals_Luc": K_T == L * u * c,
            "phase_formula_h_equals_uc_minus_B_over_p": h == (u * c - B) // prime,
            "phase_nonnegative": h >= 0,
            "chart_return": h == 0,
            "exact_reset_state_self_loop": exact_reset_self_loop,
            "C_divides_reset_support": L % C == 0,
            "self_loop_iff_C_divides_L": exact_reset_self_loop == (L % C == 0),
        }
        if not all(
            bool(phase_factorization[key])
            for key in (
                "target_support_equals_Lc",
                "target_K_equals_Luc",
                "phase_formula_h_equals_uc_minus_B_over_p",
                "phase_nonnegative",
                "self_loop_iff_C_divides_L",
            )
        ):
            raise AssertionError("reset phase factorization changed")
    return {
        "reset_support": L,
        "bundle": {
            "adapter": bundle["adapter"],
            "Q": int(bundle["complete_excess_bundle"]["Q"]),
            "M": M,
            "R": R_M,
            "K": K_M,
            "C": C,
            "d": d,
            "n": n,
        },
        "cofactor": {
            "r": r,
            "s": s,
            "gcd_L_C": g,
            "L_over_gcd": quotient,
            "target_R": R_T,
            "target_K": K_T,
            "target_support": target_support,
        },
        "gate_passes": gate,
        "target_relation": {
            "exact_reset_state_return": exact_reset_self_loop,
            "phase_h": h,
            "phase_factorization": phase_factorization,
            "direct_recursive_action": "suppress_exact_self_loop"
            if exact_reset_self_loop
            else "requires_separate_terminal_first_and_E1_E5_check",
        },
        "gate_diagnostic": {
            "size_obstruction_L_over_gcd_gt_r": quotient > r,
            "remainder_mod_L_over_gcd": r % quotient,
        },
        "arithmetic_checks": checks,
        "pi_p": {
            "reset_source": pi_p(prime, L),
            "cofactor_target": pi_p(prime, target_support) if gate else None,
            "cofactor_nonincrease_if_gate": gate and pi_p(prime, target_support) <= pi_p(prime, L),
            "cofactor_lambda": [pi_p(prime, target_support), omega(K_T // target_support)]
            if gate
            else None,
        },
    }


def named_nonselfloop_control() -> dict[str, object]:
    """A fixed h=0 chart-return that refutes automatic reset-state self-looping."""
    prime = int(NONSELFLOOP_CONTROL["p"])
    R = int(NONSELFLOOP_CONTROL["R"])
    K = int(NONSELFLOOP_CONTROL["K"])
    A = int(NONSELFLOOP_CONTROL["source_support"])
    L = int(NONSELFLOOP_CONTROL["reset_support"])
    B_prime = (prime - 1) ** 2 // 4
    if not (
        shared.canonical_chart(prime, A) == (R, K)
        and shared.canonical_chart(prime, L) == (R, K)
        and prime < R < 4 * A < 4 * L
        and A < L <= B_prime
        and K % A == 0
        and K % L == 0
        and L % A != 0
        and pi_p(prime, L) < pi_p(prime, A)
    ):
        raise AssertionError("named non-self-loop control stopped being a paid same-chart reset")
    attempt = cofactor_attempt(prime, R, K, L)
    phase = attempt["target_relation"]["phase_factorization"]
    if not isinstance(phase, dict) or not (
        attempt["gate_passes"]
        and phase["chart_return"]
        and not phase["exact_reset_state_self_loop"]
        and phase["c_C_over_gcd"] == 28
        and attempt["cofactor"]["target_support"] == 27_608
    ):
        raise AssertionError("named non-self-loop control no longer separates chart return from state loop")
    return {
        "input": {"p": prime, "R": R, "K": K, "source_support": A, "reset_support": L},
        "reset_checks": {
            "same_chart": True,
            "nonmonotone": True,
            "strict_pi_payment": True,
        },
        "cofactor_attempt": attempt,
        "boundary": (
            "This is an arithmetic control from an existing terminal-preempted p=1201 path. "
            "It is not a reset selector edge and does not provide parent or terminal-first proof."
        ),
    }


def analyse_anchor(anchor: dict[str, int]) -> dict[str, object]:
    prime, R, K, A = (anchor[key] for key in ("p", "R", "K", "A"))
    all_resets = reset_lattice(prime, R, K, A)
    source_pi = pi_p(prime, A)
    attempts = []
    for L in all_resets:
        attempt = cofactor_attempt(prime, R, K, L)
        attempt["pi_p"]["anchor_source"] = source_pi
        attempt["pi_p"]["reset_strict_payment"] = attempt["pi_p"]["reset_source"] < source_pi
        attempts.append(attempt)
    paid = [attempt for attempt in attempts if attempt["pi_p"]["reset_strict_payment"]]
    paid_hits = [attempt for attempt in paid if attempt["gate_passes"]]
    return {
        "row_id": "nonmonotone-reset:" + canonical_hash([prime, R, K, A])[:16],
        "anchor": {"p": prime, "R": R, "K": K, "absorbed_support": A},
        "B_p": (prime - 1) ** 2 // 4,
        "reset_domain": {
            "formula": "{L : L|K, A<L<=B_p, A does not divide L}",
            "all_nonmonotone_same_chart_resets": all_resets,
            "strictly_paid_resets": [attempt["reset_support"] for attempt in paid],
        },
        "attempts": attempts,
        "paid_gate_hits": paid_hits,
    }


def reset_contract() -> dict[str, object]:
    """Requirements missing from a bare numerical same-chart reset."""
    return {
        "status": "required_for_legal_recursive_reset_not_proved_by_this_atlas",
        "E1": (
            "A content-addressed parent receipt ending at H and an explicit reset receipt "
            "H -> H_L with pR+1=4K, L|K, canonical_chart(p,L)=(R,K); if several legacy "
            "receipts share an endpoint edge id, the reset must bind one canonical parent digest."
        ),
        "E2": (
            "The deterministic high_R_path_anchored_bundle_v1 replay from H_L and, if used, "
            "the cofactor target normal form with its exact support gate."
        ),
        "E3": (
            "H, H_L, transient S_L, and target T_L must be separately content-addressed in "
            "one source_tree_scope; the reset hash must bind the parent digest and the discarded "
            "support A.  A legacy edge that merely has the same numeric chart is insufficient."
        ),
        "E4": (
            "Typed F/G/hit or terminal certificates for H, H_L, S_L, and T_L, together with "
            "the marked lift Sol(p)->Sol(p) in the declared recursive direction."
        ),
        "E5": (
            "Pi_p(L)<Pi_p(A), recorded as support_reset_paid=true and outer_rank_reset=true. "
            "No old support-preservation assertion, phase token, exhaustion mark, or capability "
            "may be inherited across A not dividing L."
        ),
        "terminal_first": (
            "Before enqueuing a nonterminal reset/macro, the relevant terminal and alternate menu "
            "must be exhausted by its own bounded certificate."
        ),
    }


def build_result() -> dict[str, object]:
    rows = [analyse_anchor(anchor) for anchor in frozen_anchors()]
    attempts = [attempt for row in rows for attempt in row["attempts"]]
    nonselfloop = named_nonselfloop_control()
    paid = [attempt for attempt in attempts if attempt["pi_p"]["reset_strict_payment"]]
    paid_hits = [attempt for attempt in paid if attempt["gate_passes"]]
    paid_self_loops = [
        attempt
        for attempt in paid_hits
        if attempt["target_relation"]["exact_reset_state_return"]
    ]
    raw_hits = [attempt for attempt in attempts if attempt["gate_passes"]]
    return {
        "schema_version": 2,
        "certificate_type": "type_i_high_anchor_nonmonotone_same_chart_reset_gate_v1",
        "input": {
            "path": str(ATLAS_INPUT.relative_to(ROOT)),
            "sha256": hashlib.sha256(ATLAS_INPUT.read_bytes()).hexdigest(),
        },
        "scope": (
            "Finite read-only arithmetic atlas of distinct frozen verified-parent high anchors. "
            "It does not run selector/history or promote a reset or cofactor hit to an edge."
        ),
        "exact_domain": {
            "reset_lattice": "{L : L|K, A<L<=B_p, A does not divide L}",
            "same_chart_reason": "R<4A<4L and L|K imply canonical_chart(p,L)=(R,K)",
            "paid_subset": "Pi_p(L)<Pi_p(A)",
            "cofactor_gate": "L/gcd(L,C_L) divides r_L",
        },
        "summary": {
            "frozen_distinct_high_anchors": len(rows),
            "anchors_with_nonmonotone_reset": sum(bool(row["attempts"]) for row in rows),
            "nonmonotone_reset_attempts": len(attempts),
            "strictly_paid_reset_attempts": len(paid),
            "raw_gate_hits": len(raw_hits),
            "strictly_paid_gate_hits": len(paid_hits),
            "strictly_paid_gate_hit_exact_reset_self_loops": len(paid_self_loops),
            "paid_gate_hit_anchors": sorted(
                {
                    row["row_id"]
                    for row in rows
                    if row["paid_gate_hits"]
                }
            ),
        },
        "phase_boundary_control": nonselfloop,
        "conclusion": {
            "arithmetic": (
                "The recorded hit count concerns only a deterministic high-R bundle/gate after a "
                "same-chart nonmonotone support reset.  It is not a legal reset edge unless the "
                "separate parent/reset contract is supplied."
            ),
            "hit_boundary": (
                "Any paid gate hit whose target is exactly H_L is an h=0 direct self-loop at the "
                "reset state and must be suppressed by the direct-cofactor action rule; it does not "
                "supply a second strict recursive step."
            ),
            "phase_boundary": (
                "A gate hit need not be an exact reset-state self-loop.  Under the gate, write "
                "L=g*a, C=g*c, r=a*u and K=L*B.  Then target_support=L*c and "
                "h=(u*c-B)/p.  Exact reset-state return is equivalent to C dividing L; "
                "the named p=1201 control has h=0 but c=28."
            ),
            "legal_reset_contract": reset_contract(),
        },
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    summary = result["summary"]
    if args.verify:
        assert summary["frozen_distinct_high_anchors"] == 31
        assert summary["anchors_with_nonmonotone_reset"] == 25
        assert summary["nonmonotone_reset_attempts"] == 162
        assert summary["strictly_paid_reset_attempts"] == 135
        assert summary["raw_gate_hits"] == 1
        assert summary["strictly_paid_gate_hits"] == 1
        assert summary["strictly_paid_gate_hit_exact_reset_self_loops"] == 1
        phase_control = result["phase_boundary_control"]["cofactor_attempt"]["target_relation"][
            "phase_factorization"
        ]
        assert isinstance(phase_control, dict)
        assert phase_control["chart_return"] is True
        assert phase_control["exact_reset_state_self_loop"] is False
        print(
            "verified nonmonotone high-anchor reset atlas: "
            f"{summary['nonmonotone_reset_attempts']} resets, "
            f"{summary['strictly_paid_gate_hits']} paid gate hits"
        )
        return
    args.output.write_text(json.dumps(result, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
