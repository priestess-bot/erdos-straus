#!/usr/bin/env python3
"""Verify one CRT instance of the all-core dual-saturation s=0 no-go.

The verifier constructs a fresh p=73 depth-two receipt from the theorem's
congruences.  It performs no prime-range, denominator, selector-history, or
historical-result scan.
"""

from __future__ import annotations

import argparse
from math import gcd, lcm


P = 73
DEPTH = 2


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        exponent += 1
        value //= prime
    return exponent


def tree_nodes(prime: int, depth: int) -> list[list[int]]:
    levels = [[prime + 1]]
    for _ in range(depth):
        levels.append(
            [
                child
                for node in levels[-1]
                for child in (prime * node + 1, prime * node - prime + 1)
            ]
        )
    return levels


def crt_pair(a: int, modulus_a: int, b: int, modulus_b: int) -> tuple[int, int]:
    if gcd(modulus_a, modulus_b) != 1:
        raise AssertionError("CRT moduli are not coprime")
    multiplier = ((b - a) * pow(modulus_a, -1, modulus_b)) % modulus_b
    modulus = modulus_a * modulus_b
    return (a + modulus_a * multiplier) % modulus, modulus


def chart(prime: int, parameter: int) -> dict[str, int]:
    g = (prime + 1) // 2
    C = (prime * prime - 1) // 2
    T = prime * prime * parameter - g
    A = g * T
    K = C * T
    R = (
        2 * prime**3 * parameter
        - prime * prime
        - 2 * prime * parameter
        - prime
        + 1
    )
    return {"g": g, "C": C, "T": T, "A": A, "K": K, "R": R}


def root_coordinates(prime: int, parameter: int) -> tuple[int, int]:
    x = (
        2 * prime**3 * parameter
        - 2 * prime * prime * parameter
        - prime * prime
        - 2 * prime * parameter
        + 2 * parameter
        + 3
    )
    y = 2 * (prime * prime - 1) * parameter - prime - 2
    return x, y


def hensel_lifts(prime: int) -> list[int]:
    roots = [
        residue
        for residue in range(prime)
        if (4 * residue * residue + 10 * residue + 7) % prime == 0
    ]
    lifts: list[int] = []
    for root in roots:
        candidates = [
            root + prime * digit
            for digit in range(prime)
            if split_numerator(prime, root + prime * digit) % (prime * prime) == 0
        ]
        if len(candidates) != 1:
            raise AssertionError("a simple root lost its unique Hensel lift")
        lifts.extend(candidates)
    if len(roots) != 2 or len(lifts) != 2:
        raise AssertionError("the core quadratic no longer has two simple roots")
    return sorted(lifts)


def split_numerator(prime: int, parameter: int) -> int:
    x, y = root_coordinates(prime, parameter)
    W = prime * prime + 1
    N = prime * prime + prime + 1
    return x * y - W * N


def construct_parameter(prime: int, depth: int) -> tuple[int, int, list[list[int]]]:
    data = chart(prime, 1)
    C = data["C"]
    g = data["g"]
    W = prime * prime + 1
    N = prime * prime + prime + 1
    levels = tree_nodes(prime, depth)
    tree_modulus = (W * N) ** 2
    for node in (node for level in levels for node in level):
        tree_modulus = lcm(tree_modulus, node // gcd(node, C))
    if gcd(tree_modulus, prime) != 1:
        raise AssertionError("tree modulus acquired the determinant prime")

    parameter_mod_tree = (g * pow(prime * prime, -1, tree_modulus)) % tree_modulus
    hensel_root = hensel_lifts(prime)[0]
    base, period = crt_pair(
        parameter_mod_tree, tree_modulus, hensel_root, prime * prime
    )
    if base == 0:
        base += period

    for digit in range(prime):
        candidate = base + digit * period
        if valuation(split_numerator(prime, candidate), prime) == 2:
            return candidate, tree_modulus, levels
    raise AssertionError("every mod-p continuation unexpectedly lifted to p^3")


def verify_tree_receipt(
    prime: int, parameter: int, levels: list[list[int]], data: dict[str, int]
) -> None:
    R = data["R"]
    K = data["K"]
    for node in (node for level in levels for node in level):
        if node % prime != 1 or K % node:
            raise AssertionError("a requested tree capacity is absent")

    for level in levels[:-1]:
        for node in level:
            departure = R - node
            if valuation(departure, prime) != 1:
                raise AssertionError("tree departure is not exactly p-primary")
            selected = departure // prime
            other = R - selected
            if gcd(selected, other) != 1:
                raise AssertionError("tree raw edge acquired gcd reduction")
            plus = prime * node + 1
            minus = prime * node - prime + 1
            if not (
                gcd(selected, K) == plus
                and gcd(other, K) == minus
                and K % (plus * minus) == 0
                and selected > plus
                and other > minus
            ):
                raise AssertionError("a two-sided capacity macro changed")


def verify() -> None:
    p = P
    r, tree_modulus, levels = construct_parameter(p, DEPTH)
    data = chart(p, r)
    g, C, T, A, K, R = (data[key] for key in ("g", "C", "T", "A", "K", "R"))
    W = p * p + 1
    N = p * p + p + 1
    x, y = root_coordinates(p, r)
    Q_x = x // W
    Q_y = y // N
    multiplier = Q_x * Q_y

    q_value = 4 * r * r + 10 * r + 7
    congruence_rhs = -(q_value) + p * (4 * r * r + 2 * r - 4)
    if not (
        len(levels) == DEPTH + 1
        and [len(level) for level in levels] == [1, 2, 4]
        and p % 24 == 1
        and 4 * K == p * R + 1
        and T % tree_modulus == 0
        and T % ((W * N) ** 2) == 0
        and x + y == R
        and gcd(x, y) == 1
        and (R - (p + 1)) // p == y
        and valuation(R - (p + 1), p) == 1
        and gcd(x, K) == W
        and gcd(y, K) == N
        and x == Q_x * W
        and y == Q_y * N
        and gcd(Q_x * Q_y, K) == 1
        and gcd(Q_x, p) == gcd(Q_y, p) == 1
        and split_numerator(p, r) % (p * p) == 0
        and split_numerator(p, r) % (p * p) == congruence_rhs % (p * p)
        and valuation(multiplier - 1, p) == 2
        and multiplier == x * y // (W * N)
        and A == g * T
        and K == C * T
    ):
        raise AssertionError("dual-saturated s=0 root receipt changed")

    verify_tree_receipt(p, r, levels, data)
    print(
        "verified 1 fresh p=73 depth-2 CRT tree with dual root saturation, "
        "coprime complete-excess blocks, and exact v_73(L-1)=2"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
