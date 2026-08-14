#!/usr/bin/env python3
"""Verify the second-anchor overflow obstruction after the q=1 full-carrier root.

The check reconstructs the two forced first children, extracts their complete
anchor excess blocks, and proves by the low-chart congruence window that the
next canonical rechart is necessarily high overflow.  It does not claim a
descent or terminal beyond that overflow boundary.
"""

from __future__ import annotations

import argparse
import json
from math import gcd, lcm

import type_ii_q_one_type_i_carrier_rail_dispatch as rail


def complete_excess(anchor: int, capacity: int) -> dict[str, object]:
    """Return the complete prime-power excess of anchor beyond capacity."""
    anchor_factors = rail.factorization(anchor)
    capacity_factors = rail.factorization(capacity)
    blocks: list[dict[str, int]] = []
    Q = 1
    for prime, exponent in anchor_factors.items():
        if exponent > capacity_factors.get(prime, 0):
            Q *= prime**exponent
            blocks.append({"prime": prime, "exponent": exponent})
    if anchor % Q:
        raise AssertionError("complete-excess product did not divide anchor")
    return {"Q": Q, "beta": anchor // Q, "blocks": blocks}


def canonical_chart(prime: int, support: int) -> dict[str, int]:
    """Rebuild the unique canonical chart carrying the supplied support."""
    modulus = 4 * support
    R = (-pow(prime, -1, modulus)) % modulus
    if R == 0:
        raise AssertionError("canonical chart unexpectedly had zero residue")
    K_numerator = prime * R + 1
    if K_numerator % 4:
        raise AssertionError("canonical chart did not produce integral K")
    K = K_numerator // 4
    if not (1 <= R < modulus and K % support == 0):
        raise AssertionError("canonical support chart reconstruction failed")
    return {"R": R, "K": K}


def low_candidates(prime: int, R: int, step: int) -> list[int]:
    """Enumerate the low representatives in the known support congruence class."""
    lower_shift = -((R - 3) // step)
    upper_shift = (prime - 2 - R) // step
    return [R + step * shift for shift in range(lower_shift, upper_shift + 1)]


def odd_branch(t: int) -> dict[str, object]:
    prime = 24 * t + 1
    if not (t >= 3 and t % 2 == 1 and rail.is_prime(prime) and rail.q_one_g(6 * t + 1)):
        raise AssertionError("invalid odd q=1 G control")
    dispatch = rail.full_carrier_dispatch(prime)["dispatch"]
    R, K, A = (int(dispatch[field]) for field in ("R", "K", "support"))
    if not (
        dispatch["kind"] == "marked_absorb"
        and (R, K, A) == (20 * t + 3, (8 * t + 1) * (15 * t + 1), 2 * (8 * t + 1))
    ):
        raise AssertionError("odd first child formula changed")
    anchor = R - 1
    excess = complete_excess(anchor, K)
    Q, beta = int(excess["Q"]), int(excess["beta"])
    M = lcm(A, Q)
    B_p = (prime - 1) ** 2 // 4
    candidates = low_candidates(prime, R, 4 * A)
    next_chart = canonical_chart(prime, M)
    if not (
        anchor == 2 * (10 * t + 1)
        and Q == 10 * t + 1
        and beta == 2
        and gcd(Q, A) == 1
        and M == 2 * (8 * t + 1) * (10 * t + 1)
        and M > B_p
        and candidates == [R]
        and K % M != 0
        and next_chart["R"] > prime
    ):
        raise AssertionError("odd second-anchor overflow obstruction failed")
    return {
        "branch": "odd",
        "t": t,
        "p": prime,
        "child": {"R": R, "K": K, "support": A},
        "anchor": anchor,
        "complete_excess": excess,
        "combined_support": M,
        "B_p": B_p,
        "low_candidates": candidates,
        "canonical_next_chart": next_chart,
        "conclusion": "forced_high_overflow",
    }


def even_branch(t: int) -> dict[str, object]:
    prime = 24 * t + 1
    if not (t >= 4 and t % 2 == 0 and rail.is_prime(prime) and rail.q_one_g(6 * t + 1)):
        raise AssertionError("invalid even q=1 G control")
    s = t // 2
    if s < 2:
        raise AssertionError("p=49 is not a core-prime branch")
    dispatch = rail.full_carrier_dispatch(prime)["dispatch"]
    R, K, A = (int(dispatch[field]) for field in ("R", "K", "support"))
    if not (
        dispatch["kind"] == "fixed_n_edge"
        and (R, K, A) == (12 * s - 1, 9 * s * (16 * s - 1), 9 * s)
    ):
        raise AssertionError("even first child formula changed")
    anchor = R - 1
    excess = complete_excess(anchor, K)
    Q = int(excess["Q"])
    M = lcm(A, Q)
    B_p = (prime - 1) ** 2 // 4
    odd_excess_primes = [
        int(block["prime"])
        for block in excess["blocks"]
        if (6 * s - 1) % int(block["prime"]) == 0
    ]
    candidates = low_candidates(prime, R, 4 * A)
    next_chart = canonical_chart(prime, M)
    if not odd_excess_primes:
        raise AssertionError("even branch lost its mandatory 6s-1 excess factor")
    q = min(odd_excess_primes)
    if not (
        anchor == 2 * (6 * s - 1)
        and gcd(6 * s - 1, 9 * s) == 1
        and (16 * (6 * s - 1) - 6 * (16 * s - 1)) == -10
        and Q > 1
        and M % q == 0
        and B_p % q != 0
        and candidates == [R, prime - 2]
        and K % M != 0
        and next_chart["R"] > prime
    ):
        raise AssertionError("even second-anchor overflow obstruction failed")
    return {
        "branch": "even",
        "t": t,
        "s": s,
        "p": prime,
        "child": {"R": R, "K": K, "support": A},
        "anchor": anchor,
        "complete_excess": excess,
        "mandatory_excess_prime": q,
        "combined_support": M,
        "B_p": B_p,
        "low_candidates": candidates,
        "canonical_next_chart": next_chart,
        "conclusion": "forced_high_overflow",
    }


def verify() -> dict[str, object]:
    odd = [odd_branch(t) for t in (3, 105)]
    even = [even_branch(t) for t in (8, 10, 32, 4950)]
    expected = {
        73: (31, 1550, 2463),
        2521: (1051, 1767782, 4799167),
        193: (23, 828, 2351),
        241: (58, 2610, 3119),
    }
    for row in [*odd, *even]:
        prime = int(row["p"])
        if prime not in expected:
            continue
        Q = int(row["complete_excess"]["Q"])
        M = int(row["combined_support"])
        R_next = int(row["canonical_next_chart"]["R"])
        if (Q, M, R_next) != expected[prime]:
            raise AssertionError(f"second-anchor control changed for p={prime}")
    if not all(row["conclusion"] == "forced_high_overflow" for row in [*odd, *even]):
        raise AssertionError("a q=1 full-carrier control re-entered the low chart region")
    return {
        "status": "verified",
        "odd_controls": odd,
        "even_controls": even,
        "scope": (
            "Second-anchor low-rechart obstruction only; no high-overflow terminal, "
            "solution lift, or global G/Type I exit is asserted."
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
