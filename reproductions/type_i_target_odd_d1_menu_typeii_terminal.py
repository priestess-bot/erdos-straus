#!/usr/bin/env python3
"""Verify the D=1 target-odd shared-q Type-II terminal family."""

from __future__ import annotations

import argparse
import math


def divisors(n: int) -> list[int]:
    result: list[int] = []
    for d in range(1, math.isqrt(n) + 1):
        if n % d == 0:
            result.append(d)
            if d * d != n:
                result.append(n // d)
    return sorted(result)


def terminal(p: int, h: int) -> tuple[int, int, int]:
    assert p % 24 == 1
    assert h > 1 and (p + 4) % h == 0 and h % 4 == 3
    assert (p + h) % 4 == 0
    x = (p + h) // 4
    y = p * (x + 1) // h
    z = p * x * (x + 1) // h
    assert (p * (x + 1)) % h == 0
    assert (p * x * (x + 1)) % h == 0
    assert 4 * x * y * z == p * (y * z + x * z + x * y)
    return x, y, z


def verify() -> None:
    p73 = terminal(73, 7)
    assert p73 == (20, 219, 4380)
    p241 = terminal(241, 7)
    assert p241 == (62, 2169, 134478)

    p193 = 193
    candidates = [h for h in divisors(p193 + 4) if h > 1 and h % 4 == 3]
    assert candidates == []

    print("verified target-odd D=1 shared-q Type-II terminal")
    print(
        {
            "p73": {"h": 7, "certificate": p73},
            "p241": {"h": 7, "certificate": p241},
            "p193": {"branch": "D1_TYPE_II_FAN_EMPTY"},
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
