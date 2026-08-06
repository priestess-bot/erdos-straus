#!/usr/bin/env python3
"""Enumerate paid support-monotone same-chart lifts before a high-R cofactor gate.

For a fixed high canonical chart ``(p, R, K; A)``, a same-chart lift that
preserves the charged-support divisibility chain ``A | L`` is algebraically
available exactly on the finite divisor interval

    A | L | K,  A < L <= B_p.

The high inequality ``R < 4A`` makes every such ``L`` canonical for the same
``(p, R, K)`` chart.  The program replays the deterministic full-excess
bundle from each such support and tests the *new* cofactor gate.  It reads the
frozen parent atlas only; it never runs or changes the global selector.
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
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-high-anchor-same-chart-gate-engineering-results.json"

# These are independently typed high-macro controls, not rows from the frozen
# selector artifact.  They delimit what this arithmetic atlas can and cannot
# say about a fully replayed macro.
CONTROLS = (
    {"label": "p1201_h0_F_F_F", "p": 1201, "R": 1839, "K": 552_160, "A": 986},
    {"label": "p3793_h1_G_F_F", "p": 3793, "R": 7011, "K": 6_648_181, "A": 1811},
    {
        "label": "p60913_h2_G_G_F",
        "p": 60_913,
        "R": 72_259,
        "K": 1_100_378_117,
        "A": 18_647,
    },
)


def canonical_hash(payload: object) -> str:
    return hashlib.sha256(
        json.dumps(payload, ensure_ascii=True, sort_keys=True, separators=(",", ":")).encode(
            "ascii"
        )
    ).hexdigest()


def divisors(value: int) -> list[int]:
    if value <= 0:
        raise AssertionError("divisors require a positive value")
    result = [1]
    for prime, exponent in shared.factorization(value):
        result = [item * prime**power for item in result for power in range(exponent + 1)]
    return sorted(result)


def potential(prime: int, support: int) -> int:
    return ((prime - 1) ** 2 // 4) // support


def exact_paid_support_lattice(prime: int, R: int, K: int, A: int) -> list[int]:
    """Return precisely the support-monotone same-chart Pi_p promotions."""
    B_p = (prime - 1) ** 2 // 4
    base_conditions = {
        "core_prime": shared.is_prime(prime) and prime % 24 == 1,
        "high_canonical_chart": shared.canonical_chart(prime, A) == (R, K),
        "high_window": prime < R < 4 * A,
        "support_divides_K": K % A == 0,
        "outer_rank_domain": A <= B_p,
    }
    required_anchor_conditions = (
        "core_prime",
        "high_canonical_chart",
        "high_window",
        "support_divides_K",
    )
    if not all(base_conditions[key] for key in required_anchor_conditions):
        raise AssertionError(f"not a paid high anchor: {base_conditions}")
    if not base_conditions["outer_rank_domain"]:
        return []
    candidates = [
        L
        for L in divisors(K)
        if L % A == 0 and A < L <= B_p
    ]
    for L in candidates:
        # R<4A<4L and L|K make this a same-chart canonical support.
        if shared.canonical_chart(prime, L) != (R, K):
            raise AssertionError("divisor lattice did not preserve the chart")
        if not (potential(prime, L) < potential(prime, A)):
            raise AssertionError("paid same-chart lattice did not lower Pi_p")
        C_source = K // L
        n_source = 4 * L - R
        d_source = prime - C_source
        if not (
            C_source > 0
            and n_source > 0
            and d_source > 0
            and prime * n_source == 4 * L * d_source + 1
        ):
            raise AssertionError("re-factored same-chart overflow determinant failed")
    return candidates


def cofactor_attempt(prime: int, R: int, K: int, A: int, L: int) -> dict[str, object]:
    """Replay the high bundle from promoted support L and test its exact gate."""
    bundle = shared.high_R_path_anchored_bundle(prime=prime, R=R, support=L)
    rechart = bundle["rechart"]
    if not isinstance(rechart, dict) or rechart.get("result_class") != "overflow":
        raise AssertionError("a high anchor must replay to an overflow bundle")
    Q = int(bundle["complete_excess_bundle"]["Q"])
    M = int(rechart["M"])
    R_M = int(rechart["R"])
    K_M = int(rechart["K"])
    C = int(rechart["C"])
    d = int(rechart["d"])
    n = int(rechart["n"])
    k, r = divmod(M, prime)
    numerator = 4 * r * d + 1
    if numerator % prime:
        raise AssertionError("cofactor s integrality changed")
    s = numerator // prime
    R_T = 4 * r - s
    K_T = r * C
    g = gcd(L, C)
    a = L // g
    A_T = lcm(L, C)
    gate = r % a == 0
    target_checks = {
        "intermediate_chart": shared.canonical_chart(prime, M) == (R_M, K_M),
        "intermediate_determinant": prime * n == 4 * M * d + 1,
        "cofactor_identity": prime * s == 4 * r * d + 1,
        "target_chart_equation": prime * R_T + 1 == 4 * K_T,
        "gate": gate,
        "target_support_divides_K": gate and K_T % A_T == 0,
        "canonical_target": gate and shared.canonical_chart(prime, A_T) == (R_T, K_T),
    }
    always_required = (
        "intermediate_chart",
        "intermediate_determinant",
        "cofactor_identity",
        "target_chart_equation",
    )
    if not all(target_checks[key] for key in always_required):
        raise AssertionError("cofactor arithmetic identity changed")
    if gate and not all(target_checks.values()):
        raise AssertionError("a passing cofactor target normal form changed")
    return {
        "promoted_support": L,
        "source_same_chart": {"R": R, "K": K, "C": K // L},
        "bundle": {"Q": Q, "M": M, "R": R_M, "K": K_M, "C": C, "d": d, "n": n},
        "cofactor": {
            "k": k,
            "r": r,
            "s": s,
            "gcd_L_C": g,
            "L_over_gcd": a,
            "target_support": A_T,
            "R": R_T,
            "K": K_T,
        },
        "gate_passes": gate,
        "gate_diagnostic": {
            "size_obstruction_L_over_gcd_gt_r": a > r,
            "remainder_mod_L_over_gcd": r % a,
        },
        "target_checks": target_checks,
        "pi_p": {
            "pre_promotion": potential(prime, A),
            "promoted_source": potential(prime, L),
            "target": potential(prime, A_T) if gate else None,
            "promotion_strict": potential(prime, L) < potential(prime, A),
            "macro_strict_if_gate": gate and potential(prime, A_T) < potential(prime, L),
        },
    }


def baseline_attempt(prime: int, R: int, K: int, A: int) -> dict[str, object]:
    """The unpromoted gate is recorded only as a comparison point."""
    bundle = shared.high_R_path_anchored_bundle(prime=prime, R=R, support=A)
    rechart = bundle["rechart"]
    if not isinstance(rechart, dict) or rechart.get("result_class") != "overflow":
        raise AssertionError("baseline high bundle changed")
    M, C = int(rechart["M"]), int(rechart["C"])
    r = M % prime
    a = A // gcd(A, C)
    return {"M": M, "C": C, "r": r, "A_over_gcd": a, "gate_passes": r % a == 0}


def analyse_anchor(entry: dict[str, object], origin: str, occurrences: int) -> dict[str, object]:
    prime, R, K, A = (int(entry[key]) for key in ("p", "R", "K", "A"))
    lattice = exact_paid_support_lattice(prime, R, K, A)
    attempts = [cofactor_attempt(prime, R, K, A, L) for L in lattice]
    hits = [attempt for attempt in attempts if attempt["gate_passes"]]
    baseline = baseline_attempt(prime, R, K, A)
    return {
        "row_id": "same-chart-gate:" + canonical_hash([prime, R, K, A])[:16],
        "origin": origin,
        "frozen_occurrences": occurrences,
        "anchor": {"p": prime, "R": R, "K": K, "absorbed_support": A},
        "B_p": (prime - 1) ** 2 // 4,
        "same_chart_promotion_domain": A <= (prime - 1) ** 2 // 4,
        "K_factorization": [list(item) for item in shared.factorization(K)],
        "unpromoted_gate": baseline,
        "paid_support_lattice": lattice,
        "cofactor_attempts": attempts,
        "gate_hits_after_paid_promotion": hits,
        "scope": (
            "Arithmetic plus support-monotone Pi_p payment only. A hit does not supply a typed fiber, "
            "a content-addressed parent chain, terminal-first exhaustion, or a selector edge."
        ),
    }


def frozen_entries() -> list[tuple[dict[str, object], int]]:
    payload = json.loads(ATLAS_INPUT.read_text(encoding="utf-8"))
    grouped: dict[tuple[int, int, int, int], int] = {}
    for row in payload["rows"]:
        if not row.get("high_anchor_candidate"):
            continue
        anchor = row["anchor"]
        key = tuple(int(anchor[key]) for key in ("p", "R", "K", "absorbed_support"))
        grouped[key] = grouped.get(key, 0) + 1
    entries = []
    for prime, R, K, A in sorted(grouped):
        entries.append(({"p": prime, "R": R, "K": K, "A": A}, grouped[(prime, R, K, A)]))
    return entries


def build_result() -> dict[str, object]:
    frozen = [analyse_anchor(entry, "frozen_verified_parent_atlas", count) for entry, count in frozen_entries()]
    controls = [analyse_anchor(dict(entry), "independent_high_macro_control", 0) for entry in CONTROLS]
    frozen_attempts = [attempt for row in frozen for attempt in row["cofactor_attempts"]]
    frozen_hits = [attempt for attempt in frozen_attempts if attempt["gate_passes"]]
    return {
        "schema_version": 1,
        "certificate_type": "type_i_high_anchor_same_chart_gate_engineering_v1",
        "inputs": {
            "frozen_parent_atlas": {
                "path": str(ATLAS_INPUT.relative_to(ROOT)),
                "sha256": hashlib.sha256(ATLAS_INPUT.read_bytes()).hexdigest(),
            }
        },
        "exact_domain": {
            "paid_support_monotone_lattice": "{L : A divides L divides K, A < L <= B_p}",
            "why_same_chart": "R<4A<4L and L|K imply canonical_chart(p,L)=(R,K)",
            "exact_gate": "L/gcd(L,C_L) divides r_L, where M_L=lcm(L,Q), C_L=K_{M_L}/M_L, r_L=M_L mod p",
            "payment": "Pi_p(L)<Pi_p(A); if the gate passes, require a separate macro E5 check from L to lcm(L,C_L)",
        },
        "summary": {
            "frozen_high_anchor_occurrences": sum(row["frozen_occurrences"] for row in frozen),
            "frozen_distinct_high_anchors": len(frozen),
            "frozen_anchors_with_paid_support_promotion": sum(bool(row["paid_support_lattice"]) for row in frozen),
            "frozen_paid_promotion_attempts": len(frozen_attempts),
            "frozen_gate_hits_after_paid_promotion": len(frozen_hits),
            "frozen_baseline_gate_hits": sum(bool(row["unpromoted_gate"]["gate_passes"]) for row in frozen),
            "control_gate_hits_after_paid_promotion": sum(
                len(row["gate_hits_after_paid_promotion"]) for row in controls
            ),
        },
        "conclusion": {
            "frozen_atlas": (
                "No paid support-monotone same-chart promotion makes the high-R full-excess cofactor gate pass "
                "on any of the 31 distinct frozen verified-parent high anchors."
            ),
            "controls": (
                "The p=1201 control has one paid promoted gate hit, but its unpromoted gate already passes; "
                "p=3793 and p=60913 have no paid proper same-chart support lift. Thus the finite evidence "
                "does not exhibit a gate rescue from a failing high anchor."
            ),
            "proof_boundary": (
                "This is a finite arithmetic atlas plus the support-monotone same-chart Pi_p lemma. It neither "
                "upgrades legacy parents nor excludes non-divisibility support resets or proves global availability "
                "of a cofactor macro."
            ),
        },
        "frozen_rows": frozen,
        "independent_controls": controls,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    summary = result["summary"]
    if args.verify:
        assert summary["frozen_high_anchor_occurrences"] == 51
        assert summary["frozen_distinct_high_anchors"] == 31
        assert summary["frozen_gate_hits_after_paid_promotion"] == 0
        assert summary["frozen_baseline_gate_hits"] == 0
        assert summary["control_gate_hits_after_paid_promotion"] == 1
        print(
            "verified paid same-chart gate atlas: "
            f"{summary['frozen_paid_promotion_attempts']} frozen attempts, no gate rescue"
        )
        return
    args.output.write_text(json.dumps(result, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
