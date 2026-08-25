#!/usr/bin/env python3
"""Verify the exact support filter for the two determinant dual carriers.

For an overflow receipt pn = 4 M d + 1, write M = k p + r.  The d- and
r-dual charts are the only symmetric small-chart candidates used here.  This
script checks that their old-support divisibility tests are equivalent to the
two quotient congruences

    A/gcd(A,d) | k + 1,
    A/gcd(A,r) | d*n - 1.

The residual factors are recorded as signed q-adic support obstructions.  The
criterion is an exact filter for these dual charts, not a claim that one of
them always gives a recursive edge.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import gcd, lcm
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-universal-anchor-overflow-dual-results.json"
OUTPUT = ROOT / "reproductions" / "type-i-overflow-support-preserving-dual-criterion-results.json"
EXPECTED_INPUT_SHA256 = (
    "74724ef248bd13b5dbd0977ede341315f22302357b513c3f8b45602036d8101a"
)
EXPECTED_CASE_COUNT = 12


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def factorization(value: int) -> dict[int, int]:
    if value <= 0:
        raise AssertionError("factorization requires a positive integer")
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor:
            divisor = 3 if divisor == 2 else divisor + 2
            continue
        exponent = 0
        while value % divisor == 0:
            value //= divisor
            exponent += 1
        factors[divisor] = exponent
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[value] = 1
    return factors


def canonical_chart(prime: int, support: int) -> tuple[int, int]:
    if support <= 0:
        raise AssertionError("invalid chart support")
    modulus = 4 * support
    R = (-pow(prime, -1, modulus)) % modulus
    if not 1 <= R < modulus or R % 4 != 3:
        raise AssertionError("canonical chart representative changed")
    K = (prime * R + 1) // 4
    if K % support:
        raise AssertionError("chart support does not divide K")
    return R, K


def fixture_rows(payload: dict[str, Any]) -> list[dict[str, Any]]:
    overflow = payload["overflow_dual"]
    rows: list[dict[str, Any]] = []

    def add(name: str, prime: int, A: int, row: dict[str, Any]) -> None:
        data = dict(row["overflow"] if "overflow" in row else row)
        data.update({"name": name, "prime": prime, "A": A})
        rows.append(data)

    add("accumulated_d_one_boundary", 73, 7, overflow["accumulated_d_one_boundary"])
    add("accumulated_positive_fixed_n_edge", 409, 5, overflow["accumulated_positive_fixed_n_edge"])
    add("empty_fixed_n_window", 241, 38, overflow["empty_fixed_n_window"])

    for index, row in enumerate(overflow["reachable_accumulated_full_menu_conflict"]["bundle_receipts"]):
        add(f"reachable_conflict_bundle_{index}", 73, 19, row)

    for index, row in enumerate(overflow["root_edges"]):
        add(f"root_edge_{index}", int(row["prime"]), 1, row)

    for index, row in enumerate(overflow["lcm_dual_cycle"]["steps"]):
        add(f"lcm_cycle_step_{index}", 73, 66, row)

    add("symmetric_small_chart_support_conflict", 241, 8, overflow["symmetric_small_chart_support_conflict"])
    if len(rows) != EXPECTED_CASE_COUNT:
        raise AssertionError(f"fixture case count changed: {len(rows)}")
    return rows


def audit_channel(
    prime: int,
    A: int,
    M: int,
    n: int,
    d: int,
    side: str,
) -> dict[str, Any]:
    r = M % prime
    k = (M - r) // prime
    if not 1 <= r < prime or k < 0:
        raise AssertionError("M mod p decomposition changed")
    if prime * n != 4 * M * d + 1:
        raise AssertionError("overflow determinant identity changed")
    if side == "d":
        carrier = d
        chart_R, chart_K = canonical_chart(prime, d)
        support_modulus = A // gcd(A, d)
        quotient_residue = k + 1
    elif side == "r":
        carrier = r
        chart_R, chart_K = canonical_chart(prime, r)
        support_modulus = A // gcd(A, r)
        quotient_residue = d * n - 1
    else:
        raise AssertionError("unknown dual side")

    support_gain = carrier // gcd(A, carrier)
    obstruction = support_modulus // gcd(support_modulus, quotient_residue)
    joined_support = lcm(A, carrier)
    direct_support_divisibility = chart_K % joined_support == 0
    small_chart = chart_R < prime
    strict_gain = support_gain > 1
    criterion = small_chart and strict_gain and obstruction == 1
    direct_edge = small_chart and strict_gain and direct_support_divisibility
    if criterion != direct_edge:
        raise AssertionError(f"support criterion mismatch for {prime}, M={M}, side={side}")

    return {
        "side": side,
        "carrier": carrier,
        "chart_R": chart_R,
        "chart_K": chart_K,
        "small_chart": small_chart,
        "support_modulus": support_modulus,
        "quotient_residue": quotient_residue,
        "support_gain_factor": support_gain,
        "joined_support": joined_support,
        "support_obstruction": obstruction,
        "support_obstruction_factorization": factorization(obstruction),
        "direct_support_divisibility": direct_support_divisibility,
        "support_preserving_edge": direct_edge,
    }


def audit_case(row: dict[str, Any]) -> dict[str, Any]:
    prime = int(row["prime"])
    A = int(row["A"])
    M = int(row["M"])
    n = int(row["n"])
    d = int(row["d"])
    R_M, K_M = canonical_chart(prime, M)
    if R_M != int(row["R_M"]) or K_M != int(row["K_M"]):
        raise AssertionError(f"stored overflow chart changed: {row['name']}")
    if K_M % M or K_M // M != int(row["C"]):
        raise AssertionError(f"stored overflow quotient changed: {row['name']}")
    r = M % prime
    s = (4 * r * d + 1) // prime
    if prime * s != 4 * r * d + 1 or n != s + 4 * ((M - r) // prime) * d:
        raise AssertionError("symmetric determinant coordinates changed")
    channels = [
        audit_channel(prime, A, M, n, d, "d"),
        audit_channel(prime, A, M, n, d, "r"),
    ]
    return {
        "name": row["name"],
        "prime": prime,
        "A": A,
        "M": M,
        "r": r,
        "k": (M - r) // prime,
        "n": n,
        "d": d,
        "s": s,
        "channels": channels,
    }


def build_payload(input_path: Path = INPUT) -> dict[str, Any]:
    if sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the focused overflow input changed")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    cases = [audit_case(row) for row in fixture_rows(payload)]
    channels = [channel for case in cases for channel in case["channels"]]
    support_edges = [channel for channel in channels if channel["support_preserving_edge"]]
    obstruction_channels = [channel for channel in channels if channel["support_obstruction"] > 1]
    return {
        "arithmetic": (
            "For pn=4Md+1 and M=kp+r, the d-dual preserves old support A "
            "exactly when A/gcd(A,d) divides k+1; the r-dual preserves it exactly when "
            "A/gcd(A,r) divides d*n-1. A dual is a verified support-preserving candidate "
            "only when its chart is below p and lcm(A,carrier)>A. The quotient failure is "
            "recorded as a factored q-adic support obstruction."
        ),
        "scope_note": (
            "Exact two-channel filter only. It does not assert that a support-preserving dual "
            "exists, nor that a nontrivial obstruction yields a Type I/II certificate or a "
            "recursive edge. Fixed-n divisors beyond the symmetric d/r channels remain a "
            "separate menu."
        ),
        "input": input_path.name,
        "input_sha256": sha256(input_path),
        "case_count": len(cases),
        "dual_channel_count": len(channels),
        "support_preserving_edge_count": len(support_edges),
        "support_obstruction_channel_count": len(obstruction_channels),
        "cases": cases,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    payload = build_payload(args.input)
    if args.verify:
        if payload["case_count"] != EXPECTED_CASE_COUNT:
            raise AssertionError("fixture count changed")
        if payload["dual_channel_count"] != 2 * EXPECTED_CASE_COUNT:
            raise AssertionError("dual channel count changed")
        if payload["support_preserving_edge_count"] != 3:
            raise AssertionError("focused support-preserving edge count changed")
        for case in payload["cases"]:
            for channel in case["channels"]:
                if channel["support_preserving_edge"] and not channel["direct_support_divisibility"]:
                    raise AssertionError("a filtered edge lost direct divisibility")
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                key: payload[key]
                for key in (
                    "case_count",
                    "dual_channel_count",
                    "support_preserving_edge_count",
                    "support_obstruction_channel_count",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
