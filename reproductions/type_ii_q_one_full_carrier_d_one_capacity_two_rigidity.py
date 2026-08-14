#!/usr/bin/env python3
"""Verify the rigid q=1 immediate d=1 entry into residual capacity two.

This focused verifier checks the exact odd-branch boundary and one fixed
even q=1 C=2 receipt. It does not run a prime-range search or terminal scan.
"""

from __future__ import annotations

import argparse
from math import gcd, lcm

import type_ii_q_one_full_carrier_second_anchor_fixed_n_macro as q_one_macro
import type_ii_q_one_full_carrier_second_anchor_overflow as second_anchor
import type_ii_q_one_type_i_carrier_rail_dispatch as rail


def receiver_data(branch: str, t: int) -> dict[str, int | str]:
    row = q_one_macro.odd_macro(t) if branch == "odd" else q_one_macro.even_macro(t)
    postmacro = q_one_macro.postmacro_full_product(row)
    if postmacro["status"] != "strict_full_product_fold":
        raise AssertionError("control did not reach an immediate d=1 receiver")

    prime = int(row["prime"])
    fold = row["fold"]
    delta, n = int(fold["delta"]), int(fold["n"])
    receiver = postmacro["successor"]
    A, R, K = (int(receiver[field]) for field in ("support", "R", "K"))
    excess = second_anchor.complete_excess(R - 1, K)
    Q = int(excess["Q"])
    M = lcm(A, Q)
    E = M // A
    target = second_anchor.canonical_chart(prime, M)
    c = int(target["K"]) // M
    alpha, v = (prime + 1) // 2, (n + 1) // 2
    g = gcd(alpha, v)
    result: dict[str, int | str] = {
        "branch": branch,
        "prime": prime,
        "t": t,
        "delta": delta,
        "n": n,
        "A": A,
        "R": R,
        "K": K,
        "Q": Q,
        "M": M,
        "E": E,
        "c": c,
        "alpha": alpha,
        "v": v,
        "g": g,
        "target_R": int(target["R"]),
        "target_K": int(target["K"]),
    }
    if branch == "odd":
        result["j"] = (14 * delta + 3) // prime
    else:
        q_star = int(row["selected_carrier"]["q_star"])
        result["s"] = t // 2
        result["q_star"] = q_star
        result["j"] = (3 * q_star * delta - 4) // prime
    return result


def odd_capacity_two_exclusion() -> dict[str, int]:
    """Check the one core-prime case left by the symbolic p <= 218 bound."""
    candidates = tuple(
        (t, 24 * t + 1) for t in range(3, 10, 2) if rail.is_prime(24 * t + 1)
    )
    if candidates != ((3, 73),):
        raise AssertionError("odd C=2 finite core-prime boundary changed")

    row = receiver_data("odd", 3)
    prime, j, g = (int(row[key]) for key in ("prime", "j", "g"))
    n, alpha, v, c = (int(row[key]) for key in ("n", "alpha", "v", "c"))
    obstruction = 7 * j + 27 - 21 * g
    if not (
        prime == 73
        and j == 1
        and n == 17
        and g == 1
        and c == 27
        and 3 * (7 * v) - 5 * j * alpha == j + 3
        and obstruction == 13
        and -218 <= obstruction <= 97
        and obstruction % 7 == 6
        and obstruction % prime != 0
        and (c * (7 * j + 27) - 42 * g) % prime == 0
    ):
        raise AssertionError("odd q=1 C=2 exclusion changed")
    return {"prime": prime, "j": j, "g": g, "obstruction": obstruction}


def even_capacity_two_phase() -> dict[str, int]:
    """Replay the rigid q*=19 C=2 entrance at p=769."""
    row = receiver_data("even", 32)
    p, s, q_star, j, g = (int(row[key]) for key in ("prime", "s", "q_star", "j", "g"))
    delta = int(row["delta"])
    n, A, R, K, M, E, c = (
        int(row[key]) for key in ("n", "A", "R", "K", "M", "E", "c")
    )
    target_R, target_K = (int(row[key]) for key in ("target_R", "target_K"))
    alpha, v = int(row["alpha"]), int(row["v"])
    A2 = (p - 1) * (2 * p - 1) // 8
    h, remainder = divmod(M - A2, p)

    if not (
        p == 769
        and s == 16
        and rail.is_prime(p)
        and p % 24 == 1
        and q_star == 19
        and (6 * s - 1) % q_star == 0
        and 3 * q_star * delta - 4 == j * p
        and q_star * delta == 4 * (32 * s + 1)
        and j == 8
        and g == 1
        and n == 2 * p - 1
        and 4 * n == j * p + 4 - j
        and 4 * v - j * alpha == 4 - j
        and A == (p * n - 1) // 4
        and R == p * (2 * p - 3)
        and R % p == 0
        and row["Q"] % p != 0
        and E == (2 * p * p - 3 * p - 1) // 2
        and E % p == (-pow(2, -1, p)) % p
        and c == 2
        and (c * (12 - j) - 8 * g) % p == 0
        and target_K == 2 * M
        and p * target_R + 1 == 4 * target_K
        and target_R > p
        and M > p * p > A2
        and remainder == 0
        and h > 0
        and p == 912 * ((s - 16) // 19) + 769
        and p % 19 == 9
        and A % 19 == 0
        and M % 19 == 0
        and A2 % 19 == 17
        and h % 19 == 15
        and target_R == 2 * p - 3 + 8 * h
        and target_R % 19 == 2
        and target_K % 19 == 0
    ):
        raise AssertionError("even q=1 C=2 phase receipt changed")
    return {"prime": p, "q_star": q_star, "j": j, "phase": h, "capacity": c}


def verify() -> None:
    odd = odd_capacity_two_exclusion()
    even = even_capacity_two_phase()
    if not (
        odd["prime"] == 73
        and even["prime"] == 769
        and even["q_star"] == 19
        and even["capacity"] == 2
        and even["phase"] % 19 == 15
    ):
        raise AssertionError("q=1 C=2 rigidity classification changed")
    print(
        "verified q=1 C=2 rigidity: odd branch excluded, and the even "
        "q*=19 high-phase receipt has capacity two"
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
