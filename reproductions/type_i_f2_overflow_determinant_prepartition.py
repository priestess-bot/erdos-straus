#!/usr/bin/env python3
"""Replay the symbolic F2 determinant prepartition on focused controls.

The theorem is relative to an already admitted, actual persistent source and
its determinant receipt.  This program checks the arithmetic partition and
parent-to-target T5 ranks; it does not manufacture source actualness or grant
common-grammar admission to a target.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
from math import gcd, isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECEIPT_PATH = ROOT / "data" / "t6-wave1" / "f2-overflow-determinant-prepartition-v1.json"


@dataclass(frozen=True)
class SourceReceipt:
    name: str
    p: int
    R: int
    K: int
    A: int
    M: int
    d: int
    n: int


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def sharp_rank(p: int, K: int, A: int) -> tuple[int, int]:
    if A <= 0 or K % A:
        raise ValueError("charged support must be a positive divisor of K")
    return (p - 1) ** 2 // (4 * A), K // A


def validate_source(source: SourceReceipt) -> None:
    p, R, K, A, M, d, n = (
        source.p,
        source.R,
        source.K,
        source.A,
        source.M,
        source.d,
        source.n,
    )
    if not (
        is_prime(p)
        and p % 24 == 1
        and A > 1
        and M > 0
        and M % A == 0
        and 1 <= d < p
        and n > 0
        and p * n == 4 * M * d + 1
        and R == 4 * M - n > p
        and K == M * (p - d)
        and 4 * K == p * R + 1
        and K % A == 0
        and n % 4 == 1
    ):
        raise ValueError(f"{source.name}: invalid F2 overflow determinant receipt")


def partition(source: SourceReceipt) -> dict[str, object]:
    """Apply the theorem's post-terminal ordered arithmetic partition."""
    validate_source(source)
    p, R, K, A, M, d, n = (
        source.p,
        source.R,
        source.K,
        source.A,
        source.M,
        source.d,
        source.n,
    )
    Bp = (p - 1) ** 2 // 4
    b = M // A
    source_rank = sharp_rank(p, K, A)

    if b >= 2:
        target = {"p": p, "R": R, "K": K, "A": M}
        target_rank = sharp_rank(p, K, M)
        if not (
            target_rank < source_rank
            and target_rank[0] <= source_rank[0]
            and target_rank[1] == p - d < b * (p - d) == source_rank[1]
        ):
            raise AssertionError("same-chart branch lost its strict sharp-rank payment")
        return {
            "source": asdict(source),
            "branch": "SAME_CHART_SUPPORT_PROMOTION",
            "guard": {"b": b, "b_at_least_two": True},
            "target": target,
            "source_rank": list(source_rank),
            "target_rank": list(target_rank),
            "ticket": "LOCAL_DROP",
            "target_is_overflow": True,
            "contract_boundary": "relative_to_actual_source_and_common_E3_admission",
        }

    if M != A:
        raise AssertionError("b=1 did not force M=A")

    if A <= Bp and d >= 2:
        L = M * d
        target_R = 4 * L - n
        target_K = L * (p - 1)
        target_rank = sharp_rank(p, target_K, L)
        if n == 1:
            # The two source equations would give A=(p-1)/(4d), contradicting R>p.
            raise AssertionError("an overflow full-product branch cannot have n=1")
        if not (
            L >= 2 * A
            and target_R == (p - 1) * n - 1 > p
            and 4 * target_K == p * target_R + 1
            and target_rank[0] < source_rank[0]
            and target_rank < source_rank
        ):
            raise AssertionError("full-product branch lost its strict outer-rank payment")
        return {
            "source": asdict(source),
            "branch": "FULL_PRODUCT_FIXED_N_DESCENT",
            "guard": {"b": 1, "A_le_Bp": True, "d_at_least_two": True},
            "target": {"p": p, "R": target_R, "K": target_K, "A": L},
            "source_rank": list(source_rank),
            "target_rank": list(target_rank),
            "ticket": "LOCAL_DROP",
            "target_is_overflow": True,
            "contract_boundary": "relative_to_actual_source_and_common_E3_admission",
        }

    if A <= Bp:
        if d != 1:
            raise AssertionError("low-support complement must be d=1")
        canonical_capacity = p - 1
        if not (
            K == A * canonical_capacity
            and pow(4 * A, -1, p) == canonical_capacity
            and 5 <= n <= p - 4
        ):
            raise AssertionError("low d=1 residual is not support-canonical")
        alpha = (p + 1) // 2
        v = (n + 1) // 2
        normalized_gcd = gcd(alpha, v)
        multiplier = ((p - 1) * n - 2) // (2 * normalized_gcd)
        target_support = A * multiplier
        target_capacity = (-pow(multiplier, -1, p)) % p
        target_K = target_support * target_capacity
        target_R = (4 * target_K - 1) // p
        target_rank = sharp_rank(p, target_K, target_support)
        if not (
            multiplier > 1
            and multiplier % p != 0
            and target_support > p * p > Bp
            and target_R > p
            and 4 * target_K == p * target_R + 1
            and target_rank[0] == 0 < source_rank[0]
            and target_rank < source_rank
        ):
            raise AssertionError("low d=1 complete-excess outer drop changed")
        return {
            "source": asdict(source),
            "branch": "LOW_SUPPORT_D_ONE_COMPLETE_EXCESS_OUTER_DROP",
            "guard": {"b": 1, "A_le_Bp": True, "d": 1},
            "target": {
                "p": p,
                "R": target_R,
                "K": target_K,
                "A": target_support,
                "capacity": target_capacity,
                "multiplier": multiplier,
            },
            "source_rank": list(source_rank),
            "target_rank": list(target_rank),
            "ticket": "LOCAL_DROP",
            "target_is_overflow": True,
            "canonical_capacity": canonical_capacity,
            "contract_boundary": "relative_to_actual_source_and_common_E3_admission",
        }

    capacity = p - d
    if not (
        1 <= capacity < p
        and K == A * capacity
        and pow(4 * A, -1, p) == capacity
        and source_rank == (0, capacity)
    ):
        raise AssertionError("high-support complement is not the canonical C state")
    return {
        "source": asdict(source),
        "branch": (
            "HIGH_SUPPORT_CANONICAL_C_ONE_RESIDUAL"
            if capacity == 1
            else "HIGH_SUPPORT_CANONICAL_C_GT_ONE_RESIDUAL"
        ),
        "guard": {"b": 1, "A_gt_Bp": True, "C": capacity},
        "target": None,
        "source_rank": list(source_rank),
        "target_rank": None,
        "ticket": None,
        "canonical_capacity": capacity,
        "contract_boundary": "route_to_high_support_C_partition",
    }


