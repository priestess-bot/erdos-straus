#!/usr/bin/env python3
"""Replay finite prefixes of the universal infinite p-parent ancestry."""

from __future__ import annotations

import argparse
from math import gcd, isqrt


def is_prime(value: int) -> bool:
    """Use trial division only for the two fixed control primes."""
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor <= isqrt(value):
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def verify_node(*, p: int, R: int, K: int, node: tuple[int, int, int]) -> None:
    """Check the ordered primitive formal-node invariant."""
    A, B, m = node
    if not (
        min(node) > 0
        and A + B == R * m
        and gcd(A, B) == 1
        and p * R + 1 == 4 * K
        and R % p != 0
    ):
        raise AssertionError("raw node or chart invariant failed")


def p_parent(*, p: int, R: int, K: int, node: tuple[int, int, int]) -> tuple[int, int, int]:
    """Construct the oriented parent whose p-edge reduces exactly to node."""
    verify_node(p=p, R=R, K=K, node=node)
    A, B, m = node
    parent = (p * A * A, p * A * B - R, p * A * m - 1)
    verify_node(p=p, R=R, K=K, node=parent)
    return parent


def replay_p_edge(*, p: int, R: int, K: int, parent: tuple[int, int, int]) -> tuple[tuple[int, int, int], int]:
    """Replay the forced p-edge and return its normalized child and gcd factor."""
    verify_node(p=p, R=R, K=K, node=parent)
    A, B, m = parent
    if not (A % p == 0 and K % p != 0 and m % p == p - 1 and B % p == (-R) % p):
        raise AssertionError("parent no longer has the forced p, shift-one raw edge")
    raw_child = (A // p, (B + R) // p, (m + 1) // p)
    reduction = gcd(gcd(*raw_child[:2]), raw_child[2])
    child = tuple(value // reduction for value in raw_child)
    verify_node(p=p, R=R, K=K, node=child)
    return child, reduction


def verify_ancestry(*, p: int, R: int, K: int, start: tuple[int, int, int], depth: int) -> dict[str, object]:
    """Build and replay a finite prefix of the explicit infinite ancestry."""
    if not is_prime(p) or depth < 1:
        raise AssertionError("control must use a prime and positive ancestry depth")
    current = start
    rows = []
    for _ in range(depth):
        parent = p_parent(p=p, R=R, K=K, node=current)
        child, reduction = replay_p_edge(p=p, R=R, K=K, parent=parent)
        if child != current or reduction != current[0]:
            raise AssertionError("p-parent replay did not recover the exact ordered node")
        rows.append({"parent": parent, "child": child, "gcd_reduction": reduction})
        current = parent
    return {"p": p, "R": R, "K": K, "start": start, "depth": depth, "rows": rows}


def build_result() -> dict[str, object]:
    """Return two targeted controls without any coverage enumeration."""
    anchor = verify_ancestry(p=73, R=71, K=1296, start=(1, 70, 1), depth=4)
    c9 = verify_ancestry(p=193, R=511, K=24656, start=(736, 797, 3), depth=3)
    if not (
        anchor["rows"][0]["gcd_reduction"] == 1
        and c9["rows"][0]["gcd_reduction"] == 736
        and c9["rows"][1]["gcd_reduction"] == c9["rows"][0]["parent"][0]
    ):
        raise AssertionError("ancestry controls no longer retain their exact reductions")
    return {
        "certificate_type": "universal_infinite_p_parent_ancestry_v1",
        "scope": "Primitive formal raw nodes; no source provenance or recursive edge is claimed.",
        "anchor_control": anchor,
        "c9_dyadic_control": c9,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    build_result()
    if args.verify:
        print("verified universal infinite p-parent ancestry controls")


if __name__ == "__main__":
    main()
