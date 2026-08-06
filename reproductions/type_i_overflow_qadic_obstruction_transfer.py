#!/usr/bin/env python3
"""Verify the prime-power payment ledger for overflow dual carriers.

For pn = 4 M d + 1 and M = k p + r, an old charged support A | M has two
determinant dual channels.  For q**a || A, the q-layers available in the d
channel are supplied by v_q(d) and v_q(k+1); the r channel uses
v_q(r) and v_q(d*n-1).  This script checks the exact capped valuation
identities and the directional unit consequences.  It is a local arithmetic
ledger, not a cross-state capacity or recursive-edge proof.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import gcd
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-universal-anchor-overflow-dual-results.json"
OUTPUT = ROOT / "reproductions" / "type-i-overflow-qadic-obstruction-transfer-results.json"
EXPECTED_INPUT_SHA256 = (
    "01755f31bdbb5747c340519b997a38f021575efe0ea1652bf38278b5bf832f21"
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


def valuation(value: int, prime: int) -> int:
    if value == 0:
        raise AssertionError("valuation is only used for nonzero labels")
    value = abs(value)
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def canonical_chart(prime: int, support: int) -> tuple[int, int]:
    modulus = 4 * support
    R = (-pow(prime, -1, modulus)) % modulus
    if not 1 <= R < modulus or R % 4 != 3:
        raise AssertionError("canonical chart representative changed")
    K = (prime * R + 1) // 4
    if K % support:
        raise AssertionError("canonical support does not divide K")
    return R, K


def fixture_rows(payload: dict[str, Any]) -> list[dict[str, Any]]:
    overflow = payload["overflow_dual"]
    rows: list[dict[str, Any]] = []

    def add(name: str, prime: int, A: int, row: dict[str, Any]) -> None:
        data = dict(row["overflow"] if "overflow" in row else row)
        data.update({"name": name, "prime": prime, "A": A})
        rows.append(data)

    add("accumulated_d_one_boundary", 73, 7, overflow["accumulated_d_one_boundary"])
    add(
        "accumulated_positive_fixed_n_edge",
        409,
        5,
        overflow["accumulated_positive_fixed_n_edge"],
    )
    add("empty_fixed_n_window", 241, 38, overflow["empty_fixed_n_window"])

    for index, row in enumerate(
        overflow["reachable_accumulated_full_menu_conflict"]["bundle_receipts"]
    ):
        add(f"reachable_conflict_bundle_{index}", 73, 19, row)

    for index, row in enumerate(overflow["root_edges"]):
        add(f"root_edge_{index}", int(row["prime"]), 1, row)

    for index, row in enumerate(overflow["lcm_dual_cycle"]["steps"]):
        add(f"lcm_cycle_step_{index}", 73, 66, row)

    add(
        "symmetric_small_chart_support_conflict",
        241,
        8,
        overflow["symmetric_small_chart_support_conflict"],
    )
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
    if not 1 <= r < prime:
        raise AssertionError("M mod p decomposition changed")
    if prime * n != 4 * M * d + 1:
        raise AssertionError("overflow determinant identity changed")

    if side == "d":
        carrier = d
        chart_R, chart_K = canonical_chart(prime, d)
        label = k + 1
        label_name = "k+1"
    elif side == "r":
        carrier = r
        chart_R, chart_K = canonical_chart(prime, r)
        label = d * n - 1
        label_name = "d*n-1"
    else:
        raise AssertionError("unknown dual side")

    joined_support = A * carrier // gcd(A, carrier)
    direct_support_divisibility = chart_K % joined_support == 0
    small_chart = chart_R < prime
    strict_gain = carrier // gcd(A, carrier) > 1
    q_rows: list[dict[str, Any]] = []

    for q, a in factorization(A).items():
        carrier_height = valuation(carrier, q)
        label_height = valuation(label, q)
        paid_height = min(a, carrier_height + label_height)
        deficit_height = a - paid_height

        if side == "d":
            complementary_value = prime - r
            expected_capped_label_height = min(a, valuation(k + 1, q))
        else:
            complementary_value = prime - d
            expected_capped_label_height = min(a, valuation(d * n - 1, q))
        capped_complementary_height = min(a, valuation(complementary_value, q))
        if expected_capped_label_height != capped_complementary_height:
            raise AssertionError("determinant residue valuation transfer failed")

        if side == "d" and carrier % q == 0:
            if (d * n - 1) % q == 0:
                raise AssertionError("q|d should force dn-1 to be a q-unit")
        if side == "r" and carrier % q == 0:
            if (k + 1) % q == 0:
                raise AssertionError("q|r should force k+1 to be a q-unit")

        q_rows.append(
            {
                "q": q,
                "support_exponent": a,
                "carrier_height": carrier_height,
                "residue_label": label,
                "residue_label_name": label_name,
                "residue_height": label_height,
                "paid_height_capped": paid_height,
                "obstruction_height": deficit_height,
                "carrier_pays_any": carrier_height > 0,
                "residue_pays_any": label_height > 0,
                "carrier_divisible": carrier % q == 0,
            }
        )

    direct_obstruction = A // gcd(A, carrier)
    direct_obstruction //= gcd(direct_obstruction, label)
    formula_obstruction = 1
    for row in q_rows:
        formula_obstruction *= row["q"] ** row["obstruction_height"]
    if direct_obstruction != formula_obstruction:
        raise AssertionError("prime-power obstruction product changed")

    criterion = small_chart and strict_gain and direct_obstruction == 1
    direct_edge = small_chart and strict_gain and direct_support_divisibility
    if criterion != direct_edge:
        raise AssertionError("local obstruction criterion disagrees with direct support test")

    return {
        "side": side,
        "carrier": carrier,
        "chart_R": chart_R,
        "chart_K": chart_K,
        "small_chart": small_chart,
        "strict_gain": strict_gain,
        "joined_support": joined_support,
        "direct_support_divisibility": direct_support_divisibility,
        "support_obstruction": direct_obstruction,
        "q_layers": q_rows,
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
    if K_M % A:
        raise AssertionError("old charged support does not divide the overflow K")
    channels = [
        audit_channel(prime, A, M, n, d, "d"),
        audit_channel(prime, A, M, n, d, "r"),
    ]
    return {
        "name": row["name"],
        "prime": prime,
        "A": A,
        "M": M,
        "n": n,
        "d": d,
        "r": M % prime,
        "k": (M - M % prime) // prime,
        "channels": channels,
    }


def build_payload(input_path: Path = INPUT) -> dict[str, Any]:
    if sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the focused overflow input changed")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    cases = [audit_case(row) for row in fixture_rows(payload)]
    channels = [channel for case in cases for channel in case["channels"]]
    q_rows = [row for channel in channels for row in channel["q_layers"]]
    return {
        "arithmetic": (
            "For q**a || A, the d-channel q payment is min(a, v_q(d)+v_q(k+1)) "
            "and the r-channel payment is min(a, v_q(r)+v_q(d*n-1)). The remaining "
            "support obstruction is the uncapped deficit. The determinant congruences "
            "transfer the residue heights exactly, and q|d forces dn-1 to be a q-unit "
            "while q|r forces k+1 to be a q-unit."
        ),
        "scope_note": (
            "Exact local prime-power ledger only. It does not identify a cross-state "
            "phase, prove bounded labels, produce a Type I/II certificate, or upgrade "
            "a support reset to an E1--E5 recursive edge."
        ),
        "input": input_path.name,
        "input_sha256": sha256(input_path),
        "case_count": len(cases),
        "dual_channel_count": len(channels),
        "q_layer_row_count": len(q_rows),
        "channels_with_obstruction": sum(
            channel["support_obstruction"] > 1 for channel in channels
        ),
        "obstruction_prime_power_rows": sum(
            row["obstruction_height"] > 0 for row in q_rows
        ),
        "carrier_payment_rows": sum(row["carrier_pays_any"] for row in q_rows),
        "residue_payment_rows": sum(row["residue_pays_any"] for row in q_rows),
        "cases": cases,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_payload(args.input)
    if args.verify:
        if result["case_count"] != EXPECTED_CASE_COUNT:
            raise AssertionError("fixture count changed")
        if result["dual_channel_count"] != 2 * EXPECTED_CASE_COUNT:
            raise AssertionError("dual channel count changed")
        for case in result["cases"]:
            for channel in case["channels"]:
                if channel["support_preserving_edge"] and channel["support_obstruction"] != 1:
                    raise AssertionError("a support edge retained a nontrivial obstruction")
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                key: result[key]
                for key in (
                    "case_count",
                    "dual_channel_count",
                    "q_layer_row_count",
                    "channels_with_obstruction",
                    "obstruction_prime_power_rows",
                    "carrier_payment_rows",
                    "residue_payment_rows",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
