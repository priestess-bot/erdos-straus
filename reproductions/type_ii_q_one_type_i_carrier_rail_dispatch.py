#!/usr/bin/env python3
"""Verify the q=1 carrier rail and its first Type I dispatch.

The verifier checks only exact integer identities for fixed q=1 G controls.
It does not construct a Type II-to-Type I root-entry, run a prime-range
search, or assert a global exit.
"""

from __future__ import annotations

import argparse
import json
from math import gcd, isqrt


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def factorization(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[value] = 1
    return factors


def q_one_g(value: int) -> bool:
    return all(prime % 3 == 1 for prime in factorization(value))


def carrier_chart(prime: int, carrier: int, z: int = 0) -> dict[str, int]:
    if not (is_prime(prime) and prime % 24 == 1 and z >= 0):
        raise AssertionError("invalid core-prime carrier chart input")
    X = (prime + 3) // 4
    if not (carrier > 0 and X % carrier == 0 and carrier % 2 == 1 and carrier % 3 == 1):
        raise AssertionError("carrier does not belong to the q=1 rail")
    R = (8 * carrier + 1) // 3 + 4 * carrier * z
    K = (prime * R + 1) // 4
    Y = X // carrier
    expected_overlap = carrier * gcd(Y, 2 + 3 * z)
    if not (
        R % 4 == 3
        and prime * R + 1 == 4 * K
        and 3 * R - 1 == 4 * carrier * (2 + 3 * z)
        and K == carrier * (Y * R - (2 + 3 * z))
        and gcd(X, K) == expected_overlap
    ):
        raise AssertionError("carrier rail identity changed")
    return {
        "p": prime,
        "X": X,
        "carrier": carrier,
        "z": z,
        "R": R,
        "K": K,
        "overlap": gcd(X, K),
    }


def full_carrier_dispatch(prime: int) -> dict[str, object]:
    if not (is_prime(prime) and prime % 24 == 1):
        raise AssertionError("invalid core-prime control")
    t = (prime - 1) // 24
    X = 6 * t + 1
    root = carrier_chart(prime, X)
    R, K = root["R"], root["K"]
    M = R - 1
    raw_source = (prime, R * (prime - 1) - prime, prime - 1)
    raw_anchor = (1, R - 1, 1)
    if not (
        root["R"] == 16 * t + 3
        and K == X * (16 * t + 1)
        and 3 <= R <= prime - 2
        and gcd(M, K) == 1
        and M == 16 * t + 2 < prime
        and raw_source[0] + raw_source[1] == R * raw_source[2]
        and gcd(raw_source[0], raw_source[1]) == 1
        and K % prime != 0
        and raw_source[0] // prime == raw_anchor[0]
        and (raw_source[1] + R) % prime == 0
        and (raw_source[1] + R) // prime == raw_anchor[1]
        and (raw_source[2] + 1) % prime == 0
        and (raw_source[2] + 1) // prime == raw_anchor[2]
    ):
        raise AssertionError("full-carrier low root changed")

    if t % 2:
        R_M = 20 * t + 3
        C = (15 * t + 1) // 2
        K_M = M * C
        if not (
            1 <= R_M < 4 * M
            and R_M < prime
            and prime * R_M + 1 == 4 * K_M
            and K_M == (8 * t + 1) * (15 * t + 1)
        ):
            raise AssertionError("odd-t marked absorb formula changed")
        return {
            "root": root,
            "universal_raw_source": {
                "U": raw_source[0],
                "V": raw_source[1],
                "m": raw_source[2],
                "p_edge_anchor": list(raw_anchor),
            },
            "full_external_bundle": M,
            "dispatch": {"kind": "marked_absorb", "R": R_M, "K": K_M, "support": M},
        }

    R_M = 52 * t + 7
    C = (39 * t + 2) // 2
    K_M = M * C
    n = 12 * t + 1
    d = 9 * t // 2
    R_d = 6 * t - 1
    K_d = d * (8 * t - 1)
    if not (
        1 <= R_M < 4 * M
        and R_M > prime
        and prime * R_M + 1 == 4 * K_M
        and prime * n == 4 * M * d + 1
        and n == 4 * M - R_M == (prime + 1) // 2
        and n < 4 * d < prime + n
        and 3 <= R_d <= prime - 2
        and R_d == 4 * d - n
        and prime * R_d + 1 == 4 * K_d
        and K_d % d == 0
    ):
        raise AssertionError("even-t overflow fixed-n dispatch changed")
    return {
        "root": root,
        "universal_raw_source": {
            "U": raw_source[0],
            "V": raw_source[1],
            "m": raw_source[2],
            "p_edge_anchor": list(raw_anchor),
        },
        "full_external_bundle": M,
        "overflow": {"R": R_M, "K": K_M, "n": n, "d": d},
        "dispatch": {"kind": "fixed_n_edge", "R": R_d, "K": K_d, "support": d},
    }


def verify() -> dict[str, object]:
    controls = {prime: full_carrier_dispatch(prime) for prime in (73, 241, 2521, 118801)}
    if not all(q_one_g(control["root"]["X"]) for control in controls.values()):
        raise AssertionError("fixed q=1 G control changed")
    if not (
        controls[73]["dispatch"] == {"kind": "marked_absorb", "R": 63, "K": 1150, "support": 50}
        and controls[241]["overflow"] == {"R": 527, "K": 31752, "n": 121, "d": 45}
        and controls[241]["dispatch"] == {"kind": "fixed_n_edge", "R": 59, "K": 3555, "support": 45}
        and controls[2521]["dispatch"]
        == {"kind": "marked_absorb", "R": 2103, "K": 1325416, "support": 1682}
        and controls[118801]["dispatch"]
        == {"kind": "fixed_n_edge", "R": 29699, "K": 882067725, "support": 22275}
    ):
        raise AssertionError("full-carrier dispatch controls changed")

    partial = carrier_chart(76129, 7)
    full_z = 2 * (2719 - 1) // 3
    merged = carrier_chart(76129, 7, full_z)
    if not (
        q_one_g(partial["X"])
        and partial == {"p": 76129, "X": 19033, "carrier": 7, "z": 0, "R": 19, "K": 361613, "overlap": 7}
        and merged["z"] == 1812
        and merged["R"] == 50755
        and merged["overlap"] == 19033
        and merged["R"] == full_carrier_dispatch(76129)["root"]["R"]
    ):
        raise AssertionError("partial-to-full carrier rail control changed")

    return {
        "status": "verified",
        "full_carrier_controls": controls,
        "partial_carrier_control": {"minimum": partial, "full_merge": merged},
        "scope": (
            "Exact carrier and first-dispatch arithmetic only; no Type II-to-Type I "
            "root-entry semantics, global scheduler, or universal selector claim."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    print(json.dumps(verify(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
