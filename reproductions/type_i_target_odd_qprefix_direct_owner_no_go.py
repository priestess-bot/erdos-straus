#!/usr/bin/env python3
"""Verify the odd-q target-odd direct owner obstruction."""

from __future__ import annotations

import argparse
import math


def verify() -> None:
    p = 73
    modulus = 27
    k = (p * modulus + 1) // 4
    assert k == 493
    assert pow(2, 9, modulus) == modulus - 1

    # The order-18 character has q=3 component gamma=2*log(-1) mod 3^2.
    q = 3
    exponent = 2
    target_log = 9
    gamma = (exponent * target_log) % (q**2)
    assert gamma == 0

    beta = (-p * pow(4, -1, q**2)) % (q**2)
    assert beta == 2
    assert gamma != beta
    assert math.gcd(beta, q) == 1

    # q=2 is deliberately excluded: 4 has no inverse in a 2-primary modulus.
    assert math.gcd(4, 2) != 1

    print("verified target-odd odd-q direct owner no-go")
    print(
        {
            "p": p,
            "R": modulus,
            "K": k,
            "q": q,
            "e": 2,
            "gamma": gamma,
            "beta": beta,
            "branch": "TARGET_ODD_QPREFIX_DIRECT_OWNER_CONFLICT",
            "q2_route": "DYADIC_GATE_REQUIRED",
        }
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
