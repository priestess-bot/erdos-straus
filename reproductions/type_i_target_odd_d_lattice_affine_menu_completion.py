#!/usr/bin/env python3
"""Verify target-odd affine labels in a one-hop D-lattice menu."""

from __future__ import annotations

import argparse
import math


def route_labels(p: int, d: int, q: int, height: int) -> list[int]:
    # The controls use D=1, where both source and target lattices are singletons.
    assert d == 1
    if (p + 4) % (q**height):
        return []
    return [1]


def verify() -> None:
    # p=73, D=1: q=7 and q=11 share one physical target label.
    p = 73
    for q in (7, 11):
        labels = route_labels(p, 1, q, 1)
        assert labels == [1]
        beta = (-p * pow(4, -1, q)) % q
        assert beta == 1
        assert (p + 4 * labels[0]) % q == 0

    # p=67369, D=1: the q=7 target direction is outside this finite menu.
    p = 67369
    assert math.gcd(p, 7) == 1
    beta = (-p * pow(4, -1, 7)) % 7
    assert beta == 5
    assert route_labels(p, 1, 7, 1) == []
    assert (p + 4) % 7 != 0

    # No one-hop D-lattice route can be dyadic because every p+4*label is odd.
    assert all((p + 4 * label) % 2 == 1 for label in (1,))

    print("verified target-odd D-lattice affine menu completion")
    print(
        {
            "p73": {"D": 1, "q7_q11_labels": {"7": [1], "11": [1]}},
            "p67369": {
                "D": 1,
                "q": 7,
                "beta": beta,
                "branch": "D_LATTICE_TARGET_ODD_SOURCE_UNCLOSED",
            },
            "q2": "NO_D_LATTICE_ROUTE_BY_PARITY",
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
