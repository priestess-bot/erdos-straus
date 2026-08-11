#!/usr/bin/env python3
"""Verify the external-source bridge for internal 3p+4 Type I certificates."""

from __future__ import annotations

import argparse
import math


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def bridge_data(prime: int, gap: int) -> dict[str, int]:
    assert is_prime(prime) and prime % 24 == 1
    assert (3 * prime + 4) % gap == 0
    assert gap % 48 == (-prime) % 48

    c = (prime + gap) // 48
    q = (36 * c + 1) // gap
    assert 36 * c + 1 == q * gap
    assert q % 4 == 3
    assert (3 * prime + 4) // gap == 4 * q - 3
    assert ((prime - 1) % (q + 1) == 0) == ((84 * c) % (q + 1) == 0)

    x = 12 * c
    divisor = 16 * c
    assert x == (prime + gap) // 4
    assert divisor <= x * x and x * x % divisor == 0
    assert (prime * x + divisor) % gap == 0

    return {"C": c, "q": q, "x": x, "D": divisor}


def verify_positive_bridge(prime: int, gap: int) -> dict[str, int]:
    data = bridge_data(prime, gap)
    c, q = data["C"], data["q"]
    assert (prime - 1) % (q + 1) == 0
    k = (q + 1) // 4
    n = (q * prime + 1) // (q + 1)
    preserved = k * n
    e = 9 * c
    u = (preserved + e) // q
    v = preserved * u // e
    assert preserved == 3 * c * (4 * q - 3)
    assert e <= preserved and preserved * preserved % e == 0
    assert (preserved + e) % q == 0
    assert u == 12 * c == data["x"]
    assert u * u // e == data["D"]
    assert gap == (4 * e + 1) // q
    assert n < prime

    source = (preserved, u, v)
    target = (preserved * prime, u, v)
    assert 4 * math.prod(source) == n * (
        source[0] * source[1] + source[0] * source[2] + source[1] * source[2]
    )
    assert 4 * math.prod(target) == prime * (
        target[0] * target[1] + target[0] * target[2] + target[1] * target[2]
    )

    direct = (
        data["x"],
        (prime * data["x"] + data["D"]) // gap,
        prime * (data["x"] + prime * data["x"] * data["x"] // data["D"]) // gap,
    )
    assert direct == (u, v, preserved * prime)
    return {
        **data,
        "k": k,
        "n": n,
        "M": preserved,
        "e": e,
        "u": u,
        "v": v,
    }


def verify() -> None:
    assert verify_positive_bridge(1297, 95) == {
        "C": 29,
        "q": 11,
        "x": 348,
        "D": 464,
        "k": 3,
        "n": 1189,
        "M": 3567,
        "e": 261,
        "u": 348,
        "v": 4756,
    }
    assert verify_positive_bridge(2521, 23) == {
        "C": 53,
        "q": 83,
        "x": 636,
        "D": 848,
        "k": 21,
        "n": 2491,
        "M": 52311,
        "e": 477,
        "u": 636,
        "v": 69748,
    }

    boundary = bridge_data(4729, 23)
    assert boundary == {"C": 99, "q": 155, "x": 1188, "D": 1584}
    assert (4729 - 1) % (boundary["q"] + 1) == 48
    assert (84 * boundary["C"]) % (boundary["q"] + 1) == 48


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    print("verified the 3p+4 internal-to-external marked descent bridge")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
