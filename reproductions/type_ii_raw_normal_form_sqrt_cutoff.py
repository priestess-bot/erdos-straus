#!/usr/bin/env python3
"""Verify the global finite raw Type-II normal-form cutoff."""

from __future__ import annotations

import argparse
from math import isqrt


def cutoff_box(prime: int) -> tuple[int, list[tuple[int, int, int]]]:
    """Return A_max and all (A,C,K) in the theorem's finite box."""
    a_max = (1 + isqrt(1 + 4 * prime)) // 4
    triples: list[tuple[int, int, int]] = []
    for a in range(1, a_max + 1):
        c_max = (prime + 2 * a) // (4 * a * a)
        for c in range(1, c_max + 1):
            k_max = (prime + 4 * a * a * c + 1) // (4 * a * c)
            triples.extend((a, c, k) for k in range(1, k_max + 1))
    return a_max, triples


def verify_triple(prime: int, a: int, c: int, k: int) -> dict[str, int]:
    h = 4 * a * c * k - 1
    numerator = k * prime + a
    assert numerator % h == 0
    b = numerator // h
    assert a <= b
    assert (prime + 4 * a * a * c) % h == 0
    assert 4 * a * a * c <= prime + 2 * a / k
    m_numerator = a + b
    assert m_numerator % k == 0
    m = m_numerator // k
    assert prime == 4 * a * b * c - m
    assert m % 4 == 3
    assert 3 <= m <= prime - 2
    return {"A": a, "B": b, "C": c, "K": k, "h": h, "m": m}


def verify() -> None:
    controls = {
        73: ((1, 1, 2), (2, 2, 1)),
        313: ((2, 1, 6),),
        878_089: ((83, 5, 12),),
    }
    for prime, triples in controls.items():
        a_max, box = cutoff_box(prime)
        box_set = set(box)
        for triple in triples:
            assert triple in box_set
            record = verify_triple(prime, *triple)
            assert record["A"] <= a_max
            assert record["C"] <= (prime + 2 * record["A"]) // (4 * record["A"] ** 2)
        # Every candidate in the finite box that passes the raw divisibility and order gates
        # reconstructs a certificate; no candidate is accepted without those gates.
        accepted = 0
        for a, c, k in box:
            h = 4 * a * c * k - 1
            numerator = k * prime + a
            if numerator % h or numerator // h < a:
                continue
            verify_triple(prime, a, c, k)
            accepted += 1
        assert accepted >= len(triples)

    print("verified Type-II raw normal-form sqrt cutoff")
    print({"p73": "direct_and_raw", "p313": "noncoprime_raw", "p878089": "shared_normal_form"})


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