CONTROLS = (
    SourceReceipt("same_chart_low_to_high", 73, 3743, 68310, 66, 1518, 28, 2329),
    SourceReceipt("low_support_full_product", 73, 287, 5238, 97, 97, 19, 101),
    SourceReceipt("low_support_d_one", 73, 359, 6552, 91, 91, 1, 5),
    SourceReceipt("high_support_c_one", 73, 75, 1369, 1369, 1369, 72, 5401),
    SourceReceipt("high_support_c_two", 73, 143, 2610, 1305, 1305, 71, 5077),
    SourceReceipt("p409_anomaly", 409, 511, 52250, 5, 250, 200, 489),
)


def build_receipt() -> dict[str, object]:
    rows = [partition(source) for source in CONTROLS]
    p409 = next(row for row in rows if row["source"]["name"] == "p409_anomaly")
    if not (
        [row["branch"] for row in rows]
        == [
            "SAME_CHART_SUPPORT_PROMOTION",
            "FULL_PRODUCT_FIXED_N_DESCENT",
            "LOW_SUPPORT_D_ONE_COMPLETE_EXCESS_OUTER_DROP",
            "HIGH_SUPPORT_CANONICAL_C_ONE_RESIDUAL",
            "HIGH_SUPPORT_CANONICAL_C_GT_ONE_RESIDUAL",
            "SAME_CHART_SUPPORT_PROMOTION",
        ]
        and p409["target"] == {"p": 409, "R": 511, "K": 52250, "A": 250}
        and p409["source_rank"] == [8323, 10450]
        and p409["target_rank"] == [166, 209]
    ):
        raise AssertionError("focused determinant prepartition controls changed")
    return {
        "artifact_id": "f2_overflow_determinant_prepartition_v1",
        "theorem": "type-I-f2-overflow-determinant-prepartition",
        "status": "ARITHMETIC_AND_T5_PARTITION_ESTABLISHED_F2_OPEN",
        "branch_order": [
            "TERMINAL_FIRST",
            "SAME_CHART_SUPPORT_PROMOTION",
            "FULL_PRODUCT_FIXED_N_DESCENT",
            "LOW_SUPPORT_D_ONE_COMPLETE_EXCESS_OUTER_DROP",
            "HIGH_SUPPORT_CANONICAL_C_ONE_RESIDUAL",
            "HIGH_SUPPORT_CANONICAL_C_GT_ONE_RESIDUAL",
        ],
        "controls": rows,
        "p409_disposition": {
            "without_actual_source": "OUTSIDE_QUANTIFIED_DOMAIN",
            "with_exact_actual_determinant": "PREEMPTED_BY_SAME_CHART_SUPPORT_PROMOTION",
            "forbidden": "self_reported_fixed_n_eligibility_or_overflow_label_on_R=11_target",
        },
        "ordered_total_cofactor_disposition": {
            "b_at_least_two": "PREEMPTED_BY_EARLIER_SAME_CHART_STRICT_BRANCH",
            "b_equals_one": "REJECT_CANONICAL_STUTTER_T_EQUALS_ZERO",
            "strict_later_branch": "EMPTY",
        },
        "open_after_partition": [
            "high_support_M=A_C=1",
            "high_support_M=A_C>1",
            "common_E3_admission_for_the_three_strict_branch_types",
        ],
    }


