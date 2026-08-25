#!/usr/bin/env python3
"""Replay the C=1 R=3 direct-terminal versus G split.

The terminal branch verifies a direct Type I certificate for the original
prime. The G branch is a target-local classification boundary, not a global
nonexistence result.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECEIPT_PATH = (
    ROOT / "data" / "t6-wave1" / "f2-high-support-c1-r-three-terminal-split-v1.json"
)


def factorization(value: int) -> tuple[int, ...]:
    """Return prime factors with multiplicity for focused exact controls."""
    if value < 1:
        raise ValueError("factorization input must be positive")
    factors: list[int] = []
    while value % 2 == 0 and value > 1:
        factors.append(2)
        value //= 2
    divisor = 3
    while divisor <= isqrt(value):
        while value % divisor == 0:
            factors.append(divisor)
            value //= divisor
        divisor += 2
    if value > 1:
        factors.append(value)
    return tuple(factors)


def terminal_certificate(prime: int, q: int) -> dict[str, int]:
    """Construct the three-p-plus-one Type I certificate from declared q."""
    if prime % 24 != 1:
        raise AssertionError("prime is outside the core domain")
    N = (3 * prime + 1) // 4
    if N % q or q % 3 != 2:
        raise AssertionError("declared terminal factor is invalid")
    if q * q > N:
        raise AssertionError("two-mod-three factor should be at most sqrt(N)")
    quotient = N // q
    if (quotient + 1) % 3 or (4 * q + 1) % 3:
        raise AssertionError("three-p-plus-one congruence changed")
    r = (quotient + 1) // 3
    gap = (4 * q + 1) // 3
    x = q * r
    divisor = q * r * r
    if not (
        gap % 4 == 3
        and 3 <= gap <= prime - 2
        and 4 * x == prime + gap
        and x * x % divisor == 0
        and (prime * x + divisor) % gap == 0
    ):
        raise AssertionError("Type I normal form changed")
    y = (prime * x + divisor) // gap
    z_numerator = prime * (x + prime * x * x // divisor)
    if z_numerator % gap:
        raise AssertionError("terminal denominator is not integral")
    z = z_numerator // gap
    if Fraction(4, prime) != sum((Fraction(1, item) for item in (x, y, z)), Fraction()):
        raise AssertionError("direct Type I terminal did not verify")
    return {
        "p": prime,
        "N": N,
        "q": q,
        "r": r,
        "gap": gap,
        "x": x,
        "divisor": divisor,
        "y": y,
        "z": z,
    }


def r3_g_residual(prime: int) -> dict[str, int | str]:
    """Verify that every prime factor of N is 1 modulo 3."""
    if prime % 24 != 1:
        raise AssertionError("prime is outside the core domain")
    N = (3 * prime + 1) // 4
    factors = factorization(N)
    if not factors or any(factor % 3 != 1 for factor in factors):
        raise AssertionError("R=3 G residual factor condition changed")
    return {"p": prime, "N": N, "classification": "R3_G_RESIDUAL"}


def p_plus_four_q3(prime: int) -> list[int]:
    return sorted({factor for factor in factorization(prime + 4) if factor % 4 == 3})


def build_receipt() -> dict[str, object]:
    terminal_rows = [terminal_certificate(73, 5), terminal_certificate(313, 5)]
    residual_rows = [r3_g_residual(97), r3_g_residual(241)]
    controls = [
        {
            "p": row["p"],
            "N": row["N"],
            "q": row["q"],
            "r": row["r"],
            "gap": row["gap"],
            "certificate": [row["x"], row["y"], row["z"]],
            "p_plus_four_q3": p_plus_four_q3(row["p"]),
        }
        for row in terminal_rows
    ]
    controls.extend(
        {**row, "p_plus_four_q3": p_plus_four_q3(int(row["p"]))}
        for row in residual_rows
    )
    controls[-1]["boundary"] = "p has an independent gap-7 Type II terminal"
    if controls != [
        {"p": 73, "N": 55, "q": 5, "r": 4, "gap": 7, "certificate": [20, 220, 4015], "p_plus_four_q3": [7, 11]},
        {"p": 313, "N": 235, "q": 5, "r": 16, "gap": 7, "certificate": [80, 3760, 73555], "p_plus_four_q3": []},
        {"p": 97, "N": 73, "classification": "R3_G_RESIDUAL", "p_plus_four_q3": []},
        {
            "p": 241,
            "N": 181,
            "classification": "R3_G_RESIDUAL",
            "boundary": "p has an independent gap-7 Type II terminal",
            "p_plus_four_q3": [7],
        },
    ]:
        raise AssertionError("C1 R=3 terminal split controls changed")
    return {
        "artifact_id": "f2_high_support_c1_r_three_terminal_split_v1",
        "status": "C1_R3_TERMINAL_OR_G_RESIDUAL",
        "controls": controls,
        "conclusion": {
            "two_mod_three_factor_of_N": "DIRECT_TYPE_I_TERMINAL",
            "all_factors_one_mod_three": "R3_G_RESIDUAL_NOT_GLOBAL_NO_SOLUTION",
        },
    }


def verify() -> dict[str, object]:
    receipt = build_receipt()
    stored = json.loads(RECEIPT_PATH.read_text(encoding="utf-8"))
    if stored["artifact_id"] != receipt["artifact_id"]:
        raise AssertionError("stored artifact id changed")
    if stored["status"] != receipt["status"]:
        raise AssertionError("stored status changed")
    if stored["controls"] != receipt["controls"]:
        raise AssertionError("stored terminal/G controls changed")
    return receipt


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    receipt = verify() if args.verify else build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
