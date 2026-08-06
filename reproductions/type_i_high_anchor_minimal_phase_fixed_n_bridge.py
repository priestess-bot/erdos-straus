#!/usr/bin/env python3
"""Targeted replay of the minimal-positive-phase fixed-n descent bridge.

The four fixtures are either arithmetic-only controls or already local macro
controls.  This script verifies only the algebraic bridge from a minimal
positive cofactor phase to the bounded fixed-n pivot; it neither invokes nor
upgrades the global selector.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-high-anchor-minimal-phase-fixed-n-bridge-results.json"
)


@dataclass(frozen=True)
class Fixture:
    prime: int
    phase: int
    support: int
    anchor_R: int
    anchor_K: int
    target_defect: int
    provenance: str


FIXTURES = (
    Fixture(1201, 1, 319, 1259, 378015, 8, "arithmetic_only"),
    Fixture(1201, 2, 346, 1263, 379216, 35, "arithmetic_only"),
    Fixture(3793, 1, 1811, 7011, 6648181, 61, "local_candidate"),
    Fixture(60913, 2, 18647, 72259, 1100378117, 634, "local_candidate"),
)


def canonical_chart(prime: int, support: int) -> tuple[int, int]:
    modulus = 4 * support
    R = (-pow(prime, -1, modulus)) % modulus
    K = (prime * R + 1) // 4
    if not (1 <= R < modulus and prime * R + 1 == 4 * K and K % support == 0):
        raise AssertionError("canonical chart failed")
    return R, K


def verify_omitted_cofactor_range_boundary() -> dict[str, object]:
    """Show why the direct r-chart requirement C<p is indispensable."""
    p, h, A, R, K, d_T = 73, 1, 82, 319, 5822, 1
    q = h + 1
    C = q * A
    B = K // A
    n = 4 * A - R
    t = p - d_T
    A_T = C
    S = A_T * d_T
    R_T = 4 * A_T - n
    K_T = A_T * t
    checks = {
        "high_anchor": p < R < 4 * A
        and p * R + 1 == 4 * K
        and canonical_chart(p, A) == (R, K),
        "formal_minimal_phase": B == p - q * d_T
        and q * t == B + p * h
        and K_T - K == p * A * h,
        "target_chart": p * R_T + 1 == 4 * K_T
        and canonical_chart(p, A_T) == (R_T, K_T),
        "outside_direct_cofactor_domain": C >= p,
        "unit_target_defect": d_T == 1 and S == A_T,
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"omitted-range boundary failed: {failed}")
    return {
        "prime": p,
        "phase": h,
        "anchor": {"A": A, "R": R, "K": K, "n": n},
        "formal_target": {"C": C, "A_T": A_T, "t": t, "d_T": d_T},
        "fixed_n_quantity": {"S": S, "strict_support_growth": A_T < S},
        "classification": "excluded_without_C_less_than_p",
        "checks": checks,
    }


def verify_fixture(item: Fixture) -> dict[str, object]:
    p, h, A, R, K, d_T = (
        item.prime,
        item.phase,
        item.support,
        item.anchor_R,
        item.anchor_K,
        item.target_defect,
    )
    q = h + 1
    A_T = q * A
    B_p = (p - 1) ** 2 // 4
    B = K // A
    t = p - d_T
    n = 4 * A - R
    K_T = A_T * t
    R_T = 4 * A_T - n
    S = A_T * d_T
    L = S
    R_L = 4 * L - n
    K_L = L * (p - 1)
    pi_target = B_p // A_T
    pi_pivot = B_p // L

    checks = {
        "core_prime_class": p % 24 == 1,
        "anchor_high_canonical": p < R < 4 * A
        and p * R + 1 == 4 * K
        and K % A == 0
        and canonical_chart(p, A) == (R, K),
        "minimal_positive_parameters": h in (1, 2)
        and q in (2, 3)
        and A_T < p,
        "minimal_phase_relation": B == p - q * d_T and q * t == B + p * h,
        "target_is_fixed_n_shadow": K_T - K == p * A * h
        and p * R_T + 1 == 4 * K_T
        and canonical_chart(p, A_T) == (R_T, K_T)
        and p * n == 4 * A_T * d_T + 1,
        "residual_window": 5 <= n <= p - 4 and n % 4 == 1,
        "target_defect_forced_nonunit": d_T >= 2,
        "saturated_divisor": (
            S == (p * n - 1) // 4 and A_T < L <= B_p and 4 * L > n
        ),
        "pivot_chart": R_L == (p - 1) * n - 1
        and R_L > p
        and p * R_L + 1 == 4 * K_L
        and canonical_chart(p, L) == (R_L, K_L),
        "strict_outer_payment": pi_pivot < pi_target,
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"bridge fixture failed: {failed}")

    return {
        "prime": p,
        "phase": h,
        "provenance": item.provenance,
        "anchor": {"A": A, "B": B, "R": R, "K": K, "n": n},
        "minimal_target": {"A": A_T, "t": t, "d_T": d_T, "R": R_T, "K": K_T},
        "fixed_n_pivot": {
            "S": S,
            "L": L,
            "R": R_L,
            "K": K_L,
            "Pi_before": pi_target,
            "Pi_after": pi_pivot,
        },
        "checks": checks,
    }


def build_result() -> dict[str, object]:
    rows = [verify_fixture(item) for item in FIXTURES]
    excluded_boundary = verify_omitted_cofactor_range_boundary()
    return {
        "schema_version": 1,
        "certificate_type": "high_anchor_minimal_phase_fixed_n_bridge_v1",
        "selector_status": "analysis_evidence",
        "recursive_edge_eligible": False,
        "scope": {
            "targeted_fixtures": len(rows),
            "does_not_verify": [
                "charged_parent_receipt",
                "terminal_first_exhaustion",
                "global_E1_E5_macro_admission",
            ],
            "conditional_conclusion": (
                "A minimal positive target with an admissible inherited state receipt "
                "has a forced bounded fixed-n strict-potential successor."
            ),
        },
        "fixtures": rows,
        "excluded_boundary_without_C_less_than_p": excluded_boundary,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if not args.verify:
        args.output.write_text(
            json.dumps(result, ensure_ascii=True, indent=2) + "\n", encoding="utf-8"
        )
    print(
        json.dumps(
            {
                "fixtures": len(result["fixtures"]),
                "excluded_boundaries": 1,
                "all_strict_pivot_payments": True,
                "selector_status": result["selector_status"],
            },
            ensure_ascii=True,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