def verify() -> None:
    expected = json.loads(RECEIPT_PATH.read_text(encoding="utf-8"))
    actual = build_receipt()
    # The checked-in receipt is intentionally compact; compare mathematical
    # fields rather than incidental JSON key ordering or optional prose fields.
    expected_controls = [
        {
            "name": row["source"]["name"],
            "branch": row["branch"],
            "source_rank": row["source_rank"],
            "target_rank": row["target_rank"],
            "ticket": row["ticket"],
        }
        for row in expected["controls"]
    ]
    actual_controls = [
        {
            "name": row["source"]["name"],
            "branch": row["branch"],
            "source_rank": row["source_rank"],
            "target_rank": row["target_rank"],
            "ticket": row["ticket"],
        }
        for row in actual["controls"]
    ]
    if not (
        expected["artifact_id"] == actual["artifact_id"]
        and expected_controls == actual_controls
        and expected["ordered_total_cofactor_disposition"]
        == actual["ordered_total_cofactor_disposition"]
        and expected["p409_disposition"] == actual["p409_disposition"]
        and expected["open_after_partition"] == actual["open_after_partition"]
    ):
        raise AssertionError("stored determinant prepartition receipt is stale")
    print(
        "verified F2 determinant prepartition: b>=2 same-chart; "
        "b=1 low-support d>=2 full-product; exact low-d1/high-support residuals; "
        "p=409 preempted-or-out-of-domain"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    receipt = build_receipt()
    if args.json:
        print(json.dumps(receipt, indent=2, sort_keys=True))
        return
    if not args.verify:
        parser.error("pass --verify or --json")
    verify()


if __name__ == "__main__":
    main()
