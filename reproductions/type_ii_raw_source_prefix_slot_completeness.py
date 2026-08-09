#!/usr/bin/env python3
"""Verify raw Type-II source-prefix K-slot completeness controls."""

from __future__ import annotations

import argparse
from math import gcd, isqrt


def bounds(prime: int, a: int, c: int) -> tuple[int, int, int]:
    a_max = (1 + isqrt(1 + 4 * prime)) // 4
    assert 1 <= a <= a_max
    c_max = (prime + 2 * a) // (4 * a * a)
    assert 1 <= c <= c_max
    k_max = (prime + 4 * a * a * c + 1) // (4 * a * c)
    return a_max, c_max, k_max


def prefix_slots(prime: int, prefix: int, a: int, c: int) -> tuple[int, ...]:
    _, _, k_max = bounds(prime, a, c)
    if gcd(prefix, 4 * a * c) != 1:
        return ()
    residue = pow(4 * a * c, -1, prefix) % prefix
    if residue == 0:
        residue = prefix
    return tuple(range(residue, k_max + 1, prefix))


def raw_candidates(prime: int, prefix: int) -> tuple[tuple[int, int, int, int, int, int], int]:
    a_max = (1 + isqrt(1 + 4 * prime)) // 4
    candidates: list[tuple[int, int, int, int, int, int]] = []
    pre_slots = 0
    for a in range(1, a_max + 1):
        c_max = (prime + 2 * a) // (4 * a * a)
        for c in range(1, c_max + 1):
            slots = prefix_slots(prime, prefix, a, c)
            pre_slots += len(slots)
            for k in slots:
                h = 4 * a * c * k - 1
                numerator = k * prime + a
                if numerator % h:
                    continue
                b = numerator // h
                if b < a:
                    continue
                m_numerator = a + b
                assert m_numerator % k == 0
                m = m_numerator // k
                assert prefix and h % prefix == 0
                assert prime == 4 * a * b * c - m
                candidates.append((a, c, k, h, b, m))
    return tuple(candidates), pre_slots


def verify() -> None:
    controls = (
        (73, 7, 1),
        (73, 15, 1),
        (313, 47, 2),
        (97, 143, 0),
        (878_089, 19_919, 1),
    )
    for prime, prefix, expected_count in controls:
        candidates, pre_slots = raw_candidates(prime, prefix)
        assert len(candidates) == expected_count
        if expected_count:
            assert pre_slots >= expected_count
        else:
            assert pre_slots > 0
    p73_u7, _ = raw_candidates(73, 7)
    assert p73_u7[0] == (1, 1, 2, 7, 21, 11)
    p73_u15, _ = raw_candidates(73, 15)
    assert p73_u15[0] == (2, 2, 1, 15, 5, 7)
    p313_u47, _ = raw_candidates(313, 47)
    assert set(p313_u47) == {
        (1, 4, 3, 47, 20, 7),
        (2, 1, 6, 47, 40, 7),
    }
    p878089, _ = raw_candidates(878_089, 19_919)
    assert p878089[0] == (83, 5, 12, 19_919, 529, 51)

    # The p=97 pseudo-pooling prefix has pre-admission slots, but every E4 divisibility
    # test fails, so it is not an empty-box artifact.
    _, pre_slots = raw_candidates(97, 143)
    assert pre_slots == 6

    print("verified Type-II raw source-prefix slot completeness")
    print(
        {
            "p73_u7": "raw_hit",
            "p73_u15": "raw_hit",
            "p313_u47": "noncoprime_dedup",
            "p97_u143": "e4_empty",
            "p878089_u19919": "raw_hit",
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
