#!/usr/bin/env python3
"""Replay the high-support C=1 direct-cofactor return lemma.

The verifier checks the gate decomposition and the positive-phase contradiction
symbolically, then replays exact same-chart controls.  It does not search
sources, terminal certificates, or the global selector.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import gcd, lcm
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
RECEIPT_PATH = ROOT / "data" / "t6-wave1" / "f2-high-support-c1-direct-cofactor-return-v1.json"


def canonical_chart(prime: int, support: int) -> tuple[int, int]:
    numerator = 4 * support - 1
    if numerator <= 0 or numerator % prime:
        raise AssertionError("support is not a canonical chart")
    return numerator // prime, support


def replay_candidate(prime: int, support: int, r: int, raw_c: int) -> dict[str, int]:
    if prime % 24 != 1 or not sympy.isprime(prime):
        raise AssertionError("control prime is outside the core domain")
    bound = (prime - 1) ** 2 // 4
    if support <= bound:
        raise AssertionError("parent is not high support")
    R, K = canonical_chart(prime, support)
    if K != support or not (prime < R < 4 * support):
        raise AssertionError("parent C=1 chart changed")
    if not (1 <= r < prime and 1 <= raw_c < prime):
        raise AssertionError("candidate cofactor range changed")
    target_support = lcm(support, raw_c)
    if (r * raw_c) % target_support:
        raise AssertionError("direct-cofactor gate failed")
    target_R_numerator = 4 * r * raw_c - 1
    if target_R_numerator <= 0 or target_R_numerator % prime:
        raise AssertionError("candidate target is not a positive chart")
    target_R = target_R_numerator // prime
    difference = r * raw_c - support
    if difference % (prime * support):
        raise AssertionError("three-phase h is not integral")
    h = difference // (prime * support)
    if h not in (0, 1, 2):
        raise AssertionError("three-phase phase range changed")

    g = gcd(support, raw_c)
    a = support // g
    c = raw_c // g
    if r % a:
        raise AssertionError("gate decomposition r=a*t failed")
    t = r // a
    if r * raw_c != support * c * t:
        raise AssertionError("decomposition identity changed")

    return {
        "p": prime,
        "A": support,
        "R": R,
        "r": r,
        "C": raw_c,
        "A_C": target_support,
        "g": g,
        "a": a,
        "c": c,
        "t": t,
        "h": h,
        "R_T": target_R,
        "K_T": r * raw_c,
    }


def verify_positive_phase_barrier(prime: int) -> None:
    if prime < 73 or prime % 24 != 1:
        raise AssertionError("core-prime lower bound changed")
    upper = Fraction((prime - 1) ** 2, prime + 1)
    if not upper < prime:
        raise AssertionError("positive-phase barrier is not below p")
    bound = Fraction((prime - 1) ** 2, 4)
    if not bound > prime:
        raise AssertionError("B_p>p fails in the declared core domain")
    if not upper < bound:
        raise AssertionError("barrier does not contradict high support")


def build_receipt() -> dict[str, object]:
    controls = []
    for prime in (73, 97, 193, 241, 313):
        verify_positive_phase_barrier(prime)
        half = (prime + 1) // 2
        controls.append(replay_candidate(prime, half * half, half, half))

    for row in controls:
        if row["h"] != 0 or row["c"] != 1 or row["t"] != 1:
            raise AssertionError("control did not land in exact return")
        if row["A_C"] != row["A"] or row["R_T"] != row["R"] or row["K_T"] != row["A"]:
            raise AssertionError("same-chart return identity changed")

    return {
        "artifact_id": "f2_high_support_c1_direct_cofactor_return_v1",
        "status": "DIRECT_COFACTOR_SUBFAMILY_EXACT_RETURN",
        "positive_phase_barrier": {
            "upper_bound": "(p-1)^2/(p+1)",
            "strictly_below": "p",
            "high_support_lower_bound": "B_p>p for p>=73",
        },
        "controls": controls,
        "conclusion": {
            "h_positive": "IMPOSSIBLE",
            "h_zero": "c=t=1 and exact same-chart return",
            "paid_E5_direct_cofactor": "EMPTY",
            "whole_C1": "OPEN",
        },
    }


def verify() -> dict[str, object]:
    receipt = build_receipt()
    stored = json.loads(RECEIPT_PATH.read_text(encoding="utf-8"))
    if stored["artifact_id"] != receipt["artifact_id"]:
        raise AssertionError("stored artifact id changed")
    if stored["status"] != receipt["status"]:
        raise AssertionError("stored status changed")
    if stored["conclusion"] != {
        "direct_cofactor_paid_E5_edge": "EMPTY",
        "same_chart_return": "UNIVERSAL_ON_DECLARED_ARITHMETIC_DOMAIN",
        "whole_C1_leaf": "OPEN",
        "global_F2_or_T6": "OPEN",
    }:
        raise AssertionError("stored boundary contract changed")
    if len(stored["controls"]) != len(receipt["controls"]):
        raise AssertionError("stored controls changed")
    return receipt


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    receipt = verify() if args.verify else build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
