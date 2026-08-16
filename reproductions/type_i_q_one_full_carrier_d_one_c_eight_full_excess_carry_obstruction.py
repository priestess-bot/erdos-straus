#!/usr/bin/env python3
"""Verify the c=8 zero-k target's second full-excess carry obstruction.

This is an exact symbolic-family receipt with two fixed arithmetic controls.
It does not search primes, factor a target, or claim that every alternative
bundle or source route fails.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import type_ii_q_one_full_carrier_d_one_capacity_two_rigidity as capacity_two
import type_ii_q_one_full_carrier_d_one_zero_k_capacity_ray as zero_k
import type_ii_q_one_type_i_carrier_rail_dispatch as rail


@dataclass(frozen=True)
class C8Target:
    s: int
    prime: int
    x: int
    n: int
    A: int
    E: int
    M: int
    R: int
    K: int
    Q: int


def c_eight_target(s: int) -> C8Target:
    """Return the closed-form p-free target for the j=11, g=1 shape."""
    if s <= 0:
        raise ValueError("s must be positive")
    p = 48 * s + 1
    x = 24 * s + 1
    n = 132 * s + 1
    A = (p * n - 1) // 4
    E = (p - 1) * (66 * s + 1) - x
    M = A * E
    K = 8 * M
    R = (4 * K - 1) // p
    Q = (R - 1) // 2
    target = C8Target(s, p, x, n, A, E, M, R, K, Q)
    if not (
        p * R + 1 == 4 * K
        and n == 132 * s + 1
        and A == 9 * s * (176 * s + 5)
        and E == 3168 * s * s + 24 * s - 1
        and M == 9 * s * (176 * s + 5) * E
        and R == 3345408 * s**3 + 50688 * s * s - 1392 * s - 1
        and R % 4 == 3
        and Q == 1672704 * s**3 + 25344 * s * s - 696 * s - 1
        and 8 * Q - 75 == p * (278784 * s * s - 1584 * s - 83)
    ):
        raise AssertionError("c=8 target normal form changed")
    return target


def gcd_boundary(target: C8Target) -> None:
    """Replay the Bezout identities forcing the full-excess block Q=(R-1)/2."""
    s, x, E, M, R, K, Q = (
        target.s,
        target.x,
        target.E,
        target.M,
        target.R,
        target.K,
        target.Q,
    )
    L = 176 * s + 5
    g = math.gcd(x, 66 * s + 1)
    if not (
        g == 1
        and math.gcd(x, 7) == 1
        and math.gcd(s, x) == 1
        and math.gcd(9, x) == 1
        and 24 * L - 176 * x == -56
        and 2 * E - x * (264 * s - 9) == 7
        and math.gcd(M, x) == 1
        and math.gcd(M, R - 1) == math.gcd(M, 2)
        and R % 4 == 3
        and math.gcd(M, Q) == 1
        and Q % 2 == 1
        and K % 8 == 0
    ):
        raise AssertionError("c=8 full-excess gcd boundary changed")


def terminal_first_phase_sieve() -> tuple[int, ...]:
    """Map the gap-seven terminal miss to the three c=8 u phases."""
    if (8, 11, 1) not in zero_k.zero_k_shapes():
        raise AssertionError("c=8 zero-k shape changed")
    allowed: list[int] = []
    for u in range(7):
        s = 86 + 103 * u
        p = 48 * s + 1
        if p % 7 in {1, 2, 4}:
            allowed.append(u)
    result = tuple(allowed)
    if result != (1, 5, 6):
        raise AssertionError("gap-seven terminal-miss phase sieve changed")
    return result


def capacity_increase(target: C8Target) -> int:
    """Return the next full-excess canonical capacity and prove it exceeds eight."""
    p, Q = target.prime, target.Q
    if not rail.is_prime(p) or p < 4129 or math.gcd(p, Q) != 1:
        raise AssertionError("c=8 capacity comparison requires its core-prime control")
    c_next = (8 * pow(Q, -1, p)) % p
    if not (
        1 <= c_next < p
        and (75 * c_next - 64) % p == 0
        and all(0 < 75 * c - 64 < p for c in range(1, 9))
        and c_next > 8
    ):
        raise AssertionError("c=8 second full-excess capacity did not increase")
    return c_next


def actual_c_eight_control() -> dict[str, int]:
    """Replay the stored q-star=103 c=8 arithmetic macro control."""
    row = capacity_two.receiver_data("even", 6558)
    if not (
        row["prime"] == 157393
        and row["s"] == 3279
        and row["q_star"] == 103
        and row["j"] == 11
        and row["g"] == 1
        and row["c"] == 8
        and (6 * row["s"] - 1) % row["q_star"] == 0
    ):
        raise AssertionError("stored c=8 q-star=103 macro control changed")
    target = c_eight_target(int(row["s"]))
    gcd_boundary(target)
    c_next = capacity_increase(target)
    if not (
        target.prime == row["prime"]
        and target.M == row["M"]
        and target.R == row["target_R"]
        and target.K == row["target_K"]
        and target.Q == 58971931474577975
        and c_next == 4198
    ):
        raise AssertionError("stored c=8 full-excess carry control changed")
    return {"prime": target.prime, "next_capacity": c_next}


def parity_controls() -> None:
    """Check both possible gcd(M,R-1) parities without a prime-range search."""
    for s, expected_gcd in ((189, 1), (704, 2)):
        target = c_eight_target(s)
        if not (
            s % 103 == 86
            and math.gcd(target.x, 66 * s + 1) == 1
            and math.gcd(target.M, target.R - 1) == expected_gcd
            and math.gcd(target.M, target.Q) == 1
        ):
            raise AssertionError("c=8 parity control changed")


def verify() -> None:
    phases = terminal_first_phase_sieve()
    control = actual_c_eight_control()
    parity_controls()
    if not (phases == (1, 5, 6) and control == {"prime": 157393, "next_capacity": 4198}):
        raise AssertionError("c=8 full-excess carry receipt changed")
    print(
        "verified q=1 zero-k c=8 second full-excess carry obstruction: "
        "terminal-first residual u mod 7 is {1,5,6}, and c_next=4198"
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
