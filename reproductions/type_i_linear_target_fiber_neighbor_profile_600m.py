#!/usr/bin/env python3
"""Audit target-fiber near pairs on the frozen 200-point linear spectrum."""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-linear-b-gt-one-full-spectrum-profile-600m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-linear-target-fiber-neighbor-profile-600m-results.json"
EXPECTED_INPUT_SHA256 = "71b24dc30fce218f02d7c81cd8c716b6d60e874e7701161e0887575f2d5f3d2f"
EXPECTED_HIT_COUNT = 1_018
EXPECTED_NEAR_COUNT = 792
EXPECTED_EXCESS_COUNTS = {-1: 6, 0: 786, 1: 150, 2: 51, 3: 14, 4: 7, 5: 3, 8: 1}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def target_fiber(R: int, K: int) -> tuple[list[tuple[int, ...]], list[int], list[int]]:
    factors = sorted((int(q), int(e)) for q, e in sympy.factorint(K).items())
    primes = [q for q, _ in factors]
    budgets = [e for _, e in factors]
    vectors = []
    target = (-K) % R
    for exponents in itertools.product(
        *(range(2 * budget + 1) for budget in budgets)
    ):
        divisor = math.prod(q**exponent for q, exponent in zip(primes, exponents))
        if divisor % R == target:
            vectors.append(
                tuple(exponent - budget for exponent, budget in zip(exponents, budgets))
            )
    return vectors, primes, budgets


def pair_excess(left: tuple[int, ...], right: tuple[int, ...], budgets: list[int]) -> int:
    return max(
        abs(left_i - right_i) - budget
        for left_i, right_i, budget in zip(left, right, budgets)
    )


def oriented_terminal(
    R: int,
    K: int,
    primes: list[int],
    left: tuple[int, ...],
    right: tuple[int, ...],
) -> dict[str, object]:
    delta = [left_i - right_i for left_i, right_i in zip(left, right)]
    numerator = math.prod(
        q**power for q, power in zip(primes, delta) if power > 0
    )
    denominator = math.prod(
        q**(-power) for q, power in zip(primes, delta) if power < 0
    )
    if numerator > denominator:
        left, right = right, left
        delta = [-power for power in delta]
        numerator, denominator = denominator, numerator
    rho = Fraction(numerator, denominator)
    if not (0 < rho < 1):
        raise AssertionError("target pair did not produce a nontrivial ratio")
    if K % denominator:
        raise AssertionError("near-pair ratio does not produce an integer U")
    U = K * numerator // denominator
    E = 4 * U
    p = (4 * K - 1) // R
    n_numerator = 4 * K - E
    if (
        U < 1
        or U >= K
        or (K * K) % U
        or E % (4 * U)
        or E % R != 1 % R
        or E > 4 * K - 4 * R
        or n_numerator <= 0
        or n_numerator % R
        or n_numerator // R >= p
        or (n_numerator // R) % 4
    ):
        raise AssertionError("near-pair terminal check failed")
    return {
        "z": list(left),
        "w": list(right),
        "rho_num": numerator,
        "rho_den": denominator,
        "U": U,
        "E": E,
        "n": n_numerator // R,
    }


def audit_record(R: int, K: int) -> dict[str, object]:
    vectors, primes, budgets = target_fiber(R, K)
    if len(vectors) < 2:
        raise AssertionError("a hit state must have an antipodal target pair")
    candidates = []
    for left, right in itertools.combinations(vectors, 2):
        excess = pair_excess(left, right, budgets)
        candidates.append(
            (
                excess,
                sum(abs(left_i - right_i) for left_i, right_i in zip(left, right)),
                left,
                right,
            )
        )
    excess, distance, left, right = min(candidates)
    record: dict[str, object] = {
        "R": R,
        "K": K,
        "prime": (4 * K - 1) // R,
        "support_primes": primes,
        "support_budgets": budgets,
        "target_fiber_size": len(vectors),
        "minimum_pair_excess": excess,
        "minimum_pair_l1_distance": distance,
        "minimum_pair": {"z": list(left), "w": list(right)},
        "near_pair": excess <= 0,
    }
    if excess <= 0:
        record["terminal"] = oriented_terminal(R, K, primes, left, right)
    return record


def load_hit_states(path: Path = INPUT) -> list[tuple[int, int]]:
    if sha256(path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen full-spectrum input changed")
    payload = json.loads(path.read_text(encoding="utf-8"))
    states = []
    for profile in payload["profiles"]:
        for row in profile["records"]:
            if row["classification"] == "hit":
                states.append((int(row["R"]), int(row["K"])))
    if len(states) != EXPECTED_HIT_COUNT:
        raise AssertionError("the frozen hit-state count changed")
    return sorted(states)


def run_audit(path: Path = INPUT) -> dict[str, object]:
    records = [audit_record(R, K) for R, K in load_hit_states(path)]
    near_count = sum(bool(record["near_pair"]) for record in records)
    excess_counts = Counter(int(record["minimum_pair_excess"]) for record in records)
    expected = {str(key): value for key, value in EXPECTED_EXCESS_COUNTS.items()}
    actual = {str(key): int(value) for key, value in sorted(excess_counts.items())}
    if near_count != EXPECTED_NEAR_COUNT or actual != expected:
        raise AssertionError(
            f"target-fiber profile changed: near={near_count}, excess={actual}"
        )
    terminal_ns = [
        int(record["terminal"]["n"])
        for record in records
        if record["near_pair"]
    ]
    return {
        "arithmetic": (
            "for every hit state in the frozen 200-point complete linear spectrum, "
            "enumerate all d|K^2 with d=-K (mod R), convert to exponent vectors, "
            "find the minimum coordinate-budget pair excess, and verify the near-pair terminal"
        ),
        "scope_note": (
            "This is a finite audit of 1,018 hit states. It measures the near-pair branch "
            "of the fixed-state selector and does not prove that every Type II miss has such a state."
        ),
        "input": path.name,
        "input_sha256": sha256(path),
        "hit_state_count": len(records),
        "near_pair_count": near_count,
        "near_pair_fraction": near_count / len(records),
        "non_near_pair_count": len(records) - near_count,
        "minimum_pair_excess_distribution": actual,
        "near_terminal_n_min": min(terminal_ns),
        "near_terminal_n_max": max(terminal_ns),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.input)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {key: value for key, value in payload.items() if key != "records"},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
