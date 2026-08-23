#!/usr/bin/env python3
"""Focused replay of the deterministic low-chart support-doubling exit."""

from __future__ import annotations

import argparse
from math import lcm
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
REPRODUCTIONS = ROOT / "reproductions"
if str(REPRODUCTIONS) not in sys.path:
    sys.path.insert(0, str(REPRODUCTIONS))

import type_i_universal_anchor_overflow_dual as universal  # noqa: E402
import type_ii_q_one_full_carrier_phase_root_entry as q_one  # noqa: E402


def low_chart_exit(prime: int, R: int, A: int, max_steps: int = 256) -> dict[str, object]:
    B_p = (prime - 1) ** 2 // 4
    history: list[dict[str, object]] = []
    for _ in range(max_steps):
        K = (prime * R + 1) // 4
        if not (3 <= R <= prime - 2 and prime * R + 1 == 4 * K and K % A == 0):
            raise AssertionError("invalid low-chart source")
        source = universal.universal_p_source(prime, R)
        if K % (R - 1) == 0:
            return {
                "status": "terminal",
                "history": history,
                "terminal": {"R": R, "K": K, "A": A},
                "source": source,
            }

        Q, beta = universal.complete_bundle(R - 1, K)
        M = lcm(A, Q)
        target_R, target_K = universal.canonical_chart(prime, M)
        if not (
            Q > 1
            and beta * Q == R - 1
            and K % beta == 0
            and M > A
            and M // A >= 2
            and B_p // M < B_p // A
            and target_K % M == 0
            and target_R != prime
        ):
            raise AssertionError("support-doubling step changed")
        row = {
            "source": {"R": R, "K": K, "A": A},
            "Q": Q,
            "beta": beta,
            "target": {"R": target_R, "K": target_K, "A": M},
            "potential": {"source": B_p // A, "target": B_p // M},
        }
        history.append(row)
        if target_R > prime:
            return {"status": "overflow", "history": history, "target": row["target"]}
        R, A = target_R, M
    raise AssertionError("focused orbit exceeded its symbolic support bound")


def verify() -> dict[str, object]:
    controls: list[dict[str, object]] = []
    for prime in (73, 241, 2521):
        root = q_one.phase_root_entry(prime)["root"]
        result = low_chart_exit(
            prime,
            int(root["chart"]["R"]),
            int(root["absorbed_support"]),
        )
        B_p = (prime - 1) ** 2 // 4
        supports = [int(row["target"]["A"]) for row in result["history"]]
        previous = 1
        for support in supports:
            if support < 2 * previous:
                raise AssertionError("support did not at least double")
            previous = support
        if len(supports) > B_p.bit_length() + 1:
            raise AssertionError("focused orbit exceeded the coarse logarithmic bound")
        controls.append(
            {
                "p": prime,
                "status": result["status"],
                "step_count": len(result["history"]),
                "supports": supports,
            }
        )
    return {
        "status": "FOCUSED_LOW_CHART_EXITS_REPLAYED",
        "controls": controls,
        "proof_scope": "controls_check_implementation_only_symbolic_growth_proves_totality",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    print(verify()["status"])


if __name__ == "__main__":
    main()
