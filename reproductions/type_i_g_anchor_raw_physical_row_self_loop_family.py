#!/usr/bin/env python3
"""Check the infinite G-anchor raw-edge family with an identical physical row."""

from __future__ import annotations

import argparse
import json
from math import gcd, isqrt


PROGRESSION_MODULUS = 936
PROGRESSION_RESIDUE = 601


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    divisor = 3
    while divisor <= isqrt(n):
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def jacobi_symbol(a: int, n: int) -> int:
    """Return the Jacobi symbol (a/n) for odd positive n."""
    if n <= 0 or n % 2 == 0:
        raise ValueError("Jacobi denominator must be positive and odd")

    a %= n
    sign = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                sign = -sign
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            sign = -sign
        a %= n
    return sign if n == 1 else 0


def raw_row(p: int, label: int) -> dict[str, int]:
    R = p - 2
    K = (p - 1) ** 2 // 4
    Q = (p - 3) // 2
    x = 2 * Q // label
    y = R - x
    c = gcd(y, K)
    M = K // c
    return {
        "label": label,
        "x": x,
        "y": y,
        "c": c,
        "M": M,
        "tail": y // c,
        "d": p - c,
        "n": 4 * M - R,
    }


def ac_decompositions(shift: int) -> tuple[tuple[int, int], ...]:
    """Return all positive pairs (a, c) with shift = a**2 * c."""
    return tuple(
        (a, shift // (a * a))
        for a in range(1, isqrt(shift) + 1)
        if shift % (a * a) == 0
    )


def is_ac_target_factor(factor: int, a: int, c: int) -> bool:
    modulus = 4 * a * c
    return factor % modulus == modulus - 1


def verify_prime(p: int) -> dict[str, object]:
    assert is_prime(p)
    assert p % PROGRESSION_MODULUS == PROGRESSION_RESIDUE
    assert p % 24 == 1

    h = (p - 1) // 24
    R = p - 2
    K = (p - 1) ** 2 // 4
    Q = (p - 3) // 2
    e = Q // 13

    assert h % 3 == 1
    assert Q % 13 == 0
    assert e * 13 == Q
    assert jacobi_symbol(Q, R) == -1
    assert jacobi_symbol(13, R) == 1
    assert jacobi_symbol(e, R) == -1

    source = raw_row(p, e)
    target = raw_row(p, Q)
    assert source["x"] == 26
    assert target["x"] == 2
    assert source["y"] == p - 28
    assert target["y"] == p - 4
    assert source["c"] == target["c"] == 3
    assert source["M"] == target["M"] == K // 3
    assert source["d"] == target["d"] == p - 3
    assert source["n"] == target["n"] == 4 * K // 3 - R
    assert target["tail"] - source["tail"] == 8
    assert source["label"] != target["label"]
    assert p * source["n"] == 4 * source["M"] * source["d"] + 1

    shift = source["tail"] - 7
    decompositions = ac_decompositions(shift)
    assert shift == (p - 49) // 3
    assert p + 4 * shift == 7 * source["tail"]
    assert shift > 64
    assert all(
        not is_ac_target_factor(source["tail"], a, c)
        for a, c in decompositions
    )

    full_tail_block_excluded = shift > 2500
    if full_tail_block_excluded:
        assert all(
            not is_ac_target_factor(7 * source["tail"], a, c)
            for a, c in decompositions
        )

    return {
        "prime": p,
        "raw_edge": {"from": e, "prime_factor": 13, "to": Q},
        "shared_physical_row": {
            key: source[key] for key in ("M", "c", "d", "n")
        },
        "distinct_tails": {"from": source["tail"], "to": target["tail"]},
        "tail_ac_boundary": {
            "shift": shift,
            "p_plus_4_shift": p + 4 * shift,
            "bare_tail_excluded": True,
            "full_tail_block_excluded": full_tail_block_excluded,
        },
    }


def verify() -> dict[str, object]:
    assert gcd(PROGRESSION_RESIDUE, PROGRESSION_MODULUS) == 1
    examples = tuple(verify_prime(p) for p in (601, 5281, 8089))
    return {
        "family": "p == 601 (mod 936), p prime",
        "dirichlet_progression_is_primitive": True,
        "examples": examples,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    print(json.dumps(verify(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
