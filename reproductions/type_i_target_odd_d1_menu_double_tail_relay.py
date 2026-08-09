#!/usr/bin/env python3
"""Verify the D=1 target-odd Type-II double-tail relay."""

from __future__ import annotations

import argparse


def relay(p: int, h: int) -> dict[str, int]:
    assert p % 24 == 1
    assert h > 1 and (p + 4) % h == 0 and h % 4 == 3
    assert (p - 1) % (h + 1) == 0
    x = (p + h) // 4
    y = (x + 1) // h
    z = x * (x + 1) // h
    n = (p + h) // (h + 1)
    assert (p + h) % 4 == 0
    assert (x + 1) % h == 0
    assert n < p
    assert 4 * x * y * z == n * (y * z + x * z + x * y)
    assert 4 * x * (p * y) * (p * z) == p * ((p * y) * (p * z) + x * (p * z) + x * (p * y))
    return {"x": x, "Y": y, "Z": z, "n": n}


def verify() -> None:
    p73 = relay(73, 7)
    assert p73 == {"x": 20, "Y": 3, "Z": 60, "n": 10}
    p241 = relay(241, 7)
    assert p241 == {"x": 62, "Y": 9, "Z": 558, "n": 31}

    # Direct terminal exists for h=35, but the double-tail divisibility gate fails.
    assert (241 + 4) % 35 == 0
    assert 35 % 4 == 3
    assert (241 - 1) % 36 != 0

    print("verified target-odd D=1 double-tail relay")
    print(
        {
            "p73_h7": p73,
            "p241_h7": p241,
            "p241_h35": "DIRECT_ONLY_H_PLUS_ONE_DIVISIBILITY_FAIL",
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
