#!/usr/bin/env python3
"""Verify the unbounded same-chart rank and the sharp persistence boundary."""

from __future__ import annotations

import argparse
import json
from collections import deque
from math import gcd, lcm, prod


def factorization(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor:
            divisor = 3 if divisor == 2 else divisor + 2
            continue
        exponent = 0
        while value % divisor == 0:
            value //= divisor
            exponent += 1
        factors[divisor] = exponent
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[value] = 1
    return factors


def rank(prime: int, K: int, support: int) -> tuple[int, int]:
    bound = (prime - 1) ** 2 // 4
    if K % support:
        raise AssertionError("charged support did not divide K")
    return bound // support, K // support


def canonical_chart(prime: int, support: int) -> tuple[int, int, int]:
    cofactor = pow(4 * support, -1, prime)
    K = support * cofactor
    R = (4 * K - 1) // prime
    if not (
        4 * K == prime * R + 1
        and K % support == 0
        and 1 <= cofactor < prime
        and R % 4 == 3
    ):
        raise AssertionError("canonical chart failed")
    return R, K, cofactor


def formal_transition(
    source: tuple[int, int, int], q: int, modulus: int, K_factors: dict[int, int]
) -> tuple[int, int, int]:
    left, right, layer = source
    selected = [value for value in (left, right) if value % q == 0]
    if len(selected) != 1:
        raise AssertionError("edge label did not select one primitive side")
    value = selected[0]
    other = right if value == left else left
    if factorization(value).get(q, 0) <= K_factors.get(q, 0):
        raise AssertionError("edge label did not exceed K capacity")
    shift = (-layer) % q
    if not 1 <= shift < q or gcd(q, modulus * layer * other) != 1:
        raise AssertionError("formal shift was not a unit")
    value_0 = value // q
    other_0 = (other + modulus * shift) // q
    layer_0 = (layer + shift) // q
    common = gcd(value_0, other_0)
    if layer_0 % common:
        raise AssertionError("gcd reduction did not divide the layer")
    destination = (
        min(value_0 // common, other_0 // common),
        max(value_0 // common, other_0 // common),
        layer_0 // common,
    )
    if sum(destination[:2]) != modulus * destination[2]:
        raise AssertionError("formal target-pair invariant failed")
    return destination


def classify_centered(prime: int, R: int, K: int) -> dict[str, object]:
    factors = factorization(K)
    primes = sorted(factors)
    residues = {1}
    for q in primes:
        values = {pow(q, exponent, R) for exponent in range(-factors[q], factors[q] + 1)}
        residues = {left * right % R for left in residues for right in values}

    subgroup = {1}
    frontier = deque([1])
    while frontier:
        value = frontier.popleft()
        for q in primes:
            successor = value * q % R
            if successor not in subgroup:
                subgroup.add(successor)
                frontier.append(successor)
    target = R - 1
    classification = "hit" if target in residues else "F" if target in subgroup else "G"
    return {
        "classification": classification,
        "bounded_residue_count": len(residues),
        "subgroup_size": len(subgroup),
        "factorization": factors,
    }


def verify_persistent_promotions() -> list[dict[str, object]]:
    cases = (
        {"name": "bounded", "p": 73, "A": 19, "M": 38, "d": 12, "n": 25},
        {"name": "above_B_p", "p": 73, "A": 66, "M": 1518, "d": 28, "n": 2329},
    )
    rows = []
    for case in cases:
        p = int(case["p"])
        A = int(case["A"])
        M = int(case["M"])
        d = int(case["d"])
        n = int(case["n"])
        R = 4 * M - n
        K = M * (p - d)
        if not (
            p * n == 4 * M * d + 1
            and 4 * K == p * R + 1
            and M % A == 0
            and M // A >= 2
            and R > p
        ):
            raise AssertionError("persistent promotion fixture failed")
        source_rank = rank(p, K, A)
        target_rank = rank(p, K, M)
        if not target_rank < source_rank:
            raise AssertionError("unbounded same-chart rank did not decrease")
        rows.append(
            {
                "name": case["name"],
                "source": [R, K, A],
                "target": [R, K, M],
                "source_rank": source_rank,
                "target_rank": target_rank,
            }
        )
    if rows[1]["source"] != [3743, 68310, 66] or rows[1]["target_rank"] != (0, 45):
        raise AssertionError("high-carrier persistent control changed")
    return rows


def verify_low_support_bundle() -> dict[str, object]:
    p, R, A, Q = 409, 251, 5, 250
    K = (p * R + 1) // 4
    M = lcm(A, Q)
    R_M, K_M, cofactor = canonical_chart(p, M)
    source_rank = rank(p, K, A)
    target_rank = rank(p, K_M, M)
    if not (
        K == 25665
        and M == 250
        and (R_M, K_M, cofactor) == (511, 52250, 209)
        and R_M > p
        and target_rank[0] < source_rank[0]
        and target_rank < source_rank
    ):
        raise AssertionError("low-support bundle overflow did not become a strict edge")
    return {
        "source": [R, K, A],
        "target": [R_M, K_M, M],
        "source_rank": source_rank,
        "target_rank": target_rank,
    }


def verify_high_support_persistence_boundary() -> dict[str, object]:
    p, R, K, A = 73, 3743, 68310, 1518
    factors = factorization(K)
    if factors != {2: 1, 3: 3, 5: 1, 11: 1, 23: 1}:
        raise AssertionError("high-support source factorization changed")
    centered = classify_centered(p, R, K)
    if centered["classification"] != "F":
        raise AssertionError("high-support source ceased to be F")

    primes = sorted(factors)
    exponents = (2, -1, -3, 0, -2)
    numerator = prod(q ** max(exponent, 0) for q, exponent in zip(primes, exponents))
    denominator = prod(q ** max(-exponent, 0) for q, exponent in zip(primes, exponents))
    if not (
        (numerator, denominator) == (4, 198375)
        and numerator * pow(denominator, -1, R) % R == R - 1
        and numerator + denominator == 53 * R
        and any(abs(exponent) > factors[q] for q, exponent in zip(primes, exponents))
    ):
        raise AssertionError("explicit F witness changed")

    path = (
        ((4, 198375, 53), 2, (2, 101059, 27)),
        ((2, 101059, 27), 7, (535, 14437, 4)),
        ((535, 14437, 4), 14437, (1, 3742, 1)),
    )
    current = path[0][0]
    for source, q, expected in path:
        if current != source:
            raise AssertionError("F path lost continuity")
        current = formal_transition(source, q, R, factors)
        if current != expected:
            raise AssertionError("F path transition changed")

    node_left, node_right, layer = current
    right_factors = factorization(node_right)
    Q = prod(q**e for q, e in right_factors.items() if e > factors.get(q, 0))
    beta = node_right // Q
    if not (
        (node_left, node_right, layer) == (1, 3742, 1)
        and right_factors == {2: 1, 1871: 1}
        and (Q, beta) == (1871, 2)
        and K % (node_left * beta) == 0
        and gcd(Q, node_left * beta) == 1
        and K % Q != 0
    ):
        raise AssertionError("complete-excess bundle changed")

    M = lcm(A, Q)
    R_M, K_M, cofactor = canonical_chart(p, M)
    parent_rank = rank(p, K, A)
    target_rank = rank(p, K_M, M)
    transient_rank = rank(p, K_M, A)
    if not (
        M == 2840178
        and (R_M, K_M, cofactor) == (7314431, 133488366, 47)
        and parent_rank == (0, 45)
        and target_rank == (0, 47)
        and transient_rank == (0, 87937)
        and not target_rank < parent_rank
        and target_rank < transient_rank
    ):
        raise AssertionError("persistence boundary ranks changed")
    return {
        "source_class": centered["classification"],
        "F_witness": {"exponents": exponents, "numerator": numerator, "denominator": denominator},
        "bottom_path_length": len(path),
        "bundle": {"Q": Q, "beta": beta, "M": M},
        "parent_rank": parent_rank,
        "transient_rank": transient_rank,
        "target_rank": target_rank,
        "parent_edge_strict": target_rank < parent_rank,
        "transient_comparison_strict": target_rank < transient_rank,
    }


def run() -> dict[str, object]:
    return {
        "persistent_promotions": verify_persistent_promotions(),
        "low_support_bundle_overflow": verify_low_support_bundle(),
        "high_support_persistence_boundary": verify_high_support_persistence_boundary(),
        "theorem_status": "verified",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = run()
    if args.verify:
        print("verified unbounded same-chart promotion and persistence boundary")
    else:
        print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
