#!/usr/bin/env python3
"""Verify total-cofactor canonical projection and its persistence gate."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from math import isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MACRO_RESULTS = ROOT / "reproductions" / "type-i-high-anchor-cofactor-macro-replay-results.json"


@dataclass(frozen=True)
class FoldFixture:
    label: str
    p: int
    A: int
    M: int
    d: int
    n: int
    expected_target: tuple[int, int, int, int, int]


FIXTURES = (
    FoldFixture("p73_b2", 73, 58, 116, 14, 89, (58, 28, 89, 143, 2610)),
    FoldFixture("p73_b4", 73, 58, 232, 7, 89, (58, 28, 89, 143, 2610)),
    FoldFixture("p73_b101", 73, 58, 5858, 1, 321, (58, 28, 89, 143, 2610)),
    FoldFixture("p73_stutter", 73, 74, 4070, 72, 16057, (74, 18, 73, 223, 4070)),
    FoldFixture(
        "p1201_internal_receipt",
        1201,
        986,
        906134,
        249,
        751465,
        (986, 641, 2105, 1839, 552160),
    ),
)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def omega(value: int) -> int:
    count = 0
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            value //= divisor
            count += 1
        divisor += 1
    return count + (value > 1)


def project(fixture: FoldFixture) -> dict[str, int | tuple[int, ...]]:
    p, A, M, d, n = fixture.p, fixture.A, fixture.M, fixture.d, fixture.n
    assert is_prime(p) and p % 24 == 1
    assert p * n == 4 * M * d + 1
    assert M % A == 0 and 1 <= d < p and M % p

    b = M // A
    h, delta = divmod(b * d, p)
    C_A = pow(4 * A, -1, p)
    R_A = (4 * A * C_A - 1) // p
    K_A = A * C_A
    source_R = 4 * M - n
    source_K = M * (p - d)
    source_C = source_K // A
    t = (source_C - C_A) // p
    target_n = n - 4 * A * h
    target = (A, delta, target_n, R_A, K_A)

    assert 1 <= C_A < p and delta == p - C_A
    assert source_C == C_A + p * t
    assert t == b - 1 - h and t >= 0
    assert source_K - K_A == A * p * t
    assert source_R - R_A == 4 * A * t
    assert p * target_n == 4 * A * delta + 1
    assert target_n == 4 * A - R_A
    assert p * R_A + 1 == 4 * K_A
    assert (t == 0) == (source_C < p)
    assert (t > 0) == (source_C > p)
    assert (t > 0) == (K_A < source_K and R_A < source_R)
    assert target == fixture.expected_target
    return {
        "target": target,
        "source_R": source_R,
        "source_K": source_K,
        "source_C": source_C,
        "C_A": C_A,
        "t": t,
    }


def charged_rank(p: int, state: tuple[int, int, int]) -> tuple[int, int]:
    """Return (outer support rank, exact residual charged capacity)."""
    _, K, A = state
    assert K % A == 0
    return ((p - 1) ** 2 // (4 * A), K // A)


def p1201_macro_provenance() -> dict[str, tuple[int, int, int]]:
    """Load the recorded anchor, transient, and proper-cofactor target."""
    payload = json.loads(MACRO_RESULTS.read_text(encoding="utf-8"))
    assert payload["certificate_type"] == "high_anchor_cofactor_macro_replay_suite_v1"
    fixture = next(item for item in payload["fixtures"] if item["prime"] == 1201)
    macro = fixture["macro"]
    assert macro["certificate_type"] == "high_anchor_cofactor_macro_replay_v1"
    assert macro["selector_status"] == "analysis_evidence"
    assert macro["recursive_edge_eligible"] is False
    assert all(macro["links"].values())

    def state_tuple(name: str) -> tuple[int, int, int]:
        state = macro[name]
        assert state["state_id"].startswith("state:")
        return (int(state["R"]), int(state["K"]), int(state["absorbed_support"]))

    cofactor = macro["cofactor"]
    assert (cofactor["M"], cofactor["d"], cofactor["n"]) == (906134, 249, 751465)
    assert cofactor["g"] == 34 and cofactor["A_T"] == 27608
    return {
        "anchor": state_tuple("anchor_state"),
        "intermediate": state_tuple("intermediate_state"),
        "recorded_target": state_tuple("target_state"),
    }


def verify() -> None:
    receipts = {fixture.label: project(fixture) for fixture in FIXTURES}

    shared_target = receipts["p73_b2"]["target"]
    assert receipts["p73_b4"]["target"] == shared_target
    assert receipts["p73_b101"]["target"] == shared_target
    assert receipts["p73_stutter"]["t"] == 0

    # Exact K/A decreases although the old Omega coordinate increases.
    assert receipts["p73_b2"]["source_C"] == 118
    assert receipts["p73_b2"]["C_A"] == 45
    assert omega(118) == 2 and omega(45) == 3

    # Bind the derived total fold to the recorded anchor and transient provenance.
    internal = receipts["p1201_internal_receipt"]
    provenance = p1201_macro_provenance()
    parent = provenance["anchor"]
    source = provenance["intermediate"]
    recorded_target = provenance["recorded_target"]
    projected = internal["target"]
    assert source == (internal["source_R"], internal["source_K"], 986)
    assert internal["source_C"] == 874888 and internal["C_A"] == 560
    assert internal["t"] == 728
    assert (projected[3], projected[4], projected[0]) == parent
    assert (parent[0], parent[1] // parent[2]) == (projected[3], projected[4] // projected[0])
    assert recorded_target == (1839, 552160, 27608)
    assert charged_rank(1201, parent) == (365, 560)
    assert charged_rank(1201, recorded_target) == (13, 20)
    assert charged_rank(1201, parent) == charged_rank(
        1201, (projected[3], projected[4], projected[0])
    )

    print(f"verified {len(FIXTURES)} total-cofactor projection receipts")
    print("p73_unique_target", shared_target)
    print("omega_counterexample", "118:2 -> 45:3")
    print(
        "p1201_persistence_boundary",
        "derived total fold: parent rank stutters; recorded proper fold: (365,560)->(13,20)",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused exact checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
